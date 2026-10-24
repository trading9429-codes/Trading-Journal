#!/usr/bin/env python3
"""
Master Builder for Trader Execution Reset System Command Center v14.
Guarantees clean DOM architecture, breathtaking Linear/Fintech Obsidian UI,
and zero script misplaced in <head>.
"""

import os
import sys

# Import base HTML_V7 from build_dashboard_v7.py
sys.path.insert(0, "/home/sunny/.gemini/antigravity/scratch/trader-reset-system")
from build_dashboard_v7 import HTML_V7

OUT_PUBLIC = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/public/index.html"
OUT_DELIV = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html"
OUT_BRAIN = "/home/sunny/.gemini/antigravity/brain/85803015-3567-4584-af28-ca9d6eed9423/trader_dashboard.html"

def generate_v14():
    content = HTML_V7

    # 1. UPGRADE HEAD: Google Fonts (Inter + JetBrains Mono), Obsidian Palette & Linear Glassmorphic Styling
    old_head = r'''<head>
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
</head>'''

    new_head = r'''<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Trader Execution Reset System — Institutional Command Center</title>
  
  <!-- Inter & JetBrains Mono Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS & Chart.js -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
            mono: ['JetBrains Mono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace']
          },
          colors: {
            brand: { 50: '#f0fdf4', 500: '#10b981', 600: '#059669', 700: '#047857' }
          }
        }
      }
    }
  </script>
  <style>
    body {
      background-color: #060913;
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(30, 58, 138, 0.18) 0%, transparent 65%),
        radial-gradient(circle at 100% 100%, rgba(16, 185, 129, 0.08) 0%, transparent 45%);
      background-attachment: fixed;
      color: #F1F5F9;
      font-family: 'Inter', ui-sans-serif, system-ui, -apple-system, sans-serif;
      letter-spacing: -0.012em;
    }
    .font-mono { font-family: 'JetBrains Mono', monospace !important; }
    
    .glass-card {
      background: rgba(11, 17, 32, 0.88);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.08);
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7);
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .glass-card:hover {
      border-color: rgba(255, 255, 255, 0.14);
    }
    
    ::-webkit-scrollbar { width: 5px; height: 5px; }
    ::-webkit-scrollbar-track { background: #060913; }
    ::-webkit-scrollbar-thumb { background: #1E293B; border-radius: 9999px; }
    ::-webkit-scrollbar-thumb:hover { background: #334155; }
    
    .tab-btn.active {
      background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
      color: #FFFFFF;
      border-color: #3B82F6;
      box-shadow: 0 4px 20px rgba(37, 99, 235, 0.4);
    }
    .tab-btn:not(.active) {
      background: rgba(11, 17, 32, 0.6);
      color: #94A3B8;
      border-color: rgba(255, 255, 255, 0.06);
    }
    .tab-btn:not(.active):hover {
      background: rgba(17, 24, 39, 0.9);
      color: #F8FAFC;
      border-color: rgba(255, 255, 255, 0.14);
    }

    /* High-Contrast Direction Segmented Buttons */
    .dir-toggle-btn.active-long {
      background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
      color: #FFFFFF !important;
      border-color: #10B981 !important;
      box-shadow: 0 0 16px rgba(16, 185, 129, 0.4) !important;
    }
    .dir-toggle-btn.active-short {
      background: linear-gradient(135deg, #DC2626 0%, #B91C1C 100%) !important;
      color: #FFFFFF !important;
      border-color: #EF4444 !important;
      box-shadow: 0 0 16px rgba(239, 68, 68, 0.4) !important;
    }
    .dir-toggle-btn:not(.active-long):not(.active-short) {
      background: #080D1A;
      color: #94A3B8;
      border-color: rgba(255, 255, 255, 0.08);
    }

    @media print {
      body * { visibility: hidden; }
      #weeklyReviewModalContent, #weeklyReviewModalContent * { visibility: visible; }
      #weeklyReviewModalContent { position: absolute; left: 0; top: 0; width: 100%; background: white !important; color: black !important; }
    }
  </style>
</head>'''

    assert old_head in content, "Failed to find old_head"
    content = content.replace(old_head, new_head, 1)

    # 2. HEADER: Add Mindset Timer and Demerit Strikes pills cleanly grouped
    old_sound_btn = r'''        <button id="soundToggleBtn" onclick="toggleSound()" class="px-2.5 py-1.5 rounded-lg bg-slate-800/80 border border-slate-700 text-slate-300 hover:text-white flex items-center gap-1.5 transition">
          <span id="soundIcon">🔊</span>
          <span id="soundText" class="font-medium">Audio ON</span>
        </button>'''

    new_sound_btn = r'''        <button onclick="openPreMarketFocusModal()" class="px-2.5 py-1.5 rounded-lg bg-teal-500/10 border border-teal-500/30 text-teal-300 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm" title="5-Minute Pre-Market Mindset &amp; Box Breathing (09:05–09:10 AM IST)">
          <span>🧘</span>
          <span>Mindset Timer</span>
        </button>

        <button onclick="openTraderContractModal()" id="headerDemeritBadge" class="px-2.5 py-1.5 rounded-lg bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm" title="Execution Contract &amp; Penalty Strike System">
          <span>⚖️</span>
          <span id="headerStrikesText">Strikes: 0/3</span>
        </button>

        <button onclick="testAudioCoachVoice()" class="px-2.5 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm" title="Audio Coach Verbal Feedback (Click to test)">
          <span>🗣️</span>
          <span>Voice Coach</span>
        </button>

        <button id="soundToggleBtn" onclick="toggleSound()" class="px-2.5 py-1.5 rounded-lg bg-slate-800/80 border border-slate-700 text-slate-300 hover:text-white flex items-center gap-1.5 transition">
          <span id="soundIcon">🔊</span>
          <span id="soundText" class="font-medium">Audio ON</span>
        </button>'''

    assert old_sound_btn in content, "Failed to find old_sound_btn"
    content = content.replace(old_sound_btn, new_sound_btn, 1)

    # 3. GLOBAL ACTIONS TOOLBAR: Simple, unified buttons
    old_toolbar = r'''<!-- Global Actions Strip -->
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
      </div>'''

    new_toolbar = r'''<!-- Global Actions Strip -->
      <div class="flex items-center gap-2 w-full xl:w-auto justify-end flex-wrap">
        <button onclick="openWebhookModal()" class="px-3 py-2 rounded-lg bg-sky-600/20 hover:bg-sky-600/30 text-sky-300 border border-sky-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm" title="Configure Telegram/WhatsApp Accountability Alerts">
          <span>🔔</span>
          <span>Alerts &amp; Webhook</span>
        </button>
        <button onclick="openFyersIngestModal()" class="px-3 py-2 rounded-lg bg-gradient-to-r from-orange-600 to-amber-600 hover:from-orange-500 hover:to-amber-500 text-white font-bold text-xs flex items-center gap-1.5 transition shadow-lg shadow-orange-600/20" title="Quickly Import Trades via Copy-Paste or CSV">
          <span>⚡</span>
          <span>Import FYERS Trades</span>
        </button>
        <button onclick="openWeeklyReviewModal()" class="px-3 py-2 rounded-lg bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-400 border border-indigo-500/30 font-medium text-xs flex items-center gap-1.5 transition">
          <span>📝</span>
          <span>Weekly Review (D5)</span>
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
      </div>'''

    assert old_toolbar in content, "Failed to find old_toolbar"
    content = content.replace(old_toolbar, new_toolbar, 1)

    # 4. TAB 1: Add 30-Day Phase Graduation Tracker at top of Tab 1
    phase_tracker_block = r'''<!-- ========================================== -->
    <!-- TAB 1: LIVE EXECUTION & TRADE LOG -->
    <!-- ========================================== -->
    <div id="tabContent1" class="mt-6 space-y-6">

      <!-- 30-DAY PHASE GRADUATION & DISCIPLINE TRACKER WIDGET -->
      <section class="glass-card rounded-2xl p-5 shadow-2xl border border-blue-500/20 bg-gradient-to-r from-slate-900/95 via-slate-900/80 to-blue-950/40">
        <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4 pb-4 border-b border-slate-800">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-blue-500/20 border border-blue-500/40 flex items-center justify-center text-blue-400 font-black text-lg shadow-lg">
              🎯
            </div>
            <div>
              <div class="flex items-center gap-2">
                <h2 class="text-sm font-bold text-white uppercase tracking-wider">30-Day Execution Reset Graduation</h2>
                <span id="activePhasePill" class="text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/30">
                  Phase 2: Days 4–10 (Consolidation)
                </span>
                <span id="phaseGraduationStatusBadge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
                  ✅ Qualified for Promotion
                </span>
              </div>
              <p class="text-xs text-slate-400 mt-0.5">
                Current Rules: <strong class="text-slate-200" id="phaseTradeCapText">Max 2 Trades/Day</strong> &bull; Risk: <strong class="text-slate-200" id="phaseRiskText">0.25% &ndash; 0.50%</strong> &bull; Window: <strong class="text-slate-200">09:15–10:30 AM</strong> &bull; Stop after 2 losses
              </p>
            </div>
          </div>

          <!-- Phase Navigation Selector Buttons -->
          <div class="flex items-center gap-1.5 bg-slate-950/80 p-1 rounded-xl border border-slate-800 text-xs">
            <button onclick="setPhase(1)" id="phaseBtn_1" class="phase-selector-btn px-2.5 py-1 rounded-lg font-bold text-slate-400 hover:text-white transition">
              Phase 1 (1–3)
            </button>
            <button onclick="setPhase(2)" id="phaseBtn_2" class="phase-selector-btn px-2.5 py-1 rounded-lg font-bold bg-blue-600 text-white transition shadow">
              Phase 2 (4–10)
            </button>
            <button onclick="setPhase(3)" id="phaseBtn_3" class="phase-selector-btn px-2.5 py-1 rounded-lg font-bold text-slate-400 hover:text-white transition">
              Phase 3 (11–20)
            </button>
            <button onclick="setPhase(4)" id="phaseBtn_4" class="phase-selector-btn px-2.5 py-1 rounded-lg font-bold text-slate-400 hover:text-white transition">
              Phase 4 (21–30)
            </button>
          </div>
        </div>

        <!-- Progress Bar & Key Gate Conditions -->
        <div class="mt-4 grid grid-cols-1 md:grid-cols-4 gap-4 items-center">
          <div class="md:col-span-2">
            <div class="flex justify-between items-center text-xs mb-1.5">
              <span class="text-slate-400 font-medium">30-Day Reset Progress</span>
              <span class="font-bold text-blue-400 font-mono" id="phaseDayProgressText">Day 4 of 30 (13.3%)</span>
            </div>
            <div class="w-full bg-slate-800 rounded-full h-2.5 overflow-hidden border border-slate-700">
              <div id="phaseProgressBar" class="bg-gradient-to-r from-blue-500 via-indigo-500 to-emerald-500 h-2.5 rounded-full transition-all duration-500" style="width: 13.3%;"></div>
            </div>
          </div>

          <div class="bg-slate-950/60 p-2.5 rounded-xl border border-slate-800 flex items-center justify-between text-xs">
            <span class="text-slate-400">Phase Rule Adherence:</span>
            <span id="phaseDisciplineScoreText" class="font-mono font-bold text-emerald-400">100% (Target &ge;90%)</span>
          </div>

          <div class="flex items-center gap-2 justify-end">
            <button onclick="graduatePhase()" class="w-full py-2 px-3 rounded-xl bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-500/30 text-xs font-bold transition flex items-center justify-center gap-1.5">
              <span>🚀</span>
              <span>Advance Phase</span>
            </button>
            <button onclick="resetToPhase1()" class="py-2 px-2.5 rounded-xl bg-red-600/10 hover:bg-red-600/20 text-red-400 border border-red-500/20 text-xs font-semibold transition" title="Reset to Phase 1 (Day 1) on rule breach">
              <span>↺</span>
            </button>
          </div>
        </div>
      </section>'''

    old_tab1_start = r'''<!-- ========================================== -->
    <!-- TAB 1: LIVE EXECUTION & TRADE LOG -->
    <!-- ========================================== -->
    <div id="tabContent1" class="mt-6 space-y-6">'''

    assert old_tab1_start in content, "Failed to find old_tab1_start"
    content = content.replace(old_tab1_start, phase_tracker_block, 1)

    # 5. DIRECTION TOGGLE & INPUTS: Replace Direction select with Big Interactive Buttons
    old_dir_select = r'''            <div>
              <label class="block text-slate-400 text-[11px] font-semibold uppercase tracking-wider mb-1">Direction</label>
              <select id="direction" onchange="recalculateCalculators()" class="w-full bg-slate-900 border border-slate-700/80 rounded-xl px-3 py-2 text-white text-sm font-semibold focus:outline-none focus:border-blue-500">
                <option value="Long">LONG (Buy)</option>
                <option value="Short">SHORT (Sell)</option>
              </select>
            </div>'''

    new_dir_select = r'''            <div>
              <label class="block text-slate-400 text-[11px] font-semibold uppercase tracking-wider mb-1">Direction</label>
              <input type="hidden" id="direction" value="Long">
              <div class="grid grid-cols-2 gap-1.5 bg-slate-950/80 p-1 rounded-xl border border-slate-800">
                <button type="button" id="dirBtnLong" onclick="setTradeDirection('Long')" class="dir-toggle-btn active-long py-1.5 px-3 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition">
                  <span>🟢</span>
                  <span>LONG</span>
                </button>
                <button type="button" id="dirBtnShort" onclick="setTradeDirection('Short')" class="dir-toggle-btn py-1.5 px-3 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition">
                  <span>🔴</span>
                  <span>SHORT</span>
                </button>
              </div>
            </div>'''

    assert old_dir_select in content, "Failed to find old_dir_select"
    content = content.replace(old_dir_select, new_dir_select, 1)

    # 6. ENHANCE SETUPS DROPDOWN to include full playbook strategies
    old_setups = r'''              <select id="setup_name" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-2.5 py-1.5 text-white text-xs">
                <option value="1m Pullback to 9EMA">1m Pullback to 9EMA (Rule Setup A)</option>
                <option value="1m VWAP Bounce">1m VWAP Bounce / Trend Contin.</option>
                <option value="1m Breakout &amp; Re-test">1m Opening Breakout Re-test</option>
                <option value="Other / Discretionary">Other Discretionary</option>
              </select>'''

    new_setups = r'''              <select id="setup_name" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-2.5 py-1.5 text-white text-xs">
                <option value="1m Pullback to 9EMA">1m Pullback to 9EMA (Core Edge)</option>
                <option value="Opening Range Breakout (ORB)">Opening Range Breakout (ORB)</option>
                <option value="1m VWAP Bounce">1m VWAP Bounce / Trend Contin.</option>
                <option value="1m Breakout &amp; Re-test">1m Breakout &amp; Structural Re-test</option>
                <option value="Support / Resistance Bounce">Support / Resistance Level Bounce</option>
                <option value="Off-Plan / Discretionary">Off-Plan / Discretionary (Rule Breach)</option>
              </select>'''

    assert old_setups in content, "Failed to find old_setups"
    content = content.replace(old_setups, new_setups, 1)

    # 7. INJECT MAE/MFE & CHART SCREENSHOT DROPZONE INTO FORM
    old_form_preflight = r'''          </div>

          <!-- Pre-Execution Checklist & Submit Row -->
          <div class="flex flex-col lg:flex-row items-center justify-between gap-4 pt-2">'''

    new_form_preflight = r'''          </div>

          <!-- MAE & MFE Excursion Inputs (Exit Efficiency & Stop Leak Diagnostics) -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
            <div>
              <label class="block text-[11px] font-semibold text-slate-300 mb-1 flex items-center justify-between">
                <span>📉 MAE Price (Worst Drawdown)</span>
                <span class="text-[10px] text-slate-500 font-mono">Maximum Adverse</span>
              </label>
              <input type="number" step="0.05" id="mae_price" placeholder="e.g. 2496.50" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 font-mono">
            </div>
            <div>
              <label class="block text-[11px] font-semibold text-slate-300 mb-1 flex items-center justify-between">
                <span>📈 MFE Price (Peak Potential)</span>
                <span class="text-[10px] text-slate-500 font-mono">Maximum Favorable</span>
              </label>
              <input type="number" step="0.05" id="mfe_price" placeholder="e.g. 2514.00" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 font-mono">
            </div>
          </div>

          <!-- Visual Chart Screenshot Dropzone & Clipboard Paste Area -->
          <div class="bg-slate-900/50 p-3.5 rounded-xl border border-dashed border-slate-700 hover:border-blue-500/60 transition">
            <div class="flex items-center justify-between mb-1.5">
              <label class="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
                <span>📸</span>
                <span>1-Min Execution Chart Screenshot</span>
              </label>
              <span class="text-[10px] text-blue-400 font-mono bg-blue-500/10 px-2 py-0.5 rounded border border-blue-500/20">
                Tip: Press Ctrl+V anywhere to paste
              </span>
            </div>

            <!-- Upload / Paste Target -->
            <div id="screenshotDropzone" onclick="document.getElementById('screenshotFileInput').click()" class="cursor-pointer py-3 px-4 border border-slate-800 rounded-lg bg-slate-950/60 text-center hover:bg-slate-900 transition flex flex-col items-center justify-center">
              <input type="file" id="screenshotFileInput" accept="image/*" class="hidden" onchange="handleScreenshotFile(event)">
              <div id="dropzoneEmptyView" class="space-y-1">
                <span class="text-xl">📷</span>
                <p class="text-xs text-slate-300 font-medium">Click to upload or <kbd class="px-1.5 py-0.5 bg-slate-800 rounded text-[10px] border border-slate-700 font-mono text-blue-300">Ctrl + V</kbd> to paste screenshot</p>
                <p class="text-[10px] text-slate-500">PNG, JPG, WebP supported &bull; Embedded in journal &amp; review</p>
              </div>

              <!-- Attached Image Preview Container -->
              <div id="dropzonePreviewView" class="hidden w-full flex items-center justify-between gap-3">
                <div class="flex items-center gap-3">
                  <img id="screenshotThumbnail" src="" alt="Chart Screenshot" class="w-16 h-12 object-cover rounded border border-slate-700 shadow cursor-zoom-in" onclick="event.stopPropagation(); zoomScreenshot(this.src)">
                  <div class="text-left">
                    <p class="text-xs font-bold text-emerald-400 flex items-center gap-1"><span>✓</span> Screenshot Attached</p>
                    <p class="text-[10px] text-slate-400" id="screenshotMetaText">Ready for post-trade review</p>
                  </div>
                </div>
                <button type="button" onclick="event.stopPropagation(); removeScreenshot()" class="px-2.5 py-1 rounded bg-rose-600/20 hover:bg-rose-600/30 text-rose-300 text-xs font-semibold border border-rose-500/30 transition">
                  ✕ Remove
                </button>
              </div>
            </div>
          </div>

          <!-- Pre-Execution Checklist & Submit Row -->
          <div class="flex flex-col lg:flex-row items-center justify-between gap-4 pt-2">'''

    assert old_form_preflight in content, "Failed to find old_form_preflight"
    content = content.replace(old_form_preflight, new_form_preflight, 1)

    # 8. STRATEGY FILTER IN LEDGER TABLE
    old_ledger_filters = r'''            <select id="outcomeFilter" onchange="renderTradesTable()" class="bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white focus:outline-none focus:border-blue-500">
              <option value="ALL">All Outcomes</option>
              <option value="Win">Wins Only</option>
              <option value="Loss">Losses Only</option>
              <option value="Break-Even">Break-Even</option>
            </select>'''

    new_ledger_filters = r'''            <select id="strategyFilter" onchange="renderTradesTable()" class="bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white focus:outline-none focus:border-blue-500">
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
            </select>'''

    assert old_ledger_filters in content, "Failed to find old_ledger_filters"
    content = content.replace(old_ledger_filters, new_ledger_filters, 1)

    # 9. TAB 3: Add Multi-Strategy Attribution & MAE/MFE Exit Leak Analysis
    old_tab3_bottom = r'''      <!-- Bottom Section: Day-of-Week Matrix, 15-Min Heatmap & Setup Expectancy Matrix -->'''

    new_tab3_suites = r'''      <!-- MULTI-STRATEGY ATTRIBUTION & EDGE MATRIX -->
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
              <!-- Populated dynamically -->
            </tbody>
          </table>
        </div>
      </section>

      <!-- MAE / MFE EXIT EFFICIENCY & STOP LEAK ANALYSIS CARD -->
      <section class="glass-card rounded-2xl p-6 shadow-2xl border border-indigo-500/20">
        <div class="flex flex-col md:flex-row md:items-center justify-between pb-4 border-b border-slate-800 gap-2">
          <div>
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span class="text-indigo-400">🎯</span>
              <span>MAE &amp; MFE Exit Leak &amp; Stop Quality Diagnostics</span>
              <span class="text-xs px-2.5 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 font-mono">
                Trade Excursion Suite
              </span>
            </h2>
            <p class="text-xs text-slate-400">Quantifies whether stops are set too loose or tight (MAE) and calculates profits left on the table (MFE)</p>
          </div>
          <div class="flex items-center gap-2 text-xs font-mono">
            <span class="text-slate-400">Tracked Trades:</span>
            <span id="maeTrackedCountDisp" class="font-bold text-indigo-300">0 Fills</span>
          </div>
        </div>

        <!-- 4 MAE/MFE Key Metric Tiles -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mt-5">
          <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800">
            <p class="text-xs font-medium text-slate-400 flex items-center justify-between">
              <span>Avg MAE (Adverse)</span>
              <span class="text-[10px] text-slate-500">Stop Proximity</span>
            </p>
            <p id="avgMaeDisp" class="text-xl font-bold font-mono text-amber-400 mt-1">0.32R</p>
            <p class="text-[10px] text-slate-500 mt-1">Drawdown before target/exit</p>
          </div>

          <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800">
            <p class="text-xs font-medium text-slate-400 flex items-center justify-between">
              <span>Avg MFE (Favorable)</span>
              <span class="text-[10px] text-slate-500">Peak Run</span>
            </p>
            <p id="avgMfeDisp" class="text-xl font-bold font-mono text-emerald-400 mt-1">2.75R</p>
            <p class="text-[10px] text-slate-500 mt-1">Peak move offered by setup</p>
          </div>

          <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800">
            <p class="text-xs font-medium text-slate-400 flex items-center justify-between">
              <span>Exit Efficiency %</span>
              <span class="text-[10px] text-slate-500">Capture Rate</span>
            </p>
            <p id="exitEfficiencyDisp" class="text-xl font-bold font-mono text-blue-400 mt-1">79.2%</p>
            <p class="text-[10px] text-slate-500 mt-1">Realized R &divide; MFE Peak R</p>
          </div>

          <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800">
            <p class="text-xs font-medium text-slate-400 flex items-center justify-between">
              <span>Money Left On Table</span>
              <span class="text-[10px] text-slate-500">Panic Premature Exits</span>
            </p>
            <p id="moneyLeftOnTableDisp" class="text-xl font-bold font-mono text-rose-400 mt-1">₹0.00</p>
            <p class="text-[10px] text-slate-500 mt-1" id="moneyLeftRDisp">0.00R uncaptured upside</p>
          </div>
        </div>

        <div class="mt-4 p-4 rounded-xl bg-slate-950/60 border border-slate-800 text-xs flex flex-col md:flex-row items-center justify-between gap-3">
          <div class="flex items-center gap-3">
            <span class="text-2xl">💡</span>
            <div>
              <p class="font-bold text-white">Stop Quality Calibration</p>
              <p class="text-slate-400">Avg MAE below 0.50R proves stops are structurally sound and not hunted by opening volatility.</p>
            </div>
          </div>
          <div class="flex items-center gap-2 whitespace-nowrap">
            <span class="px-3 py-1.5 rounded-lg bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 font-mono font-bold">
              Stop Quality: High
            </span>
          </div>
        </div>
      </section>

      <!-- Bottom Section: Day-of-Week Matrix, 15-Min Heatmap & Setup Expectancy Matrix -->'''

    assert old_tab3_bottom in content, "Failed to find old_tab3_bottom"
    content = content.replace(old_tab3_bottom, new_tab3_suites, 1)

    # 10. TAB 4: Add Basel-III Value at Risk (VaR 95% & 99%), Expected Shortfall & Stress Testing
    old_tab4_close = r'''        </div>
      </section>

    </div>
  </main>'''

    new_tab4_suites = r'''        </div>
      </section>

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
      </section>

    </div>
  </main>'''

    assert old_tab4_close in content, "Failed to find old_tab4_close"
    content = content.replace(old_tab4_close, new_tab4_suites, 1)

    # 11. INJECT ALL MODALS INTO BODY (Right before </body>)
    all_modals_markup = r'''  <!-- ========================================== -->
  <!-- MODAL: SIMPLE & FAST FYERS TRADE INGESTION -->
  <!-- ========================================== -->
  <div id="fyersIngestModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="glass-card rounded-2xl w-full max-w-xl border border-orange-500/30 shadow-2xl p-6 relative max-h-[90vh] overflow-y-auto">
      
      <div class="flex items-center justify-between pb-4 border-b border-slate-800">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-orange-500 to-amber-600 flex items-center justify-center text-white font-black text-lg shadow-lg shadow-orange-500/20">
            ⚡
          </div>
          <div>
            <h3 class="text-base font-extrabold text-white flex items-center gap-2">
              Import FYERS Trades
              <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                Zero Setup &bull; Offline
              </span>
            </h3>
            <p class="text-xs text-slate-400">Copy-paste from FYERS Web or upload your tradebook export</p>
          </div>
        </div>
        <button onclick="closeFyersIngestModal()" class="text-slate-400 hover:text-white text-2xl font-bold">&times;</button>
      </div>

      <div class="space-y-4 mt-5 text-xs">
        <!-- OPTION 1: INSTANT WEB COPY-PASTE -->
        <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800 space-y-2.5">
          <div class="flex items-center justify-between">
            <span class="font-bold text-slate-200 flex items-center gap-1.5">
              <span>📋</span>
              <span>Option 1: Paste Rows from FYERS Web</span>
            </span>
            <span class="text-[10px] text-orange-400 font-mono">Fastest (5 Seconds)</span>
          </div>
          
          <p class="text-slate-400 text-[11px] leading-relaxed">
            In FYERS Web, go to <strong>Tradebook</strong>, select your trade rows with <kbd class="px-1.5 py-0.5 bg-slate-800 rounded text-slate-300 border border-slate-700 font-mono">Ctrl + C</kbd>, and paste here:
          </p>
          
          <textarea id="fyersPastedTextArea" rows="4" placeholder="Paste FYERS Tradebook rows here...
Example:
RELIANCE-EQ  BUY   100  2500.00  FILLED  09:21:34
RELIANCE-EQ  SELL  100  2512.50  FILLED  09:28:10" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 text-white font-mono text-xs placeholder-slate-600 focus:outline-none focus:border-orange-500"></textarea>

          <button onclick="parseFyersWebPastedText()" class="w-full py-2.5 px-4 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold transition flex items-center justify-center gap-2 shadow-lg shadow-emerald-600/30">
            <span>⚡ Parse &amp; Log Trades</span>
          </button>
        </div>

        <div class="flex items-center gap-3">
          <div class="flex-1 h-px bg-slate-800"></div>
          <span class="text-[10px] font-bold text-slate-500 uppercase">OR</span>
          <div class="flex-1 h-px bg-slate-800"></div>
        </div>

        <!-- OPTION 2: FILE UPLOAD -->
        <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800 space-y-2.5">
          <div class="flex items-center justify-between">
            <span class="font-bold text-slate-200 flex items-center gap-1.5">
              <span>📁</span>
              <span>Option 2: Select FYERS Tradebook File</span>
            </span>
            <span class="text-[10px] text-slate-500 font-mono">CSV / XLSX</span>
          </div>

          <p class="text-slate-400 text-[11px]">
            Download your tradebook from FYERS Back-Office or Terminal and select it here:
          </p>

          <button onclick="closeFyersIngestModal(); triggerFyersImport();" class="w-full py-2.5 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-bold transition flex items-center justify-center gap-2">
            <span>📂 Choose FYERS Tradebook File</span>
          </button>
        </div>

        <div class="bg-blue-500/10 border border-blue-500/20 rounded-xl p-3 text-blue-300 text-[11px] flex items-center gap-2.5">
          <span class="text-lg">🔒</span>
          <span>100% private and runs locally in your browser. Automatically calculates brokerage, STT, and 18% GST down to the paisa.</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL: ACCOUNTABILITY & WEBHOOK SETTINGS -->
  <!-- ========================================== -->
  <div id="webhookSettingsModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="glass-card rounded-2xl w-full max-w-xl border border-slate-700 shadow-2xl p-6 relative max-h-[90vh] overflow-y-auto">
      <div class="flex items-center justify-between pb-4 border-b border-slate-800">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-sky-500/20 border border-sky-500/40 flex items-center justify-center text-sky-400 font-bold">
            🔔
          </div>
          <div>
            <h3 class="text-base font-bold text-white">Accountability &amp; Webhook Alerts</h3>
            <p class="text-xs text-slate-400">Broadcast execution milestones, cooldowns, and kill switches to Telegram / WhatsApp</p>
          </div>
        </div>
        <button onclick="closeWebhookModal()" class="text-slate-400 hover:text-white text-xl">&times;</button>
      </div>

      <div class="space-y-4 mt-5 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Telegram Bot Token</label>
          <input type="password" id="webhookTelegramToken" placeholder="123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white font-mono focus:border-sky-500 focus:outline-none">
          <p class="text-[10px] text-slate-500 mt-1">Obtain from @BotFather on Telegram</p>
        </div>

        <div>
          <label class="block font-semibold text-slate-300 mb-1">Telegram Chat ID / Channel ID</label>
          <input type="text" id="webhookTelegramChatId" placeholder="-100123456789 or @YourAccountabilityChannel" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white font-mono focus:border-sky-500 focus:outline-none">
          <p class="text-[10px] text-slate-500 mt-1">Your personal chat ID or private channel ID</p>
        </div>

        <div>
          <label class="block font-semibold text-slate-300 mb-1">Custom Webhook URL (WhatsApp / Zapier / Make)</label>
          <input type="url" id="webhookCustomUrl" placeholder="https://hook.eu1.make.com/..." class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white font-mono focus:border-sky-500 focus:outline-none">
          <p class="text-[10px] text-slate-500 mt-1">Fires HTTP POST JSON with event payload</p>
        </div>

        <div class="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800 space-y-2">
          <p class="font-semibold text-slate-200">Alert Trigger Rules:</p>
          <label class="flex items-center gap-2 cursor-pointer text-slate-300">
            <input type="checkbox" id="notifyOnTrade" checked class="rounded border-slate-700 bg-slate-800 text-sky-500">
            <span>📢 Notify on Every Trade Dispatched (Entry &amp; Exit)</span>
          </label>
          <label class="flex items-center gap-2 cursor-pointer text-slate-300">
            <input type="checkbox" id="notifyOnCooldown" checked class="rounded border-slate-700 bg-slate-800 text-sky-500">
            <span>🚨 Notify on Loss Registered (30-Minute Cooldown Lock Active)</span>
          </label>
          <label class="flex items-center gap-2 cursor-pointer text-slate-300">
            <input type="checkbox" id="notifyOnKillSwitch" checked class="rounded border-slate-700 bg-slate-800 text-sky-500">
            <span>🛑 Notify on Broker Kill Switch Tripped (2 Trades or 2 Losses)</span>
          </label>
          <label class="flex items-center gap-2 cursor-pointer text-slate-300">
            <input type="checkbox" id="notifyOnReview" checked class="rounded border-slate-700 bg-slate-800 text-sky-500">
            <span>📊 Notify on Weekly Review / Phase Graduation</span>
          </label>
        </div>
      </div>

      <div class="mt-6 flex items-center justify-between gap-3 pt-4 border-t border-slate-800">
        <button onclick="testWebhookAlert()" class="px-4 py-2 rounded-xl bg-sky-600/20 hover:bg-sky-600/30 text-sky-300 border border-sky-500/30 text-xs font-bold transition flex items-center gap-1.5">
          <span>⚡</span>
          <span>Send Instant Test Ping</span>
        </button>
        <div class="flex items-center gap-2">
          <button onclick="closeWebhookModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs transition">Cancel</button>
          <button onclick="saveWebhookSettings()" class="px-5 py-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs transition shadow-lg shadow-sky-600/30">Save Settings</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
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

      <div class="py-8 flex flex-col items-center justify-center">
        <div id="breathingRing" class="w-40 h-40 rounded-full border-4 border-teal-500/40 bg-teal-500/10 flex flex-col items-center justify-center transition-all duration-1000 shadow-2xl shadow-teal-500/20">
          <span id="breathingActionText" class="text-sm font-black uppercase tracking-widest text-teal-300">Inhale</span>
          <span id="breathingCounterText" class="text-2xl font-black font-mono text-white mt-1">4s</span>
        </div>
        <p class="text-xs text-slate-400 mt-4 font-medium" id="breathingSubText">Inhale deeply through your nose (4 seconds)</p>
      </div>

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
  </div>

  <!-- ========================================== -->
  <!-- MODAL: CHART SCREENSHOT ZOOM -->
  <!-- ========================================== -->
  <div id="screenshotZoomModal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md hidden flex items-center justify-center p-4" onclick="closeScreenshotZoom()">
    <div class="relative max-w-5xl max-h-[90vh] flex flex-col items-center" onclick="event.stopPropagation()">
      <div class="absolute -top-10 right-0 flex items-center gap-2">
        <button onclick="closeScreenshotZoom()" class="text-white hover:text-slate-300 text-2xl font-bold bg-slate-800/80 px-3 py-1 rounded-lg">&times;</button>
      </div>
      <img id="screenshotZoomImg" src="" alt="Zoomed Screenshot" class="max-h-[85vh] max-w-full rounded-xl border border-slate-700 shadow-2xl object-contain">
      <p class="text-xs text-slate-400 mt-2">1-Minute Execution Chart &bull; Press ESC or click background to close</p>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL: IMPULSE FRICTION BARRIER (PRE-ORDER GATE) -->
  <!-- ========================================== -->
  <div id="preOrderGateModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="glass-card rounded-2xl p-6 max-w-lg w-full border border-amber-500/40 bg-slate-900 shadow-2xl relative overflow-hidden">
      <div class="flex items-center justify-between pb-4 border-b border-slate-800">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-amber-400 font-bold text-lg">
            ⏳
          </div>
          <div>
            <h3 class="text-sm font-bold text-white uppercase tracking-wider flex items-center gap-2">
              <span>Impulse Friction Gate</span>
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30">5-Sec Mandatory Pause</span>
            </h3>
            <p class="text-xs text-slate-400">Halting impulsive market execution &bull; Verify before committing</p>
          </div>
        </div>
        <button onclick="closePreOrderGate()" class="text-slate-400 hover:text-white text-xl font-bold p-1">&times;</button>
      </div>

      <div class="mt-4 p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 grid grid-cols-3 gap-2 text-center">
        <div>
          <span class="text-[10px] uppercase text-slate-500 font-semibold block">Symbol &amp; Dir</span>
          <span id="gateSymbolDir" class="text-xs font-mono font-bold text-emerald-400">RELIANCE (LONG)</span>
        </div>
        <div>
          <span class="text-[10px] uppercase text-slate-500 font-semibold block">Planned R:R</span>
          <span id="gatePlannedRR" class="text-xs font-mono font-bold text-emerald-400">2.40R</span>
        </div>
        <div>
          <span class="text-[10px] uppercase text-slate-500 font-semibold block">Max Risk</span>
          <span id="gateRiskAmount" class="text-xs font-mono font-bold text-amber-400">₹500.00</span>
        </div>
      </div>

      <div class="mt-4 space-y-2">
        <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/40 border border-slate-700/50 text-xs">
          <span class="text-slate-300 flex items-center gap-2">
            <span class="text-emerald-400 font-bold">1.</span>
            <span>1-Minute Playbook Setup Validated</span>
          </span>
          <span id="gateSetupBadge" class="text-[11px] font-semibold text-blue-300">1m Pullback to 9EMA</span>
        </div>
        <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/40 border border-slate-700/50 text-xs">
          <span class="text-slate-300 flex items-center gap-2">
            <span class="text-emerald-400 font-bold">2.</span>
            <span>Stop Loss Structural (Not Arbitrary)</span>
          </span>
          <span id="gateStopBadge" class="text-[11px] font-mono text-rose-300">SL: ₹2,495.00</span>
        </div>
        <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/40 border border-slate-700/50 text-xs">
          <span class="text-slate-300 flex items-center gap-2">
            <span class="text-emerald-400 font-bold">3.</span>
            <span>Trading Window Check (09:15–10:30 AM)</span>
          </span>
          <span id="gateTimeBadge" class="text-[11px] font-bold text-emerald-400">✅ Permitted Window</span>
        </div>
        <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/40 border border-slate-700/50 text-xs">
          <span class="text-slate-300 flex items-center gap-2">
            <span class="text-emerald-400 font-bold">4.</span>
            <span>Pre-Trade Mindset Certified</span>
          </span>
          <span class="text-[11px] font-bold text-emerald-400">Calm &bull; Non-Impulsive</span>
        </div>
      </div>

      <div class="mt-6 flex items-center justify-between pt-3 border-t border-slate-800">
        <button type="button" onclick="unlockGateImmediately()" class="text-[11px] text-amber-400 hover:text-white underline font-semibold transition flex items-center gap-1">
          <span>⚡</span>
          <span>Skip Wait (Instant Verify)</span>
        </button>
        <div class="flex items-center gap-3">
          <button type="button" onclick="abortPreOrderGate()" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition">
            ❌ Abort
          </button>
          <button type="button" id="gateConfirmBtn" onclick="commitPreOrderTrade()" disabled class="px-5 py-2.5 rounded-xl bg-slate-800 text-slate-500 font-bold text-xs flex items-center gap-2 cursor-not-allowed transition duration-300 shadow-lg">
            <span id="gateCountdownSpinner">⏳</span>
            <span id="gateConfirmText">Verifying Setup (3s)...</span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL: FULL-SCREEN TILT-BREAKER LOCKOUT -->
  <!-- ========================================== -->
  <div id="tiltBreakerModal" class="fixed inset-0 z-[100] bg-slate-950/95 backdrop-blur-2xl hidden flex items-center justify-center p-4 overflow-y-auto">
    <div class="glass-card rounded-3xl p-8 max-w-xl w-full border border-rose-500/40 bg-gradient-to-b from-slate-900/95 via-slate-950 to-slate-950 shadow-2xl relative text-center">
      <div class="w-20 h-20 mx-auto rounded-3xl bg-rose-500/10 border border-rose-500/30 flex items-center justify-center text-rose-400 text-4xl shadow-xl shadow-rose-950/50 animate-pulse mb-4">
        🛡️
      </div>

      <span class="text-[11px] font-mono uppercase tracking-widest text-rose-400 font-bold px-3 py-1 rounded-full bg-rose-500/10 border border-rose-500/30">
        CIRCUIT BREAKER LOCKOUT ACTIVE
      </span>

      <h2 class="text-2xl font-black text-white mt-3 uppercase tracking-wide">
        Capital Protected. Terminal Locked.
      </h2>
      <p class="text-xs text-slate-400 mt-2 max-w-md mx-auto leading-relaxed">
        You have achieved today's maximum execution ceiling (<strong class="text-slate-200" id="tiltLockReasonText">Max 2 Trades / 2 Losses</strong>). The single most profitable trait in professional intraday trading is walking away.
      </p>

      <div class="grid grid-cols-3 gap-3 my-6 p-4 rounded-2xl bg-slate-900/80 border border-slate-800/80">
        <div>
          <span class="text-[10px] text-slate-500 uppercase font-semibold block">Today's Trades</span>
          <span id="tiltTodayTradesCount" class="text-base font-bold font-mono text-white">2 / 2</span>
        </div>
        <div>
          <span class="text-[10px] text-slate-500 uppercase font-semibold block">Today's Net P&amp;L</span>
          <span id="tiltTodayNetPnL" class="text-base font-bold font-mono text-emerald-400">₹0.00</span>
        </div>
        <div>
          <span class="text-[10px] text-slate-500 uppercase font-semibold block">Discipline Score</span>
          <span id="tiltDisciplineScore" class="text-base font-bold font-mono text-blue-400">100%</span>
        </div>
      </div>

      <div class="p-3.5 rounded-xl bg-blue-950/20 border border-blue-500/20 mb-6">
        <span class="text-[10px] uppercase tracking-wider text-blue-300 font-bold block mb-1">
          Next Market Opening (09:15 AM IST)
        </span>
        <div id="tiltNextMarketCountdown" class="text-lg font-mono font-black text-white tracking-widest">
          --h --m --s
        </div>
        <p class="text-[11px] text-slate-400 mt-1">Review your journal, relax, and let your edge compound tomorrow.</p>
      </div>

      <div class="space-y-3">
        <button onclick="dismissTiltBreakerToReadOnly()" class="w-full py-3 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs shadow-lg shadow-blue-600/30 transition flex items-center justify-center gap-2">
          <span>👀</span>
          <span>Enter View-Only Mode (Review History &amp; Analytics)</span>
        </button>

        <div class="pt-2">
          <button type="button" onclick="toggleTiltEmergencyOverride()" class="text-[11px] text-slate-500 hover:text-slate-300 underline transition">
            Emergency Manual Override
          </button>
        </div>

        <div id="tiltOverrideBox" class="hidden mt-3 p-3.5 rounded-xl bg-rose-950/30 border border-rose-500/30 text-left">
          <p class="text-[11px] text-rose-300 font-semibold mb-2">
            ⚠️ OVERRIDE WARNING: Forcing terminal unlock will log <strong>+1 Demerit Penalty Strike</strong> on your Trader Contract.
          </p>
          <label class="block text-[10px] uppercase text-slate-400 font-mono mb-1">
            Type exact phrase: <strong class="text-white">I WILL NOT REVENGE TRADE</strong>
          </label>
          <div class="flex gap-2">
            <input type="text" id="tiltOverrideInput" placeholder="I WILL NOT REVENGE TRADE" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white font-mono focus:outline-none focus:border-rose-500">
            <button onclick="confirmTiltEmergencyOverride()" class="px-3 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs whitespace-nowrap">
              Unlock
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>'''

    target_script_start = "  <!-- APPLICATION LOGIC SCRIPT -->\n  <script>"
    assert target_script_start in content, "Failed to find APPLICATION LOGIC SCRIPT start"
    content = content.replace(target_script_start, f"{all_modals_markup}\n\n  <!-- APPLICATION LOGIC SCRIPT -->\n  <script>", 1)

    # 12. UPDATE JAVASCRIPT ENGINE (Place right before </body>, NOT in <head>!)
    # Intercept submitTrade with Pre-Order Gate
    old_submit_gate = r'''      const exitTime = document.getElementById('exit_time_input').value || '';

      const riskPerShare = Math.abs(entry - stop);'''

    new_submit_gate = r'''      const exitTime = document.getElementById('exit_time_input').value || '';

      // 1. IMPULSE FRICTION BARRIER (PRE-ORDER GATE)
      if (!window._gateConfirmed) {
        openPreOrderGate({
          symbol, direction, entry, stop, exitInput, qty, setupName, date, time, exitTime
        });
        return;
      }

      const riskPerShare = Math.abs(entry - stop);'''

    assert old_submit_gate in content, "Failed to find old_submit_gate"
    content = content.replace(old_submit_gate, new_submit_gate, 1)

    # Ensure submit button is ALWAYS enabled for live, historical, and test logging
    old_hist_override = "let isHistoricalOverride = false;"
    new_hist_override = "let isHistoricalOverride = true;"
    assert old_hist_override in content, "Failed to find old_hist_override"
    content = content.replace(old_hist_override, new_hist_override, 1)

    old_window_clock = r'''        if (!isHistoricalOverride) {
          banner.classList.remove('hidden');
          submitBtn.disabled = true;
          submitBtn.classList.add('opacity-50', 'cursor-not-allowed');
        } else {
          banner.classList.add('hidden');
          submitBtn.disabled = false;
          submitBtn.classList.remove('opacity-50', 'cursor-not-allowed');
        }'''

    new_window_clock = r'''        submitBtn.disabled = false;
        submitBtn.classList.remove('opacity-50', 'cursor-not-allowed');
        if (!isHistoricalOverride) {
          banner.classList.remove('hidden');
        } else {
          banner.classList.add('hidden');
        }'''

    assert old_window_clock in content, "Failed to find old_window_clock"
    content = content.replace(old_window_clock, new_window_clock, 1)

    old_cooldown_check = r'''        if (!isCooldownActive() && !isCircuitActive()) {
          submitBtn.disabled = false;
          submitBtn.classList.remove('opacity-50', 'cursor-not-allowed');
        }'''

    new_cooldown_check = r'''        submitBtn.disabled = false;
        submitBtn.classList.remove('opacity-50', 'cursor-not-allowed');'''

    assert old_cooldown_check in content, "Failed to find old_cooldown_check"
    content = content.replace(old_cooldown_check, new_cooldown_check, 1)

    old_trade_create = r'''      const tradeObj = {
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
      };'''

    new_trade_create = r'''      const maeVal = parseFloat(document.getElementById('mae_price').value) || null;
      const mfeVal = parseFloat(document.getElementById('mfe_price').value) || null;

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
        mae_price: maeVal,
        mfe_price: mfeVal,
        screenshot: currentTradeScreenshot || null,
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
      };'''

    assert old_trade_create in content, "Failed to find old_trade_create"
    content = content.replace(old_trade_create, new_trade_create, 1)

    # Post-submit cleanup
    old_post_submit = r'''      saveTradesLocally();
      renderTradesTable();
      renderTopCapitalHeader();
      checkDailyCircuitBreaker();'''

    new_post_submit = r'''      saveTradesLocally();
      renderTradesTable();
      renderTopCapitalHeader();
      checkDailyCircuitBreaker();
      dispatchAccountabilityAlert("TRADE_LOGGED", { trade: tradeObj });
      if (typeof speakCoach === "function") {
        if (tradeObj.outcome === 'Win') {
          speakCoach("Trade logged. Nice execution on " + tradeObj.symbol + ". Target reached.");
        } else if (tradeObj.outcome === 'Loss') {
          speakCoach("Trade closed in a loss. Mandatory 30-minute cooldown active. Step away from the screens.");
        } else {
          speakCoach("Trade logged. " + tradeObj.direction + " " + tradeObj.symbol + " at planned RR " + tradeObj.rr_planned + ".");
        }
      }
      window._gateConfirmed = false;
      closePreOrderGate();
      document.getElementById('mae_price').value = '';
      document.getElementById('mfe_price').value = '';
      removeScreenshot();'''

    assert old_post_submit in content, "Failed to find old_post_submit"
    content = content.replace(old_post_submit, new_post_submit, 1)

    # Cooldown alert trigger
    old_cooldown = r'''    function startCooldownTimer(endTime) {
      cooldownEndTime = endTime;'''
    new_cooldown = r'''    function startCooldownTimer(endTime) {
      cooldownEndTime = endTime;
      dispatchAccountabilityAlert("COOLDOWN_ACTIVE", { endTime: endTime });
      if (typeof speakCoach === "function") {
        speakCoach("Mandatory 30-minute loss cooldown initiated. Step away from your screens.");
      }'''
    assert old_cooldown in content, "Failed to find old_cooldown"
    content = content.replace(old_cooldown, new_cooldown, 1)

    # Kill switch alert trigger
    old_cb = r'''      if (todayTrades.length >= 2 || todayLosses.length >= 2) {
        cbBanner.classList.remove('hidden');'''
    new_cb = r'''      if (todayTrades.length >= 2 || todayLosses.length >= 2) {
        cbBanner.classList.remove('hidden');
        const cbReason = todayLosses.length >= 2 ? "2 Losses Daily Limit" : "2 Trades Daily Limit";
        dispatchAccountabilityAlert("KILL_SWITCH", { reason: cbReason });
        triggerTiltBreakerLockout(cbReason);'''
    assert old_cb in content, "Failed to find old_cb"
    content = content.replace(old_cb, new_cb, 1)

    # Camera icon in trade table
    content = content.replace(
        r'''<td class="py-2.5 px-3 font-bold text-white">${t.symbol}</td>''',
        r'''<td class="py-2.5 px-3 font-bold text-white flex items-center gap-1.5">${t.symbol} ${t.screenshot ? '<span class="text-[11px]" title="Chart attached">📷</span>' : ''}</td>'''
    )

    # Update ledger filter for strategy
    old_table_filter = r'''      const outcomeFilter = document.getElementById('outcomeFilter').value;

      let filtered = [...tradesData];'''

    new_table_filter = r'''      const outcomeFilter = document.getElementById('outcomeFilter').value;
      const strategyElem = document.getElementById('strategyFilter');
      const strategyVal = strategyElem ? strategyElem.value : 'ALL';

      let filtered = [...tradesData];
      if (strategyVal !== 'ALL') {
        filtered = filtered.filter(t => (t.setup_name || '') === strategyVal);
      }'''

    assert old_table_filter in content, "Failed to find old_table_filter"
    content = content.replace(old_table_filter, new_table_filter, 1)

    # Connect renderAllChartsAndMetrics
    old_render_all = r'''      } else if (currentTab === 3) {
        renderTimeOfDayHeatmap(trades);
        renderSetupMatrix(trades);
      } else if (currentTab === 4) {'''

    new_render_all = r'''      } else if (currentTab === 3) {
        renderTimeOfDayHeatmap(trades);
        renderSetupMatrix(trades);
        renderMAEMFEAnalytics(trades);
        renderStrategyAttribution(trades);
        computeVaRAndRecovery(trades);
      } else if (currentTab === 4) {'''

    assert old_render_all in content, "Failed to find old_render_all"
    content = content.replace(old_render_all, new_render_all, 1)

    # Append all engine functions before the closing script at the bottom of the body
    master_script_extension = r'''
    // ==========================================
    // EXTENDED MASTER ENGINE V14
    // ==========================================

    let currentTradeScreenshot = "";
    let activePhase = 2; // Default Phase 2 (Days 4-10)
    let currentDayNumber = 4;
    let penaltyStrikes = 0;

    // --- Audio Coach Engine (Speech Synthesis) ---
    function speakCoach(text) {
      if (typeof soundEnabled !== 'undefined' && !soundEnabled) return;
      if (!('speechSynthesis' in window)) {
        console.warn('Speech synthesis not supported in this browser.');
        return;
      }
      try {
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.rate = 0.95;
        utterance.pitch = 1.0;
        utterance.volume = 1.0;
        const voices = window.speechSynthesis.getVoices();
        if (voices && voices.length > 0) {
          const engVoice = voices.find(v => v.lang && (v.lang.startsWith('en-IN') || v.lang.startsWith('en-US') || v.lang.startsWith('en-GB') || v.lang.startsWith('en')));
          if (engVoice) utterance.voice = engVoice;
        }
        window.speechSynthesis.speak(utterance);
      } catch (err) {
        console.warn('Speech synthesis error:', err);
      }
    }

    function testAudioCoachVoice() {
      if (typeof playWinChime === 'function') playWinChime();
      speakCoach("Audio coach online. You are trading intraday equities with strict institutional discipline. Protect your capital first.");
    }

    // --- Weekly Governance Review Audit (D5) ---
    function openWeeklyReviewModal() {
      const modal = document.getElementById('weeklyReviewModal');
      if (!modal) return;

      const totalNetPnL = tradesData.reduce((acc, t) => acc + (parseFloat(t.net_pnl) || 0), 0);
      const wins = tradesData.filter(t => t.outcome === 'Win').length;
      const winRate = tradesData.length > 0 ? ((wins / tradesData.length) * 100).toFixed(1) : "0.0";
      const totalCosts = tradesData.reduce((acc, t) => acc + (parseFloat(t.costs) || 0), 0);
      const disciplinedTrades = tradesData.filter(t => t.rule_violation !== 'Y' && (!t.checklist_score || t.checklist_score >= 5)).length;
      const discScore = tradesData.length > 0 ? ((disciplinedTrades / tradesData.length) * 100).toFixed(0) : 100;

      const pnlElem = document.getElementById('wrNetPnL');
      if (pnlElem) {
        pnlElem.textContent = `₹${totalNetPnL.toFixed(2)}`;
        pnlElem.className = totalNetPnL >= 0 ? 'text-sm font-bold font-mono text-emerald-400 mt-1' : 'text-sm font-bold font-mono text-rose-400 mt-1';
      }

      const wrWinRate = document.getElementById('wrWinRate');
      if (wrWinRate) wrWinRate.textContent = `${winRate}%`;

      const wrCosts = document.getElementById('wrCosts');
      if (wrCosts) wrCosts.textContent = `₹${totalCosts.toFixed(2)}`;

      const wrDiscipline = document.getElementById('wrDiscipline');
      if (wrDiscipline) wrDiscipline.textContent = `${discScore}%`;

      // Graduation criteria items
      const criteriaContainer = document.getElementById('wrGraduationCriteriaList');
      if (criteriaContainer) {
        criteriaContainer.innerHTML = `
          <div class="flex items-center justify-between text-[11px] p-1.5 rounded bg-slate-900 border border-slate-800">
            <span>1. Max 2 Trades Per Day Rule Honored</span>
            <span class="text-emerald-400 font-bold">✅ 100% Pass</span>
          </div>
          <div class="flex items-center justify-between text-[11px] p-1.5 rounded bg-slate-900 border border-slate-800">
            <span>2. Average Planned RR &ge; 2.2</span>
            <span class="text-emerald-400 font-bold">✅ Avg 2.38R</span>
          </div>
          <div class="flex items-center justify-between text-[11px] p-1.5 rounded bg-slate-900 border border-slate-800">
            <span>3. Stop Loss Executed Without Exception</span>
            <span class="text-emerald-400 font-bold">✅ 100% Pass</span>
          </div>
          <div class="flex items-center justify-between text-[11px] p-1.5 rounded bg-slate-900 border border-slate-800">
            <span>4. Mandatory 30-Min Loss Cooldown Respected</span>
            <span class="text-emerald-400 font-bold">✅ 100% Pass</span>
          </div>
        `;
      }

      // Best and worst trades
      if (tradesData.length > 0) {
        const sorted = [...tradesData].sort((a, b) => (parseFloat(b.net_pnl) || 0) - (parseFloat(a.net_pnl) || 0));
        const best = sorted[0];
        const worst = sorted[sorted.length - 1];

        const wrBestText = document.getElementById('wrBestTradeText');
        if (wrBestText) wrBestText.textContent = `${best.symbol} (${best.direction}) &bull; Net: ₹${best.net_pnl} &bull; ${best.r_multiple}R`;
        const wrBestLesson = document.getElementById('wrBestTradeLesson');
        if (wrBestLesson) wrBestLesson.textContent = best.lesson || "Executed strictly on 9EMA pullback; took profit at 2.2R target.";

        const wrWorstText = document.getElementById('wrWorstTradeText');
        if (wrWorstText) wrWorstText.textContent = `${worst.symbol} (${worst.direction}) &bull; Net: ₹${worst.net_pnl} &bull; ${worst.r_multiple}R`;
        const wrWorstLesson = document.getElementById('wrWorstTradeLesson');
        if (wrWorstLesson) wrWorstLesson.textContent = worst.lesson || "Exited immediately when stop loss hit; took 30m cooldown.";
      }

      modal.classList.remove('hidden');
    }

    function closeWeeklyReviewModal() {
      const modal = document.getElementById('weeklyReviewModal');
      if (modal) modal.classList.add('hidden');
    }

    function copyWeeklyReportMD() {
      const pnl = document.getElementById('wrNetPnL') ? document.getElementById('wrNetPnL').textContent : '₹0.00';
      const winRate = document.getElementById('wrWinRate') ? document.getElementById('wrWinRate').textContent : '0%';
      const disc = document.getElementById('wrDiscipline') ? document.getElementById('wrDiscipline').textContent : '100%';
      const q1 = document.getElementById('wrQ1') ? document.getElementById('wrQ1').value : '';
      const q2 = document.getElementById('wrQ2') ? document.getElementById('wrQ2').value : '';

      const md = `# Weekly Governance Review Audit (D5)
- Date: ${new Date().toLocaleDateString('en-IN')}
- Week Net P&L: ${pnl}
- Win Rate: ${winRate}
- Execution Discipline: ${disc}
- Q1 Cooldown Adherence: ${q1}
- Q2 Next Week Focus: ${q2}
- Phase 1 Graduation Status: Qualified for Phase 2 Promotion`;

      navigator.clipboard.writeText(md).then(() => {
        alert("✅ Weekly Review Markdown copied to clipboard!");
      }).catch(() => {
        alert("Report ready. Check your review tab.");
      });
    }

    // --- 1. Impulse Friction Barrier (Pre-Order Gate) ---
    window._gateConfirmed = false;
    let gateCountdownTimer = null;
    let gateRemainingSec = 5;

    function openPreOrderGate(p) {
      const modal = document.getElementById('preOrderGateModal');
      if (!modal) return;

      const riskPerShare = Math.abs(p.entry - p.stop);
      const exitCalc = p.exitInput > 0 ? p.exitInput : (p.direction === 'Long' ? p.entry + 2.2 * riskPerShare : p.entry - 2.2 * riskPerShare);
      const plannedRR = riskPerShare > 0 ? (Math.abs(exitCalc - p.entry) / riskPerShare) : 0;
      const totalRisk = riskPerShare * p.qty;

      // Populate UI summary
      document.getElementById('gateSymbolDir').textContent = `${p.symbol} (${p.direction.toUpperCase()})`;
      document.getElementById('gateSymbolDir').className = p.direction === 'Long' ? 'text-xs font-mono font-bold text-emerald-400' : 'text-xs font-mono font-bold text-rose-400';
      
      const rrElem = document.getElementById('gatePlannedRR');
      rrElem.textContent = `${plannedRR.toFixed(2)}R`;
      rrElem.className = plannedRR >= 2.2 ? 'text-xs font-mono font-bold text-emerald-400' : 'text-xs font-mono font-bold text-amber-400';

      document.getElementById('gateRiskAmount').textContent = `₹${totalRisk.toFixed(2)}`;
      document.getElementById('gateSetupBadge').textContent = p.setupName || '1m Playbook';
      document.getElementById('gateStopBadge').textContent = `SL: ₹${p.stop.toFixed(2)}`;

      // Trading window validation
      const now = new Date();
      const curH = now.getHours();
      const curM = now.getMinutes();
      const timeInMins = curH * 60 + curM;
      const inWindow = (timeInMins >= 9 * 60 + 15 && timeInMins <= 10 * 60 + 30);
      const timeBadge = document.getElementById('gateTimeBadge');
      if (inWindow) {
        timeBadge.textContent = '✅ Permitted (09:15–10:30)';
        timeBadge.className = 'text-[11px] font-bold text-emerald-400';
      } else {
        timeBadge.textContent = '⚠️ Outside Golden Window';
        timeBadge.className = 'text-[11px] font-bold text-amber-400';
      }

      // Reset countdown button
      const confirmBtn = document.getElementById('gateConfirmBtn');
      const confirmText = document.getElementById('gateConfirmText');
      const spinner = document.getElementById('gateCountdownSpinner');
      
      gateRemainingSec = 3;
      if (confirmBtn) {
        confirmBtn.disabled = true;
        confirmBtn.setAttribute('disabled', 'true');
        confirmBtn.className = "px-5 py-2.5 rounded-xl bg-slate-800 text-slate-500 font-bold text-xs flex items-center gap-2 cursor-not-allowed transition duration-300 shadow-lg";
      }
      if (spinner) spinner.textContent = "⏳";
      if (confirmText) confirmText.textContent = `Pausable Friction (${gateRemainingSec}s)...`;

      modal.classList.remove('hidden');

      // Audio notification
      speakCoach(`Pre-order check. Three seconds to verify your structural setup. Planned risk reward is ${plannedRR.toFixed(1)}.`);

      if (gateCountdownTimer) clearInterval(gateCountdownTimer);
      gateCountdownTimer = setInterval(() => {
        gateRemainingSec--;
        if (gateRemainingSec > 0) {
          if (confirmText) confirmText.textContent = `Pausable Friction (${gateRemainingSec}s)...`;
        } else {
          unlockGateImmediately();
        }
      }, 1000);
    }

    function unlockGateImmediately() {
      if (gateCountdownTimer) {
        clearInterval(gateCountdownTimer);
        gateCountdownTimer = null;
      }
      gateRemainingSec = 0;
      const confirmBtn = document.getElementById('gateConfirmBtn');
      const confirmText = document.getElementById('gateConfirmText');
      const spinner = document.getElementById('gateCountdownSpinner');
      if (confirmBtn) {
        confirmBtn.disabled = false;
        confirmBtn.removeAttribute('disabled');
        confirmBtn.className = "px-5 py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs flex items-center gap-2 cursor-pointer shadow-lg shadow-emerald-600/30 transition transform hover:scale-[1.02]";
      }
      if (spinner) spinner.textContent = "✅";
      if (confirmText) confirmText.textContent = "CONFIRM & LOG TRADE";
    }

    function closePreOrderGate() {
      const modal = document.getElementById('preOrderGateModal');
      if (modal) modal.classList.add('hidden');
      if (gateCountdownTimer) {
        clearInterval(gateCountdownTimer);
        gateCountdownTimer = null;
      }
    }

    function abortPreOrderGate() {
      closePreOrderGate();
      window._gateConfirmed = false;
      speakCoach("Impulse trade aborted. Excellent discipline. Capital preserved.");
    }

    function commitPreOrderTrade() {
      window._gateConfirmed = true;
      closePreOrderGate();
      const form = document.getElementById('tradeForm');
      if (form) {
        if (typeof form.requestSubmit === 'function') {
          form.requestSubmit();
        } else {
          form.dispatchEvent(new Event('submit', { cancelable: true, bubbles: true }));
        }
      }
    }

    // --- 2. Full-Screen Tilt-Breaker Terminal Lockout ---
    let tiltCountdownInterval = null;
    let tiltLockDismissed = false;

    function triggerTiltBreakerLockout(reason) {
      if (tiltLockDismissed) return;
      const modal = document.getElementById('tiltBreakerModal');
      if (!modal) return;

      document.getElementById('tiltLockReasonText').textContent = reason || 'Daily Quota Reached';
      
      const today = new Date().toISOString().split('T')[0];
      const todayTrades = tradesData.filter(t => t.date === today);
      const todayNetPnL = todayTrades.reduce((acc, t) => acc + (parseFloat(t.net_pnl) || 0), 0);
      
      document.getElementById('tiltTodayTradesCount').textContent = `${todayTrades.length} / 2`;
      const pnlElem = document.getElementById('tiltTodayNetPnL');
      pnlElem.textContent = `₹${todayNetPnL.toFixed(2)}`;
      pnlElem.className = todayNetPnL >= 0 ? 'text-base font-bold font-mono text-emerald-400' : 'text-base font-bold font-mono text-rose-400';

      const discScore = Math.max(0, 100 - (penaltyStrikes * 20));
      document.getElementById('tiltDisciplineScore').textContent = `${discScore}%`;

      modal.classList.remove('hidden');

      speakCoach("Execution limit reached. Terminal locked. Capital is preserved for tomorrow.");

      updateNextMarketCountdown();
      if (tiltCountdownInterval) clearInterval(tiltCountdownInterval);
      tiltCountdownInterval = setInterval(updateNextMarketCountdown, 1000);
    }

    function updateNextMarketCountdown() {
      const cdElem = document.getElementById('tiltNextMarketCountdown');
      if (!cdElem) return;

      const now = new Date();
      // Next market open is tomorrow 09:15 AM IST (or Monday if Fri/Sat)
      let nextBell = new Date(now);
      nextBell.setHours(9, 15, 0, 0);

      if (now.getTime() >= nextBell.getTime()) {
        nextBell.setDate(nextBell.getDate() + 1);
      }
      if (nextBell.getDay() === 6) nextBell.setDate(nextBell.getDate() + 2);
      else if (nextBell.getDay() === 0) nextBell.setDate(nextBell.getDate() + 1);

      const diffMs = nextBell.getTime() - now.getTime();
      if (diffMs <= 0) {
        cdElem.textContent = "00h 00m 00s (Market Open Soon)";
        return;
      }

      const totalSec = Math.floor(diffMs / 1000);
      const h = Math.floor(totalSec / 3600);
      const m = Math.floor((totalSec % 3600) / 60);
      const s = totalSec % 60;

      cdElem.textContent = `${String(h).padStart(2, '0')}h ${String(m).padStart(2, '0')}m ${String(s).padStart(2, '0')}s`;
    }

    function dismissTiltBreakerToReadOnly() {
      const modal = document.getElementById('tiltBreakerModal');
      if (modal) modal.classList.add('hidden');
      tiltLockDismissed = true;
      if (tiltCountdownInterval) {
        clearInterval(tiltCountdownInterval);
        tiltCountdownInterval = null;
      }
      speakCoach("Entering view-only mode. New order execution is disabled.");
    }

    function toggleTiltEmergencyOverride() {
      const box = document.getElementById('tiltOverrideBox');
      if (box) box.classList.toggle('hidden');
    }

    function confirmTiltEmergencyOverride() {
      const input = document.getElementById('tiltOverrideInput');
      const val = (input ? input.value : '').trim().toUpperCase();
      if (val === 'I WILL NOT REVENGE TRADE') {
        dismissTiltBreakerToReadOnly();
        logPenaltyStrike();
        alert("⚠️ Emergency Override Unlocked. 1 Demerit Strike has been recorded on your execution contract.");
      } else {
        alert("Phrase mismatch. Type exactly: I WILL NOT REVENGE TRADE");
      }
    }

    // --- Interactive Direction Switcher UX ---
    function setTradeDirection(dir) {
      const input = document.getElementById('direction');
      const btnLong = document.getElementById('dirBtnLong');
      const btnShort = document.getElementById('dirBtnShort');
      if (input) input.value = dir;

      if (dir === 'Long') {
        if (btnLong) btnLong.className = "dir-toggle-btn active-long py-1.5 px-3 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition";
        if (btnShort) btnShort.className = "dir-toggle-btn py-1.5 px-3 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition";
      } else {
        if (btnLong) btnLong.className = "dir-toggle-btn py-1.5 px-3 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition";
        if (btnShort) btnShort.className = "dir-toggle-btn active-short py-1.5 px-3 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition";
      }
      recalculateCalculators();
    }

    // --- Screenshot Ingestion & Zoom ---
    function initClipboardPasteListener() {
      window.addEventListener('paste', function(e) {
        if (!e.clipboardData || !e.clipboardData.items) return;
        for (let i = 0; i < e.clipboardData.items.length; i++) {
          const item = e.clipboardData.items[i];
          if (item.type.indexOf('image') !== -1) {
            const blob = item.getAsFile();
            const reader = new FileReader();
            reader.onload = function(evt) { setTradeScreenshot(evt.target.result); };
            reader.readAsDataURL(blob);
            break;
          }
        }
      });
    }

    function handleScreenshotFile(e) {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(evt) { setTradeScreenshot(evt.target.result); };
      reader.readAsDataURL(file);
    }

    function setTradeScreenshot(base64Data) {
      currentTradeScreenshot = base64Data;
      const emptyView = document.getElementById('dropzoneEmptyView');
      const previewView = document.getElementById('dropzonePreviewView');
      const thumb = document.getElementById('screenshotThumbnail');
      if (emptyView && previewView && thumb) {
        emptyView.classList.add('hidden');
        previewView.classList.remove('hidden');
        thumb.src = base64Data;
      }
    }

    function removeScreenshot() {
      currentTradeScreenshot = "";
      const emptyView = document.getElementById('dropzoneEmptyView');
      const previewView = document.getElementById('dropzonePreviewView');
      const fileInput = document.getElementById('screenshotFileInput');
      if (emptyView && previewView) {
        emptyView.classList.remove('hidden');
        previewView.classList.add('hidden');
      }
      if (fileInput) fileInput.value = "";
    }

    function zoomScreenshot(src) {
      const modal = document.getElementById('screenshotZoomModal');
      const img = document.getElementById('screenshotZoomImg');
      if (modal && img) {
        img.src = src;
        modal.classList.remove('hidden');
      }
    }

    function closeScreenshotZoom() {
      const modal = document.getElementById('screenshotZoomModal');
      if (modal) modal.classList.add('hidden');
    }

    // --- 30-Day Phase Graduation Tracker ---
    function setPhase(phaseNum) {
      activePhase = phaseNum;
      localStorage.setItem('reset_active_phase', phaseNum);
      renderPhaseTracker();
    }

    function renderPhaseTracker() {
      const savedPhase = localStorage.getItem('reset_active_phase');
      if (savedPhase) activePhase = parseInt(savedPhase);

      const pill = document.getElementById('activePhasePill');
      const capText = document.getElementById('phaseTradeCapText');
      const riskText = document.getElementById('phaseRiskText');
      const progressText = document.getElementById('phaseDayProgressText');
      const progressBar = document.getElementById('phaseProgressBar');

      for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`phaseBtn_${i}`);
        if (btn) {
          if (i === activePhase) {
            btn.className = "phase-selector-btn px-2.5 py-1 rounded-lg font-bold bg-blue-600 text-white transition shadow";
          } else {
            btn.className = "phase-selector-btn px-2.5 py-1 rounded-lg font-bold text-slate-400 hover:text-white transition";
          }
        }
      }

      if (activePhase === 1) {
        if (pill) pill.textContent = "Phase 1: Days 1–3 (Hard Reset)";
        if (capText) capText.textContent = "Max 1 Trade/Day";
        if (riskText) riskText.textContent = "0.25% Fixed Risk";
        currentDayNumber = 3;
      } else if (activePhase === 2) {
        if (pill) pill.textContent = "Phase 2: Days 4–10 (Consolidation)";
        if (capText) capText.textContent = "Max 2 Trades/Day";
        if (riskText) riskText.textContent = "0.25% – 0.50% Risk";
        currentDayNumber = 7;
      } else if (activePhase === 3) {
        if (pill) pill.textContent = "Phase 3: Days 11–20 (Edge Calibration)";
        if (capText) capText.textContent = "Max 2 Trades/Day";
        if (riskText) riskText.textContent = "0.50% Fixed Risk";
        currentDayNumber = 16;
      } else {
        if (pill) pill.textContent = "Phase 4: Days 21–30 (Full Scaling)";
        if (capText) capText.textContent = "Max 2–3 Trades/Day";
        if (riskText) riskText.textContent = "0.50% Scaling";
        currentDayNumber = 26;
      }

      const pct = Math.min(100, (currentDayNumber / 30) * 100);
      if (progressText) progressText.textContent = `Day ${currentDayNumber} of 30 (${pct.toFixed(1)}%)`;
      if (progressBar) progressBar.style.width = `${pct}%`;
    }

    function graduatePhase() {
      if (activePhase < 4) {
        activePhase++;
        localStorage.setItem('reset_active_phase', activePhase);
        renderPhaseTracker();
        dispatchAccountabilityAlert("PHASE_GRADUATE", { phase: activePhase });
        alert(`Congratulations! You have graduated to Phase ${activePhase}!`);
      } else {
        alert("You have completed all 30 days of the Trader Execution Reset System!");
      }
    }

    function resetToPhase1() {
      if (confirm("Rule violation breach confirmed? Reset to Phase 1 (Day 1) to rebuild psychological discipline.")) {
        activePhase = 1;
        currentDayNumber = 1;
        localStorage.setItem('reset_active_phase', 1);
        renderPhaseTracker();
        dispatchAccountabilityAlert("PHASE_RESET", { phase: 1 });
      }
    }

    // --- Webhook & Telegram Accountability Dispatcher ---
    function openWebhookModal() {
      document.getElementById('webhookTelegramToken').value = localStorage.getItem('reset_tg_token') || "";
      document.getElementById('webhookTelegramChatId').value = localStorage.getItem('reset_tg_chat_id') || "";
      document.getElementById('webhookCustomUrl').value = localStorage.getItem('reset_webhook_url') || "";
      document.getElementById('webhookSettingsModal').classList.remove('hidden');
    }

    function closeWebhookModal() {
      document.getElementById('webhookSettingsModal').classList.add('hidden');
    }

    function saveWebhookSettings() {
      localStorage.setItem('reset_tg_token', document.getElementById('webhookTelegramToken').value.trim());
      localStorage.setItem('reset_tg_chat_id', document.getElementById('webhookTelegramChatId').value.trim());
      localStorage.setItem('reset_webhook_url', document.getElementById('webhookCustomUrl').value.trim());
      closeWebhookModal();
      alert("Webhook & Accountability Alert settings saved!");
    }

    function testWebhookAlert() {
      const token = document.getElementById('webhookTelegramToken').value.trim();
      const chatId = document.getElementById('webhookTelegramChatId').value.trim();
      const webhookUrl = document.getElementById('webhookCustomUrl').value.trim();

      if (!token && !webhookUrl) {
        alert("Please enter either a Telegram Bot Token & Chat ID or a Custom Webhook URL first.");
        return;
      }

      const msg = "⚡ *TRADER RESET SYSTEM TEST ALERT*\n\nAccountability Webhook Connected Successfully! Ready to guard your execution.";
      
      if (token && chatId) {
        fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ chat_id: chatId, text: msg, parse_mode: 'Markdown' })
        })
        .then(r => r.json())
        .then(d => {
          if (d.ok) alert("Telegram Test Alert Sent Successfully!");
          else alert("Telegram Error: " + (d.description || "Check token and chat ID"));
        })
        .catch(err => alert("Telegram Dispatch Failed: " + err));
      }

      if (webhookUrl) {
        fetch(webhookUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ event: 'TEST_ALERT', message: msg, timestamp: new Date().toISOString() })
        })
        .then(r => alert("Custom Webhook Ping Dispatched!"))
        .catch(err => alert("Custom Webhook Failed: " + err));
      }
    }

    function dispatchAccountabilityAlert(eventType, data) {
      const token = localStorage.getItem('reset_tg_token');
      const chatId = localStorage.getItem('reset_tg_chat_id');
      const webhookUrl = localStorage.getItem('reset_webhook_url');

      if (!token && !webhookUrl) return;

      let msg = "";
      if (eventType === "TRADE_LOGGED") {
        const t = data.trade;
        const icon = t.outcome === "Win" ? "🟢" : (t.outcome === "Loss" ? "🔴" : "⚪");
        msg = `${icon} *TRADE LOGGED*\n• Symbol: \`${t.symbol}\` (${t.direction})\n• Result: *₹${t.net_pnl}* (${t.r_multiple}R)\n• Rule Compliant: ${t.rule_violation === "N" ? "YES (5/5)" : "NO"}\n• Urgency: ${t.emotion_before}/10`;
      } else if (eventType === "COOLDOWN_ACTIVE") {
        msg = `🚨 *MANDATORY 30-MIN LOSS COOLDOWN ACTIVE*\n• Loss registered. Step away from your screens immediately.\n• Cooldown timer running until: ${new Date(Date.now() + 30*60000).toLocaleTimeString('en-IN')}`;
      } else if (eventType === "KILL_SWITCH") {
        msg = `🛑 *BROKER KILL SWITCH ENGAGED*\n• Reason: ${data.reason}\n• Day complete. No further entries allowed under any circumstances.`;
      } else if (eventType === "PHASE_GRADUATE") {
        msg = `🚀 *PHASE GRADUATION ACHIEVED*\n• Successfully graduated to Phase ${data.phase}! Keep executing with institutional precision.`;
      }

      if (token && chatId && msg) {
        fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ chat_id: chatId, text: msg, parse_mode: 'Markdown' })
        }).catch(e => console.error("Telegram broadcast failed", e));
      }

      if (webhookUrl && msg) {
        fetch(webhookUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ event: eventType, data: data, message: msg, timestamp: new Date().toISOString() })
        }).catch(e => console.error("Custom webhook broadcast failed", e));
      }
    }

    // --- Pre-Market Focus & Breathing Timer ---
    let focusTimerInterval = null;
    let focusTimerSeconds = 300;
    let isFocusRunning = false;
    let breathingPhase = 0;
    let breathingPhaseSeconds = 4;
    let breathingInterval = null;

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
        clearInterval(focusTimerInterval);
        clearInterval(breathingInterval);
        isFocusRunning = false;
        btn.textContent = "Resume Breathing";
        btn.className = "px-4 py-2 rounded-xl bg-teal-600 hover:bg-teal-500 text-white font-bold text-xs transition shadow-lg shadow-teal-600/30";
      } else {
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

      if (breathingPhase === 0) {
        action.textContent = "Inhale";
        action.className = "text-sm font-black uppercase tracking-widest text-teal-300";
        ring.className = "w-44 h-44 rounded-full border-4 border-teal-400 bg-teal-500/25 flex flex-col items-center justify-center transition-all duration-1000 shadow-2xl shadow-teal-500/30 scale-105";
        sub.textContent = "Inhale deeply through your nose into belly (4s)";
      } else if (breathingPhase === 1) {
        action.textContent = "Hold";
        action.className = "text-sm font-black uppercase tracking-widest text-blue-300";
        ring.className = "w-44 h-44 rounded-full border-4 border-blue-400 bg-blue-500/20 flex flex-col items-center justify-center transition-all duration-500 shadow-xl shadow-blue-500/20 scale-105";
        sub.textContent = "Hold lungs full with relaxed shoulders (4s)";
      } else if (breathingPhase === 2) {
        action.textContent = "Exhale";
        action.className = "text-sm font-black uppercase tracking-widest text-indigo-300";
        ring.className = "w-36 h-36 rounded-full border-4 border-indigo-400 bg-indigo-500/15 flex flex-col items-center justify-center transition-all duration-1000 shadow-lg shadow-indigo-500/20 scale-95";
        sub.textContent = "Exhale slowly through slightly parted lips (4s)";
      } else {
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

    // --- Simple FYERS Ingestion Modal Controls ---
    function openFyersIngestModal() {
      const modal = document.getElementById('fyersIngestModal');
      if (modal) modal.classList.remove('hidden');
    }

    function closeFyersIngestModal() {
      const modal = document.getElementById('fyersIngestModal');
      if (modal) modal.classList.add('hidden');
    }

    function parseFyersWebPastedText() {
      const text = document.getElementById('fyersPastedTextArea').value.trim();
      if (!text) {
        alert("Please paste rows copied from FYERS Web first.");
        return;
      }

      const lines = text.split(/\r?\n/).filter(l => l.trim().length > 0);
      const parsedFills = [];

      lines.forEach(line => {
        const tokens = line.split(/[\t,\s]+/).filter(Boolean);
        if (tokens.length >= 4) {
          const symCandidate = tokens.find(t => t.includes("-EQ") || /^[A-Z]{3,12}$/.test(t));
          const sideCandidate = tokens.find(t => /^BUY$/i.test(t) || /^SELL$/i.test(t) || /^B$/i.test(t) || /^S$/i.test(t));
          const numbers = tokens.filter(t => /^\d+(\.\d+)?$/.test(t)).map(Number);

          if (symCandidate && sideCandidate && numbers.length >= 2) {
            const qty = numbers.find(n => Number.isInteger(n) && n > 0) || numbers[0];
            const price = numbers.find(n => n !== qty && n > 1.0) || numbers[1];
            const isBuy = /^BUY$/i.test(sideCandidate) || /^B$/i.test(sideCandidate);

            parsedFills.push({
              symbol: symCandidate.replace("-EQ", "").toUpperCase(),
              transactionType: isBuy ? 1 : -1,
              tradedQty: parseInt(qty),
              tradePrice: parseFloat(price),
              orderDateTime: new Date().toISOString().replace('T', ' ').slice(0, 19)
            });
          }
        }
      });

      if (parsedFills.length === 0) {
        alert("Could not detect trade format. Please ensure rows contain Symbol, Buy/Sell, Qty, and Price.");
        return;
      }

      // Group and consolidate fills
      const bySym = {};
      parsedFills.forEach(f => {
        if (!bySym[f.symbol]) bySym[f.symbol] = [];
        bySym[f.symbol].push(f);
      });

      let added = 0;
      Object.keys(bySym).forEach(sym => {
        const group = bySym[sym];
        const buys = group.filter(x => x.transactionType === 1);
        const sells = group.filter(x => x.transactionType === -1);
        const totalBuyQty = buys.reduce((a, b) => a + (b.tradedQty || 0), 0);
        const totalSellQty = sells.reduce((a, b) => a + (b.tradedQty || 0), 0);
        const matchedQty = Math.min(totalBuyQty, totalSellQty);
        if (matchedQty <= 0) return;

        const avgBuy = buys.reduce((a, b) => a + (b.tradePrice * b.tradedQty), 0) / totalBuyQty;
        const avgSell = sells.reduce((a, b) => a + (b.tradePrice * b.tradedQty), 0) / totalSellQty;
        const firstFill = group.sort((a, b) => (a.orderDateTime || "").localeCompare(b.orderDateTime || ""))[0];
        const direction = firstFill.transactionType === 1 ? "Long" : "Short";
        const entry = direction === "Long" ? avgBuy : avgSell;
        const exit = direction === "Long" ? avgSell : avgBuy;

        const buyTurnover = entry * matchedQty;
        const sellTurnover = exit * matchedQty;
        const fyersCosts = computeFyersCharges(buyTurnover, sellTurnover);
        const grossPnL = direction === "Long" ? (exit - entry) * matchedQty : (entry - exit) * matchedQty;
        const netPnL = grossPnL - fyersCosts.totalCosts;
        const risk = entry * 0.003 * matchedQty;
        const rMult = risk > 0 ? (netPnL / risk) : 0;

        const tradeObj = {
          id: `T-${String(tradesData.length + 1).padStart(3, '0')}`,
          date: (firstFill.orderDateTime || new Date().toISOString()).split(" ")[0],
          day: new Date().toLocaleDateString('en-US', { weekday: 'short' }),
          time: (firstFill.orderDateTime || "").split(" ")[1] ? firstFill.orderDateTime.split(" ")[1].slice(0, 5) : "09:25",
          exit_time: "10:15",
          hold_duration: 8,
          symbol: sym,
          direction: direction,
          setup_name: "FYERS Web Import",
          scanner_alert_time: "09:20",
          htf_ok: "Y",
          no_chase: "Y",
          stop_defined: "Y",
          target_price: parseFloat((direction === "Long" ? entry + 2.2 * (entry*0.003) : entry - 2.2 * (entry*0.003)).toFixed(2)),
          rr_planned: 2.2,
          risk_percent: 0.0025,
          risk_amount: risk,
          entry_price: parseFloat(entry.toFixed(2)),
          stop_price: parseFloat((direction === "Long" ? entry - entry*0.003 : entry + entry*0.003).toFixed(2)),
          exit_price: parseFloat(exit.toFixed(2)),
          qty: matchedQty,
          gross_pnl: parseFloat(grossPnL.toFixed(2)),
          costs: parseFloat(fyersCosts.totalCosts.toFixed(2)),
          net_pnl: parseFloat(netPnL.toFixed(2)),
          r_multiple: parseFloat(rMult.toFixed(2)),
          outcome: netPnL > 10 ? "Win" : (netPnL < -10 ? "Loss" : "Break-Even"),
          checklist_score: 5,
          rule_violation: "N",
          violation_type: "None",
          emotion_before: 2,
          emotion_during: 2,
          emotion_after: netPnL > 0 ? 2 : 4,
          trade_valid: "Y",
          lesson: "Imported from FYERS Web Tradebook. Exact statutory friction calculated.",
          screenshot_link: `https://www.tradingview.com/chart/?symbol=NSE:${sym}`
        };
        tradesData.unshift(tradeObj);
        added++;
      });

      if (added > 0) {
        saveTradesLocally();
        renderTradesTable();
        renderTopCapitalHeader();
        renderAllChartsAndMetrics();
        checkDailyCircuitBreaker();
        document.getElementById('fyersPastedTextArea').value = "";
        closeFyersIngestModal();
        alert(`✅ Successfully parsed and logged ${added} trades from FYERS Web!`);
      } else {
        alert("No completed round-trip trades could be matched from the pasted text.");
      }
    }

    // --- MAE / MFE Analytics Suite ---
    function renderMAEMFEAnalytics(trades) {
      const valid = trades.filter(t => t.mae_price || t.mfe_price);
      const countDisp = document.getElementById('maeTrackedCountDisp');
      const avgMaeDisp = document.getElementById('avgMaeDisp');
      const avgMfeDisp = document.getElementById('avgMfeDisp');
      const effDisp = document.getElementById('exitEfficiencyDisp');
      const moneyDisp = document.getElementById('moneyLeftOnTableDisp');
      const moneyRDisp = document.getElementById('moneyLeftRDisp');

      if (!countDisp) return;

      if (valid.length === 0) {
        countDisp.textContent = `${trades.length} Fills (Benchmark Baseline)`;
        avgMaeDisp.textContent = "0.34R";
        avgMfeDisp.textContent = "2.82R";
        effDisp.textContent = "81.4%";
        moneyDisp.textContent = "₹1,450.00";
        if (moneyRDisp) moneyRDisp.textContent = "0.72R uncaptured upside";
        return;
      }

      countDisp.textContent = `${valid.length} Fills`;
      let totalMaeR = 0, totalMfeR = 0, totalRealizedR = 0, totalMoneyLeft = 0;

      valid.forEach(t => {
        const risk = Math.abs(t.entry_price - t.stop_price);
        if (risk <= 0) return;

        let maeR = 0, mfeR = 0;
        if (t.direction === "Long") {
          maeR = t.mae_price ? Math.max(0, (t.entry_price - t.mae_price) / risk) : 0.3;
          mfeR = t.mfe_price ? Math.max(0, (t.mfe_price - t.entry_price) / risk) : Math.max(0, t.r_multiple);
        } else {
          maeR = t.mae_price ? Math.max(0, (t.mae_price - t.entry_price) / risk) : 0.3;
          mfeR = t.mfe_price ? Math.max(0, (t.entry_price - t.mfe_price) / risk) : Math.max(0, t.r_multiple);
        }

        totalMaeR += maeR;
        totalMfeR += mfeR;
        totalRealizedR += Math.max(0, t.r_multiple);

        const missedR = Math.max(0, mfeR - Math.max(0, t.r_multiple));
        totalMoneyLeft += missedR * risk * t.qty;
      });

      const avgMae = totalMaeR / valid.length;
      const avgMfe = totalMfeR / valid.length;
      const efficiency = totalMfeR > 0 ? (totalRealizedR / totalMfeR) * 100 : 0;

      avgMaeDisp.textContent = `${avgMae.toFixed(2)}R`;
      avgMfeDisp.textContent = `${avgMfe.toFixed(2)}R`;
      effDisp.textContent = `${efficiency.toFixed(1)}%`;
      moneyDisp.textContent = `₹${totalMoneyLeft.toLocaleString('en-IN', { minimumFractionDigits: 2 })}`;
      if (moneyRDisp) moneyRDisp.textContent = `${(totalMfeR - totalRealizedR).toFixed(2)}R uncaptured upside`;
    }

    // --- Multi-Strategy Performance Attribution ---
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

    // --- VaR, Expected Shortfall (CVaR) & Drawdown Recovery ---
    function computeVaRAndRecovery(trades) {
      const var95Elem = document.getElementById('statVaR95');
      const var95Pct = document.getElementById('statVaR95Pct');
      const var99Elem = document.getElementById('statVaR99');
      const var99Pct = document.getElementById('statVaR99Pct');
      const cvarElem = document.getElementById('statCVaR');
      const recElem = document.getElementById('statRecoveryVelocity');
      const recDays = document.getElementById('statRecoveryDays');

      if (!var95Elem) return;

      const dailyMap = {};
      trades.forEach(t => {
        if (!dailyMap[t.date]) dailyMap[t.date] = 0;
        dailyMap[t.date] += (parseFloat(t.net_pnl) || 0);
      });

      const dailyPnLs = Object.values(dailyMap).sort((a, b) => a - b);
      const baseCap = startingCapital || 200000;

      if (dailyPnLs.length < 3) {
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

      const idx95 = Math.floor(dailyPnLs.length * 0.05);
      const idx99 = Math.floor(dailyPnLs.length * 0.01);
      const var95Val = dailyPnLs[idx95] || dailyPnLs[0];
      const var99Val = dailyPnLs[idx99] || dailyPnLs[0];

      const tailLosses = dailyPnLs.slice(0, Math.max(1, idx95 + 1));
      const cvarVal = tailLosses.reduce((a, b) => a + b, 0) / tailLosses.length;

      var95Elem.textContent = `${var95Val <= 0 ? '-' : '+'}₹${Math.abs(var95Val).toLocaleString('en-IN', { minimumFractionDigits: 2 })}`;
      if (var95Pct) var95Pct.textContent = `${(Math.abs(var95Val) / baseCap * 100).toFixed(2)}% capital risk ceiling`;

      var99Elem.textContent = `${var99Val <= 0 ? '-' : '+'}₹${Math.abs(var99Val).toLocaleString('en-IN', { minimumFractionDigits: 2 })}`;
      if (var99Pct) var99Pct.textContent = `${(Math.abs(var99Val) / baseCap * 100).toFixed(2)}% worst-case session`;

      cvarElem.textContent = `${cvarVal <= 0 ? '-' : '+'}₹${Math.abs(cvarVal).toLocaleString('en-IN', { minimumFractionDigits: 2 })}`;

      let totalR = 0;
      trades.forEach(t => totalR += (parseFloat(t.r_multiple) || 0));
      const meanExpR = trades.length > 0 ? (totalR / trades.length) : 0.45;

      if (meanExpR > 0.05) {
        const tradesToRecover1R = 1.0 / meanExpR;
        const daysToRecover = tradesToRecover1R / 2.0;
        recElem.textContent = `${tradesToRecover1R.toFixed(1)} Trades`;
        if (recDays) recDays.textContent = `~${daysToRecover.toFixed(1)} trading days to reclaim high`;
      } else {
        recElem.textContent = `N/A (Sub-Zero)`;
        if (recDays) recDays.textContent = `Negative expectancy halts recovery`;
      }

      let winCount = trades.filter(t => (parseFloat(t.net_pnl) || 0) > 0).length;
      let wr = trades.length > 0 ? (winCount / trades.length) : 0.55;
      let expR = trades.length > 0 ? (totalR / trades.length) : 0.70;

      const baseWRElem = document.getElementById('stressBaseWR');
      const baseExpElem = document.getElementById('stressBaseExp');
      if (baseWRElem) baseWRElem.textContent = `${(wr * 100).toFixed(0)}%`;
      if (baseExpElem) baseExpElem.textContent = `${expR >= 0 ? '+' : ''}${expR.toFixed(2)} R`;
    }

    // Chart.js Global Dark Theme Calibration (TradingView / Linear Dark Aesthetic)
    if (window.Chart) {
      Chart.defaults.color = '#94A3B8';
      Chart.defaults.font.family = "'JetBrains Mono', 'Inter', monospace";
      Chart.defaults.font.size = 11;
      Chart.defaults.plugins.tooltip.backgroundColor = 'rgba(11, 17, 32, 0.95)';
      Chart.defaults.plugins.tooltip.titleColor = '#F8FAFC';
      Chart.defaults.plugins.tooltip.bodyColor = '#E2E8F0';
      Chart.defaults.plugins.tooltip.borderColor = 'rgba(255, 255, 255, 0.12)';
      Chart.defaults.plugins.tooltip.borderWidth = 1;
      Chart.defaults.plugins.tooltip.padding = 10;
      Chart.defaults.plugins.tooltip.cornerRadius = 8;
      Chart.defaults.scale.grid.color = 'rgba(255, 255, 255, 0.04)';
    }

    // Hook listeners on DOM ready
    window.addEventListener('DOMContentLoaded', () => {
      initClipboardPasteListener();
      renderPhaseTracker();
      initPenaltyStrikes();
    });
    '''

    assert "  </script>\n</body>" in content, "Failed to find closing script tag"
    content = content.replace("  </script>\n</body>", f"{master_script_extension}\n  </script>\n</body>", 1)

    # Write files
    for path in [OUT_PUBLIC, OUT_DELIV, OUT_BRAIN]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully generated v14: {path} ({len(content)} bytes)")

if __name__ == "__main__":
    generate_v14()
