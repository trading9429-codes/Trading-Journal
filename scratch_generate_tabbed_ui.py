html_code = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Trader Execution Reset System — Command Center</title>
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
    .glass-card { background: rgba(17, 24, 39, 0.75); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.08); }
    .glass-card-hover:hover { border-color: rgba(59, 130, 246, 0.4); }
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #080D1A; }
    ::-webkit-scrollbar-thumb { background: #1F2937; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #374151; }
  </style>
</head>
<body class="min-h-screen pb-16">

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
          <p class="text-xs text-slate-400">Intraday 1-Minute Equities • FYERS Statutory Charges Calibrated • Max 2 Trades/Day</p>
        </div>
      </div>

      <!-- Execution Status Badges -->
      <div class="flex items-center gap-2 flex-wrap text-xs font-mono">
        <div class="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
          <span class="text-slate-400">Live Clock:</span>
          <span id="istClock" class="font-bold text-slate-200">--:--:-- IST</span>
        </div>
        <div class="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 flex items-center gap-2">
          <span class="text-slate-400">Window:</span>
          <span id="windowStatus" class="font-bold text-amber-400">09:15–10:30 AM IST</span>
        </div>
        <div class="px-3 py-1.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 flex items-center gap-2 text-emerald-300">
          <span>🛡️ Kill Switch:</span>
          <span class="font-bold">ARMED (2 Losses / 2R)</span>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Navigation Tabs -->
  <div class="max-w-7xl mx-auto px-4 lg:px-8 mt-5">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3 flex-wrap gap-3">
      
      <!-- Primary Tab Switcher -->
      <div class="flex items-center gap-2 bg-slate-900/90 p-1.5 rounded-xl border border-slate-800">
        <button type="button" id="tabBtnEntry" onclick="switchTab('entry')" class="px-5 py-2 rounded-lg text-xs font-bold transition flex items-center gap-2 bg-gradient-to-r from-blue-600 to-indigo-600 text-white shadow-md shadow-blue-500/20">
          <span>⚡</span>
          <span>Tab 1: Trade Entry & History Log</span>
        </button>
        <button type="button" id="tabBtnAnalytics" onclick="switchTab('analytics')" class="px-5 py-2 rounded-lg text-xs font-bold transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800/60">
          <span>📊</span>
          <span>Tab 2: Analytics & Visual Metrics</span>
        </button>
      </div>

      <!-- Quick Capital & Return Snapshot Header -->
      <div class="flex items-center gap-3 text-xs font-mono">
        <div class="px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center gap-2">
          <span class="text-slate-400">Starting Capital:</span>
          <span id="headerStartingCap" class="font-bold text-white">₹2,00,000.00</span>
        </div>
        <div class="px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center gap-2">
          <span class="text-slate-400">Current Capital:</span>
          <span id="headerCurrentCap" class="font-bold text-emerald-400">₹2,01,358.05</span>
          <span id="headerROI" class="text-[10px] font-bold px-1.5 py-0.2 rounded bg-emerald-500/20 text-emerald-300">(+0.68%)</span>
        </div>
      </div>

    </div>
  </div>

  <!-- Content Container -->
  <div class="max-w-7xl mx-auto px-4 lg:px-8 mt-6">

    <!-- ========================================================================= -->
    <!-- TAB 1: TRADE ENTRY & HISTORY LOG -->
    <!-- ========================================================================= -->
    <div id="tabContentEntry" class="space-y-6">

      <!-- Fast Trade Logger Card -->
      <div class="glass-card p-6 rounded-2xl shadow-xl relative overflow-hidden border border-blue-500/20">
        <div class="absolute -top-12 -right-12 w-48 h-48 bg-blue-500/10 rounded-full blur-3xl pointer-events-none"></div>

        <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-800 gap-2">
          <div>
            <h2 class="text-base font-extrabold text-white uppercase tracking-wider flex items-center gap-2">
              <span>⚡</span> 10-Second Fast Trade Logger
            </h2>
            <p class="text-xs text-slate-400 mt-0.5">Minimal-friction entry • Automatic Planned RR verification (≥ 2.2 RR) • Exact FYERS statutory costs</p>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs text-slate-400 font-mono">Max Risk Budget (0.25%): <strong id="riskBudgetLabel" class="text-amber-300">₹500.00</strong></span>
            <button type="button" onclick="downloadExcelInfo()" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 font-mono py-1.5 px-3 rounded-lg border border-slate-700 transition flex items-center gap-1.5">
              <span>📊</span> Master Excel
            </button>
          </div>
        </div>

        <div class="mt-4">
          <!-- Quick Watchlist Stock Chips -->
          <div class="flex items-center gap-2 overflow-x-auto pb-2 text-xs">
            <span class="text-[11px] text-slate-400 font-semibold whitespace-nowrap">Watchlist:</span>
            <button type="button" onclick="setSymbol('RELIANCE')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-slate-300 border border-slate-700/60">RELIANCE</button>
            <button type="button" onclick="setSymbol('TCS')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-slate-300 border border-slate-700/60">TCS</button>
            <button type="button" onclick="setSymbol('INFY')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-slate-300 border border-slate-700/60">INFY</button>
            <button type="button" onclick="setSymbol('HDFCBANK')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-slate-300 border border-slate-700/60">HDFCBANK</button>
            <button type="button" onclick="setSymbol('SBIN')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-slate-300 border border-slate-700/60">SBIN</button>
            <button type="button" onclick="setSymbol('ICICIBANK')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-slate-300 border border-slate-700/60">ICICIBANK</button>
            <button type="button" onclick="setSymbol('LT')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-slate-300 border border-slate-700/60">LT</button>
          </div>

          <form id="tradeForm" onsubmit="submitTrade(event)" class="mt-4 space-y-4">
            <!-- Row 1: Symbol, Direction, Entry Price, Stop Price -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
              <div>
                <label class="block text-slate-400 mb-1 font-semibold">Symbol</label>
                <input type="text" id="inpSymbol" required value="SBIN" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-white font-mono uppercase focus:ring-1 focus:ring-blue-500 focus:outline-none">
              </div>

              <div>
                <label class="block text-slate-400 mb-1 font-semibold">Direction</label>
                <div class="grid grid-cols-2 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-700">
                  <button type="button" id="btnLong" onclick="setDirection('Long')" class="py-1.5 rounded-lg font-bold text-xs bg-emerald-600 text-white transition">Long ↗</button>
                  <button type="button" id="btnShort" onclick="setDirection('Short')" class="py-1.5 rounded-lg font-bold text-xs text-slate-400 hover:text-white transition">Short ↘</button>
                </div>
              </div>

              <div>
                <label class="block text-slate-400 mb-1 font-semibold">Entry Price (₹)</label>
                <input type="number" id="inpEntry" required step="0.05" value="780.00" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-white font-mono focus:ring-1 focus:ring-blue-500 focus:outline-none" oninput="onEntryOrStopChange()">
              </div>

              <div>
                <label class="block text-slate-400 mb-1 font-semibold">Stop Price (₹)</label>
                <input type="number" id="inpStop" required step="0.05" value="778.00" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-white font-mono focus:ring-1 focus:ring-blue-500 focus:outline-none" oninput="onEntryOrStopChange()">
              </div>
            </div>

            <!-- Row 2: Target Price, Exit Price, Quantity, Time -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
              <div>
                <label class="block text-slate-400 mb-1 font-semibold flex items-center justify-between">
                  <span>Target Price (₹)</span>
                  <span class="text-[10px] text-emerald-400 font-normal">≥ 2.2R setup</span>
                </label>
                <input type="number" id="inpTarget" required step="0.05" value="784.50" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-white font-mono focus:ring-1 focus:ring-blue-500 focus:outline-none" oninput="calcPreview()">
              </div>

              <div>
                <label class="block text-slate-400 mb-1 font-semibold">Exit Price (₹)</label>
                <input type="number" id="inpExit" required step="0.05" value="784.50" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-white font-mono focus:ring-1 focus:ring-blue-500 focus:outline-none" oninput="calcPreview()">
              </div>

              <div>
                <label class="block text-slate-400 mb-1 font-semibold flex items-center justify-between">
                  <span>Quantity</span>
                  <span id="riskAmtSpan" class="text-[10px] text-slate-400 font-mono">Risk: ₹500</span>
                </label>
                <input type="number" id="inpQty" required step="1" value="250" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-white font-mono focus:ring-1 focus:ring-blue-500 focus:outline-none" oninput="calcPreview()">
              </div>

              <div>
                <label class="block text-slate-400 mb-1 font-semibold">Time (09:15–10:30)</label>
                <input type="text" id="inpTime" value="09:35" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-white font-mono focus:ring-1 focus:ring-blue-500 focus:outline-none">
              </div>
            </div>

            <!-- Row 3: Quality Checklist 5/5 check & Zero Violations -->
            <div class="flex items-center justify-between p-3 rounded-xl bg-slate-900/60 border border-slate-800 text-xs flex-wrap gap-2">
              <label class="inline-flex items-center gap-2.5 cursor-pointer">
                <input type="checkbox" id="inpChecklist5" checked class="w-4 h-4 rounded text-blue-600 bg-slate-900 border-slate-700 focus:ring-0">
                <span class="font-bold text-slate-200">5-Point Checklist Scored 5/5</span>
                <span class="text-[10px] text-slate-400">(Scanner + HTF Context + No Chase + Defined Stop + In Window)</span>
              </label>
              <label class="inline-flex items-center gap-2.5 cursor-pointer">
                <input type="checkbox" id="inpNoViolation" checked class="w-4 h-4 rounded text-emerald-600 bg-slate-900 border-slate-700 focus:ring-0">
                <span class="font-bold text-emerald-400">Zero Rule Violations</span>
              </label>
            </div>

            <!-- Instant Live Reactive Preview Bar -->
            <div class="p-4 rounded-xl bg-slate-900/95 border border-slate-800 grid grid-cols-2 sm:grid-cols-4 gap-3 text-center font-mono text-xs shadow-inner">
              <div class="border-r border-slate-800 pr-2">
                <span class="text-slate-400 text-[10px] block uppercase font-semibold">Planned RR (|Tgt-Ent|/Risk)</span>
                <span id="prevRR" class="font-bold text-emerald-400 text-sm">2.25 RR ✓</span>
              </div>
              <div class="border-r border-slate-800 pr-2">
                <span class="text-slate-400 text-[10px] block uppercase font-semibold">FYERS Statutory Charges</span>
                <span id="prevFriction" class="font-bold text-rose-400 text-sm">₹115.84</span>
              </div>
              <div class="border-r border-slate-800 pr-2">
                <span class="text-slate-400 text-[10px] block uppercase font-semibold">Realized Net P&L</span>
                <span id="prevNetPnL" class="font-bold text-emerald-400 text-sm">+₹1,009.16</span>
              </div>
              <div>
                <span class="text-slate-400 text-[10px] block uppercase font-semibold">Realized Net R</span>
                <span id="prevNetR" class="font-bold text-cyan-400 text-sm">+2.02 R</span>
              </div>
            </div>

            <!-- Detailed Charges Breakdown Pill -->
            <div id="chargesBreakdownText" class="text-[11px] font-mono text-slate-400 bg-slate-900/40 px-3.5 py-1.5 rounded-lg border border-slate-800 text-center">
              FYERS Breakdown: Brokerage: ₹40.00 • STT: ₹49.03 • Exch: ₹11.62 • SEBI: ₹0.04 • Stamp: ₹5.85 • GST: ₹9.30
            </div>

            <!-- Action Buttons -->
            <div class="flex items-center gap-3 pt-1">
              <button type="submit" id="submitBtn" class="flex-1 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-extrabold py-3.5 px-4 rounded-xl shadow-lg shadow-blue-600/30 transition text-xs flex items-center justify-center gap-2">
                <span>💾</span> Log Trade & Synchronize
              </button>
              <button type="button" onclick="copyExcelRow()" class="bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold py-3.5 px-4 rounded-xl border border-slate-700 transition text-xs flex items-center gap-1.5 whitespace-nowrap">
                <span>📋</span> Copy for Excel Quick_Log
              </button>
            </div>
          </form>
        </div>
      </div>

      <!-- Trade History Log Table Card -->
      <div class="glass-card rounded-2xl p-6 shadow-xl">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div>
            <h2 class="text-base font-extrabold text-white uppercase tracking-wider flex items-center gap-2">
              <span>📋</span> Trade Execution Journal & History Log
            </h2>
            <p class="text-xs text-slate-400 mt-0.5">Direct 1:1 mapping with `Quick_Log` & `Trade_Log` tabs in Excel.</p>
          </div>
          <div class="flex items-center gap-2">
            <button type="button" onclick="clearExamples()" class="px-3 py-1.5 rounded-lg bg-rose-500/10 hover:bg-rose-500/20 text-rose-400 border border-rose-500/30 text-xs font-bold transition">
              🗑️ Clear Examples
            </button>
            <button type="button" onclick="reloadDefaults()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold transition">
              🔄 Reload Benchmark Seed
            </button>
          </div>
        </div>

        <div class="overflow-x-auto mt-4">
          <table class="w-full text-xs text-left font-mono">
            <thead class="text-[11px] uppercase bg-slate-900/90 text-slate-400 border-b border-slate-800">
              <tr>
                <th class="p-2.5">Trade ID</th>
                <th class="p-2.5">Date & Time</th>
                <th class="p-2.5">Symbol</th>
                <th class="p-2.5">Side</th>
                <th class="p-2.5 text-right">Entry</th>
                <th class="p-2.5 text-right">Stop</th>
                <th class="p-2.5 text-right">Target</th>
                <th class="p-2.5 text-right">Exit</th>
                <th class="p-2.5 text-right">Qty</th>
                <th class="p-2.5 text-right">Planned RR</th>
                <th class="p-2.5 text-right">FYERS Costs</th>
                <th class="p-2.5 text-right">Net P&L</th>
                <th class="p-2.5 text-right">Net R</th>
                <th class="p-2.5 text-center">Outcome</th>
              </tr>
            </thead>
            <tbody id="tradeTableBody" class="divide-y divide-slate-800 text-slate-200">
              <!-- Dynamically populated -->
            </tbody>
          </table>
        </div>
      </div>

    </div>

    <!-- ========================================================================= -->
    <!-- TAB 2: ANALYTICS, METRICS & VISUAL CHARTS -->
    <!-- ========================================================================= -->
    <div id="tabContentAnalytics" class="space-y-6 hidden">

      <!-- Configuration Card: Starting Capital & Risk Parameter Enforcer -->
      <div class="glass-card p-5 rounded-2xl shadow-xl border border-indigo-500/20 flex flex-col lg:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-indigo-500/10 border border-indigo-500/30 flex items-center justify-center text-indigo-400 text-lg font-bold">
            💰
          </div>
          <div>
            <h3 class="text-sm font-bold text-white uppercase tracking-wider">Account Starting Capital & Risk Allocation</h3>
            <p class="text-xs text-slate-400 mt-0.5">Powers portfolio ROI %, real-world equity curve, and strict 0.25%–0.50% position sizing.</p>
          </div>
        </div>

        <!-- Starting Capital Inputs & Presets -->
        <div class="flex items-center gap-2 flex-wrap text-xs">
          <div class="flex items-center gap-1.5 bg-slate-900 border border-slate-700 px-3 py-1.5 rounded-xl font-mono">
            <span class="text-slate-400 font-bold">₹</span>
            <input type="number" id="inpStartingCapital" value="200000" step="5000" class="w-28 bg-transparent text-white font-bold focus:outline-none" onchange="updateStartingCapital(this.value)">
          </div>
          <button type="button" onclick="quickSetCapital(100000)" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-slate-300">1 Lakh</button>
          <button type="button" onclick="quickSetCapital(200000)" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-slate-300">2 Lakh</button>
          <button type="button" onclick="quickSetCapital(500000)" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-slate-300">5 Lakh</button>
          <button type="button" onclick="quickSetCapital(1000000)" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-slate-300">10 Lakh</button>
        </div>
      </div>

      <!-- Date Filter Bar (Powers all metrics, charts & distributions) -->
      <div class="glass-card p-3.5 rounded-2xl shadow-xl flex flex-col md:flex-row items-center justify-between gap-3 border border-slate-800">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="text-xs font-bold text-slate-300 flex items-center gap-1.5 uppercase tracking-wider mr-1">
            <span>📅</span> Date Range:
          </span>
          <button type="button" onclick="setDateFilter('all')" id="btnFilterAll" class="px-3 py-1 rounded-lg text-xs font-bold bg-blue-600 text-white transition shadow-sm shadow-blue-500/20">All Time</button>
          <button type="button" onclick="setDateFilter('today')" id="btnFilterToday" class="px-3 py-1 rounded-lg text-xs font-bold bg-slate-800 text-slate-400 hover:text-white transition">Today</button>
          <button type="button" onclick="setDateFilter('yesterday')" id="btnFilterYesterday" class="px-3 py-1 rounded-lg text-xs font-bold bg-slate-800 text-slate-400 hover:text-white transition">Yesterday</button>
          <button type="button" onclick="setDateFilter('week')" id="btnFilterWeek" class="px-3 py-1 rounded-lg text-xs font-bold bg-slate-800 text-slate-400 hover:text-white transition">This Week</button>
          <button type="button" onclick="setDateFilter('seed')" id="btnFilterSeed" class="px-3 py-1 rounded-lg text-xs font-bold bg-slate-800 text-slate-400 hover:text-white transition">Oct 20–21 (Seed)</button>
        </div>

        <div class="flex items-center gap-2 flex-wrap text-xs font-mono">
          <div class="flex items-center gap-1.5 bg-slate-900 border border-slate-700/80 px-2.5 py-1 rounded-lg">
            <span class="text-slate-400 text-[11px]">From:</span>
            <input type="date" id="filterFromDate" class="bg-transparent text-white focus:outline-none text-xs" onchange="onCustomDateChange()">
          </div>
          <div class="flex items-center gap-1.5 bg-slate-900 border border-slate-700/80 px-2.5 py-1 rounded-lg">
            <span class="text-slate-400 text-[11px]">To:</span>
            <input type="date" id="filterToDate" class="bg-transparent text-white focus:outline-none text-xs" onchange="onCustomDateChange()">
          </div>
          <button type="button" onclick="resetDateFilter()" title="Reset Filter" class="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">
            🔄
          </button>
          <span id="filterActiveBadge" class="text-[11px] font-bold px-2.5 py-1 rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 whitespace-nowrap">
            Showing 3 of 3 Trades
          </span>
        </div>
      </div>

      <!-- Comprehensive Trading Metrics Grid (8 KPI Cards) -->
      <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3">
        
        <!-- 1. Current Capital -->
        <div class="glass-card glass-card-hover p-3.5 rounded-xl border-l-4 border-l-emerald-500">
          <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Current Capital</div>
          <div id="metricCurrentCap" class="text-base font-extrabold font-mono text-emerald-400 mt-1">₹2,01,358</div>
          <div id="metricROI" class="text-[10px] font-bold text-emerald-300 mt-0.5">+0.68% ROI</div>
        </div>

        <!-- 2. Net Realized P&L -->
        <div class="glass-card glass-card-hover p-3.5 rounded-xl border-l-4 border-l-emerald-500">
          <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Net Realized P&L</div>
          <div id="metricNetPnL" class="text-base font-extrabold font-mono text-emerald-400 mt-1">+₹1,358.05</div>
          <div class="text-[10px] text-slate-400 mt-0.5">Net of FYERS</div>
        </div>

        <!-- 3. Profit Factor -->
        <div class="glass-card glass-card-hover p-3.5 rounded-xl border-l-4 border-l-blue-500">
          <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Profit Factor</div>
          <div id="metricProfitFactor" class="text-base font-extrabold font-mono text-blue-400 mt-1">3.23</div>
          <div class="text-[10px] text-slate-400 mt-0.5">Wins / Losses</div>
        </div>

        <!-- 4. Expectancy (R) -->
        <div class="glass-card glass-card-hover p-3.5 rounded-xl border-l-4 border-l-cyan-500">
          <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Avg Net R / Trade</div>
          <div id="metricAvgR" class="text-base font-extrabold font-mono text-cyan-400 mt-1">+0.90 R</div>
          <div id="metricExpRupee" class="text-[10px] text-slate-400 mt-0.5">+₹452 / trade</div>
        </div>

        <!-- 5. Win Rate % -->
        <div class="glass-card glass-card-hover p-3.5 rounded-xl border-l-4 border-l-indigo-500">
          <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Win Rate %</div>
          <div id="metricWinRate" class="text-base font-extrabold font-mono text-indigo-400 mt-1">66.7%</div>
          <div id="metricWinLossCounts" class="text-[10px] text-slate-400 mt-0.5">2 W / 1 L</div>
        </div>

        <!-- 6. Payoff Ratio (Avg Win / Avg Loss) -->
        <div class="glass-card glass-card-hover p-3.5 rounded-xl border-l-4 border-l-purple-500">
          <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Payoff Ratio</div>
          <div id="metricPayoff" class="text-base font-extrabold font-mono text-purple-400 mt-1">1.62</div>
          <div id="metricAvgWinLoss" class="text-[10px] text-slate-400 mt-0.5">₹983 / ₹609</div>
        </div>

        <!-- 7. Max Drawdown -->
        <div class="glass-card glass-card-hover p-3.5 rounded-xl border-l-4 border-l-amber-500">
          <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Max Drawdown</div>
          <div id="metricMaxDD" class="text-base font-extrabold font-mono text-amber-400 mt-1">-₹608.54</div>
          <div id="metricMaxDDPct" class="text-[10px] text-slate-400 mt-0.5">-0.30% of peak</div>
        </div>

        <!-- 8. FYERS Friction Drag -->
        <div class="glass-card glass-card-hover p-3.5 rounded-xl border-l-4 border-l-rose-500">
          <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400">FYERS Charges</div>
          <div id="metricFriction" class="text-base font-extrabold font-mono text-rose-400 mt-1">₹341.95</div>
          <div id="metricFrictionDrag" class="text-[10px] text-slate-400 mt-0.5">14.8% Drag</div>
        </div>

      </div>

      <!-- Charts Row 1: Real-World Account Equity Curve (7 cols) + Win/Loss Pipe/Donut (5 cols) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

        <!-- Account Equity Curve (7 cols) -->
        <div class="lg:col-span-7 glass-card p-5 rounded-2xl shadow-xl">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <h2 class="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
                <span>📈</span> Real-World Account Equity Curve (₹)
              </h2>
              <p class="text-xs text-slate-400 mt-0.5">Starting capital evolving trade-by-trade net of all statutory friction.</p>
            </div>
            <span id="equityFilterLabel" class="text-xs font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">ALL TIME</span>
          </div>
          <div class="mt-4 h-72">
            <canvas id="equityChart"></canvas>
          </div>
        </div>

        <!-- Outcome Pipe / Donut Chart (5 cols) -->
        <div class="lg:col-span-5 glass-card p-5 rounded-2xl shadow-xl flex flex-col justify-between">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <h2 class="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
                <span>🍩</span> Trade Outcome Distribution
              </h2>
              <p class="text-xs text-slate-400 mt-0.5">Wins vs Losses vs Breakeven (Pipe Chart)</p>
            </div>
            <span id="totalTradesBadge" class="text-xs font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-300">3 Trades</span>
          </div>
          <div class="mt-4 h-56 flex items-center justify-center">
            <canvas id="outcomeDonutChart"></canvas>
          </div>
          <div class="pt-3 border-t border-slate-800/80 flex items-center justify-around text-xs font-mono text-center">
            <div><span class="text-emerald-400 font-bold block text-sm" id="donutWins">2 Wins</span><span class="text-[10px] text-slate-400">Target Hit</span></div>
            <div><span class="text-rose-400 font-bold block text-sm" id="donutLosses">1 Loss</span><span class="text-[10px] text-slate-400">Stop Respected</span></div>
            <div><span class="text-amber-400 font-bold block text-sm" id="donutBE">0 BE</span><span class="text-[10px] text-slate-400">Breakeven</span></div>
          </div>
        </div>

      </div>

      <!-- Charts Row 2: Net R-Expectancy Histogram + Long vs Short Setup Breakdown -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

        <!-- R-Multiple Distribution Bar Chart (7 cols) -->
        <div class="lg:col-span-7 glass-card p-5 rounded-2xl shadow-xl">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <h2 class="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
                <span>📊</span> Realized Net R-Multiple Distribution
              </h2>
              <p class="text-xs text-slate-400 mt-0.5">Expectancy target: Win bars ≥ +1.8R, Losses strictly capped at -1.0R to -1.25R.</p>
            </div>
            <span class="text-xs font-mono text-cyan-400 font-bold">R-Expectancy</span>
          </div>
          <div class="mt-4 h-64">
            <canvas id="rMultipleChart"></canvas>
          </div>
        </div>

        <!-- Long vs Short Discipline & Setup Breakdown (5 cols) -->
        <div class="lg:col-span-5 glass-card p-5 rounded-2xl shadow-xl flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
              <h2 class="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
                <span>⚖️</span> Long vs Short Setup Breakdown
              </h2>
              <span class="text-xs font-mono text-slate-400">Directional Edge</span>
            </div>

            <div class="mt-4 space-y-4 font-mono text-xs">
              <!-- Long Side -->
              <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800">
                <div class="flex items-center justify-between pb-1">
                  <span class="font-bold text-emerald-400 flex items-center gap-1.5">
                    <span>↗</span> Long Trades (<span id="longTradesCount">2</span>)
                  </span>
                  <span id="longWinRate" class="font-bold text-emerald-400">100.0% Win Rate</span>
                </div>
                <div class="flex items-center justify-between text-slate-400 text-[11px] mt-1 pt-1 border-t border-slate-800/60">
                  <span>Net P&L: <strong id="longNetPnL" class="text-emerald-300">+₹1,966.59</strong></span>
                  <span>Avg R: <strong id="longAvgR" class="text-cyan-300">+1.97 R</strong></span>
                </div>
              </div>

              <!-- Short Side -->
              <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800">
                <div class="flex items-center justify-between pb-1">
                  <span class="font-bold text-rose-400 flex items-center gap-1.5">
                    <span>↘</span> Short Trades (<span id="shortTradesCount">1</span>)
                  </span>
                  <span id="shortWinRate" class="font-bold text-rose-400">0.0% Win Rate</span>
                </div>
                <div class="flex items-center justify-between text-slate-400 text-[11px] mt-1 pt-1 border-t border-slate-800/60">
                  <span>Net P&L: <strong id="shortNetPnL" class="text-rose-300">-₹608.54</strong></span>
                  <span>Avg R: <strong id="shortAvgR" class="text-rose-300">-1.22 R</strong></span>
                </div>
              </div>
            </div>
          </div>

          <!-- Discipline Seal -->
          <div class="mt-4 p-3 rounded-xl bg-emerald-950/20 border border-emerald-500/20 flex items-center justify-between text-xs font-mono">
            <div>
              <span class="text-slate-400 block text-[10px]">EXECUTION QUALITY</span>
              <span class="font-bold text-emerald-400">5/5 Checklist: 100% (3/3)</span>
            </div>
            <div class="text-right">
              <span class="text-slate-400 block text-[10px]">RULE LEAKS</span>
              <span class="font-bold text-emerald-400">0 Violations</span>
            </div>
          </div>
        </div>

      </div>

    </div>

  </div>

  <script>
    // System State
    let activeDirection = 'Long';
    let currentFilterMode = 'all';
    let filterFrom = null;
    let filterTo = null;
    let startingCapital = parseFloat(localStorage.getItem('trader_starting_capital')) || 200000.0;

    // Verified seed trades
    let tradesData = [
      {
        id: 'T-001',
        date: '2026-10-20',
        time: '09:25',
        symbol: 'RELIANCE',
        direction: 'Long',
        entry_price: 2500.00,
        stop_price: 2495.00,
        target_price: 2511.00,
        exit_price: 2511.00,
        qty: 100,
        rr_planned: 2.20,
        costs: 135.10,
        net_pnl: 964.90,
        r_multiple: 1.93,
        outcome: 'Win',
        checklist_score: 5,
        rule_violation: 'N'
      },
      {
        id: 'T-002',
        date: '2026-10-20',
        time: '10:05',
        symbol: 'TCS',
        direction: 'Short',
        entry_price: 3500.00,
        stop_price: 3510.00,
        target_price: 3478.00,
        exit_price: 3510.00,
        qty: 50,
        rr_planned: 2.20,
        costs: 108.54,
        net_pnl: -608.54,
        r_multiple: -1.22,
        outcome: 'Loss',
        checklist_score: 5,
        rule_violation: 'N'
      },
      {
        id: 'T-003',
        date: '2026-10-21',
        time: '09:40',
        symbol: 'INFY',
        direction: 'Long',
        entry_price: 1450.00,
        stop_price: 1445.00,
        target_price: 1461.00,
        exit_price: 1461.00,
        qty: 100,
        rr_planned: 2.20,
        costs: 98.31,
        net_pnl: 1001.69,
        r_multiple: 2.00,
        outcome: 'Win',
        checklist_score: 5,
        rule_violation: 'N'
      }
    ];

    let equityChart, outcomeChart, rChart;

    // Tab Switching Logic
    function switchTab(tab) {
      const contentEntry = document.getElementById('tabContentEntry');
      const contentAnalytics = document.getElementById('tabContentAnalytics');
      const btnEntry = document.getElementById('tabBtnEntry');
      const btnAnalytics = document.getElementById('tabBtnAnalytics');

      const activeClass = 'px-5 py-2 rounded-lg text-xs font-bold transition flex items-center gap-2 bg-gradient-to-r from-blue-600 to-indigo-600 text-white shadow-md shadow-blue-500/20';
      const inactiveClass = 'px-5 py-2 rounded-lg text-xs font-bold transition flex items-center gap-2 text-slate-400 hover:text-white hover:bg-slate-800/60';

      if (tab === 'entry') {
        contentEntry.classList.remove('hidden');
        contentAnalytics.classList.add('hidden');
        btnEntry.className = activeClass;
        btnAnalytics.className = inactiveClass;
      } else {
        contentEntry.classList.add('hidden');
        contentAnalytics.classList.remove('hidden');
        btnAnalytics.className = activeClass;
        btnEntry.className = inactiveClass;
        renderAnalyticsView();
      }
    }

    // Capital Setting Handlers
    function updateStartingCapital(val) {
      const num = parseFloat(val);
      if (!isNaN(num) && num > 0) {
        startingCapital = num;
        localStorage.setItem('trader_starting_capital', startingCapital);
        document.getElementById('inpStartingCapital').value = startingCapital;
        renderTopCapitalHeader();
        renderAnalyticsView();
        calcPreview();
      }
    }

    function quickSetCapital(val) {
      updateStartingCapital(val);
    }

    function renderTopCapitalHeader() {
      const netTotal = tradesData.reduce((acc, t) => acc + Number(t.net_pnl), 0);
      const curr = startingCapital + netTotal;
      const roi = startingCapital > 0 ? ((netTotal / startingCapital) * 100) : 0;

      document.getElementById('headerStartingCap').textContent = '₹' + startingCapital.toLocaleString('en-IN', {minimumFractionDigits: 2});
      document.getElementById('headerCurrentCap').textContent = '₹' + curr.toLocaleString('en-IN', {minimumFractionDigits: 2});
      const roiElem = document.getElementById('headerROI');
      roiElem.textContent = (roi >= 0 ? '+' : '') + roi.toFixed(2) + '%';
      roiElem.className = roi >= 0 ? 'text-[10px] font-bold px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300' : 'text-[10px] font-bold px-1.5 py-0.5 rounded bg-rose-500/20 text-rose-300';

      const risk025 = startingCapital * 0.0025;
      document.getElementById('riskBudgetLabel').textContent = '₹' + risk025.toFixed(2);
    }

    // Filter helper
    function getFilteredTrades() {
      if (!filterFrom && !filterTo) {
        return tradesData;
      }
      return tradesData.filter(t => {
        if (filterFrom && t.date < filterFrom) return false;
        if (filterTo && t.date > filterTo) return false;
        return true;
      });
    }

    function setDateFilter(mode) {
      currentFilterMode = mode;
      const today = new Date();
      const todayStr = today.toISOString().split('T')[0];

      const fromInput = document.getElementById('filterFromDate');
      const toInput = document.getElementById('filterToDate');

      if (mode === 'all') {
        filterFrom = null;
        filterTo = null;
        fromInput.value = '';
        toInput.value = '';
      } else if (mode === 'today') {
        filterFrom = todayStr;
        filterTo = todayStr;
        fromInput.value = todayStr;
        toInput.value = todayStr;
      } else if (mode === 'yesterday') {
        const y = new Date(today);
        y.setDate(y.getDate() - 1);
        const yStr = y.toISOString().split('T')[0];
        filterFrom = yStr;
        filterTo = yStr;
        fromInput.value = yStr;
        toInput.value = yStr;
      } else if (mode === 'week') {
        const d = new Date(today);
        const day = d.getDay();
        const diff = d.getDate() - day + (day === 0 ? -6 : 1);
        const monday = new Date(d.setDate(diff));
        const sunday = new Date(monday);
        sunday.setDate(monday.getDate() + 6);
        filterFrom = monday.toISOString().split('T')[0];
        filterTo = sunday.toISOString().split('T')[0];
        fromInput.value = filterFrom;
        toInput.value = filterTo;
      } else if (mode === 'seed') {
        filterFrom = '2026-10-20';
        filterTo = '2026-10-21';
        fromInput.value = filterFrom;
        toInput.value = filterTo;
      }

      updateFilterButtonsUI();
      renderAnalyticsView();
    }

    function onCustomDateChange() {
      currentFilterMode = 'custom';
      filterFrom = document.getElementById('filterFromDate').value || null;
      filterTo = document.getElementById('filterToDate').value || null;
      updateFilterButtonsUI();
      renderAnalyticsView();
    }

    function resetDateFilter() {
      setDateFilter('all');
    }

    function updateFilterButtonsUI() {
      const btnAll = document.getElementById('btnFilterAll');
      const btnToday = document.getElementById('btnFilterToday');
      const btnYesterday = document.getElementById('btnFilterYesterday');
      const btnWeek = document.getElementById('btnFilterWeek');
      const btnSeed = document.getElementById('btnFilterSeed');

      const inactiveClass = 'px-3 py-1 rounded-lg text-xs font-bold bg-slate-800 text-slate-400 hover:text-white transition';
      const activeClass = 'px-3 py-1 rounded-lg text-xs font-bold bg-blue-600 text-white transition shadow-sm shadow-blue-500/20';

      btnAll.className = currentFilterMode === 'all' ? activeClass : inactiveClass;
      btnToday.className = currentFilterMode === 'today' ? activeClass : inactiveClass;
      btnYesterday.className = currentFilterMode === 'yesterday' ? activeClass : inactiveClass;
      btnWeek.className = currentFilterMode === 'week' ? activeClass : inactiveClass;
      btnSeed.className = currentFilterMode === 'seed' ? activeClass : inactiveClass;

      const labelElem = document.getElementById('equityFilterLabel');
      if (currentFilterMode === 'all') labelElem.textContent = 'ALL TIME';
      else if (currentFilterMode === 'today') labelElem.textContent = 'TODAY';
      else if (currentFilterMode === 'yesterday') labelElem.textContent = 'YESTERDAY';
      else if (currentFilterMode === 'week') labelElem.textContent = 'THIS WEEK';
      else if (currentFilterMode === 'seed') labelElem.textContent = 'OCT 20–21';
      else labelElem.textContent = (filterFrom || 'Start') + ' → ' + (filterTo || 'End');
    }

    // FYERS Equity Intraday Charges Calculator
    function calculateFyersCharges(entry, exit, qty, direction) {
      const buyPrice = direction === 'Long' ? entry : exit;
      const sellPrice = direction === 'Long' ? exit : entry;
      
      const buyTurnover = buyPrice * qty;
      const sellTurnover = sellPrice * qty;
      const totalTurnover = buyTurnover + sellTurnover;
      
      const brokBuy = Math.min(buyTurnover * 0.0003, 20.0);
      const brokSell = Math.min(sellTurnover * 0.0003, 20.0);
      const totalBrokerage = brokBuy + brokSell;
      
      const stt = sellTurnover * 0.00025;
      const exch = totalTurnover * 0.0000297;
      const sebi = totalTurnover * 0.0000001;
      const stamp = buyTurnover * 0.00003;
      const gst = (totalBrokerage + exch + sebi) * 0.18;
      
      const totalCosts = totalBrokerage + stt + exch + sebi + stamp + gst;
      
      return {
        buyTurnover,
        sellTurnover,
        totalTurnover,
        brokerage: Math.round(totalBrokerage * 100) / 100,
        stt: Math.round(stt * 100) / 100,
        exchangeCharges: Math.round(exch * 100) / 100,
        sebiFee: Math.round(sebi * 100) / 100,
        stampDuty: Math.round(stamp * 100) / 100,
        gst: Math.round(gst * 100) / 100,
        totalCosts: Math.round(totalCosts * 100) / 100
      };
    }

    function setDirection(dir) {
      activeDirection = dir;
      const btnL = document.getElementById('btnLong');
      const btnS = document.getElementById('btnShort');
      if (dir === 'Long') {
        btnL.className = 'py-1.5 rounded-lg font-bold text-xs bg-emerald-600 text-white transition';
        btnS.className = 'py-1.5 rounded-lg font-bold text-xs text-slate-400 hover:text-white transition';
      } else {
        btnS.className = 'py-1.5 rounded-lg font-bold text-xs bg-rose-600 text-white transition';
        btnL.className = 'py-1.5 rounded-lg font-bold text-xs text-slate-400 hover:text-white transition';
      }
      onEntryOrStopChange();
    }

    function setSymbol(sym) {
      document.getElementById('inpSymbol').value = sym;
      calcPreview();
    }

    function onEntryOrStopChange() {
      const entry = parseFloat(document.getElementById('inpEntry').value) || 0;
      const stop = parseFloat(document.getElementById('inpStop').value) || 0;
      const risk = Math.abs(entry - stop);
      
      if (entry > 0 && risk > 0) {
        const suggestedTarget = activeDirection === 'Long' ? (entry + 2.2 * risk) : (entry - 2.2 * risk);
        const tgtElem = document.getElementById('inpTarget');
        if (!tgtElem.dataset.userEdited) {
          tgtElem.value = (Math.round(suggestedTarget * 20) / 20).toFixed(2);
        }
      }
      calcPreview();
    }

    function calcPreview() {
      const entry = parseFloat(document.getElementById('inpEntry').value) || 0;
      const stop = parseFloat(document.getElementById('inpStop').value) || 0;
      const target = parseFloat(document.getElementById('inpTarget').value) || 0;
      const exit = parseFloat(document.getElementById('inpExit').value) || 0;
      const qty = parseFloat(document.getElementById('inpQty').value) || 0;

      if (entry > 0 && stop > 0 && qty > 0) {
        const riskPerShare = Math.abs(entry - stop);
        const totalRisk = riskPerShare * qty;
        document.getElementById('riskAmtSpan').textContent = 'Risk: ₹' + totalRisk.toFixed(2);

        // Planned RR check
        const plannedReward = target > 0 ? Math.abs(target - entry) : Math.abs(exit - entry);
        const plannedRR = riskPerShare > 0 ? (plannedReward / riskPerShare) : 0;

        // FYERS Charges
        const charges = calculateFyersCharges(entry, exit > 0 ? exit : entry, qty, activeDirection);

        // Net P&L & Net R
        const realizedReward = activeDirection === 'Long' ? (exit - entry) : (entry - exit);
        const grossPnL = realizedReward * qty;
        const netPnL = grossPnL - charges.totalCosts;
        const netR = totalRisk > 0 ? (netPnL / totalRisk) : 0;

        // Preview UI
        const rrElem = document.getElementById('prevRR');
        const isRRValid = plannedRR >= 2.2;
        rrElem.textContent = plannedRR.toFixed(2) + ' RR' + (isRRValid ? ' ✓' : ' ⚠ <2.2');
        rrElem.className = isRRValid ? 'font-bold text-emerald-400 text-sm' : 'font-bold text-rose-400 text-sm animate-pulse';

        document.getElementById('prevFriction').textContent = '₹' + charges.totalCosts.toFixed(2);
        document.getElementById('chargesBreakdownText').textContent = 
          `FYERS Breakdown: Brokerage: ₹${charges.brokerage.toFixed(2)} • STT: ₹${charges.stt.toFixed(2)} • Exch: ₹${charges.exchangeCharges.toFixed(2)} • SEBI: ₹${charges.sebiFee.toFixed(2)} • Stamp: ₹${charges.stampDuty.toFixed(2)} • GST: ₹${charges.gst.toFixed(2)}`;

        const netElem = document.getElementById('prevNetPnL');
        netElem.textContent = (netPnL >= 0 ? '+₹' : '-₹') + Math.abs(netPnL).toFixed(2);
        netElem.className = netPnL >= 0 ? 'font-bold text-emerald-400 text-sm' : 'font-bold text-rose-400 text-sm';

        const rElem = document.getElementById('prevNetR');
        rElem.textContent = (netR >= 0 ? '+' : '') + netR.toFixed(2) + ' R';
        rElem.className = netR >= 0 ? 'font-bold text-cyan-400 text-sm' : 'font-bold text-rose-400 text-sm';
      }
    }

    // Render Tab 1 Table
    function renderTradeTable() {
      const tbody = document.getElementById('tradeTableBody');
      tbody.innerHTML = '';
      if (tradesData.length === 0) {
        tbody.innerHTML = '<tr><td colspan="14" class="p-8 text-center text-slate-500 italic">No trades logged yet. Use the 10-Second Fast Logger above to enter your first trade!</td></tr>';
      } else {
        tradesData.slice().reverse().forEach(t => {
          const tr = document.createElement('tr');
          tr.className = 'hover:bg-slate-800/40 transition';
          tr.innerHTML = `
            <td class="p-2.5 font-bold text-blue-400">${t.id}</td>
            <td class="p-2.5 text-slate-400">${t.date} ${t.time}</td>
            <td class="p-2.5 font-bold">${t.symbol}</td>
            <td class="p-2.5"><span class="px-1.5 py-0.5 rounded ${t.direction === 'Long' ? 'bg-emerald-500/10 text-emerald-400' : 'bg-rose-500/10 text-rose-400'} font-bold">${t.direction}</span></td>
            <td class="p-2.5 text-right font-mono">₹${Number(t.entry_price).toFixed(2)}</td>
            <td class="p-2.5 text-right font-mono">₹${Number(t.stop_price).toFixed(2)}</td>
            <td class="p-2.5 text-right font-mono text-emerald-300">₹${Number(t.target_price || (t.entry_price + 2.2*Math.abs(t.entry_price-t.stop_price))).toFixed(2)}</td>
            <td class="p-2.5 text-right font-mono">₹${Number(t.exit_price).toFixed(2)}</td>
            <td class="p-2.5 text-right font-mono">${t.qty}</td>
            <td class="p-2.5 text-right font-mono ${t.rr_planned >= 2.2 ? 'text-emerald-400' : 'text-rose-400'} font-bold">${Number(t.rr_planned).toFixed(2)}</td>
            <td class="p-2.5 text-right font-mono text-rose-400">₹${Number(t.costs).toFixed(2)}</td>
            <td class="p-2.5 text-right font-mono font-bold ${t.net_pnl >= 0 ? 'text-emerald-400' : 'text-rose-400'}">${t.net_pnl >= 0 ? '+' : ''}₹${Number(t.net_pnl).toFixed(2)}</td>
            <td class="p-2.5 text-right font-mono font-bold ${t.r_multiple >= 0 ? 'text-cyan-400' : 'text-rose-400'}">${t.r_multiple >= 0 ? '+' : ''}${Number(t.r_multiple).toFixed(2)} R</td>
            <td class="p-2.5 text-center"><span class="px-1.5 py-0.5 rounded ${t.outcome === 'Win' ? 'bg-emerald-500/20 text-emerald-300' : 'bg-rose-500/20 text-rose-300'} font-bold">${t.outcome}</span></td>
          `;
          tbody.appendChild(tr);
        });
      }
    }

    // Render Tab 2 Analytics View (Metrics + Visuals)
    function renderAnalyticsView() {
      const filtered = getFilteredTrades();
      const n = filtered.length;
      const totalAll = tradesData.length;

      // Update badge
      const badge = document.getElementById('filterActiveBadge');
      badge.textContent = `Showing ${n} of ${totalAll} Trades`;
      badge.className = n < totalAll ? 'text-[11px] font-bold px-2.5 py-1 rounded-lg bg-amber-500/10 text-amber-400 border border-amber-500/30 whitespace-nowrap' : 'text-[11px] font-bold px-2.5 py-1 rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 whitespace-nowrap';

      // Calculations
      let totalNet = 0;
      let totalR = 0;
      let totalCosts = 0;
      let wins = 0;
      let losses = 0;
      let be = 0;
      let grossWins = 0;
      let grossLosses = 0;

      let longCount = 0;
      let longWins = 0;
      let longNet = 0;
      let longR = 0;

      let shortCount = 0;
      let shortWins = 0;
      let shortNet = 0;
      let shortR = 0;

      // Calculate Drawdown
      let peakCapital = startingCapital;
      let maxDDAmount = 0;
      let maxDDPct = 0;
      let runningCap = startingCapital;

      filtered.forEach(t => {
        const net = Number(t.net_pnl);
        const r = Number(t.r_multiple);
        const cost = Number(t.costs);

        totalNet += net;
        totalR += r;
        totalCosts += cost;

        if (t.outcome === 'Win') {
          wins++;
          grossWins += net;
        } else if (t.outcome === 'Loss') {
          losses++;
          grossLosses += Math.abs(net);
        } else {
          be++;
        }

        if (t.direction === 'Long') {
          longCount++;
          longNet += net;
          longR += r;
          if (t.outcome === 'Win') longWins++;
        } else {
          shortCount++;
          shortNet += net;
          shortR += r;
          if (t.outcome === 'Win') shortWins++;
        }

        // Drawdown tracking
        runningCap += net;
        if (runningCap > peakCapital) {
          peakCapital = runningCap;
        } else {
          const dd = peakCapital - runningCap;
          const ddPct = peakCapital > 0 ? (dd / peakCapital) * 100 : 0;
          if (dd > maxDDAmount) maxDDAmount = dd;
          if (ddPct > maxDDPct) maxDDPct = ddPct;
        }
      });

      const currentCap = startingCapital + totalNet;
      const roiPct = startingCapital > 0 ? (totalNet / startingCapital) * 100 : 0;
      const profitFactor = grossLosses > 0 ? (grossWins / grossLosses) : (grossWins > 0 ? 99.9 : 0);
      const avgR = n > 0 ? (totalR / n) : 0;
      const winRate = n > 0 ? ((wins / n) * 100) : 0;
      const avgWin = wins > 0 ? (grossWins / wins) : 0;
      const avgLoss = losses > 0 ? (grossLosses / losses) : 0;
      const payoff = avgLoss > 0 ? (avgWin / avgLoss) : (avgWin > 0 ? 99.9 : 0);
      const expRupee = n > 0 ? (totalNet / n) : 0;
      const frictionDrag = (grossWins + totalCosts) > 0 ? ((totalCosts / (grossWins + totalCosts)) * 100) : 0;

      // Populate 8 KPI Metric Cards
      document.getElementById('metricCurrentCap').textContent = '₹' + currentCap.toLocaleString('en-IN', {maximumFractionDigits: 0});
      document.getElementById('metricROI').textContent = `${roiPct >= 0 ? '+' : ''}${roiPct.toFixed(2)}% ROI`;
      document.getElementById('metricROI').className = roiPct >= 0 ? 'text-[10px] font-bold text-emerald-300 mt-0.5' : 'text-[10px] font-bold text-rose-300 mt-0.5';

      document.getElementById('metricNetPnL').textContent = (totalNet >= 0 ? '+₹' : '-₹') + Math.abs(totalNet).toLocaleString('en-IN', {minimumFractionDigits: 2, maximumFractionDigits: 2});
      document.getElementById('metricNetPnL').className = totalNet >= 0 ? 'text-base font-extrabold font-mono text-emerald-400 mt-1' : 'text-base font-extrabold font-mono text-rose-400 mt-1';

      document.getElementById('metricProfitFactor').textContent = profitFactor >= 99 ? '∞' : profitFactor.toFixed(2);
      document.getElementById('metricAvgR').textContent = `${avgR >= 0 ? '+' : ''}${avgR.toFixed(2)} R`;
      document.getElementById('metricExpRupee').textContent = `${expRupee >= 0 ? '+' : ''}₹${expRupee.toFixed(0)} / trade`;

      document.getElementById('metricWinRate').textContent = winRate.toFixed(1) + '%';
      document.getElementById('metricWinLossCounts').textContent = `${wins} W / ${losses} L / ${be} BE`;

      document.getElementById('metricPayoff').textContent = payoff >= 99 ? '∞' : payoff.toFixed(2);
      document.getElementById('metricAvgWinLoss').textContent = `₹${avgWin.toFixed(0)} / ₹${avgLoss.toFixed(0)}`;

      document.getElementById('metricMaxDD').textContent = maxDDAmount > 0 ? `-₹${maxDDAmount.toFixed(2)}` : '₹0.00';
      document.getElementById('metricMaxDDPct').textContent = maxDDPct > 0 ? `-${maxDDPct.toFixed(2)}% of peak` : '0.0% of peak';

      document.getElementById('metricFriction').textContent = '₹' + totalCosts.toLocaleString('en-IN', {minimumFractionDigits: 2, maximumFractionDigits: 2});
      document.getElementById('metricFrictionDrag').textContent = `${frictionDrag.toFixed(1)}% Drag`;

      document.getElementById('totalTradesBadge').textContent = `${n} Trades`;
      document.getElementById('donutWins').textContent = `${wins} Wins`;
      document.getElementById('donutLosses').textContent = `${losses} Losses`;
      document.getElementById('donutBE').textContent = `${be} BE`;

      // Long vs Short UI
      document.getElementById('longTradesCount').textContent = longCount;
      document.getElementById('longWinRate').textContent = (longCount > 0 ? ((longWins / longCount) * 100).toFixed(1) : '0.0') + '% Win Rate';
      document.getElementById('longNetPnL').textContent = (longNet >= 0 ? '+₹' : '-₹') + Math.abs(longNet).toFixed(2);
      document.getElementById('longAvgR').textContent = (longCount > 0 ? (longR / longCount).toFixed(2) : '0.00') + ' R';

      document.getElementById('shortTradesCount').textContent = shortCount;
      document.getElementById('shortWinRate').textContent = (shortCount > 0 ? ((shortWins / shortCount) * 100).toFixed(1) : '0.0') + '% Win Rate';
      document.getElementById('shortNetPnL').textContent = (shortNet >= 0 ? '+₹' : '-₹') + Math.abs(shortNet).toFixed(2);
      document.getElementById('shortAvgR').textContent = (shortCount > 0 ? (shortR / shortCount).toFixed(2) : '0.00') + ' R';

      renderCharts(filtered, wins, losses, be);
    }

    // Render Charts
    function renderCharts(filtered, wins, losses, be) {
      // 1. Account Equity Curve (Real Capital in Rupees)
      const ctxEq = document.getElementById('equityChart').getContext('2d');
      const labels = filtered.length > 0 ? ['Start', ...filtered.map(t => `${t.id} (${t.date.slice(5)})`)] : ['Start'];
      let running = startingCapital;
      const dataEq = [startingCapital];
      filtered.forEach(t => {
        running += Number(t.net_pnl);
        dataEq.push(Math.round(running * 100) / 100);
      });

      if (equityChart) equityChart.destroy();
      equityChart = new Chart(ctxEq, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: 'Account Capital (₹)',
            data: dataEq,
            borderColor: '#10B981',
            backgroundColor: 'rgba(16, 185, 129, 0.12)',
            fill: true,
            tension: 0.25,
            borderWidth: 2.5,
            pointBackgroundColor: '#10B981',
            pointRadius: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            x: { grid: { color: 'rgba(51, 65, 85, 0.4)' }, ticks: { color: '#94A3B8', font: { family: 'monospace' } } },
            y: { grid: { color: 'rgba(51, 65, 85, 0.4)' }, ticks: { color: '#94A3B8', font: { family: 'monospace' }, callback: v => '₹' + v.toLocaleString() } }
          }
        }
      });

      // 2. Win / Loss Pipe Donut Chart
      const ctxDonut = document.getElementById('outcomeDonutChart').getContext('2d');
      if (outcomeChart) outcomeChart.destroy();
      const donutData = (wins === 0 && losses === 0 && be === 0) ? [0, 0, 0] : [wins, losses, be];
      outcomeChart = new Chart(ctxDonut, {
        type: 'doughnut',
        data: {
          labels: ['Wins', 'Losses', 'Breakeven'],
          datasets: [{
            data: donutData,
            backgroundColor: ['#10B981', '#EF4444', '#F59E0B'],
            borderColor: '#0F172A',
            borderWidth: 3
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { position: 'bottom', labels: { color: '#CBD5E1', font: { family: 'monospace', size: 11 } } }
          },
          cutout: '68%'
        }
      });

      // 3. R-Multiple Bar Chart
      const ctxR = document.getElementById('rMultipleChart').getContext('2d');
      if (rChart) rChart.destroy();
      const labelsR = filtered.length > 0 ? filtered.map(t => t.id) : ['No Data'];
      const dataR = filtered.length > 0 ? filtered.map(t => Number(t.r_multiple)) : [0];
      const colorsR = filtered.length > 0 ? filtered.map(t => Number(t.r_multiple) >= 0 ? '#10B981' : '#EF4444') : ['#64748B'];

      rChart = new Chart(ctxR, {
        type: 'bar',
        data: {
          labels: labelsR,
          datasets: [{
            label: 'Realized Net R',
            data: dataR,
            backgroundColor: colorsR,
            borderRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            x: { grid: { display: false }, ticks: { color: '#94A3B8', font: { family: 'monospace' } } },
            y: { grid: { color: 'rgba(51, 65, 85, 0.4)' }, ticks: { color: '#94A3B8', font: { family: 'monospace' }, callback: v => v + 'R' } }
          }
        }
      });
    }

    // Submit New Trade
    function submitTrade(e) {
      e.preventDefault();
      const symbol = document.getElementById('inpSymbol').value.toUpperCase().trim();
      const entry = parseFloat(document.getElementById('inpEntry').value);
      const stop = parseFloat(document.getElementById('inpStop').value);
      const target = parseFloat(document.getElementById('inpTarget').value);
      const exit = parseFloat(document.getElementById('inpExit').value);
      const qty = parseInt(document.getElementById('inpQty').value);
      const time = document.getElementById('inpTime').value;
      const score = document.getElementById('inpChecklist5').checked ? 5 : 4;
      const noViolation = document.getElementById('inpNoViolation').checked;

      const riskPerShare = Math.abs(entry - stop);
      if (riskPerShare === 0) {
        alert("⚠️ Entry Price and Stop Price cannot be identical.");
        return;
      }

      const totalRisk = riskPerShare * qty;
      const maxAllowedRisk = startingCapital * 0.005; // 0.5% max risk
      if (totalRisk > maxAllowedRisk) {
        if (!confirm(`⚠️ Trade risk (₹${totalRisk.toFixed(2)}) exceeds your 0.50% capital cap (₹${maxAllowedRisk.toFixed(2)}). Do you still want to log this trade?`)) {
          return;
        }
      }

      // Target-based Planned RR
      const plannedReward = Math.abs(target - entry);
      const plannedRR = Math.round((plannedReward / riskPerShare) * 100) / 100;
      if (plannedRR < 2.2) {
        if (!confirm(`⚠️ Planned RR is ${plannedRR} RR (< 2.2 RR minimum). Rule 4 violation. Are you sure you took this trade?`)) {
          return;
        }
      }

      // FYERS Statutory Calculation
      const charges = calculateFyersCharges(entry, exit, qty, activeDirection);
      const realizedReward = activeDirection === 'Long' ? (exit - entry) : (entry - exit);
      const grossPnL = Math.round(realizedReward * qty * 100) / 100;
      const netPnL = Math.round((grossPnL - charges.totalCosts) * 100) / 100;
      const netR = totalRisk > 0 ? Math.round((netPnL / totalRisk) * 100) / 100 : 0;
      const outcome = netPnL > 0 ? 'Win' : (netPnL < 0 ? 'Loss' : 'BE');

      const newId = 'T-' + String(tradesData.length + 1).padStart(3, '0');
      const today = new Date().toISOString().split('T')[0];

      const newTrade = {
        id: newId,
        date: today,
        time: time,
        symbol: symbol,
        direction: activeDirection,
        entry_price: entry,
        stop_price: stop,
        target_price: target,
        exit_price: exit,
        qty: qty,
        rr_planned: plannedRR,
        costs: charges.totalCosts,
        net_pnl: netPnL,
        r_multiple: netR,
        outcome: outcome,
        checklist_score: score,
        rule_violation: noViolation ? 'N' : 'Y'
      };

      tradesData.push(newTrade);
      renderTradeTable();
      renderTopCapitalHeader();
      renderAnalyticsView();

      // Attempt background save to local server
      try {
        fetch('/api/trades', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(newTrade)
        }).catch(() => {});
      } catch(err) {}

      alert(`✅ Trade ${newId} logged! Net P&L: ₹${netPnL.toFixed(2)} (${netR.toFixed(2)}R) after ₹${charges.totalCosts.toFixed(2)} FYERS statutory charges.`);
    }

    function copyExcelRow() {
      if (tradesData.length === 0) {
        alert("No trades logged yet.");
        return;
      }
      const last = tradesData[tradesData.length - 1];
      const textToCopy = `${last.id}\\t${last.date}\\t${last.time}\\t${last.symbol}\\t${last.direction}\\t${last.entry_price}\\t${last.stop_price}\\t${last.target_price}\\t${last.exit_price}\\t${last.qty}`;
      navigator.clipboard.writeText(textToCopy).then(() => {
        alert("📋 Copied to clipboard! Switch to Excel 'Quick_Log' sheet and paste into the blue columns.");
      }).catch(() => {
        prompt("Copy trade row manually:", textToCopy);
      });
    }

    function clearExamples() {
      if (confirm("Clear benchmark seed examples to begin clean live logging?")) {
        tradesData = [];
        renderTradeTable();
        renderTopCapitalHeader();
        renderAnalyticsView();
      }
    }

    function reloadDefaults() {
      tradesData = [
        { id: 'T-001', date: '2026-10-20', time: '09:25', symbol: 'RELIANCE', direction: 'Long', entry_price: 2500, stop_price: 2495, target_price: 2511, exit_price: 2511, qty: 100, rr_planned: 2.20, costs: 135.10, net_pnl: 964.90, r_multiple: 1.93, outcome: 'Win', checklist_score: 5, rule_violation: 'N' },
        { id: 'T-002', date: '2026-10-20', time: '10:05', symbol: 'TCS', direction: 'Short', entry_price: 3500, stop_price: 3510, target_price: 3478, exit_price: 3510, qty: 50, rr_planned: 2.20, costs: 108.54, net_pnl: -608.54, r_multiple: -1.22, outcome: 'Loss', checklist_score: 5, rule_violation: 'N' },
        { id: 'T-003', date: '2026-10-21', time: '09:40', symbol: 'INFY', direction: 'Long', entry_price: 1450, stop_price: 1445, target_price: 1461, exit_price: 1461, qty: 100, rr_planned: 2.20, costs: 98.31, net_pnl: 1001.69, r_multiple: 2.00, outcome: 'Win', checklist_score: 5, rule_violation: 'N' }
      ];
      renderTradeTable();
      renderTopCapitalHeader();
      renderAnalyticsView();
    }

    function downloadExcelInfo() {
      alert("Master Excel Workbook is located at:\\n/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D3_Tracking_Spreadsheet.xlsx\\n\\nContains 6 tabs: Dashboard, Quick_Log, Trade_Log, Daily_Scorecard, Weekly_Review, Journal.");
    }

    function updateClock() {
      const now = new Date();
      const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
      const istTime = new Date(utc + (3600000 * 5.5));
      const hours = istTime.getHours();
      const minutes = istTime.getMinutes();
      const seconds = istTime.getSeconds();
      
      const timeStr = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')} IST`;
      document.getElementById('istClock').textContent = timeStr;

      const totalMinutes = hours * 60 + minutes;
      const isOpen = totalMinutes >= (9 * 60 + 15) && totalMinutes <= (10 * 60 + 30);
      const winElem = document.getElementById('windowStatus');
      if (isOpen) {
        winElem.textContent = 'OPEN (09:15–10:30)';
        winElem.className = 'font-bold text-emerald-400 text-xs animate-pulse';
      } else {
        winElem.textContent = 'CLOSED (09:15–10:30)';
        winElem.className = 'font-bold text-amber-400 text-xs';
      }
    }

    document.getElementById('inpTarget').addEventListener('input', function() {
      this.dataset.userEdited = "true";
    });

    window.onload = function() {
      document.getElementById('inpStartingCapital').value = startingCapital;
      renderTopCapitalHeader();
      renderTradeTable();
      renderAnalyticsView();
      calcPreview();
      setInterval(updateClock, 1000);
      updateClock();
    };
  </script>
</body>
</html>
"""

# Write to all 3 destinations
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/public/index.html", "w") as f:
    f.write(html_code)

with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html", "w") as f:
    f.write(html_code)

with open("/home/sunny/.gemini/antigravity/brain/85803015-3567-4584-af28-ca9d6eed9423/trader_dashboard.html", "w") as f:
    f.write(html_code)

print("Generated modern tabbed dashboard across web/public/index.html, deliverables/Dashboard.html, and trader_dashboard.html successfully.")
