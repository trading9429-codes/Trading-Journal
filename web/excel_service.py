import zipfile
import html
import os
import sys
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XLSX_PATH = os.environ.get("XLSX_PATH", os.path.join(BASE_DIR, "deliverables", "D3_Tracking_Spreadsheet.xlsx"))
DATA_JSON_PATH = os.environ.get("DATA_JSON_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "trades_store.json"))

class SharedStringsTable:
    def __init__(self):
        self.strings = []
        self.str_to_idx = {}
        
    def get_index(self, s):
        if s is None:
            s = ""
        s = str(s)
        if s in self.str_to_idx:
            return self.str_to_idx[s]
        idx = len(self.strings)
        self.strings.append(s)
        self.str_to_idx[s] = idx
        return idx
        
    def to_xml(self):
        parts = [
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
            f'<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="{len(self.strings)}" uniqueCount="{len(self.strings)}">'
        ]
        for s in self.strings:
            escaped = html.escape(s)
            parts.append(f'<si><t>{escaped}</t></si>')
        parts.append('</sst>')
        return "".join(parts)

def col_letter(col_idx):
    result = ""
    while col_idx > 0:
        col_idx, remainder = divmod(col_idx - 1, 26)
        result = chr(65 + remainder) + result
    return result

def escape_xml(s):
    if s is None:
        return ""
    return html.escape(str(s))

def make_cell(ref, val=None, formula=None, style_id=None, cell_type=None, sst=None):
    s_attr = f' s="{style_id}"' if style_id is not None else ""
    if formula is not None:
        f_xml = f'<f>{escape_xml(formula)}</f>'
        if cell_type == "str" or (cell_type is None and isinstance(val, str) and val != ""):
            v_xml = f'<v>{escape_xml(val)}</v>' if val is not None else '<v></v>'
            return f'<c r="{ref}"{s_attr} t="str">{f_xml}{v_xml}</c>'
        else:
            v_xml = f'<v>{escape_xml(val)}</v>' if val is not None else '<v></v>'
            return f'<c r="{ref}"{s_attr}>{f_xml}{v_xml}</c>'
    elif val is None or val == "":
        return f'<c r="{ref}"{s_attr}/>'
    elif cell_type == "s" or isinstance(val, str):
        if sst is not None:
            s_idx = sst.get_index(val)
            return f'<c r="{ref}"{s_attr} t="s"><v>{s_idx}</v></c>'
        else:
            return f'<c r="{ref}"{s_attr} t="inlineStr"><is><t>{escape_xml(val)}</t></is></c>'
    elif isinstance(val, (int, float)):
        return f'<c r="{ref}"{s_attr}><v>{val}</v></c>'
    else:
        if sst is not None:
            s_idx = sst.get_index(str(val))
            return f'<c r="{ref}"{s_attr} t="s"><v>{s_idx}</v></c>'
        else:
            return f'<c r="{ref}"{s_attr} t="inlineStr"><is><t>{escape_xml(str(val))}</t></is></c>'

def calculate_fyers_charges(entry: float, exit_p: float, qty: int, direction: str):
    """
    FYERS Equity Intraday Statutory & Brokerage Charges:
    • Buy Turnover = Buy Price * Quantity
    • Sell Turnover = Sell Price * Quantity
    • Total Turnover = Buy Turnover + Sell Turnover
    • Brokerage = min(Buy Turnover * 0.0003, 20) + min(Sell Turnover * 0.0003, 20)
    • STT = Sell Turnover * 0.00025 (0.025% on sell side)
    • Exchange Charges = Total Turnover * 0.0000297 (0.00297% on NSE)
    • SEBI Fee = Total Turnover * 0.0000001 (Rs. 10 per crore)
    • Stamp Duty = Buy Turnover * 0.00003 (0.003% on buy side)
    • GST = (Total Brokerage + Exchange Charges + SEBI Fee) * 0.18
    """
    buy_price = entry if direction == "Long" else exit_p
    sell_price = exit_p if direction == "Long" else entry
    
    buy_turnover = round(buy_price * qty, 2)
    sell_turnover = round(sell_price * qty, 2)
    total_turnover = round(buy_turnover + sell_turnover, 2)
    
    brokerage_buy = min(buy_turnover * 0.0003, 20.0)
    brokerage_sell = min(sell_turnover * 0.0003, 20.0)
    total_brokerage = round(brokerage_buy + brokerage_sell, 2)
    
    stt = round(sell_turnover * 0.00025, 2)
    exchange_charges = round(total_turnover * 0.0000297, 2)
    sebi_fee = round(total_turnover * 0.0000001, 2)
    stamp_duty = round(buy_turnover * 0.00003, 2)
    gst = round((total_brokerage + exchange_charges + sebi_fee) * 0.18, 2)
    
    total_costs = round(total_brokerage + stt + exchange_charges + sebi_fee + stamp_duty + gst, 2)
    
    return {
        "buy_turnover": buy_turnover,
        "sell_turnover": sell_turnover,
        "total_turnover": total_turnover,
        "brokerage": total_brokerage,
        "stt": stt,
        "exchange_charges": exchange_charges,
        "sebi_fee": sebi_fee,
        "stamp_duty": stamp_duty,
        "gst": gst,
        "total_costs": total_costs
    }

DEFAULT_TRADES = [
    {
        "id": "T-001 [EXAMPLE]",
        "date": "2026-10-20",
        "day": "Tue",
        "time": "09:25",
        "symbol": "RELIANCE",
        "direction": "Long",
        "setup_name": "1m Pullback to 9EMA",
        "scanner_alert_time": "09:23",
        "htf_ok": "Y",
        "no_chase": "Y",
        "stop_defined": "Y",
        "target_price": 2511.00,
        "rr_planned": 2.20,
        "risk_percent": 0.0025,
        "risk_amount": 500.00,
        "entry_price": 2500.00,
        "stop_price": 2495.00,
        "exit_price": 2511.00,
        "qty": 100,
        "gross_pnl": 1100.00,
        "costs": 135.10,
        "net_pnl": 964.90,
        "r_multiple": 1.93,
        "outcome": "Win",
        "checklist_score": 5,
        "rule_violation": "N",
        "violation_type": "None",
        "emotion_before": 2,
        "emotion_during": 3,
        "emotion_after": 2,
        "trade_valid": "Y",
        "lesson": "Followed plan, entry at limit, patient exit at 2.2R target.",
        "screenshot_link": "https://tradingview.com/x/example1"
    },
    {
        "id": "T-002 [EXAMPLE]",
        "date": "2026-10-20",
        "day": "Tue",
        "time": "10:05",
        "symbol": "TCS",
        "direction": "Short",
        "setup_name": "1m Breakdown Re-test",
        "scanner_alert_time": "10:02",
        "htf_ok": "Y",
        "no_chase": "Y",
        "stop_defined": "Y",
        "target_price": 3478.00,
        "rr_planned": 2.20,
        "risk_percent": 0.0025,
        "risk_amount": 500.00,
        "entry_price": 3500.00,
        "stop_price": 3510.00,
        "exit_price": 3510.00,
        "qty": 50,
        "gross_pnl": -500.00,
        "costs": 108.54,
        "net_pnl": -608.54,
        "r_multiple": -1.22,
        "outcome": "Loss",
        "checklist_score": 5,
        "rule_violation": "N",
        "violation_type": "None",
        "emotion_before": 3,
        "emotion_during": 4,
        "emotion_after": 3,
        "trade_valid": "Y",
        "lesson": "Setup failed normally; respected stop without hesitation; entered 30m cooldown.",
        "screenshot_link": "https://tradingview.com/x/example2"
    },
    {
        "id": "T-003 [EXAMPLE]",
        "date": "2026-10-21",
        "day": "Wed",
        "time": "09:40",
        "symbol": "INFY",
        "direction": "Long",
        "setup_name": "1m Momentum Breakout",
        "scanner_alert_time": "09:38",
        "htf_ok": "Y",
        "no_chase": "Y",
        "stop_defined": "Y",
        "target_price": 1461.00,
        "rr_planned": 2.20,
        "risk_percent": 0.0025,
        "risk_amount": 500.00,
        "entry_price": 1450.00,
        "stop_price": 1445.00,
        "exit_price": 1461.00,
        "qty": 100,
        "gross_pnl": 1100.00,
        "costs": 98.31,
        "net_pnl": 1001.69,
        "r_multiple": 2.00,
        "outcome": "Win",
        "checklist_score": 5,
        "rule_violation": "N",
        "violation_type": "None",
        "emotion_before": 2,
        "emotion_during": 3,
        "emotion_after": 2,
        "trade_valid": "Y",
        "lesson": "Good patience waiting for bar close confirmation. Exited at 2.2R target.",
        "screenshot_link": "https://tradingview.com/x/example3"
    }
]

def get_weekday_from_date(date_str: str, fallback: str = "Mon") -> str:
    """Safely and accurately extracts 3-letter weekday (Mon, Tue, Wed, Thu, Fri, Sat, Sun)."""
    if not date_str:
        return fallback or "Mon"
    date_str = str(date_str).strip()
    
    day_map = {
        "monday": "Mon", "mon": "Mon",
        "tuesday": "Tue", "tue": "Tue",
        "wednesday": "Wed", "wed": "Wed",
        "thursday": "Thu", "thu": "Thu",
        "friday": "Fri", "fri": "Fri",
        "saturday": "Sat", "sat": "Sat",
        "sunday": "Sun", "sun": "Sun"
    }
    if date_str.lower() in day_map:
        return day_map[date_str.lower()]

    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d", "%d.%m.%Y", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
        try:
            return datetime.strptime(date_str, fmt).strftime("%a")
        except ValueError:
            pass

    try:
        from dateutil import parser
        return parser.parse(date_str).strftime("%a")
    except Exception:
        pass

    return fallback or "Mon"

class ExcelTradeManager:
    def __init__(self):
        self.trades = self._load_data()
        self.sync_excel_file()
        
    def _load_data(self):
        # 1. Try loading from remote GitHub backup if configured
        try:
            from github_sync import get_remote_file_info
            _, remote_trades, err = get_remote_file_info()
            if remote_trades and isinstance(remote_trades, list) and len(remote_trades) > 0:
                print(f"[Cloud Backup] Loaded {len(remote_trades)} trades from GitHub backup.")
                for t in remote_trades:
                    if isinstance(t, dict):
                        t["day"] = get_weekday_from_date(t.get("date"), t.get("day"))
                self._save_local(remote_trades)
                return remote_trades
        except Exception as e:
            pass

        # 2. Try loading from local DATA_JSON_PATH
        if os.path.exists(DATA_JSON_PATH):
            try:
                with open(DATA_JSON_PATH, "r") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        for t in data:
                            if isinstance(t, dict):
                                t["day"] = get_weekday_from_date(t.get("date"), t.get("day"))
                        return data
            except Exception:
                pass
        self._save_local(DEFAULT_TRADES)
        return DEFAULT_TRADES
        
    def _save_local(self, trades_list):
        os.makedirs(os.path.dirname(DATA_JSON_PATH), exist_ok=True)
        with open(DATA_JSON_PATH, "w") as f:
            json.dump(trades_list, f, indent=2)

    def _save_data(self, trades_list):
        self._save_local(trades_list)
        try:
            from github_sync import async_push_trades
            async_push_trades(trades_list)
        except Exception as e:
            pass
            
    def get_trades(self):
        return self.trades
        
    def add_trade(self, payload):
        symbol = str(payload.get("symbol", "")).strip().upper()
        direction = str(payload.get("direction", "Long")).capitalize()
        entry = float(payload.get("entry_price", 0))
        stop = float(payload.get("stop_price", 0))
        exit_p = float(payload.get("exit_price", 0))
        qty = int(payload.get("qty", 1))
        
        now = datetime.now()
        date_str = str(payload.get("date") or now.strftime("%Y-%m-%d"))
        time_str = str(payload.get("time") or now.strftime("%H:%M"))
        exit_time_str = str(payload.get("exit_time") or time_str)
        day_str = get_weekday_from_date(date_str, payload.get("day"))
        
        setup_name = str(payload.get("setup_name") or "1m Indicator Setup")
        scanner_time = str(payload.get("scanner_alert_time") or time_str)
        lesson = str(payload.get("lesson") or "Trade logged via Web Quick-Logger")
        screenshot = str(payload.get("screenshot_link") or payload.get("screenshot") or "")
        
        # Calculations
        risk_per_share = abs(entry - stop)
        risk_amount = round(risk_per_share * qty, 2)
        reward_per_share = (exit_p - entry) if direction == "Long" else (entry - exit_p)
        
        # Target Price
        target = float(payload.get("target_price") or payload.get("target") or 0.0)
        if target <= 0:
            target = round(entry + 2.2 * risk_per_share if direction == "Long" else entry - 2.2 * risk_per_share, 2)

        rr_planned = float(payload.get("rr_planned") or (round(abs(target - entry) / risk_per_share, 2) if risk_per_share > 0 else 0.0))
        
        # Costs / FYERS Brokerage
        if payload.get("costs") is not None and float(payload.get("costs")) > 0:
            costs = round(float(payload.get("costs")), 2)
        else:
            try:
                charges = calculate_fyers_charges(entry, exit_p, qty, direction)
                costs = float(charges.get("total_costs", 0.0))
            except Exception:
                turnover = (entry * qty) + (exit_p * qty)
                costs = round(0.0011 * turnover, 2)
                
        gross_pnl = float(payload.get("gross_pnl") if payload.get("gross_pnl") is not None else round(reward_per_share * qty, 2))
        net_pnl = float(payload.get("net_pnl") if payload.get("net_pnl") is not None else round(gross_pnl - costs, 2))
        r_multiple = float(payload.get("r_multiple") if payload.get("r_multiple") is not None else (round(net_pnl / risk_amount, 2) if risk_amount > 0 else 0.0))
        outcome = payload.get("outcome") or ("Win" if net_pnl > 0 else ("Loss" if net_pnl < 0 else "BE"))
        
        checklist_score = int(payload.get("checklist_score", 5))
        rule_violation = "Y" if payload.get("rule_violation") in [True, "Y", "y"] else "N"
        violation_type = str(payload.get("violation_type") or "None")
        
        trade_valid = "Y" if (checklist_score >= 5 and rule_violation == "N" and rr_planned >= 2.2) else "N"
        
        trade_num = len(self.trades) + 1
        new_id = str(payload.get("id") or f"T-{trade_num:03d}")
        
        new_trade = {
            "id": new_id,
            "date": date_str,
            "day": day_str,
            "time": time_str,
            "exit_time": exit_time_str,
            "hold_duration": int(payload.get("hold_duration") or 0),
            "symbol": symbol,
            "direction": direction,
            "setup_name": setup_name,
            "scanner_alert_time": scanner_time,
            "htf_ok": payload.get("htf_ok", "Y"),
            "no_chase": payload.get("no_chase", "Y"),
            "stop_defined": payload.get("stop_defined", "Y"),
            "target_price": target,
            "rr_planned": rr_planned,
            "risk_percent": float(payload.get("risk_percent", 0.0025)),
            "risk_amount": risk_amount,
            "entry_price": entry,
            "stop_price": stop,
            "exit_price": exit_p,
            "qty": qty,
            "gross_pnl": gross_pnl,
            "costs": costs,
            "net_pnl": net_pnl,
            "r_multiple": r_multiple,
            "outcome": outcome,
            "checklist_score": checklist_score,
            "rule_violation": rule_violation,
            "violation_type": violation_type,
            "emotion_before": int(payload.get("emotion_before", 2)),
            "emotion_during": int(payload.get("emotion_during", 3)),
            "emotion_after": int(payload.get("emotion_after", 2)),
            "mental_state": payload.get("mental_state") or "Calm & Patient",
            "tags": payload.get("tags") or [],
            "screenshot_data": payload.get("screenshot_data") or "",
            "trade_valid": trade_valid,
            "lesson": lesson,
            "screenshot_link": screenshot
        }
        
        self.trades.append(new_trade)
        self._save_data(self.trades)
        self.sync_excel_file()
        return new_trade
        
    def reset_examples(self):
        self.trades = []
        self._save_data(self.trades)
        self.sync_excel_file()
        return {"status": "ok", "message": "Example trades cleared. Ready for fresh live trading."}

    def reload_defaults(self):
        self.trades = list(DEFAULT_TRADES)
        self._save_data(self.trades)
        self.sync_excel_file()
        return {"status": "ok", "message": "Defaults reloaded."}

    def set_trades(self, trades_list):
        for t in trades_list:
            if isinstance(t, dict):
                t["day"] = get_weekday_from_date(t.get("date"), t.get("day"))
        self.trades = list(trades_list)
        self._save_data(self.trades)
        self.sync_excel_file()
        return {"status": "ok", "message": f"{len(self.trades)} trades synchronized to Excel workbook."}

    def get_stats(self):
        total_trades = len(self.trades)
        if total_trades == 0:
            return {
                "total_trades": 0,
                "wins": 0,
                "losses": 0,
                "win_rate": 0.0,
                "net_pnl": 0.0,
                "avg_r": 0.0,
                "adherence_pct": 100.0,
                "violations": 0,
                "revenge_trades": 0,
                "total_friction": 0.0
            }
            
        wins = sum(1 for t in self.trades if t.get("outcome") == "Win")
        losses = sum(1 for t in self.trades if t.get("outcome") == "Loss")
        net_pnl = round(sum(t.get("net_pnl", 0) for t in self.trades), 2)
        total_r = sum(t.get("r_multiple", 0) for t in self.trades)
        avg_r = round(total_r / total_trades, 2)
        win_rate = round((wins / total_trades) * 100, 1)
        
        score_5_count = sum(1 for t in self.trades if t.get("checklist_score", 0) >= 5)
        adherence_pct = round((score_5_count / total_trades) * 100, 1)
        violations = sum(1 for t in self.trades if t.get("rule_violation") == "Y")
        revenge = sum(1 for t in self.trades if t.get("violation_type") == "Revenge")
        friction = round(sum(t.get("costs", 0) for t in self.trades), 2)
        
        return {
            "total_trades": total_trades,
            "wins": wins,
            "losses": losses,
            "win_rate": win_rate,
            "net_pnl": net_pnl,
            "avg_r": avg_r,
            "adherence_pct": adherence_pct,
            "violations": violations,
            "revenge_trades": revenge,
            "total_friction": friction
        }

    def sync_excel_file(self):
        from build_v2_system import build_sheet_xml, styles_xml
        sst = SharedStringsTable()
        stats = self.get_stats()
        
        # Re-build complete openxml sheets matching our verified schema
        # 0. Dashboard Tab
        dash_widths = {
            1: 4, 2: 22, 3: 16, 4: 16, 5: 4, 6: 22, 7: 18, 8: 18, 9: 4, 10: 22, 11: 18, 12: 18
        }
        
        dash_custom_rows = {
            1: {"height": 34, "cells": [{"ref": "B1", "val": "TRADER EXECUTION RESET SYSTEM — VISUAL COMMAND CENTER", "s": 10}]},
            2: {"height": 18, "cells": [{"ref": "B2", "val": "NSE Equities 1m | Window: 09:15–10:30 AM IST | Starting Capital: ₹2,00,000 | Risk: 0.25% (₹500) | Min RR: ≥ 2.2 | FYERS Charges", "s": 11}]},
            4: {
                "height": 18,
                "cells": [
                    {"ref": "B4", "val": "STARTING & CURRENT CAPITAL", "s": 12}, {"ref": "C4", "val": "", "s": 12}, {"ref": "D4", "val": "", "s": 12},
                    {"ref": "F4", "val": "CUMULATIVE NET P&L", "s": 12}, {"ref": "G4", "val": "", "s": 12}, {"ref": "H4", "val": "", "s": 12},
                    {"ref": "J4", "val": "CHECKLIST ADHERENCE", "s": 12}, {"ref": "K4", "val": "", "s": 12}, {"ref": "L4", "val": "", "s": 12},
                ]
            },
            5: {
                "height": 30,
                "cells": [
                    {"ref": "B5", "val": f"₹{200000 + stats['net_pnl']:,.2f} ({((stats['net_pnl']/200000)*100):+.2f}%)", "s": 13}, {"ref": "C5", "val": "", "s": 13}, {"ref": "D5", "val": "", "s": 13},
                    {"ref": "F5", "f": "SUM(Trade_Log!U2:U100)", "val": stats["net_pnl"], "s": 14}, {"ref": "G5", "val": "", "s": 14}, {"ref": "H5", "val": "", "s": 14},
                    {"ref": "J5", "f": 'IF(COUNTA(Trade_Log!B2:B100)=0,0,COUNTIF(Trade_Log!X2:X100,5)/COUNTA(Trade_Log!B2:B100))', "val": stats["adherence_pct"] / 100.0, "s": 15}, {"ref": "K5", "val": "", "s": 15}, {"ref": "L5", "val": "", "s": 15},
                ]
            },
            6: {
                "height": 18,
                "cells": [
                    {"ref": "B6", "val": "Starting Capital: ₹2,00,000 | Risk: ₹500 (0.25%)", "s": 16}, {"ref": "C6", "val": "", "s": 16}, {"ref": "D6", "val": "", "s": 16},
                    {"ref": "F6", "val": "Net of FYERS Brokerage & Statutory Taxes (STT, GST, Exch, SEBI, Stamp)", "s": 16}, {"ref": "G6", "val": "", "s": 16}, {"ref": "H6", "val": "", "s": 16},
                    {"ref": "J6", "val": "Target: ≥ 95% | Below 90% = Demotion", "s": 16}, {"ref": "K6", "val": "", "s": 16}, {"ref": "L6", "val": "", "s": 16},
                ]
            },
            8: {
                "height": 18,
                "cells": [
                    {"ref": "B8", "val": "AVERAGE NET R / TRADE", "s": 12}, {"ref": "C8", "val": "", "s": 12}, {"ref": "D8", "val": "", "s": 12},
                    {"ref": "F8", "val": "WIN RATE % (TRADES)", "s": 12}, {"ref": "G8", "val": "", "s": 12}, {"ref": "H8", "val": "", "s": 12},
                    {"ref": "J8", "val": "DISCIPLINE LEAK DETECTOR", "s": 12}, {"ref": "K8", "val": "", "s": 12}, {"ref": "L8", "val": "", "s": 12},
                ]
            },
            9: {
                "height": 30,
                "cells": [
                    {"ref": "B9", "f": 'IFERROR(AVERAGE(Trade_Log!V2:V100),0)', "val": stats["avg_r"], "s": 18}, {"ref": "C9", "val": "", "s": 18}, {"ref": "D9", "val": "", "s": 18},
                    {"ref": "F9", "f": 'IF(COUNTA(Trade_Log!B2:B100)=0,0,COUNTIF(Trade_Log!W2:W100,"Win")/COUNTA(Trade_Log!B2:B100))', "val": stats["win_rate"] / 100.0, "s": 15}, {"ref": "G9", "val": "", "s": 15}, {"ref": "H9", "val": "", "s": 15},
                    {"ref": "J9", "f": 'COUNTIF(Trade_Log!Y2:Y100,"Y") + COUNTIF(Trade_Log!Z2:Z100,"Revenge")', "val": stats["violations"] + stats["revenge_trades"], "s": 13}, {"ref": "K9", "val": "", "s": 13}, {"ref": "L9", "val": "", "s": 13},
                ]
            },
            10: {
                "height": 18,
                "cells": [
                    {"ref": "B10", "val": "Mathematical Expectancy After Friction", "s": 16}, {"ref": "C10", "val": "", "s": 16}, {"ref": "D10", "val": "", "s": 16},
                    {"ref": "F10", "val": "Quality 5/5 Execution > Quantity", "s": 16}, {"ref": "G10", "val": "", "s": 16}, {"ref": "H10", "val": "", "s": 16},
                    {"ref": "J10", "val": "Zero Tolerance for Rule Violations", "s": 16}, {"ref": "K10", "val": "", "s": 16}, {"ref": "L10", "val": "", "s": 16},
                ]
            },
            12: {
                "height": 24,
                "cells": [
                    {"ref": "B12", "val": "EXECUTION BOUNDARIES", "s": 17}, {"ref": "C12", "val": "", "s": 17}, {"ref": "D12", "val": "", "s": 17},
                    {"ref": "F12", "val": "WIN / LOSS PIE CHART & STATS", "s": 17}, {"ref": "G12", "val": "", "s": 17}, {"ref": "H12", "val": "", "s": 17},
                    {"ref": "J12", "val": "", "s": 17}, {"ref": "K12", "val": "", "s": 17}, {"ref": "L12", "val": "", "s": 17},
                ]
            },
            13: {
                "height": 20,
                "cells": [
                    {"ref": "B13", "val": "Trading Window", "s": 7}, {"ref": "C13", "val": "09:15 to 10:30 AM IST", "s": 9}, {"ref": "D13", "val": "Locked at 10:30", "s": 0},
                    {"ref": "F13", "val": "Wins", "s": 7}, {"ref": "G13", "val": stats["wins"], "s": 5}, {"ref": "H13", "val": f"{stats['win_rate']}%", "s": 3},
                ]
            },
            14: {
                "height": 20,
                "cells": [
                    {"ref": "B14", "val": "Minimum Planned RR", "s": 7}, {"ref": "C14", "val": "≥ 2.2 RR", "s": 9}, {"ref": "D14", "val": "Strict technical target", "s": 0},
                    {"ref": "F14", "val": "Losses", "s": 7}, {"ref": "G14", "val": stats["losses"], "s": 5}, {"ref": "H14", "val": f"{round(100.0 - stats['win_rate'], 1)}%", "s": 3},
                ]
            },
            15: {
                "height": 20,
                "cells": [
                    {"ref": "B15", "val": "Broker Kill Switch", "s": 7}, {"ref": "C15", "val": "ACTIVE / ENFORCED", "s": 9}, {"ref": "D15", "val": "Locks on 2 losses / 2R", "s": 0},
                    {"ref": "F15", "val": "Total Trades", "s": 7}, {"ref": "G15", "val": stats["total_trades"], "s": 5}, {"ref": "H15", "val": "100.0%", "s": 3},
                ]
            },
            16: {
                "height": 20,
                "cells": [
                    {"ref": "B16", "val": "Loss Cooldown", "s": 7}, {"ref": "C16", "val": "30 MINUTES", "s": 9}, {"ref": "D16", "val": "Physical break away", "s": 0},
                    {"ref": "F16", "val": "FYERS Statutory Charges", "s": 7}, {"ref": "G16", "val": stats["total_friction"], "s": 4}, {"ref": "H16", "val": "Verified", "s": 3},
                ]
            }
        }
        
        sheet0_xml = build_sheet_xml(headers=None, rows=[], max_rows=22, col_widths=dash_widths, freeze_panes=False, custom_top_rows=dash_custom_rows, drawing_rId="rId1")
        
        # 1. Quick_Log Sheet
        quick_headers = [
            "Trade_ID","Date","Time","Symbol","Direction","Entry_Price","Stop_Price","Target_Price","Exit_Price","Qty",
            "Planned_RR","FYERS_Costs","Net_PnL","Net_R","Outcome","Valid_5of5"
        ]
        quick_header_map = {1: 1, 2: 24, 3: 24, 4: 24, 5: 24, 6: 24, 7: 24, 8: 24, 9: 24, 10: 24, 11: 25, 12: 25, 13: 25, 14: 25, 15: 25, 16: 25}
        quick_custom_top = {1: {"height": 30, "cells": [{"ref": "A1", "val": "⚡ QUICK LOG: Fill ONLY the Blue Columns (B to J). All calculations, FYERS charges & R-multiples are 100% automated!", "s": 17}]}}
        quick_rows = []
        for t in self.trades:
            target_val = t.get("target_price") or (t["entry_price"] + 2.2*abs(t["entry_price"]-t["stop_price"]) if t["direction"] == "Long" else t["entry_price"] - 2.2*abs(t["entry_price"]-t["stop_price"]))
            quick_rows.append([
                {"val": t["id"], "s": 5},
                {"val": t["date"], "s": 26},
                {"val": t["time"], "s": 26},
                {"val": t["symbol"], "s": 26},
                {"val": t["direction"], "s": 26},
                {"val": t["entry_price"], "s": 27},
                {"val": t["stop_price"], "s": 27},
                {"val": round(target_val, 2), "s": 27},
                {"val": t["exit_price"], "s": 27},
                {"val": t["qty"], "s": 26},
                {"val": t["rr_planned"], "s": 6},
                {"val": t["costs"], "s": 4},
                {"val": t["net_pnl"], "s": 4},
                {"val": t["r_multiple"], "s": 19},
                {"val": t["outcome"], "s": 5},
                {"val": "Y (5/5)" if t["trade_valid"] == "Y" else "N (<2.2R)", "s": 5}
            ])
            
        sheet_quick_xml = build_sheet_xml(headers=quick_headers, rows=quick_rows, max_rows=50, col_widths={1: 16, 2: 13, 3: 11, 4: 12, 5: 11, 6: 13, 7: 13, 8: 13, 9: 13, 10: 10, 11: 13, 12: 14, 13: 14, 14: 12, 15: 11, 16: 14}, freeze_panes=True, custom_top_rows=quick_custom_top, header_style_map=quick_header_map)
        
        # 2. Trade_Log Sheet (Master 32 cols)
        trade_headers = [
            "Trade_ID","Date","Day","Entry_Time","Symbol","Direction","Setup_Name","Scanner_Alert_Time",
            "HTF_Context_OK","Entry_Planned_NoChase","Stop_Defined_Before_Entry","RR_Planned","Risk_Percent",
            "Risk_Amount","Entry_Price","Stop_Price","Exit_Price","Qty","Gross_PnL","Costs","Net_PnL",
            "R_Multiple","Outcome","Checklist_Score_0to5","Rule_Violation","Violation_Type",
            "Emotion_Before_1to10","Emotion_During_1to10","Emotion_After_1to10","Trade_Valid","Lesson","Screenshot_Link"
        ]
        trade_header_map = {1: 1, 2: 24, 3: 25, 4: 24, 5: 24, 6: 24, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 25, 13: 25, 14: 25, 15: 24, 16: 24, 17: 24, 18: 24, 19: 25, 20: 25, 21: 25, 22: 25, 23: 25, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 25, 31: 1, 32: 1}
        trade_rows = []
        for t in self.trades:
            trade_rows.append([
                {"val": t["id"], "s": 5},
                {"val": t["date"], "s": 2},
                {"val": t["day"], "s": 5},
                {"val": t["time"], "s": 5},
                {"val": t["symbol"], "s": 5},
                {"val": t["direction"], "s": 5},
                {"val": t["setup_name"], "s": 0},
                {"val": t["scanner_alert_time"], "s": 5},
                {"val": t["htf_ok"], "s": 5},
                {"val": t["no_chase"], "s": 5},
                {"val": t["stop_defined"], "s": 5},
                {"val": t["rr_planned"], "s": 6},
                {"val": t["risk_percent"], "s": 3},
                {"val": t["risk_amount"], "s": 4},
                {"val": t["entry_price"], "s": 4},
                {"val": t["stop_price"], "s": 4},
                {"val": t["exit_price"], "s": 4},
                {"val": t["qty"], "s": 0},
                {"val": t["gross_pnl"], "s": 4},
                {"val": t["costs"], "s": 4},
                {"val": t["net_pnl"], "s": 4},
                {"val": t["r_multiple"], "s": 6},
                {"val": t["outcome"], "s": 5},
                {"val": t["checklist_score"], "s": 5},
                {"val": t["rule_violation"], "s": 5},
                {"val": t["violation_type"], "s": 5},
                {"val": t["emotion_before"], "s": 5},
                {"val": t["emotion_during"], "s": 5},
                {"val": t["emotion_after"], "s": 5},
                {"val": t["trade_valid"], "s": 5},
                {"val": t["lesson"], "s": 0},
                {"val": t["screenshot_link"], "s": 0}
            ])
            
        trade_widths = {1: 18, 2: 13, 3: 8, 4: 12, 5: 12, 6: 11, 7: 24, 8: 18, 9: 17, 10: 22, 11: 24, 12: 13, 13: 13, 14: 14, 15: 13, 16: 13, 17: 13, 18: 10, 19: 13, 20: 12, 21: 13, 22: 12, 23: 11, 24: 21, 25: 15, 26: 22, 27: 21, 28: 21, 29: 20, 30: 13, 31: 40, 32: 30}
        sheet1_xml = build_sheet_xml(headers=trade_headers, rows=trade_rows, max_rows=50, col_widths=trade_widths, header_style_map=trade_header_map)
        
        # 3. Daily_Scorecard Sheet
        daily_headers = ["Date","Trades_Taken","Max_Trades_Allowed","Losses","Max_Losses_Allowed","Daily_Net_PnL","Daily_R","Checklist_Trades_5of5","Rule_Violations","Adherence_Score_0to5","Adherence_Pct","Hit_Daily_Loss_Limit","Stopped_After_2_Losses","Notes"]
        daily_map = {}
        for t in self.trades:
            d = t["date"]
            if d not in daily_map:
                daily_map[d] = {"trades": 0, "losses": 0, "net_pnl": 0.0, "net_r": 0.0, "c5": 0, "v": 0}
            daily_map[d]["trades"] += 1
            if t["outcome"] == "Loss": daily_map[d]["losses"] += 1
            daily_map[d]["net_pnl"] = round(daily_map[d]["net_pnl"] + t["net_pnl"], 2)
            daily_map[d]["net_r"] = round(daily_map[d]["net_r"] + t["r_multiple"], 2)
            if t["checklist_score"] >= 5: daily_map[d]["c5"] += 1
            if t["rule_violation"] == "Y": daily_map[d]["v"] += 1
            
        daily_rows = []
        for d, vals in daily_map.items():
            daily_rows.append([
                {"val": d, "s": 2},
                {"val": vals["trades"], "s": 5},
                {"val": 2, "s": 5},
                {"val": vals["losses"], "s": 5},
                {"val": 2, "s": 5},
                {"val": vals["net_pnl"], "s": 4},
                {"val": vals["net_r"], "s": 6},
                {"val": vals["c5"], "s": 5},
                {"val": vals["v"], "s": 5},
                {"val": 5, "s": 5},
                {"val": 1.0, "s": 3},
                {"val": "N", "s": 5},
                {"val": "N", "s": 5},
                {"val": "09:15-10:30 window followed strictly.", "s": 0}
            ])
        sheet2_xml = build_sheet_xml(headers=daily_headers, rows=daily_rows, max_rows=35, col_widths={1: 13, 2: 14, 3: 19, 4: 10, 5: 19, 6: 15, 7: 11, 8: 22, 9: 16, 10: 22, 11: 15, 12: 20, 13: 23, 14: 45})
        
        # 4. Weekly_Review Sheet
        weekly_headers = ["Week_Start","Week_End","Trades","Wins","Losses","Win_Rate","Net_PnL","Avg_R","Expectancy_R","Checklist_Adherence_Pct","Violations","Revenge_Trades","Best_Time_Window","Worst_Time_Window","Top_Mistake","Rule_To_Tighten"]
        weekly_rows = [[
            {"val": "2026-10-19", "s": 2}, {"val": "2026-10-23", "s": 2},
            {"val": stats["total_trades"], "s": 5}, {"val": stats["wins"], "s": 5}, {"val": stats["losses"], "s": 5},
            {"val": stats["win_rate"] / 100.0, "s": 3}, {"val": stats["net_pnl"], "s": 4}, {"val": stats["avg_r"], "s": 6},
            {"val": stats["avg_r"], "s": 6}, {"val": stats["adherence_pct"] / 100.0, "s": 3},
            {"val": stats["violations"], "s": 5}, {"val": stats["revenge_trades"], "s": 5},
            {"val": "09:15-10:00", "s": 5}, {"val": "None", "s": 5},
            {"val": "Clean execution inside window", "s": 0}, {"val": "Maintain RR >= 2.2 and 30m cooldown", "s": 0}
        ]]
        sheet3_xml = build_sheet_xml(headers=weekly_headers, rows=weekly_rows, max_rows=10, col_widths={1: 13, 2: 13, 3: 10, 4: 10, 5: 10, 6: 12, 7: 14, 8: 10, 9: 14, 10: 23, 11: 12, 12: 16, 13: 18, 14: 18, 15: 35, 16: 35})
        
        # 5. Journal Sheet
        journal_headers = ["Date","Trade_ID","Symbol","Setup","What_I_Saw","Why_I_Entered","Emotion_Before","Emotion_During","Emotion_After","Rule_Violation","What_I_Did_Well","What_Ill_Do_Differently","Screenshot_Link"]
        journal_rows = []
        for t in self.trades:
            journal_rows.append([
                {"val": t["date"], "s": 2},
                {"val": t["id"], "s": 5},
                {"val": t["symbol"], "s": 5},
                {"val": t["setup_name"], "s": 0},
                {"val": f"Higher timeframe alignment inside 09:15-10:30 window.", "s": 0},
                {"val": f"Setup confirmed. Limit order filled at planned level.", "s": 0},
                {"val": t["emotion_before"], "s": 5},
                {"val": t["emotion_during"], "s": 5},
                {"val": t["emotion_after"], "s": 5},
                {"val": t["rule_violation"], "s": 5},
                {"val": "Followed rules, limit order, passive target execution.", "s": 0},
                {"val": "Continue strictly enforcing 30-min cooldown after loss.", "s": 0},
                {"val": t["screenshot_link"], "s": 0}
            ])
        sheet4_xml = build_sheet_xml(headers=journal_headers, rows=journal_rows, max_rows=30, col_widths={1: 13, 2: 18, 3: 12, 4: 22, 5: 35, 6: 35, 7: 15, 8: 15, 9: 15, 10: 15, 11: 35, 12: 35, 13: 30})
        
        # Chart XML
        chart1_pie_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<c:chartSpace xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <c:chart>
    <c:title><c:tx><c:rich><a:bodyPr/><a:lstStyle/><a:p><a:pPr><a:defRPr b="1" sz="1100"><a:solidFill><a:srgbClr val="0F172A"/></a:solidFill></a:defRPr></a:pPr><a:r><a:t>Win / Loss Distribution</a:t></a:r></a:p></c:rich></c:tx><c:overlay val="0"/></c:title>
    <c:plotArea>
      <c:layout/>
      <c:pieChart>
        <c:varyColors val="1"/>
        <c:ser>
          <c:idx val="0"/><c:order val="0"/>
          <c:tx><c:v>Outcomes</c:v></c:tx>
          <c:cat><c:strLit><c:ptCount val="2"/><c:pt idx="0"><c:v>Wins ({stats['win_rate']}%)</c:v></c:pt><c:pt idx="1"><c:v>Losses ({round(100.0 - stats['win_rate'], 1)}%)</c:v></c:pt></c:strLit></c:cat>
          <c:val><c:numLit><c:ptCount val="2"/><c:pt idx="0"><c:v>{stats['wins']}</c:v></c:pt><c:pt idx="1"><c:v>{stats['losses']}</c:v></c:pt></c:numLit></c:val>
        </c:ser>
      </c:pieChart>
    </c:plotArea>
    <c:legend><c:legendPos val="b"/><c:overlay val="0"/></c:legend>
  </c:chart>
</c:chartSpace>"""

        drawing_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<xdr:wsDr xmlns:xdr="http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <xdr:twoCellAnchor>
    <xdr:from><xdr:col>8</xdr:col><xdr:colOff>50000</xdr:colOff><xdr:row>12</xdr:row><xdr:rowOff>50000</xdr:rowOff></xdr:from>
    <xdr:to><xdr:col>12</xdr:col><xdr:colOff>50000</xdr:colOff><xdr:row>19</xdr:row><xdr:rowOff>150000</xdr:rowOff></xdr:to>
    <xdr:graphicFrame macro=""><xdr:nvGraphicFramePr><xdr:cNvPr id="2" name="PieChart1"/><xdr:cNvGraphicFramePr/></xdr:nvGraphicFramePr><xdr:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/></xdr:xfrm><a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/chart"><c:chart xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart" r:id="rId1"/></a:graphicData></a:graphic></xdr:graphicFrame><xdr:clientData/>
  </xdr:twoCellAnchor>
</xdr:wsDr>"""

        drawing_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/chart" Target="../charts/chart1.xml"/>
</Relationships>"""

        sheet1_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/drawing" Target="../drawings/drawing1.xml"/>
</Relationships>"""

        content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet3.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet4.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet5.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet6.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
  <Override PartName="/xl/sharedStrings.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"/>
  <Override PartName="/xl/drawings/drawing1.xml" ContentType="application/vnd.openxmlformats-officedocument.drawing+xml"/>
  <Override PartName="/xl/charts/chart1.xml" ContentType="application/vnd.openxmlformats-officedocument.drawingml.chart+xml"/>
</Types>"""

        root_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>"""

        wb_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet3.xml"/>
  <Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet4.xml"/>
  <Relationship Id="rId5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet5.xml"/>
  <Relationship Id="rId6" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet6.xml"/>
  <Relationship Id="rId7" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId8" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings" Target="sharedStrings.xml"/>
</Relationships>"""

        workbook_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="Dashboard" sheetId="1" r:id="rId1"/>
    <sheet name="Quick_Log" sheetId="2" r:id="rId2"/>
    <sheet name="Trade_Log" sheetId="3" r:id="rId3"/>
    <sheet name="Daily_Scorecard" sheetId="4" r:id="rId4"/>
    <sheet name="Weekly_Review" sheetId="5" r:id="rId5"/>
    <sheet name="Journal" sheetId="6" r:id="rId6"/>
  </sheets>
</workbook>"""

        sst_xml = sst.to_xml()
        os.makedirs(os.path.dirname(XLSX_PATH), exist_ok=True)
        with zipfile.ZipFile(XLSX_PATH, 'w', zipfile.ZIP_DEFLATED) as z:
            z.writestr('[Content_Types].xml', content_types)
            z.writestr('_rels/.rels', root_rels)
            z.writestr('xl/_rels/workbook.xml.rels', wb_rels)
            z.writestr('xl/workbook.xml', workbook_xml)
            z.writestr('xl/styles.xml', styles_xml)
            z.writestr('xl/sharedStrings.xml', sst_xml)
            z.writestr('xl/worksheets/_rels/sheet1.xml.rels', sheet1_rels)
            z.writestr('xl/worksheets/sheet1.xml', sheet0_xml) # Dashboard
            z.writestr('xl/worksheets/sheet2.xml', sheet_quick_xml) # Quick_Log
            z.writestr('xl/worksheets/sheet3.xml', sheet1_xml) # Trade_Log
            z.writestr('xl/worksheets/sheet4.xml', sheet2_xml) # Daily_Scorecard
            z.writestr('xl/worksheets/sheet5.xml', sheet3_xml) # Weekly_Review
            z.writestr('xl/worksheets/sheet6.xml', sheet4_xml) # Journal
            z.writestr('xl/drawings/drawing1.xml', drawing_xml)
            z.writestr('xl/drawings/_rels/drawing1.xml.rels', drawing_rels)
            z.writestr('xl/charts/chart1.xml', chart1_pie_xml)

manager = ExcelTradeManager()
