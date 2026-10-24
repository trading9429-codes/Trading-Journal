#!/usr/bin/env python3
"""
Builder for Trader Execution Reset System Command Center v12.
Adds:
1. 🧘 Pre-Market 5-Minute Focus & Box Breathing Timer (09:05–09:10 AM IST)
2. ⚖️ Trader Execution Rules Contract & Penalty Strike Demerit System (0/3 strikes)
3. 📊 Multi-Strategy Attribution Suite (9EMA Pullback vs ORB vs VWAP vs S/R Bounce) with Strategy Filter in Ledger
"""

import os
import re

SRC_PATH = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html"
OUT_PUBLIC = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/public/index.html"
OUT_DELIV = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html"
OUT_BRAIN = "/home/sunny/.gemini/antigravity/brain/85803015-3567-4584-af28-ca9d6eed9423/trader_dashboard.html"

def build_v12():
    with open(SRC_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Title
    content = content.replace(
        "<title>Trader Execution Reset System — Institutional Command Center</title>",
        "<title>Trader Execution Reset System — Institutional Command Center v12</title>"
    )

    # 2. Add Pre-Market Mindset & Demerit Strike pills into the Top Header Command Bar
    old_header_controls = """        <button id="soundToggleBtn" onclick="toggleSound()" class="px-2.5 py-1.5 rounded-lg bg-slate-800/80 border border-slate-700 text-slate-300 hover:text-white flex items-center gap-1.5 transition">
          <span id="soundIcon">🔊</span>
          <span id="soundText" class="font-medium">Audio ON</span>
        </button>"""

    new_header_controls = """        <button onclick="openPreMarketFocusModal()" class="px-2.5 py-1.5 rounded-lg bg-teal-500/10 border border-teal-500/30 text-teal-300 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm" title="5-Minute Pre-Market Mindset &amp; Box Breathing (09:05–09:10 AM IST)">
          <span>🧘</span>
          <span>Mindset Timer</span>
        </button>

        <button onclick="openTraderContractModal()" id="headerDemeritBadge" class="px-2.5 py-1.5 rounded-lg bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm" title="Execution Contract &amp; Penalty Strike System">
          <span>⚖️</span>
          <span id="headerStrikesText">Strikes: 0/3</span>
        </button>

        <button id="soundToggleBtn" onclick="toggleSound()" class="px-2.5 py-1.5 rounded-lg bg-slate-800/80 border border-slate-700 text-slate-300 hover:text-white flex items-center gap-1.5 transition">
          <span id="soundIcon">🔊</span>
          <span id="soundText" class="font-medium">Audio ON</span>
        </button>"""

    assert old_header_controls in content, "Failed to find old_header_controls"
    content = content.replace(old_header_controls, new_header_controls, 1)

    # 3. Enhance Trade Logger setup_name Dropdown to include all Playbook Strategies
    old_setup_dropdown = """              <select id="setup_name" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-2.5 py-1.5 text-white text-xs">
                <option value="1m Pullback to 9EMA">1m Pullback to 9EMA (Rule Setup A)</option>
                <option value="1m VWAP Bounce">1m VWAP Bounce / Trend Contin.</option>
                <option value="1m Breakout &amp; Re-test">1m Opening Breakout Re-test</option>
                <option value="Other / Discretionary">Other Discretionary</option>
              </select>"""

    new_setup_dropdown = """              <select id="setup_name" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-2.5 py-1.5 text-white text-xs">
                <option value="1m Pullback to 9EMA">1m Pullback to 9EMA (Core Edge)</option>
                <option value="Opening Range Breakout (ORB)">Opening Range Breakout (ORB)</option>
                <option value="1m VWAP Bounce">1m VWAP Bounce / Trend Contin.</option>
                <option value="1m Breakout &amp; Re-test">1m Breakout &amp; Structural Re-test</option>
                <option value="Support / Resistance Bounce">Support / Resistance Level Bounce</option>
                <option value="Off-Plan / Discretionary">Off-Plan / Discretionary (Rule Breach)</option>
              </select>"""

    assert old_setup_dropdown in content, "Failed to find old_setup_dropdown"
    content = content.replace(old_setup_dropdown, new_setup_dropdown, 1)

    # 4. Add Strategy Filter Dropdown in Trades Ledger Table (Tab 1)
    old_ledger_filters = """            <select id="outcomeFilter" onchange="renderTradesTable()" class="bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white focus:outline-none focus:border-blue-500">
              <option value="ALL">All Outcomes</option>
              <option value="Win">Wins Only</option>
              <option value="Loss">Losses Only</option>
              <option value="Break-Even">Break-Even</option>
            </select>"""

    new_ledger_filters = """            <select id="strategyFilter" onchange="renderTradesTable()" class="bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white focus:outline-none focus:border-blue-500">
              <option value="ALL">All Strategies</option>
              <option value="1m Pullback to 9EMA">9EMA Pullback</option>
              <option value="Opening Range Breakout (ORB)">ORB</option>
              <option value="1m VWAP Bounce">VWAP Bounce</option>
              <option value="1m Breakout &amp; Re-test">Breakout &amp; Retest</option>
              <option value="Support / Resistance Bounce">S/R Bounce</option>
              <option value="Off-Plan / Discretionary">Off-Plan</option>
            </select>
            <select id="outcomeFilter" onchange="renderTradesTable()" class="bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white focus:outline-none focus:border-blue-500">
              <option value="ALL">All Outcomes</option>
              <option value="Win">Wins Only</option>
              <option value="Loss">Losses Only</option>
              <option value="Break-Even">Break-Even</option>
            </select>"""

    assert old_ledger_filters in content, "Failed to find old_ledger_filters"
    content = content.replace(old_ledger_filters, new_ledger_filters, 1)

    # 5. Add Multi-Strategy Comparative Attribution Matrix to Tab 3 (Edge & Leaks)
    strategy_attribution_markup = """      <!-- MULTI-STRATEGY ATTRIBUTION & EDGE MATRIX -->
      <section class="glass-card rounded-2xl p-6 shadow-2xl border border-teal-500/20 bg-teal-950/5">
        <div class="flex flex-col sm:flex-row items-center justify-between pb-4 border-b border-slate-800 gap-2">
          <div>
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <span class="text-teal-400">📊</span>
              <span>Multi-Strategy Performance Attribution</span>
              <span class="text-xs px-2.5 py-0.5 rounded-full bg-teal-500/10 text-teal-300 border border-teal-500/20 font-mono">
                Strategy Breakdown
              </span>
            </h3>
            <p class="text-xs text-slate-400">Dissecting edge quality across your structural playbooks to allocate capital efficiently</p>
          </div>
          <div class="flex items-center gap-2 text-xs font-mono">
            <span class="text-slate-400">Top Strategy:</span>
            <span id="bestStrategyPill" class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold">1m Pullback to 9EMA</span>
          </div>
        </div>

        <div class="overflow-x-auto mt-4">
          <table class="w-full text-left text-xs font-mono">
            <thead class="bg-slate-950/60 text-slate-400 text-[11px] uppercase border-b border-slate-800">
              <tr>
                <th class="py-2.5 px-3 font-sans">Playbook Strategy</th>
                <th class="py-2.5 px-2 text-center">Trades</th>
                <th class="py-2.5 px-2 text-center">Win Rate</th>
                <th class="py-2.5 px-2 text-center">Net R</th>
                <th class="py-2.5 px-2 text-center">Profit Factor</th>
                <th class="py-2.5 px-2 text-right">Net P&amp;L</th>
                <th class="py-2.5 px-3 text-center">Edge Grade</th>
              </tr>
            </thead>
            <tbody id="strategyAttributionTableBody" class="divide-y divide-slate-800/40 text-slate-300">
              <!-- Populated dynamically via renderStrategyAttribution() -->
            </tbody>
          </table>
        </div>
      </section>

      <!-- SETUP EXPECTANCY MATRIX -->"""

    old_tab3_marker = """      <!-- SETUP EXPECTANCY MATRIX -->"""
    if old_tab3_marker in content:
        content = content.replace(old_tab3_marker, strategy_attribution_markup, 1)

    # 6. Add Modals: Pre-Market Focus & Breathing Modal, and Trader Execution Contract Modal
    new_modals_v12 = """  <!-- ========================================== -->
  <!-- MODAL: PRE-MARKET 5-MIN FOCUS & BREATHING TIMER -->
  <!-- ========================================== -->
  <div id="preMarketFocusModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="glass-card rounded-2xl w-full max-w-xl border border-teal-500/30 shadow-2xl p-6 relative max-h-[92vh] overflow-y-auto">
      
      <div class="flex items-center justify-between pb-4 border-b border-slate-800">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-xl bg-teal-500/20 border border-teal-500/40 flex items-center justify-center text-teal-400 font-bold text-lg">
            🧘
          </div>
          <div>
            <h3 class="text-base font-extrabold text-white">Pre-Market Focus &amp; Box Breathing</h3>
            <p class="text-xs text-slate-400">09:05–09:10 AM IST Grounding &bull; Lowers Heart Rate &bull; Prevents Impulse Openings</p>
          </div>
        </div>
        <button onclick="closePreMarketFocusModal()" class="text-slate-400 hover:text-white text-2xl font-bold">&times;</button>
      </div>

      <!-- Breathing Visualizer Circle -->
      <div class="py-8 flex flex-col items-center justify-center">
        <div id="breathingRing" class="w-40 h-40 rounded-full border-4 border-teal-500/40 bg-teal-500/10 flex flex-col items-center justify-center transition-all duration-1000 shadow-2xl shadow-teal-500/20">
          <span id="breathingActionText" class="text-sm font-black uppercase tracking-widest text-teal-300">Inhale</span>
          <span id="breathingCounterText" class="text-2xl font-black font-mono text-white mt-1">4s</span>
        </div>
        <p class="text-xs text-slate-400 mt-4 font-medium" id="breathingSubText">Inhale deeply through your nose (4 seconds)</p>
      </div>

      <!-- Digital Timer & Controls -->
      <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800 flex items-center justify-between">
        <div>
          <span class="text-[10px] text-slate-400 uppercase font-bold">Session Remaining</span>
          <div id="focusTimerDisplay" class="text-2xl font-black font-mono text-white">05:00</div>
        </div>
        <div class="flex items-center gap-2">
          <button id="focusTimerToggleBtn" onclick="toggleFocusTimer()" class="px-4 py-2 rounded-xl bg-teal-600 hover:bg-teal-500 text-white font-bold text-xs transition shadow-lg shadow-teal-600/30">
            Start Breathing
          </button>
          <button onclick="resetFocusTimer()" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition">
            Reset
          </button>
        </div>
      </div>

      <!-- Core Trader Affirmations -->
      <div class="mt-4 p-3.5 bg-slate-950/60 rounded-xl border border-slate-800 space-y-2 text-xs">
        <p class="font-bold text-teal-300 flex items-center gap-1.5"><span>⚡</span> Pre-Flight Mindset Covenant:</p>
        <p class="text-slate-300 italic">&ldquo;My scanner generates candidates, not entries. I do not chase. I wait for the candle to close at my 9EMA level.&rdquo;</p>
        <p class="text-slate-300 italic">&ldquo;Max 2 trades today. If a loss hits, I walk away for 30 minutes without negotiation.&rdquo;</p>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL: TRADER EXECUTION CONTRACT & DEMERIT STRIKES -->
  <!-- ========================================== -->
  <div id="traderContractModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="glass-card rounded-2xl w-full max-w-2xl border border-indigo-500/30 shadow-2xl p-6 relative max-h-[92vh] overflow-y-auto">
      
      <div class="flex items-center justify-between pb-4 border-b border-slate-800">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-xl bg-indigo-500/20 border border-indigo-500/40 flex items-center justify-center text-indigo-400 font-bold text-lg">
            ⚖️
          </div>
          <div>
            <h3 class="text-base font-extrabold text-white">Trader Execution Contract &amp; Penalty Strikes</h3>
            <p class="text-xs text-slate-400">Non-Negotiable Operating Rules &bull; Three-Strike Phase Demotion System</p>
          </div>
        </div>
        <button onclick="closeTraderContractModal()" class="text-slate-400 hover:text-white text-2xl font-bold">&times;</button>
      </div>

      <!-- Active Strikes Scorecard -->
      <div class="grid grid-cols-3 gap-3 mt-4 text-center">
        <div class="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
          <span class="text-[10px] text-slate-400 uppercase font-bold">Active Strikes</span>
          <div id="contractActiveStrikesDisp" class="text-2xl font-black font-mono text-emerald-400 mt-0.5">0 / 3</div>
          <span class="text-[10px] text-slate-500">3 strikes = Demotion</span>
        </div>
        <div class="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
          <span class="text-[10px] text-slate-400 uppercase font-bold">Accountability Status</span>
          <div id="contractStatusDisp" class="text-sm font-bold text-emerald-400 mt-2">CLEAN RECORD</div>
          <span class="text-[10px] text-slate-500">100% Phase Compliant</span>
        </div>
        <div class="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
          <span class="text-[10px] text-slate-400 uppercase font-bold">Active Risk Cap</span>
          <div id="contractRiskCapDisp" class="text-sm font-bold text-blue-400 mt-2">0.25% – 0.50%</div>
          <span class="text-[10px] text-slate-500">Governed by Phase</span>
        </div>
      </div>

      <!-- Non-Negotiable Contract Clauses -->
      <div class="mt-4 p-4 bg-slate-950/80 rounded-xl border border-slate-800 text-xs space-y-2.5">
        <h4 class="font-bold text-white uppercase text-[11px] tracking-wider text-indigo-300">My 5 Non-Negotiable Execution Commandments:</h4>
        <div class="space-y-1.5 text-slate-300">
          <p><strong>1. Strict Window:</strong> I trade strictly between <strong>09:15 and 10:30 AM IST</strong>. At 10:30, all trading halts regardless of market conditions.</p>
          <p><strong>2. Trade &amp; Loss Limits:</strong> Max 2 trades per day. If 2 losses occur, I lock my terminal immediately.</p>
          <p><strong>3. 30-Minute Cooldown:</strong> Following any losing trade, I will stand up and walk away from my desk for a full 30 minutes.</p>
          <p><strong>4. Structural Minimum RR:</strong> Every trade must structurally offer <strong>&ge; 2.2 planned R:R</strong>. No chasing market orders.</p>
          <p><strong>5. Zero Tampering:</strong> I will never average down, widen a stop-loss, or take unverified discretionary trades.</p>
        </div>
      </div>

      <!-- Strike Management Action Buttons -->
      <div class="mt-4 flex flex-col sm:flex-row items-center justify-between gap-3 pt-3 border-t border-slate-800">
        <button onclick="logPenaltyStrike()" class="w-full sm:w-auto px-4 py-2 rounded-xl bg-rose-600/20 hover:bg-rose-600/30 text-rose-300 border border-rose-500/30 text-xs font-bold transition flex items-center justify-center gap-1.5">
          <span>⚠️</span>
          <span>Self-Report Rule Infraction (+1 Strike)</span>
        </button>
        <button onclick="clearPenaltyStrikes()" class="w-full sm:w-auto px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition">
          ↺ Reset Strikes (After 5 Clean Days)
        </button>
      </div>

    </div>
  </div>"""

    content = content.replace("</body>", f"{new_modals_v12}\n</body>")

    # 7. JavaScript Engine Extensions for:
    # - Pre-Market Focus & Breathing Timer (4s Inhale, 4s Hold, 4s Exhale, 4s Hold)
    # - Penalty Strikes & Demerit System
    # - Multi-Strategy Performance Attribution Table
    v12_js_engine = """
    // ==========================================
    // EXTENDED ENGINE V12: PRE-MARKET FOCUS, STRIKES & MULTI-STRATEGY
    // ==========================================

    let focusTimerInterval = null;
    let focusTimerSeconds = 300; // 5 minutes
    let isFocusRunning = false;
    let breathingPhase = 0; // 0: Inhale, 1: Hold, 2: Exhale, 3: Hold
    let breathingPhaseSeconds = 4;
    let breathingInterval = null;

    // --- Pre-Market Focus & Breathing Timer ---
    function openPreMarketFocusModal() {
      const modal = document.getElementById('preMarketFocusModal');
      if (modal) modal.classList.remove('hidden');
    }

    function closePreMarketFocusModal() {
      const modal = document.getElementById('preMarketFocusModal');
      if (modal) modal.classList.add('hidden');
      if (isFocusRunning) toggleFocusTimer();
    }

    function toggleFocusTimer() {
      const btn = document.getElementById('focusTimerToggleBtn');
      if (isFocusRunning) {
        // Pause
        clearInterval(focusTimerInterval);
        clearInterval(breathingInterval);
        isFocusRunning = false;
        btn.textContent = "Resume Breathing";
        btn.className = "px-4 py-2 rounded-xl bg-teal-600 hover:bg-teal-500 text-white font-bold text-xs transition shadow-lg shadow-teal-600/30";
      } else {
        // Start
        isFocusRunning = true;
        btn.textContent = "Pause Timer";
        btn.className = "px-4 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow-lg shadow-amber-600/30";
        focusTimerInterval = setInterval(updateFocusCountdown, 1000);
        startBreathingCycle();
      }
    }

    function resetFocusTimer() {
      clearInterval(focusTimerInterval);
      clearInterval(breathingInterval);
      isFocusRunning = false;
      focusTimerSeconds = 300;
      document.getElementById('focusTimerDisplay').textContent = "05:00";
      const btn = document.getElementById('focusTimerToggleBtn');
      btn.textContent = "Start Breathing";
      btn.className = "px-4 py-2 rounded-xl bg-teal-600 hover:bg-teal-500 text-white font-bold text-xs transition shadow-lg shadow-teal-600/30";
      resetBreathingDisplay();
    }

    function updateFocusCountdown() {
      if (focusTimerSeconds <= 0) {
        clearInterval(focusTimerInterval);
        clearInterval(breathingInterval);
        isFocusRunning = false;
        document.getElementById('focusTimerDisplay').textContent = "00:00";
        alert("🧘 Pre-Market Mindset Grounding Complete! Heart rate normalized. You are ready for disciplined execution.");
        const chkCalm = document.getElementById('chk_calm');
        if (chkCalm) chkCalm.checked = true;
        closePreMarketFocusModal();
        return;
      }
      focusTimerSeconds--;
      const m = Math.floor(focusTimerSeconds / 60);
      const s = focusTimerSeconds % 60;
      document.getElementById('focusTimerDisplay').textContent = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    }

    function startBreathingCycle() {
      breathingPhase = 0;
      breathingPhaseSeconds = 4;
      updateBreathingUI();
      if (breathingInterval) clearInterval(breathingInterval);
      breathingInterval = setInterval(() => {
        breathingPhaseSeconds--;
        if (breathingPhaseSeconds <= 0) {
          breathingPhase = (breathingPhase + 1) % 4;
          breathingPhaseSeconds = 4;
        }
        updateBreathingUI();
      }, 1000);
    }

    function updateBreathingUI() {
      const ring = document.getElementById('breathingRing');
      const action = document.getElementById('breathingActionText');
      const count = document.getElementById('breathingCounterText');
      const sub = document.getElementById('breathingSubText');
      if (!ring || !action || !count) return;

      count.textContent = `${breathingPhaseSeconds}s`;

      if (breathingPhase === 0) { // Inhale
        action.textContent = "Inhale";
        action.className = "text-sm font-black uppercase tracking-widest text-teal-300";
        ring.className = "w-44 h-44 rounded-full border-4 border-teal-400 bg-teal-500/25 flex flex-col items-center justify-center transition-all duration-1000 shadow-2xl shadow-teal-500/30 scale-105";
        sub.textContent = "Inhale deeply through your nose into belly (4s)";
      } else if (breathingPhase === 1) { // Hold (Full)
        action.textContent = "Hold";
        action.className = "text-sm font-black uppercase tracking-widest text-blue-300";
        ring.className = "w-44 h-44 rounded-full border-4 border-blue-400 bg-blue-500/20 flex flex-col items-center justify-center transition-all duration-500 shadow-xl shadow-blue-500/20 scale-105";
        sub.textContent = "Hold lungs full with relaxed shoulders (4s)";
      } else if (breathingPhase === 2) { // Exhale
        action.textContent = "Exhale";
        action.className = "text-sm font-black uppercase tracking-widest text-indigo-300";
        ring.className = "w-36 h-36 rounded-full border-4 border-indigo-400 bg-indigo-500/15 flex flex-col items-center justify-center transition-all duration-1000 shadow-lg shadow-indigo-500/20 scale-95";
        sub.textContent = "Exhale slowly through slightly parted lips (4s)";
      } else { // Hold (Empty)
        action.textContent = "Hold";
        action.className = "text-sm font-black uppercase tracking-widest text-slate-300";
        ring.className = "w-36 h-36 rounded-full border-4 border-slate-500 bg-slate-800/40 flex flex-col items-center justify-center transition-all duration-500 shadow scale-95";
        sub.textContent = "Hold lungs empty in pure stillness (4s)";
      }
    }

    function resetBreathingDisplay() {
      const ring = document.getElementById('breathingRing');
      const action = document.getElementById('breathingActionText');
      const count = document.getElementById('breathingCounterText');
      if (ring && action && count) {
        ring.className = "w-40 h-40 rounded-full border-4 border-teal-500/40 bg-teal-500/10 flex flex-col items-center justify-center transition-all duration-1000 shadow-2xl shadow-teal-500/20";
        action.textContent = "Inhale";
        count.textContent = "4s";
      }
    }

    // --- Trader Execution Contract & Penalty Strikes ---
    let penaltyStrikes = 0;

    function initPenaltyStrikes() {
      const saved = localStorage.getItem('trader_penalty_strikes');
      penaltyStrikes = saved !== null ? parseInt(saved) : 0;
      updateStrikesUI();
    }

    function openTraderContractModal() {
      updateStrikesUI();
      const modal = document.getElementById('traderContractModal');
      if (modal) modal.classList.remove('hidden');
    }

    function closeTraderContractModal() {
      const modal = document.getElementById('traderContractModal');
      if (modal) modal.classList.add('hidden');
    }

    function updateStrikesUI() {
      const headerText = document.getElementById('headerStrikesText');
      const headerBadge = document.getElementById('headerDemeritBadge');
      const disp = document.getElementById('contractActiveStrikesDisp');
      const status = document.getElementById('contractStatusDisp');

      if (headerText) headerText.textContent = `Strikes: ${penaltyStrikes}/3`;
      if (disp) disp.textContent = `${penaltyStrikes} / 3`;

      if (penaltyStrikes === 0) {
        if (headerBadge) headerBadge.className = "px-2.5 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm";
        if (disp) disp.className = "text-2xl font-black font-mono text-emerald-400 mt-0.5";
        if (status) { status.textContent = "CLEAN RECORD"; status.className = "text-sm font-bold text-emerald-400 mt-2"; }
      } else if (penaltyStrikes === 1) {
        if (headerBadge) headerBadge.className = "px-2.5 py-1.5 rounded-lg bg-amber-500/10 border border-amber-500/30 text-amber-300 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm";
        if (disp) disp.className = "text-2xl font-black font-mono text-amber-400 mt-0.5";
        if (status) { status.textContent = "STRIKE 1 (WARNING)"; status.className = "text-sm font-bold text-amber-400 mt-2"; }
      } else if (penaltyStrikes === 2) {
        if (headerBadge) headerBadge.className = "px-2.5 py-1.5 rounded-lg bg-orange-500/10 border border-orange-500/30 text-orange-400 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm";
        if (disp) disp.className = "text-2xl font-black font-mono text-orange-400 mt-0.5";
        if (status) { status.textContent = "STRIKE 2 (0.25% RISK CAP)"; status.className = "text-sm font-bold text-orange-400 mt-2"; }
      } else {
        if (headerBadge) headerBadge.className = "px-2.5 py-1.5 rounded-lg bg-rose-500/10 border border-rose-500/30 text-rose-400 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm animate-pulse";
        if (disp) disp.className = "text-2xl font-black font-mono text-rose-400 mt-0.5";
        if (status) { status.textContent = "STRIKE 3 (DEMOTED TO PHASE 1)"; status.className = "text-sm font-bold text-rose-400 mt-2"; }
      }
    }

    function logPenaltyStrike() {
      const reason = prompt("Enter the execution rule breached (e.g., traded past 10:30, widened stop, revenge entered):");
      if (!reason) return;

      penaltyStrikes = Math.min(3, penaltyStrikes + 1);
      localStorage.setItem('trader_penalty_strikes', penaltyStrikes);
      updateStrikesUI();

      if (penaltyStrikes >= 3) {
        alert("🚨 3 STRIKES ACCUMULATED! Execution Contract breached. Automatic demotion back to Phase 1 (Day 1) enforced.");
        resetToPhase1();
      } else {
        alert(`⚠️ Strike ${penaltyStrikes}/3 logged: "${reason}". Honor your commitments.`);
      }
      dispatchAccountabilityAlert("KILL_SWITCH", { reason: `Penalty Strike ${penaltyStrikes}/3: ${reason}` });
    }

    function clearPenaltyStrikes() {
      if (confirm("Reset penalty strikes to 0/3? Only proceed if you have completed 5 consecutive 100% compliant trading sessions.")) {
        penaltyStrikes = 0;
        localStorage.setItem('trader_penalty_strikes', 0);
        updateStrikesUI();
        alert("Penalty strikes cleared! Keep executing with institutional discipline.");
      }
    }

    // --- Multi-Strategy Attribution Table ---
    function renderStrategyAttribution(trades) {
      const tbody = document.getElementById('strategyAttributionTableBody');
      const bestPill = document.getElementById('bestStrategyPill');
      if (!tbody) return;

      const strategies = {};
      trades.forEach(t => {
        const s = t.setup_name || "1m Pullback to 9EMA";
        if (!strategies[s]) {
          strategies[s] = { count: 0, wins: 0, totalR: 0, netPnL: 0, grossWin: 0, grossLoss: 0 };
        }
        const net = parseFloat(t.net_pnl) || 0;
        const r = parseFloat(t.r_multiple) || 0;
        strategies[s].count++;
        strategies[s].netPnL += net;
        strategies[s].totalR += r;
        if (net > 0) {
          strategies[s].wins++;
          strategies[s].grossWin += net;
        } else if (net < 0) {
          strategies[s].grossLoss += Math.abs(net);
        }
      });

      if (Object.keys(strategies).length === 0) {
        tbody.innerHTML = `<tr><td colspan="7" class="text-center py-4 text-slate-500">No strategy trades logged.</td></tr>`;
        return;
      }

      let bestName = "";
      let bestNetR = -999;

      tbody.innerHTML = Object.entries(strategies).map(([name, data]) => {
        const wr = data.count > 0 ? (data.wins / data.count) * 100 : 0;
        const pf = data.grossLoss > 0 ? (data.grossWin / data.grossLoss).toFixed(2) : (data.grossWin > 0 ? "99.0" : "0.00");
        const pnl = Math.round(data.netPnL);
        const r = data.totalR;

        if (r > bestNetR && data.count >= 1) {
          bestNetR = r;
          bestName = name;
        }

        let grade = "Grade A (Prime)";
        let gradeClass = "bg-emerald-500/20 text-emerald-300 border-emerald-500/30";
        if (wr < 45 || pnl < 0) {
          grade = "Leaking Capital";
          gradeClass = "bg-rose-500/20 text-rose-300 border-rose-500/30";
        } else if (wr < 55) {
          grade = "Grade B (Moderate)";
          gradeClass = "bg-blue-500/20 text-blue-300 border-blue-500/30";
        }

        return `
          <tr class="hover:bg-slate-900/40 transition">
            <td class="py-2.5 px-3 font-semibold text-white font-sans">${name}</td>
            <td class="py-2.5 px-2 text-center text-slate-300">${data.count}</td>
            <td class="py-2.5 px-2 text-center font-bold ${wr >= 50 ? 'text-emerald-400' : 'text-amber-400'}">${wr.toFixed(0)}%</td>
            <td class="py-2.5 px-2 text-center font-bold ${r >= 0 ? 'text-emerald-400' : 'text-rose-400'}">${r >= 0 ? '+' : ''}${r.toFixed(2)}R</td>
            <td class="py-2.5 px-2 text-center text-blue-400 font-bold">${pf}</td>
            <td class="py-2.5 px-2 text-right font-bold ${pnl >= 0 ? 'text-emerald-400' : 'text-rose-400'}">₹${pnl.toLocaleString('en-IN')}</td>
            <td class="py-2.5 px-3 text-center">
              <span class="text-[10px] font-bold px-2 py-0.5 rounded border ${gradeClass}">${grade}</span>
            </td>
          </tr>
        `;
      }).join('');

      if (bestPill && bestName) {
        bestPill.textContent = bestName;
      }
    }
    """

    # Hook initPenaltyStrikes on DOM ready
    content = content.replace(
        "renderPhaseTracker();",
        "renderPhaseTracker();\n      initPenaltyStrikes();"
    )

    # Hook renderStrategyAttribution in renderAllChartsAndMetrics
    content = content.replace(
        "computeVaRAndRecovery(trades);",
        "computeVaRAndRecovery(trades);\n      renderStrategyAttribution(trades);"
    )

    # Hook Strategy Filter into renderTradesTable
    old_render_filter = """      const outcomeVal = document.getElementById('outcomeFilter').value;
      const searchVal = document.getElementById('tradeTableSearch').value.toLowerCase().trim();

      const filtered = tradesData.filter(t => {
        if (outcomeVal !== 'ALL' && t.outcome !== outcomeVal) return false;"""

    new_render_filter = """      const outcomeVal = document.getElementById('outcomeFilter').value;
      const strategyElem = document.getElementById('strategyFilter');
      const strategyVal = strategyElem ? strategyElem.value : 'ALL';
      const searchVal = document.getElementById('tradeTableSearch').value.toLowerCase().trim();

      const filtered = tradesData.filter(t => {
        if (outcomeVal !== 'ALL' && t.outcome !== outcomeVal) return false;
        if (strategyVal !== 'ALL' && (t.setup_name || '') !== strategyVal) return false;"""

    if old_render_filter in content:
        content = content.replace(old_render_filter, new_render_filter, 1)

    # Inject v12_js_engine before closing script
    assert "  </script>" in content, "Failed to find closing script tag"
    content = content.replace("  </script>", f"{v12_js_engine}\n  </script>", 1)

    # Write files
    for path in [OUT_PUBLIC, OUT_DELIV, OUT_BRAIN]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully generated v12: {path} ({len(content)} bytes)")

if __name__ == "__main__":
    build_v12()
