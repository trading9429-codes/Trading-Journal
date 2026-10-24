html_content = """<!DOCTYPE html>
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
            darkbg: '#0B0F19',
            cardbg: '#111827',
            cardborder: '#1F2937'
          }
        }
      }
    }
  </script>
  <style>
    body { background-color: #080D1A; color: #E2E8F0; font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    .glass-card { background: rgba(17, 24, 39, 0.75); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.07); }
    .glass-card-hover:hover { border-color: rgba(59, 130, 246, 0.4); }
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #080D1A; }
    ::-webkit-scrollbar-thumb { background: #1F2937; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #374151; }
  </style>
</head>
<body class="min-h-screen pb-12">

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
          <p class="text-xs text-slate-400">Intraday 1-Minute Equities • FYERS Statutory Friction Calibrated • Max 2 Trades/Day</p>
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
          <span class="text-slate-400">Trading Window:</span>
          <span id="windowStatus" class="font-bold text-amber-400">09:15–10:30 AM IST</span>
        </div>
        <div class="px-3 py-1.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 flex items-center gap-2 text-emerald-300">
          <span>🛡️ Kill Switch:</span>
          <span class="font-bold">ARMED (2 Losses / 2R)</span>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Dashboard Container -->
  <div class="max-w-7xl mx-auto px-4 lg:px-8 mt-6 space-y-6">

    <!-- Date Filter & Analysis Range Controller -->
    <div class="glass-card p-3.5 rounded-2xl shadow-xl flex flex-col md:flex-row items-center justify-between gap-3 border border-slate-800">
      <div class="flex items-center gap-2 flex-wrap">
        <span class="text-xs font-bold text-slate-300 flex items-center gap-1.5 uppercase tracking-wider mr-1">
          <span>📅</span> Date Filter:
        </span>
        <!-- Preset quick buttons -->
        <button type="button" onclick="setDateFilter('all')" id="btnFilterAll" class="px-3 py-1 rounded-lg text-xs font-bold bg-blue-600 text-white transition shadow-sm shadow-blue-500/20">All Time</button>
        <button type="button" onclick="setDateFilter('today')" id="btnFilterToday" class="px-3 py-1 rounded-lg text-xs font-bold bg-slate-800 text-slate-400 hover:text-white transition">Today</button>
        <button type="button" onclick="setDateFilter('yesterday')" id="btnFilterYesterday" class="px-3 py-1 rounded-lg text-xs font-bold bg-slate-800 text-slate-400 hover:text-white transition">Yesterday</button>
        <button type="button" onclick="setDateFilter('week')" id="btnFilterWeek" class="px-3 py-1 rounded-lg text-xs font-bold bg-slate-800 text-slate-400 hover:text-white transition">This Week</button>
        <button type="button" onclick="setDateFilter('seed')" id="btnFilterSeed" class="px-3 py-1 rounded-lg text-xs font-bold bg-slate-800 text-slate-400 hover:text-white transition">Oct 20–21 (Seed)</button>
      </div>

      <!-- Custom Date Inputs -->
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

    <!-- Top KPI Widgets Grid (Dynamically updated by Date Filter) -->
    <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-3">
      
      <!-- Net Cumulative P&L -->
      <div class="glass-card glass-card-hover p-4 rounded-xl shadow-lg border-l-4 border-l-emerald-500">
        <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400 flex items-center justify-between">
          <span>Net Realized P&L</span>
          <span class="text-emerald-400">₹</span>
        </div>
        <div id="kpiNetPnL" class="text-xl font-extrabold font-mono text-emerald-400 mt-1.5">+₹1,358.05</div>
        <div class="text-[11px] text-slate-400 mt-1 flex items-center gap-1">
          <span>After FYERS friction</span>
        </div>
      </div>

      <!-- Average Realized R -->
      <div class="glass-card glass-card-hover p-4 rounded-xl shadow-lg border-l-4 border-l-cyan-500">
        <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400 flex items-center justify-between">
          <span>Avg Net R / Trade</span>
          <span class="text-cyan-400">R</span>
        </div>
        <div id="kpiAvgR" class="text-xl font-extrabold font-mono text-cyan-400 mt-1.5">+0.90 R</div>
        <div class="text-[11px] text-slate-400 mt-1">Mathematical expectancy</div>
      </div>

      <!-- Checklist Adherence % -->
      <div class="glass-card glass-card-hover p-4 rounded-xl shadow-lg border-l-4 border-l-blue-500">
        <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400 flex items-center justify-between">
          <span>5/5 Adherence</span>
          <span class="text-blue-400">🎯</span>
        </div>
        <div id="kpiAdherence" class="text-xl font-extrabold font-mono text-blue-400 mt-1.5">100.0%</div>
        <div class="text-[11px] text-slate-400 mt-1">Target: ≥ 95%</div>
      </div>

      <!-- Win Rate % -->
      <div class="glass-card glass-card-hover p-4 rounded-xl shadow-lg border-l-4 border-l-indigo-500">
        <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400 flex items-center justify-between">
          <span>Win Rate %</span>
          <span class="text-indigo-400">%</span>
        </div>
        <div id="kpiWinRate" class="text-xl font-extrabold font-mono text-indigo-400 mt-1.5">66.7%</div>
        <div id="kpiTradeCounts" class="text-[11px] text-slate-400 mt-1">2 Wins / 1 Loss</div>
      </div>

      <!-- Total Friction Paid -->
      <div class="glass-card glass-card-hover p-4 rounded-xl shadow-lg border-l-4 border-l-rose-500">
        <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400 flex items-center justify-between">
          <span>FYERS Charges</span>
          <span class="text-rose-400">₹</span>
        </div>
        <div id="kpiFriction" class="text-xl font-extrabold font-mono text-rose-400 mt-1.5">₹341.95</div>
        <div class="text-[11px] text-slate-400 mt-1">Brokerage, STT, GST, Exch</div>
      </div>

      <!-- Discipline / Rule Violations -->
      <div class="glass-card glass-card-hover p-4 rounded-xl shadow-lg border-l-4 border-l-amber-500">
        <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400 flex items-center justify-between">
          <span>Rule Violations</span>
          <span class="text-amber-400">🛡️</span>
        </div>
        <div id="kpiViolations" class="text-xl font-extrabold font-mono text-emerald-400 mt-1.5">0</div>
        <div class="text-[11px] text-slate-400 mt-1">Zero leak tolerance</div>
      </div>

    </div>

    <!-- Middle Row: 10-Second Fast Logger & Outcome Donut Chart -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

      <!-- 10-Second Anti-Procrastination Quick Logger (7 cols) -->
      <div class="lg:col-span-7 glass-card p-5 rounded-2xl shadow-xl relative overflow-hidden border border-blue-500/20">
        <div class="absolute -top-12 -right-12 w-36 h-36 bg-blue-500/10 rounded-full blur-2xl pointer-events-none"></div>

        <div class="flex items-center justify-between pb-3 border-b border-slate-800">
          <div>
            <h2 class="text-sm font-bold text-white uppercase tracking-wider flex items-center gap-2">
              <span>⚡</span> 10-Second Fast Trade Logger
            </h2>
            <p class="text-xs text-slate-400 mt-0.5">Effortless entry • Target-based Planned RR check (≥ 2.2) • FYERS exact statutory calculation</p>
          </div>
          <button type="button" onclick="downloadExcelInfo()" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 font-mono py-1 px-2.5 rounded-lg border border-slate-700 transition flex items-center gap-1.5">
            <span>📊</span> Excel File
          </button>
        </div>

        <div class="mt-3">
          <!-- Quick Stock Chips -->
          <div class="flex items-center gap-2 overflow-x-auto pb-1 text-xs">
            <span class="text-[11px] text-slate-400 font-semibold whitespace-nowrap">Quick Watchlist:</span>
            <button type="button" onclick="setSymbol('RELIANCE')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 font-mono text-slate-300">RELIANCE</button>
            <button type="button" onclick="setSymbol('TCS')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 font-mono text-slate-300">TCS</button>
            <button type="button" onclick="setSymbol('INFY')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 font-mono text-slate-300">INFY</button>
            <button type="button" onclick="setSymbol('HDFCBANK')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 font-mono text-slate-300">HDFCBANK</button>
            <button type="button" onclick="setSymbol('SBIN')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 font-mono text-slate-300">SBIN</button>
            <button type="button" onclick="setSymbol('ICICIBANK')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 font-mono text-slate-300">ICICIBANK</button>
          </div>

          <form id="tradeForm" onsubmit="submitTrade(event)" class="mt-3 space-y-3">
            <!-- Row 1: Symbol, Direction, Entry, Stop -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
              <div>
                <label class="block text-slate-400 mb-1 font-semibold">Symbol</label>
                <input type="text" id="inpSymbol" required value="SBIN" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white font-mono uppercase focus:ring-1 focus:ring-blue-500 focus:outline-none">
              </div>

              <div>
                <label class="block text-slate-400 mb-1 font-semibold">Direction</label>
                <div class="grid grid-cols-2 gap-1 bg-slate-900 p-1 rounded-lg border border-slate-700">
                  <button type="button" id="btnLong" onclick="setDirection('Long')" class="py-1 rounded font-bold text-xs bg-emerald-600 text-white transition">Long ↗</button>
                  <button type="button" id="btnShort" onclick="setDirection('Short')" class="py-1 rounded font-bold text-xs text-slate-400 hover:text-white transition">Short ↘</button>
                </div>
              </div>

              <div>
                <label class="block text-slate-400 mb-1 font-semibold">Entry Price (₹)</label>
                <input type="number" id="inpEntry" required step="0.05" value="780.00" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white font-mono focus:ring-1 focus:ring-blue-500 focus:outline-none" oninput="onEntryOrStopChange()">
              </div>

              <div>
                <label class="block text-slate-400 mb-1 font-semibold">Stop Price (₹)</label>
                <input type="number" id="inpStop" required step="0.05" value="778.00" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white font-mono focus:ring-1 focus:ring-blue-500 focus:outline-none" oninput="onEntryOrStopChange()">
              </div>
            </div>

            <!-- Row 2: Target Price, Exit Price, Quantity, Time -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
              <div>
                <label class="block text-slate-400 mb-1 font-semibold flex items-center justify-between">
                  <span>Target Price (₹)</span>
                  <span class="text-[10px] text-emerald-400 font-normal">≥ 2.2R setup</span>
                </label>
                <input type="number" id="inpTarget" required step="0.05" value="784.50" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white font-mono focus:ring-1 focus:ring-blue-500 focus:outline-none" oninput="calcPreview()">
              </div>

              <div>
                <label class="block text-slate-400 mb-1 font-semibold">Exit Price (₹)</label>
                <input type="number" id="inpExit" required step="0.05" value="784.50" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white font-mono focus:ring-1 focus:ring-blue-500 focus:outline-none" oninput="calcPreview()">
              </div>

              <div>
                <label class="block text-slate-400 mb-1 font-semibold">Quantity</label>
                <input type="number" id="inpQty" required step="1" value="250" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white font-mono focus:ring-1 focus:ring-blue-500 focus:outline-none" oninput="calcPreview()">
              </div>

              <div>
                <label class="block text-slate-400 mb-1 font-semibold">Time (09:15–10:30)</label>
                <input type="text" id="inpTime" value="09:35" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white font-mono focus:ring-1 focus:ring-blue-500 focus:outline-none">
              </div>
            </div>

            <!-- Row 3: Quality Checklist 5/5 check & No Violation -->
            <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-900/60 border border-slate-800 text-xs">
              <label class="inline-flex items-center gap-2 cursor-pointer">
                <input type="checkbox" id="inpChecklist5" checked class="w-4 h-4 rounded text-blue-600 bg-slate-900 border-slate-700 focus:ring-0">
                <span class="font-bold text-slate-200">5-Point Checklist Scored 5/5</span>
                <span class="text-[10px] text-slate-400">(Scanner + HTF + No Chase + Defined Stop + In Window)</span>
              </label>
              <label class="inline-flex items-center gap-2 cursor-pointer">
                <input type="checkbox" id="inpNoViolation" checked class="w-4 h-4 rounded text-emerald-600 bg-slate-900 border-slate-700 focus:ring-0">
                <span class="font-bold text-emerald-400">Zero Rule Violations</span>
              </label>
            </div>

            <!-- Instant Live Reactive Preview Bar -->
            <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 grid grid-cols-2 sm:grid-cols-4 gap-2 text-center font-mono text-xs shadow-inner">
              <div class="border-r border-slate-800 pr-2">
                <span class="text-slate-400 text-[10px] block uppercase font-semibold">Planned RR (|Tgt-Ent|/Risk)</span>
                <span id="prevRR" class="font-bold text-emerald-400 text-sm">2.25 RR</span>
              </div>
              <div class="border-r border-slate-800 pr-2">
                <span class="text-slate-400 text-[10px] block uppercase font-semibold">FYERS Charges</span>
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

            <!-- Live Charges Breakdown Capsule -->
            <div id="chargesBreakdownText" class="text-[11px] font-mono text-slate-400 bg-slate-900/40 px-3 py-1.5 rounded-lg border border-slate-800 text-center">
              FYERS Breakdown: Brokerage: ₹40.00 • STT: ₹49.03 • Exch: ₹11.62 • SEBI: ₹0.04 • Stamp: ₹5.85 • GST: ₹9.30
            </div>

            <!-- Action Buttons -->
            <div class="flex items-center gap-3 pt-1">
              <button type="submit" id="submitBtn" class="flex-1 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-extrabold py-3 px-4 rounded-xl shadow-lg shadow-blue-600/30 transition text-xs flex items-center justify-center gap-2">
                <span>💾</span> Log Trade & Synchronize Charts
              </button>
              <button type="button" onclick="copyExcelRow()" class="bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold py-3 px-4 rounded-xl border border-slate-700 transition text-xs flex items-center gap-1.5 whitespace-nowrap">
                <span>📋</span> Copy for Excel Quick_Log
              </button>
            </div>
          </form>
        </div>
      </div>

      <!-- Donut Chart: Win/Loss Distribution (5 cols) -->
      <div class="lg:col-span-5 glass-card p-5 rounded-2xl shadow-xl flex flex-col justify-between">
        <div class="flex items-center justify-between pb-3 border-b border-slate-800">
          <div>
            <h2 class="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
              <span>🍩</span> Win / Loss Distribution
            </h2>
            <p class="text-xs text-slate-400 mt-0.5">Calculated net of FYERS statutory charges.</p>
          </div>
          <span id="totalTradesBadge" class="text-xs font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-300">3 Trades</span>
        </div>
        <div class="mt-4 h-64 flex items-center justify-center">
          <canvas id="outcomeDonutChart"></canvas>
        </div>
        <div class="pt-3 border-t border-slate-800/80 flex items-center justify-around text-xs font-mono text-center">
          <div><span class="text-emerald-400 font-bold block text-sm" id="donutWins">2 Wins</span><span class="text-[10px] text-slate-400">Target Hit</span></div>
          <div><span class="text-rose-400 font-bold block text-sm" id="donutLosses">1 Loss</span><span class="text-[10px] text-slate-400">Stop Respected</span></div>
          <div><span class="text-amber-400 font-bold block text-sm" id="donutBE">0 BE</span><span class="text-[10px] text-slate-400">Breakeven</span></div>
        </div>
      </div>
    </div>

    <!-- Visual Graphs Row: Equity Curve & R-Multiple Bar Chart -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
      
      <!-- Equity Curve Line Chart (7 cols) -->
      <div class="lg:col-span-7 glass-card p-5 rounded-2xl shadow-xl">
        <div class="flex items-center justify-between pb-3 border-b border-slate-800">
          <div>
            <h2 class="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
              <span>📈</span> Cumulative Net Capital Curve (₹)
            </h2>
            <p class="text-xs text-slate-400 mt-0.5">True net equity growth after deducting FYERS brokerage, STT, and taxes.</p>
          </div>
          <span id="equityFilterLabel" class="text-xs font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">ALL TIME</span>
        </div>
        <div class="mt-4 h-64">
          <canvas id="equityChart"></canvas>
        </div>
      </div>

      <!-- R-Multiple Distribution Bar Chart (5 cols) -->
      <div class="lg:col-span-5 glass-card p-5 rounded-2xl shadow-xl flex flex-col justify-between">
        <div class="flex items-center justify-between pb-3 border-b border-slate-800">
          <div>
            <h2 class="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
              <span>📊</span> Realized Net R-Multiple Expectancy
            </h2>
            <p class="text-xs text-slate-400 mt-0.5">Target: Green bars ≥ +1.8R, Loss bars kept at -1.0R to -1.25R.</p>
          </div>
          <span class="text-xs font-mono text-cyan-400 font-bold">Expectancy</span>
        </div>
        <div class="mt-4 h-64">
          <canvas id="rMultipleChart"></canvas>
        </div>
      </div>
    </div>

    <!-- Live Trade History Table -->
    <div class="glass-card rounded-2xl p-5 shadow-xl">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-800">
        <div>
          <h2 class="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
            <span>📋</span> Synchronized Trade History Log
          </h2>
          <p class="text-xs text-slate-400 mt-0.5">Filtered dynamically by selected date range • Matches Excel `Trade_Log` & `Quick_Log` tabs.</p>
        </div>
        <div class="flex items-center gap-2">
          <button type="button" onclick="clearExamples()" class="px-3 py-1.5 rounded-lg bg-rose-500/10 hover:bg-rose-500/20 text-rose-400 border border-rose-500/30 text-xs font-bold transition">
            🗑️ Clear Examples
          </button>
          <button type="button" onclick="reloadDefaults()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold transition">
            🔄 Reload Seed Data
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
            <!-- Dynamically populated based on date filter -->
          </tbody>
        </table>
      </div>
    </div>

  </div>

  <script>
    let activeDirection = 'Long';
    let currentFilterMode = 'all'; // 'all', 'today', 'yesterday', 'week', 'seed', 'custom'
    let filterFrom = null;
    let filterTo = null;

    // Verified seed trades with exact FYERS charges and Planned RR >= 2.2
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

    // Filter helper: returns trades within active date filter
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

    // Set filter presets
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
        // Current week Monday to Sunday
        const d = new Date(today);
        const day = d.getDay();
        const diff = d.getDate() - day + (day === 0 ? -6 : 1); // Monday
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
      renderDashboard();
    }

    function onCustomDateChange() {
      currentFilterMode = 'custom';
      filterFrom = document.getElementById('filterFromDate').value || null;
      filterTo = document.getElementById('filterToDate').value || null;
      updateFilterButtonsUI();
      renderDashboard();
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

    // FYERS Equity Intraday Statutory & Brokerage Calculator
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
        btnL.className = 'py-1 rounded font-bold text-xs bg-emerald-600 text-white transition';
        btnS.className = 'py-1 rounded font-bold text-xs text-slate-400 hover:text-white transition';
      } else {
        btnS.className = 'py-1 rounded font-bold text-xs bg-rose-600 text-white transition';
        btnL.className = 'py-1 rounded font-bold text-xs text-slate-400 hover:text-white transition';
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
      
      // Auto-suggest a 2.2R target if valid entry & stop
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

        // Planned RR calculation: |Target - Entry| / |Entry - Stop|
        const plannedRewardPerShare = target > 0 ? Math.abs(target - entry) : Math.abs(exit - entry);
        const plannedRR = riskPerShare > 0 ? (plannedRewardPerShare / riskPerShare) : 0;

        // FYERS Exact Statutory Calculation
        const charges = calculateFyersCharges(entry, exit > 0 ? exit : entry, qty, activeDirection);

        // Realized Gross P&L
        const realizedRewardPerShare = activeDirection === 'Long' ? (exit - entry) : (entry - exit);
        const grossPnL = realizedRewardPerShare * qty;
        const netPnL = grossPnL - charges.totalCosts;
        const netR = totalRisk > 0 ? (netPnL / totalRisk) : 0;

        // Update Planned RR Preview
        const rrElem = document.getElementById('prevRR');
        const isRRValid = plannedRR >= 2.2;
        rrElem.textContent = plannedRR.toFixed(2) + ' RR' + (isRRValid ? ' ✓' : ' ⚠ <2.2');
        rrElem.className = isRRValid ? 'font-bold text-emerald-400 text-sm' : 'font-bold text-rose-400 text-sm animate-pulse';

        // Update Friction Preview
        document.getElementById('prevFriction').textContent = '₹' + charges.totalCosts.toFixed(2);

        // Detailed charges text
        document.getElementById('chargesBreakdownText').textContent = 
          `FYERS Breakdown: Brokerage: ₹${charges.brokerage.toFixed(2)} • STT: ₹${charges.stt.toFixed(2)} • Exch: ₹${charges.exchangeCharges.toFixed(2)} • SEBI: ₹${charges.sebiFee.toFixed(2)} • Stamp: ₹${charges.stampDuty.toFixed(2)} • GST: ₹${charges.gst.toFixed(2)}`;

        // Update Net P&L Preview
        const netElem = document.getElementById('prevNetPnL');
        netElem.textContent = (netPnL >= 0 ? '+₹' : '-₹') + Math.abs(netPnL).toFixed(2);
        netElem.className = netPnL >= 0 ? 'font-bold text-emerald-400 text-sm' : 'font-bold text-rose-400 text-sm';

        // Update Realized Net R Preview
        const rElem = document.getElementById('prevNetR');
        rElem.textContent = (netR >= 0 ? '+' : '') + netR.toFixed(2) + ' R';
        rElem.className = netR >= 0 ? 'font-bold text-cyan-400 text-sm' : 'font-bold text-rose-400 text-sm';
      }
    }

    function renderDashboard() {
      const filteredTrades = getFilteredTrades();
      const countFiltered = filteredTrades.length;
      const countTotal = tradesData.length;

      // Update badge
      const badge = document.getElementById('filterActiveBadge');
      badge.textContent = `Showing ${countFiltered} of ${countTotal} Trades`;
      if (countFiltered < countTotal) {
        badge.className = 'text-[11px] font-bold px-2.5 py-1 rounded-lg bg-amber-500/10 text-amber-400 border border-amber-500/30 whitespace-nowrap';
      } else {
        badge.className = 'text-[11px] font-bold px-2.5 py-1 rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 whitespace-nowrap';
      }

      let totalNet = 0;
      let totalR = 0;
      let wins = 0;
      let losses = 0;
      let be = 0;
      let totalFriction = 0;
      let score5 = 0;
      let violations = 0;

      filteredTrades.forEach(t => {
        totalNet += Number(t.net_pnl);
        totalR += Number(t.r_multiple);
        totalFriction += Number(t.costs);
        if (t.outcome === 'Win') wins++;
        else if (t.outcome === 'Loss') losses++;
        else be++;

        if (t.checklist_score >= 5) score5++;
        if (t.rule_violation === 'Y') violations++;
      });

      const avgR = countFiltered > 0 ? (totalR / countFiltered) : 0;
      const winRate = countFiltered > 0 ? ((wins / countFiltered) * 100) : 0;
      const adherence = countFiltered > 0 ? ((score5 / countFiltered) * 100) : 100.0;

      document.getElementById('kpiNetPnL').textContent = (totalNet >= 0 ? '+₹' : '-₹') + Math.abs(totalNet).toLocaleString('en-IN', {minimumFractionDigits: 2, maximumFractionDigits: 2});
      document.getElementById('kpiAvgR').textContent = (avgR >= 0 ? '+' : '') + avgR.toFixed(2) + ' R';
      document.getElementById('kpiAdherence').textContent = adherence.toFixed(1) + '%';
      document.getElementById('kpiWinRate').textContent = winRate.toFixed(1) + '%';
      document.getElementById('kpiTradeCounts').textContent = `${wins} Wins / ${losses} Losses`;
      document.getElementById('kpiFriction').textContent = '₹' + totalFriction.toLocaleString('en-IN', {minimumFractionDigits: 2, maximumFractionDigits: 2});
      document.getElementById('kpiViolations').textContent = violations;
      document.getElementById('totalTradesBadge').textContent = `${countFiltered} Trades`;

      document.getElementById('donutWins').textContent = `${wins} Wins`;
      document.getElementById('donutLosses').textContent = `${losses} Losses`;
      document.getElementById('donutBE').textContent = `${be} BE`;

      // Render Table with Filtered Trades
      const tbody = document.getElementById('tradeTableBody');
      tbody.innerHTML = '';
      if (countFiltered === 0) {
        tbody.innerHTML = `<tr><td colspan="14" class="p-8 text-center text-slate-500 italic">No trades found within the selected date range (${filterFrom || 'Start'} to ${filterTo || 'End'}). Click 'All Time' or reset the filter above to view all records.</td></tr>`;
      } else {
        filteredTrades.slice().reverse().forEach(t => {
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

      renderCharts(filteredTrades, wins, losses, be);
    }

    function renderCharts(filteredTrades, wins, losses, be) {
      // 1. Cumulative Equity Curve
      const ctxEq = document.getElementById('equityChart').getContext('2d');
      const labels = filteredTrades.length > 0 ? ['Start', ...filteredTrades.map(t => `${t.id} (${t.date.slice(5)})`)] : ['No Trades in Range'];
      let cum = 0;
      const dataEq = [0];
      filteredTrades.forEach(t => {
        cum += Number(t.net_pnl);
        dataEq.push(Math.round(cum * 100) / 100);
      });

      if (equityChart) equityChart.destroy();
      equityChart = new Chart(ctxEq, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: 'Net Capital (₹)',
            data: dataEq,
            borderColor: '#10B981',
            backgroundColor: 'rgba(16, 185, 129, 0.12)',
            fill: true,
            tension: 0.3,
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
            y: { grid: { color: 'rgba(51, 65, 85, 0.4)' }, ticks: { color: '#94A3B8', font: { family: 'monospace' }, callback: v => '₹' + v } }
          }
        }
      });

      // 2. Win / Loss Donut Chart (Pipe chart)
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
      const labelsR = filteredTrades.length > 0 ? filteredTrades.map(t => t.id) : ['No Data'];
      const dataR = filteredTrades.length > 0 ? filteredTrades.map(t => Number(t.r_multiple)) : [0];
      const colorsR = filteredTrades.length > 0 ? filteredTrades.map(t => Number(t.r_multiple) >= 0 ? '#10B981' : '#EF4444') : ['#64748B'];

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

      // Target-based Planned RR
      const plannedReward = Math.abs(target - entry);
      const plannedRR = Math.round((plannedReward / riskPerShare) * 100) / 100;
      if (plannedRR < 2.2) {
        if (!confirm(`⚠️ Planned RR is ${plannedRR} RR, which is below the required minimum of 2.2 RR (Rule 4 violation). Are you sure you took this trade?`)) {
          return;
        }
      }

      // FYERS Statutory Calculation
      const charges = calculateFyersCharges(entry, exit, qty, activeDirection);
      const realizedReward = activeDirection === 'Long' ? (exit - entry) : (entry - exit);
      const grossPnL = Math.round(realizedReward * qty * 100) / 100;
      const netPnL = Math.round((grossPnL - charges.totalCosts) * 100) / 100;
      const totalRisk = riskPerShare * qty;
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
      renderDashboard();

      // Trigger server save if available
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
      // Format matches Quick_Log columns: Trade_ID, Date, Time, Symbol, Direction, Entry, Stop, Target, Exit, Qty
      const textToCopy = `${last.id}\\t${last.date}\\t${last.time}\\t${last.symbol}\\t${last.direction}\\t${last.entry_price}\\t${last.stop_price}\\t${last.target_price}\\t${last.exit_price}\\t${last.qty}`;
      navigator.clipboard.writeText(textToCopy).then(() => {
        alert("📋 Copied to clipboard! Switch to Excel 'Quick_Log' sheet and paste into the blue columns.");
      }).catch(() => {
        prompt("Copy trade row manually:", textToCopy);
      });
    }

    function clearExamples() {
      if (confirm("Clear seed examples to begin clean live session logging?")) {
        tradesData = [];
        renderDashboard();
      }
    }

    function reloadDefaults() {
      tradesData = [
        { id: 'T-001', date: '2026-10-20', time: '09:25', symbol: 'RELIANCE', direction: 'Long', entry_price: 2500, stop_price: 2495, target_price: 2511, exit_price: 2511, qty: 100, rr_planned: 2.20, costs: 135.10, net_pnl: 964.90, r_multiple: 1.93, outcome: 'Win', checklist_score: 5, rule_violation: 'N' },
        { id: 'T-002', date: '2026-10-20', time: '10:05', symbol: 'TCS', direction: 'Short', entry_price: 3500, stop_price: 3510, target_price: 3478, exit_price: 3510, qty: 50, rr_planned: 2.20, costs: 108.54, net_pnl: -608.54, r_multiple: -1.22, outcome: 'Loss', checklist_score: 5, rule_violation: 'N' },
        { id: 'T-003', date: '2026-10-21', time: '09:40', symbol: 'INFY', direction: 'Long', entry_price: 1450, stop_price: 1445, target_price: 1461, exit_price: 1461, qty: 100, rr_planned: 2.20, costs: 98.31, net_pnl: 1001.69, r_multiple: 2.00, outcome: 'Win', checklist_score: 5, rule_violation: 'N' }
      ];
      renderDashboard();
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

    // Set flag when user manually changes target
    document.getElementById('inpTarget').addEventListener('input', function() {
      this.dataset.userEdited = "true";
    });

    window.onload = function() {
      renderDashboard();
      calcPreview();
      setInterval(updateClock, 1000);
      updateClock();
    };
  </script>
</body>
</html>
"""

# Write to web/public/index.html
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/public/index.html", "w") as f:
    f.write(html_content)

# Write to deliverables/Dashboard.html
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html", "w") as f:
    f.write(html_content)

# Write to artifact trader_dashboard.html
with open("/home/sunny/.gemini/antigravity/brain/85803015-3567-4584-af28-ca9d6eed9423/trader_dashboard.html", "w") as f:
    f.write(html_content)

print("Updated public/index.html, deliverables/Dashboard.html, and trader_dashboard.html with date filter successfully.")
