# Trader Execution Reset System

**Version:** 1.0 (Calibrated & Modernized)  
**Timeframe:** Intraday 1-Minute Equities (India / NSE)  
**Trading Window:** 09:15 to 10:30 AM IST (75 Minutes)  
**Minimum Risk-to-Reward:** ≥ 2.2 RR  
**Cost Model:** FYERS Statutory Intraday Equity Charges (Brokerage + STT + Exch + SEBI + Stamp + GST)  
**Platform Kill Switch:** Active / Verified  
**Spreadsheet Format:** Microsoft Excel (`.xlsx`) with SharedStrings & Modern Dashboard Tab  

---

## Client Profile & Root Cause Alignment

* **The Problem:** 30–40 trades per day, overtrading, revenge trading, and emotional execution on a 1-minute chart.
* **The Root Cause:** The indicator is not the primary leak. The leak is trade frequency and undisciplined execution. The scanner produces candidates, not entries.
* **The Solution:** A trade is valid **only** if a 5-point checklist scores 5/5, planned RR is $\ge 2.2$, execution is inside 09:15–10:30 AM, and risk is limited to 2 trades/day with a 2-loss stop.

---

## Deliverables Summary

| Deliverable | File | Description |
|---|---|---|
| **Dashboard** | `Dashboard.html` | Institutional Web Command Center v13: **Full Institutional Design Overhaul (Inter + JetBrains Mono Typography & Obsidian Glassmorphic Dark UI)**: <br>&bull; **Header & Governance** — Real-Time IST Market Clock, 10:30 AM Auto-Lockout, **5-Minute Pre-Market Focus & Box Breathing Timer (09:05–09:10 AM IST)**, **Trader Execution Contract & Penalty Strike Demerit System (0/3 strikes with automated Phase 1 demotion)**, and Sound Effects.<br>&bull; **Tab 1: ⚡ Live Execution & Ledger** — **Interactive Segmented Direction Switchers (🟢 LONG / 🔴 SHORT)** with instant risk recalculation, **30-Day Phase Graduation & Discipline Milestone Tracker** (Phase 1–4 progress bar, day counter & rule compliance gate), 1-Click Position Sizer with **Custom Risk Amount (₹)** input plus 0.25%/0.50% quick presets and MIS 5x leverage preview, **MAE & MFE Excursion Inputs**, **1-Minute Execution Chart Screenshot Attachment** (with `Ctrl+V` clipboard paste, drag-and-drop & full-size zoom modal), Pre-trade urgency/tilt slider, Target Planned RR $\ge 2.2$ validator, FYERS statutory charge calculator, 30-min loss cooldown timer, Daily 2-trade/2-loss kill switch, **Telegram & WhatsApp Accountability Webhook Alert Dispatcher** (auto-broadcasts trades, cooldowns, and kill switch trips with live test ping), **Streamlined FYERS Ingestion Engine** (Zero-API copy-paste from FYERS Web or file drag & drop with automatic statutory charge parsing), **Interactive Strategy Filter (9EMA, ORB, VWAP, S/R Bounce, Off-Plan)** in the Filtered Trade Ledger with live edit/delete, and JSON Database Vault backup & restore.<br>&bull; **Tab 2: 📈 Performance & Equity** — Date Range Filtering, Editable Starting Capital, "Cost of Indiscipline" 100% compliance simulator, 8 Primary KPI Scorecards (Win Rate, Profit Factor, Net P&L, Net R, Avg Trade, Max Drawdown, Avg RR, Rule Discipline %), Full-Width Cumulative Equity curve (`height: 320px`), Outcome & Rule Discipline Donut charts, and Long vs Short Directional Edge breakdown.<br>&bull; **Tab 3: 🧠 Edge & Leaks** — **Multi-Strategy Performance Attribution Matrix** (dissects edge, win rate, net R, profit factor, and cost friction per playbook strategy), **MAE & MFE Exit Leak & Stop Quality Diagnostics** (Avg MAE adverse drawdown in R, Avg MFE peak potential in R, Exit Efficiency capture rate %, and Money Left on Table ₹), Hold Duration Asymmetry (Win vs Loss hold duration & asymmetry ratio), Streak Tracker & Post-Cooldown Variance Engine, Emotional Urgency Tilt Correlation Matrix (1–3 Calm vs 4–6 Moderate vs 7–10 Tilt), Day-of-Week Edge Matrix (Mon–Fri Win Rate, Net P&L, Expectancy), 15-Minute Time-of-Day Execution Heatmap, and Setup Expectancy Matrix.<br>&bull; **Tab 4: 🎲 Quant Risk & Monte Carlo** — **Value at Risk (VaR 95% & 99% Tail Risk)**, **Expected Shortfall (CVaR)**, **Drawdown Recovery Velocity (Trades & Days)**, **Execution Stress-Testing & Variance Sensitivity Table**, Kelly Criterion ($f^*$ optimal fraction & Quarter-Kelly recommendation), Risk of Ruin 10% & 20% Drawdown probability engine, Annualized Sortino & Sharpe Ratios, FYERS Statutory Cost Drag % & Churn turnover ratio, and 30-Day Monte Carlo compound growth projector with 1,000 iterations and 5th/50th/95th percentile outcome bands. |
| **D1** | `D1_30_Day_Reset_Plan.md` | 30-day phased roadmap, trade caps, pass conditions, and graduation criteria. |
| **D2** | `D2_Daily_Checklist.md` | Pre-market, per-trade (verbatim 5/5 with $\ge 2.2\text{ RR}$), and printable daily sheet. |
| **D3** | `D3_Tracking_Spreadsheet.xlsx` | 5-tab modernized workbook (`Dashboard`, `Trade_Log`, `Daily_Scorecard`, `Weekly_Review`, `Journal`) with full sharedStrings XML, KPI summary cards, automated FYERS statutory charges, data validations, and conditional formatting. |
| **D4** | `D4_Trade_Journal_Template.md` | Post-trade reflection template v2.0: MAE/MFE excursion tracking, Exit Efficiency %, visual screenshot checklist, FYERS statutory cost transparency, and 1–10 emotional calibration scale. |
| **D5** | `D5_Weekly_Review_Template.md` | Governance audit questionnaire v2.0: Weekly MAE/MFE exit leak audit, True Edge vs Cost of Indiscipline dollar loss, 30-Day Phase Graduation Gate decision matrix, and risk audit. |
| **D6** | `D6_Quick_Reference_Card.md` | Single-page printable desk card with hard rules, checklist, and kill switches. |
| **D7** | `D7_Usage_Instructions.md` | Operating guide detailing daily routines and spreadsheet maintenance ($\le 1$ page). |
| **FYERS Guide** | `FYERS_API_Integration_Guide.md` | Friction-Free FYERS Tradebook Ingestion Guide: (1) Instant copy-paste from FYERS Web table (0 API tokens, 0 IP whitelisting), (2) Drag-and-drop tradebook CSV/XLSX, and (3) Automated Python CLI bridge. |
| **Sample CSV** | `sample_trades_import.csv` | Ready-to-use CSV template for bulk importing trades into the dashboard with automated calculation of FYERS costs, Net P&L, and Net R. |

---

## Non-Negotiable Hard Rules

1. **Max Trades:** Max 3 trades/day; reset begins strictly at 1–2 trades/day.
2. **Max Losses:** Max 2 losses/day $\rightarrow$ stop trading immediately for the day.
3. **Daily Loss Limit:** 0.5%–1.0% portfolio risk or 2R $\rightarrow$ broker kill switch locks platform.
4. **Mandatory Cooldown:** After any loss $\rightarrow$ mandatory 30-minute break away from screens.
5. **No Same-Day Re-Entry:** No re-entering the same ticker on the same day.
6. **Fixed Time Window:** **09:15 to 10:30 AM IST**. No trades past 10:30 AM.
7. **Limit Orders Only:** No chasing. Limit orders stationed at planned levels only.
8. **No Averaging / Widening:** No averaging down. No widening stops. No adding to losers.
9. **Single Position:** Exactly one open position at a time.
10. **Minimum RR:** Planned structural setup must offer $\ge 2.2\text{ RR}$.
11. **Emotional Gate:** Subjective urgency/FOMO $>6/10 \rightarrow$ strict NO TRADE.
12. **Rule Violation Hard Stop:** Any rule violation $\rightarrow$ stop for the day immediately.
13. **Risk Size:** Risk per trade is strictly 0.25%–0.50% during the reset.
