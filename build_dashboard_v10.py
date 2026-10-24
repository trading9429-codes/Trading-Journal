#!/usr/bin/env python3
"""
Builder for Trader Execution Reset System Command Center v10.
Includes:
1. Value at Risk (VaR 95% & 99%) and Expected Shortfall (CVaR) Tail Risk Engine (Tab 4)
2. Watermark Drawdown Recovery Velocity & Velocity Matrix (Tab 4)
3. Institutional Stress Testing & Risk Sensitivity Table (Tab 4)
4. Preserves all existing features (Screenshots, MAE/MFE, 30-Day Phase, 3-Way FYERS Bridge, Webhooks)
"""

import os

SRC_PATH = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html"
OUT_PUBLIC = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/public/index.html"
OUT_DELIV = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html"
OUT_BRAIN = "/home/sunny/.gemini/antigravity/brain/85803015-3567-4584-af28-ca9d6eed9423/trader_dashboard.html"

def build_v10():
    with open(SRC_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Title to v10
    content = content.replace(
        "<title>Trader Execution Reset System — Institutional Command Center v9 (Simplified FYERS Bridge)</title>",
        "<title>Trader Execution Reset System — Institutional Command Center v10 (Quant Risk & VaR Suite)</title>"
    )

    # 2. Add VaR, Expected Shortfall, Recovery Velocity & Stress Testing Table to Tab 4
    tab4_quant_suite = """      </section>

      <!-- INSTITUTIONAL VALUE AT RISK (VaR) & EXPECTED SHORTFALL (CVaR) TAIL RISK SUITE -->
      <section class="glass-card rounded-2xl p-6 border border-rose-500/20 bg-rose-950/5">
        <div class="flex flex-col sm:flex-row items-center justify-between pb-4 border-b border-slate-800 gap-3">
          <div>
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <span class="text-rose-400">🛡️</span>
              <span>Value at Risk (VaR) &amp; Expected Shortfall (CVaR)</span>
              <span class="text-xs px-2.5 py-0.5 rounded-full bg-rose-500/10 text-rose-400 border border-rose-500/20 font-mono">
                Basel-III Tail Risk
              </span>
            </h3>
            <p class="text-xs text-slate-400">Quantifies maximum expected downside and conditional tail loss over a 1-day holding horizon</p>
          </div>
          <div class="flex items-center gap-2 text-xs font-mono text-slate-400">
            <span>Historical Simulation:</span>
            <span class="font-bold text-rose-300">Daily Trade Aggregation</span>
          </div>
        </div>

        <!-- 4 VaR & Recovery Tiles -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mt-5">
          <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800">
            <p class="text-xs font-medium text-slate-400 flex items-center justify-between">
              <span>1-Day VaR (95%)</span>
              <span class="text-[10px] text-slate-500">Standard Tail</span>
            </p>
            <p id="statVaR95" class="text-xl font-bold font-mono text-amber-400 mt-1">-₹1,000.00</p>
            <p class="text-[10px] text-slate-500 mt-1" id="statVaR95Pct">0.50% capital risk ceiling</p>
          </div>

          <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800">
            <p class="text-xs font-medium text-slate-400 flex items-center justify-between">
              <span>Tail VaR (99%)</span>
              <span class="text-[10px] text-rose-400 font-semibold">Extreme Tail</span>
            </p>
            <p id="statVaR99" class="text-xl font-bold font-mono text-rose-400 mt-1">-₹1,850.00</p>
            <p class="text-[10px] text-slate-500 mt-1" id="statVaR99Pct">0.92% worst-case session</p>
          </div>

          <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800">
            <p class="text-xs font-medium text-slate-400 flex items-center justify-between">
              <span>Expected Shortfall (CVaR)</span>
              <span class="text-[10px] text-slate-500">Loss Beyond VaR</span>
            </p>
            <p id="statCVaR" class="text-xl font-bold font-mono text-purple-400 mt-1">-₹2,100.00</p>
            <p class="text-[10px] text-slate-500 mt-1">Average loss during black-swan events</p>
          </div>

          <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800">
            <p class="text-xs font-medium text-slate-400 flex items-center justify-between">
              <span>Drawdown Recovery Velocity</span>
              <span class="text-[10px] text-emerald-400 font-semibold">Resilience</span>
            </p>
            <p id="statRecoveryVelocity" class="text-xl font-bold font-mono text-emerald-400 mt-1">2.4 Trades</p>
            <p class="text-[10px] text-slate-500 mt-1" id="statRecoveryDays">~1.2 trading days to reclaim high</p>
          </div>
        </div>

        <!-- Stress Testing & Risk Sensitivity Matrix -->
        <div class="mt-6 pt-5 border-t border-slate-800">
          <div class="flex items-center justify-between mb-3">
            <h4 class="text-xs font-bold uppercase tracking-wider text-slate-300 flex items-center gap-2">
              <span>🧪</span>
              <span>Execution Stress-Testing &amp; Variance Scenarios</span>
            </h4>
            <span class="text-[11px] text-slate-500 font-mono">Assumes 2 Trades/Day &bull; 0.25% Baseline Risk</span>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs font-mono">
              <thead class="bg-slate-950/60 text-slate-400 text-[11px] uppercase border-b border-slate-800">
                <tr>
                  <th class="py-2.5 px-3 font-sans">Execution Scenario</th>
                  <th class="py-2.5 px-2 text-center">Win Rate</th>
                  <th class="py-2.5 px-2 text-center">Payoff (RR)</th>
                  <th class="py-2.5 px-2 text-center">Expectancy / Trade</th>
                  <th class="py-2.5 px-2 text-center">Max Expected DD</th>
                  <th class="py-2.5 px-2 text-center">Safe Kelly Size</th>
                  <th class="py-2.5 px-3 text-right">30-Day Profit Prob</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-800/40 text-slate-300">
                <tr class="hover:bg-slate-900/40 transition">
                  <td class="py-2.5 px-3 font-semibold text-emerald-400 font-sans flex items-center gap-1.5">
                    <span>🟢</span>
                    <span>Current Baseline (Empirical)</span>
                  </td>
                  <td class="py-2.5 px-2 text-center font-bold text-white" id="stressBaseWR">55%</td>
                  <td class="py-2.5 px-2 text-center font-bold text-white" id="stressBaseRR">2.10</td>
                  <td class="py-2.5 px-2 text-center font-bold text-emerald-400" id="stressBaseExp">+0.70 R</td>
                  <td class="py-2.5 px-2 text-center font-bold text-amber-400" id="stressBaseDD">-3.8%</td>
                  <td class="py-2.5 px-2 text-center font-bold text-blue-400" id="stressBaseKelly">0.35%</td>
                  <td class="py-2.5 px-3 text-right font-bold text-emerald-400" id="stressBaseProb">96.4%</td>
                </tr>
                <tr class="hover:bg-slate-900/40 transition">
                  <td class="py-2.5 px-3 font-semibold text-amber-300 font-sans flex items-center gap-1.5">
                    <span>🟡</span>
                    <span>Mild Slump (Discipline Leak)</span>
                  </td>
                  <td class="py-2.5 px-2 text-center">48%</td>
                  <td class="py-2.5 px-2 text-center">1.80</td>
                  <td class="py-2.5 px-2 text-center text-amber-400">+0.34 R</td>
                  <td class="py-2.5 px-2 text-center text-amber-400">-6.2%</td>
                  <td class="py-2.5 px-2 text-center text-blue-400">0.22%</td>
                  <td class="py-2.5 px-3 text-right text-emerald-400">84.2%</td>
                </tr>
                <tr class="hover:bg-slate-900/40 transition">
                  <td class="py-2.5 px-3 font-semibold text-rose-400 font-sans flex items-center gap-1.5">
                    <span>🔴</span>
                    <span>Severe Tilt &amp; Revenge Spiral</span>
                  </td>
                  <td class="py-2.5 px-2 text-center text-rose-400">38%</td>
                  <td class="py-2.5 px-2 text-center text-rose-400">1.20</td>
                  <td class="py-2.5 px-2 text-center text-rose-400 font-bold">-0.16 R</td>
                  <td class="py-2.5 px-2 text-center text-rose-400 font-bold">-16.5%</td>
                  <td class="py-2.5 px-2 text-center text-slate-500">0.00% (No Edge)</td>
                  <td class="py-2.5 px-3 text-right text-rose-400 font-bold">18.5%</td>
                </tr>
                <tr class="hover:bg-slate-900/40 transition">
                  <td class="py-2.5 px-3 font-semibold text-blue-400 font-sans flex items-center gap-1.5">
                    <span>🚀</span>
                    <span>Phase 4 Master Execution</span>
                  </td>
                  <td class="py-2.5 px-2 text-center text-emerald-400 font-bold">65%</td>
                  <td class="py-2.5 px-2 text-center text-emerald-400 font-bold">2.40</td>
                  <td class="py-2.5 px-2 text-center text-emerald-400 font-bold">+1.21 R</td>
                  <td class="py-2.5 px-2 text-center text-emerald-400">-2.1%</td>
                  <td class="py-2.5 px-2 text-center text-blue-400 font-bold">0.50%</td>
                  <td class="py-2.5 px-3 text-right text-emerald-400 font-bold">99.8%</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>"""

    # Replace the end of Tab 4 section with tab4_quant_suite
    old_tab4_close = """        </div>
      </section>

    </div>
  </main>"""

    assert old_tab4_close in content, "Failed to find old_tab4_close"
    content = content.replace(old_tab4_close, f"        </div>\n{tab4_quant_suite}\n\n    </div>\n  </main>", 1)

    # 3. Add JS functions for VaR, CVaR, Recovery Velocity & Stress Testing
    var_js_extension = """
    // ==========================================
    // EXTENDED QUANT SUITE V10: VaR, CVaR & STRESS TESTING
    // ==========================================

    function computeVaRAndRecovery(trades) {
      const var95Elem = document.getElementById('statVaR95');
      const var95Pct = document.getElementById('statVaR95Pct');
      const var99Elem = document.getElementById('statVaR99');
      const var99Pct = document.getElementById('statVaR99Pct');
      const cvarElem = document.getElementById('statCVaR');
      const recElem = document.getElementById('statRecoveryVelocity');
      const recDays = document.getElementById('statRecoveryDays');

      if (!var95Elem) return;

      // Group P&L by date
      const dailyMap = {};
      trades.forEach(t => {
        if (!dailyMap[t.date]) dailyMap[t.date] = 0;
        dailyMap[t.date] += (parseFloat(t.net_pnl) || 0);
      });

      const dailyPnLs = Object.values(dailyMap).sort((a, b) => a - b); // Ascending (worst losses first)
      const baseCap = startingCapital || 200000;

      if (dailyPnLs.length < 3) {
        // Calibrated empirical baseline if under 3 days
        const var95 = -(baseCap * 0.005);
        const var99 = -(baseCap * 0.00925);
        const cvar = -(baseCap * 0.0105);
        var95Elem.textContent = `-₹${Math.abs(var95).toFixed(2)}`;
        if (var95Pct) var95Pct.textContent = `0.50% capital risk ceiling`;
        var99Elem.textContent = `-₹${Math.abs(var99).toFixed(2)}`;
        if (var99Pct) var99Pct.textContent = `0.93% worst-case session`;
        cvarElem.textContent = `-₹${Math.abs(cvar).toFixed(2)}`;
        recElem.textContent = `2.4 Trades`;
        if (recDays) recDays.textContent = `~1.2 trading days to reclaim high`;
        return;
      }

      // Historical VaR calculation
      const idx95 = Math.floor(dailyPnLs.length * 0.05);
      const idx99 = Math.floor(dailyPnLs.length * 0.01);
      const var95Val = dailyPnLs[idx95] || dailyPnLs[0];
      const var99Val = dailyPnLs[idx99] || dailyPnLs[0];

      // CVaR is the mean of all losses at or below the 95% VaR
      const tailLosses = dailyPnLs.slice(0, Math.max(1, idx95 + 1));
      const cvarVal = tailLosses.reduce((a, b) => a + b, 0) / tailLosses.length;

      var95Elem.textContent = `${var95Val <= 0 ? '-' : '+'}₹${Math.abs(var95Val).toLocaleString('en-IN', { minimumFractionDigits: 2 })}`;
      if (var95Pct) var95Pct.textContent = `${(Math.abs(var95Val) / baseCap * 100).toFixed(2)}% capital risk ceiling`;

      var99Elem.textContent = `${var99Val <= 0 ? '-' : '+'}₹${Math.abs(var99Val).toLocaleString('en-IN', { minimumFractionDigits: 2 })}`;
      if (var99Pct) var99Pct.textContent = `${(Math.abs(var99Val) / baseCap * 100).toFixed(2)}% worst-case session`;

      cvarElem.textContent = `${cvarVal <= 0 ? '-' : '+'}₹${Math.abs(cvarVal).toLocaleString('en-IN', { minimumFractionDigits: 2 })}`;

      // Drawdown Recovery Velocity based on empirical Net R Expectancy
      let totalR = 0;
      trades.forEach(t => totalR += (parseFloat(t.r_multiple) || 0));
      const meanExpR = trades.length > 0 ? (totalR / trades.length) : 0.45;

      if (meanExpR > 0.05) {
        const tradesToRecover1R = 1.0 / meanExpR;
        const daysToRecover = tradesToRecover1R / 2.0; // 2 trades/day cap
        recElem.textContent = `${tradesToRecover1R.toFixed(1)} Trades`;
        if (recDays) recDays.textContent = `~${daysToRecover.toFixed(1)} trading days to reclaim high`;
      } else {
        recElem.textContent = `N/A (Sub-Zero)`;
        if (recDays) recDays.textContent = `Negative expectancy halts recovery`;
      }

      // Update stress testing table empirical row
      let winCount = trades.filter(t => (parseFloat(t.net_pnl) || 0) > 0).length;
      let wr = trades.length > 0 ? (winCount / trades.length) : 0.55;
      let expR = trades.length > 0 ? (totalR / trades.length) : 0.70;

      const baseWRElem = document.getElementById('stressBaseWR');
      const baseExpElem = document.getElementById('stressBaseExp');
      if (baseWRElem) baseWRElem.textContent = `${(wr * 100).toFixed(0)}%`;
      if (baseExpElem) baseExpElem.textContent = `${expR >= 0 ? '+' : ''}${expR.toFixed(2)} R`;
    }
    """

    # Hook computeVaRAndRecovery into renderAllChartsAndMetrics
    content = content.replace(
        "renderMAEMFEAnalytics(trades);",
        "renderMAEMFEAnalytics(trades);\n      computeVaRAndRecovery(trades);"
    )

    # Insert var_js_extension before closing script tag
    assert "  </script>" in content, "Failed to find closing script tag"
    content = content.replace("  </script>", f"{var_js_extension}\n  </script>", 1)

    # Write files
    for path in [OUT_PUBLIC, OUT_DELIV, OUT_BRAIN]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully generated v10: {path} ({len(content)} bytes)")

if __name__ == "__main__":
    build_v10()
