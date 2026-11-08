#!/usr/bin/env python3
"""
FYERS Trades Ingestion & Matching Engine
Trader Execution Reset System • Intraday Equities (NSE)

Features:
- Robust multi-format parsing: CSV, TSV, XLSX, JSON, and Web Copy-Paste
- Automatic column detection (Tradebook or Orderbook exports)
- FIFO & chronological fill matching for Buy & Sell legs
- Exact FYERS Statutory Friction Computation (STT, GST, Exchange, SEBI, Stamp)
- Strict Rule Baseline Integration:
    * Planned SL: exactly 0.8% of entry price
    * Planned Target: exactly 2.0% of entry price
    * Planned Risk:Reward: 2.50R (2.0% / 0.8%)
    * Default Setup Name: "Default Setup" (fully customizable/alterable)
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
        
        # Look for sheet1 or any sheet
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
    
    # Detect delimiter
    sample = lines[0]
    if '\t' in sample:
        delimiter = '\t'
    elif ',' in sample:
        delimiter = ','
    elif ';' in sample:
        delimiter = ';'
    else:
        delimiter = None
    
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
    Identifies headers and maps columns flexibly.
    """
    if not rows:
        return []

    # Find header row
    header_idx = -1
    col_map = {}
    for i, row in enumerate(rows[:10]):
        lowered = [str(c).lower().replace(' ', '').replace('_', '') for c in row]
        has_sym = any('symbol' in c or 'scrip' in c or 'instrument' in c for c in lowered)
        has_side = any('side' in c or 'type' in c or 'action' in c or 'buysell' in c or 'transtype' in c for c in lowered)
        has_qty = any('qty' in c or 'quantity' in c or 'shares' in c or 'tradedqty' in c for c in lowered)
        has_price = any('price' in c or 'rate' in c or 'tradeprice' in c or 'avgprice' in c for c in lowered)

        if (has_sym and has_qty and has_price) or (has_sym and has_side):
            header_idx = i
            for c_i, col in enumerate(lowered):
                if any(k in col for k in ['symbol', 'scrip', 'instrument', 'tradingsymbol']):
                    col_map['symbol'] = c_i
                elif any(k in col for k in ['side', 'action', 'type', 'buysell', 'transtype', 'tradetype']):
                    col_map['side'] = c_i
                elif any(k in col for k in ['qty', 'quantity', 'tradedqty', 'shares', 'filledqty']):
                    col_map['qty'] = c_i
                elif any(k in col for k in ['price', 'tradeprice', 'avgprice', 'rate', 'avg.price', 'fillprice']):
                    col_map['price'] = c_i
                elif any(k in col for k in ['tradetime', 'ordertime', 'time', 'timestamp', 'tradedatetime']):
                    col_map['time'] = c_i
                elif any(k in col for k in ['tradedate', 'date', 'orderdate']):
                    col_map['date'] = c_i
                elif any(k in col for k in ['status', 'orderstatus']):
                    col_map['status'] = c_i
            break

    fills = []
    data_rows = rows[header_idx + 1:] if header_idx != -1 else rows

    for row in data_rows:
        if not row or len(row) < 3:
            continue

        sym = ""
        side = ""
        qty = 0
        price = 0.0
        time_str = ""
        date_str = ""
        status = "FILLED"

        if header_idx != -1 and 'symbol' in col_map and 'qty' in col_map and 'price' in col_map:
            try:
                sym = str(row[col_map['symbol']]).strip()
                side_raw = str(row[col_map.get('side', -1)]).upper() if 'side' in col_map and col_map['side'] < len(row) else ""
                side = "BUY" if any(b in side_raw for b in ["BUY", "B", "1"]) else ("SELL" if any(s in side_raw for s in ["SELL", "S", "-1"]) else "")
                
                qty_raw = re.sub(r'[^\d]', '', str(row[col_map['qty']]))
                qty = int(qty_raw) if qty_raw else 0
                
                price_raw = re.sub(r'[^\d.]', '', str(row[col_map['price']]))
                price = float(price_raw) if price_raw else 0.0

                if 'time' in col_map and col_map['time'] < len(row):
                    time_str = str(row[col_map['time']]).strip()
                if 'date' in col_map and col_map['date'] < len(row):
                    date_str = str(row[col_map['date']]).strip()
                if 'status' in col_map and col_map['status'] < len(row):
                    status = str(row[col_map['status']]).upper()
            except Exception:
                continue
        else:
            # Fallback heuristic row parsing (e.g. pasted web row)
            line_str = " ".join(row)
            tokens = re.split(r'[\t\s,]+', line_str)
            for t in tokens:
                if (t.endswith("-EQ") or t.startswith("NSE:") or (t.isupper() and 2 <= len(t) <= 12 and t.isalpha())) and not sym:
                    sym = t
                elif t.upper() in ["BUY", "SELL", "B", "S"] and not side:
                    side = "BUY" if t.upper() in ["BUY", "B"] else "SELL"
                elif ":" in t and len(t) in [5, 8] and not time_str:
                    time_str = t
                elif ("-" in t or "/" in t) and len(t) in [8, 9, 10] and not date_str:
                    date_str = t
            
            numbers = []
            for t in tokens:
                clean_n = re.sub(r'[^\d.]', '', t)
                if clean_n and re.match(r'^\d+(\.\d+)?$', clean_n):
                    numbers.append(float(clean_n))
            if numbers:
                int_candidates = [int(n) for n in numbers if n.is_integer() and 1 <= n <= 500000]
                if int_candidates:
                    qty = int_candidates[0]
                    price_candidates = [n for n in numbers if n != qty and n >= 1.0]
                    if price_candidates:
                        price = price_candidates[0]

        # Ignore non-filled orders if status is present
        if status not in ["FILLED", "EXECUTED", "COMPLETE", "TRADED", "SUCCESS"]:
            continue

        sym = sym.replace("NSE:", "").replace("-EQ", "").strip().upper()
        if sym and side and qty > 0 and price > 0:
            fills.append({
                "symbol": sym,
                "side": side,
                "qty": qty,
                "price": price,
                "date": date_str,
                "time": time_str
            })

    return fills

def match_roundtrip_trades(fills, existing_count=0, default_setup=DEFAULT_SETUP_NAME):
    """
    Pairs BUY and SELL fills using FIFO matching for each symbol.
    Generates compliant trade objects with 0.8% SL, 2.0% Target, and 2.50R.
    """
    if not fills:
        return []

    from collections import defaultdict
    by_symbol = defaultdict(list)
    for f in fills:
        by_symbol[f["symbol"]].append(f)

    matched_trades = []
    trade_idx = existing_count

    for sym, sym_fills in by_symbol.items():
        buy_queue = [dict(f) for f in sym_fills if f["side"] == "BUY"]
        sell_queue = [dict(f) for f in sym_fills if f["side"] == "SELL"]

        while buy_queue and sell_queue:
            b = buy_queue[0]
            s = sell_queue[0]
            matched_qty = min(b["qty"], s["qty"])
            if matched_qty <= 0:
                break

            # Chronological direction determination
            b_time = b.get("time") or "09:20:00"
            s_time = s.get("time") or "09:30:00"
            is_long = b_time <= s_time

            entry_px = b["price"] if is_long else s["price"]
            exit_px = s["price"] if is_long else b["price"]
            entry_time = b_time if is_long else s_time
            exit_time = s_time if is_long else b_time
            trade_date = b.get("date") or s.get("date") or datetime.now().strftime("%Y-%m-%d")

            # Standardize date format to YYYY-MM-DD
            if "/" in trade_date:
                parts = trade_date.split("/")
                if len(parts) == 3:
                    if len(parts[2]) == 4: # DD/MM/YYYY
                        trade_date = f"{parts[2]}-{parts[1].zfill(2)}-{parts[0].zfill(2)}"
                    elif len(parts[0]) == 4: # YYYY/MM/DD
                        trade_date = f"{parts[0]}-{parts[1].zfill(2)}-{parts[2].zfill(2)}"

            # Format times to HH:MM
            entry_time_clean = entry_time[:5] if len(entry_time) >= 5 else "09:20"
            exit_time_clean = exit_time[:5] if len(exit_time) >= 5 else "09:30"

            # -------------------------------------------------------------
            # EXACT RULE BASELINE CALCULATIONS (0.8% SL, 2.0% TARGET, 2.50R)
            # -------------------------------------------------------------
            direction = "Long" if is_long else "Short"
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

            gross_pnl = round((exit_px - entry_px) * matched_qty if direction == "Long" else (entry_px - exit_px) * matched_qty, 2)
            net_pnl = round(gross_pnl - costs, 2)
            r_multiple = round(net_pnl / risk_amount, 2) if risk_amount > 0 else 0.0

            outcome = "Win" if net_pnl > 10 else ("Loss" if net_pnl < -10 else "Break-Even")

            trade_idx += 1
            trade_obj = {
                "id": f"T-{trade_idx:03d}",
                "date": trade_date,
                "day": get_weekday_from_date(trade_date, "Mon"),
                "time": entry_time_clean,
                "exit_time": exit_time_clean,
                "hold_duration": 8,
                "symbol": sym,
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
                "entry_price": round(entry_px, 2),
                "stop_price": stop_px,
                "exit_price": round(exit_px, 2),
                "qty": matched_qty,
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
                "lesson": f"Imported FYERS Tradebook fill. 0.8% planned SL (₹{stop_px}), 2.0% target (₹{target_px}).",
                "screenshot_link": f"https://www.tradingview.com/chart/?symbol=NSE:{sym}"
            }
            matched_trades.append(trade_obj)

            b["qty"] -= matched_qty
            s["qty"] -= matched_qty
            if b["qty"] <= 0:
                buy_queue.pop(0)
            if s["qty"] <= 0:
                sell_queue.pop(0)

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
