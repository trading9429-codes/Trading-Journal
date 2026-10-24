with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/excel_service.py", "r") as f:
    text = f.read()

# Replace DEFAULT_TRADES
old_defaults = """DEFAULT_TRADES = [
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
        "rr_planned": 2.20,
        "risk_percent": 0.0025,
        "risk_amount": 500.00,
        "entry_price": 2500.00,
        "stop_price": 2495.00,
        "exit_price": 2511.00,
        "qty": 100,
        "gross_pnl": 1100.00,
        "costs": 551.21,
        "net_pnl": 548.79,
        "r_multiple": 1.10,
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
        "rr_planned": 2.20,
        "risk_percent": 0.0025,
        "risk_amount": 500.00,
        "entry_price": 3500.00,
        "stop_price": 3510.00,
        "exit_price": 3510.00,
        "qty": 50,
        "gross_pnl": -500.00,
        "costs": 385.55,
        "net_pnl": -885.55,
        "r_multiple": -1.77,
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
        "rr_planned": 2.20,
        "risk_percent": 0.0025,
        "risk_amount": 500.00,
        "entry_price": 1450.00,
        "stop_price": 1445.00,
        "exit_price": 1461.00,
        "qty": 100,
        "gross_pnl": 1100.00,
        "costs": 320.21,
        "net_pnl": 779.79,
        "r_multiple": 1.56,
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
]"""

new_defaults = """def calculate_fyers_charges(entry: float, exit_p: float, qty: int, direction: str):
    \"\"\"
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
    \"\"\"
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
]"""

text = text.replace(old_defaults, new_defaults)

# Update add_trade
old_add_trade = """        # Calculations
        risk_per_share = abs(entry - stop)
        risk_amount = round(risk_per_share * qty, 2)
        reward_per_share = (exit_p - entry) if direction == "Long" else (entry - exit_p)
        rr_planned = round(abs(exit_p - entry) / risk_per_share, 2) if risk_per_share > 0 else 0.0
        
        turnover = (entry * qty) + (exit_p * qty)
        costs = round(0.0011 * turnover, 2) # 0.11% statutory turnover friction
        gross_pnl = round(reward_per_share * qty, 2)
        net_pnl = round(gross_pnl - costs, 2)
        r_multiple = round(net_pnl / risk_amount, 2) if risk_amount > 0 else 0.0
        outcome = "Win" if net_pnl > 0 else ("Loss" if net_pnl < 0 else "BE")
        
        checklist_score = int(payload.get("checklist_score", 5))
        rule_violation = "Y" if payload.get("rule_violation") in [True, "Y", "y"] else "N"
        violation_type = str(payload.get("violation_type") or "None")
        
        trade_valid = "Y" if (checklist_score >= 5 and rule_violation == "N" and rr_planned >= 2.2) else "N" """

new_add_trade = """        target = float(payload.get("target_price", 0)) if payload.get("target_price") else 0.0
        
        # Risk per share
        risk_per_share = abs(entry - stop)
        risk_amount = round(risk_per_share * qty, 2)
        
        # Planned RR (Target Price based: |Target - Entry| / |Entry - Stop|)
        if target > 0 and risk_per_share > 0:
            planned_reward_per_share = abs(target - entry)
            rr_planned = round(planned_reward_per_share / risk_per_share, 2)
        elif payload.get("rr_planned"):
            rr_planned = float(payload.get("rr_planned"))
        elif risk_per_share > 0:
            planned_reward_per_share = abs(exit_p - entry)
            rr_planned = round(planned_reward_per_share / risk_per_share, 2)
        else:
            rr_planned = 0.0
            
        # Realized Gross P&L
        realized_reward_per_share = (exit_p - entry) if direction == "Long" else (entry - exit_p)
        gross_pnl = round(realized_reward_per_share * qty, 2)
        
        # FYERS Exact Intraday Statutory Charges
        charges = calculate_fyers_charges(entry, exit_p, qty, direction)
        costs = charges["total_costs"]
        net_pnl = round(gross_pnl - costs, 2)
        r_multiple = round(net_pnl / risk_amount, 2) if risk_amount > 0 else 0.0
        outcome = "Win" if net_pnl > 0 else ("Loss" if net_pnl < 0 else "BE")
        
        checklist_score = int(payload.get("checklist_score", 5))
        rule_violation = "Y" if payload.get("rule_violation") in [True, "Y", "y"] else "N"
        violation_type = str(payload.get("violation_type") or "None")
        
        # Hard Rule: Planned RR must be >= 2.2 and 5/5 checklist
        trade_valid = "Y" if (checklist_score >= 5 and rule_violation == "N" and rr_planned >= 2.2) else "N" """

text = text.replace(old_add_trade, new_add_trade)

# Also add target_price to new_trade dict
text = text.replace(
    '"stop_defined": payload.get("stop_defined", "Y"),\n            "rr_planned": rr_planned,',
    '"stop_defined": payload.get("stop_defined", "Y"),\n            "target_price": target if target > 0 else (entry + 2.2*risk_per_share if direction == "Long" else entry - 2.2*risk_per_share),\n            "rr_planned": rr_planned,'
)

# In sync_excel_file: update friction descriptions
text = text.replace(
    '"B2", "val": "NSE Equities 1m | Window: 09:15–10:30 AM IST | Risk: 0.25%–0.50% | Min RR: 2.2 | Friction: 0.11% Turnover"',
    '"B2", "val": "NSE Equities 1m | Window: 09:15–10:30 AM IST | Risk: 0.25%–0.50% | Min RR: ≥ 2.2 | FYERS Brokerage & Taxes"'
)
text = text.replace(
    '"F6", "val": "Net of 0.11% Turnover Friction & Taxes"',
    '"F6", "val": "Net of FYERS Brokerage & Statutory Taxes (STT, GST, Exch, SEBI, Stamp)"'
)
text = text.replace(
    '{"ref": "F16", "val": "Turnover Friction (0.11%)", "s": 7}, {"ref": "G16", "val": stats["total_friction"], "s": 4}, {"ref": "H16", "val": "0.11%", "s": 3},',
    '{"ref": "F16", "val": "FYERS Statutory Charges", "s": 7}, {"ref": "G16", "val": stats["total_friction"], "s": 4}, {"ref": "H16", "val": "Verified", "s": 3},'
)

# Update Quick_Log in sync_excel_file
old_sync_quick = """        # 1. Quick_Log Sheet
        quick_headers = [
            "Trade_ID","Date","Time","Symbol","Direction","Entry_Price","Stop_Price","Exit_Price","Qty",
            "Target_RR","Friction_0.11%","Net_PnL","Net_R","Outcome","Valid_5of5"
        ]
        quick_header_map = {1: 1, 2: 24, 3: 24, 4: 24, 5: 24, 6: 24, 7: 24, 8: 24, 9: 24, 10: 25, 11: 25, 12: 25, 13: 25, 14: 25, 15: 25}
        quick_custom_top = {1: {"height": 30, "cells": [{"ref": "A1", "val": "⚡ QUICK LOG: Fill ONLY the Blue Columns (B to I). All calculations, friction & R-multiples are 100% automated!", "s": 17}]}}
        quick_rows = []
        for t in self.trades:
            quick_rows.append([
                {"val": t["id"], "s": 5},
                {"val": t["date"], "s": 26},
                {"val": t["time"], "s": 26},
                {"val": t["symbol"], "s": 26},
                {"val": t["direction"], "s": 26},
                {"val": t["entry_price"], "s": 27},
                {"val": t["stop_price"], "s": 27},
                {"val": t["exit_price"], "s": 27},
                {"val": t["qty"], "s": 26},
                {"val": t["rr_planned"], "s": 6},
                {"val": t["costs"], "s": 4},
                {"val": t["net_pnl"], "s": 4},
                {"val": t["r_multiple"], "s": 19},
                {"val": t["outcome"], "s": 5},
                {"val": "Y (5/5)" if t["trade_valid"] == "Y" else "N (<2.2R)", "s": 5}
            ])
            
        sheet_quick_xml = build_sheet_xml(headers=quick_headers, rows=quick_rows, max_rows=50, col_widths={1: 16, 2: 13, 3: 11, 4: 12, 5: 11, 6: 13, 7: 13, 8: 13, 9: 10, 10: 13, 11: 14, 12: 14, 13: 12, 14: 11, 15: 14}, freeze_panes=True, custom_top_rows=quick_custom_top, header_style_map=quick_header_map)"""

new_sync_quick = """        # 1. Quick_Log Sheet
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
            
        sheet_quick_xml = build_sheet_xml(headers=quick_headers, rows=quick_rows, max_rows=50, col_widths={1: 16, 2: 13, 3: 11, 4: 12, 5: 11, 6: 13, 7: 13, 8: 13, 9: 13, 10: 10, 11: 13, 12: 14, 13: 14, 14: 12, 15: 11, 16: 14}, freeze_panes=True, custom_top_rows=quick_custom_top, header_style_map=quick_header_map)"""

text = text.replace(old_sync_quick, new_sync_quick)

with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/excel_service.py", "w") as f:
    f.write(text)

print("Updated excel_service.py successfully.")
