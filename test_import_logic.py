import csv

sample_path = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/sample_trades_import.csv"
with open(sample_path, "r") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Sample CSV read successfully. Found {len(rows)} rows.")
for r in rows[:3]:
    print(r["Trade_ID"], r["Date"], r["Symbol"], r["Direction"], r["Entry_Price"], r["Exit_Price"])
