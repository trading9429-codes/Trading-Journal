import re

# 1. Update D1_30_Day_Reset_Plan.md
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D1_30_Day_Reset_Plan.md", "r") as f:
    d1 = f.read()

d1 = d1.replace(
    "**Cost Structure:** 0.11% of total turnover",
    "**Cost Structure:** FYERS Statutory Intraday Charges (Brokerage + STT + Exch + SEBI + Stamp + GST)"
)
d1 = d1.replace(
    "(0.11% of turnover: brokerage, STT, exchange turnover fees, GST, stamp duty)",
    "(FYERS equity intraday statutory formula: ₹20 cap brokerage, 0.025% STT on sell, 0.00297% exch, SEBI, stamp duty, 18% GST)"
)
d1 = d1.replace(
    "(automated in column T at 0.11% of turnover)",
    "(automated in column T using exact FYERS statutory formulas)"
)
d1 = d1.replace(
    "($Avg_R > 0$ after 0.11% turnover costs)",
    "($Avg_R > 0$ after FYERS statutory transaction friction)"
)
d1 = d1.replace(
    "after factoring in 0.11% turnover friction and slippage",
    "after factoring in FYERS statutory transaction friction"
)
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D1_30_Day_Reset_Plan.md", "w") as f:
    f.write(d1)

# 2. Update D2_Daily_Checklist.md
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D2_Daily_Checklist.md", "r") as f:
    d2 = f.read()
d2 = d2.replace(
    "turnover costs (0.11%)",
    "FYERS statutory transaction charges"
)
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D2_Daily_Checklist.md", "w") as f:
    f.write(d2)

# 3. Update D4_Trade_Journal_Template.md
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D4_Trade_Journal_Template.md", "r") as f:
    d4 = f.read()
d4 = d4.replace(
    "**Cost Model:** 0.11% of turnover (₹0.0011 × Total Value Transacted)",
    "**Cost Model:** FYERS Statutory Intraday Charges (Brokerage, STT 0.025%, Exch 0.00297%, SEBI, Stamp, GST 18%)"
)
d4 = d4.replace(
    "* **Costs (0.11% Turnover):** ₹ [0.0011 × (Entry Turnover + Exit Turnover)]",
    "* **Costs (FYERS Statutory Charges):** ₹ [Brokerage + STT + Exch + SEBI + Stamp + GST]"
)
d4 = d4.replace(
    "### Example Row 1: Winning Trade (2.2 RR Hit, Net of 0.11% Friction)",
    "### Example Row 1: Winning Trade (2.2 RR Hit, Net of FYERS Friction)"
)
d4 = d4.replace("* **Costs (0.11%):** ₹551.21", "* **Costs (FYERS):** ₹135.10")
d4 = d4.replace("* **Net P&L:** ₹548.79", "* **Net P&L:** ₹964.90")
d4 = d4.replace("* **Realized R-Multiple:** +1.10 R", "* **Realized R-Multiple:** +1.93 R")

d4 = d4.replace("* **Costs (0.11%):** ₹385.55", "* **Costs (FYERS):** ₹108.54")
d4 = d4.replace("* **Net P&L:** -₹885.55", "* **Net P&L:** -₹608.54")
d4 = d4.replace("* **Realized R-Multiple:** -1.77 R", "* **Realized R-Multiple:** -1.22 R")

with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D4_Trade_Journal_Template.md", "w") as f:
    f.write(d4)

# 4. Update D5_Weekly_Review_Template.md
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D5_Weekly_Review_Template.md", "r") as f:
    d5 = f.read()
d5 = d5.replace(
    "**Cost Model:** 0.11% of turnover (₹0.0011 × Total Value Transacted)",
    "**Cost Model:** FYERS Statutory Intraday Charges (Brokerage, STT, Exch, SEBI, Stamp, GST)"
)
d5 = d5.replace("Net P&L after 0.11% turnover friction", "Net P&L after FYERS statutory transaction friction")
d5 = d5.replace("Total transaction friction paid (0.11% turnover)", "Total transaction friction paid (FYERS charges)")
d5 = d5.replace("after 0.11% turnover costs", "after FYERS statutory charges")
d5 = d5.replace("(automated 0.11%)", "(automated FYERS statutory charges)")
d5 = d5.replace("after 0.11% turnover friction", "after FYERS statutory charges")
d5 = d5.replace("After 0.11% Friction", "After FYERS Statutory Charges")
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D5_Weekly_Review_Template.md", "w") as f:
    f.write(d5)

# 5. Update D6_Quick_Reference_Card.md
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D6_Quick_Reference_Card.md", "r") as f:
    d6 = f.read()
d6 = d6.replace(
    "* **Friction Awareness:** Costs equal 0.11% of turnover. Overtrading destroys edge.",
    "* **Friction Awareness:** FYERS statutory friction (Brokerage, STT, GST, Exch) penalizes overtrading. Overtrading destroys edge."
)
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D6_Quick_Reference_Card.md", "w") as f:
    f.write(d6)

# 6. Update D7_Usage_Instructions.md
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D7_Usage_Instructions.md", "r") as f:
    d7 = f.read()
d7 = d7.replace(
    "**Cost Model:** 0.11% of turnover",
    "**Cost Model:** FYERS Equity Intraday Statutory Charges (Brokerage + STT + Exch + SEBI + Stamp + GST)"
)
d7 = d7.replace(
    "Formulas in C, N, S, T (0.11% turnover costs), U, V, W, AD calculate automatically.",
    "Formulas in C, N, S, T (FYERS statutory charges), U, V, W, AD calculate automatically."
)
d7 = d7.replace(
    "(Cost formula in Column T automatically computes `=ROUND(0.0011*(Entry*Qty + Exit*Qty), 2)`)",
    "(Cost formula in Column T automatically computes exact FYERS statutory charges including brokerage cap, STT on sell, GST, and turnover levies)"
)
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D7_Usage_Instructions.md", "w") as f:
    f.write(d7)

# 7. Update README.md
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/README.md", "r") as f:
    readme = f.read()
readme = readme.replace(
    "**Cost Model:** 0.11% of turnover (₹0.0011 × Total Value Transacted)",
    "**Cost Model:** FYERS Statutory Intraday Equity Charges (Brokerage + STT + Exch + SEBI + Stamp + GST)"
)
readme = readme.replace(
    "0.11% turnover friction calculator",
    "FYERS statutory intraday charges calculator & target-based Planned RR validator"
)
readme = readme.replace(
    "automated 0.11% turnover friction",
    "automated FYERS statutory charges"
)
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/README.md", "w") as f:
    f.write(readme)

print("Updated all markdown deliverables successfully.")
