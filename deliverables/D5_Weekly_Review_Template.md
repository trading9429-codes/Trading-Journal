# Weekly Review Template & Protocol (D5)

**System:** Trader Execution Reset System  
**Version:** 2.0 (Institutional Calibrated)  
**Trading Window:** 09:15 to 10:30 AM IST  
**Minimum Technical RR:** ≥ 2.2 RR  
**Cost Model:** FYERS Statutory Intraday Charges (Brokerage, STT, Exch, SEBI, Stamp, GST)  

---

## 1. Objective & Timing

The Weekly Review is your mandatory governance audit. It must be conducted every weekend (Saturday or Sunday) before the markets open on Monday.

* **Target Adherence:** $\ge 95\%$ checklist adherence.
* **Underperformance Penalty:** If adherence is $<90\%$, you are strictly demoted to paper trading or micro sizing (0.25% maximum risk) for the entire upcoming week.
* **Graduation Gate:** You must maintain $\ge 95\%$ adherence across the current 30-day reset phase with positive net expectancy before unlocking increased sizing or trade caps.

---

## 2. Quantitative Weekly Audit Scorecard

Fill out these verified metrics calculated by the Command Center ([`Dashboard.html`](file:///home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html)) or spreadsheet:

| Metric | Target | Actual This Week | Status |
|---|---|---|---|
| **Total Trades Taken** | $\le 2$ trades/day ($\le 10$ weekly) | _____ | `[ PASS / FAIL ]` |
| **5/5 Rule Adherence Rate** | $\ge 95\%$ | _____% | `[ PASS / FAIL ]` |
| **Gross P&L vs Net P&L** | Positive Net P&L | ₹_____ (Net) | `[ PASS / FAIL ]` |
| **FYERS Cost Drag %** | $< 15\%$ of Gross Profits | _____% | `[ PASS / FAIL ]` |
| **Average Net Expectancy** | $\ge +0.40\text{R}$ / trade | _____R | `[ PASS / FAIL ]` |
| **Avg MAE (Adverse Drawdown)** | $0.25\text{R} \le \text{MAE} \le 0.50\text{R}$ | _____R | `[ PASS / FAIL ]` |
| **Exit Efficiency %** | $\ge 70\%$ of MFE Potential | _____% | `[ PASS / FAIL ]` |
| **Cost of Indiscipline (₹)** | ₹0.00 (Zero FOMO trades) | ₹_____ | `[ PASS / FAIL ]` |
| **30-Min Cooldown Honored** | $100\%$ compliance after loss | _____ / _____ | `[ PASS / FAIL ]` |
| **Broker Kill Switch Tripped** | $0$ rule breaches (0 post-10:30) | _____ times | `[ PASS / FAIL ]` |

---

## 3. The 6 Mandatory Weekend Review Questions

Answer these six questions in writing every weekend:

### Q1: How many trades vs my max?
* Total trades executed: _____
* Maximum permitted by reset schedule (2 trades/day cap): _____
* *Binary check:* Did I take more than 2 trades on any single day? `[ YES / NO ]`
* *Root cause if YES:* What triggered the urge to exceed the daily limit?

### Q2: How many trades were not 5/5 checklist trades?
* Total non-5/5 trades taken: _____
* Did any trade fail the structural planned $\text{RR} \ge 2.2$ threshold?
* *Root cause:* Why was an entry taken without full 5/5 confirmation?

### Q3: Did I honor the mandatory 30-minute cooldown after EVERY loss?
* Losses registered this week: _____
* Cooldowns observed in full (30 minutes completely away from screens): _____
* Were there any revenge trades taken inside the cooldown window? `[ YES / NO ]`

### Q4: MAE / MFE Exit Leak Audit
* Was my average MAE $>0.80\text{R}$ on any specific setup? (Stops too tight or late entries)
* What was my Exit Efficiency? If $<60\%$, how much ₹ did I leave on the table due to premature fear exits?
* Actionable fix: ___________________________________________________________

### Q5: What was my true "Cost of Indiscipline"?
* Compare Actual Net P&L vs 100% Rule Compliance P&L in the dashboard simulator.
* *Dollar amount lost to emotional indiscipline:* **₹__________**
* Did I lose money to the market or to my own lack of self-restraint?

### Q6: 30-Day Phase Graduation Gate Assessment
* Current Active Phase: `[ Phase 1 (Days 1–3) / Phase 2 (Days 4–10) / Phase 3 (Days 11–20) / Phase 4 (Days 21–30) ]`
* **Graduation Criteria:**
  - [x] Zero broker kill switch overrides
  - [x] $\ge 90\%$ rule adherence rate
  - [x] No post-10:30 AM IST trades
  - [x] 100% loss cooldowns respected
* **Decision:**
  - `[ PROMOTE TO NEXT PHASE ]` &rarr; Advance trade cap / sizing.
  - `[ MAINTAIN CURRENT PHASE ]` &rarr; Reiterate discipline for another 5 trading sessions.
  - `[ RESET TO PHASE 1 (DAY 1) ]` &rarr; Mandatory reset upon deliberate rule violation.
