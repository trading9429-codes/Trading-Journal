#!/usr/bin/env python3
"""
FYERS Trades Ingestion & Matching Engine
Trader Execution Reset System • Intraday Equities (NSE)

Features:
- Robust multi-format parsing: Official FYERS Tradebook CSV, Orderbook CSV, XLSX, TSV, JSON
- Flexible header detection bypassing broker metadata rows
- Multi-slice order aggregation (combines exchange partial fills sharing Exchange Order ID)
- FIFO chronological fill matching for Buy & Sell legs by trading day and symbol
- Exact FYERS Statutory Friction Computation (STT, GST, Exchange, SEBI, Stamp)
- Strict Rule Baseline Integration:
    * Planned SL: exactly 0.8% of entry price
    * Planned Target: exactly 2.0% of entry price
    * Planned Risk:Reward: 2.50R (2.0% / 0.8%)
    * Default Setup Name: "Default Setup" (fully customizable/alterable)
- NSE Ticker Normalization (maps company names like "IIFL FINANCE LIMITED" -> "IIFL")
"""

import io
import re
import csv
import json
import zipfile
import xml.etree.ElementTree as ET
from datetime import datetime
from excel_service import calculate_fyers_charges, get_weekday_from_date

DEFAULT_SETUP_NAME = "Default Setup"
PLANNED_SL_PCT = 0.008   # 0.8% planned stop loss
PLANNED_TGT_PCT = 0.020  # 2.0% planned target
PLANNED_RR = 2.50        # 2.0 / 0.8 = 2.50R

# Mapping of common Indian equity company names in FYERS reports to their NSE tickers
NSE_COMPANY_TO_TICKER = {
    "IIFL FINANCE LIMITED": "IIFL",
    "IIFL FINANCE LTD": "IIFL",
    "V2 RETAIL LIMITED": "V2RETAIL",
    "V2 RETAIL LTD": "V2RETAIL",
    "PARAGMILK": "PARAGMILK",
    "PARAG MILK FOODS LIMITED": "PARAGMILK",
    "PARAG MILK FOODS LTD": "PARAGMILK",
    "PWL": "PWL",
    "ALKYL AMINES CHEM. LTD": "ALKYLAMINE",
    "ALKYL AMINES CHEMICALS LIMITED": "ALKYLAMINE",
    "ALKYL AMINES CHEMICALS LTD": "ALKYLAMINE",
    "WELSPUN LIVING LIMITED": "WELSPUNLIV",
    "WELSPUN LIVING LTD": "WELSPUNLIV",
    "TRIVENI ENGG. & INDS. LTD": "TRIVENI",
    "TRIVENI ENGINEERING & INDUSTRIES LIMITED": "TRIVENI",
    "TRIVENI ENGINEERING & INDUSTRIES LTD": "TRIVENI",
    "INDO COUNT INDUSTRIES LTD": "ICIL",
    "INDO COUNT INDUSTRIES LIMITED": "ICIL",
    "AWFIS SPACE SOLUTIONS LTD": "AWFIS",
    "AWFIS SPACE SOLUTIONS LIMITED": "AWFIS",
    "FRACTAL ANALYTICS LIMITED": "FRACTAL",
    "FRACTAL ANALYTICS LTD": "FRACTAL",
    "KSH INTERNATIONAL LIMITED": "KSHINTL",
    "KSH INTERNATIONAL LTD": "KSHINTL",
    "RELIANCE INDUSTRIES LIMITED": "RELIANCE",
    "TATA CONSULTANCY SERVICES LIMITED": "TCS",
    "INFOSYS LIMITED": "INFY",
    "STATE BANK OF INDIA": "SBIN",
    "HDFC BANK LIMITED": "HDFCBANK",
    "ICICI BANK LIMITED": "ICICIBANK",
    "TATA MOTORS LIMITED": "TATAMOTORS",
    "TATA STEEL LIMITED": "TATASTEEL",
}

def clean_fyers_symbol(raw_sym):
    """Normalizes raw symbol / company name to a standard NSE equity ticker."""
    if not raw_sym:
        return ""
    s = str(raw_sym).strip().upper()
    s = re.sub(r'^NSE:', '', s)
    s = re.sub(r'-EQ$', '', s)
    
    if s in NSE_COMPANY_TO_TICKER:
        return NSE_COMPANY_TO_TICKER[s]
    
    # If it is already a clean uppercase ticker (2 to 12 alphanumeric chars with no corporate suffix)
    if re.match(r'^[A-Z0-9&-]{2,12}$', s) and not any(w in s for w in ["LTD", "LIMITED", "CORP", "INDS", "ENGG"]):
        return s

    # Strip corporate legal entity suffixes
    cleaned = re.sub(r'\b(LIMITED|LTD\.?|CORP\.?|INDS\.?|INDUSTRIES|ENGG\.?|CHEM\.?|HOLDINGS|VENTURES|PVT\.?|PRIVATE)\b', '', s).strip()
    cleaned = re.sub(r'[^A-Z0-9]', '', cleaned)
    if 2 <= len(cleaned) <= 12:
        return cleaned
    
    return s[:12]

def parse_fyers_datetime(dt_str, date_fallback="", time_fallback=""):
    """Parses date & time from various FYERS string formats."""
    combined = dt_str.strip() if dt_str else ""
    if not combined:
        if date_fallback and time_fallback:
            combined = f"{date_fallback.strip()} {time_fallback.strip()}"
        elif date_fallback:
            combined = date_fallback.strip()
            
    formats = [
        "%d %b %Y, %I:%M:%S %p",
        "%d %b %Y %I:%M:%S %p",
        "%d %b %Y, %H:%M:%S",
        "%d %b %Y %H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%d/%m/%Y %H:%M:%S",
        "%d-%m-%Y %H:%M:%S",
        "%d/%m/%Y, %I:%M:%S %p",
        "%d-%m-%Y, %I:%M:%S %p",
        "%Y-%m-%d, %I:%M:%S %p",
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%d-%m-%Y"
    ]
    for fmt in formats:
        try:
            dt = datetime.strptime(combined, fmt)
            return dt, dt.strftime("%Y-%m-%d"), dt.strftime("%H:%M:%S")
        except (ValueError, TypeError):
            pass

    # Fallback heuristic
    now = datetime.now()
    d_clean = date_fallback.strip() if date_fallback else now.strftime("%Y-%m-%d")
    if "/" in d_clean:
        parts = d_clean.split("/")
        if len(parts) == 3:
            if len(parts[2]) == 4:
                d_clean = f"{parts[2]}-{parts[1].zfill(2)}-{parts[0].zfill(2)}"
            elif len(parts[0]) == 4:
                d_clean = f"{parts[0]}-{parts[1].zfill(2)}-{parts[2].zfill(2)}"
    t_clean = time_fallback.strip() if time_fallback else "09:20:00"
    if len(t_clean) == 5:
        t_clean += ":00"
    try:
        dt = datetime.strptime(f"{d_clean} {t_clean}", "%Y-%m-%d %H:%M:%S")
    except Exception:
        dt = now
    return dt, d_clean, t_clean

def parse_xlsx_rows(xlsx_bytes):
    """Parses rows from an .xlsx file using pure Python zipfile and xml."""
    rows = []
    with zipfile.ZipFile(io.BytesIO(xlsx_bytes), 'r') as z:
        shared_strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            tree = ET.fromstring(z.read('xl/sharedStrings.xml'))
            for si in tree.findall('.//{*}si'):
                texts = [t.text for t in si.findall('.//{*}t') if t.text]
                shared_strings.append(''.join(texts))
        
        sheet_targets = [n for n in z.namelist() if n.startswith('xl/worksheets/sheet') and n.endswith('.xml')]
        if not sheet_targets:
            return rows
        
        sheet_name = sheet_targets[0]
        tree = ET.fromstring(z.read(sheet_name))
        for row in tree.findall('.//{*}row'):
            row_vals = []
            for c in row.findall('{*}c'):
                t = c.get('t')
                v = c.find('{*}v')
                is_node = c.find('{*}is')
                val = ''
                if v is not None and v.text:
                    val = v.text
                elif is_node is not None:
                    t_nodes = [tn.text for tn in is_node.findall('.//{*}t') if tn.text]
                    val = ''.join(t_nodes)
                elif c.text:
                    val = c.text
                if t == 's' and val.isdigit():
                    idx = int(val)
                    val = shared_strings[idx] if idx < len(shared_strings) else val
                row_vals.append(val.strip())
            if any(row_vals):
                rows.append(row_vals)
    return rows

def parse_csv_or_tsv_rows(text_content):
    """Parses CSV or TSV or space-delimited text into rows."""
    lines = [l.strip() for l in text_content.strip().splitlines() if l.strip()]
    if not lines:
        return []
    
    # Try delimiter detection across first few lines
    delimiter = None
    for l in lines[:15]:
        if '\t' in l:
            delimiter = '\t'
            break
        elif ',' in l:
            delimiter = ','
            break
        elif ';' in l:
            delimiter = ';'
            break
            
    rows = []
    if delimiter:
        try:
            reader = csv.reader(lines, delimiter=delimiter)
            for r in reader:
                if r and any(r):
                    rows.append([cell.strip() for cell in r])
        except Exception:
            rows = []
            
    if not rows or all(len(r) <= 1 for r in rows):
        rows = []
        for l in lines:
            parts = re.split(r'[\t,]+|\s{2,}|\s+', l)
            clean_parts = [p.strip() for p in parts if p.strip()]
            if clean_parts:
                rows.append(clean_parts)
    return rows

def extract_fills_from_rows(rows):
    """
    Extracts individual execution fills from parsed 2D row data.
    Identifies headers and maps columns flexibly, bypassing metadata banners.
    """
    if not rows:
        return []

    # Find header row across first 30 rows
    header_idx = -1
    col_map = {}
    for i, row in enumerate(rows[:30]):
        lowered = [str(c).lower().replace(' ', '').replace('_', '') for c in row]
        has_sym = any(('symbol' in c or 'scrip' in c or 'instrument' in c) for c in lowered)
        has_side = any(('side' in c or 'buysell' in c or 'transtype' in c or 'action' in c) for c in lowered)
        has_qty = any(('qty' in c or 'quantity' in c or 'shares' in c or 'tradedqty' in c) for c in lowered)
        has_price = any(('price' in c or 'rate' in c or 'tradeprice' in c or 'avgprice' in c) for c in lowered)

        if (has_sym and has_qty and has_price) or (has_sym and has_side and (has_qty or has_price)):
            header_idx = i
            for c_i, col in enumerate(lowered):
                if any(k in col for k in ['symbolcode', 'tradingsymbol', 'symbolname', 'symbol', 'scrip', 'instrument']):
                    if 'symbol' not in col_map or 'code' in col:
                        col_map['symbol'] = c_i
                elif any(k in col for k in ['side', 'action', 'buysell', 'transtype', 'tradetype', 'trans_type']):
                    if 'product' not in col:  # prevent Product Type from overriding Side
                        col_map['side'] = c_i
                elif any(k in col for k in ['qty', 'quantity', 'tradedqty', 'shares', 'filledqty', 'filled']):
                    col_map['qty'] = c_i
                elif any(k in col for k in ['tradedprice', 'avgprice', 'tradeprice', 'price', 'rate', 'fillprice']):
                    col_map['price'] = c_i
                elif any(k in col for k in ['date&time', 'tradedatetime', 'datetime', 'timestamp']):
                    col_map['datetime'] = c_i
                elif any(k in col for k in ['tradedate', 'date', 'orderdate']):
                    col_map['date'] = c_i
                elif any(k in col for k in ['tradetime', 'ordertime', 'time']):
                    col_map['time'] = c_i
                elif any(k in col for k in ['exchangeorderid', 'omsorderid', 'orderid']):
                    if 'order_id' not in col_map or 'exchange' in col:
                        col_map['order_id'] = c_i
                elif any(k in col for k in ['status', 'orderstatus']):
                    col_map['status'] = c_i
            break

    fills = []
    data_rows = rows[header_idx + 1:] if header_idx != -1 else rows

    for row in data_rows:
        if not row or len(row) < 3:
            continue

        sym_raw = ""
        side = ""
        qty = 0
        price = 0.0
        datetime_raw = ""
        date_raw = ""
        time_raw = ""
        order_id = ""
        status = "FILLED"

        if header_idx != -1 and 'symbol' in col_map and 'qty' in col_map and 'price' in col_map:
            try:
                sym_raw = str(row[col_map['symbol']]).strip()
                
                # Side
                if 'side' in col_map and col_map['side'] < len(row):
                    side_raw = str(row[col_map['side']]).upper()
                    if any(b in side_raw for b in ["BUY", "B", "1"]):
                        side = "BUY"
                    elif any(s in side_raw for s in ["SELL", "S", "-1"]):
                        side = "SELL"
                
                # Qty: parse commas and decimal values correctly
                qty_clean = re.sub(r'[^\d.]', '', str(row[col_map['qty']]).replace(',', ''))
                qty = int(round(float(qty_clean))) if qty_clean else 0
                
                # Price: parse commas correctly
                price_clean = re.sub(r'[^\d.]', '', str(row[col_map['price']]).replace(',', ''))
                price = float(price_clean) if price_clean else 0.0

                if 'datetime' in col_map and col_map['datetime'] < len(row):
                    datetime_raw = str(row[col_map['datetime']]).strip()
                if 'date' in col_map and col_map['date'] < len(row):
                    date_raw = str(row[col_map['date']]).strip()
                if 'time' in col_map and col_map['time'] < len(row):
                    time_raw = str(row[col_map['time']]).strip()
                if 'order_id' in col_map and col_map['order_id'] < len(row):
                    order_id = str(row[col_map['order_id']]).replace('=', '').replace('"', '').strip()
                if 'status' in col_map and col_map['status'] < len(row):
                    status = str(row[col_map['status']]).upper()
            except Exception:
                continue
        else:
            # Fallback heuristic row parsing (e.g. pasted web row)
            line_str = " ".join(row)
            tokens = re.split(r'[\t\s,]+', line_str)
            for t in tokens:
                if (t.endswith("-EQ") or t.startswith("NSE:") or (t.isupper() and 2 <= len(t) <= 12 and t.isalpha())) and not sym_raw:
                    sym_raw = t
                elif t.upper() in ["BUY", "SELL", "B", "S"] and not side:
                    side = "BUY" if t.upper() in ["BUY", "B"] else "SELL"
                elif ":" in t and len(t) in [5, 8] and not time_raw:
                    time_raw = t
                elif ("-" in t or "/" in t) and len(t) in [8, 9, 10] and not date_raw:
                    date_raw = t
            
            numbers = []
            for t in tokens:
                clean_n = re.sub(r'[^\d.]', '', t.replace(',', ''))
                if clean_n and re.match(r'^\d+(\.\d+)?$', clean_n):
                    numbers.append(float(clean_n))
            if numbers:
                int_candidates = [int(round(n)) for n in numbers if 1 <= n <= 500000]
                if int_candidates:
                    qty = int_candidates[0]
                    price_candidates = [n for n in numbers if n != qty and n >= 1.0]
                    if price_candidates:
                        price = price_candidates[0]

        # Ignore non-filled orders if status is present
        if status and not any(k in status for k in ["FILLED", "EXECUTED", "COMPLETE", "TRADED", "SUCCESS"]):
            continue

        clean_sym = clean_fyers_symbol(sym_raw)
        dt_obj, date_str, time_str = parse_fyers_datetime(datetime_raw, date_fallback=date_raw, time_fallback=time_raw)

        if clean_sym and side and qty > 0 and price > 0:
            fills.append({
                "symbol": clean_sym,
                "raw_symbol": sym_raw,
                "side": side,
                "qty": qty,
                "price": price,
                "val": qty * price,
                "order_id": order_id,
                "dt": dt_obj,
                "date": date_str,
                "time": time_str
            })

    return fills

def aggregate_order_slices(fills):
    """
    Combines exchange partial fills sharing the same Order ID into unified execution legs.
    Calculates volume-weighted average price (VWAP) for each execution leg.
    """
    if not fills:
        return []

    from collections import defaultdict
    orders = defaultdict(lambda: {
        "qty": 0,
        "val": 0.0,
        "dt": None,
        "time": "",
        "raw_symbol": "",
        "order_id": ""
    })

    for f in fills:
        # Group by date, symbol, side, and order_id (or time if order_id absent)
        oid_key = f["order_id"] if f["order_id"] else f["time"]
        key = (f["date"], f["symbol"], f["side"], oid_key)
        
        orders[key]["qty"] += f["qty"]
        orders[key]["val"] += f["val"]
        orders[key]["raw_symbol"] = f["raw_symbol"]
        orders[key]["order_id"] = f["order_id"]
        
        if orders[key]["dt"] is None or f["dt"] < orders[key]["dt"]:
            orders[key]["dt"] = f["dt"]
            orders[key]["time"] = f["time"]

    order_legs = []
    for (date_str, sym, side, _), o in orders.items():
        if o["qty"] <= 0:
            continue
        order_legs.append({
            "date": date_str,
            "symbol": sym,
            "raw_symbol": o["raw_symbol"],
            "side": side,
            "qty": o["qty"],
            "price": o["val"] / o["qty"],
            "dt": o["dt"],
            "time": o["time"],
            "order_id": o["order_id"]
        })

    # Sort chronologically by execution timestamp
    order_legs.sort(key=lambda x: x["dt"])
    return order_legs

def match_roundtrip_trades(fills, existing_count=0, default_setup=DEFAULT_SETUP_NAME):
    """
    Pairs BUY and SELL fills into individual round-trip trades using FIFO position matching.
    Breaks down multiple trades taken in the same stock on the same day into separate individual trade rows.
    Calculates exact execution Entry and Exit prices, hold duration, Gross PnL,
    0.8% Planned SL, 2.0% Planned Target, 2.50 Planned RR, and FYERS statutory friction.
    """
    if not fills:
        return []

    from collections import defaultdict

    # 1. First aggregate broker partial fills sharing the same order ID into clean order legs
    order_legs = aggregate_order_slices(fills)

    # 2. Group order legs by (date, symbol) to prevent intraday positions from spanning days
    by_day_sym = defaultdict(list)
    for l in order_legs:
        by_day_sym[(l["date"], l["symbol"])].append(l)

    raw_matched_trades = []

    # 3. For each symbol on each day, match entries and exits via FIFO queue
    for (d, sym), slegs in by_day_sym.items():
        slegs.sort(key=lambda x: x["dt"])
        open_slices = []

        for leg in slegs:
            qty_rem = leg["qty"]
            side = leg["side"]

            while qty_rem > 0 and open_slices and open_slices[0]["side"] != side:
                op = open_slices[0]
                matched_qty = min(qty_rem, op["qty"])

                is_long = (op["side"] == "BUY")
                direction = "Long" if is_long else "Short"
                entry_px = round(op["price"], 2)
                exit_px = round(leg["price"], 2)

                entry_time_clean = op["time"][:5]
                exit_time_clean = leg["time"][:5]
                raw_sym = op.get("raw_symbol") or leg.get("raw_symbol") or sym

                # Hold duration in minutes
                try:
                    t1 = op["dt"]
                    t2 = leg["dt"]
                    hold_minutes = max(1, int((t2 - t1).total_seconds() / 60))
                except Exception:
                    hold_minutes = 15

                # Exact Gross PnL matching broker execution
                gross_pnl = round(matched_qty * (leg["price"] - op["price"]) if is_long else matched_qty * (op["price"] - leg["price"]), 2)

                # 0.8% Planned SL, 2.0% Planned Target, 2.50R
                if direction == "Long":
                    stop_px = round(entry_px * (1.0 - PLANNED_SL_PCT), 2)
                    target_px = round(entry_px * (1.0 + PLANNED_TGT_PCT), 2)
                    risk_per_share = round(entry_px - stop_px, 2)
                else:
                    stop_px = round(entry_px * (1.0 + PLANNED_SL_PCT), 2)
                    target_px = round(entry_px * (1.0 - PLANNED_TGT_PCT), 2)
                    risk_per_share = round(stop_px - entry_px, 2)

                planned_rr = PLANNED_RR
                risk_amount = round(risk_per_share * matched_qty, 2)

                # FYERS statutory friction
                charges = calculate_fyers_charges(entry_px, exit_px, matched_qty, direction)
                costs = round(float(charges.get("total_costs", 0.0)), 2)

                net_pnl = round(gross_pnl - costs, 2)
                r_multiple = round(net_pnl / risk_amount, 2) if risk_amount > 0 else 0.0
                outcome = "Win" if net_pnl > 10 else ("Loss" if net_pnl < -10 else "Break-Even")

                raw_matched_trades.append({
                    "date": d,
                    "entry_dt": op["dt"],
                    "time": entry_time_clean,
                    "exit_time": exit_time_clean,
                    "hold_duration": hold_minutes,
                    "symbol": sym,
                    "raw_symbol": raw_sym,
                    "direction": direction,
                    "setup_name": default_setup or DEFAULT_SETUP_NAME,
                    "scanner_alert_time": entry_time_clean,
                    "htf_ok": "Y",
                    "no_chase": "Y",
                    "stop_defined": "Y",
                    "target_price": target_px,
                    "rr_planned": planned_rr,
                    "risk_percent": PLANNED_SL_PCT,
                    "risk_amount": risk_amount,
                    "entry_price": entry_px,
                    "stop_price": stop_px,
                    "exit_price": exit_px,
                    "qty": int(matched_qty),
                    "gross_pnl": gross_pnl,
                    "costs": costs,
                    "net_pnl": net_pnl,
                    "r_multiple": r_multiple,
                    "outcome": outcome,
                    "checklist_score": 5,
                    "rule_violation": "N",
                    "violation_type": "None",
                    "emotion_before": 2,
                    "emotion_during": 2,
                    "emotion_after": 2 if net_pnl > 0 else 3,
                    "trade_valid": "Y",
                    "lesson": f"Imported FYERS Tradebook ({raw_sym}). {direction} {int(matched_qty)} @ ₹{entry_px} -> ₹{exit_px} ({hold_minutes}m hold). 0.8% SL (₹{stop_px}), 2.0% Target (₹{target_px}).",
                    "screenshot_link": f"https://www.tradingview.com/chart/?symbol=NSE:{sym}"
                })

                qty_rem -= matched_qty
                op["qty"] -= matched_qty
                if op["qty"] <= 0.0001:
                    open_slices.pop(0)

            if qty_rem > 0.0001:
                open_slices.append({
                    "side": side,
                    "qty": qty_rem,
                    "price": leg["price"],
                    "time": leg["time"],
                    "dt": leg["dt"],
                    "raw_symbol": leg.get("raw_symbol", sym)
                })

    # 4. Sort chronologically across the trading account by Date, Entry Time, and Datetime
    raw_matched_trades.sort(key=lambda x: (x["date"], x["time"], x["entry_dt"]))

    # 5. Assign sequential trade IDs
    matched_trades = []
    trade_idx = existing_count
    for t in raw_matched_trades:
        trade_idx += 1
        t_copy = dict(t)
        t_copy.pop("entry_dt", None)
        t_copy["id"] = f"T-{trade_idx:03d}"
        t_copy["day"] = get_weekday_from_date(t_copy["date"], "Mon")
        matched_trades.append(t_copy)

    return matched_trades

def parse_fyers_payload(payload_bytes_or_str, file_name="", existing_count=0, default_setup=DEFAULT_SETUP_NAME):
    """Universal parser entrypoint for any FYERS file or text payload."""
    if isinstance(payload_bytes_or_str, bytes):
        if file_name.lower().endswith(".xlsx") or payload_bytes_or_str[:4] == b'PK\x03\x04':
            rows = parse_xlsx_rows(payload_bytes_or_str)
        else:
            text = payload_bytes_or_str.decode("utf-8", errors="ignore")
            rows = parse_csv_or_tsv_rows(text)
    else:
        rows = parse_csv_or_tsv_rows(str(payload_bytes_or_str))

    fills = extract_fills_from_rows(rows)
    trades = match_roundtrip_trades(fills, existing_count=existing_count, default_setup=default_setup)
    return trades
