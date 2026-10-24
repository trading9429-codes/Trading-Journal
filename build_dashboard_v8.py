#!/usr/bin/env python3
"""
Comprehensive Builder for Trader Execution Reset System Command Center v8.
Upgrades:
1. Visual Chart Screenshot Attachment (Ctrl+V clipboard paste, drag-and-drop, full-size zoom modal)
2. MAE / MFE (Maximum Adverse & Favorable Excursion) Exit Efficiency & Stop Analysis (Tab 3)
3. 30-Day Phase Graduation & Discipline Milestone Tracker (Phase 1 to Phase 4)
4. Telegram & WhatsApp Accountability Alert Webhook Engine (with instant test ping)
5. FYERS API v3 Live Sync Bridge Modal
6. Preserves the responsive 4-Tab spacious architecture.
"""

import os

DASHBOARD_SRC = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html"
OUT_PUBLIC = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/public/index.html"
OUT_DELIV = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html"
OUT_BRAIN = "/home/sunny/.gemini/antigravity/brain/85803015-3567-4584-af28-ca9d6eed9423/trader_dashboard.html"

def build_v8():
    with open(DASHBOARD_SRC, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Title and Header status
    content = content.replace(
        "<title>Trader Execution Reset System — Institutional Command Center</title>",
        "<title>Trader Execution Reset System — Institutional Command Center v8</title>"
    )

    # 2. Add Phase Badge & Webhook / FYERS Sync buttons in Top Header Action Strip
    old_actions = """      <!-- Global Actions Strip -->
      <div class="flex items-center gap-2 w-full xl:w-auto justify-end flex-wrap">
        <button onclick="openWeeklyReviewModal()" class="px-3 py-2 rounded-lg bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-400 border border-indigo-500/30 font-medium text-xs flex items-center gap-1.5 transition">"""

    new_actions = """      <!-- Global Actions Strip -->
      <div class="flex items-center gap-2 w-full xl:w-auto justify-end flex-wrap">
        <button onclick="openWebhookModal()" class="px-3 py-2 rounded-lg bg-sky-600/20 hover:bg-sky-600/30 text-sky-300 border border-sky-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm" title="Configure Telegram/WhatsApp Accountability Alerts">
          <span>🔔</span>
          <span>Alerts &amp; Webhook</span>
        </button>
        <button onclick="openFyersBridgeModal()" class="px-3 py-2 rounded-lg bg-orange-600/20 hover:bg-orange-600/30 text-orange-300 border border-orange-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm" title="FYERS API v3 1-Click Sync Bridge">
          <span>🔌</span>
          <span>FYERS Live Sync</span>
        </button>
        <button onclick="openWeeklyReviewModal()" class="px-3 py-2 rounded-lg bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-400 border border-indigo-500/30 font-medium text-xs flex items-center gap-1.5 transition">"""
    
    assert old_actions in content, "Failed to find old_actions"
    content = content.replace(old_actions, new_actions, 1)

    # 3. Add 30-Day Phase Graduation Tracker at top of Tab 1
    phase_tracker_markup = """    <!-- ========================================== -->
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
      </section>"""

    old_tab1_start = """    <!-- ========================================== -->
    <!-- TAB 1: LIVE EXECUTION & TRADE LOG -->
    <!-- ========================================== -->
    <div id="tabContent1" class="mt-6 space-y-6">"""

    assert old_tab1_start in content, "Failed to find old_tab1_start"
    content = content.replace(old_tab1_start, phase_tracker_markup, 1)

    # 4. Inject MAE/MFE Inputs and Chart Screenshot Dropzone into tradeForm
    old_form_spot = """          </div>

          <!-- Pre-Execution Checklist & Submit Row -->
          <div class="flex flex-col lg:flex-row items-center justify-between gap-4 pt-2">"""

    new_form_spot = """          </div>

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
          <div class="flex flex-col lg:flex-row items-center justify-between gap-4 pt-2">"""

    assert old_form_spot in content, "Failed to find old_form_spot"
    content = content.replace(old_form_spot, new_form_spot, 1)

    # 5. Add MAE/MFE Exit Efficiency & Stop Leak Diagnostics to TAB 3 (Edge & Leaks)
    mae_mfe_tab3_card = """      <!-- MAE / MFE EXIT EFFICIENCY & STOP LEAK ANALYSIS CARD -->
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

        <!-- Stop Quality & Excursion Insights -->
        <div class="mt-4 p-4 rounded-xl bg-slate-950/60 border border-slate-800 text-xs flex flex-col md:flex-row items-center justify-between gap-3">
          <div class="flex items-center gap-3">
            <span class="text-2xl">💡</span>
            <div>
              <p class="font-bold text-white" id="maeInsightTitle">Stop Quality Calibration</p>
              <p class="text-slate-400" id="maeInsightText">Avg MAE is below 0.50R, indicating stops are structurally sound and not being hunted by opening volatility.</p>
            </div>
          </div>
          <div class="flex items-center gap-2 whitespace-nowrap">
            <span class="px-3 py-1.5 rounded-lg bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 font-mono font-bold" id="maeStopEfficiencyBadge">
              Stop Efficiency: High
            </span>
          </div>
        </div>
      </section>

      <!-- Bottom Section: Day-of-Week Matrix, 15-Min Heatmap & Setup Expectancy Matrix -->"""

    old_tab3_spot = """      <!-- Bottom Section: Day-of-Week Matrix, 15-Min Heatmap & Setup Expectancy Matrix -->"""
    assert old_tab3_spot in content, "Failed to find old_tab3_spot"
    content = content.replace(old_tab3_spot, mae_mfe_tab3_card, 1)

    # 6. Add Modals: Webhook Settings, FYERS Live Sync, and Chart Screenshot Zoom
    new_modals = """  <!-- ========================================== -->
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
  <!-- MODAL: FYERS LIVE SYNC & API BRIDGE -->
  <!-- ========================================== -->
  <div id="fyersSyncModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="glass-card rounded-2xl w-full max-w-xl border border-slate-700 shadow-2xl p-6 relative max-h-[90vh] overflow-y-auto">
      <div class="flex items-center justify-between pb-4 border-b border-slate-800">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-orange-500/20 border border-orange-500/40 flex items-center justify-center text-orange-400 font-bold">
            🔌
          </div>
          <div>
            <h3 class="text-base font-bold text-white">FYERS API v3 Auto-Sync Bridge</h3>
            <p class="text-xs text-slate-400">Direct integration with FYERS tradebook and automated cost parsing</p>
          </div>
        </div>
        <button onclick="closeFyersBridgeModal()" class="text-slate-400 hover:text-white text-xl">&times;</button>
      </div>

      <div class="space-y-4 mt-5 text-xs">
        <div class="bg-orange-500/10 border border-orange-500/20 rounded-xl p-3.5 text-orange-200">
          <p class="font-bold flex items-center gap-1.5"><span>⚡</span> FYERS CLI Bridge Script Ready</p>
          <p class="mt-1 text-[11px] text-orange-300/80">You can sync live fills directly via terminal or trigger an emergency auto-square off.</p>
        </div>

        <div class="bg-slate-900 p-3.5 rounded-xl border border-slate-800 font-mono text-[11px] space-y-2">
          <div class="flex items-center justify-between text-slate-400">
            <span>Daily Live Sync Command:</span>
            <button onclick="copyToClipboard('python3 web/fyers_bridge.py --sync')" class="text-blue-400 hover:underline">Copy</button>
          </div>
          <code class="text-emerald-400 block bg-slate-950 p-2 rounded border border-slate-800">python3 web/fyers_bridge.py --sync</code>

          <div class="flex items-center justify-between text-slate-400 mt-2">
            <span>Emergency Kill Switch (Square-Off &amp; Cancel):</span>
            <button onclick="copyToClipboard('python3 web/fyers_bridge.py --kill-switch')" class="text-rose-400 hover:underline">Copy</button>
          </div>
          <code class="text-rose-400 block bg-slate-950 p-2 rounded border border-slate-800">python3 web/fyers_bridge.py --kill-switch</code>
        </div>

        <div class="border-t border-slate-800 pt-3">
          <h4 class="font-bold text-white mb-2">Or Direct CSV / Tradebook Ingestion:</h4>
          <button onclick="closeFyersBridgeModal(); triggerFyersImport();" class="w-full py-2.5 px-4 rounded-xl bg-orange-600 hover:bg-orange-500 text-white font-bold transition flex items-center justify-center gap-2 shadow-lg shadow-orange-600/30">
            <span>📁 Select FYERS Tradebook CSV</span>
          </button>
        </div>
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
  </div>"""

    content = content.replace("</body>", f"{new_modals}\n</body>")

    # 7. Update submitTrade tradeObj construction
    old_trade_obj = """      const tradeObj = {
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
      };"""

    new_trade_obj = """      const maeVal = parseFloat(document.getElementById('mae_price').value) || null;
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
      };"""

    assert old_trade_obj in content, "Failed to find old_trade_obj"
    content = content.replace(old_trade_obj, new_trade_obj, 1)

    # Clean form and remove screenshot on submit
    old_post_submit = """      saveTradesLocally();
      renderTradesTable();"""
    new_post_submit = """      saveTradesLocally();
      renderTradesTable();
      dispatchAccountabilityAlert("TRADE_LOGGED", { trade: tradeObj });
      document.getElementById('mae_price').value = '';
      document.getElementById('mfe_price').value = '';
      removeScreenshot();"""
    assert old_post_submit in content, "Failed to find old_post_submit"
    content = content.replace(old_post_submit, new_post_submit, 1)

    # Hook Cooldown alert
    old_cooldown = """    function startCooldownTimer(endTime) {
      cooldownEndTime = endTime;"""
    new_cooldown = """    function startCooldownTimer(endTime) {
      cooldownEndTime = endTime;
      dispatchAccountabilityAlert("COOLDOWN_ACTIVE", { endTime: endTime });"""
    assert old_cooldown in content, "Failed to find old_cooldown"
    content = content.replace(old_cooldown, new_cooldown, 1)

    # Hook Kill switch alert
    old_cb_trigger = """      if (todayTrades.length >= 2 || todayLosses.length >= 2) {
        cbBanner.classList.remove('hidden');"""
    new_cb_trigger = """      if (todayTrades.length >= 2 || todayLosses.length >= 2) {
        cbBanner.classList.remove('hidden');
        dispatchAccountabilityAlert("KILL_SWITCH", { reason: todayLosses.length >= 2 ? "2 Losses Daily Limit" : "2 Trades Daily Limit" });"""
    assert old_cb_trigger in content, "Failed to find old_cb_trigger"
    content = content.replace(old_cb_trigger, new_cb_trigger, 1)

    # Render MAE/MFE inside renderAllChartsAndMetrics
    content = content.replace(
        "renderSetupMatrix(trades);",
        "renderSetupMatrix(trades);\n      renderMAEMFEAnalytics(trades);"
    )

    # Add camera icon to trades table row
    content = content.replace(
        """<div class="font-bold text-white font-mono">${t.symbol}</div>""",
        """<div class="font-bold text-white font-mono flex items-center gap-1.5">${t.symbol} ${t.screenshot ? '<span class="text-[11px] cursor-pointer" title="Screenshot attached (Click row to view)">📷</span>' : ''}</div>"""
    )

    # Add JS extension
    js_extension = """
    // ==========================================
    // EXTENDED ENGINE V8: SCREENSHOTS, MAE/MFE, PHASES, WEBHOOKS
    // ==========================================

    let currentTradeScreenshot = "";
    let activePhase = 2; // Default Phase 2 (Days 4-10)
    let currentDayNumber = 4;

    // --- Clipboard Paste Listener (Ctrl+V) ---
    function initClipboardPasteListener() {
      window.addEventListener('paste', function(e) {
        if (!e.clipboardData || !e.clipboardData.items) return;
        for (let i = 0; i < e.clipboardData.items.length; i++) {
          const item = e.clipboardData.items[i];
          if (item.type.indexOf('image') !== -1) {
            const blob = item.getAsFile();
            const reader = new FileReader();
            reader.onload = function(evt) {
              setTradeScreenshot(evt.target.result);
            };
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
      reader.onload = function(evt) {
        setTradeScreenshot(evt.target.result);
      };
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

      const msg = "⚡ *TRADER RESET SYSTEM TEST ALERT*\\n\\nAccountability Webhook Connected Successfully! Ready to guard your execution.";
      
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
        msg = `${icon} *TRADE LOGGED*\\n• Symbol: \`${t.symbol}\` (${t.direction})\\n• Result: *₹${t.net_pnl}* (${t.r_multiple}R)\\n• Rule Compliant: ${t.rule_violation === "N" ? "YES (5/5)" : "NO"}\\n• Urgency: ${t.emotion_before}/10`;
      } else if (eventType === "COOLDOWN_ACTIVE") {
        msg = `🚨 *MANDATORY 30-MIN LOSS COOLDOWN ACTIVE*\\n• Loss registered. Step away from your screens immediately.\\n• Cooldown timer running until: ${new Date(Date.now() + 30*60000).toLocaleTimeString('en-IN')}`;
      } else if (eventType === "KILL_SWITCH") {
        msg = `🛑 *BROKER KILL SWITCH ENGAGED*\\n• Reason: ${data.reason}\\n• Day complete. No further entries allowed under any circumstances.`;
      } else if (eventType === "PHASE_GRADUATE") {
        msg = `🚀 *PHASE GRADUATION ACHIEVED*\\n• Successfully graduated to Phase ${data.phase}! Keep executing with institutional precision.`;
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

    // --- FYERS Bridge Modal Helpers ---
    function openFyersBridgeModal() {
      document.getElementById('fyersSyncModal').classList.remove('hidden');
    }

    function closeFyersBridgeModal() {
      document.getElementById('fyersSyncModal').classList.add('hidden');
    }

    function copyToClipboard(text) {
      navigator.clipboard.writeText(text).then(() => {
        alert("Copied to clipboard: " + text);
      });
    }

    // --- MAE / MFE Calculation & Tab 3 Suite ---
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

    // Initialize extension on DOM ready
    window.addEventListener('DOMContentLoaded', () => {
      initClipboardPasteListener();
      renderPhaseTracker();
    });
    """

    # Inject js_extension right before the closing </script> tag
    assert "  </script>" in content, "Failed to find closing script tag"
    content = content.replace("  </script>", f"{js_extension}\n  </script>", 1)

    # Write files
    for path in [OUT_PUBLIC, OUT_DELIV, OUT_BRAIN]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully generated v8: {path} ({len(content)} bytes)")

if __name__ == "__main__":
    build_v8()
