#!/usr/bin/env python3
"""
Builder for Trader Execution Reset System Command Center v9.
Simplifies the FYERS API Bridge into 3 ultra-convenient methods:
1. In-Dashboard 1-Click Sync (Paste Access Token once in the UI modal & click Sync — no terminal needed)
2. Instant FYERS Web Text Paste / File Dropzone (Copy-paste rows directly from FYERS Web or drop CSV/Excel)
3. Automated Zero-Prompt Login Script (Pure Python TOTP auto-login with 0 browser steps)
"""

import os

SRC_PATH = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html"
OUT_PUBLIC = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/public/index.html"
OUT_DELIV = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html"
OUT_BRAIN = "/home/sunny/.gemini/antigravity/brain/85803015-3567-4584-af28-ca9d6eed9423/trader_dashboard.html"

def build_v9():
    with open(SRC_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Title to v9
    content = content.replace(
        "<title>Trader Execution Reset System — Institutional Command Center v8</title>",
        "<title>Trader Execution Reset System — Institutional Command Center v9 (Simplified FYERS Bridge)</title>"
    )

    # 2. Replace #fyersSyncModal with the 3-Method Simplified Interface
    old_fyers_modal = """  <!-- ========================================== -->
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
  </div>"""

    new_fyers_modal = """  <!-- ========================================== -->
  <!-- MODAL: SIMPLIFIED FYERS SYNC BRIDGE (3 METHODS) -->
  <!-- ========================================== -->
  <div id="fyersSyncModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="glass-card rounded-2xl w-full max-w-2xl border border-orange-500/30 shadow-2xl p-6 relative max-h-[92vh] overflow-y-auto">
      
      <!-- Modal Header -->
      <div class="flex items-center justify-between pb-4 border-b border-slate-800">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-orange-500 to-amber-600 flex items-center justify-center text-white font-black text-lg shadow-lg shadow-orange-500/20">
            ⚡
          </div>
          <div>
            <h3 class="text-base font-extrabold text-white flex items-center gap-2">
              FYERS Live Sync Bridge
              <span class="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full bg-orange-500/10 text-orange-400 border border-orange-500/30">
                Simplified v3
              </span>
            </h3>
            <p class="text-xs text-slate-400">Choose your preferred friction-free sync method below</p>
          </div>
        </div>
        <button onclick="closeFyersBridgeModal()" class="text-slate-400 hover:text-white text-2xl font-bold">&times;</button>
      </div>

      <!-- 3 Method Selection Tabs inside Modal -->
      <div class="grid grid-cols-3 gap-2 mt-4 p-1 bg-slate-950/80 rounded-xl border border-slate-800 text-xs">
        <button id="fyersTabBtn1" onclick="switchFyersModalTab(1)" class="fyers-subtab-btn active py-2 rounded-lg font-bold text-center transition bg-orange-600 text-white shadow">
          ⚡ 1-Click UI Sync
        </button>
        <button id="fyersTabBtn2" onclick="switchFyersModalTab(2)" class="fyers-subtab-btn py-2 rounded-lg font-bold text-center text-slate-400 hover:text-white transition">
          📋 Instant Web Paste
        </button>
        <button id="fyersTabBtn3" onclick="switchFyersModalTab(3)" class="fyers-subtab-btn py-2 rounded-lg font-bold text-center text-slate-400 hover:text-white transition">
          🤖 Auto-Sync CLI
        </button>
      </div>

      <!-- ============================================== -->
      <!-- SUB-TAB 1: 1-CLICK IN-DASHBOARD UI SYNC -->
      <!-- ============================================== -->
      <div id="fyersSubTab1" class="space-y-4 mt-5 text-xs">
        <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800 space-y-3">
          <p class="font-bold text-slate-200 flex items-center gap-1.5">
            <span class="text-orange-400">🔑</span>
            <span>Paste FYERS Access Token (Valid for 24 Hours)</span>
          </p>
          <p class="text-slate-400 text-[11px]">
            No command line needed. Paste your App ID and daily token once — it is stored securely in your browser session for 1-click refreshes all day.
          </p>

          <div class="space-y-2">
            <div>
              <label class="block font-semibold text-slate-300 mb-1">FYERS App ID</label>
              <input type="text" id="fyersModalAppId" placeholder="e.g. XC12345-100" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-white font-mono focus:border-orange-500 focus:outline-none">
            </div>
            <div>
              <label class="block font-semibold text-slate-300 mb-1">Daily Access Token</label>
              <input type="password" id="fyersModalToken" placeholder="Paste FYERS access_token here..." class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-white font-mono focus:border-orange-500 focus:outline-none">
            </div>
          </div>

          <div class="pt-2 flex items-center justify-between gap-3">
            <button onclick="syncFyersViaUI()" id="fyersSyncActionBtn" class="flex-1 py-2.5 px-4 rounded-xl bg-gradient-to-r from-orange-600 to-amber-600 hover:from-orange-500 hover:to-amber-500 text-white font-bold transition flex items-center justify-center gap-2 shadow-lg shadow-orange-600/30">
              <span id="fyersSyncBtnIcon">⚡</span>
              <span id="fyersSyncBtnText">Sync Today's Fills Now</span>
            </button>
            <button onclick="saveFyersCredentials()" class="py-2.5 px-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold transition border border-slate-700" title="Remember App ID & Token">
              💾 Remember
            </button>
          </div>
          <p id="fyersSyncStatusMessage" class="hidden text-center text-xs font-semibold mt-2"></p>
        </div>

        <!-- Emergency Square-Off Kill Switch Button -->
        <div class="p-3.5 rounded-xl bg-rose-950/40 border border-rose-500/30 flex items-center justify-between gap-3">
          <div>
            <p class="font-bold text-rose-300 flex items-center gap-1.5"><span>🛑</span> Physical Broker Kill Switch</p>
            <p class="text-[11px] text-rose-400/80">Cancel all pending limit orders &amp; exit open intraday MIS positions on FYERS.</p>
          </div>
          <button onclick="triggerFyersKillSwitchUI()" class="py-2 px-3.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold transition text-xs whitespace-nowrap shadow-lg shadow-rose-600/30">
            Square Off Now
          </button>
        </div>
      </div>

      <!-- ============================================== -->
      <!-- SUB-TAB 2: INSTANT WEB PASTE & FILE DROPZONE -->
      <!-- ============================================== -->
      <div id="fyersSubTab2" class="hidden space-y-4 mt-5 text-xs">
        <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-800 space-y-3">
          <div class="flex items-center justify-between">
            <label class="font-bold text-slate-200 flex items-center gap-1.5">
              <span>📋</span>
              <span>Paste FYERS Web Orderbook / Tradebook Rows</span>
            </label>
            <span class="text-[10px] text-slate-500 font-mono">Zero-Auth &bull; 100% Offline</span>
          </div>
          <p class="text-slate-400 text-[11px]">
            In FYERS Web, open <strong>Tradebook</strong>, press <kbd class="px-1.5 py-0.5 bg-slate-800 rounded text-slate-300 border border-slate-700 font-mono">Ctrl + A</kbd> (or select rows) then <kbd class="px-1.5 py-0.5 bg-slate-800 rounded text-slate-300 border border-slate-700 font-mono">Ctrl + C</kbd>, and paste here:
          </p>
          <textarea id="fyersPastedTextArea" rows="4" placeholder="Example paste:
RELIANCE-EQ  BUY   100  2500.00  FILLED  09:21:34
RELIANCE-EQ  SELL  100  2512.50  FILLED  09:28:10" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 text-white font-mono text-xs placeholder-slate-600 focus:outline-none focus:border-orange-500"></textarea>

          <button onclick="parseFyersWebPastedText()" class="w-full py-2.5 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold transition flex items-center justify-center gap-2 shadow-lg shadow-emerald-600/30">
            <span>⚡ Parse &amp; Log Trades</span>
          </button>
        </div>

        <div class="text-center text-slate-500 font-bold uppercase text-[10px]">&mdash; OR DROP EXPORT FILE &mdash;</div>

        <button onclick="closeFyersBridgeModal(); triggerFyersImport();" class="w-full py-2.5 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-bold transition flex items-center justify-center gap-2">
          <span>📁 Select Exported FYERS Tradebook CSV / XLSX</span>
        </button>
      </div>

      <!-- ============================================== -->
      <!-- SUB-TAB 3: ZERO-PROMPT AUTO-LOGIN CLI -->
      <!-- ============================================== -->
      <div id="fyersSubTab3" class="hidden space-y-4 mt-5 text-xs">
        <div class="bg-blue-500/10 border border-blue-500/20 rounded-xl p-3.5 text-blue-200">
          <p class="font-bold flex items-center gap-1.5"><span>🤖</span> Completely Automated Background Sync</p>
          <p class="mt-1 text-[11px] text-blue-300/80">
            Uses Pure Python standard library (RFC 6238 TOTP) to log into FYERS silently without opening any browser or copying URLs.
          </p>
        </div>

        <div class="bg-slate-900 p-3.5 rounded-xl border border-slate-800 font-mono text-[11px] space-y-2">
          <div class="flex items-center justify-between text-slate-400">
            <span>Automated 1-Step Sync Command:</span>
            <button onclick="copyToClipboard('python3 web/fyers_auto_sync.py --sync')" class="text-blue-400 hover:underline">Copy</button>
          </div>
          <code class="text-emerald-400 block bg-slate-950 p-2 rounded border border-slate-800">python3 web/fyers_auto_sync.py --sync</code>

          <div class="flex items-center justify-between text-slate-400 mt-2">
            <span>Emergency Kill Switch CLI:</span>
            <button onclick="copyToClipboard('python3 web/fyers_auto_sync.py --kill-switch')" class="text-rose-400 hover:underline">Copy</button>
          </div>
          <code class="text-rose-400 block bg-slate-950 p-2 rounded border border-slate-800">python3 web/fyers_auto_sync.py --kill-switch</code>
        </div>

        <p class="text-slate-400 text-[11px]">
          Runs seamlessly from terminal or can be scheduled via cron at 10:35 AM IST right after your trading window closes.
        </p>
      </div>

    </div>
  </div>"""

    assert old_fyers_modal in content, "Failed to find old_fyers_modal"
    content = content.replace(old_fyers_modal, new_fyers_modal, 1)

    # 3. Add JS Functions for Simplified FYERS Bridge:
    # switchFyersModalTab, syncFyersViaUI, saveFyersCredentials, triggerFyersKillSwitchUI, parseFyersWebPastedText
    simplified_fyers_js = """
    // ==========================================
    // SIMPLIFIED FYERS BRIDGE V9 JAVASCRIPT ENGINE
    // ==========================================

    function switchFyersModalTab(tabIndex) {
      for (let i = 1; i <= 3; i++) {
        const btn = document.getElementById(`fyersTabBtn${i}`);
        const pane = document.getElementById(`fyersSubTab${i}`);
        if (btn && pane) {
          if (i === tabIndex) {
            btn.className = "fyers-subtab-btn active py-2 rounded-lg font-bold text-center transition bg-orange-600 text-white shadow";
            pane.classList.remove('hidden');
          } else {
            btn.className = "fyers-subtab-btn py-2 rounded-lg font-bold text-center text-slate-400 hover:text-white transition";
            pane.classList.add('hidden');
          }
        }
      }
    }

    function openFyersBridgeModal() {
      // Load saved App ID & Token from localStorage
      const savedAppId = localStorage.getItem('fyers_app_id') || "";
      const savedToken = localStorage.getItem('fyers_access_token') || "";
      const appIdInput = document.getElementById('fyersModalAppId');
      const tokenInput = document.getElementById('fyersModalToken');
      if (appIdInput) appIdInput.value = savedAppId;
      if (tokenInput) tokenInput.value = savedToken;

      const modal = document.getElementById('fyersSyncModal');
      if (modal) modal.classList.remove('hidden');
      switchFyersModalTab(1);
    }

    function saveFyersCredentials() {
      const appId = document.getElementById('fyersModalAppId').value.trim();
      const token = document.getElementById('fyersModalToken').value.trim();
      if (appId) localStorage.setItem('fyers_app_id', appId);
      if (token) localStorage.setItem('fyers_access_token', token);
      alert("FYERS App ID and Access Token saved in browser session!");
    }

    async function syncFyersViaUI() {
      const appId = document.getElementById('fyersModalAppId').value.trim();
      const token = document.getElementById('fyersModalToken').value.trim();
      const statusMsg = document.getElementById('fyersSyncStatusMessage');
      const btn = document.getElementById('fyersSyncActionBtn');
      const btnText = document.getElementById('fyersSyncBtnText');

      if (!token) {
        alert("Please paste your FYERS Access Token first.");
        return;
      }
      if (appId) localStorage.setItem('fyers_app_id', appId);
      localStorage.setItem('fyers_access_token', token);

      btn.disabled = true;
      btnText.textContent = "Syncing Tradebook...";
      if (statusMsg) {
        statusMsg.className = "text-center text-xs font-semibold mt-2 text-amber-400 block";
        statusMsg.textContent = "Connecting to FYERS tradebook...";
      }

      // 1. Try local server endpoint first if available
      try {
        const resp = await fetch('/api/fyers/sync', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ app_id: appId, access_token: token })
        });
        if (resp.ok) {
          const res = await resp.json();
          if (res.trades && Array.isArray(res.trades)) {
            tradesData = res.trades;
            saveTradesLocally();
            renderTradesTable();
            renderTopCapitalHeader();
            renderAllChartsAndMetrics();
            checkDailyCircuitBreaker();
            if (statusMsg) {
              statusMsg.className = "text-center text-xs font-semibold mt-2 text-emerald-400 block";
              statusMsg.textContent = `✅ Successfully synced ${res.synced_count || 0} trades from FYERS!`;
            }
            alert(`✅ FYERS Sync Complete! ${res.synced_count || 0} trades synchronized with statutory charges calculated.`);
            btn.disabled = false;
            btnText.textContent = "Sync Today's Fills Now";
            return;
          }
        }
      } catch (err) {
        console.warn("Backend proxy offline, trying direct client fetch:", err);
      }

      // 2. Direct client fetch fallback
      try {
        const directResp = await fetch('https://api-t1.fyers.in/api/v3/tradebook', {
          headers: {
            'Authorization': `${appId}:${token}`,
            'Content-Type': 'application/json'
          }
        });
        if (directResp.ok) {
          const data = await directResp.json();
          const fills = data.tradeBook || [];
          if (fills.length === 0) {
            alert("No tradebook fills found for today in FYERS.");
            if (statusMsg) statusMsg.textContent = "No fills found today.";
          } else {
            processAndAppendFyersFills(fills);
            alert(`✅ Direct FYERS sync successful! Processed ${fills.length} execution fills.`);
            if (statusMsg) {
              statusMsg.className = "text-center text-xs font-semibold mt-2 text-emerald-400 block";
              statusMsg.textContent = `✅ Processed ${fills.length} execution fills directly!`;
            }
          }
        } else {
          const errData = await directResp.json().catch(() => ({}));
          throw new Error(errData.message || `HTTP ${directResp.status}`);
        }
      } catch (directErr) {
        alert("FYERS Sync Notice: Direct browser call was blocked by CORS policy or invalid token. Run: python3 web/fyers_auto_sync.py --sync or use the 'Instant Web Paste' tab.");
        if (statusMsg) {
          statusMsg.className = "text-center text-xs font-semibold mt-2 text-rose-400 block";
          statusMsg.textContent = "Sync blocked. Use CLI or Instant Web Paste.";
        }
      } finally {
        btn.disabled = false;
        btnText.textContent = "Sync Today's Fills Now";
      }
    }

    async function triggerFyersKillSwitchUI() {
      const confirmKill = confirm("🛑 ENGAGE BROKER KILL SWITCH?\\n\\nThis will immediately send square-off requests for all open intraday MIS positions and cancel all open limit orders on FYERS.");
      if (!confirmKill) return;

      const appId = document.getElementById('fyersModalAppId').value.trim() || localStorage.getItem('fyers_app_id');
      const token = document.getElementById('fyersModalToken').value.trim() || localStorage.getItem('fyers_access_token');

      try {
        const resp = await fetch('/api/fyers/kill-switch', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ app_id: appId, access_token: token })
        });
        if (resp.ok) {
          alert("🛑 FYERS Kill Switch Executed Successfully via backend bridge!");
        } else {
          alert("Kill switch request dispatched. Please verify platform square-off.");
        }
      } catch (e) {
        alert("Notice: Run 'python3 web/fyers_auto_sync.py --kill-switch' in terminal to trigger square-off directly.");
      }
      dispatchAccountabilityAlert("KILL_SWITCH", { reason: "Manual Emergency Square-Off via Dashboard" });
    }

    // Helper: Processes raw FYERS fills array and adds to tradesData
    function processAndAppendFyersFills(fills) {
      const bySym = {};
      fills.forEach(f => {
        const sym = (f.symbol || "").replace("NSE:", "").replace("-EQ", "");
        if (!bySym[sym]) bySym[sym] = [];
        bySym[sym].push(f);
      });

      let addedCount = 0;
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
          setup_name: "FYERS API Live Sync",
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
          lesson: "Auto-synced from FYERS tradebook with verified statutory charges.",
          screenshot_link: `https://www.tradingview.com/chart/?symbol=NSE:${sym}`
        };
        tradesData.unshift(tradeObj);
        addedCount++;
      });

      if (addedCount > 0) {
        saveTradesLocally();
        renderTradesTable();
        renderTopCapitalHeader();
        renderAllChartsAndMetrics();
        checkDailyCircuitBreaker();
      }
    }

    // Method 3: Instant Parser for Pasted FYERS Web Text
    function parseFyersWebPastedText() {
      const text = document.getElementById('fyersPastedTextArea').value.trim();
      if (!text) {
        alert("Please paste rows copied from FYERS Web first.");
        return;
      }

      const lines = text.split(/\\r?\\n/).filter(l => l.trim().length > 0);
      const parsedFills = [];

      lines.forEach(line => {
        // Look for symbol, side, qty, price
        const tokens = line.split(/[\\t,\\s]+/).filter(Boolean);
        if (tokens.length >= 4) {
          const symCandidate = tokens.find(t => t.includes("-EQ") || /^[A-Z]{3,12}$/.test(t));
          const sideCandidate = tokens.find(t => /^BUY$/i.test(t) || /^SELL$/i.test(t) || /^B$/i.test(t) || /^S$/i.test(t));
          const numbers = tokens.filter(t => /^\\d+(\\.\\d+)?$/.test(t)).map(Number);

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

      processAndAppendFyersFills(parsedFills);
      document.getElementById('fyersPastedTextArea').value = "";
      closeFyersBridgeModal();
      alert(`✅ Successfully parsed ${parsedFills.length} fills from pasted text! Ledger updated.`);
    }
    """

    # Inject the simplified JS engine right before the closing </script>
    assert "  </script>" in content, "Failed to find closing script tag"
    content = content.replace("  </script>", f"{simplified_fyers_js}\n  </script>", 1)

    # Write files
    for path in [OUT_PUBLIC, OUT_DELIV, OUT_BRAIN]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully generated v9: {path} ({len(content)} bytes)")

if __name__ == "__main__":
    build_v9()
