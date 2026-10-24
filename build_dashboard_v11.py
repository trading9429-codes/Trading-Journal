#!/usr/bin/env python3
"""
Builder for Trader Execution Reset System Command Center v11.
Removes the complex 1-click API sync modal and replaces it with an ultra-simple,
friction-free FYERS Ingestion Interface:
1. Instant Copy-Paste from FYERS Web (Select rows in FYERS Web -> Ctrl+C -> Ctrl+V -> Done)
2. Drag & Drop FYERS Tradebook CSV/Excel file
3. Zero developer tokens, zero IP whitelisting, zero CORS issues, 100% private & offline.
"""

import os
import re

SRC_PATH = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html"
OUT_PUBLIC = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/public/index.html"
OUT_DELIV = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html"
OUT_BRAIN = "/home/sunny/.gemini/antigravity/brain/85803015-3567-4584-af28-ca9d6eed9423/trader_dashboard.html"

def build_v11():
    with open(SRC_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Title
    content = content.replace(
        "<title>Trader Execution Reset System — Institutional Command Center v10 (Quant Risk & VaR Suite)</title>",
        "<title>Trader Execution Reset System — Institutional Command Center</title>"
    )

    # 2. Update Global Action Strip Header: Remove complex API button, unify into 1 clean "⚡ Import FYERS Trades"
    old_buttons = """        <button onclick="openWebhookModal()" class="px-3 py-2 rounded-lg bg-sky-600/20 hover:bg-sky-600/30 text-sky-300 border border-sky-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm" title="Configure Telegram/WhatsApp Accountability Alerts">
          <span>🔔</span>
          <span>Alerts &amp; Webhook</span>
        </button>
        <button onclick="openFyersBridgeModal()" class="px-3 py-2 rounded-lg bg-orange-600/20 hover:bg-orange-600/30 text-orange-300 border border-orange-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm" title="FYERS API v3 1-Click Sync Bridge">
          <span>🔌</span>
          <span>FYERS Live Sync</span>
        </button>
        <button onclick="openWeeklyReviewModal()" class="px-3 py-2 rounded-lg bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-400 border border-indigo-500/30 font-medium text-xs flex items-center gap-1.5 transition">
          <span>📝</span>
          <span>Weekly Review (D5)</span>
        </button>
        <button onclick="triggerFyersImport()" class="px-3 py-2 rounded-lg bg-orange-600/20 hover:bg-orange-600/30 text-orange-400 border border-orange-500/30 font-medium text-xs flex items-center gap-1.5 transition">
          <span>⚡</span>
          <span>Import FYERS</span>
        </button>"""

    new_buttons = """        <button onclick="openWebhookModal()" class="px-3 py-2 rounded-lg bg-sky-600/20 hover:bg-sky-600/30 text-sky-300 border border-sky-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm" title="Configure Telegram/WhatsApp Accountability Alerts">
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
        </button>"""

    assert old_buttons in content, "Failed to find old_buttons"
    content = content.replace(old_buttons, new_buttons, 1)

    # 3. Replace the complex fyersSyncModal with the clean fyersIngestModal
    # Find fyersSyncModal
    modal_pattern = r'<div id="fyersSyncModal"[\s\S]*?</div>\s*</div>\s*</div>'
    
    clean_fyers_modal = """  <!-- ========================================== -->
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
  </div>"""

    content = re.sub(modal_pattern, clean_fyers_modal, content)

    # 4. Update JS modal openers and closers
    js_modal_functions = """
    // Simple FYERS Ingestion Modal Controls
    function openFyersIngestModal() {
      const modal = document.getElementById('fyersIngestModal');
      if (modal) modal.classList.remove('hidden');
    }

    function closeFyersIngestModal() {
      const modal = document.getElementById('fyersIngestModal');
      if (modal) modal.classList.add('hidden');
    }
    """

    content = content.replace("function openFyersBridgeModal() {", f"{js_modal_functions}\n    function openFyersBridgeModal() {{ openFyersIngestModal(); return; }} function _deprecated_openFyersBridgeModal() {{")

    # Write files
    for path in [OUT_PUBLIC, OUT_DELIV, OUT_BRAIN]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully generated v11: {path} ({len(content)} bytes)")

if __name__ == "__main__":
    build_v11()
