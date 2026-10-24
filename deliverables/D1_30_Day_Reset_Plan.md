# 30-Day Execution Reset Plan (D1)

**System:** Trader Execution Reset System  
**Version:** 1.0 (Client Calibrated)  
**Target Timeframe:** 1-Minute Intraday Equities (India / NSE)  
**Trading Window:** 09:15 to 10:30 AM IST  
**Minimum Acceptable RR:** 2.2 RR (1:2.2)  
**Cost Structure:** FYERS Statutory Intraday Charges (Brokerage + STT + Exch + SEBI + Stamp + GST)  
**Broker Kill Switch:** Active / Enforced  

---

## 1. Hard Execution Rules (Non-Negotiable)

These rules govern every trading day during the 30-day reset. They are binary and non-negotiable:

1. **Trade Cap:** Maximum 3 trades per day. The reset starts strictly at 1–2 trades per day.
2. **Loss Cap:** Maximum 2 losses per day. When 2 losses occur, stop trading for the day immediately.
3. **Daily Loss Limit:** Maximum portfolio risk of 0.5%–1.0% or 2R (whichever hits first). Broker kill switch must be active; close platform upon trigger.
4. **Mandatory Cooldown:** After any loss, enforce an immediate 30-minute no-trade cooldown away from the terminal.
5. **No Same-Day Re-Entry:** No re-entry on the same ticker on the same day unless explicitly defined in written setup rules.
6. **Fixed Trading Window:** **09:15 to 10:30 AM IST**. Zero trades permitted before 09:15 or after 10:30 AM.
7. **Limit Orders Only:** No chasing price. Entry is executed via limit order at planned level only.
8. **Zero Averaging / Widening:** No averaging down. No widening stops. No adding to a losing position.
9. **Single Position Limit:** Exactly one open position at any time. No concurrent open positions.
10. **Minimum Technical RR:** **Minimum 2.2 RR planned**. Setups with $<2.2\text{ RR}$ to structural target are invalid.
11. **Emotional Gate:** If subjective FOMO, urgency, or agitation is rated >6/10, trade entry is prohibited.
12. **Rule Violation Stop:** Any rule violation triggers an immediate hard stop for the day, even if the trade was profitable.
13. **Reset Risk Allocation:** Risk per trade is strictly capped at 0.25%–0.50% of account equity.

---

## 2. 30-Day Phased Reset Schedule

| Days | Max trades/day | Risk/trade | Main focus | Pass condition |
|---|---|---|---|---|
| 1–3 | 1–2 | 0.25% or paper | Follow checklist + journal every trade | 100% checklist adherence |
| 4–7 | 2 | 0.25% | Stop after 2 losses; 30-min cooldown | No revenge trade, no chase |
| 8–14 | 2 | 0.25–0.5% | Fixed trading window + time-of-day review | Adherence ≥95% |
| 15–21 | 3 only if prior week ≥95% | 0.5% | Eliminate random entries | Zero checklist violations |
| 22–30 | 3 | 0.5% | Prove expectancy after costs | Positive expectancy + ≥95% adherence |

> **Reset Rule:** If a week’s pass condition fails, you must repeat that entire week before advancing to the next phase.

---

## 3. Detailed Phase Breakdown

### Phase 1: Days 1–3 — Baseline Calibration & Friction Setup
* **Max Trades/Day:** 1–2 trades.
* **Risk/Trade:** 0.25% of account equity or paper trade.
* **Trading Window:** Strictly 09:15 to 10:30 AM IST. Terminal closed by 10:30 AM sharp.
* **Objective:** Establish the habit of physical friction before clicking entry. The scanner only alerts candidates; it does not authorize orders.
* **Mandatory Actions:**
  * Complete pre-market checklist before terminal launch.
  * Score every setup on the 5-point checklist. Only take 5/5 setups with $\ge 2.2\text{ RR}$.
  * Complete the trade journal entry immediately after trade exit.
* **Pass Condition:** 100% checklist adherence over all 3 days.

### Phase 2: Days 4–7 — Loss Containment & Emotional Braking
* **Max Trades/Day:** 2 trades.
* **Risk/Trade:** 0.25% of account equity.
* **Objective:** Enforce immediate behavioral shutdown on losses to eliminate revenge trading cascades.
* **Mandatory Actions:**
  * If Trade 1 is a loss: Step away from desk for 30 minutes. Complete post-loss journal entry.
  * If Trade 2 is a loss: Broker kill switch active / shut down terminal immediately. No exceptions.
  * No market orders; limit orders only at planned price.
* **Pass Condition:** Zero revenge trades, zero chase entries, 100% compliance with 2-loss stop.

### Phase 3: Days 8–14 — Trading Window Lockdown & Time-of-Day Analysis
* **Max Trades/Day:** 2 trades.
* **Risk/Trade:** 0.25%–0.50%.
* **Objective:** Restrict execution strictly to the 09:15–10:30 AM opening liquidity window and eliminate mid-day overtrading.
* **Mandatory Actions:**
  * Open terminal at 09:15 AM; terminate platform at 10:30 AM.
  * Log exact entry time of all alerts and executions in `Trade_Log`.
  * Conduct mid-reset weekend review to confirm zero trades leaked past 10:30 AM.
* **Pass Condition:** Overall checklist adherence ≥95% for the week.

### Phase 4: Days 15–21 — Elimination of Marginal & Random Setups
* **Max Trades/Day:** 3 trades (only permitted if Phase 3 adherence was ≥95%; otherwise maintain 2 trades).
* **Risk/Trade:** 0.50%.
* **Objective:** Filter out "setup-adjacent" random entries. Confirm scanner signals have explicit 15m/5m higher-timeframe alignment and clear structural $\ge 2.2\text{ RR}$.
* **Mandatory Actions:**
  * Audit checklist item 1 (scanner rules) and item 2 (higher-timeframe context) before order placement.
  * Verify planned Risk-to-Reward (RR) is $\ge 2.2\text{ RR}$ based on technical structure.
* **Pass Condition:** Zero checklist violations across the entire 7-day period.

### Phase 5: Days 22–30 — Expectancy Verification After Transaction Friction
* **Max Trades/Day:** 3 trades.
* **Risk/Trade:** 0.50%.
* **Objective:** Validate positive mathematical expectancy ($R$) when netting statutory costs (FYERS equity intraday statutory formula: ₹20 cap brokerage, 0.025% STT on sell, 0.00297% exch, SEBI, stamp duty, 18% GST).
* **Mandatory Actions:**
  * Calculate net expectancy in $R$-multiples via `Weekly_Review`.
  * Ensure gross wins are not consumed by transaction friction (automated in column T using exact FYERS statutory formulas).
  * Complete 30-day cumulative performance and discipline audit.
* **Pass Condition:** Positive net expectancy ($Avg\_R > 0$ after FYERS statutory transaction friction) and checklist adherence ≥95%.

---

## 4. Graduation Criteria

You may only graduate from the 30-day reset and increase risk size if **all** of the following criteria are met simultaneously:

1. **Adherence Gate:** ≥95% checklist adherence across the final 2 consecutive weeks.
2. **Net Expectancy:** Positive expectancy ($R$-multiple > 0) after factoring in FYERS statutory transaction friction.
3. **Emotional Control:** Zero revenge-trading episodes and zero stop-widening in the prior 14 calendar days.
4. **Drawdown Boundary:** Maximum drawdown remained strictly within defined daily and weekly risk parameters.
5. **Sample Size:** 50 or more trade signals logged, categorized, and audited.
6. **Indicator Verification:** The underlying setup edge is verified:
   * No indicator repainting or lookahead bias.
   * Execution triggered only after candle close confirmation on the 1-minute chart.
   * 100–200 historic/forward signals validated.

**Failure to Graduate:** If any condition is unmet, repeat Phase 3 and Phase 4 with paper trading or micro size (0.25%) until two consecutive clean weeks are recorded.

---

## 5. Escalation Protocol

* **Any Single Rule Violation:** Stop trading immediately for the rest of the day. Log the violation in `Trade_Log` (Column Y = "Y") and record the root trigger in `Journal`.
* **Two Daily Losses:** Hard stop for the day. Close trading software. Broker kill switch active.
* **Daily Loss Limit Reached:** Broker kill switch triggers or manual shutdown. Walk away from the workstation.
* **Urge to Revenge Trade:** Immediate 30-minute mandatory break away from screens. Trader must write out the physical reset statement:  
  *“I lost because [Technical Reason]. My next valid setup must have [Checklist Conditions].”*
* **Weekly Adherence < 90%:** Demotion. The following week must be traded on paper or with micro size (0.25% risk maximum).
* **Repeated Violations (2 Consecutive Weeks < 90%):** Cease all live intraday discretionary trading immediately. Require full migration to higher timeframes (15m/1h), algorithmic execution with hardware risk locks, or structured paper trading until adherence reaches 100% for 10 consecutive sessions.
