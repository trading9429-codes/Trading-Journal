with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/excel_service.py", "r") as f:
    text = f.read()

text = text.replace(
    '{"ref": "B2", "val": "NSE Equities 1m | Window: 09:15–10:30 AM IST | Risk: 0.25%–0.50% | Min RR: ≥ 2.2 | FYERS Brokerage & Taxes", "s": 11}',
    '{"ref": "B2", "val": "NSE Equities 1m | Window: 09:15–10:30 AM IST | Starting Capital: ₹2,00,000 | Risk: 0.25% (₹500) | Min RR: ≥ 2.2 | FYERS Charges", "s": 11}'
)
text = text.replace(
    '{"ref": "B4", "val": "CURRENT RESET STATUS", "s": 12},',
    '{"ref": "B4", "val": "STARTING & CURRENT CAPITAL", "s": 12},'
)
text = text.replace(
    '{"ref": "B5", "val": "PHASE 1 (DAYS 1–3)", "s": 13},',
    '{"ref": "B5", "val": f"₹{200000 + stats[\'net_pnl\']:,.2f} ({((stats[\'net_pnl\']/200000)*100):+.2f}%)", "s": 13},'
)
text = text.replace(
    '{"ref": "B6", "val": "Max 2 Trades/Day | Risk: 0.25% | Stop: 2 Losses", "s": 16},',
    '{"ref": "B6", "val": "Starting Capital: ₹2,00,000 | Risk: ₹500 (0.25%)", "s": 16},'
)

with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/excel_service.py", "w") as f:
    f.write(text)

print("Updated excel_service.py.")
