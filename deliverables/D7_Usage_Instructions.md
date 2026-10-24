# Usage Instructions (D7)

**System:** Trader Execution Reset System  
**Version:** 1.0 (Client Calibrated)  
**Trading Window:** 09:15 to 10:30 AM IST  
**Minimum RR:** ≥ 2.2 RR  
**Cost Model:** FYERS Equity Intraday Statutory Charges (Brokerage + STT + Exch + SEBI + Stamp + GST)  
**Length:** $\le 1$ Page  

---

## 1. File Catalog

* `D1_30_Day_Reset_Plan.md`: Your 30-day roadmap. Contains phase progression, volume caps, risk limits, and graduation criteria.
* `D2_Daily_Checklist.md`: Your operational gate. Contains pre-market setup, verbatim 5-point checklist, and printable daily execution sheet.
* `D3_Tracking_Spreadsheet.xlsx`: Your primary data engine (4 tabs: `Trade_Log`, `Daily_Scorecard`, `Weekly_Review`, `Journal`).
* `D4_Trade_Journal_Template.md`: Markdown companion for individual trade documentation and emotional reflection.
* `D5_Weekly_Review_Template.md`: Weekend governance questionnaire and review protocol.
* `D6_Quick_Reference_Card.md`: One-page printable desk card for real-time discipline enforcement.

---

## 2. Daily Operating Routine

### A. Pre-Market (09:00 to 09:15 AM)
1. Print a physical copy of the checklist block from `D2_Daily_Checklist.md` (or open your digital tracker).
2. Confirm your broker's hard daily loss kill switch is enabled.
3. Lock your daily trading window to **09:15 to 10:30 AM IST**.
4. Rate emotional readiness. If scored $<4/5$, keep the trading terminal closed today.

### B. Intraday Execution (09:15 to 10:30 AM IST)
1. 1-minute scanner alerts a candidate ticker. **Do not click buy/sell.**
2. Evaluate against the **5-Point Checklist** in `D2_Daily_Checklist.md` or `D6_Quick_Reference_Card.md`.
3. Confirm planned structural Risk-to-Reward is **$\ge 2.2\text{ RR}$**.
4. If all 5 boxes are checked (5/5), submit a **Limit Order** at your planned level with an immediate hard stop.
5. If stopped out:
   * 1st Loss: Enforce mandatory 30-minute cooldown away from the desk.
   * 2nd Loss: Hard stop. Broker kill switch locks the platform. Day is terminated.
6. At 10:30 AM sharp: Close the trading platform. No trades allowed past 10:30 AM.

### C. Post-Market Close (10:30 to 10:45 AM)
1. Open `D3_Tracking_Spreadsheet.xlsx` $\rightarrow$ **Trade_Log** tab.
2. Log trade execution details (Columns A to AF). Formulas in C, N, S, T (FYERS statutory charges), U, V, W, AD calculate automatically.
3. Switch to the **Journal** tab. Record observations, emotions (1–10 scale), and lessons.
4. Switch to the **Daily_Scorecard** tab. Enter today's date in Column A and your Adherence Score (0–5) in Column J.

---

## 3. Weekend Routine (Every Saturday / Sunday)

1. Open `D3_Tracking_Spreadsheet.xlsx` $\rightarrow$ **Weekly_Review** tab.
2. Enter the week's start and end dates in Columns A and B. Review the automated metrics.
3. Open `D5_Weekly_Review_Template.md` and answer the 6 Weekend Review Questions in writing.
4. **Gate Evaluation:**
   * If adherence was $\ge 95\%$ and week's pass condition met: Advance to the next phase in `D1_30_Day_Reset_Plan.md`.
   * If pass condition failed: Repeat the current week.
   * If adherence was $<90\%$: Trade micro size (0.25%) or paper trade the following week.

---

## 4. First-Time Spreadsheet Setup

The spreadsheet contains pre-loaded example rows clearly labeled `[EXAMPLE]`. Before logging your first real trade:
1. Verify formulas are active (Cost formula in Column T automatically computes exact FYERS statutory charges including brokerage cap, STT on sell, GST, and turnover levies).
2. Highlight and delete the seed values in Rows 2–4 of `Trade_Log`, Rows 2–3 of `Daily_Scorecard`, Row 2 of `Weekly_Review`, and Rows 2–3 of `Journal`.
3. Keep row formulas intact for dragging down.
