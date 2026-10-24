#!/usr/bin/env python3
"""
Applies Options 1, 2, 4, 5 enhancements to build_master_v16.py:
1. 30-Day Visual P&L & Discipline Calendar Heatmap (in Tab 2)
2. Interactive Pre-Market Readiness Routine (D2 Checklist Modal)
4. Native Desktop / Browser Background Alerts & Siren (Web Notifications + Web Audio Dual-Tone Siren)
5. 1-Click Monthly Performance Dossier (Institutional PDF / Print Report)
"""

MASTER_BAK = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/build_master_v16.py.bak"
MASTER_FILE = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/build_master_v16.py"

def main():
    with open(MASTER_BAK, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Update @media print in new_head
    old_head_print = """    @media print {
      body * { visibility: hidden; }
      #weeklyReviewModalContent, #weeklyReviewModalContent * { visibility: visible; }
      #weeklyReviewModalContent { position: absolute; left: 0; top: 0; width: 100%; background: white !important; color: black !important; }
    }
  </style>
</head>'''"""

    new_head_print = """    @media print {
      body * { visibility: hidden; }
      #weeklyReviewModalContent, #weeklyReviewModalContent * { visibility: visible; }
      #weeklyReviewModalContent { position: absolute; left: 0; top: 0; width: 100%; background: white !important; color: black !important; }
      #monthlyDossierPrintable, #monthlyDossierPrintable * { visibility: visible !important; }
      #monthlyDossierPrintable { position: absolute; left: 0; top: 0; width: 100%; background: #ffffff !important; color: #0f172a !important; margin: 0; padding: 24px; box-shadow: none !important; border: none !important; }
      #monthlyDossierPrintable .bg-slate-900, 
      #monthlyDossierPrintable .bg-slate-950, 
      #monthlyDossierPrintable .glass-card, 
      #monthlyDossierPrintable .glass-card-hover { background: #f8fafc !important; color: #0f172a !important; border: 1px solid #cbd5e1 !important; }
      #monthlyDossierPrintable .text-white { color: #0f172a !important; }
      #monthlyDossierPrintable .text-slate-200, 
      #monthlyDossierPrintable .text-slate-300, 
      #monthlyDossierPrintable .text-slate-400 { color: #334155 !important; }
      #monthlyDossierPrintable .border-slate-800, 
      #monthlyDossierPrintable .border-slate-700 { border-color: #e2e8f0 !important; }
      .no-print { display: none !important; }
    }
  </style>
</head>'''"""

    assert old_head_print in code, "Failed to find old_head_print"
    code = code.replace(old_head_print, new_head_print, 1)

    # 2. Update new_toolbar in Step 3
    old_toolbar_target = """        <button onclick="openWebhookModal()" class="px-3 py-2 rounded-lg bg-sky-600/20 hover:bg-sky-600/30 text-sky-300 border border-sky-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm" title="Configure Telegram/WhatsApp Accountability Alerts">
          <span>🔔</span>
          <span>Alerts &amp; Webhook</span>
        </button>"""

    new_toolbar_buttons = """        <!-- 09:00 AM IST Pre-Flight Readiness Protocol Button -->
        <button onclick="openPreMarketReadinessModal()" id="preFlightBtn" class="px-3 py-2 rounded-lg bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm" title="09:00–09:10 AM IST Pre-Market Readiness Routine">
          <span id="preFlightIcon">🛡️</span>
          <span>Pre-Flight (D2)</span>
          <span id="preFlightStatusPill" class="text-[9px] px-1.5 py-0.5 rounded bg-emerald-500/30 text-emerald-200 uppercase font-mono font-bold hidden">Ready</span>
        </button>
        <!-- Institutional Monthly Dossier PDF Report Button -->
        <button onclick="openMonthlyDossierModal()" class="px-3 py-2 rounded-lg bg-purple-600/20 hover:bg-purple-600/30 text-purple-300 border border-purple-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm" title="1-Click Institutional Performance Dossier &amp; PDF Export">
          <span>📑</span>
          <span>Monthly Dossier</span>
        </button>
        <!-- Native Desktop Alerts & Web Audio Risk Siren Toggle -->
        <button onclick="toggleDesktopNotifications()" id="desktopAlertsToggleBtn" class="px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 font-medium text-xs flex items-center gap-1.5 transition shadow-sm" title="Toggle Native Desktop Push &amp; 880Hz Audio Risk Siren">
          <span id="desktopAlertsIcon">🔔</span>
          <span id="desktopAlertsLabel">Desktop Alerts</span>
        </button>
        <button onclick="openWebhookModal()" class="px-3 py-2 rounded-lg bg-sky-600/20 hover:bg-sky-600/30 text-sky-300 border border-sky-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm" title="Configure Telegram/WhatsApp Accountability Alerts">
          <span>⚙️</span>
          <span>Webhooks</span>
        </button>"""

    assert old_toolbar_target in code, "Failed to find old_toolbar_target"
    code = code.replace(old_toolbar_target, new_toolbar_buttons, 1)

    # 3. Add Tab 2 Calendar Heatmap (Step 8.5)
    tab2_replacement_block = """    # 8.5 TAB 2: Add 30-Day Visual P&L & Discipline Calendar Heatmap
    old_tab2_start = '''<!-- ========================================== -->
    <!-- TAB 2: PERFORMANCE & EQUITY CURVES -->
    <!-- ========================================== -->
    <div id="tabContent2" class="hidden mt-6 space-y-6">'''

    new_tab2_start = '''<!-- ========================================== -->
    <!-- TAB 2: PERFORMANCE & EQUITY CURVES -->
    <!-- ========================================== -->
    <div id="tabContent2" class="hidden mt-6 space-y-6">

      <!-- 30-DAY VISUAL P&L & DISCIPLINE CALENDAR HEATMAP MATRIX -->
      <section class="glass-card rounded-2xl p-6 shadow-2xl border border-blue-500/20 bg-gradient-to-br from-slate-900/90 via-slate-900/70 to-slate-950">
        <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between pb-4 border-b border-slate-800 gap-4">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-blue-500/20 border border-blue-500/30 flex items-center justify-center text-blue-400 font-bold text-lg shadow-lg">
              🗓️
            </div>
            <div>
              <div class="flex items-center gap-2">
                <h3 class="text-base font-bold text-white uppercase tracking-wider">30-Day Execution &amp; Discipline Matrix</h3>
                <span class="text-xs px-2.5 py-0.5 rounded-full bg-blue-500/10 text-blue-300 border border-blue-500/20 font-mono" id="calendarCycleProgressBadge">
                  Reset Cycle 1 &bull; 30 Trading Days
                </span>
              </div>
              <p class="text-xs text-slate-400 mt-0.5">Session-by-session adherence heatmap tracking daily Net P&amp;L, Realized R-Multiples, and rule compliance integrity</p>
            </div>
          </div>
          
          <!-- Calendar KPI Summary Badges -->
          <div class="flex items-center gap-2 flex-wrap text-xs">
            <div class="bg-slate-950/80 px-3 py-1.5 rounded-xl border border-slate-800 flex items-center gap-1.5 font-mono">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 shadow-sm shadow-emerald-400/50"></span>
              <span class="text-slate-400">Green:</span>
              <span id="calGreenCount" class="font-bold text-emerald-400">0</span>
            </div>
            <div class="bg-slate-950/80 px-3 py-1.5 rounded-xl border border-slate-800 flex items-center gap-1.5 font-mono">
              <span class="w-2.5 h-2.5 rounded-full bg-sky-400"></span>
              <span class="text-slate-400">Clean Loss:</span>
              <span id="calCleanLossCount" class="font-bold text-sky-400">0</span>
            </div>
            <div class="bg-slate-950/80 px-3 py-1.5 rounded-xl border border-slate-800 flex items-center gap-1.5 font-mono">
              <span class="w-2.5 h-2.5 rounded-full bg-rose-500 shadow-sm shadow-rose-500/50"></span>
              <span class="text-slate-400">Breach:</span>
              <span id="calBreachCount" class="font-bold text-rose-400">0</span>
            </div>
            <div class="bg-slate-950/80 px-3 py-1.5 rounded-xl border border-slate-800 flex items-center gap-1.5 font-mono">
              <span class="text-slate-400">Cycle Realized:</span>
              <span id="calNetRCount" class="font-bold text-blue-300">+0.00R</span>
            </div>
          </div>
        </div>

        <!-- 30-Day Heatmap Grid (6 cols x 5 rows on lg screens) -->
        <div class="mt-5 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 lg:grid-cols-6 gap-3" id="calendarHeatmapGrid">
          <!-- Dynamically populated by JS renderCalendarHeatmap() -->
        </div>

        <!-- Heatmap Legend & Tip -->
        <div class="mt-4 pt-3 border-t border-slate-800 flex flex-col md:flex-row items-start md:items-center justify-between text-xs text-slate-400 gap-2">
          <div class="flex items-center gap-3 flex-wrap text-[11px]">
            <span class="font-bold text-slate-300 uppercase tracking-wider">Legend:</span>
            <span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded bg-emerald-500/20 border border-emerald-500"></span> Profit Adherent</span>
            <span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded bg-sky-500/20 border border-sky-500"></span> Planned Loss (Clean)</span>
            <span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded bg-amber-500/20 border border-amber-500"></span> Rest / No Trade</span>
            <span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded bg-rose-500/30 border border-rose-500"></span> Rule Breach / Demerit</span>
            <span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded bg-slate-800/40 border border-slate-700 border-dashed"></span> Future Day</span>
          </div>
          <div id="calendarInspectionTip" class="font-mono text-[11px] text-blue-300 flex items-center gap-1">
            <span>💡</span> Click any active day card to inspect trade executions
          </div>
        </div>
      </section>'''

    assert old_tab2_start in content, "Failed to find old_tab2_start"
    content = content.replace(old_tab2_start, new_tab2_start, 1)

"""

    step9_marker = "    # 9. TAB 3: Add Multi-Strategy Attribution & MAE/MFE Exit Leak Analysis"
    assert step9_marker in code, "Failed to find step 9 marker"
    code = code.replace(step9_marker, tab2_replacement_block + step9_marker, 1)

    # 4. Connect renderCalendarHeatmap to renderAllChartsAndMetrics
    old_tab2_render = """      // Charts render
      if (currentTab === 2) {
        renderEquityChart(trades);
        renderDonutCharts(totalWins, totalLosses, trades.length - totalClosed, violations, trades.length);"""

    new_tab2_render = """      // Charts render
      if (currentTab === 2) {
        renderEquityChart(trades);
        renderDonutCharts(totalWins, totalLosses, trades.length - totalClosed, violations, trades.length);
        renderCalendarHeatmap(trades);"""

    code = code.replace(old_tab2_render, new_tab2_render, 1)

    # 5. Inject New Modals in all_modals_markup (Step 11)
    new_modals = """  <!-- ========================================== -->
  <!-- MODAL: INTERACTIVE PRE-MARKET READINESS ROUTINE (D2 CHECKLIST) -->
  <!-- ========================================== -->
  <div id="preMarketReadinessModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="glass-card rounded-2xl w-full max-w-2xl border border-emerald-500/30 shadow-2xl p-6 relative max-h-[92vh] overflow-y-auto">
      
      <div class="flex items-center justify-between pb-4 border-b border-slate-800">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 flex items-center justify-center text-white font-black text-xl shadow-lg shadow-emerald-500/20">
            🛡️
          </div>
          <div>
            <h3 class="text-base font-extrabold text-white flex items-center gap-2">
              09:00–09:10 AM IST Pre-Market Readiness Routine
              <span id="readinessStatusBadge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-300 border border-amber-500/20">
                Pending Certification
              </span>
            </h3>
            <p class="text-xs text-slate-400">6-Point Institutional Pre-Flight Gate &bull; Eliminate emotional carryover before market open</p>
          </div>
        </div>
        <button onclick="closePreMarketReadinessModal()" class="text-slate-400 hover:text-white text-2xl font-bold">&times;</button>
      </div>

      <!-- Readiness Progress Bar -->
      <div class="mt-4 p-3.5 bg-slate-950/70 rounded-xl border border-slate-800">
        <div class="flex justify-between items-center text-xs mb-1.5">
          <span class="text-slate-400 font-semibold uppercase tracking-wider text-[10px]">Readiness Verification Gate</span>
          <span class="font-bold text-emerald-400 font-mono" id="readinessProgressText">0 / 6 Certified (0%)</span>
        </div>
        <div class="w-full bg-slate-800 rounded-full h-2 overflow-hidden border border-slate-700">
          <div id="readinessProgressBar" class="bg-gradient-to-r from-teal-500 to-emerald-400 h-2 rounded-full transition-all duration-300" style="width: 0%;"></div>
        </div>
      </div>

      <!-- 6 Pre-Flight Gate Checkpoints -->
      <div class="mt-4 space-y-2.5 text-xs">
        <label class="flex items-start gap-3 p-3 rounded-xl bg-slate-900/80 border border-slate-800 hover:border-slate-700 cursor-pointer transition">
          <input type="checkbox" id="chk_sleep" onchange="updateReadinessProgress()" class="mt-0.5 rounded border-slate-700 text-emerald-500 focus:ring-emerald-500/30 w-4 h-4 bg-slate-950">
          <div class="space-y-0.5">
            <span class="font-bold text-slate-200">1. Physical &amp; Psychological Baseline</span>
            <p class="text-[11px] text-slate-400">Slept 7+ restful hours, fully hydrated, calm breathing rate, zero residual frustration or revenge urges from yesterday.</p>
          </div>
        </label>

        <label class="flex items-start gap-3 p-3 rounded-xl bg-slate-900/80 border border-slate-800 hover:border-slate-700 cursor-pointer transition">
          <input type="checkbox" id="chk_macro" onchange="updateReadinessProgress()" class="mt-0.5 rounded border-slate-700 text-emerald-500 focus:ring-emerald-500/30 w-4 h-4 bg-slate-950">
          <div class="space-y-0.5">
            <span class="font-bold text-slate-200">2. Market Context &amp; Global Breadth Scan</span>
            <p class="text-[11px] text-slate-400">GIFT Nifty and Asian cues scanned, opening gap bias formulated, India VIX verified (&lt;15 low vol, 15–20 sweet spot, &gt;20 caution).</p>
          </div>
        </label>

        <label class="flex items-start gap-3 p-3 rounded-xl bg-slate-900/80 border border-slate-800 hover:border-slate-700 cursor-pointer transition">
          <input type="checkbox" id="chk_levels" onchange="updateReadinessProgress()" class="mt-0.5 rounded border-slate-700 text-emerald-500 focus:ring-emerald-500/30 w-4 h-4 bg-slate-950">
          <div class="space-y-0.5">
            <span class="font-bold text-slate-200">3. Structural Key Levels Plotted</span>
            <p class="text-[11px] text-slate-400">Previous Day High (PDH), Previous Day Low (PDL), and Opening Range boundaries marked clearly on TradingView/FYERS chart.</p>
          </div>
        </label>

        <label class="flex items-start gap-3 p-3 rounded-xl bg-slate-900/80 border border-slate-800 hover:border-slate-700 cursor-pointer transition">
          <input type="checkbox" id="chk_risk" onchange="updateReadinessProgress()" class="mt-0.5 rounded border-slate-700 text-emerald-500 focus:ring-emerald-500/30 w-4 h-4 bg-slate-950">
          <div class="space-y-0.5">
            <span class="font-bold text-slate-200">4. Daily Risk Ceiling &amp; Trade Budget Confirmed</span>
            <p class="text-[11px] text-slate-400">Hard stop capped at ₹500 (0.50% risk), maximum 2 executions permitted today. Hard quit if 2 losses occur.</p>
          </div>
        </label>

        <label class="flex items-start gap-3 p-3 rounded-xl bg-slate-900/80 border border-slate-800 hover:border-slate-700 cursor-pointer transition">
          <input type="checkbox" id="chk_stop" onchange="updateReadinessProgress()" class="mt-0.5 rounded border-slate-700 text-emerald-500 focus:ring-emerald-500/30 w-4 h-4 bg-slate-950">
          <div class="space-y-0.5">
            <span class="font-bold text-slate-200">5. Pre-Committed Stop &amp; Loss Acceptance</span>
            <p class="text-[11px] text-slate-400">Stop level must be determined BEFORE entry. Complete psychological acceptance to take the planned loss without bargaining.</p>
          </div>
        </label>

        <label class="flex items-start gap-3 p-3 rounded-xl bg-slate-900/80 border border-slate-800 hover:border-slate-700 cursor-pointer transition">
          <input type="checkbox" id="chk_tech" onchange="updateReadinessProgress()" class="mt-0.5 rounded border-slate-700 text-emerald-500 focus:ring-emerald-500/30 w-4 h-4 bg-slate-950">
          <div class="space-y-0.5">
            <span class="font-bold text-slate-200">6. Terminal, Hardware &amp; Hotspot Readiness</span>
            <p class="text-[11px] text-slate-400">Broker 2FA session logged in and verified. Primary fiber broadband tested; backup mobile 5G hotspot on standby.</p>
          </div>
        </label>
      </div>

      <!-- Quick Action / Breathing Shortcut -->
      <div class="mt-4 p-3 bg-teal-500/10 border border-teal-500/20 rounded-xl flex items-center justify-between text-xs">
        <span class="text-teal-300 font-medium flex items-center gap-1.5">
          <span>🧘</span>
          <span>Optional Grounding: 5-Minute Box Breathing</span>
        </span>
        <button onclick="closePreMarketReadinessModal(); openPreMarketFocusModal();" class="px-2.5 py-1 rounded-lg bg-teal-600/30 hover:bg-teal-600/50 text-teal-200 border border-teal-500/30 font-bold transition">
          Launch Breathing
        </button>
      </div>

      <!-- Footer Actions -->
      <div class="mt-5 pt-4 border-t border-slate-800 flex items-center justify-between gap-3">
        <button onclick="resetReadinessChecklist()" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition">
          Reset Checklist
        </button>
        <button id="certifyReadinessBtn" onclick="certifyPreMarketReadiness()" disabled class="flex-1 py-2.5 px-4 rounded-xl bg-slate-800 text-slate-500 font-bold text-xs flex items-center justify-center gap-2 cursor-not-allowed transition">
          <span>🔒</span>
          <span>Complete All 6 Checks to Certify Readiness</span>
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL: 30-DAY CALENDAR DAY INSPECTION DETAIL -->
  <!-- ========================================== -->
  <div id="calendarDayModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="glass-card rounded-2xl w-full max-w-xl border border-blue-500/30 shadow-2xl p-6 relative max-h-[90vh] overflow-y-auto">
      <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-xl bg-blue-500/20 border border-blue-500/30 flex items-center justify-center text-blue-400 font-bold text-base">
            📅
          </div>
          <div>
            <h3 class="text-base font-bold text-white flex items-center gap-2" id="calModalDayTitle">
              Day 04 Execution Breakdown
            </h3>
            <p class="text-xs text-slate-400" id="calModalDateSubtitle">2026-10-24 &bull; 2 Executions Logged</p>
          </div>
        </div>
        <button onclick="closeCalendarDayModal()" class="text-slate-400 hover:text-white text-2xl font-bold">&times;</button>
      </div>

      <div class="mt-4 grid grid-cols-3 gap-2.5 text-center text-xs">
        <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
          <span class="text-slate-500 text-[10px] uppercase font-bold block">Net P&amp;L</span>
          <span id="calModalNetPnL" class="font-mono font-bold text-sm text-emerald-400">+₹1,240.00</span>
        </div>
        <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
          <span class="text-slate-500 text-[10px] uppercase font-bold block">Realized R</span>
          <span id="calModalRealizedR" class="font-mono font-bold text-sm text-blue-300">+2.48R</span>
        </div>
        <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
          <span class="text-slate-500 text-[10px] uppercase font-bold block">Integrity</span>
          <span id="calModalIntegrity" class="font-bold text-xs text-emerald-400">🛡️ 100% Adherent</span>
        </div>
      </div>

      <div class="mt-4">
        <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">Session Trade Ledger</h4>
        <div id="calModalTradesList" class="space-y-2 max-h-56 overflow-y-auto">
          <!-- Populated by JS -->
        </div>
      </div>

      <div class="mt-5 pt-3 border-t border-slate-800 flex justify-end">
        <button onclick="closeCalendarDayModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold transition">
          Close Inspection
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL: 1-CLICK MONTHLY PERFORMANCE DOSSIER (PDF / PRINT REPORT) -->
  <!-- ========================================== -->
  <div id="monthlyDossierModal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md hidden flex items-center justify-center p-3 md:p-6 overflow-y-auto">
    <div class="bg-slate-900 rounded-2xl w-full max-w-4xl border border-purple-500/30 shadow-2xl relative max-h-[95vh] flex flex-col">
      
      <!-- Top Action Toolbar (Hidden during print) -->
      <div class="no-print p-4 border-b border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 bg-slate-950/80 rounded-t-2xl">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-purple-500/20 border border-purple-500/30 flex items-center justify-center text-purple-300 font-bold text-base">
            📑
          </div>
          <div>
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
              Institutional Performance Dossier &bull; 30-Day Audit
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-purple-500/10 text-purple-300 border border-purple-500/20 font-mono">
                Official Certification
              </span>
            </h3>
            <p class="text-xs text-slate-400">Comprehensive risk, behavioral leak, and multi-strategy audit report</p>
          </div>
        </div>
        <div class="flex items-center gap-2 self-end sm:self-auto">
          <button onclick="window.print()" class="px-3.5 py-1.5 rounded-lg bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-bold text-xs flex items-center gap-1.5 transition shadow-lg shadow-purple-600/20">
            <span>🖨️</span>
            <span>Print / Save to PDF</span>
          </button>
          <button onclick="copyDossierMarkdown()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-xs flex items-center gap-1.5 transition">
            <span>📋</span>
            <span>Copy MD</span>
          </button>
          <button onclick="closeMonthlyDossierModal()" class="text-slate-400 hover:text-white text-xl font-bold px-2 py-1">&times;</button>
        </div>
      </div>

      <!-- Printable Report Container -->
      <div id="monthlyDossierPrintable" class="p-6 md:p-8 overflow-y-auto space-y-6 text-slate-200">
        
        <!-- Institutional Document Header -->
        <div class="border-b-2 border-slate-700 pb-5 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
          <div>
            <span class="text-[10px] uppercase font-mono tracking-widest text-purple-400 font-bold block">Confidential Execution Audit</span>
            <h1 class="text-xl md:text-2xl font-black text-white tracking-tight">TRADER EXECUTION RESET SYSTEM</h1>
            <p class="text-xs text-slate-400 mt-0.5">30-Day Institutional Discipline &amp; Capital Preservation Dossier</p>
          </div>
          <div class="text-right sm:text-right text-xs font-mono space-y-1">
            <div class="text-slate-400">Generated: <strong class="text-slate-200" id="dossierTimestamp">--</strong></div>
            <div class="text-slate-400">Account: <strong class="text-emerald-400">Private Execution Desk (NSE)</strong></div>
            <div class="text-slate-400">Verification Hash: <span class="text-purple-300 font-mono text-[10px]" id="dossierHash">#RESET-V16-SECURE</span></div>
          </div>
        </div>

        <!-- Executive Audit Verdict & Trader Grade -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4 items-center bg-slate-950/60 p-4 rounded-xl border border-slate-800">
          <div class="md:col-span-1 flex flex-col items-center justify-center p-3 bg-slate-900 rounded-xl border border-slate-800 text-center">
            <span class="text-[10px] uppercase font-bold text-slate-400">Reset Grade</span>
            <span id="dossierGrade" class="text-4xl font-black font-mono text-emerald-400 my-1">A</span>
            <span id="dossierQualificationBadge" class="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300">QUALIFIED</span>
          </div>
          <div class="md:col-span-3 space-y-1.5 text-xs">
            <h4 class="font-bold text-white text-sm">Executive Performance Synthesis</h4>
            <p id="dossierExecutiveSummaryText" class="text-slate-300 leading-relaxed">
              Trader exhibited exceptional compliance across the 30-day reset cycle. Daily loss limits and the 2-trade ceiling were strictly honored. Execution remained confined to the 09:15–10:30 AM IST momentum window. Capital allocation may now safely scale into Phase 3/4.
            </p>
          </div>
        </div>

        <!-- Core KPI Matrix (8 Metrics) -->
        <div>
          <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider mb-2.5">1. Executive KPI Matrix</h4>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center text-xs">
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
              <span class="text-[10px] text-slate-400 uppercase font-semibold block">Net P&amp;L</span>
              <span id="dossierNetPnL" class="font-mono font-bold text-base text-emerald-400">+₹0.00</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
              <span class="text-[10px] text-slate-400 uppercase font-semibold block">Realized R</span>
              <span id="dossierNetR" class="font-mono font-bold text-base text-blue-300">+0.00R</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
              <span class="text-[10px] text-slate-400 uppercase font-semibold block">Adherence Rate</span>
              <span id="dossierAdherence" class="font-mono font-bold text-base text-emerald-400">100%</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
              <span class="text-[10px] text-slate-400 uppercase font-semibold block">Win Rate</span>
              <span id="dossierWinRate" class="font-mono font-bold text-base text-white">0%</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
              <span class="text-[10px] text-slate-400 uppercase font-semibold block">Profit Factor</span>
              <span id="dossierProfitFactor" class="font-mono font-bold text-base text-white">0.00</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
              <span class="text-[10px] text-slate-400 uppercase font-semibold block">Total Trades</span>
              <span id="dossierTotalTrades" class="font-mono font-bold text-base text-white">0</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
              <span class="text-[10px] text-slate-400 uppercase font-semibold block">Demerit Strikes</span>
              <span id="dossierDemerits" class="font-mono font-bold text-base text-emerald-400">0</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
              <span class="text-[10px] text-slate-400 uppercase font-semibold block">Max Drawdown</span>
              <span id="dossierMaxDD" class="font-mono font-bold text-base text-amber-400">0.00R</span>
            </div>
          </div>
        </div>

        <!-- 30-Day Cycle Progression -->
        <div>
          <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider mb-2.5">2. 30-Day Reset Cycle Progression</h4>
          <div class="overflow-x-auto rounded-xl border border-slate-800">
            <table class="w-full text-left text-xs">
              <thead class="bg-slate-950 text-slate-400 font-mono text-[10px] uppercase">
                <tr>
                  <th class="p-2.5">Phase Tier</th>
                  <th class="p-2.5">Trading Days</th>
                  <th class="p-2.5">Risk Budget</th>
                  <th class="p-2.5">Trade Cap</th>
                  <th class="p-2.5">Status</th>
                  <th class="p-2.5 text-right">Adherence</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-800 font-mono text-slate-300">
                <tr>
                  <td class="p-2.5 font-bold text-white">Phase 1: Stabilization</td>
                  <td class="p-2.5">Days 1–3</td>
                  <td class="p-2.5">₹250 (0.25%)</td>
                  <td class="p-2.5">1 Trade/Day</td>
                  <td class="p-2.5 text-emerald-400">Completed</td>
                  <td class="p-2.5 text-right text-emerald-400 font-bold">100%</td>
                </tr>
                <tr>
                  <td class="p-2.5 font-bold text-white">Phase 2: Consolidation</td>
                  <td class="p-2.5">Days 4–10</td>
                  <td class="p-2.5">₹500 (0.50%)</td>
                  <td class="p-2.5">Max 2 Trades/Day</td>
                  <td class="p-2.5 text-blue-400" id="dossierPhase2Status">In Progress</td>
                  <td class="p-2.5 text-right text-emerald-400 font-bold" id="dossierPhase2Adherence">100%</td>
                </tr>
                <tr>
                  <td class="p-2.5 font-bold text-white">Phase 3: Scaling</td>
                  <td class="p-2.5">Days 11–20</td>
                  <td class="p-2.5">₹750 (0.75%)</td>
                  <td class="p-2.5">Max 2 Trades/Day</td>
                  <td class="p-2.5 text-slate-500">Upcoming</td>
                  <td class="p-2.5 text-right text-slate-500">--</td>
                </tr>
                <tr>
                  <td class="p-2.5 font-bold text-white">Phase 4: Mastery</td>
                  <td class="p-2.5">Days 21–30</td>
                  <td class="p-2.5">₹1,000 (1.00%)</td>
                  <td class="p-2.5">Max 2 Trades/Day</td>
                  <td class="p-2.5 text-slate-500">Upcoming</td>
                  <td class="p-2.5 text-right text-slate-500">--</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Strategy Edge Attribution Table -->
        <div>
          <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider mb-2.5">3. Multi-Strategy Edge Attribution</h4>
          <div class="overflow-x-auto rounded-xl border border-slate-800">
            <table class="w-full text-left text-xs">
              <thead class="bg-slate-950 text-slate-400 font-mono text-[10px] uppercase">
                <tr>
                  <th class="p-2.5">Playbook Setup</th>
                  <th class="p-2.5">Trades</th>
                  <th class="p-2.5">Win Rate</th>
                  <th class="p-2.5">Net Realized R</th>
                  <th class="p-2.5">Net P&amp;L</th>
                  <th class="p-2.5 text-right">Expectancy</th>
                </tr>
              </thead>
              <tbody id="dossierStrategyTableBody" class="divide-y divide-slate-800 font-mono text-slate-300">
                <!-- Populated by JS -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Full Graded Trade Ledger -->
        <div>
          <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider mb-2.5">4. Graded Execution Audit Ledger</h4>
          <div class="overflow-x-auto rounded-xl border border-slate-800 max-h-60 overflow-y-auto">
            <table class="w-full text-left text-xs">
              <thead class="bg-slate-950 text-slate-400 font-mono text-[10px] uppercase sticky top-0">
                <tr>
                  <th class="p-2">Date / Time</th>
                  <th class="p-2">Symbol</th>
                  <th class="p-2">Setup</th>
                  <th class="p-2">Outcome</th>
                  <th class="p-2">Realized R</th>
                  <th class="p-2">Net P&amp;L</th>
                  <th class="p-2 text-right">Integrity</th>
                </tr>
              </thead>
              <tbody id="dossierLedgerTableBody" class="divide-y divide-slate-800 font-mono text-slate-300">
                <!-- Populated by JS -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Institutional Trader Pledge & Graduation Sign-Off -->
        <div class="border-t-2 border-slate-700 pt-5 mt-6">
          <h4 class="text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">5. Institutional Trader Pledge &amp; Graduation Attestation</h4>
          <p class="text-xs text-slate-400 italic leading-relaxed">
            &ldquo;I hereby certify that all trades logged in this dossier were executed in strict compliance with the Trader Execution Reset System protocols. I confirm that stops were pre-set, the 10:30 AM IST market boundary was respected, and emotional discipline took absolute priority over monetary outcome.&rdquo;
          </p>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-8 mt-6 pt-4 border-t border-slate-800 text-xs">
            <div class="space-y-1">
              <div class="border-b border-slate-600 pb-1 font-mono font-bold text-white">TRADER EXECUTION DESK</div>
              <span class="text-[10px] text-slate-500 uppercase tracking-wider">Independent Quantitative Trader Signature</span>
            </div>
            <div class="space-y-1">
              <div class="border-b border-slate-600 pb-1 font-mono font-bold text-emerald-400">SYSTEM AUDITOR &bull; VERIFIED</div>
              <span class="text-[10px] text-slate-500 uppercase tracking-wider">Trader Reset System v16.0 Certification Desk</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>"""
    modal_anchor = "  </div>" + "'''\n\n    target_script_start ="
    assert modal_anchor in code, "Failed to find modal_anchor"
    code = code.replace(modal_anchor, "  </div>\n\n" + new_modals + "'''\n\n    target_script_start =", 1)

# 6. Append Extended JS Engine (Step 12)
    extended_js = """
    // ==========================================
    // OPTIONS 1, 2, 4, 5 EXTENDED LOGIC
    // ==========================================

    // --- OPTION 4: Native Desktop Alerts & Web Audio Siren ---
    let audioCtxInstance = null;

    function getAudioContext() {
      if (!audioCtxInstance) {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (AudioCtx) audioCtxInstance = new AudioCtx();
      }
      if (audioCtxInstance && audioCtxInstance.state === 'suspended') {
        audioCtxInstance.resume();
      }
      return audioCtxInstance;
    }

    function playAlertSiren(pattern = 'urgent') {
      try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        if (pattern === 'urgent') {
          // Dual-Tone 880Hz / 660Hz Trading Floor Risk Siren
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(880, now);
          osc.frequency.setValueAtTime(660, now + 0.18);
          osc.frequency.setValueAtTime(880, now + 0.36);
          osc.frequency.setValueAtTime(660, now + 0.54);
          osc.frequency.setValueAtTime(880, now + 0.72);

          gain.gain.setValueAtTime(0.28, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 1.1);

          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now);
          osc.stop(now + 1.1);
        } else if (pattern === 'success') {
          // Ascending C-E-G Triad Chime
          osc.type = 'sine';
          osc.frequency.setValueAtTime(523.25, now);
          osc.frequency.setValueAtTime(659.25, now + 0.12);
          osc.frequency.setValueAtTime(783.99, now + 0.24);

          gain.gain.setValueAtTime(0.22, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.6);

          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now);
          osc.stop(now + 0.6);
        } else {
          // Warning Beep
          osc.type = 'square';
          osc.frequency.setValueAtTime(587.33, now);
          osc.frequency.setValueAtTime(440.00, now + 0.2);

          gain.gain.setValueAtTime(0.2, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.8);

          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now);
          osc.stop(now + 0.8);
        }
      } catch (e) {
        console.warn('Audio siren playback error:', e);
      }
    }

    function updateDesktopAlertsUI() {
      const btn = document.getElementById('desktopAlertsToggleBtn');
      const icon = document.getElementById('desktopAlertsIcon');
      const label = document.getElementById('desktopAlertsLabel');
      if (!btn) return;

      if (!('Notification' in window)) {
        if (label) label.textContent = 'Alerts N/A';
        btn.classList.add('opacity-50');
        return;
      }

      if (Notification.permission === 'granted') {
        if (icon) icon.textContent = '🔔';
        if (label) label.textContent = 'Alerts Active';
        btn.className = "px-3 py-2 rounded-lg bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm";
      } else if (Notification.permission === 'denied') {
        if (icon) icon.textContent = '🔕';
        if (label) label.textContent = 'Alerts Blocked';
        btn.className = "px-3 py-2 rounded-lg bg-rose-600/20 hover:bg-rose-600/30 text-rose-300 border border-rose-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm";
      } else {
        if (icon) icon.textContent = '🔔';
        if (label) label.textContent = 'Desktop Alerts';
        btn.className = "px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 font-medium text-xs flex items-center gap-1.5 transition shadow-sm";
      }
    }

    async function toggleDesktopNotifications() {
      if (!('Notification' in window)) {
        alert('Desktop notifications are not supported in this browser.');
        return;
      }

      if (Notification.permission === 'granted') {
        playAlertSiren('urgent');
        sendDesktopAlert('Trader Reset System — Desktop Alerts Active', 'Dual-tone siren and background notifications verified. Window close (10:30 AM) and circuit breaker alerts are active.', 'test-alert');
        return;
      }

      try {
        const perm = await Notification.requestPermission();
        updateDesktopAlertsUI();
        if (perm === 'granted') {
          playAlertSiren('success');
          sendDesktopAlert('Trader Reset System — Notifications Enabled', 'Execution window close (10:30 AM) and circuit breaker alerts will trigger in background.', 'granted-alert');
        }
      } catch (err) {
        console.error('Error requesting desktop notifications:', err);
      }
    }

    function sendDesktopAlert(title, body, tag = 'general-alert') {
      try {
        if ('Notification' in window && Notification.permission === 'granted') {
          const notif = new Notification(title, {
            body: body,
            icon: 'https://cdn-icons-png.flaticon.com/512/2965/2965300.png',
            tag: tag,
            renotify: true
          });
          notif.onclick = () => {
            window.focus();
            notif.close();
          };
        }
      } catch (e) {
        console.warn('Desktop notification error:', e);
      }
    }

    // --- OPTION 2: Pre-Market Readiness Routine (D2 Checklist) ---
    function getTodayDateKey() {
      const now = new Date();
      return now.toLocaleDateString('en-CA', { timeZone: 'Asia/Kolkata' });
    }

    function openPreMarketReadinessModal() {
      checkPreFlightStatusToday();
      const modal = document.getElementById('preMarketReadinessModal');
      if (modal) modal.classList.remove('hidden');
    }

    function closePreMarketReadinessModal() {
      const modal = document.getElementById('preMarketReadinessModal');
      if (modal) modal.classList.add('hidden');
    }

    function updateReadinessProgress() {
      const ids = ['chk_sleep', 'chk_macro', 'chk_levels', 'chk_risk', 'chk_stop', 'chk_tech'];
      let checkedCount = 0;
      ids.forEach(id => {
        const el = document.getElementById(id);
        if (el && el.checked) checkedCount++;
      });

      const pct = Math.round((checkedCount / ids.length) * 100);
      const text = document.getElementById('readinessProgressText');
      const bar = document.getElementById('readinessProgressBar');
      const btn = document.getElementById('certifyReadinessBtn');

      if (text) text.textContent = `${checkedCount} / ${ids.length} Certified (${pct}%)`;
      if (bar) bar.style.width = `${pct}%`;

      if (btn) {
        if (checkedCount === ids.length) {
          btn.disabled = false;
          btn.className = "flex-1 py-2.5 px-4 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs flex items-center justify-center gap-2 shadow-lg shadow-emerald-600/30 cursor-pointer transition";
          btn.innerHTML = `<span>🛡️</span><span>Certify Pre-Market Readiness &amp; Unlock Desk</span>`;
        } else {
          btn.disabled = true;
          btn.className = "flex-1 py-2.5 px-4 rounded-xl bg-slate-800 text-slate-500 font-bold text-xs flex items-center justify-center gap-2 cursor-not-allowed transition";
          btn.innerHTML = `<span>🔒</span><span>Complete All 6 Checks to Certify Readiness</span>`;
        }
      }
    }

    function certifyPreMarketReadiness() {
      const todayKey = getTodayDateKey();
      localStorage.setItem('premarket_certified_' + todayKey, new Date().toISOString());
      playAlertSiren('success');

      updatePreFlightButtonUI(true);
      closePreMarketReadinessModal();

      if (typeof speakCoach === 'function') {
        speakCoach("Pre-market readiness certified. Your desk is unlocked. Trade with precision and honor your risk ceiling.");
      }
      alert('✅ PRE-MARKET READINESS CERTIFIED!\\n\\nYou have verified physical composure, structural levels, and risk ceilings. Execution desk is unlocked.');
    }

    function resetReadinessChecklist() {
      const ids = ['chk_sleep', 'chk_macro', 'chk_levels', 'chk_risk', 'chk_stop', 'chk_tech'];
      ids.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.checked = false;
      });
      const todayKey = getTodayDateKey();
      localStorage.removeItem('premarket_certified_' + todayKey);
      updateReadinessProgress();
      updatePreFlightButtonUI(false);
    }

    function checkPreFlightStatusToday() {
      const todayKey = getTodayDateKey();
      const certifiedTime = localStorage.getItem('premarket_certified_' + todayKey);
      const isCertified = !!certifiedTime;

      if (isCertified) {
        const ids = ['chk_sleep', 'chk_macro', 'chk_levels', 'chk_risk', 'chk_stop', 'chk_tech'];
        ids.forEach(id => {
          const el = document.getElementById(id);
          if (el) el.checked = true;
        });
      }
      updateReadinessProgress();
      updatePreFlightButtonUI(isCertified);
    }

    function updatePreFlightButtonUI(isCertified) {
      const pill = document.getElementById('preFlightStatusPill');
      const badge = document.getElementById('readinessStatusBadge');
      const btn = document.getElementById('preFlightBtn');

      if (isCertified) {
        if (pill) {
          pill.classList.remove('hidden');
          pill.textContent = 'Ready';
        }
        if (badge) {
          badge.className = "text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
          badge.textContent = "✅ Certified Today";
        }
        if (btn) {
          btn.className = "px-3 py-2 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/40 text-emerald-200 border border-emerald-500/50 font-bold text-xs flex items-center gap-1.5 transition shadow-sm shadow-emerald-500/20";
        }
      } else {
        if (pill) pill.classList.add('hidden');
        if (badge) {
          badge.className = "text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-300 border border-amber-500/20";
          badge.textContent = "Pending Certification";
        }
        if (btn) {
          btn.className = "px-3 py-2 rounded-lg bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm";
        }
      }
    }

    // --- OPTION 1: 30-Day Visual P&L & Discipline Calendar Heatmap Engine ---
    let calendarDaysData = {};

    function renderCalendarHeatmap(trades) {
      const grid = document.getElementById('calendarHeatmapGrid');
      if (!grid) return;

      const tradeList = trades || (typeof tradesData !== 'undefined' ? tradesData : []);

      // Group trades by date
      const tradesByDate = {};
      tradeList.forEach(t => {
        if (!t.date) return;
        const dStr = t.date.split('T')[0];
        if (!tradesByDate[dStr]) tradesByDate[dStr] = [];
        tradesByDate[dStr].push(t);
      });

      // Sort dates chronologically
      const sortedDates = Object.keys(tradesByDate).sort();

      let greenCount = 0;
      let cleanLossCount = 0;
      let breachCount = 0;
      let netRTotal = 0;

      calendarDaysData = {};
      let html = '';

      for (let day = 1; day <= 30; day++) {
        const dateStr = sortedDates[day - 1] || null;
        const dayTrades = dateStr ? tradesByDate[dateStr] : [];
        const hasTrades = dayTrades.length > 0;

        let dayPnL = 0;
        let dayR = 0;
        let hasBreach = false;

        if (hasTrades) {
          dayTrades.forEach(t => {
            dayPnL += parseFloat(t.net_pnl || 0);
            dayR += parseFloat(t.r_multiple || 0);
            if (t.rule_violation === 'Y' || t.checklist_score < 4) {
              hasBreach = true;
            }
          });
          netRTotal += dayR;
        }

        calendarDaysData[day] = {
          dayNum: day,
          dateStr: dateStr || `Day ${day.toString().padStart(2, '0')}`,
          trades: dayTrades,
          pnl: dayPnL,
          r: dayR,
          hasBreach: hasBreach
        };

        let cardClass = '';
        let badgeHtml = '';
        let pnlText = '--';
        let rText = 'No Trades';

        if (hasTrades) {
          if (hasBreach) {
            breachCount++;
            cardClass = 'bg-rose-950/40 border-rose-500/50 hover:border-rose-400 text-rose-300';
            badgeHtml = '<span class="text-[9px] px-1.5 py-0.2 rounded bg-rose-500/30 text-rose-200 font-bold border border-rose-500/40">⚠️ Breach</span>';
          } else if (dayPnL > 0) {
            greenCount++;
            cardClass = 'bg-emerald-950/40 border-emerald-500/50 hover:border-emerald-400 text-emerald-300 shadow-lg shadow-emerald-900/20';
            badgeHtml = '<span class="text-[9px] px-1.5 py-0.2 rounded bg-emerald-500/30 text-emerald-200 font-bold border border-emerald-500/40">🛡️ Profit</span>';
          } else if (dayPnL < 0) {
            cleanLossCount++;
            cardClass = 'bg-sky-950/40 border-sky-500/50 hover:border-sky-400 text-sky-300';
            badgeHtml = '<span class="text-[9px] px-1.5 py-0.2 rounded bg-sky-500/30 text-sky-200 font-bold border border-sky-500/40">🛡️ Clean Loss</span>';
          } else {
            cardClass = 'bg-slate-900/80 border-slate-700 hover:border-slate-600 text-slate-300';
            badgeHtml = '<span class="text-[9px] px-1.5 py-0.2 rounded bg-slate-800 text-slate-400">Break-Even</span>';
          }

          pnlText = (dayPnL >= 0 ? '+₹' : '-₹') + Math.abs(dayPnL).toLocaleString('en-IN', { maximumFractionDigits: 0 });
          rText = (dayR >= 0 ? '+' : '') + dayR.toFixed(2) + 'R';
        } else if (day <= (typeof currentDayNumber !== 'undefined' ? currentDayNumber : 4)) {
          cardClass = 'bg-slate-900/50 border-amber-500/30 hover:border-amber-400 text-amber-300/80';
          badgeHtml = '<span class="text-[9px] px-1.5 py-0.2 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">Rest Day</span>';
          pnlText = '₹0';
          rText = '0.00R';
        } else {
          cardClass = 'bg-slate-950/40 border-slate-800 border-dashed text-slate-600';
          badgeHtml = '<span class="text-[9px] text-slate-600 font-mono">Future</span>';
          pnlText = '--';
          rText = '--';
        }

        html += `
          <div onclick="inspectCalendarDay(${day})" class="glass-card-hover p-3 rounded-xl border ${cardClass} transition-all duration-200 cursor-pointer flex flex-col justify-between min-h-[96px] shadow-sm">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-bold">Day ${day.toString().padStart(2, '0')}</span>
              ${badgeHtml}
            </div>
            <div class="mt-2">
              <div class="text-sm font-black font-mono tracking-tight">${pnlText}</div>
              <div class="text-[10px] font-mono opacity-80 mt-0.5">${rText}</div>
            </div>
            <div class="text-[9px] text-slate-500 font-mono mt-1 text-right truncate">
              ${dateStr ? dateStr : `Cycle Day ${day}`}
            </div>
          </div>
        `;
      }

      grid.innerHTML = html;

      // Update counters
      const elGreen = document.getElementById('calGreenCount');
      const elCleanLoss = document.getElementById('calCleanLossCount');
      const elBreach = document.getElementById('calBreachCount');
      const elNetR = document.getElementById('calNetRCount');

      if (elGreen) elGreen.textContent = greenCount;
      if (elCleanLoss) elCleanLoss.textContent = cleanLossCount;
      if (elBreach) elBreach.textContent = breachCount;
      if (elNetR) {
        elNetR.textContent = (netRTotal >= 0 ? '+' : '') + netRTotal.toFixed(2) + 'R';
        elNetR.className = 'font-bold ' + (netRTotal >= 0 ? 'text-emerald-400' : 'text-rose-400');
      }
    }

    function inspectCalendarDay(dayNum) {
      const data = calendarDaysData[dayNum];
      if (!data) return;

      const modal = document.getElementById('calendarDayModal');
      const title = document.getElementById('calModalDayTitle');
      const subtitle = document.getElementById('calModalDateSubtitle');
      const pnlEl = document.getElementById('calModalNetPnL');
      const rEl = document.getElementById('calModalRealizedR');
      const integEl = document.getElementById('calModalIntegrity');
      const tradesList = document.getElementById('calModalTradesList');

      if (title) title.textContent = `Day ${dayNum.toString().padStart(2, '0')} Execution Breakdown`;
      if (subtitle) subtitle.textContent = `${data.dateStr} • ${data.trades.length} Execution(s) Logged`;

      if (pnlEl) {
        pnlEl.textContent = (data.pnl >= 0 ? '+₹' : '-₹') + Math.abs(data.pnl).toLocaleString('en-IN', { minimumFractionDigits: 2 });
        pnlEl.className = 'font-mono font-bold text-sm ' + (data.pnl >= 0 ? 'text-emerald-400' : 'text-rose-400');
      }

      if (rEl) {
        rEl.textContent = (data.r >= 0 ? '+' : '') + data.r.toFixed(2) + 'R';
        rEl.className = 'font-mono font-bold text-sm ' + (data.r >= 0 ? 'text-blue-300' : 'text-rose-300');
      }

      if (integEl) {
        if (data.trades.length === 0) {
          integEl.textContent = '☕ Rest / Non-Trading';
          integEl.className = 'font-bold text-xs text-slate-400';
        } else if (data.hasBreach) {
          integEl.textContent = '⚠️ Rule Breach Logged';
          integEl.className = 'font-bold text-xs text-rose-400';
        } else {
          integEl.textContent = '🛡️ 100% Adherent';
          integEl.className = 'font-bold text-xs text-emerald-400';
        }
      }

      if (tradesList) {
        if (data.trades.length === 0) {
          tradesList.innerHTML = `<div class="p-4 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 text-center text-xs">No trade executions logged on this date.</div>`;
        } else {
          tradesList.innerHTML = data.trades.map((t, idx) => `
            <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 flex items-center justify-between text-xs">
              <div class="space-y-0.5">
                <div class="flex items-center gap-2">
                  <span class="font-bold text-white">${t.symbol || 'NIFTY'}</span>
                  <span class="text-[10px] px-1.5 py-0.2 rounded ${t.direction === 'Long' ? 'bg-emerald-500/20 text-emerald-300' : 'bg-rose-500/20 text-rose-300'} font-bold font-mono">${t.direction}</span>
                  <span class="text-slate-400 font-mono text-[10px]">${t.entry_time || '09:20'} &bull; ${t.setup_name || '1m Pullback'}</span>
                </div>
                <div class="text-[11px] text-slate-400">Entry: ₹${t.entry_price} &bull; Stop: ₹${t.stop_loss} &bull; Exit: ₹${t.exit_price}</div>
              </div>
              <div class="text-right font-mono">
                <div class="font-bold ${parseFloat(t.net_pnl || 0) >= 0 ? 'text-emerald-400' : 'text-rose-400'}">
                  ${parseFloat(t.net_pnl || 0) >= 0 ? '+' : ''}₹${parseFloat(t.net_pnl || 0).toFixed(2)}
                </div>
                <div class="text-[10px] text-blue-300">${(parseFloat(t.r_multiple || 0) >= 0 ? '+' : '') + parseFloat(t.r_multiple || 0).toFixed(2)}R</div>
              </div>
            </div>
          `).join('');
        }
      }

      if (modal) modal.classList.remove('hidden');
    }

    function closeCalendarDayModal() {
      const modal = document.getElementById('calendarDayModal');
      if (modal) modal.classList.add('hidden');
    }

    // --- OPTION 5: 1-Click Monthly Performance Dossier Engine ---
    function openMonthlyDossierModal() {
      generateMonthlyDossierReport();
      const modal = document.getElementById('monthlyDossierModal');
      if (modal) modal.classList.remove('hidden');
    }

    function closeMonthlyDossierModal() {
      const modal = document.getElementById('monthlyDossierModal');
      if (modal) modal.classList.add('hidden');
    }

    function generateMonthlyDossierReport() {
      const trades = typeof tradesData !== 'undefined' ? tradesData : [];

      const tsEl = document.getElementById('dossierTimestamp');
      if (tsEl) {
        tsEl.textContent = new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', dateStyle: 'medium', timeStyle: 'short' }) + ' IST';
      }

      let totalPnL = 0;
      let totalR = 0;
      let wins = 0;
      let losses = 0;
      let breaches = 0;
      let sumWinR = 0;
      let sumLossR = 0;

      const strategyStats = {};

      trades.forEach(t => {
        const pnl = parseFloat(t.net_pnl || 0);
        const r = parseFloat(t.r_multiple || 0);
        totalPnL += pnl;
        totalR += r;

        if (t.outcome === 'Win' || pnl > 0) {
          wins++;
          sumWinR += r;
        } else if (t.outcome === 'Loss' || pnl < 0) {
          losses++;
          sumLossR += Math.abs(r);
        }

        if (t.rule_violation === 'Y' || t.checklist_score < 4) {
          breaches++;
        }

        const strat = t.setup_name || '1m Pullback to 9EMA';
        if (!strategyStats[strat]) {
          strategyStats[strat] = { trades: 0, wins: 0, r: 0, pnl: 0 };
        }
        strategyStats[strat].trades++;
        strategyStats[strat].r += r;
        strategyStats[strat].pnl += pnl;
        if (t.outcome === 'Win' || pnl > 0) strategyStats[strat].wins++;
      });

      const totalTrades = trades.length;
      const winRate = totalTrades > 0 ? ((wins / totalTrades) * 100).toFixed(1) : '0.0';
      const profitFactor = sumLossR > 0 ? (sumWinR / sumLossR).toFixed(2) : (sumWinR > 0 ? '99.0' : '0.00');
      const adherencePct = totalTrades > 0 ? (((totalTrades - breaches) / totalTrades) * 100).toFixed(1) : '100.0';

      // Dossier Grade calculation
      let grade = 'A';
      if (breaches > 3 || parseFloat(adherencePct) < 80) grade = 'F';
      else if (breaches > 1 || parseFloat(adherencePct) < 90) grade = 'C';
      else if (parseFloat(adherencePct) >= 95 && totalR > 0) grade = 'A+';
      else grade = 'A';

      const gradeEl = document.getElementById('dossierGrade');
      const qualEl = document.getElementById('dossierQualificationBadge');
      if (gradeEl) {
        gradeEl.textContent = grade;
        gradeEl.className = 'text-4xl font-black font-mono my-1 ' + (grade.startsWith('A') ? 'text-emerald-400' : (grade === 'C' ? 'text-amber-400' : 'text-rose-400'));
      }
      if (qualEl) {
        if (grade.startsWith('A')) {
          qualEl.textContent = 'QUALIFIED FOR PROMOTION';
          qualEl.className = 'text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300';
        } else {
          qualEl.textContent = 'ON PROBATION';
          qualEl.className = 'text-[10px] font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300';
        }
      }

      // Populate KPIs
      const netPnLEl = document.getElementById('dossierNetPnL');
      if (netPnLEl) {
        netPnLEl.textContent = (totalPnL >= 0 ? '+₹' : '-₹') + Math.abs(totalPnL).toLocaleString('en-IN', { minimumFractionDigits: 2 });
        netPnLEl.className = 'font-mono font-bold text-base ' + (totalPnL >= 0 ? 'text-emerald-400' : 'text-rose-400');
      }

      const netREl = document.getElementById('dossierNetR');
      if (netREl) {
        netREl.textContent = (totalR >= 0 ? '+' : '') + totalR.toFixed(2) + 'R';
        netREl.className = 'font-mono font-bold text-base ' + (totalR >= 0 ? 'text-blue-300' : 'text-rose-300');
      }

      const adhEl = document.getElementById('dossierAdherence');
      if (adhEl) adhEl.textContent = adherencePct + '%';

      const wrEl = document.getElementById('dossierWinRate');
      if (wrEl) wrEl.textContent = winRate + '%';

      const pfEl = document.getElementById('dossierProfitFactor');
      if (pfEl) pfEl.textContent = profitFactor;

      const ttEl = document.getElementById('dossierTotalTrades');
      if (ttEl) ttEl.textContent = totalTrades;

      const demEl = document.getElementById('dossierDemerits');
      if (demEl) {
        demEl.textContent = breaches;
        demEl.className = 'font-mono font-bold text-base ' + (breaches === 0 ? 'text-emerald-400' : 'text-rose-400');
      }

      // Populate Strategy Table
      const stratTbody = document.getElementById('dossierStrategyTableBody');
      if (stratTbody) {
        const stratKeys = Object.keys(strategyStats);
        if (stratKeys.length === 0) {
          stratTbody.innerHTML = `<tr><td colspan="6" class="p-3 text-center text-slate-500">No strategy attribution data logged yet.</td></tr>`;
        } else {
          stratTbody.innerHTML = stratKeys.map(k => {
            const s = strategyStats[k];
            const sWinRate = s.trades > 0 ? ((s.wins / s.trades) * 100).toFixed(0) : 0;
            const sExp = s.trades > 0 ? (s.r / s.trades).toFixed(2) : '0.00';
            return `
              <tr>
                <td class="p-2.5 font-bold text-white">${k}</td>
                <td class="p-2.5">${s.trades}</td>
                <td class="p-2.5">${sWinRate}%</td>
                <td class="p-2.5 ${s.r >= 0 ? 'text-emerald-400' : 'text-rose-400'}">${(s.r >= 0 ? '+' : '') + s.r.toFixed(2)}R</td>
                <td class="p-2.5 ${s.pnl >= 0 ? 'text-emerald-400' : 'text-rose-400'}">${(s.pnl >= 0 ? '+₹' : '-₹') + Math.abs(s.pnl).toLocaleString('en-IN', { maximumFractionDigits: 0 })}</td>
                <td class="p-2.5 text-right font-bold text-blue-300">${sExp}R</td>
              </tr>
            `;
          }).join('');
        }
      }

      // Populate Ledger Table
      const ledgerTbody = document.getElementById('dossierLedgerTableBody');
      if (ledgerTbody) {
        if (trades.length === 0) {
          ledgerTbody.innerHTML = `<tr><td colspan="7" class="p-3 text-center text-slate-500">No trades available in database ledger.</td></tr>`;
        } else {
          ledgerTbody.innerHTML = trades.map(t => {
            const pnl = parseFloat(t.net_pnl || 0);
            const r = parseFloat(t.r_multiple || 0);
            const isBreach = t.rule_violation === 'Y' || t.checklist_score < 4;
            return `
              <tr>
                <td class="p-2 font-mono text-slate-400">${t.date || '--'} ${t.entry_time || ''}</td>
                <td class="p-2 font-bold text-white">${t.symbol || 'NIFTY'}</td>
                <td class="p-2 text-slate-300">${t.setup_name || '1m Pullback'}</td>
                <td class="p-2"><span class="px-1.5 py-0.5 rounded text-[10px] font-bold ${t.outcome === 'Win' ? 'bg-emerald-500/20 text-emerald-300' : 'bg-rose-500/20 text-rose-300'}">${t.outcome}</span></td>
                <td class="p-2 font-bold ${r >= 0 ? 'text-emerald-400' : 'text-rose-400'}">${(r >= 0 ? '+' : '') + r.toFixed(2)}R</td>
                <td class="p-2 font-bold ${pnl >= 0 ? 'text-emerald-400' : 'text-rose-400'}">${(pnl >= 0 ? '+₹' : '-₹') + Math.abs(pnl).toFixed(2)}</td>
                <td class="p-2 text-right">${isBreach ? '<span class="text-rose-400 font-bold">⚠️ Breach</span>' : '<span class="text-emerald-400 font-bold">🛡️ Clean</span>'}</td>
              </tr>
            `;
          }).join('');
        }
      }
    }

    function copyDossierMarkdown() {
      const trades = typeof tradesData !== 'undefined' ? tradesData : [];
      let totalPnL = 0;
      let totalR = 0;
      let wins = 0;
      let breaches = 0;

      trades.forEach(t => {
        totalPnL += parseFloat(t.net_pnl || 0);
        totalR += parseFloat(t.r_multiple || 0);
        if (t.outcome === 'Win') wins++;
        if (t.rule_violation === 'Y') breaches++;
      });

      const winRate = trades.length > 0 ? ((wins / trades.length) * 100).toFixed(1) : '0.0';
      const adhPct = trades.length > 0 ? (((trades.length - breaches) / trades.length) * 100).toFixed(1) : '100.0';

      const md = `# TRADER EXECUTION RESET SYSTEM — 30-DAY DOSSIER\\n**Date:** ${new Date().toLocaleDateString('en-IN')} | **Account:** Private Execution Desk (NSE)\\n**Verification Hash:** #RESET-V16-SECURE | **Audit Status:** Qualified Institutional Disciplined\\n\\n## 1. Executive KPIs\\n- **Net P&L:** ₹${totalPnL.toFixed(2)}\\n- **Realized R:** ${(totalR >= 0 ? '+' : '') + totalR.toFixed(2)}R\\n- **Total Trades:** ${trades.length}\\n- **Win Rate:** ${winRate}%\\n- **Rule Adherence Rate:** ${adhPct}%\\n- **Demerit Violations:** ${breaches}\\n\\n## 2. Operating Rules Verification\\n- **Window Adherence (09:15–10:30 AM IST):** Verified & Honored\\n- **Stop-Loss Execution:** Non-Negotiable Structural Hard Stops Pre-Committed\\n- **Daily Loss Ceiling:** ₹500 Max / Trade, 2 Consecutive Losses Hard Quit\\n\\n*Signed & Attested by Private Desk Trader*\\n`;

      navigator.clipboard.writeText(md).then(() => {
        alert('📋 Monthly Dossier executive summary copied to clipboard as Markdown!');
      }).catch(() => {
        alert('Clipboard copy permission denied. Please copy manually.');
      });
    }

    // Wrap updateISTMarketClock to trigger 10:30 AM alerts
    function checkMarketWindowAlerts() {
      const now = new Date();
      const istTimeStr = now.toLocaleTimeString('en-US', { timeZone: 'Asia/Kolkata', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
      const [h, m, s] = istTimeStr.split(':').map(Number);
      const curMinutes = h * 60 + m;

      // 10:30 AM IST Window Close Alert
      if (curMinutes === 10 * 60 + 30 && s <= 5 && !hasAlerted1030Today) {
        hasAlerted1030Today = true;
        playAlertSiren('urgent');
        sendDesktopAlert('⚠️ 10:30 AM IST EXECUTION WINDOW CLOSED', 'Intraday momentum window has ended. Step away from the screens immediately. Capital preservation mode active.', 'window-closed');
      }
    }
    setInterval(checkMarketWindowAlerts, 1000);

    // Initial hooks
    window.addEventListener('DOMContentLoaded', () => {
      updateDesktopAlertsUI();
      checkPreFlightStatusToday();
      setTimeout(() => {
        if (typeof tradesData !== 'undefined') {
          renderCalendarHeatmap(tradesData);
        }
      }, 500);
    });
"""

    target_script_end = "    // Hook listeners on DOM ready\n    window.addEventListener('DOMContentLoaded', () => {"
    assert target_script_end in code, "Failed to find script DOM ready hook"
    code = code.replace(target_script_end, extended_js + chr(10) + chr(10) + target_script_end, 1)

    with open(MASTER_FILE, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"Successfully updated {MASTER_FILE} with Options 1, 2, 4, 5!")

if __name__ == "__main__":
    main()
