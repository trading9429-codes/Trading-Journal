# Trade Journal Template & Protocol (D4)

**System:** Trader Execution Reset System  
**Version:** 2.0 (Institutional Calibrated)  
**Trading Window:** 09:15 to 10:30 AM IST  
**Minimum Technical RR:** ≥ 2.2 RR  
**Cost Model:** FYERS Statutory Intraday Charges (Brokerage ₹20 cap, STT 0.025% on sell, Exch 0.00297%, SEBI, Stamp, GST 18%)  

---

## 1. Overview & Operational Rule

You must journal every executed trade **immediately after the position is closed**. Do not batch journal entries at the end of the day; emotional recall degrades rapidly within 15 minutes of an exit.

In the companion spreadsheet [`D3_Tracking_Spreadsheet.xlsx`](file:///home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D3_Tracking_Spreadsheet.xlsx) and the Web Command Center ([`Dashboard.html`](file:///home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html)), journal reflections are permanently stored with attached chart screenshots and excursion metrics.

---

## 2. Comprehensive Trade Schema (`Journal`)

| Field | Data Type / Validation | Description |
|---|---|---|
| **Date & Time** | `YYYY-MM-DD` & `HH:MM` | Timestamp strictly within 09:15–10:30 AM IST |
| **Trade_ID & Symbol** | Text | e.g. `T-004` & `RELIANCE` |
| **Setup Name** | Dropdown | `1m Pullback to 9EMA`, `Opening Range Breakout (ORB)`, `VWAP Reversal`, `Breakout + Retest` |
| **Planned Entry / SL / TP** | Number (2 decimals) | Must meet planned structural $\text{RR} \ge 2.2$ |
| **MAE Price** | Number (2 decimals) | **Maximum Adverse Excursion:** Lowest price reached during Long / Highest during Short |
| **MFE Price** | Number (2 decimals) | **Maximum Favorable Excursion:** Peak price expansion before exit |
| **Exit Efficiency %** | Formula | $(\text{Exit} - \text{Entry}) / (\text{MFE} - \text{Entry}) \times 100$ |
| **FYERS Costs** | INR (₹) | Total statutory tax friction (Brokerage + STT + Exch + SEBI + Stamp + GST) |
| **Net Realized R** | Decimal | Realized net multiple after all statutory costs |
| **Emotion (Before/During/After)** | Integer `1–10` | 1–3 Calm, 4–6 Alert, >6 Tilt (Trade strictly barred if Before >6) |
| **Rule Adherence (5/5)** | Boolean / Checklist | Window, Setup, RR $\ge 2.2$, No chase, Calm mind |
| **Chart Screenshot** | Embedded Base64 / URL | 1-minute execution chart with entry candle, stop level, and 9EMA |

---

## 3. Emotional State Calibration Scale (1 to 10)

* **1–2 (Optimal / Grounded):** Calm, objective, indifferent to win or loss. Mindful of process.
* **3–4 (Alert / Controlled):** Normal slight tension, focused on execution, strictly respecting limits.
* **5–6 (Elevated / Agitated):** Impatience building, micro-checking 1-second candles, fear of missing the move.
* **7–8 (High Danger / Reactive):** Heart rate elevated, impulse to increase size, urge to move stop loss, frustration.
* **9–10 (Compulsive / Tilt):** Full revenge state, market order smashing, total disregard for rules.

> **Non-Negotiable Hard Gate:** If `Emotion_Before` is rated **> 6**, trade entry is strictly prohibited. Step away immediately.

---

## 4. MAE & MFE Excursion Leak Analysis

Every trade journal must audit two structural excursion questions:
1. **Was my Stop Loss too wide or too tight? (MAE Audit)**
   * $\text{MAE (in R)} = \frac{|\text{Entry} - \text{MAE Price}|}{|\text{Entry} - \text{Stop Price}|}$
   * *Ideal:* $0.20\text{R} \le \text{MAE} \le 0.50\text{R}$. If $\text{MAE} > 0.85\text{R}$, entry timing was late or stop was nearly hunted.
2. **Did I leave money on the table out of fear? (MFE Audit)**
   * $\text{Exit Efficiency} = \frac{\text{Net Realized R}}{\text{MFE Potential R}} \times 100$
   * *Target:* $\ge 70\%$. If $<50\%$, panic exit occurred before structural target was reached.

---

## 5. Copy-Paste Markdown Journal Template

```markdown
### Trade Entry: [Trade_ID] — [Date] — [Symbol]
* **Trading Window Check:** Logged at [HH:MM] IST (Strictly 09:15–10:30) `[ PASS / FAIL ]`
* **Setup Name:** [e.g. 1m Pullback to 9EMA]
* **Execution Direction:** [ LONG / SHORT ]
* **Entry:** ₹[0.00] | **Stop:** ₹[0.00] | **Target:** ₹[0.00] | **Planned RR:** [e.g. 2.4 RR]
* **MAE Price (Worst Drawdown):** ₹[0.00] ([0.00]R)
* **MFE Price (Peak Potential):** ₹[0.00] ([0.00]R)
* **Exit Efficiency:** [0.0]% captured
* **FYERS Statutory Costs:** ₹[0.00] (Brokerage: ₹___, STT: ₹___, GST: ₹___)
* **Net P&L:** ₹[0.00] | **Net R-Multiple:** [0.00]R

#### Psychology & Mindset:
* **Emotion Before Entry (1–10):** [ ] (Must be ≤ 6)
* **Emotion During Trade (1–10):** [ ]
* **Emotion After Exit (1–10):** [ ]
* **Mandatory 30-Min Loss Cooldown:** [ N/A / Honored in full away from screens ]

#### 5-Point Rule Checklist Verification:
- [x] 1. Inside 09:15–10:30 AM IST window
- [x] 2. Structural planned RR ≥ 2.2
- [x] 3. Hard limit order stationed (no market chasing)
- [x] 4. Hard stop placed at market structure (no widening)
- [x] 5. Calm emotional mindset (<6/10 urgency)

#### Post-Trade Reflection:
* **What worked well:** [Observed 9EMA bounce, waited for candle close]
* **What could be improved:** [Did not panic when price pulled back 0.3R into entry]
* **Key Lesson:** [Single actionable rule refinement]
* **Chart Screenshot Attached:** [ Yes / No ]
```
