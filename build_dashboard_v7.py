"""
Builder script to generate Trader Execution Reset System Command Center v7.
Splits the crunched analytics and metrics across 4 dedicated, spacious tabs:
1. ⚡ Live Execution & Ledger
2. 📈 Performance & Equity Curves
3. 🧠 Edge Diagnostics & Leaks (15-min Heatmap, Setup Expectancy, Day-of-Week, Tilt Correlation, Hold Asymmetry, Streaks)
4. 🎲 Quant Risk & Monte Carlo (Kelly, Risk of Ruin, Sortino/Sharpe, Cost Drag, 30-Day Monte Carlo 1,000 Runs)
"""

import os

HTML_V7 = r'''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Trader Execution Reset System — Institutional Command Center</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: { 50: '#f0fdf4', 500: '#10b981', 600: '#059669', 700: '#047857' },
            darkbg: '#080D1A',
            cardbg: '#111827',
            cardborder: '#1F2937'
          }
        }
      }
    }
  </script>
  <style>
    body { background-color: #080D1A; color: #E2E8F0; font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    .glass-card { background: rgba(17, 24, 39, 0.85); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.08); }
    .glass-card-hover:hover { border-color: rgba(59, 130, 246, 0.4); }
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #080D1A; }
    ::-webkit-scrollbar-thumb { background: #1F2937; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #374151; }
    .tab-btn.active { background-color: #2563EB; color: #ffffff; border-color: #3B82F6; box-shadow: 0 0 15px rgba(37, 99, 235, 0.4); }
    .tab-btn:not(.active) { background-color: #111827; color: #94A3B8; border-color: #1F2937; }
    @media print {
      body * { visibility: hidden; }
      #weeklyReviewModalContent, #weeklyReviewModalContent * { visibility: visible; }
      #weeklyReviewModalContent { position: absolute; left: 0; top: 0; width: 100%; background: white !important; color: black !important; }
    }
  </style>
</head>
<body class="min-h-screen pb-16">
  <!-- Hidden File Inputs -->
  <input type="file" id="csvFileInput" accept=".csv,.json,text/csv,application/json" class="hidden" onchange="handleFileImport(event)">
  <input type="file" id="fyersFileInput" accept=".csv,text/csv" class="hidden" onchange="handleFyersFileImport(event)">
  <input type="file" id="vaultFileInput" accept=".json,application/json" class="hidden" onchange="handleVaultRestore(event)">

  <!-- Sticky Top Execution Command Bar -->
  <header class="sticky top-0 z-50 glass-card border-b border-slate-800 px-4 lg:px-8 py-3">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-3">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-emerald-500 to-blue-600 flex items-center justify-center font-black text-white shadow-lg shadow-emerald-500/20">
          ⚡
        </div>
        <div>
          <h1 class="text-base font-extrabold text-white tracking-tight flex items-center gap-2">
            Trader Execution Reset System
            <span class="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
              Phase 1 Active (Days 1–3)
            </span>
          </h1>
          <p class="text-xs text-slate-400">Intraday 1-Min NSE Equities &bull; 09:15–10:30 AM IST &bull; Target RR &ge; 2.2 &bull; Max 2 Trades/Day</p>
        </div>
      </div>

      <!-- Live Terminal Status, IST Clock, Window Guard & Indicators -->
      <div class="flex items-center gap-2.5 text-xs flex-wrap justify-end">
        <div class="bg-slate-900/90 border border-slate-800 px-3 py-1.5 rounded-lg flex items-center gap-2 font-mono">
          <span class="text-slate-400">🕒 IST:</span>
          <span id="headerLiveISTClock" class="font-bold text-white text-xs">--:--:-- IST</span>
        </div>

        <div id="headerWindowPill" class="px-2.5 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-bold flex items-center gap-1.5">
          <span id="headerWindowDot" class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span id="headerWindowText">Window Active</span>
        </div>

        <button id="soundToggleBtn" onclick="toggleSound()" class="px-2.5 py-1.5 rounded-lg bg-slate-800/80 border border-slate-700 text-slate-300 hover:text-white flex items-center gap-1.5 transition">
          <span id="soundIcon">🔊</span>
          <span id="soundText" class="font-medium">Audio ON</span>
        </button>

        <div class="bg-slate-900/90 border border-slate-800 px-3 py-1.5 rounded-lg flex items-center gap-2">
          <span class="text-slate-400">Capital:</span>
          <span class="font-bold text-white font-mono" id="headerStartingCapDisplay">₹200,000</span>
          <span class="text-slate-600">|</span>
          <span class="text-slate-400">Current:</span>
          <span class="font-bold font-mono" id="headerCurrentCapDisplay">₹200,000</span>
        </div>

        <div id="cooldownHeaderBadge" class="hidden px-2.5 py-1.5 rounded-lg bg-amber-500/10 border border-amber-500/30 text-amber-400 font-mono font-bold flex items-center gap-1.5">
          <span>⏳</span>
          <span id="cooldownTimerText">30:00</span>
        </div>

        <div id="headerKillSwitchBadge" class="px-2.5 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-medium flex items-center gap-1.5">
          <span id="headerDailyStatusText">Today: 0/2 Trades</span>
        </div>

        <a href="/api/download" download="D3_Tracking_Spreadsheet.xlsx" class="px-3 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white font-semibold transition flex items-center gap-1.5 shadow-sm">
          <span>📥</span>
          <span>Download .XLSX</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Live Trading Window Closed Alert Banner (When past 10:30 AM IST) -->
  <div id="windowClosedBanner" class="hidden bg-gradient-to-r from-indigo-950/90 via-slate-900 to-indigo-950/90 border-b border-indigo-500/40 px-4 py-2.5 text-center text-xs font-semibold text-indigo-200">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <div class="flex items-center gap-2">
        <span class="text-base">🛑</span>
        <span><strong>09:15–10:30 AM IST TRADING WINDOW CLOSED:</strong> Intraday momentum edge closes at 10:30 AM. Preserving capital. Real-time entries locked.</span>
      </div>
      <label class="flex items-center gap-2 text-xs text-indigo-300 cursor-pointer">
        <input type="checkbox" id="historicalLoggingOverride" onchange="toggleHistoricalMode(this.checked)" class="rounded bg-slate-800 border-indigo-500">
        <span>Enable Past Trade Logging Mode</span>
      </label>
    </div>
  </div>

  <!-- Cooldown Active Alert Banner -->
  <div id="cooldownBanner" class="hidden bg-gradient-to-r from-amber-950/80 via-amber-900/60 to-amber-950/80 border-b border-amber-500/40 px-4 py-2.5 text-center text-xs font-semibold text-amber-200">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <div class="flex items-center gap-2">
        <span class="text-base">⚠️</span>
        <span><strong>MANDATORY 30-MIN LOSS COOLDOWN ACTIVE:</strong> Loss registered. Step away from your screens immediately. Next trade entry is locked for <span id="cooldownCountdownSpan" class="font-mono font-bold text-amber-300 text-sm">30:00</span>.</span>
      </div>
      <button onclick="overrideCooldown()" class="text-[11px] underline text-amber-400 hover:text-white transition">Override (Emergency Only)</button>
    </div>
  </div>

  <!-- Daily Circuit Breaker Banner -->
  <div id="circuitBreakerBanner" class="hidden bg-gradient-to-r from-red-950/90 via-rose-900/80 to-red-950/90 border-b border-red-500/50 px-4 py-2.5 text-center text-xs font-semibold text-rose-200">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <div class="flex items-center gap-2">
        <span class="text-base">🚨</span>
        <span><strong>BROKER KILL SWITCH ENGAGED:</strong> Daily limit reached (<span id="circuitReasonText">2 Trades Max / 2 Losses Max</span>). Rule 3 strictly requires terminal shutdown. Walk away!</span>
      </div>
      <button onclick="overrideKillSwitch()" class="text-[11px] underline text-rose-300 hover:text-white transition">Discipline Override</button>
    </div>
  </div>

  <!-- Main Container -->
  <main class="max-w-7xl mx-auto px-4 lg:px-8 mt-6">
    <!-- Top Tab Navigation Controls & Action Strip (4 SPACIOUS TABS) -->
    <div class="flex flex-col xl:flex-row items-center justify-between gap-4 border-b border-slate-800 pb-4">
      <!-- 4 Responsive Tab Navigation Buttons -->
      <div class="flex items-center gap-2 w-full xl:w-auto overflow-x-auto pb-1 xl:pb-0">
        <button id="tabBtn1" onclick="switchTab(1)" class="tab-btn active px-4 py-2.5 rounded-xl font-bold text-xs sm:text-sm border flex items-center gap-2 transition duration-200 whitespace-nowrap">
          <span>⚡</span>
          <span>Live Execution</span>
        </button>
        <button id="tabBtn2" onclick="switchTab(2)" class="tab-btn px-4 py-2.5 rounded-xl font-bold text-xs sm:text-sm border flex items-center gap-2 transition duration-200 whitespace-nowrap">
          <span>📈</span>
          <span>Performance &amp; Equity</span>
        </button>
        <button id="tabBtn3" onclick="switchTab(3)" class="tab-btn px-4 py-2.5 rounded-xl font-bold text-xs sm:text-sm border flex items-center gap-2 transition duration-200 whitespace-nowrap">
          <span>🧠</span>
          <span>Edge &amp; Leaks</span>
        </button>
        <button id="tabBtn4" onclick="switchTab(4)" class="tab-btn px-4 py-2.5 rounded-xl font-bold text-xs sm:text-sm border flex items-center gap-2 transition duration-200 whitespace-nowrap">
          <span>🎲</span>
          <span>Quant Risk &amp; Monte Carlo</span>
        </button>
      </div>

      <!-- Global Actions Strip -->
      <div class="flex items-center gap-2 w-full xl:w-auto justify-end flex-wrap">
        <button onclick="openWeeklyReviewModal()" class="px-3 py-2 rounded-lg bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-400 border border-indigo-500/30 font-medium text-xs flex items-center gap-1.5 transition">
          <span>📝</span>
          <span>Weekly Review (D5)</span>
        </button>
        <button onclick="triggerFyersImport()" class="px-3 py-2 rounded-lg bg-orange-600/20 hover:bg-orange-600/30 text-orange-400 border border-orange-500/30 font-medium text-xs flex items-center gap-1.5 transition">
          <span>⚡</span>
          <span>Import FYERS</span>
        </button>
        <button onclick="triggerImport()" class="px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 font-medium text-xs flex items-center gap-1.5 transition">
          <span>📁</span>
          <span>Import CSV</span>
        </button>
        <button onclick="exportTradesCSV()" class="px-3 py-2 rounded-lg bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-400 border border-emerald-500/30 font-medium text-xs flex items-center gap-1.5 transition">
          <span>💾</span>
          <span>Export CSV</span>
        </button>
        <button onclick="backupDatabaseVault()" class="px-2.5 py-2 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs transition" title="Download timestamped JSON Database Vault backup">
          <span>🛡️ Backup</span>
        </button>
        <button onclick="triggerVaultRestore()" class="px-2.5 py-2 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-slate-400 hover:text-white border border-slate-700 text-xs transition" title="Restore state from JSON Database Vault">
          <span>🔄 Restore</span>
        </button>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 1: LIVE EXECUTION & TRADE LOG -->
    <!-- ========================================== -->
    <div id="tabContent1" class="mt-6 space-y-6">
      
      <!-- Quick Trade Entry Card -->
      <section class="glass-card rounded-2xl p-6 shadow-2xl relative overflow-hidden">
        <div class="flex flex-col md:flex-row md:items-center justify-between pb-4 border-b border-slate-800/80 gap-3">
          <div>
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span class="text-emerald-400">⚡</span>
              <span>Fast Intraday Trade Logger</span>
            </h2>
            <p class="text-xs text-slate-400">Position Sizer (Presets + Custom ₹) &bull; Planned RR &ge; 2.2 Validation &bull; Real-time FYERS Costs</p>
          </div>
          
          <div class="flex items-center gap-2 bg-slate-900/90 border border-slate-800 px-3 py-1.5 rounded-xl">
            <span class="text-xs text-slate-400">Mindset State:</span>
            <span id="urgencyStateBadge" class="text-xs font-bold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
              Calm &amp; Focused (Level 2/10)
            </span>
          </div>
        </div>

        <form id="tradeForm" onsubmit="submitTrade(event)" class="mt-5 space-y-5">
          <!-- Row 1: Core Trade Parameters with 1-Click Position Sizing Engine -->
          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
            <div>
              <label class="block text-slate-400 text-[11px] font-semibold uppercase tracking-wider mb-1">Symbol (NSE)</label>
              <input type="text" id="symbol" required placeholder="RELIANCE" class="w-full bg-slate-900 border border-slate-700/80 rounded-xl px-3 py-2 text-white font-mono text-sm uppercase focus:outline-none focus:border-blue-500">
            </div>

            <div>
              <label class="block text-slate-400 text-[11px] font-semibold uppercase tracking-wider mb-1">Direction</label>
              <select id="direction" onchange="recalculateCalculators()" class="w-full bg-slate-900 border border-slate-700/80 rounded-xl px-3 py-2 text-white text-sm font-semibold focus:outline-none focus:border-blue-500">
                <option value="Long">LONG (Buy)</option>
                <option value="Short">SHORT (Sell)</option>
              </select>
            </div>

            <div>
              <label class="block text-slate-400 text-[11px] font-semibold uppercase tracking-wider mb-1">Entry Price (₹)</label>
              <input type="number" step="0.05" id="entry_price" required placeholder="2500.00" oninput="recalculateCalculators()" class="w-full bg-slate-900 border border-slate-700/80 rounded-xl px-3 py-2 text-white font-mono text-sm focus:outline-none focus:border-blue-500">
            </div>

            <div>
              <label class="block text-slate-400 text-[11px] font-semibold uppercase tracking-wider mb-1">Stop Loss (₹)</label>
              <input type="number" step="0.05" id="stop_price" required placeholder="2495.00" oninput="recalculateCalculators()" class="w-full bg-slate-900 border border-slate-700/80 rounded-xl px-3 py-2 text-white font-mono text-sm focus:outline-none focus:border-blue-500">
            </div>

            <div>
              <label class="block text-slate-400 text-[11px] font-semibold uppercase tracking-wider mb-1">Exit Price (₹)</label>
              <input type="number" step="0.05" id="exit_price" placeholder="2511.00" oninput="recalculateCalculators()" class="w-full bg-slate-900 border border-slate-700/80 rounded-xl px-3 py-2 text-white font-mono text-sm focus:outline-none focus:border-blue-500">
            </div>

            <div>
              <div class="flex justify-between items-center mb-1">
                <label class="block text-slate-400 text-[11px] font-semibold uppercase tracking-wider">Quantity</label>
                <button type="button" onclick="autoApplyPositionSize()" id="autoQtyBtn" class="text-[10px] text-blue-400 hover:text-white font-bold underline transition">
                  ⚡ Auto-Size
                </button>
              </div>
              <input type="number" step="1" id="qty" required placeholder="100" oninput="recalculateCalculators()" class="w-full bg-slate-900 border border-slate-700/80 rounded-xl px-3 py-2 text-white font-mono text-sm focus:outline-none focus:border-blue-500">
            </div>
          </div>

          <!-- Position Sizing Calibration Strip with Custom Risk -->
          <div class="bg-blue-950/20 border border-blue-500/20 rounded-xl p-3 flex flex-col md:flex-row items-center justify-between gap-3 text-xs">
            <div class="flex items-center gap-2 flex-wrap">
              <span class="text-blue-300 font-bold uppercase text-[10px]">Position Sizer:</span>
              <button type="button" onclick="setRiskMode(0.0025)" id="riskMode_025" class="risk-mode-btn px-2.5 py-1 rounded-lg bg-blue-600 text-white font-bold text-[11px]">0.25% (₹500)</button>
              <button type="button" onclick="setRiskMode(0.0050)" id="riskMode_050" class="risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]">0.50% (₹1,000)</button>
              <button type="button" onclick="setRiskMode('custom')" id="riskMode_custom" class="risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]">Custom ₹</button>
              
              <!-- Custom Rupee Risk Input -->
              <div id="customRiskContainer" class="hidden items-center gap-1 bg-slate-900 border border-slate-700 rounded-lg px-2 py-0.5">
                <span class="text-slate-400 font-mono text-xs">₹</span>
                <input type="number" id="customRiskInput" step="50" min="50" value="500" oninput="onCustomRiskChange(this.value)" class="w-20 bg-transparent text-white font-mono text-xs font-bold focus:outline-none" placeholder="Risk ₹">
              </div>

              <span class="text-slate-500">|</span>
              <span class="text-slate-400">Risk Capital:</span>
              <span id="calculatedRiskAmountDisp" class="font-mono font-bold text-white">₹500.00</span>
              <span id="riskPctBadge" class="text-[10px] text-blue-400 font-mono">(0.25%)</span>
            </div>

            <div class="flex items-center gap-3 font-mono text-[11px]">
              <div>
                <span class="text-slate-400">Max Sized Qty:</span>
                <span id="sizedQtyDisp" class="font-bold text-emerald-400">0 shs</span>
              </div>
              <div>
                <span class="text-slate-400">MIS 5x Margin:</span>
                <span id="misMarginDisp" class="font-bold text-slate-300">₹0.00</span>
              </div>
              <button type="button" onclick="autoApplyPositionSize()" class="px-2.5 py-1 rounded-lg bg-blue-600/30 hover:bg-blue-600/50 text-blue-300 border border-blue-500/40 text-[10px] font-bold transition">
                Apply Qty
              </button>
            </div>
          </div>

          <!-- Row 2: Setup Name, Date, Entry Time, Exit Time, Urgency Slider -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3 items-center bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
            <div>
              <label class="block text-slate-400 text-[11px] font-semibold uppercase tracking-wider mb-1">Setup Type</label>
              <select id="setup_name" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-2.5 py-1.5 text-white text-xs">
                <option value="1m Pullback to 9EMA">1m Pullback to 9EMA (Rule Setup A)</option>
                <option value="1m VWAP Bounce">1m VWAP Bounce / Trend Contin.</option>
                <option value="1m Breakout &amp; Re-test">1m Opening Breakout Re-test</option>
                <option value="Other / Discretionary">Other Discretionary</option>
              </select>
            </div>

            <div>
              <label class="block text-slate-400 text-[11px] font-semibold uppercase tracking-wider mb-1">Date</label>
              <input type="date" id="trade_date" required class="w-full bg-slate-800 border border-slate-700 rounded-lg px-2 py-1.5 text-white text-xs font-mono">
            </div>

            <div>
              <label class="block text-slate-400 text-[11px] font-semibold uppercase tracking-wider mb-1">Entry &bull; Exit Time</label>
              <div class="flex gap-1.5">
                <input type="time" id="trade_time" required class="w-1/2 bg-slate-800 border border-slate-700 rounded-lg px-2 py-1.5 text-white text-xs font-mono" title="Entry Time">
                <input type="time" id="exit_time_input" class="w-1/2 bg-slate-800 border border-slate-700 rounded-lg px-2 py-1.5 text-white text-xs font-mono" title="Exit Time (Optional for hold duration)">
              </div>
            </div>

            <!-- Pre-Trade Urgency / Emotional State Slider -->
            <div class="lg:col-span-2">
              <div class="flex justify-between items-center mb-1">
                <label class="text-slate-400 text-[11px] font-semibold uppercase tracking-wider">
                  Pre-Trade Urgency / Emotion (1 = Zen &bull; 10 = Rushing / FOMO)
                </label>
                <span id="urgencyValueText" class="font-mono font-bold text-xs text-emerald-400">2 / 10</span>
              </div>
              <input type="range" id="urgencySlider" min="1" max="10" value="2" oninput="updateUrgencySlider(this.value)" class="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-blue-500">
              <p id="urgencyWarning" class="hidden text-[11px] text-amber-400 font-semibold mt-1 flex items-center gap-1">
                <span>⚠️ High Urgency detected (>6). Rule 4: Step away for 60s, take 3 deep breaths before entering.</span>
              </p>
            </div>
          </div>

          <!-- Live Math Validation Bar (Planned RR, Position Risk, FYERS Breakdown Preview) -->
          <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-3 p-3.5 bg-slate-950/60 rounded-xl border border-slate-800/80 text-xs">
            <div>
              <div class="text-slate-500 text-[10px] uppercase font-bold">Risk Per Share (R)</div>
              <div id="riskPerShareDisp" class="text-sm font-mono font-bold text-slate-200">₹0.00</div>
            </div>
            <div>
              <div class="text-slate-500 text-[10px] uppercase font-bold">Planned Target (2.2R)</div>
              <div id="minTargetDisp" class="text-sm font-mono font-bold text-blue-400">₹0.00</div>
            </div>
            <div>
              <div class="text-slate-500 text-[10px] uppercase font-bold">Planned RR</div>
              <div id="plannedRRDisp" class="text-sm font-mono font-bold text-slate-200">0.00</div>
            </div>
            <div>
              <div class="text-slate-500 text-[10px] uppercase font-bold">FYERS Statutory Cost</div>
              <div id="estimatedCostDisp" class="text-sm font-mono font-bold text-amber-400">₹0.00</div>
            </div>
            <div>
              <div class="text-slate-500 text-[10px] uppercase font-bold">Net P&amp;L (Est.)</div>
              <div id="previewNetPnLDisp" class="text-sm font-mono font-bold text-slate-200">₹0.00</div>
            </div>
            <div>
              <div class="text-slate-500 text-[10px] uppercase font-bold">Realized Net R</div>
              <div id="previewRealizedRDisp" class="text-sm font-mono font-bold text-slate-200">0.00 R</div>
            </div>
          </div>

          <!-- Pre-Execution Checklist & Submit Row -->
          <div class="flex flex-col lg:flex-row items-center justify-between gap-4 pt-2">
            <div class="flex flex-wrap items-center gap-3 text-xs text-slate-300">
              <span class="font-bold text-slate-400 uppercase text-[10px]">Pre-Flight:</span>
              <label class="flex items-center gap-1.5 cursor-pointer">
                <input type="checkbox" id="chk_time" checked class="rounded border-slate-700 bg-slate-800 text-blue-600 focus:ring-0">
                <span>09:15–10:30 Window</span>
              </label>
              <label class="flex items-center gap-1.5 cursor-pointer">
                <input type="checkbox" id="chk_rr" checked class="rounded border-slate-700 bg-slate-800 text-blue-600 focus:ring-0">
                <span>Planned RR &ge; 2.2</span>
              </label>
              <label class="flex items-center gap-1.5 cursor-pointer">
                <input type="checkbox" id="chk_sl" checked class="rounded border-slate-700 bg-slate-800 text-blue-600 focus:ring-0">
                <span>Hard Stop Defined</span>
              </label>
              <label class="flex items-center gap-1.5 cursor-pointer">
                <input type="checkbox" id="chk_chase" checked class="rounded border-slate-700 bg-slate-800 text-blue-600 focus:ring-0">
                <span>No Chasing (Limit Order)</span>
              </label>
              <label class="flex items-center gap-1.5 cursor-pointer">
                <input type="checkbox" id="chk_calm" checked class="rounded border-slate-700 bg-slate-800 text-blue-600 focus:ring-0">
                <span>Calm Mindset</span>
              </label>
            </div>

            <!-- Submit Button & Quick TSV Excel Copy -->
            <div class="flex items-center gap-2 w-full lg:w-auto justify-end">
              <button type="button" onclick="copyQuickLogTSV()" class="px-3.5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-semibold text-xs transition flex items-center gap-1.5" title="Copy row formatted for Excel Quick_Log sheet">
                <span>📋 Copy for Excel</span>
              </button>
              <button type="submit" id="submitTradeBtn" class="px-6 py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs uppercase tracking-wider transition shadow-lg shadow-emerald-600/30 flex items-center gap-2">
                <span>💾 Commit &amp; Log Trade</span>
              </button>
            </div>
          </div>
        </form>
      </section>

      <!-- Active Trades Ledger & Filters -->
      <section class="glass-card rounded-2xl p-6 shadow-2xl">
        <div class="flex flex-col sm:flex-row items-center justify-between pb-4 border-b border-slate-800 gap-3">
          <div>
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span>📋</span>
              <span>Executed Trades Ledger</span>
              <span id="tradesCountBadge" class="text-xs px-2 py-0.5 rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/20 font-mono">
                0 Trades
              </span>
            </h2>
            <p class="text-xs text-slate-400">Click any row to inspect FYERS breakdown, TradingView chart &amp; journal lessons</p>
          </div>

          <!-- Table Search, Filter & Utility Buttons -->
          <div class="flex items-center gap-2 w-full sm:w-auto flex-wrap justify-end">
            <input type="text" id="tradeTableSearch" placeholder="Search symbol, setup..." oninput="renderTradesTable()" class="bg-slate-900 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500">
            <select id="outcomeFilter" onchange="renderTradesTable()" class="bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white focus:outline-none focus:border-blue-500">
              <option value="ALL">All Outcomes</option>
              <option value="Win">Wins Only</option>
              <option value="Loss">Losses Only</option>
              <option value="Break-Even">Break-Even</option>
            </select>
            <button onclick="copyAllExcelTSV()" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs border border-slate-700 transition" title="Copy all visible trades in Excel TSV format">
              <span>📋 Copy All</span>
            </button>
            <button onclick="resetToBenchmarkData()" class="px-2.5 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-400 hover:text-white text-xs border border-slate-700 transition" title="Reload benchmark examples">
              <span>🔄 Reset Demo</span>
            </button>
            <button onclick="clearAllTrades()" class="px-2.5 py-1.5 rounded-lg bg-rose-950/30 hover:bg-rose-900/50 text-rose-400 text-xs border border-rose-900/40 transition" title="Clear all trades for live session">
              <span>🗑️ Clear</span>
            </button>
          </div>
        </div>

        <!-- Scrollable Responsive Trades Table -->
        <div class="overflow-x-auto mt-4 rounded-xl border border-slate-800">
          <table class="w-full text-left border-collapse text-xs">
            <thead>
              <tr class="bg-slate-900/90 text-slate-400 uppercase text-[10px] font-bold tracking-wider border-b border-slate-800">
                <th class="py-3 px-3">Trade ID</th>
                <th class="py-3 px-3">Date &bull; Time</th>
                <th class="py-3 px-3">Symbol</th>
                <th class="py-3 px-3">Side</th>
                <th class="py-3 px-3 text-right">Entry</th>
                <th class="py-3 px-3 text-right">Stop</th>
                <th class="py-3 px-3 text-right">Exit</th>
                <th class="py-3 px-3 text-right">Qty</th>
                <th class="py-3 px-3 text-center">Planned RR</th>
                <th class="py-3 px-3 text-right">Costs</th>
                <th class="py-3 px-3 text-right">Net P&amp;L</th>
                <th class="py-3 px-3 text-center">Realized R</th>
                <th class="py-3 px-3 text-center">Outcome</th>
                <th class="py-3 px-3 text-center">Actions</th>
              </tr>
            </thead>
            <tbody id="tradesTableBody" class="divide-y divide-slate-800/60 font-mono">
              <!-- Dynamically populated via JS -->
            </tbody>
          </table>
        </div>
      </section>
    </div>

    <!-- ========================================== -->
    <!-- TAB 2: PERFORMANCE & EQUITY CURVES -->
    <!-- ========================================== -->
    <div id="tabContent2" class="hidden mt-6 space-y-6">
      
      <!-- Filter Bar, Indiscipline Simulator Toggle & Capital Strip -->
      <section class="glass-card rounded-2xl p-5 shadow-xl flex flex-col md:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="text-xs font-semibold text-slate-400 uppercase text-[10px]">Filter Period:</span>
          <button onclick="setDateFilter('ALL')" id="dateBtn_ALL" class="date-filter-btn px-3 py-1.5 rounded-lg bg-blue-600 text-white font-bold text-xs transition">All Time</button>
          <button onclick="setDateFilter('TODAY')" id="dateBtn_TODAY" class="date-filter-btn px-3 py-1.5 rounded-lg bg-slate-800 text-slate-400 hover:text-white font-medium text-xs transition">Today</button>
          <button onclick="setDateFilter('7D')" id="dateBtn_7D" class="date-filter-btn px-3 py-1.5 rounded-lg bg-slate-800 text-slate-400 hover:text-white font-medium text-xs transition">Last 7 Days</button>
          <button onclick="setDateFilter('30D')" id="dateBtn_30D" class="date-filter-btn px-3 py-1.5 rounded-lg bg-slate-800 text-slate-400 hover:text-white font-medium text-xs transition">Last 30 Days</button>
        </div>

        <!-- Cost of Indiscipline / What-If Simulator Toggle -->
        <div class="flex items-center gap-2 bg-slate-900 border border-slate-800 px-3 py-1.5 rounded-xl">
          <label class="flex items-center gap-2 cursor-pointer text-xs">
            <input type="checkbox" id="indisciplineSimToggle" onchange="toggleIndisciplineSim(this.checked)" class="rounded bg-slate-800 border-slate-700 text-emerald-500 focus:ring-0">
            <span class="font-bold text-slate-300">🛡️ Filter Out Rule Violations (True Edge Simulator)</span>
          </label>
        </div>

        <!-- Starting Capital Input -->
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-2 bg-slate-900 border border-slate-700/80 px-3 py-1.5 rounded-xl">
            <span class="text-xs text-slate-400">Starting Capital (₹):</span>
            <input type="number" id="startingCapitalInput" value="200000" step="5000" onchange="updateStartingCapital(this.value)" class="w-24 bg-transparent text-white font-mono font-bold text-xs focus:outline-none text-right">
          </div>
          <button onclick="resetSeedCapitalPrompt()" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white text-xs transition" title="Reset capital to default ₹2,00,000">
            🔄
          </button>
        </div>
      </section>

      <!-- Indiscipline Impact Summary Alert -->
      <div id="indisciplineAlertBanner" class="hidden glass-card bg-emerald-950/30 border border-emerald-500/30 p-4 rounded-2xl flex items-center justify-between text-xs text-emerald-200">
        <div class="flex items-center gap-3">
          <span class="text-2xl">💡</span>
          <div>
            <div class="font-bold text-emerald-300">True Edge Simulation Active (100% Rule Compliance)</div>
            <p class="text-[11px] text-emerald-200/80">Hiding trades with rule violations or checklist scores &lt; 5/5 to reveal your actual execution edge.</p>
          </div>
        </div>
        <div class="text-right font-mono">
          <div class="text-[10px] text-slate-400 uppercase">Cost of Indiscipline</div>
          <div id="costOfIndisciplineAmount" class="font-bold text-rose-400 text-sm">-₹0.00</div>
        </div>
      </div>

      <!-- SPACIOUS CORE SCORECARD (6 KEY CARDS) -->
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
        <div class="glass-card rounded-2xl p-4 border border-slate-800">
          <div class="text-[10px] uppercase font-bold text-slate-400 tracking-wider">Total Net P&amp;L</div>
          <div class="text-xl font-black font-mono mt-1 text-emerald-400" id="statNetPnL">₹0.00</div>
          <div class="text-[10px] text-slate-500 mt-1" id="statGrossCostSub">Gross: ₹0 &bull; Cost: ₹0</div>
        </div>

        <div class="glass-card rounded-2xl p-4 border border-slate-800">
          <div class="text-[10px] uppercase font-bold text-slate-400 tracking-wider">Win Rate</div>
          <div class="text-xl font-black font-mono mt-1 text-white" id="statWinRate">0.0%</div>
          <div class="text-[10px] text-slate-500 mt-1" id="statWinLossRatio">0 Wins &bull; 0 Losses</div>
        </div>

        <div class="glass-card rounded-2xl p-4 border border-slate-800">
          <div class="text-[10px] uppercase font-bold text-slate-400 tracking-wider">Profit Factor</div>
          <div class="text-xl font-black font-mono mt-1 text-blue-400" id="statProfitFactor">0.00</div>
          <div class="text-[10px] text-slate-500 mt-1" id="statTotalRSub">Total Net R: 0.00R</div>
        </div>

        <div class="glass-card rounded-2xl p-4 border border-slate-800">
          <div class="text-[10px] uppercase font-bold text-slate-400 tracking-wider">Expectancy (R/Trade)</div>
          <div class="text-xl font-black font-mono mt-1 text-indigo-400" id="statExpectancyR">+0.00 R</div>
          <div class="text-[10px] text-slate-500 mt-1">Mathematical Edge</div>
        </div>

        <div class="glass-card rounded-2xl p-4 border border-slate-800">
          <div class="text-[10px] uppercase font-bold text-slate-400 tracking-wider">R-Efficiency Score</div>
          <div class="text-xl font-black font-mono mt-1 text-teal-400" id="statEfficiencyScore">0%</div>
          <div class="text-[10px] text-slate-500 mt-1" id="statEfficiencyDesc">Realized vs Planned</div>
        </div>

        <div class="glass-card rounded-2xl p-4 border border-slate-800">
          <div class="text-[10px] uppercase font-bold text-slate-400 tracking-wider">Discipline Adherence</div>
          <div class="text-xl font-black font-mono mt-1 text-emerald-400" id="statDisciplineScore">100%</div>
          <div class="text-[10px] text-slate-500 mt-1" id="statViolationsCount">0 Rule Violations</div>
        </div>
      </div>

      <!-- SPACIOUS MAIN CHARTS: CUMULATIVE EQUITY & DONUT DIAGNOSTICS -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- High-Resolution Wide Equity Curve -->
        <div class="lg:col-span-2 glass-card rounded-2xl p-6 border border-slate-800">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <h3 class="text-base font-bold text-white flex items-center gap-2">
                <span>📈</span>
                <span>Cumulative Net Equity Curve (₹)</span>
              </h3>
              <p class="text-xs text-slate-400">Account balance progression strictly factoring FYERS turnover &amp; statutory taxes</p>
            </div>
            <span class="text-xs font-mono font-bold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-lg border border-emerald-500/20" id="chartTotalReturnBadge">
              +0.00% ROI
            </span>
          </div>
          <div class="mt-4 relative" style="height: 320px;">
            <canvas id="equityChart"></canvas>
          </div>
        </div>

        <!-- Outcome & Rule Compliance Donut Charts -->
        <div class="glass-card rounded-2xl p-6 border border-slate-800 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
              <h3 class="text-base font-bold text-white flex items-center gap-2">
                <span>🎯</span>
                <span>Outcome &amp; Rules</span>
              </h3>
            </div>
            <div class="mt-4 grid grid-cols-2 gap-3">
              <div class="text-center">
                <div class="text-[10px] uppercase text-slate-400 font-bold mb-2">Trade Outcomes</div>
                <div class="relative" style="height: 140px;">
                  <canvas id="outcomeDonutChart"></canvas>
                </div>
              </div>
              <div class="text-center">
                <div class="text-[10px] uppercase text-slate-400 font-bold mb-2">Rule Discipline</div>
                <div class="relative" style="height: 140px;">
                  <canvas id="disciplineDonutChart"></canvas>
                </div>
              </div>
            </div>
          </div>
          <!-- Directional Edge Long vs Short Strip -->
          <div class="p-3.5 bg-slate-900/80 rounded-xl border border-slate-800 text-xs mt-4">
            <div class="text-[11px] uppercase font-bold text-slate-400 mb-2 flex justify-between">
              <span>Directional Edge</span>
              <span id="directionalBiasBadge" class="text-blue-400 font-bold">Balanced</span>
            </div>
            <div class="grid grid-cols-2 gap-2 text-center font-mono">
              <div class="bg-slate-950 p-2 rounded-lg">
                <span class="text-emerald-400 font-bold">LONG:</span>
                <span id="longStatsText" class="text-white block mt-0.5">0W (₹0)</span>
              </div>
              <div class="bg-slate-950 p-2 rounded-lg">
                <span class="text-rose-400 font-bold">SHORT:</span>
                <span id="shortStatsText" class="text-white block mt-0.5">0W (₹0)</span>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- ========================================== -->
    <!-- TAB 3: EDGE DIAGNOSTICS & LEAKS -->
    <!-- ========================================== -->
    <div id="tabContent3" class="hidden mt-6 space-y-6">
      
      <!-- Top Section: Behavioral Leak Diagnostics (Hold Duration, Streak Tracker, Tilt Correlation) -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        <!-- Trade Duration & Hold Asymmetry Card -->
        <div class="glass-card rounded-2xl p-5 border border-slate-800 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
              <h3 class="text-sm font-bold text-white flex items-center gap-2">
                <span>⏳</span>
                <span>Hold Duration Asymmetry</span>
              </h3>
              <span id="durationQualityBadge" class="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                Patient Exits
              </span>
            </div>
            <p class="text-[11px] text-slate-400 mt-2">
              Detects whether winners are being cut prematurely vs holding losers hoping for breakeven.
            </p>
            <div class="grid grid-cols-2 gap-3 mt-4 text-center font-mono">
              <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800">
                <div class="text-[10px] text-emerald-400 uppercase font-bold">Avg Win Hold</div>
                <div class="text-lg font-bold text-white mt-1" id="statAvgWinHold">8.5m</div>
                <div class="text-[9px] text-slate-500">Target Hold</div>
              </div>
              <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800">
                <div class="text-[10px] text-rose-400 uppercase font-bold">Avg Loss Hold</div>
                <div class="text-lg font-bold text-white mt-1" id="statAvgLossHold">3.2m</div>
                <div class="text-[9px] text-slate-500">Stop Respected</div>
              </div>
            </div>
          </div>
          <div class="p-2.5 bg-slate-900/70 rounded-xl border border-slate-800 text-[11px] text-slate-300 mt-4 flex items-center justify-between">
            <span>Asymmetry Ratio:</span>
            <span class="font-bold font-mono text-emerald-400" id="statHoldAsymmetryRatio">2.65x (Target &ge; 1.5x)</span>
          </div>
        </div>

        <!-- Streak & Consecutive Variance Tracker -->
        <div class="glass-card rounded-2xl p-5 border border-slate-800 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
              <h3 class="text-sm font-bold text-white flex items-center gap-2">
                <span>🔥</span>
                <span>Streak &amp; Variance Engine</span>
              </h3>
              <span id="currentStreakBadge" class="text-[10px] font-bold px-2 py-0.5 rounded bg-blue-500/10 text-blue-400 border border-blue-500/20">
                Streak: +2 Wins
              </span>
            </div>
            <p class="text-[11px] text-slate-400 mt-2">
              Tracks consecutive runs and recovery discipline immediately after mandatory 30m loss cooldowns.
            </p>
            <div class="grid grid-cols-2 gap-3 mt-4 text-center font-mono">
              <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800">
                <div class="text-[10px] text-slate-400 uppercase font-bold">Max Win Streak</div>
                <div class="text-lg font-bold text-emerald-400 mt-1" id="statMaxWinStreak">3 trades</div>
                <div class="text-[9px] text-slate-500">Consecutive Wins</div>
              </div>
              <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800">
                <div class="text-[10px] text-slate-400 uppercase font-bold">Max Loss Streak</div>
                <div class="text-lg font-bold text-rose-400 mt-1" id="statMaxLossStreak">1 trade</div>
                <div class="text-[9px] text-slate-500">Hard Cap &le; 2/day</div>
              </div>
            </div>
          </div>
          <div class="p-2.5 bg-slate-900/70 rounded-xl border border-slate-800 text-[11px] text-slate-300 mt-4 flex items-center justify-between">
            <span>Post-Loss Recovery Win%:</span>
            <span class="font-bold font-mono text-blue-400" id="statPostCooldownWR">100% (Disciplined)</span>
          </div>
        </div>

        <!-- Emotional Urgency Correlation Table -->
        <div class="glass-card rounded-2xl p-5 border border-slate-800 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
              <h3 class="text-sm font-bold text-white flex items-center gap-2">
                <span>🧠</span>
                <span>Emotional Tilt Correlation</span>
              </h3>
              <span class="text-[10px] text-slate-400">Pre-Trade Urgency</span>
            </div>
            <p class="text-[11px] text-slate-400 mt-2">
              Empirical correlation of your self-reported 1–10 mindset level vs trade success.
            </p>
            <div class="overflow-x-auto mt-3 rounded-xl border border-slate-800">
              <table class="w-full text-left text-xs font-mono">
                <thead>
                  <tr class="bg-slate-900 text-slate-400 uppercase text-[9px] border-b border-slate-800">
                    <th class="py-2 px-2.5">State</th>
                    <th class="py-2 px-1 text-center">Trades</th>
                    <th class="py-2 px-1 text-center">Win%</th>
                    <th class="py-2 px-2.5 text-right">Net P&amp;L</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-800/60 text-[11px]">
                  <tr>
                    <td class="py-2 px-2.5 text-emerald-400 font-bold font-sans">Calm (1–3)</td>
                    <td class="py-2 px-1 text-center text-slate-300" id="tiltTrades_1">0</td>
                    <td class="py-2 px-1 text-center font-bold text-white" id="tiltWR_1">0%</td>
                    <td class="py-2 px-2.5 text-right font-bold text-emerald-400" id="tiltPnL_1">₹0</td>
                  </tr>
                  <tr>
                    <td class="py-2 px-2.5 text-amber-400 font-bold font-sans">Alert (4–6)</td>
                    <td class="py-2 px-1 text-center text-slate-300" id="tiltTrades_2">0</td>
                    <td class="py-2 px-1 text-center font-bold text-white" id="tiltWR_2">0%</td>
                    <td class="py-2 px-2.5 text-right font-bold text-slate-300" id="tiltPnL_2">₹0</td>
                  </tr>
                  <tr>
                    <td class="py-2 px-2.5 text-rose-400 font-bold font-sans">Tilt Risk (7–10)</td>
                    <td class="py-2 px-1 text-center text-slate-300" id="tiltTrades_3">0</td>
                    <td class="py-2 px-1 text-center font-bold text-white" id="tiltWR_3">0%</td>
                    <td class="py-2 px-2.5 text-right font-bold text-rose-400" id="tiltPnL_3">₹0</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="text-[10px] text-slate-400 mt-2 text-center" id="tiltInsightNote">
            Calm trades deliver highest expectancy.
          </div>
        </div>

      </div>

      <!-- Bottom Section: Day-of-Week Matrix, 15-Min Heatmap & Setup Expectancy Matrix -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        <!-- Day-of-Week Edge Matrix -->
        <div class="glass-card rounded-2xl p-5 border border-slate-800">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <h3 class="text-sm font-bold text-white flex items-center gap-2">
                <span>📅</span>
                <span>Day-of-Week Edge Matrix</span>
              </h3>
              <p class="text-[11px] text-slate-400">Weekly session performance breakdown</p>
            </div>
          </div>

          <div class="overflow-x-auto mt-4 rounded-xl border border-slate-800">
            <table class="w-full text-left text-xs font-mono">
              <thead>
                <tr class="bg-slate-900 text-slate-400 uppercase text-[10px] border-b border-slate-800">
                  <th class="py-2.5 px-3 font-sans">Day</th>
                  <th class="py-2.5 px-1 text-center">Trades</th>
                  <th class="py-2.5 px-1 text-center">Win%</th>
                  <th class="py-2.5 px-1 text-center">PF</th>
                  <th class="py-2.5 px-2.5 text-right">Net P&amp;L</th>
                </tr>
              </thead>
              <tbody id="weekdayMatrixBody" class="divide-y divide-slate-800/60 text-xs">
                <!-- Dynamically populated via JS -->
              </tbody>
            </table>
          </div>

          <div class="mt-4 p-3 bg-slate-900/60 rounded-xl border border-slate-800 text-[11px] text-slate-400 flex justify-between items-center">
            <span>Peak: <strong class="text-emerald-400" id="bestWeekdayText">Tuesday</strong></span>
            <span>Drain: <strong class="text-rose-400" id="worstWeekdayText">None</strong></span>
          </div>
        </div>

        <!-- 15-Minute Time-of-Day Performance Heatmap -->
        <div class="glass-card rounded-2xl p-5 border border-slate-800">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <h3 class="text-sm font-bold text-white flex items-center gap-2">
                <span>⏱️</span>
                <span>Time-of-Day Performance Heatmap</span>
              </h3>
              <p class="text-[11px] text-slate-400">Testing your 09:15 to 10:30 window profitability</p>
            </div>
          </div>

          <div class="mt-4 relative" style="height: 160px;">
            <canvas id="timeOfDayChart"></canvas>
          </div>

          <div class="grid grid-cols-4 gap-1.5 mt-3 text-center">
            <div class="bg-slate-900/80 p-1.5 rounded-lg border border-slate-800">
              <div class="text-[9px] text-slate-400 font-bold">09:15–09:30</div>
              <div class="text-xs font-mono font-bold text-white mt-0.5" id="todPnL_1">₹0.00</div>
              <div class="text-[8px] text-slate-500" id="todCount_1">0 trds</div>
            </div>
            <div class="bg-slate-900/80 p-1.5 rounded-lg border border-slate-800">
              <div class="text-[9px] text-slate-400 font-bold">09:30–10:00</div>
              <div class="text-xs font-mono font-bold text-white mt-0.5" id="todPnL_2">₹0.00</div>
              <div class="text-[8px] text-slate-500" id="todCount_2">0 trds</div>
            </div>
            <div class="bg-slate-900/80 p-1.5 rounded-lg border border-slate-800">
              <div class="text-[9px] text-slate-400 font-bold">10:00–10:30</div>
              <div class="text-xs font-mono font-bold text-white mt-0.5" id="todPnL_3">₹0.00</div>
              <div class="text-[8px] text-slate-500" id="todCount_3">0 trds</div>
            </div>
            <div class="bg-slate-900/80 p-1.5 rounded-lg border border-slate-800">
              <div class="text-[9px] text-slate-400 font-bold">Post 10:30</div>
              <div class="text-xs font-mono font-bold text-rose-400 mt-0.5" id="todPnL_4">₹0.00</div>
              <div class="text-[8px] text-slate-500" id="todCount_4">0 trds</div>
            </div>
          </div>
        </div>

        <!-- Setup Expectancy Matrix Table -->
        <div class="glass-card rounded-2xl p-5 border border-slate-800 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
              <h3 class="text-sm font-bold text-white flex items-center gap-2">
                <span>🎯</span>
                <span>Setup Expectancy Matrix</span>
              </h3>
              <span class="text-[10px] text-slate-400">By Strategy</span>
            </div>

            <div class="overflow-x-auto mt-4 rounded-xl border border-slate-800">
              <table class="w-full text-left text-xs">
                <thead>
                  <tr class="bg-slate-900 text-slate-400 uppercase text-[10px] border-b border-slate-800">
                    <th class="py-2.5 px-2 font-sans">Setup</th>
                    <th class="py-2.5 px-1 text-center">Trds</th>
                    <th class="py-2.5 px-1 text-center">Win%</th>
                    <th class="py-2.5 px-1 text-center">PF</th>
                    <th class="py-2.5 px-2 text-right">Net P&amp;L</th>
                  </tr>
                </thead>
                <tbody id="setupMatrixBody" class="divide-y divide-slate-800/60 font-mono text-xs">
                  <!-- Populated via JS -->
                </tbody>
              </table>
            </div>
          </div>

          <div class="mt-4 p-2.5 bg-blue-950/20 border border-blue-500/20 rounded-xl text-[10px] text-blue-300">
            💡 Prioritize setups with positive Net R and eliminate losing variants.
          </div>
        </div>

      </div>

    </div>

    <!-- ========================================== -->
    <!-- TAB 4: QUANT RISK & MONTE CARLO -->
    <!-- ========================================== -->
    <div id="tabContent4" class="hidden mt-6 space-y-6">
      
      <!-- Top Row: Institutional Quant Risk Scorecard -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <!-- Kelly Criterion Card -->
        <div class="glass-card rounded-2xl p-5 border border-blue-500/20 bg-blue-950/10">
          <div class="flex items-center justify-between">
            <span class="text-[11px] uppercase font-bold text-blue-400 tracking-wider">Kelly Criterion (f*)</span>
            <span class="text-[9px] px-1.5 py-0.5 rounded bg-blue-500/20 text-blue-300 font-bold" id="kellyStatusBadge">Safe Sizing</span>
          </div>
          <div class="text-2xl font-black font-mono mt-2 text-white" id="statKellyFraction">0.00%</div>
          <div class="text-xs text-slate-400 mt-2" id="statKellyRecSub">Quarter-Kelly: 0.35% (Recommended)</div>
        </div>

        <!-- Risk of Ruin (RoR) Card -->
        <div class="glass-card rounded-2xl p-5 border border-emerald-500/20 bg-emerald-950/10">
          <div class="flex items-center justify-between">
            <span class="text-[11px] uppercase font-bold text-emerald-400 tracking-wider">Risk of Ruin (RoR)</span>
            <span class="text-[9px] px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold">10% DD Probability</span>
          </div>
          <div class="text-2xl font-black font-mono mt-2 text-white" id="statRiskOfRuin">0.0%</div>
          <div class="text-xs text-slate-400 mt-2" id="statRoRSub">20% DD Risk: &lt; 0.01%</div>
        </div>

        <!-- Sortino & Sharpe Ratio Card -->
        <div class="glass-card rounded-2xl p-5 border border-purple-500/20 bg-purple-950/10">
          <div class="flex items-center justify-between">
            <span class="text-[11px] uppercase font-bold text-purple-400 tracking-wider">Sortino Ratio</span>
            <span class="text-[9px] px-1.5 py-0.5 rounded bg-purple-500/20 text-purple-300 font-bold">Downside Adjusted</span>
          </div>
          <div class="text-2xl font-black font-mono mt-2 text-white" id="statSortinoRatio">0.00</div>
          <div class="text-xs text-slate-400 mt-2" id="statSharpeSub">Sharpe: 0.00 (Annualized)</div>
        </div>

        <!-- FYERS Commission Friction & Turnover Drag Card -->
        <div class="glass-card rounded-2xl p-5 border border-amber-500/20 bg-amber-950/10">
          <div class="flex items-center justify-between">
            <span class="text-[11px] uppercase font-bold text-amber-400 tracking-wider">FYERS Cost Drag %</span>
            <span class="text-[9px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-bold" id="costDragGrade">Optimal Friction</span>
          </div>
          <div class="text-2xl font-black font-mono mt-2 text-white" id="statCostDragPct">0.0%</div>
          <div class="text-xs text-slate-400 mt-2" id="statTurnoverChurnSub">Turnover: ₹0 (₹0 / ₹1 retained)</div>
        </div>
      </div>

      <!-- Spacious High-Resolution 30-Day Monte Carlo Compound Growth Projector -->
      <section class="glass-card rounded-2xl p-6 border border-slate-800">
        <div class="flex flex-col sm:flex-row items-center justify-between pb-4 border-b border-slate-800 gap-3">
          <div>
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <span>🚀</span>
              <span>30-Day Monte Carlo Compound Growth Projector (1,000 Iterations)</span>
            </h3>
            <p class="text-xs text-slate-400">Simulating 60 future trades (2 trades/day &times; 30 days) using empirical payoff ratio and win-rate</p>
          </div>
          <button onclick="runMonteCarloSimulation()" class="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs flex items-center gap-1.5 transition shadow-lg shadow-blue-600/30">
            <span>🎲 Re-Run 1,000 Simulations</span>
          </button>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-4 gap-6 mt-6">
          <div class="lg:col-span-3 relative" style="height: 320px;">
            <canvas id="monteCarloChart"></canvas>
          </div>
          
          <div class="flex flex-col justify-around bg-slate-900/70 p-5 rounded-xl border border-slate-800 space-y-4">
            <div>
              <div class="text-xs uppercase font-bold text-emerald-400">95th Percentile (Bull Case)</div>
              <div class="text-xl font-black font-mono text-white mt-1" id="mcPerc95">₹0.00</div>
              <div class="text-xs text-slate-400 mt-0.5">Optimal execution streak</div>
            </div>
            <div class="pt-3 border-t border-slate-800">
              <div class="text-xs uppercase font-bold text-blue-400">50th Percentile (Median Expected)</div>
              <div class="text-xl font-black font-mono text-white mt-1" id="mcPerc50">₹0.00</div>
              <div class="text-xs text-slate-400 mt-0.5">Most realistic 30-day target</div>
            </div>
            <div class="pt-3 border-t border-slate-800">
              <div class="text-xs uppercase font-bold text-rose-400">5th Percentile (Drawdown Floor)</div>
              <div class="text-xl font-black font-mono text-white mt-1" id="mcPerc5">₹0.00</div>
              <div class="text-xs text-slate-400 mt-0.5">Stress-tested worst variance</div>
            </div>
          </div>
        </div>
      </section>

    </div>
  </main>

  <!-- ========================================== -->
  <!-- MODAL 1: TRADE INSPECTION & JOURNAL MODAL -->
  <!-- ========================================== -->
  <div id="tradeModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
    <div class="glass-card bg-slate-900 rounded-2xl max-w-2xl w-full border border-slate-700 shadow-2xl p-6 relative">
      <div class="flex items-center justify-between pb-4 border-b border-slate-800">
        <div class="flex items-center gap-3">
          <span class="text-xl">🔍</span>
          <div>
            <h3 class="text-base font-bold text-white flex items-center gap-2" id="modalTradeTitle">
              Trade T-001 &bull; RELIANCE
            </h3>
            <p class="text-xs text-slate-400" id="modalTradeSubtitle">2026-10-20 &bull; 09:25 AM</p>
          </div>
        </div>
        <button onclick="closeTradeModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition">✕</button>
      </div>

      <div class="mt-4 space-y-4">
        <div class="grid grid-cols-4 gap-2 text-center">
          <div class="bg-slate-950 p-2 rounded-xl border border-slate-800">
            <div class="text-[10px] text-slate-400 uppercase">Gross P&amp;L</div>
            <div class="text-xs font-mono font-bold text-white mt-0.5" id="modalGrossPnL">₹0.00</div>
          </div>
          <div class="bg-slate-950 p-2 rounded-xl border border-slate-800">
            <div class="text-[10px] text-slate-400 uppercase">FYERS Costs</div>
            <div class="text-xs font-mono font-bold text-amber-400 mt-0.5" id="modalCosts">₹0.00</div>
          </div>
          <div class="bg-slate-950 p-2 rounded-xl border border-slate-800">
            <div class="text-[10px] text-slate-400 uppercase">Net P&amp;L</div>
            <div class="text-xs font-mono font-bold text-emerald-400 mt-0.5" id="modalNetPnL">₹0.00</div>
          </div>
          <div class="bg-slate-950 p-2 rounded-xl border border-slate-800">
            <div class="text-[10px] text-slate-400 uppercase">Realized R</div>
            <div class="text-xs font-mono font-bold text-blue-400 mt-0.5" id="modalRealizedR">+0.00 R</div>
          </div>
        </div>

        <div class="bg-slate-950/70 p-3.5 rounded-xl border border-slate-800 text-xs">
          <div class="text-[11px] font-bold text-slate-300 uppercase tracking-wider mb-2 flex items-center justify-between">
            <span>🧾 FYERS Statutory Charges Breakdown</span>
            <span class="text-[10px] text-slate-500">Intraday Equity (NSE)</span>
          </div>
          <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-[11px] font-mono" id="modalChargesGrid">
            <!-- Dynamically populated -->
          </div>
        </div>

        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-semibold text-slate-300">TradingView Chart View</span>
            <a id="modalTVLink" href="#" target="_blank" class="px-2.5 py-1 rounded-lg bg-blue-600/30 text-blue-300 hover:text-white border border-blue-500/40 text-xs font-medium transition flex items-center gap-1">
              <span>📈 Open TV Chart</span>
              <span>↗</span>
            </a>
          </div>
          <div id="modalScreenshotContainer" class="hidden pt-2">
            <img id="modalScreenshotImg" src="" alt="Chart Screenshot" class="w-full max-h-48 object-cover rounded-lg border border-slate-700">
          </div>
        </div>

        <div class="space-y-2">
          <label class="block text-xs font-semibold text-slate-300">Journal Lesson &amp; Mental Notes</label>
          <textarea id="modalLessonInput" rows="3" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 font-sans" placeholder="What worked? Did you follow your 9EMA entry criteria? How was your mental clarity?"></textarea>
        </div>

        <div class="flex items-center justify-between pt-3 border-t border-slate-800">
          <button onclick="deleteTradeFromModal()" class="px-3 py-2 rounded-xl bg-rose-600/20 hover:bg-rose-600/30 text-rose-400 border border-rose-500/30 text-xs font-bold transition">
            Delete Trade
          </button>
          <button onclick="saveModalJournal()" class="px-5 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold transition">
            Save Journal Notes
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL 2: FYERS TRADEBOOK PARSER PREVIEW -->
  <!-- ========================================== -->
  <div id="fyersModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
    <div class="glass-card bg-slate-900 rounded-2xl max-w-3xl w-full border border-slate-700 shadow-2xl p-6 relative">
      <div class="flex items-center justify-between pb-4 border-b border-slate-800">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-400 flex items-center justify-center font-bold">⚡</div>
          <div>
            <h3 class="text-base font-bold text-white">FYERS Tradebook CSV Parser</h3>
            <p class="text-xs text-slate-400">Auto-pairing BUY &amp; SELL executions via FIFO matching</p>
          </div>
        </div>
        <button onclick="closeFyersModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition">✕</button>
      </div>

      <div class="mt-4 space-y-4">
        <p class="text-xs text-slate-300">
          The parser detected and consolidated the following round-trip intraday trades from your FYERS tradebook:
        </p>

        <div class="max-h-64 overflow-y-auto rounded-xl border border-slate-800">
          <table class="w-full text-left text-xs">
            <thead>
              <tr class="bg-slate-950 text-slate-400 uppercase text-[10px] border-b border-slate-800">
                <th class="py-2.5 px-3">Symbol</th>
                <th class="py-2.5 px-2">Side</th>
                <th class="py-2.5 px-2 text-right">Entry</th>
                <th class="py-2.5 px-2 text-right">Exit</th>
                <th class="py-2.5 px-2 text-right">Qty</th>
                <th class="py-2.5 px-2 text-right">Net P&amp;L</th>
                <th class="py-2.5 px-3 text-center">Outcome</th>
              </tr>
            </thead>
            <tbody id="fyersPreviewTableBody" class="divide-y divide-slate-800/60 font-mono">
              <!-- Populated via parser -->
            </tbody>
          </table>
        </div>

        <div class="flex items-center justify-between pt-3 border-t border-slate-800">
          <button onclick="closeFyersModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold">
            Cancel
          </button>
          <button onclick="commitFyersParsedTrades()" class="px-5 py-2 rounded-xl bg-gradient-to-r from-orange-600 to-amber-600 hover:from-orange-500 hover:to-amber-500 text-white text-xs font-bold shadow-lg shadow-orange-600/30">
            Confirm &amp; Import Matched Trades
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL 3: AUTOMATED WEEKLY REVIEW REPORT (D5) -->
  <!-- ========================================== -->
  <div id="weeklyReviewModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
    <div id="weeklyReviewModalContent" class="glass-card bg-slate-900 rounded-2xl max-w-3xl w-full border border-slate-700 shadow-2xl p-6 relative max-h-[90vh] overflow-y-auto">
      <div class="flex items-center justify-between pb-4 border-b border-slate-800">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-400 flex items-center justify-center font-bold">📝</div>
          <div>
            <h3 class="text-base font-bold text-white">Weekly Governance Review Audit (D5)</h3>
            <p class="text-xs text-slate-400">Institutional Performance &amp; Phase 1 Audit</p>
          </div>
        </div>
        <button onclick="closeWeeklyReviewModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition">✕</button>
      </div>

      <div class="mt-4 space-y-5 text-xs text-slate-300">
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
          <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
            <div class="text-[10px] text-slate-400 uppercase">Week Net P&amp;L</div>
            <div class="text-sm font-bold font-mono text-emerald-400 mt-1" id="wrNetPnL">₹0.00</div>
          </div>
          <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
            <div class="text-[10px] text-slate-400 uppercase">Win Rate</div>
            <div class="text-sm font-bold font-mono text-white mt-1" id="wrWinRate">0%</div>
          </div>
          <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
            <div class="text-[10px] text-slate-400 uppercase">Total FYERS Costs</div>
            <div class="text-sm font-bold font-mono text-amber-400 mt-1" id="wrCosts">₹0.00</div>
          </div>
          <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
            <div class="text-[10px] text-slate-400 uppercase">Discipline Score</div>
            <div class="text-sm font-bold font-mono text-emerald-400 mt-1" id="wrDiscipline">100%</div>
          </div>
        </div>

        <div class="bg-slate-950/70 p-4 rounded-xl border border-slate-800 space-y-2">
          <div class="font-bold text-slate-200 uppercase text-[11px] mb-1">Phase 1 (Days 1–3) Graduation Criteria Audit</div>
          <div class="space-y-1.5" id="wrGraduationCriteriaList">
            <!-- Dynamically populated -->
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div class="bg-slate-950/70 p-3 rounded-xl border border-emerald-500/20">
            <div class="text-[10px] uppercase font-bold text-emerald-400">Best Execution of the Week</div>
            <div class="mt-1 font-mono text-white font-bold" id="wrBestTradeText">--</div>
            <p class="text-[11px] text-slate-400 mt-1" id="wrBestTradeLesson">--</p>
          </div>
          <div class="bg-slate-950/70 p-3 rounded-xl border border-rose-500/20">
            <div class="text-[10px] uppercase font-bold text-rose-400">Biggest Loss / Leak</div>
            <div class="mt-1 font-mono text-white font-bold" id="wrWorstTradeText">--</div>
            <p class="text-[11px] text-slate-400 mt-1" id="wrWorstTradeLesson">--</p>
          </div>
        </div>

        <div class="space-y-3">
          <div class="font-bold text-slate-200 uppercase text-[11px]">Weekend Self-Audit Reflection</div>
          <div>
            <label class="block text-[11px] text-slate-400 mb-1">1. Did you honor the 30-minute cooldown without exception after every loss?</label>
            <input type="text" id="wrQ1" value="Yes, walked away immediately from screens." class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 text-xs text-white">
          </div>
          <div>
            <label class="block text-[11px] text-slate-400 mb-1">2. What one rule improvement will you focus on next week?</label>
            <input type="text" id="wrQ2" value="Wait strictly for candle confirmation on 1m pullback; avoid entering early." class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 text-xs text-white">
          </div>
        </div>

        <div class="flex items-center justify-between pt-3 border-t border-slate-800">
          <button onclick="copyWeeklyReportMD()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition flex items-center gap-1.5">
            <span>📋 Copy Markdown Report</span>
          </button>
          <div class="flex gap-2">
            <button onclick="window.print()" class="px-4 py-2 rounded-xl bg-indigo-600/30 hover:bg-indigo-600/50 text-indigo-300 border border-indigo-500/40 text-xs font-semibold transition">
              🖨️ Print / Save PDF
            </button>
            <button onclick="closeWeeklyReviewModal()" class="px-5 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold transition">
              Done
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- APPLICATION LOGIC SCRIPT -->
  <script>
    let startingCapital = 200000;
    let activeDateFilter = 'ALL';
    let currentTab = 1;
    let soundEnabled = true;
    let tradesData = [];
    let cooldownEndTime = null;
    let cooldownInterval = null;
    let activeModalTradeId = null;
    let pendingFyersTrades = [];
    let riskModeType = 'percent';
    let riskModePercent = 0.0025;
    let customRiskAmount = 500;
    let isIndisciplineSimActive = false;
    let isHistoricalOverride = false;

    let chartEquity = null;
    let chartOutcomeDonut = null;
    let chartDisciplineDonut = null;
    let chartTimeOfDay = null;
    let chartMonteCarlo = null;

    const DEFAULT_BENCHMARK_TRADES = [
      {
        id: "T-001",
        date: "2026-10-20",
        day: "Tue",
        time: "09:25",
        exit_time: "09:34",
        hold_duration: 9,
        symbol: "RELIANCE",
        direction: "Long",
        setup_name: "1m Pullback to 9EMA",
        scanner_alert_time: "09:23",
        htf_ok: "Y",
        no_chase: "Y",
        stop_defined: "Y",
        target_price: 2511.0,
        rr_planned: 2.2,
        risk_percent: 0.0025,
        risk_amount: 500.0,
        entry_price: 2500.0,
        stop_price: 2495.0,
        exit_price: 2511.0,
        qty: 100,
        gross_pnl: 1100.0,
        costs: 135.1,
        net_pnl: 964.9,
        r_multiple: 1.93,
        outcome: "Win",
        checklist_score: 5,
        rule_violation: "N",
        violation_type: "None",
        emotion_before: 2,
        emotion_during: 3,
        emotion_after: 2,
        trade_valid: "Y",
        lesson: "Followed plan, entry at limit, patient exit at 2.2R target.",
        screenshot_link: "https://www.tradingview.com/chart/?symbol=NSE:RELIANCE"
      },
      {
        id: "T-002",
        date: "2026-10-20",
        day: "Tue",
        time: "10:05",
        exit_time: "10:08",
        hold_duration: 3,
        symbol: "TCS",
        direction: "Short",
        setup_name: "1m Pullback to 9EMA",
        scanner_alert_time: "10:02",
        htf_ok: "Y",
        no_chase: "Y",
        stop_defined: "Y",
        target_price: 3478.0,
        rr_planned: 2.2,
        risk_percent: 0.0025,
        risk_amount: 500.0,
        entry_price: 3500.0,
        stop_price: 3510.0,
        exit_price: 3510.0,
        qty: 50,
        gross_pnl: -500.0,
        costs: 108.54,
        net_pnl: -608.54,
        r_multiple: -1.22,
        outcome: "Loss",
        checklist_score: 5,
        rule_violation: "N",
        violation_type: "None",
        emotion_before: 3,
        emotion_during: 4,
        emotion_after: 3,
        trade_valid: "Y",
        lesson: "Setup failed normally; respected stop without hesitation; entered 30m cooldown.",
        screenshot_link: "https://www.tradingview.com/chart/?symbol=NSE:TCS"
      },
      {
        id: "T-003",
        date: "2026-10-21",
        day: "Wed",
        time: "09:40",
        exit_time: "09:48",
        hold_duration: 8,
        symbol: "INFY",
        direction: "Long",
        setup_name: "1m Breakout & Re-test",
        scanner_alert_time: "09:38",
        htf_ok: "Y",
        no_chase: "Y",
        stop_defined: "Y",
        target_price: 1461.0,
        rr_planned: 2.2,
        risk_percent: 0.0025,
        risk_amount: 500.0,
        entry_price: 1450.0,
        stop_price: 1445.0,
        exit_price: 1461.0,
        qty: 100,
        gross_pnl: 1100.0,
        costs: 98.31,
        net_pnl: 1001.69,
        r_multiple: 2.0,
        outcome: "Win",
        checklist_score: 5,
        rule_violation: "N",
        violation_type: "None",
        emotion_before: 2,
        emotion_during: 3,
        emotion_after: 2,
        trade_valid: "Y",
        lesson: "Good patience waiting for bar close confirmation. Exited at 2.2R target.",
        screenshot_link: "https://www.tradingview.com/chart/?symbol=NSE:INFY"
      }
    ];

    // --- Web Audio API Terminal Sound Synthesizer ---
    let audioCtx = null;
    function getAudioContext() {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
      return audioCtx;
    }

    function toggleSound() {
      soundEnabled = !soundEnabled;
      localStorage.setItem('soundEnabled', soundEnabled ? 'true' : 'false');
      updateSoundUI();
    }

    function updateSoundUI() {
      const icon = document.getElementById('soundIcon');
      const text = document.getElementById('soundText');
      if (soundEnabled) {
        icon.textContent = '🔊';
        text.textContent = 'Audio ON';
      } else {
        icon.textContent = '🔇';
        text.textContent = 'Muted';
      }
    }

    function playWinChime() {
      if (!soundEnabled) return;
      try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        [523.25, 659.25, 783.99].forEach((freq, idx) => {
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, now + idx * 0.08);
          gain.gain.setValueAtTime(0.001, now + idx * 0.08);
          gain.gain.exponentialRampToValueAtTime(0.15, now + idx * 0.08 + 0.02);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + idx * 0.08 + 0.35);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + idx * 0.08);
          osc.stop(now + idx * 0.08 + 0.36);
        });
      } catch(e) { console.warn("Audio chime error:", e); }
    }

    function playLossAlert() {
      if (!soundEnabled) return;
      try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        [220.0, 174.61].forEach((freq, idx) => {
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, now + idx * 0.12);
          gain.gain.setValueAtTime(0.001, now + idx * 0.12);
          gain.gain.exponentialRampToValueAtTime(0.2, now + idx * 0.12 + 0.02);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + idx * 0.12 + 0.4);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + idx * 0.12);
          osc.stop(now + idx * 0.12 + 0.42);
        });
      } catch(e) { console.warn("Audio chime error:", e); }
    }

    // --- Live IST Clock & Market Window Engine (09:15 to 10:30 AM) ---
    function updateISTMarketClock() {
      const now = new Date();
      const istTimeStr = now.toLocaleTimeString('en-US', { timeZone: 'Asia/Kolkata', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
      const [h, m, s] = istTimeStr.split(':').map(Number);
      const curMinutes = h * 60 + m;

      document.getElementById('headerLiveISTClock').textContent = `${istTimeStr} IST`;

      const pill = document.getElementById('headerWindowPill');
      const dot = document.getElementById('headerWindowDot');
      const text = document.getElementById('headerWindowText');
      const banner = document.getElementById('windowClosedBanner');
      const submitBtn = document.getElementById('submitTradeBtn');

      const openMin = 9 * 60 + 15;
      const closeMin = 10 * 60 + 30;

      if (curMinutes >= openMin && curMinutes < closeMin) {
        const remaining = closeMin - curMinutes;
        pill.className = 'px-2.5 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-bold flex items-center gap-1.5';
        dot.className = 'w-2 h-2 rounded-full bg-emerald-400 animate-pulse';
        text.textContent = `Active Window (${remaining}m left)`;
        banner.classList.add('hidden');
        if (!isCooldownActive() && !isCircuitActive()) {
          submitBtn.disabled = false;
          submitBtn.classList.remove('opacity-50', 'cursor-not-allowed');
        }
      } else if (curMinutes < openMin && curMinutes >= 9 * 60) {
        const toOpen = openMin - curMinutes;
        pill.className = 'px-2.5 py-1.5 rounded-lg bg-amber-500/10 border border-amber-500/30 text-amber-400 font-bold flex items-center gap-1.5';
        dot.className = 'w-2 h-2 rounded-full bg-amber-400';
        text.textContent = `Pre-Market (${toOpen}m to open)`;
        banner.classList.add('hidden');
      } else {
        pill.className = 'px-2.5 py-1.5 rounded-lg bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 font-bold flex items-center gap-1.5';
        dot.className = 'w-2 h-2 rounded-full bg-indigo-400';
        text.textContent = 'Window Closed';

        if (!isHistoricalOverride) {
          banner.classList.remove('hidden');
          submitBtn.disabled = true;
          submitBtn.classList.add('opacity-50', 'cursor-not-allowed');
        } else {
          banner.classList.add('hidden');
          submitBtn.disabled = false;
          submitBtn.classList.remove('opacity-50', 'cursor-not-allowed');
        }
      }
    }

    function toggleHistoricalMode(val) {
      isHistoricalOverride = val;
      updateISTMarketClock();
    }

    function isCooldownActive() {
      return cooldownEndTime && Date.now() < cooldownEndTime;
    }

    function isCircuitActive() {
      const todayStr = new Date().toISOString().split('T')[0];
      const todayTrades = tradesData.filter(t => t.date === todayStr);
      const todayLosses = todayTrades.filter(t => t.outcome === 'Loss');
      return todayTrades.length >= 2 || todayLosses.length >= 2;
    }

    // --- FYERS Intraday Equity Statutory Charges Exact Formula ---
    function computeFyersCharges(buyTurnover, sellTurnover) {
      const totalTurnover = buyTurnover + sellTurnover;
      const buyBrok = Math.min(buyTurnover * 0.0003, 20.0);
      const sellBrok = Math.min(sellTurnover * 0.0003, 20.0);
      const totalBrokerage = buyBrok + sellBrok;
      const stt = sellTurnover * 0.00025;
      const exchangeCharges = totalTurnover * 0.0000297;
      const sebiFee = totalTurnover * 0.0000001;
      const stampDuty = buyTurnover * 0.00003;
      const gst = (totalBrokerage + exchangeCharges + sebiFee) * 0.18;
      const totalCosts = totalBrokerage + stt + exchangeCharges + sebiFee + stampDuty + gst;

      return {
        buyTurnover,
        sellTurnover,
        totalTurnover,
        totalBrokerage,
        stt,
        exchangeCharges,
        sebiFee,
        stampDuty,
        gst,
        totalCosts
      };
    }

    // --- 1-Click Position Sizing Engine with Custom Risk Support ---
    function setRiskMode(mode) {
      const btn025 = document.getElementById('riskMode_025');
      const btn050 = document.getElementById('riskMode_050');
      const btnCust = document.getElementById('riskMode_custom');
      const custContainer = document.getElementById('customRiskContainer');

      if (mode === 0.0025) {
        riskModeType = 'percent';
        riskModePercent = 0.0025;
        btn025.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-blue-600 text-white font-bold text-[11px]';
        btn050.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
        btnCust.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
        custContainer.classList.add('hidden');
        custContainer.classList.remove('flex');
      } else if (mode === 0.0050) {
        riskModeType = 'percent';
        riskModePercent = 0.0050;
        btn050.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-blue-600 text-white font-bold text-[11px]';
        btn025.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
        btnCust.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
        custContainer.classList.add('hidden');
        custContainer.classList.remove('flex');
      } else if (mode === 'custom') {
        riskModeType = 'custom';
        btnCust.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-blue-600 text-white font-bold text-[11px]';
        btn025.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
        btn050.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
        custContainer.classList.remove('hidden');
        custContainer.classList.add('flex');
        const inputVal = parseFloat(document.getElementById('customRiskInput').value);
        if (inputVal > 0) customRiskAmount = inputVal;
      }
      recalculateCalculators();
    }

    function onCustomRiskChange(val) {
      const num = parseFloat(val);
      if (num > 0) {
        customRiskAmount = num;
        recalculateCalculators();
      }
    }

    function autoApplyPositionSize() {
      const entry = parseFloat(document.getElementById('entry_price').value) || 0;
      const stop = parseFloat(document.getElementById('stop_price').value) || 0;
      if (entry <= 0 || stop <= 0) {
        alert("Enter Entry Price and Stop Loss first to calculate position size.");
        return;
      }
      const riskPerShare = Math.abs(entry - stop);
      if (riskPerShare <= 0) return;

      const riskAmt = riskModeType === 'custom' ? customRiskAmount : (startingCapital * riskModePercent);
      const maxShares = Math.max(1, Math.floor(riskAmt / riskPerShare));
      document.getElementById('qty').value = maxShares;
      recalculateCalculators();
    }

    // --- Tab Switching (4 SPACIOUS TABS) ---
    function switchTab(tabNum) {
      currentTab = tabNum;
      for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`tabBtn${i}`);
        const content = document.getElementById(`tabContent${i}`);
        if (btn && content) {
          if (i === tabNum) {
            btn.classList.add('active');
            content.classList.remove('hidden');
          } else {
            btn.classList.remove('active');
            content.classList.add('hidden');
          }
        }
      }
      renderAllChartsAndMetrics();
    }

    // --- Urgency Slider Control ---
    function updateUrgencySlider(val) {
      const num = parseInt(val);
      const disp = document.getElementById('urgencyValueText');
      const badge = document.getElementById('urgencyStateBadge');
      const warn = document.getElementById('urgencyWarning');

      disp.textContent = `${num} / 10`;

      if (num <= 3) {
        disp.className = 'font-mono font-bold text-xs text-emerald-400';
        badge.className = 'text-xs font-bold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20';
        badge.textContent = `Calm & Focused (${num}/10)`;
        warn.classList.add('hidden');
      } else if (num <= 6) {
        disp.className = 'font-mono font-bold text-xs text-amber-400';
        badge.className = 'text-xs font-bold px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20';
        badge.textContent = `Moderate Alert (${num}/10)`;
        warn.classList.add('hidden');
      } else {
        disp.className = 'font-mono font-bold text-xs text-rose-400';
        badge.className = 'text-xs font-bold px-2 py-0.5 rounded-full bg-rose-500/10 text-rose-400 border border-rose-500/20 animate-pulse';
        badge.textContent = `Tilt Risk High (${num}/10)`;
        warn.classList.remove('hidden');
      }
    }

    // --- Cooldown & Anti-Tilt Circuit Breaker Engine ---
    function checkCooldownStatus() {
      const savedCooldown = localStorage.getItem('cooldownEndTime');
      if (savedCooldown) {
        const end = parseInt(savedCooldown);
        if (Date.now() < end) {
          startCooldownTimer(end);
          return;
        } else {
          clearCooldownTimer();
        }
      }
    }

    function triggerLossCooldown() {
      const end = Date.now() + 30 * 60 * 1000;
      localStorage.setItem('cooldownEndTime', end.toString());
      startCooldownTimer(end);
      playLossAlert();
    }

    function startCooldownTimer(endTime) {
      cooldownEndTime = endTime;
      const banner = document.getElementById('cooldownBanner');
      const badge = document.getElementById('cooldownHeaderBadge');
      banner.classList.remove('hidden');
      badge.classList.remove('hidden');

      if (cooldownInterval) clearInterval(cooldownInterval);

      updateCooldownDisplay();
      cooldownInterval = setInterval(updateCooldownDisplay, 1000);
    }

    function updateCooldownDisplay() {
      if (!cooldownEndTime) return;
      const remaining = cooldownEndTime - Date.now();
      if (remaining <= 0) {
        clearCooldownTimer();
        return;
      }
      const m = Math.floor(remaining / 60000);
      const s = Math.floor((remaining % 60000) / 1000);
      const str = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
      document.getElementById('cooldownCountdownSpan').textContent = str;
      document.getElementById('cooldownTimerText').textContent = str;
    }

    function clearCooldownTimer() {
      if (cooldownInterval) clearInterval(cooldownInterval);
      cooldownInterval = null;
      cooldownEndTime = null;
      localStorage.removeItem('cooldownEndTime');
      document.getElementById('cooldownBanner').classList.add('hidden');
      document.getElementById('cooldownHeaderBadge').classList.add('hidden');
    }

    function overrideCooldown() {
      if (confirm("⚠️ OVERRIDE COOLDOWN: Are you sure? Rule 2 requires 30 minutes away from screens after any loss to prevent emotional revenge trading.")) {
        clearCooldownTimer();
      }
    }

    function checkDailyCircuitBreaker() {
      const todayStr = new Date().toISOString().split('T')[0];
      const todayTrades = tradesData.filter(t => t.date === todayStr);
      const todayLosses = todayTrades.filter(t => t.outcome === 'Loss');
      
      const headerStatus = document.getElementById('headerDailyStatusText');
      const headerBadge = document.getElementById('headerKillSwitchBadge');
      const cbBanner = document.getElementById('circuitBreakerBanner');
      const cbReason = document.getElementById('circuitReasonText');

      headerStatus.textContent = `Today: ${todayTrades.length}/2 Trades (${todayLosses.length} Loss)`;

      if (todayTrades.length >= 2 || todayLosses.length >= 2) {
        cbBanner.classList.remove('hidden');
        if (todayLosses.length >= 2) {
          cbReason.textContent = "2 Losses Max Hit for the Day";
        } else {
          cbReason.textContent = "2 Trades Max Hit for the Day";
        }
        headerBadge.className = 'px-2.5 py-1.5 rounded-lg bg-rose-500/10 border border-rose-500/30 text-rose-400 font-bold flex items-center gap-1.5 animate-pulse';
      } else {
        cbBanner.classList.add('hidden');
        headerBadge.className = 'px-2.5 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-medium flex items-center gap-1.5';
      }
    }

    function overrideKillSwitch() {
      if (confirm("🚨 KILL SWITCH OVERRIDE: Proceed only if you are logging past back-office trades. Live trading after daily limits violates Phase 1 rules!")) {
        document.getElementById('circuitBreakerBanner').classList.add('hidden');
      }
    }

    // --- Starting Capital Management ---
    function initStartingCapital() {
      const saved = localStorage.getItem('startingCapital');
      if (saved) {
        startingCapital = parseFloat(saved) || 200000;
      }
      document.getElementById('startingCapitalInput').value = startingCapital;
      renderTopCapitalHeader();
    }

    function updateStartingCapital(val) {
      const num = parseFloat(val);
      if (num > 0) {
        startingCapital = num;
        localStorage.setItem('startingCapital', startingCapital.toString());
        renderTopCapitalHeader();
        recalculateCalculators();
        renderAllChartsAndMetrics();
      }
    }

    function resetSeedCapitalPrompt() {
      updateStartingCapital(200000);
      document.getElementById('startingCapitalInput').value = 200000;
    }

    function renderTopCapitalHeader() {
      document.getElementById('headerStartingCapDisplay').textContent = `₹${startingCapital.toLocaleString('en-IN')}`;
      const totalNetPnL = tradesData.reduce((acc, t) => acc + (parseFloat(t.net_pnl) || 0), 0);
      const currentCap = startingCapital + totalNetPnL;
      const curDisp = document.getElementById('headerCurrentCapDisplay');
      curDisp.textContent = `₹${Math.round(currentCap).toLocaleString('en-IN')}`;
      if (totalNetPnL >= 0) {
        curDisp.className = 'font-bold font-mono text-emerald-400';
      } else {
        curDisp.className = 'font-bold font-mono text-rose-400';
      }

      const btn025 = document.getElementById('riskMode_025');
      const btn050 = document.getElementById('riskMode_050');
      if (btn025) btn025.textContent = `0.25% (₹${Math.round(startingCapital * 0.0025).toLocaleString('en-IN')})`;
      if (btn050) btn050.textContent = `0.50% (₹${Math.round(startingCapital * 0.0050).toLocaleString('en-IN')})`;
    }

    // --- Date Filtering & Indiscipline Simulator ---
    function setDateFilter(filterType) {
      activeDateFilter = filterType;
      document.querySelectorAll('.date-filter-btn').forEach(btn => {
        btn.className = 'date-filter-btn px-3 py-1.5 rounded-lg bg-slate-800 text-slate-400 hover:text-white font-medium text-xs transition';
      });
      const activeBtn = document.getElementById(`dateBtn_${filterType}`);
      if (activeBtn) {
        activeBtn.className = 'date-filter-btn px-3 py-1.5 rounded-lg bg-blue-600 text-white font-bold text-xs transition';
      }
      renderAllChartsAndMetrics();
    }

    function toggleIndisciplineSim(checked) {
      isIndisciplineSimActive = checked;
      const banner = document.getElementById('indisciplineAlertBanner');
      if (checked) {
        banner.classList.remove('hidden');
      } else {
        banner.classList.add('hidden');
      }
      renderAllChartsAndMetrics();
    }

    function getFilteredTrades() {
      let filtered = [...tradesData];
      const today = new Date();
      const todayStr = today.toISOString().split('T')[0];

      if (activeDateFilter === 'TODAY') {
        filtered = filtered.filter(t => t.date === todayStr);
      } else if (activeDateFilter === '7D') {
        const cutoff = new Date(today.getTime() - 7 * 86400000).toISOString().split('T')[0];
        filtered = filtered.filter(t => t.date >= cutoff);
      } else if (activeDateFilter === '30D') {
        const cutoff = new Date(today.getTime() - 30 * 86400000).toISOString().split('T')[0];
        filtered = filtered.filter(t => t.date >= cutoff);
      }

      if (isIndisciplineSimActive) {
        filtered = filtered.filter(t => t.rule_violation !== 'Y' && (!t.checklist_score || t.checklist_score >= 5));
      }

      return filtered;
    }

    // --- Dynamic Form Real-Time Calculations ---
    function recalculateCalculators() {
      const entry = parseFloat(document.getElementById('entry_price').value) || 0;
      const stop = parseFloat(document.getElementById('stop_price').value) || 0;
      const exit = parseFloat(document.getElementById('exit_price').value) || 0;
      const qty = parseInt(document.getElementById('qty').value) || 0;
      const direction = document.getElementById('direction').value;

      const riskAmt = riskModeType === 'custom' ? customRiskAmount : (startingCapital * riskModePercent);
      document.getElementById('calculatedRiskAmountDisp').textContent = `₹${riskAmt.toFixed(2)}`;
      const effPct = startingCapital > 0 ? ((riskAmt / startingCapital) * 100).toFixed(2) : '0.00';
      const pctBadge = document.getElementById('riskPctBadge');
      if (pctBadge) pctBadge.textContent = `(${effPct}%)`;

      if (entry <= 0 || stop <= 0) {
        document.getElementById('riskPerShareDisp').textContent = '₹0.00';
        document.getElementById('minTargetDisp').textContent = '₹0.00';
        document.getElementById('plannedRRDisp').textContent = '0.00';
        document.getElementById('estimatedCostDisp').textContent = '₹0.00';
        document.getElementById('previewNetPnLDisp').textContent = '₹0.00';
        document.getElementById('previewRealizedRDisp').textContent = '0.00 R';
        document.getElementById('sizedQtyDisp').textContent = '0 shs';
        document.getElementById('misMarginDisp').textContent = '₹0.00';
        return;
      }

      const riskPerShare = Math.abs(entry - stop);
      document.getElementById('riskPerShareDisp').textContent = `₹${riskPerShare.toFixed(2)}`;

      const maxShares = Math.max(1, Math.floor(riskAmt / riskPerShare));
      document.getElementById('sizedQtyDisp').textContent = `${maxShares} shs`;
      const misMargin = (entry * maxShares) / 5.0;
      document.getElementById('misMarginDisp').textContent = `₹${Math.round(misMargin).toLocaleString('en-IN')}`;

      let minTarget = direction === 'Long' ? entry + 2.2 * riskPerShare : entry - 2.2 * riskPerShare;
      document.getElementById('minTargetDisp').textContent = `₹${minTarget.toFixed(2)}`;

      let plannedRR = 0;
      if (exit > 0) {
        const plannedReward = Math.abs(exit - entry);
        plannedRR = riskPerShare > 0 ? (plannedReward / riskPerShare) : 0;
      } else {
        plannedRR = 2.2;
      }
      const rrElem = document.getElementById('plannedRRDisp');
      rrElem.textContent = `${plannedRR.toFixed(2)} RR`;
      rrElem.className = plannedRR >= 2.2 ? 'text-sm font-mono font-bold text-emerald-400' : 'text-sm font-mono font-bold text-amber-400';

      if (qty > 0) {
        const actualExit = exit > 0 ? exit : minTarget;
        const buyTurnover = direction === 'Long' ? (entry * qty) : (actualExit * qty);
        const sellTurnover = direction === 'Long' ? (actualExit * qty) : (entry * qty);
        
        const fyers = computeFyersCharges(buyTurnover, sellTurnover);
        document.getElementById('estimatedCostDisp').textContent = `₹${fyers.totalCosts.toFixed(2)}`;

        let grossPnL = 0;
        if (exit > 0) {
          grossPnL = direction === 'Long' ? (exit - entry) * qty : (entry - exit) * qty;
        } else {
          grossPnL = direction === 'Long' ? (minTarget - entry) * qty : (entry - minTarget) * qty;
        }
        const netPnL = grossPnL - fyers.totalCosts;
        const totalRisk = riskPerShare * qty;
        const realizedR = totalRisk > 0 ? (netPnL / totalRisk) : 0;

        const pnlElem = document.getElementById('previewNetPnLDisp');
        pnlElem.textContent = `₹${netPnL.toFixed(2)}`;
        pnlElem.className = netPnL >= 0 ? 'text-sm font-mono font-bold text-emerald-400' : 'text-sm font-mono font-bold text-rose-400';

        const rElem = document.getElementById('previewRealizedRDisp');
        rElem.textContent = `${realizedR >= 0 ? '+' : ''}${realizedR.toFixed(2)} R`;
        rElem.className = realizedR >= 0 ? 'text-sm font-mono font-bold text-emerald-400' : 'text-sm font-mono font-bold text-rose-400';
      }
    }

    // --- Submit Trade ---
    async function submitTrade(e) {
      e.preventDefault();

      const urgencyVal = parseInt(document.getElementById('urgencySlider').value);
      if (urgencyVal > 6) {
        const proceed = confirm(`⚠️ HIGH EMOTIONAL URGENCY (${urgencyVal}/10): Phase 1 rules enforce high self-control. Do you certify you have verified the setup objectively without rushing?`);
        if (!proceed) return;
      }

      const symbol = document.getElementById('symbol').value.toUpperCase().trim();
      const direction = document.getElementById('direction').value;
      const entry = parseFloat(document.getElementById('entry_price').value);
      const stop = parseFloat(document.getElementById('stop_price').value);
      const exitInput = parseFloat(document.getElementById('exit_price').value);
      const qty = parseInt(document.getElementById('qty').value);
      const setupName = document.getElementById('setup_name').value;
      const date = document.getElementById('trade_date').value;
      const time = document.getElementById('trade_time').value;
      const exitTime = document.getElementById('exit_time_input').value || '';

      const riskPerShare = Math.abs(entry - stop);
      if (riskPerShare <= 0) {
        alert("Stop loss cannot equal Entry price.");
        return;
      }

      const exit = exitInput > 0 ? exitInput : (direction === 'Long' ? entry + 2.2 * riskPerShare : entry - 2.2 * riskPerShare);

      const buyTurnover = direction === 'Long' ? (entry * qty) : (exit * qty);
      const sellTurnover = direction === 'Long' ? (exit * qty) : (entry * qty);
      const fyers = computeFyersCharges(buyTurnover, sellTurnover);

      const grossPnL = direction === 'Long' ? (exit - entry) * qty : (entry - exit) * qty;
      const netPnL = grossPnL - fyers.totalCosts;
      const totalRisk = riskPerShare * qty;
      const realizedR = totalRisk > 0 ? (netPnL / totalRisk) : 0;
      const plannedRR = Math.abs(exit - entry) / riskPerShare;

      let outcome = 'Break-Even';
      if (netPnL > 10) outcome = 'Win';
      else if (netPnL < -10) outcome = 'Loss';

      let holdDuration = 6;
      if (exitTime && time) {
        const [h1, m1] = time.split(':').map(Number);
        const [h2, m2] = exitTime.split(':').map(Number);
        const diff = (h2 * 60 + m2) - (h1 * 60 + m1);
        if (diff > 0) holdDuration = diff;
      } else {
        holdDuration = outcome === 'Win' ? 8 : 3;
      }

      let score = 0;
      if (document.getElementById('chk_time').checked) score++;
      if (document.getElementById('chk_rr').checked) score++;
      if (document.getElementById('chk_sl').checked) score++;
      if (document.getElementById('chk_chase').checked) score++;
      if (document.getElementById('chk_calm').checked) score++;

      const ruleViolation = score < 5 ? 'Y' : 'N';

      const tradeObj = {
        id: `T-${String(tradesData.length + 1).padStart(3, '0')}`,
        date: date,
        day: new Date(date).toLocaleDateString('en-US', { weekday: 'short' }),
        time: time,
        exit_time: exitTime || time,
        hold_duration: holdDuration,
        symbol: symbol,
        direction: direction,
        setup_name: setupName,
        scanner_alert_time: time,
        htf_ok: 'Y',
        no_chase: 'Y',
        stop_defined: 'Y',
        target_price: parseFloat((direction === 'Long' ? entry + 2.2 * riskPerShare : entry - 2.2 * riskPerShare).toFixed(2)),
        rr_planned: parseFloat(plannedRR.toFixed(2)),
        risk_percent: parseFloat((totalRisk / startingCapital).toFixed(4)),
        risk_amount: totalRisk,
        entry_price: entry,
        stop_price: stop,
        exit_price: exit,
        qty: qty,
        gross_pnl: parseFloat(grossPnL.toFixed(2)),
        costs: parseFloat(fyers.totalCosts.toFixed(2)),
        net_pnl: parseFloat(netPnL.toFixed(2)),
        r_multiple: parseFloat(realizedR.toFixed(2)),
        outcome: outcome,
        checklist_score: score,
        rule_violation: ruleViolation,
        violation_type: ruleViolation === 'Y' ? 'Checklist Incomplete' : 'None',
        emotion_before: urgencyVal,
        emotion_during: 2,
        emotion_after: outcome === 'Win' ? 2 : 4,
        trade_valid: 'Y',
        lesson: outcome === 'Win' ? 'Executed strictly on 9EMA system, honored planned target.' : 'Honored stop loss immediately; taking mandatory 30m cooldown.',
        screenshot_link: `https://www.tradingview.com/chart/?symbol=NSE:${symbol}`
      };

      if (outcome === 'Win') {
        playWinChime();
      } else if (outcome === 'Loss') {
        triggerLossCooldown();
      }

      try {
        const resp = await fetch('/api/trades', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(tradeObj)
        });
        if (resp.ok) {
          const res = await resp.json();
          tradesData.push(res.trade || tradeObj);
        } else {
          tradesData.push(tradeObj);
        }
      } catch (err) {
        console.warn("Backend sync offline, saving locally:", err);
        tradesData.push(tradeObj);
      }

      saveTradesLocally();
      renderTradesTable();
      renderTopCapitalHeader();
      checkDailyCircuitBreaker();

      document.getElementById('symbol').value = '';
      document.getElementById('entry_price').value = '';
      document.getElementById('stop_price').value = '';
      document.getElementById('exit_price').value = '';
      document.getElementById('qty').value = '';
      document.getElementById('exit_time_input').value = '';
      recalculateCalculators();
    }

    // --- Save and Load Trades ---
    function saveTradesLocally() {
      localStorage.setItem('traderResetTrades', JSON.stringify(tradesData));
    }

    async function loadTrades() {
      try {
        const resp = await fetch('/api/trades');
        if (resp.ok) {
          const data = await resp.json();
          if (data && data.trades && data.trades.length > 0) {
            tradesData = data.trades;
            saveTradesLocally();
            renderTradesTable();
            renderTopCapitalHeader();
            checkDailyCircuitBreaker();
            return;
          }
        }
      } catch (err) {
        console.warn("Could not load from API, falling back to localStorage", err);
      }

      const saved = localStorage.getItem('traderResetTrades');
      if (saved) {
        try {
          tradesData = JSON.parse(saved);
        } catch(e) { tradesData = []; }
      }

      if (!tradesData || tradesData.length === 0) {
        tradesData = JSON.parse(JSON.stringify(DEFAULT_BENCHMARK_TRADES));
        saveTradesLocally();
      }

      renderTradesTable();
      renderTopCapitalHeader();
      checkDailyCircuitBreaker();
    }

    function resetToBenchmarkData() {
      if (confirm("Reload benchmark seed trades?")) {
        tradesData = JSON.parse(JSON.stringify(DEFAULT_BENCHMARK_TRADES));
        saveTradesLocally();
        syncTradesWithBackend();
        renderTradesTable();
        renderTopCapitalHeader();
        checkDailyCircuitBreaker();
        renderAllChartsAndMetrics();
      }
    }

    function clearAllTrades() {
      if (confirm("Are you sure you want to delete ALL trades to start completely fresh?")) {
        tradesData = [];
        saveTradesLocally();
        syncTradesWithBackend();
        renderTradesTable();
        renderTopCapitalHeader();
        checkDailyCircuitBreaker();
        renderAllChartsAndMetrics();
      }
    }

    // --- Database JSON Vault (Backup & Restore) ---
    function backupDatabaseVault() {
      const vaultData = {
        exportedAt: new Date().toISOString(),
        startingCapital: startingCapital,
        soundEnabled: soundEnabled,
        trades: tradesData
      };
      const blob = new Blob([JSON.stringify(vaultData, null, 2)], { type: 'application/json' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      const dateStr = new Date().toISOString().split('T')[0];
      link.download = `trader_vault_${dateStr}.json`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function triggerVaultRestore() {
      document.getElementById('vaultFileInput').click();
    }

    function handleVaultRestore(e) {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(evt) {
        try {
          const parsed = JSON.parse(evt.target.result);
          if (parsed && Array.isArray(parsed.trades)) {
            tradesData = parsed.trades;
            if (parsed.startingCapital) {
              updateStartingCapital(parsed.startingCapital);
            }
            saveTradesLocally();
            syncTradesWithBackend();
            renderTradesTable();
            renderTopCapitalHeader();
            checkDailyCircuitBreaker();
            renderAllChartsAndMetrics();
            alert(`🎉 Vault Restored! Successfully loaded ${tradesData.length} trades.`);
          } else {
            alert("Invalid Vault JSON structure.");
          }
        } catch(err) {
          alert("Error parsing Vault file: " + err.message);
        } finally {
          e.target.value = '';
        }
      };
      reader.readAsText(file);
    }

    // --- Render Trades Table ---
    function renderTradesTable() {
      const tbody = document.getElementById('tradesTableBody');
      const search = (document.getElementById('tradeTableSearch').value || '').toLowerCase();
      const outcomeFilter = document.getElementById('outcomeFilter').value;

      let filtered = [...tradesData];
      if (search) {
        filtered = filtered.filter(t => 
          (t.symbol && t.symbol.toLowerCase().includes(search)) ||
          (t.setup_name && t.setup_name.toLowerCase().includes(search)) ||
          (t.lesson && t.lesson.toLowerCase().includes(search))
        );
      }
      if (outcomeFilter !== 'ALL') {
        filtered = filtered.filter(t => t.outcome === outcomeFilter);
      }

      document.getElementById('tradesCountBadge').textContent = `${tradesData.length} Trades (${filtered.length} visible)`;

      if (filtered.length === 0) {
        tbody.innerHTML = `<tr><td colspan="14" class="text-center py-8 text-slate-500 font-sans">No trades found matching current filter.</td></tr>`;
        return;
      }

      const rows = [...filtered].reverse().map(t => {
        const isWin = t.outcome === 'Win';
        const isLoss = t.outcome === 'Loss';
        const pnlClass = isWin ? 'text-emerald-400 font-bold' : (isLoss ? 'text-rose-400 font-bold' : 'text-slate-300');
        const badgeClass = isWin 
          ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' 
          : (isLoss ? 'bg-rose-500/10 text-rose-400 border border-rose-500/20' : 'bg-slate-700 text-slate-300');

        const plannedRR = parseFloat(t.rr_planned || 2.2).toFixed(2);
        const realizedR = parseFloat(t.r_multiple || 0).toFixed(2);
        const netPnL = parseFloat(t.net_pnl || 0).toFixed(2);
        const costs = parseFloat(t.costs || 0).toFixed(2);

        return `
          <tr class="hover:bg-slate-800/40 transition border-b border-slate-800/50 cursor-pointer" onclick="openTradeModal('${t.id}')">
            <td class="py-2.5 px-3 font-bold text-blue-400">${t.id}</td>
            <td class="py-2.5 px-3 text-slate-400 font-sans text-[11px]">${t.date} <span class="text-slate-500">&bull;</span> ${t.time}</td>
            <td class="py-2.5 px-3 font-bold text-white">${t.symbol}</td>
            <td class="py-2.5 px-3">
              <span class="px-1.5 py-0.5 rounded text-[10px] font-bold ${t.direction === 'Long' ? 'bg-emerald-950 text-emerald-400 border border-emerald-800' : 'bg-rose-950 text-rose-400 border border-rose-800'}">
                ${t.direction}
              </span>
            </td>
            <td class="py-2.5 px-3 text-right text-slate-300">₹${Number(t.entry_price).toFixed(2)}</td>
            <td class="py-2.5 px-3 text-right text-rose-400/90">₹${Number(t.stop_price).toFixed(2)}</td>
            <td class="py-2.5 px-3 text-right text-slate-300">₹${Number(t.exit_price).toFixed(2)}</td>
            <td class="py-2.5 px-3 text-right text-slate-400">${t.qty}</td>
            <td class="py-2.5 px-3 text-center ${plannedRR >= 2.2 ? 'text-emerald-400' : 'text-amber-400'} font-bold">${plannedRR}</td>
            <td class="py-2.5 px-3 text-right text-amber-400/90 font-mono">₹${costs}</td>
            <td class="py-2.5 px-3 text-right font-mono ${pnlClass}">₹${netPnL}</td>
            <td class="py-2.5 px-3 text-center font-mono font-bold ${realizedR >= 0 ? 'text-emerald-400' : 'text-rose-400'}">
              ${realizedR >= 0 ? '+' : ''}${realizedR}R
            </td>
            <td class="py-2.5 px-3 text-center">
              <span class="px-2 py-0.5 rounded-full text-[10px] font-sans font-bold ${badgeClass}">${t.outcome}</span>
            </td>
            <td class="py-2.5 px-3 text-center" onclick="event.stopPropagation()">
              <button onclick="openTradeModal('${t.id}')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-[10px] font-sans font-semibold mr-1">
                🔍
              </button>
              <button onclick="deleteTrade('${t.id}')" class="px-2 py-1 bg-rose-950/40 hover:bg-rose-900/60 text-rose-400 rounded text-[10px] font-sans font-semibold">
                ✕
              </button>
            </td>
          </tr>
        `;
      }).join('');

      tbody.innerHTML = rows;
    }

    // --- Modal Trade Inspection & Journal ---
    function openTradeModal(tradeId) {
      const trade = tradesData.find(t => t.id === tradeId);
      if (!trade) return;
      activeModalTradeId = tradeId;

      document.getElementById('modalTradeTitle').innerHTML = `
        <span>Trade ${trade.id} &bull; ${trade.symbol}</span>
        <span class="px-2 py-0.5 rounded text-[11px] font-bold ${trade.direction === 'Long' ? 'bg-emerald-950 text-emerald-400 border border-emerald-800' : 'bg-rose-950 text-rose-400 border border-rose-800'}">
          ${trade.direction}
        </span>
      `;
      document.getElementById('modalTradeSubtitle').textContent = `${trade.date} (${trade.day || ''}) &bull; ${trade.time} IST &bull; Setup: ${trade.setup_name || 'Standard'}`;

      document.getElementById('modalGrossPnL').textContent = `₹${Number(trade.gross_pnl || 0).toFixed(2)}`;
      document.getElementById('modalCosts').textContent = `₹${Number(trade.costs || 0).toFixed(2)}`;
      
      const netElem = document.getElementById('modalNetPnL');
      netElem.textContent = `₹${Number(trade.net_pnl || 0).toFixed(2)}`;
      netElem.className = trade.net_pnl >= 0 ? 'text-xs font-mono font-bold text-emerald-400 mt-0.5' : 'text-xs font-mono font-bold text-rose-400 mt-0.5';

      const rElem = document.getElementById('modalRealizedR');
      const r = parseFloat(trade.r_multiple || 0);
      rElem.textContent = `${r >= 0 ? '+' : ''}${r.toFixed(2)} R`;
      rElem.className = r >= 0 ? 'text-xs font-mono font-bold text-blue-400 mt-0.5' : 'text-xs font-mono font-bold text-rose-400 mt-0.5';

      const buyTurnover = trade.direction === 'Long' ? (trade.entry_price * trade.qty) : (trade.exit_price * trade.qty);
      const sellTurnover = trade.direction === 'Long' ? (trade.exit_price * trade.qty) : (trade.entry_price * trade.qty);
      const fyers = computeFyersCharges(buyTurnover, sellTurnover);

      const chargesGrid = document.getElementById('modalChargesGrid');
      chargesGrid.innerHTML = `
        <div class="bg-slate-900 p-2 rounded">Buy Turnover: <span class="text-white">₹${buyTurnover.toFixed(2)}</span></div>
        <div class="bg-slate-900 p-2 rounded">Sell Turnover: <span class="text-white">₹${sellTurnover.toFixed(2)}</span></div>
        <div class="bg-slate-900 p-2 rounded">Total Brokerage: <span class="text-amber-300">₹${fyers.totalBrokerage.toFixed(2)}</span></div>
        <div class="bg-slate-900 p-2 rounded">STT (0.025% Sell): <span class="text-amber-300">₹${fyers.stt.toFixed(2)}</span></div>
        <div class="bg-slate-900 p-2 rounded">Exchange Chg (NSE): <span class="text-amber-300">₹${fyers.exchangeCharges.toFixed(2)}</span></div>
        <div class="bg-slate-900 p-2 rounded">SEBI Turnover Fee: <span class="text-amber-300">₹${fyers.sebiFee.toFixed(2)}</span></div>
        <div class="bg-slate-900 p-2 rounded">Stamp Duty: <span class="text-amber-300">₹${fyers.stampDuty.toFixed(2)}</span></div>
        <div class="bg-slate-900 p-2 rounded">GST (18%): <span class="text-amber-300">₹${fyers.gst.toFixed(2)}</span></div>
        <div class="bg-slate-900 p-2 rounded font-bold text-rose-300">Total Deductions: ₹${fyers.totalCosts.toFixed(2)}</div>
      `;

      const tvLink = document.getElementById('modalTVLink');
      tvLink.href = `https://www.tradingview.com/chart/?symbol=NSE:${trade.symbol}`;

      const ssContainer = document.getElementById('modalScreenshotContainer');
      const ssImg = document.getElementById('modalScreenshotImg');
      if (trade.screenshot_link && trade.screenshot_link.match(/\.(jpeg|jpg|gif|png|webp)/i)) {
        ssImg.src = trade.screenshot_link;
        ssContainer.classList.remove('hidden');
      } else {
        ssContainer.classList.add('hidden');
      }

      document.getElementById('modalLessonInput').value = trade.lesson || '';
      document.getElementById('tradeModal').classList.remove('hidden');
    }

    function closeTradeModal() {
      document.getElementById('tradeModal').classList.add('hidden');
      activeModalTradeId = null;
    }

    function saveModalJournal() {
      if (!activeModalTradeId) return;
      const trade = tradesData.find(t => t.id === activeModalTradeId);
      if (trade) {
        trade.lesson = document.getElementById('modalLessonInput').value.trim();
        saveTradesLocally();
        renderTradesTable();
        syncTradesWithBackend();
      }
      closeTradeModal();
    }

    function deleteTradeFromModal() {
      if (!activeModalTradeId) return;
      deleteTrade(activeModalTradeId);
      closeTradeModal();
    }

    function deleteTrade(tradeId) {
      if (confirm(`Are you sure you want to delete trade ${tradeId}?`)) {
        tradesData = tradesData.filter(t => t.id !== tradeId);
        saveTradesLocally();
        syncTradesWithBackend();
        renderTradesTable();
        renderTopCapitalHeader();
        checkDailyCircuitBreaker();
        renderAllChartsAndMetrics();
      }
    }

    async function syncTradesWithBackend() {
      try {
        await fetch('/api/trades/bulk', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(tradesData)
        });
      } catch (e) {
        console.warn("Backend bulk sync skipped/offline", e);
      }
    }

    // --- CSV Import & Export ---
    function triggerImport() {
      document.getElementById('csvFileInput').click();
    }

    function triggerFyersImport() {
      document.getElementById('fyersFileInput').click();
    }

    function exportTradesCSV() {
      if (tradesData.length === 0) {
        alert("No trades available to export.");
        return;
      }
      const headers = [
        "Trade_ID", "Date", "Time", "Symbol", "Direction",
        "Entry_Price", "Stop_Price", "Target_Price", "Exit_Price", "Qty",
        "Planned_RR", "FYERS_Costs", "Net_PnL", "Realized_R", "Outcome",
        "Checklist_Score", "Rule_Violation", "Lesson"
      ];

      const rows = tradesData.map(t => [
        t.id,
        t.date,
        t.time,
        t.symbol,
        t.direction,
        Number(t.entry_price).toFixed(2),
        Number(t.stop_price).toFixed(2),
        Number(t.target_price || 0).toFixed(2),
        Number(t.exit_price).toFixed(2),
        t.qty,
        Number(t.rr_planned || 2.2).toFixed(2),
        Number(t.costs || 0).toFixed(2),
        Number(t.net_pnl || 0).toFixed(2),
        Number(t.r_multiple || 0).toFixed(2),
        t.outcome,
        t.checklist_score,
        t.rule_violation || 'N',
        `"${(t.lesson || '').replace(/"/g, '""')}"`
      ]);

      const csvString = [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
      const blob = new Blob([csvString], { type: 'text/csv;charset=utf-8;' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      const today = new Date().toISOString().split('T')[0];
      link.download = `trades_export_${today}.csv`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function copyQuickLogTSV() {
      const entry = parseFloat(document.getElementById('entry_price').value) || 0;
      const stop = parseFloat(document.getElementById('stop_price').value) || 0;
      const exit = parseFloat(document.getElementById('exit_price').value) || 0;
      const qty = parseInt(document.getElementById('qty').value) || 0;
      const sym = (document.getElementById('symbol').value || '').toUpperCase();
      const dir = document.getElementById('direction').value;
      const date = document.getElementById('trade_date').value;
      const time = document.getElementById('trade_time').value;

      if (!sym || entry <= 0 || stop <= 0 || qty <= 0) {
        alert("Please enter Symbol, Entry, Stop Loss, and Quantity first.");
        return;
      }

      const risk = Math.abs(entry - stop);
      const tgt = dir === 'Long' ? (entry + 2.2 * risk) : (entry - 2.2 * risk);
      const tsvLine = `T-${String(tradesData.length + 1).padStart(3, '0')}\t${date}\t${time}\t${sym}\t${dir}\t${entry}\t${stop}\t${tgt.toFixed(2)}\t${exit || tgt.toFixed(2)}\t${qty}`;

      navigator.clipboard.writeText(tsvLine).then(() => {
        alert("📋 Copied to clipboard in Excel Quick_Log format!");
      });
    }

    function copyAllExcelTSV() {
      if (tradesData.length === 0) {
        alert("No trades to copy.");
        return;
      }
      const lines = tradesData.map(t => {
        return `${t.id}\t${t.date}\t${t.time}\t${t.symbol}\t${t.direction}\t${t.entry_price}\t${t.stop_price}\t${t.target_price}\t${t.exit_price}\t${t.qty}`;
      });
      navigator.clipboard.writeText(lines.join('\n')).then(() => {
        alert(`📋 Copied all ${tradesData.length} trades in Excel TSV format!`);
      });
    }

    // --- Standard CSV / JSON Import Parser ---
    function handleFileImport(e) {
      const file = e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(evt) {
        try {
          const content = evt.target.result;
          if (file.name.endsWith('.json')) {
            const parsed = JSON.parse(content);
            if (Array.isArray(parsed)) {
              applyImportedTrades(parsed);
              return;
            }
          }
          parseStandardCSV(content);
        } catch(err) {
          alert("Error parsing file: " + err.message);
        } finally {
          e.target.value = '';
        }
      };
      reader.readAsText(file);
    }

    function parseStandardCSV(csvText) {
      const lines = csvText.split(/\r\n|\n/).filter(line => line.trim() !== '');
      if (lines.length < 2) {
        alert("CSV must contain a header row and data rows.");
        return;
      }

      const rawHeaders = lines[0].split(',').map(h => h.trim().toLowerCase().replace(/['"]/g, ''));
      const findCol = (...names) => {
        for (let name of names) {
          const idx = rawHeaders.indexOf(name.toLowerCase());
          if (idx !== -1) return idx;
        }
        return -1;
      };

      const colSymbol = findCol('symbol', 'ticker');
      const colEntry = findCol('entry_price', 'entry', 'buy_price');
      const colStop = findCol('stop_price', 'stop', 'sl');
      const colExit = findCol('exit_price', 'exit', 'sell_price');
      const colQty = findCol('qty', 'quantity', 'size');
      const colDate = findCol('date');
      const colTime = findCol('time');
      const colDir = findCol('direction', 'side');
      const colLesson = findCol('lesson', 'notes');

      if (colSymbol === -1 || colEntry === -1 || colStop === -1) {
        alert("CSV missing required columns: Symbol, Entry_Price, Stop_Price.");
        return;
      }

      const parsedTrades = [];
      const today = new Date().toISOString().split('T')[0];

      for (let i = 1; i < lines.length; i++) {
        const line = lines[i];
        const cells = line.split(',').map(c => c.trim().replace(/^"|"$/g, ''));
        if (cells.length <= colSymbol) continue;

        const symbol = (cells[colSymbol] || '').toUpperCase();
        const entry = parseFloat(cells[colEntry]);
        const stop = parseFloat(cells[colStop]);
        if (!symbol || isNaN(entry) || isNaN(stop)) continue;

        const qty = colQty !== -1 && !isNaN(parseInt(cells[colQty])) ? parseInt(cells[colQty]) : 100;
        const risk = Math.abs(entry - stop);
        const dir = colDir !== -1 && cells[colDir] ? cells[colDir] : (entry > stop ? 'Long' : 'Short');
        const defaultExit = dir === 'Long' ? (entry + 2.2 * risk) : (entry - 2.2 * risk);
        const exit = colExit !== -1 && !isNaN(parseFloat(cells[colExit])) ? parseFloat(cells[colExit]) : defaultExit;

        const buyTurnover = dir === 'Long' ? (entry * qty) : (exit * qty);
        const sellTurnover = dir === 'Long' ? (exit * qty) : (entry * qty);
        const fyers = computeFyersCharges(buyTurnover, sellTurnover);

        const grossPnL = dir === 'Long' ? (exit - entry) * qty : (entry - exit) * qty;
        const netPnL = grossPnL - fyers.totalCosts;
        const totalRisk = risk * qty;
        const realizedR = totalRisk > 0 ? (netPnL / totalRisk) : 0;

        let outcome = 'Break-Even';
        if (netPnL > 10) outcome = 'Win';
        else if (netPnL < -10) outcome = 'Loss';

        parsedTrades.push({
          id: `T-${String(tradesData.length + parsedTrades.length + 1).padStart(3, '0')}`,
          date: (colDate !== -1 && cells[colDate]) ? cells[colDate] : today,
          day: 'Mon',
          time: (colTime !== -1 && cells[colTime]) ? cells[colTime] : '09:30',
          exit_time: '09:38',
          hold_duration: 8,
          symbol: symbol,
          direction: dir,
          setup_name: '1m Pullback to 9EMA',
          scanner_alert_time: '09:28',
          htf_ok: 'Y',
          no_chase: 'Y',
          stop_defined: 'Y',
          target_price: parseFloat(defaultExit.toFixed(2)),
          rr_planned: 2.2,
          risk_percent: 0.0025,
          risk_amount: totalRisk,
          entry_price: entry,
          stop_price: stop,
          exit_price: exit,
          qty: qty,
          gross_pnl: parseFloat(grossPnL.toFixed(2)),
          costs: parseFloat(fyers.totalCosts.toFixed(2)),
          net_pnl: parseFloat(netPnL.toFixed(2)),
          r_multiple: parseFloat(realizedR.toFixed(2)),
          outcome: outcome,
          checklist_score: 5,
          rule_violation: 'N',
          violation_type: 'None',
          emotion_before: 2,
          emotion_during: 2,
          emotion_after: 2,
          trade_valid: 'Y',
          lesson: colLesson !== -1 && cells[colLesson] ? cells[colLesson] : 'Imported via CSV',
          screenshot_link: `https://www.tradingview.com/chart/?symbol=NSE:${symbol}`
        });
      }

      applyImportedTrades(parsedTrades);
    }

    // --- FYERS Tradebook Raw CSV Parser (FIFO Matching) ---
    function handleFyersFileImport(e) {
      const file = e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(evt) {
        try {
          parseRawFyersTradebook(evt.target.result);
        } catch(err) {
          alert("Error parsing FYERS file: " + err.message);
        } finally {
          e.target.value = '';
        }
      };
      reader.readAsText(file);
    }

    function parseRawFyersTradebook(csvContent) {
      const lines = csvContent.split(/\r\n|\n/).filter(l => l.trim() !== '');
      if (lines.length < 2) {
        alert("Invalid FYERS CSV: File is empty or lacks headers.");
        return;
      }

      const headers = lines[0].split(',').map(h => h.trim().toLowerCase().replace(/['"]/g, ''));
      const findCol = (...names) => {
        for (let name of names) {
          const idx = headers.findIndex(h => h.includes(name.toLowerCase()));
          if (idx !== -1) return idx;
        }
        return -1;
      };

      const colSym = findCol('symbol', 'scrip');
      const colSide = findCol('side', 'type', 'action', 'buy/sell', 'trade type');
      const colPrice = findCol('price', 'trade price', 'avg price');
      const colQty = findCol('qty', 'quantity', 'trade qty', 'shares');
      const colTime = findCol('time', 'trade time', 'date');

      if (colSym === -1 || colPrice === -1 || colQty === -1) {
        alert("Could not identify FYERS columns (Symbol, Price, Qty).");
        return;
      }

      const executionsBySymbol = {};
      for (let i = 1; i < lines.length; i++) {
        const cells = lines[i].split(',').map(c => c.trim().replace(/^"|"$/g, ''));
        if (cells.length <= colSym) continue;

        let symbol = cells[colSym].replace('NSE:', '').replace('-EQ', '').trim().toUpperCase();
        let side = (colSide !== -1 ? cells[colSide] : 'BUY').toUpperCase();
        let price = parseFloat(cells[colPrice]);
        let qty = parseInt(cells[colQty]);
        let timeStr = (colTime !== -1 ? cells[colTime] : '09:30');

        if (!symbol || isNaN(price) || isNaN(qty) || qty <= 0) continue;

        if (!executionsBySymbol[symbol]) executionsBySymbol[symbol] = [];
        executionsBySymbol[symbol].push({
          symbol,
          side: side.includes('BUY') || side === 'B' ? 'BUY' : 'SELL',
          price,
          qty,
          time: timeStr
        });
      }

      pendingFyersTrades = [];
      const today = new Date().toISOString().split('T')[0];

      for (const [symbol, execs] of Object.entries(executionsBySymbol)) {
        let buyQueue = [];
        let sellQueue = [];

        for (const ex of execs) {
          if (ex.side === 'BUY') buyQueue.push({...ex});
          else sellQueue.push({...ex});
        }

        while (buyQueue.length > 0 && sellQueue.length > 0) {
          const buyEx = buyQueue[0];
          const sellEx = sellQueue[0];
          const matchedQty = Math.min(buyEx.qty, sellEx.qty);

          const isLong = true;
          const entryPrice = isLong ? buyEx.price : sellEx.price;
          const exitPrice = isLong ? sellEx.price : buyEx.price;

          const buyTurnover = entryPrice * matchedQty;
          const sellTurnover = exitPrice * matchedQty;
          const fyers = computeFyersCharges(buyTurnover, sellTurnover);

          const grossPnL = (exitPrice - entryPrice) * matchedQty;
          const netPnL = grossPnL - fyers.totalCosts;

          const riskPerShare = Math.max(entryPrice * 0.003, 1.0);
          const stopPrice = isLong ? entryPrice - riskPerShare : entryPrice + riskPerShare;
          const totalRisk = riskPerShare * matchedQty;
          const realizedR = totalRisk > 0 ? (netPnL / totalRisk) : 0;

          let outcome = 'Break-Even';
          if (netPnL > 10) outcome = 'Win';
          else if (netPnL < -10) outcome = 'Loss';

          pendingFyersTrades.push({
            id: `FYERS-${String(tradesData.length + pendingFyersTrades.length + 1).padStart(3, '0')}`,
            date: today,
            day: 'Intraday',
            time: buyEx.time.length <= 8 ? buyEx.time : '09:30',
            exit_time: sellEx.time.length <= 8 ? sellEx.time : '09:38',
            hold_duration: 8,
            symbol: symbol,
            direction: isLong ? 'Long' : 'Short',
            setup_name: 'FYERS Intraday Execution',
            scanner_alert_time: buyEx.time,
            htf_ok: 'Y',
            no_chase: 'Y',
            stop_defined: 'Y',
            target_price: parseFloat((entryPrice + 2.2 * riskPerShare).toFixed(2)),
            rr_planned: 2.2,
            risk_percent: 0.0025,
            risk_amount: totalRisk,
            entry_price: entryPrice,
            stop_price: parseFloat(stopPrice.toFixed(2)),
            exit_price: exitPrice,
            qty: matchedQty,
            gross_pnl: parseFloat(grossPnL.toFixed(2)),
            costs: parseFloat(fyers.totalCosts.toFixed(2)),
            net_pnl: parseFloat(netPnL.toFixed(2)),
            r_multiple: parseFloat(realizedR.toFixed(2)),
            outcome: outcome,
            checklist_score: 5,
            rule_violation: 'N',
            violation_type: 'None',
            emotion_before: 2,
            emotion_during: 2,
            emotion_after: 2,
            trade_valid: 'Y',
            lesson: 'Direct import from FYERS Tradebook CSV',
            screenshot_link: `https://www.tradingview.com/chart/?symbol=NSE:${symbol}`
          });

          buyEx.qty -= matchedQty;
          sellEx.qty -= matchedQty;
          if (buyEx.qty <= 0) buyQueue.shift();
          if (sellEx.qty <= 0) sellQueue.shift();
        }
      }

      if (pendingFyersTrades.length === 0) {
        alert("No matched round-trip BUY/SELL execution pairs could be formed from this tradebook file.");
        return;
      }

      renderFyersPreviewModal();
    }

    function renderFyersPreviewModal() {
      const tbody = document.getElementById('fyersPreviewTableBody');
      tbody.innerHTML = pendingFyersTrades.map(t => `
        <tr class="border-b border-slate-800">
          <td class="py-2 px-3 font-bold text-white">${t.symbol}</td>
          <td class="py-2 px-2 text-emerald-400 font-bold">${t.direction}</td>
          <td class="py-2 px-2 text-right">₹${t.entry_price.toFixed(2)}</td>
          <td class="py-2 px-2 text-right">₹${t.exit_price.toFixed(2)}</td>
          <td class="py-2 px-2 text-right text-slate-300">${t.qty}</td>
          <td class="py-2 px-2 text-right font-bold ${t.net_pnl >= 0 ? 'text-emerald-400' : 'text-rose-400'}">₹${t.net_pnl.toFixed(2)}</td>
          <td class="py-2 px-3 text-center">
            <span class="px-2 py-0.5 rounded-full text-[10px] font-sans font-bold ${t.outcome === 'Win' ? 'bg-emerald-500/10 text-emerald-400' : 'bg-rose-500/10 text-rose-400'}">${t.outcome}</span>
          </td>
        </tr>
      `).join('');

      document.getElementById('fyersModal').classList.remove('hidden');
    }

    function closeFyersModal() {
      document.getElementById('fyersModal').classList.add('hidden');
      pendingFyersTrades = [];
    }

    function commitFyersParsedTrades() {
      if (pendingFyersTrades.length > 0) {
        applyImportedTrades(pendingFyersTrades);
        closeFyersModal();
      }
    }

    function applyImportedTrades(trades) {
      if (!Array.isArray(trades) || trades.length === 0) return;
      tradesData = [...tradesData, ...trades];
      saveTradesLocally();
      syncTradesWithBackend();
      renderTradesTable();
      renderTopCapitalHeader();
      checkDailyCircuitBreaker();
      renderAllChartsAndMetrics();
      alert(`🎉 Successfully imported ${trades.length} trades!`);
    }

    // --- ADVANCED INSTITUTIONAL ANALYTICS & METRICS ---
    function renderAllChartsAndMetrics() {
      const trades = getFilteredTrades();

      let totalGross = 0;
      let totalCosts = 0;
      let totalNet = 0;
      let totalWins = 0;
      let totalLosses = 0;
      let grossProfit = 0;
      let grossLoss = 0;
      let totalRealizedR = 0;
      let totalPlannedRR = 0;
      let violations = 0;
      let totalTurnover = 0;

      let longWins = 0, longLosses = 0, longNet = 0;
      let shortWins = 0, shortLosses = 0, shortNet = 0;

      let winHoldTotal = 0, winHoldCount = 0;
      let lossHoldTotal = 0, lossHoldCount = 0;

      const tiltBuckets = {
        1: { count: 0, wins: 0, pnl: 0, totalR: 0 },
        2: { count: 0, wins: 0, pnl: 0, totalR: 0 },
        3: { count: 0, wins: 0, pnl: 0, totalR: 0 }
      };

      const weekdayMatrix = {
        'Mon': { count: 0, wins: 0, grossWin: 0, grossLoss: 0, netPnL: 0 },
        'Tue': { count: 0, wins: 0, grossWin: 0, grossLoss: 0, netPnL: 0 },
        'Wed': { count: 0, wins: 0, grossWin: 0, grossLoss: 0, netPnL: 0 },
        'Thu': { count: 0, wins: 0, grossWin: 0, grossLoss: 0, netPnL: 0 },
        'Fri': { count: 0, wins: 0, grossWin: 0, grossLoss: 0, netPnL: 0 }
      };

      const returnsList = [];

      trades.forEach(t => {
        const net = parseFloat(t.net_pnl) || 0;
        const gross = parseFloat(t.gross_pnl) || (net + (parseFloat(t.costs) || 0));
        const costs = parseFloat(t.costs) || 0;
        const r = parseFloat(t.r_multiple) || 0;
        const plannedR = parseFloat(t.rr_planned || 2.2);
        const hold = t.hold_duration || (net > 0 ? 8 : 3);
        const urgency = parseInt(t.emotion_before) || 2;
        const dayStr = t.day || 'Mon';

        totalGross += gross;
        totalCosts += costs;
        totalNet += net;
        totalRealizedR += r;
        totalPlannedRR += plannedR;
        returnsList.push(r);

        const buyTurnover = t.direction === 'Long' ? (t.entry_price * t.qty) : (t.exit_price * t.qty);
        const sellTurnover = t.direction === 'Long' ? (t.exit_price * t.qty) : (t.entry_price * t.qty);
        totalTurnover += (buyTurnover + sellTurnover);

        if (net > 0) {
          totalWins++;
          grossProfit += net;
          winHoldTotal += hold;
          winHoldCount++;
        } else if (net < 0) {
          totalLosses++;
          grossLoss += Math.abs(net);
          lossHoldTotal += hold;
          lossHoldCount++;
        }

        if (t.direction === 'Long') {
          longNet += net;
          if (net > 0) longWins++; else if (net < 0) longLosses++;
        } else {
          shortNet += net;
          if (net > 0) shortWins++; else if (net < 0) shortLosses++;
        }

        let bIdx = 1;
        if (urgency >= 7) bIdx = 3;
        else if (urgency >= 4) bIdx = 2;
        tiltBuckets[bIdx].count++;
        tiltBuckets[bIdx].pnl += net;
        tiltBuckets[bIdx].totalR += r;
        if (net > 0) tiltBuckets[bIdx].wins++;

        const cleanDay = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'].includes(dayStr) ? dayStr : 'Tue';
        weekdayMatrix[cleanDay].count++;
        weekdayMatrix[cleanDay].netPnL += net;
        if (net > 0) {
          weekdayMatrix[cleanDay].wins++;
          weekdayMatrix[cleanDay].grossWin += net;
        } else if (net < 0) {
          weekdayMatrix[cleanDay].grossLoss += Math.abs(net);
        }

        if (t.rule_violation === 'Y' || (t.checklist_score && t.checklist_score < 5)) {
          violations++;
        }
      });

      const totalClosed = totalWins + totalLosses;
      const winRate = totalClosed > 0 ? (totalWins / totalClosed) * 100 : 0;
      const profitFactor = grossLoss > 0 ? (grossProfit / grossLoss) : (grossProfit > 0 ? 99.0 : 0.0);
      const expectancyR = trades.length > 0 ? (totalRealizedR / trades.length) : 0;
      const disciplineScore = trades.length > 0 ? Math.round(((trades.length - violations) / trades.length) * 100) : 100;
      const efficiencyScore = totalPlannedRR > 0 ? Math.max(0, Math.min(100, Math.round((Math.max(0, totalRealizedR) / totalPlannedRR) * 100))) : 0;

      // Kelly Criterion
      const avgWinR = winHoldCount > 0 ? (grossProfit / (totalWins * (startingCapital * riskModePercent))) : 2.0;
      const avgLossR = lossHoldCount > 0 ? (grossLoss / (totalLosses * (startingCapital * riskModePercent))) : 1.0;
      const payoffB = avgLossR > 0 ? (avgWinR / avgLossR) : 2.0;
      const pWin = totalClosed > 0 ? (totalWins / totalClosed) : 0.55;
      const pLoss = 1.0 - pWin;

      let kellyF = pWin - (pLoss / Math.max(0.1, payoffB));
      let safeKelly = Math.max(0, Math.min(0.05, kellyF / 4.0));
      
      const kellyElem = document.getElementById('statKellyFraction');
      const kellyStatus = document.getElementById('kellyStatusBadge');
      if (kellyElem && kellyStatus) {
        if (kellyF > 0) {
          kellyElem.textContent = `${(kellyF * 100).toFixed(1)}% Full Kelly`;
          kellyStatus.textContent = 'Positive Edge';
          kellyStatus.className = 'text-[9px] px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold';
        } else {
          kellyElem.textContent = `0.0% (Sub-optimal)`;
          kellyStatus.textContent = 'Zero Edge';
          kellyStatus.className = 'text-[9px] px-1.5 py-0.5 rounded bg-rose-500/20 text-rose-300 font-bold';
        }
        document.getElementById('statKellyRecSub').textContent = `Quarter-Kelly: ${(safeKelly * 100).toFixed(2)}% (Target: 0.25%–0.50%)`;
      }

      // Risk of Ruin
      let edgeZ = (pWin * payoffB - pLoss) / (payoffB + 1.0);
      let ror10 = 0.0;
      let ror20 = 0.0;
      if (edgeZ > 0.05) {
        const base = (1.0 - edgeZ) / (1.0 + edgeZ);
        const units10 = 0.10 / riskModePercent;
        const units20 = 0.20 / riskModePercent;
        ror10 = Math.min(100.0, Math.pow(base, units10) * 100.0);
        ror20 = Math.min(100.0, Math.pow(base, units20) * 100.0);
      } else {
        ror10 = 99.0;
        ror20 = 85.0;
      }
      const rorElem = document.getElementById('statRiskOfRuin');
      if (rorElem) {
        rorElem.textContent = `${ror10.toFixed(2)}%`;
        document.getElementById('statRoRSub').textContent = `20% DD Risk: ${ror20 < 0.01 ? '< 0.01%' : ror20.toFixed(2) + '%'}`;
      }

      // Sharpe & Sortino
      let meanR = returnsList.length > 0 ? (returnsList.reduce((a,b)=>a+b, 0) / returnsList.length) : 0;
      let varianceR = returnsList.length > 1 
        ? returnsList.reduce((acc, r) => acc + Math.pow(r - meanR, 2), 0) / (returnsList.length - 1)
        : 1.0;
      let stdR = Math.sqrt(varianceR);
      let downsideReturns = returnsList.filter(r => r < 0);
      let downsideVariance = downsideReturns.length > 0
        ? downsideReturns.reduce((acc, r) => acc + Math.pow(r, 2), 0) / downsideReturns.length
        : 0.1;
      let downsideStd = Math.sqrt(downsideVariance);

      let sharpeAnnual = stdR > 0 ? (meanR / stdR) * Math.sqrt(500) : 0;
      let sortinoRatio = downsideStd > 0 ? (meanR / downsideStd) * Math.sqrt(500) : 9.99;

      const sortinoElem = document.getElementById('statSortinoRatio');
      if (sortinoElem) {
        sortinoElem.textContent = sortinoRatio >= 0 ? sortinoRatio.toFixed(2) : '0.00';
        document.getElementById('statSharpeSub').textContent = `Sharpe: ${sharpeAnnual.toFixed(2)} (Annualized)`;
      }

      // FYERS Cost Drag % & Turnover Churn
      let costDrag = grossProfit > 0 ? (totalCosts / grossProfit) * 100 : 0;
      let turnoverPerNet = totalNet > 0 ? Math.round(totalTurnover / totalNet) : 0;

      const costDragElem = document.getElementById('statCostDragPct');
      if (costDragElem) {
        costDragElem.textContent = `${costDrag.toFixed(1)}%`;
        const dragGradeElem = document.getElementById('costDragGrade');
        if (dragGradeElem) {
          if (costDrag < 15) {
            dragGradeElem.textContent = 'Optimal Friction';
            dragGradeElem.className = 'text-[9px] px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold';
          } else if (costDrag < 30) {
            dragGradeElem.textContent = 'Moderate Drag';
            dragGradeElem.className = 'text-[9px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-bold';
          } else {
            dragGradeElem.textContent = 'High Drag / Churn';
            dragGradeElem.className = 'text-[9px] px-1.5 py-0.5 rounded bg-rose-500/20 text-rose-300 font-bold';
          }
        }
        document.getElementById('statTurnoverChurnSub').textContent = `Turnover: ₹${Math.round(totalTurnover).toLocaleString('en-IN')} (₹${turnoverPerNet} to ₹1)`;
      }

      // Trade Duration Asymmetry
      let avgWinHold = winHoldCount > 0 ? (winHoldTotal / winHoldCount) : 8.0;
      let avgLossHold = lossHoldCount > 0 ? (lossHoldTotal / lossHoldCount) : 3.0;
      let asymmetryRatio = avgLossHold > 0 ? (avgWinHold / avgLossHold) : 2.5;

      const winHoldElem = document.getElementById('statAvgWinHold');
      if (winHoldElem) {
        winHoldElem.textContent = `${avgWinHold.toFixed(1)}m`;
        document.getElementById('statAvgLossHold').textContent = `${avgLossHold.toFixed(1)}m`;
        document.getElementById('statHoldAsymmetryRatio').textContent = `${asymmetryRatio.toFixed(2)}x (Target &ge; 1.5x)`;

        const durBadge = document.getElementById('durationQualityBadge');
        if (durBadge) {
          if (asymmetryRatio >= 1.5) {
            durBadge.textContent = 'Patient Exits';
            durBadge.className = 'text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20';
          } else {
            durBadge.textContent = 'Early Fear Exit Risk';
            durBadge.className = 'text-[10px] font-bold px-2 py-0.5 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20';
          }
        }
      }

      // Streak Tracker
      let curStreak = 0;
      let maxWinStreak = 0;
      let maxLossStreak = 0;
      let tempWin = 0;
      let tempLoss = 0;
      let postLossRecoveryWins = 0;
      let postLossRecoveryTotal = 0;

      for (let i = 0; i < trades.length; i++) {
        const net = parseFloat(trades[i].net_pnl) || 0;
        if (net > 0) {
          tempWin++;
          tempLoss = 0;
          if (tempWin > maxWinStreak) maxWinStreak = tempWin;
        } else if (net < 0) {
          tempLoss++;
          tempWin = 0;
          if (tempLoss > maxLossStreak) maxLossStreak = tempLoss;
        }

        if (i > 0 && (parseFloat(trades[i-1].net_pnl) || 0) < 0) {
          postLossRecoveryTotal++;
          if (net > 0) postLossRecoveryWins++;
        }
      }

      if (trades.length > 0) {
        const lastNet = parseFloat(trades[trades.length - 1].net_pnl) || 0;
        let count = 0;
        const isWinLast = lastNet > 0;
        for (let i = trades.length - 1; i >= 0; i--) {
          const n = parseFloat(trades[i].net_pnl) || 0;
          if ((n > 0 && isWinLast) || (n < 0 && !isWinLast)) count++;
          else break;
        }
        curStreak = isWinLast ? count : -count;
      }

      const maxWinElem = document.getElementById('statMaxWinStreak');
      if (maxWinElem) {
        maxWinElem.textContent = `${maxWinStreak} trades`;
        document.getElementById('statMaxLossStreak').textContent = `${maxLossStreak} trades`;
        const curStreakElem = document.getElementById('currentStreakBadge');
        if (curStreakElem) {
          if (curStreak >= 0) {
            curStreakElem.textContent = `Streak: +${curStreak} Wins`;
            curStreakElem.className = 'text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20';
          } else {
            curStreakElem.textContent = `Streak: ${curStreak} Loss`;
            curStreakElem.className = 'text-[10px] font-bold px-2 py-0.5 rounded bg-rose-500/10 text-rose-400 border border-rose-500/20';
          }
        }
        const postLossWR = postLossRecoveryTotal > 0 ? Math.round((postLossRecoveryWins / postLossRecoveryTotal) * 100) : 100;
        document.getElementById('statPostCooldownWR').textContent = `${postLossWR}% (${postLossRecoveryWins}/${postLossRecoveryTotal})`;
      }

      // Tilt Correlation
      for (let b = 1; b <= 3; b++) {
        const tCount = tiltBuckets[b].count;
        const tWins = tiltBuckets[b].wins;
        const tPnL = tiltBuckets[b].pnl;
        const tWR = tCount > 0 ? Math.round((tWins / tCount) * 100) : 0;

        const countElem = document.getElementById(`tiltTrades_${b}`);
        if (countElem) {
          countElem.textContent = tCount;
          document.getElementById(`tiltWR_${b}`).textContent = `${tWR}%`;
          const pnlElem = document.getElementById(`tiltPnL_${b}`);
          pnlElem.textContent = `₹${Math.round(tPnL).toLocaleString('en-IN')}`;
          pnlElem.className = tPnL >= 0 ? 'py-2 px-2.5 text-right font-bold text-emerald-400' : 'py-2 px-2.5 text-right font-bold text-rose-400';
        }
      }

      // Weekday Matrix
      const weekdayTbody = document.getElementById('weekdayMatrixBody');
      if (weekdayTbody) {
        let bestDay = 'Tue';
        let worstDay = 'None';
        let maxDayPnL = -999999;
        let minDayPnL = 999999;

        weekdayTbody.innerHTML = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'].map(day => {
          const item = weekdayMatrix[day];
          const wr = item.count > 0 ? Math.round((item.wins / item.count) * 100) : 0;
          const pf = item.grossLoss > 0 ? (item.grossWin / item.grossLoss).toFixed(2) : (item.grossWin > 0 ? '99.0' : '0.00');
          const pnl = Math.round(item.netPnL);

          if (pnl > maxDayPnL && item.count > 0) { maxDayPnL = pnl; bestDay = day; }
          if (pnl < minDayPnL && item.count > 0 && pnl < 0) { minDayPnL = pnl; worstDay = day; }

          return `
            <tr class="border-b border-slate-800/40">
              <td class="py-2.5 px-3 font-semibold text-white font-sans">${day}</td>
              <td class="py-2.5 px-1 text-center text-slate-300">${item.count}</td>
              <td class="py-2.5 px-1 text-center font-bold ${wr >= 50 ? 'text-emerald-400' : 'text-amber-400'}">${wr}%</td>
              <td class="py-2.5 px-1 text-center text-blue-400 font-bold">${pf}</td>
              <td class="py-2.5 px-2.5 text-right font-bold ${pnl >= 0 ? 'text-emerald-400' : 'text-rose-400'}">₹${pnl.toLocaleString('en-IN')}</td>
            </tr>
          `;
        }).join('');

        const bestDayElem = document.getElementById('bestWeekdayText');
        if (bestDayElem) bestDayElem.textContent = bestDay;
        const worstDayElem = document.getElementById('worstWeekdayText');
        if (worstDayElem) worstDayElem.textContent = worstDay;
      }

      // Update Standard Metrics in DOM
      const netPnLElem = document.getElementById('statNetPnL');
      if (netPnLElem) {
        netPnLElem.textContent = `₹${totalNet.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
        netPnLElem.className = totalNet >= 0 ? 'text-xl font-black font-mono mt-1 text-emerald-400' : 'text-xl font-black font-mono mt-1 text-rose-400';
        document.getElementById('statGrossCostSub').textContent = `Gross: ₹${Math.round(totalGross).toLocaleString('en-IN')} • Costs: ₹${Math.round(totalCosts).toLocaleString('en-IN')}`;

        document.getElementById('statWinRate').textContent = `${winRate.toFixed(1)}%`;
        document.getElementById('statWinLossRatio').textContent = `${totalWins} Wins • ${totalLosses} Losses`;

        document.getElementById('statProfitFactor').textContent = profitFactor.toFixed(2);
        document.getElementById('statTotalRSub').textContent = `Total Net R: ${totalRealizedR >= 0 ? '+' : ''}${totalRealizedR.toFixed(2)}R`;

        const expElem = document.getElementById('statExpectancyR');
        expElem.textContent = `${expectancyR >= 0 ? '+' : ''}${expectancyR.toFixed(2)} R`;
        expElem.className = expectancyR >= 0 ? 'text-xl font-black font-mono mt-1 text-indigo-400' : 'text-xl font-black font-mono mt-1 text-rose-400';

        document.getElementById('statEfficiencyScore').textContent = `${efficiencyScore}%`;
        document.getElementById('statEfficiencyDesc').textContent = efficiencyScore >= 75 ? 'Optimal Hold Target' : 'Check for Early Exits';

        document.getElementById('statDisciplineScore').textContent = `${disciplineScore}%`;
        document.getElementById('statViolationsCount').textContent = `${violations} Violations`;

        const longTotal = longWins + longLosses;
        const shortTotal = shortWins + shortLosses;
        const longWR = longTotal > 0 ? Math.round((longWins / longTotal) * 100) : 0;
        const shortWR = shortTotal > 0 ? Math.round((shortWins / shortTotal) * 100) : 0;
        document.getElementById('longStatsText').textContent = `${longWR}% WR (₹${Math.round(longNet).toLocaleString('en-IN')})`;
        document.getElementById('shortStatsText').textContent = `${shortWR}% WR (₹${Math.round(shortNet).toLocaleString('en-IN')})`;
        
        const dirBadge = document.getElementById('directionalBiasBadge');
        if (dirBadge) {
          if (longNet > shortNet + 500) {
            dirBadge.textContent = 'Long Biased';
            dirBadge.className = 'text-emerald-400 font-bold';
          } else if (shortNet > longNet + 500) {
            dirBadge.textContent = 'Short Biased';
            dirBadge.className = 'text-rose-400 font-bold';
          } else {
            dirBadge.textContent = 'Balanced';
            dirBadge.className = 'text-blue-400 font-bold';
          }
        }

        const totalReturnPct = startingCapital > 0 ? (totalNet / startingCapital) * 100 : 0;
        const roiElem = document.getElementById('chartTotalReturnBadge');
        if (roiElem) {
          roiElem.textContent = `${totalReturnPct >= 0 ? '+' : ''}${totalReturnPct.toFixed(2)}% ROI`;
          roiElem.className = totalReturnPct >= 0 
            ? 'text-xs font-mono font-bold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-lg border border-emerald-500/20' 
            : 'text-xs font-mono font-bold text-rose-400 bg-rose-500/10 px-2.5 py-1 rounded-lg border border-rose-500/20';
        }
      }

      // Charts render
      if (currentTab === 2) {
        renderEquityChart(trades);
        renderDonutCharts(totalWins, totalLosses, trades.length - totalClosed, violations, trades.length);
      } else if (currentTab === 3) {
        renderTimeOfDayHeatmap(trades);
        renderSetupMatrix(trades);
      } else if (currentTab === 4) {
        runMonteCarloSimulation();
      }
    }

    function renderEquityChart(trades) {
      const ctx = document.getElementById('equityChart');
      if (!ctx) return;

      const labels = ['Start', ...trades.map((t, idx) => `T-${idx + 1}`)];
      let runningCapital = startingCapital;
      const dataPoints = [startingCapital];

      trades.forEach(t => {
        runningCapital += (parseFloat(t.net_pnl) || 0);
        dataPoints.push(runningCapital);
      });

      if (chartEquity) chartEquity.destroy();

      chartEquity = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: 'Net Account Capital (₹)',
            data: dataPoints,
            borderColor: '#10B981',
            backgroundColor: 'rgba(16, 185, 129, 0.08)',
            fill: true,
            tension: 0.25,
            pointBackgroundColor: '#10B981',
            pointRadius: 4,
            borderWidth: 2
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              callbacks: {
                label: (ctx) => `Capital: ₹${Math.round(ctx.parsed.y).toLocaleString('en-IN')}`
              }
            }
          },
          scales: {
            x: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#64748B', font: { size: 10 } } },
            y: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#64748B', font: { size: 10 }, callback: v => '₹' + v.toLocaleString('en-IN') } }
          }
        }
      });
    }

    function renderDonutCharts(wins, losses, be, violations, total) {
      const ctxOutcome = document.getElementById('outcomeDonutChart');
      const ctxDisc = document.getElementById('disciplineDonutChart');
      if (!ctxOutcome || !ctxDisc) return;

      if (chartOutcomeDonut) chartOutcomeDonut.destroy();
      chartOutcomeDonut = new Chart(ctxOutcome, {
        type: 'doughnut',
        data: {
          labels: ['Wins', 'Losses', 'BE'],
          datasets: [{
            data: [wins, losses, be],
            backgroundColor: ['#10B981', '#F43F5E', '#64748B'],
            borderWidth: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          cutout: '70%',
          plugins: { legend: { display: false } }
        }
      });

      const cleanTrades = Math.max(0, total - violations);
      if (chartDisciplineDonut) chartDisciplineDonut.destroy();
      chartDisciplineDonut = new Chart(ctxDisc, {
        type: 'doughnut',
        data: {
          labels: ['Followed Rules', 'Violations'],
          datasets: [{
            data: [cleanTrades, violations],
            backgroundColor: ['#3B82F6', '#EF4444'],
            borderWidth: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          cutout: '70%',
          plugins: { legend: { display: false } }
        }
      });
    }

    function renderTimeOfDayHeatmap(trades) {
      const buckets = {
        '09:15-09:30': { pnl: 0, count: 0, wins: 0 },
        '09:30-10:00': { pnl: 0, count: 0, wins: 0 },
        '10:00-10:30': { pnl: 0, count: 0, wins: 0 },
        'Post 10:30':   { pnl: 0, count: 0, wins: 0 }
      };

      trades.forEach(t => {
        const time = t.time || '09:30';
        const net = parseFloat(t.net_pnl) || 0;
        let bKey = 'Post 10:30';
        if (time >= '09:15' && time < '09:30') bKey = '09:15-09:30';
        else if (time >= '09:30' && time < '10:00') bKey = '09:30-10:00';
        else if (time >= '10:00' && time <= '10:30') bKey = '10:00-10:30';

        buckets[bKey].pnl += net;
        buckets[bKey].count += 1;
        if (net > 0) buckets[bKey].wins += 1;
      });

      document.getElementById('todPnL_1').textContent = `₹${Math.round(buckets['09:15-09:30'].pnl).toLocaleString('en-IN')}`;
      document.getElementById('todCount_1').textContent = `${buckets['09:15-09:30'].count} trds`;
      document.getElementById('todPnL_2').textContent = `₹${Math.round(buckets['09:30-10:00'].pnl).toLocaleString('en-IN')}`;
      document.getElementById('todCount_2').textContent = `${buckets['09:30-10:00'].count} trds`;
      document.getElementById('todPnL_3').textContent = `₹${Math.round(buckets['10:00-10:30'].pnl).toLocaleString('en-IN')}`;
      document.getElementById('todCount_3').textContent = `${buckets['10:00-10:30'].count} trds`;
      document.getElementById('todPnL_4').textContent = `₹${Math.round(buckets['Post 10:30'].pnl).toLocaleString('en-IN')}`;
      document.getElementById('todCount_4').textContent = `${buckets['Post 10:30'].count} trds`;

      const ctx = document.getElementById('timeOfDayChart');
      if (!ctx) return;
      if (chartTimeOfDay) chartTimeOfDay.destroy();

      const labels = Object.keys(buckets);
      const dataPnL = labels.map(k => buckets[k].pnl);
      const bgColors = dataPnL.map(v => v >= 0 ? '#10B981' : '#F43F5E');

      chartTimeOfDay = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Net P&L (₹)',
            data: dataPnL,
            backgroundColor: bgColors,
            borderRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            x: { grid: { display: false }, ticks: { color: '#94A3B8', font: { size: 10 } } },
            y: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#94A3B8', font: { size: 10 } } }
          }
        }
      });
    }

    function renderSetupMatrix(trades) {
      const setups = {};
      trades.forEach(t => {
        const s = t.setup_name || '1m Pullback to 9EMA';
        if (!setups[s]) setups[s] = { count: 0, wins: 0, grossWin: 0, grossLoss: 0, totalR: 0, netPnL: 0 };
        const net = parseFloat(t.net_pnl) || 0;
        const r = parseFloat(t.r_multiple) || 0;
        setups[s].count += 1;
        setups[s].netPnL += net;
        setups[s].totalR += r;
        if (net > 0) {
          setups[s].wins += 1;
          setups[s].grossWin += net;
        } else if (net < 0) {
          setups[s].grossLoss += Math.abs(net);
        }
      });

      const tbody = document.getElementById('setupMatrixBody');
      if (!tbody) return;
      if (Object.keys(setups).length === 0) {
        tbody.innerHTML = `<tr><td colspan="5" class="text-center py-4 text-slate-500">No setup data logged.</td></tr>`;
        return;
      }

      tbody.innerHTML = Object.entries(setups).map(([name, stat]) => {
        const wr = stat.count > 0 ? (stat.wins / stat.count) * 100 : 0;
        const pf = stat.grossLoss > 0 ? (stat.grossWin / stat.grossLoss).toFixed(2) : (stat.grossWin > 0 ? '99.0' : '0.00');
        const pnl = Math.round(stat.netPnL);

        return `
          <tr class="border-b border-slate-800/40">
            <td class="py-2.5 px-2 font-semibold text-white font-sans">${name}</td>
            <td class="py-2.5 px-1 text-center text-slate-300">${stat.count}</td>
            <td class="py-2.5 px-1 text-center font-bold ${wr >= 50 ? 'text-emerald-400' : 'text-amber-400'}">${wr.toFixed(0)}%</td>
            <td class="py-2.5 px-1 text-center text-blue-400 font-bold">${pf}</td>
            <td class="py-2.5 px-2 text-right font-bold ${pnl >= 0 ? 'text-emerald-400' : 'text-rose-400'}">₹${pnl.toLocaleString('en-IN')}</td>
          </tr>
        `;
      }).join('');
    }

    function runMonteCarloSimulation() {
      const trades = tradesData.length > 0 ? tradesData : [];
      let winCount = 0;
      let totalRWin = 0;
      let lossCount = 0;
      let totalRLoss = 0;

      trades.forEach(t => {
        const r = parseFloat(t.r_multiple) || 0;
        if (r > 0) { winCount++; totalRWin += r; }
        else if (r < 0) { lossCount++; totalRLoss += Math.abs(r); }
      });

      const totalTrades = winCount + lossCount;
      const winRate = totalTrades >= 3 ? (winCount / totalTrades) : 0.55;
      const avgWinR = winCount > 0 ? (totalRWin / winCount) : 2.1;
      const avgLossR = lossCount > 0 ? (totalRLoss / lossCount) : 1.0;

      const numSimulations = 1000;
      const tradingDays = 30;
      const tradesPerDay = 2;
      const totalFutureTrades = tradingDays * tradesPerDay;
      const riskPerTradePct = riskModePercent;

      const simulationPaths = [];
      const finalEquities = [];

      for (let sim = 0; sim < numSimulations; sim++) {
        let cap = startingCapital;
        const path = [cap];

        for (let t = 0; t < totalFutureTrades; t++) {
          const riskAmt = cap * riskPerTradePct;
          const isWin = Math.random() < winRate;
          if (isWin) {
            const winR = avgWinR * (0.85 + Math.random() * 0.3);
            cap += riskAmt * winR;
          } else {
            const lossR = avgLossR * (0.9 + Math.random() * 0.2);
            cap -= riskAmt * lossR;
          }
          if ((t + 1) % tradesPerDay === 0) {
            path.push(cap);
          }
        }
        simulationPaths.push(path);
        finalEquities.push(cap);
      }

      finalEquities.sort((a, b) => a - b);
      const perc5 = finalEquities[Math.floor(numSimulations * 0.05)];
      const perc50 = finalEquities[Math.floor(numSimulations * 0.50)];
      const perc95 = finalEquities[Math.floor(numSimulations * 0.95)];

      const perc5Elem = document.getElementById('mcPerc5');
      if (perc5Elem) {
        perc5Elem.textContent = `₹${Math.round(perc5).toLocaleString('en-IN')}`;
        document.getElementById('mcPerc50').textContent = `₹${Math.round(perc50).toLocaleString('en-IN')}`;
        document.getElementById('mcPerc95').textContent = `₹${Math.round(perc95).toLocaleString('en-IN')}`;
      }

      const daysLabels = ['Day 0', ...Array.from({ length: tradingDays }, (_, i) => `Day ${i + 1}`)];
      const curve5 = [];
      const curve50 = [];
      const curve95 = [];

      for (let day = 0; day <= tradingDays; day++) {
        const dayVals = simulationPaths.map(p => p[day]).sort((a, b) => a - b);
        curve5.push(dayVals[Math.floor(numSimulations * 0.05)]);
        curve50.push(dayVals[Math.floor(numSimulations * 0.50)]);
        curve95.push(dayVals[Math.floor(numSimulations * 0.95)]);
      }

      const ctx = document.getElementById('monteCarloChart');
      if (!ctx) return;
      if (chartMonteCarlo) chartMonteCarlo.destroy();

      chartMonteCarlo = new Chart(ctx, {
        type: 'line',
        data: {
          labels: daysLabels,
          datasets: [
            {
              label: '95th Percentile (Favorable)',
              data: curve95,
              borderColor: '#10B981',
              backgroundColor: 'rgba(16, 185, 129, 0.05)',
              fill: '+1',
              borderWidth: 1.5,
              pointRadius: 0
            },
            {
              label: '50th Percentile (Median Expected)',
              data: curve50,
              borderColor: '#3B82F6',
              backgroundColor: 'rgba(59, 130, 246, 0.1)',
              fill: false,
              borderWidth: 2.5,
              pointRadius: 0
            },
            {
              label: '5th Percentile (Drawdown Floor)',
              data: curve5,
              borderColor: '#F43F5E',
              backgroundColor: 'transparent',
              fill: false,
              borderWidth: 1.5,
              pointRadius: 0
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              labels: { color: '#94A3B8', font: { size: 10 } }
            },
            tooltip: {
              callbacks: {
                label: (ctx) => `${ctx.dataset.label}: ₹${Math.round(ctx.parsed.y).toLocaleString('en-IN')}`
              }
            }
          },
          scales: {
            x: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#64748B', font: { size: 10 } } },
            y: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#64748B', font: { size: 10 }, callback: v => '₹' + v.toLocaleString('en-IN') } }
          }
        }
      });
    }

    // --- Initialization on Load ---
    window.addEventListener('DOMContentLoaded', () => {
      const today = new Date().toISOString().split('T')[0];
      const timeElem = document.getElementById('trade_time');
      const dateElem = document.getElementById('trade_date');
      if (dateElem) dateElem.value = today;
      if (timeElem) timeElem.value = '09:25';

      const savedSound = localStorage.getItem('soundEnabled');
      if (savedSound !== null) soundEnabled = (savedSound === 'true');
      updateSoundUI();

      initStartingCapital();
      checkCooldownStatus();
      loadTrades();
      recalculateCalculators();

      updateISTMarketClock();
      setInterval(updateISTMarketClock, 1000);
    });
  </script>
</body>
</html>
'''

def main():
    target_paths = [
        "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/public/index.html",
        "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html",
        "/home/sunny/.gemini/antigravity/brain/85803015-3567-4584-af28-ca9d6eed9423/trader_dashboard.html"
    ]

    for p in target_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(HTML_V7)
        print(f"Successfully written v7: {p} ({len(HTML_V7)} bytes)")

if __name__ == "__main__":
    main()
