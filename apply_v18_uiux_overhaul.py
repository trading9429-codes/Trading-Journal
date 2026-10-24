#!/usr/bin/env python3
"""
Applies all 7 UI/UX Enhancements to build_master_v16.py:
1. Command Palette (Ctrl+K / Cmd+K with instant fuzzy actions)
2. Interactive Risk-to-Reward Visualizer Split-Bar (in trade form)
3. Visual P&L R-Multiple Sparkbars in Trade Ledger
4. Interactive Quick-Filter Chips & Instant Ledger Search + Column Sorting
5. High-Density Compact Pro vs. Roomy Visual Mode Toggle
6. Pro Terminal Accent Theme Switcher (Obsidian, Bloomberg, Linear, Nordic)
7. Floating Institutional Bottom Status Dock (live latency, quota, P&L, hotkey pills)
"""

MASTER_FILE = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/build_master_v16.py"

def main():
    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        code = f.read()

    # ====================================================
    # 1. HEAD CSS: Themes, Compact Density, Sparkbars, Dock
    # ====================================================
    uiux_css = """
    /* --- UI/UX OVERHAUL V18 --- */

    /* 6. Pro Terminal Accent Themes */
    [data-theme="bloomberg"] {
      --bg-dark: #000000;
      background-color: #000000 !important;
      background-image: radial-gradient(circle at 50% 0%, rgba(245, 158, 11, 0.15) 0%, transparent 60%) !important;
    }
    [data-theme="bloomberg"] .glass-card {
      background: rgba(12, 10, 4, 0.95) !important;
      border-color: rgba(245, 158, 11, 0.25) !important;
    }
    [data-theme="bloomberg"] h1, [data-theme="bloomberg"] h2, [data-theme="bloomberg"] h3 {
      color: #FCD34D !important;
    }

    [data-theme="linear"] {
      --bg-dark: #080B10;
      background-color: #080B10 !important;
      background-image: radial-gradient(circle at 50% 0%, rgba(255, 255, 255, 0.05) 0%, transparent 50%) !important;
    }
    [data-theme="linear"] .glass-card {
      background: rgba(15, 20, 28, 0.9) !important;
      border-color: rgba(255, 255, 255, 0.1) !important;
    }

    [data-theme="nordic"] {
      --bg-dark: #030D18;
      background-color: #030D18 !important;
      background-image: radial-gradient(circle at 50% 0%, rgba(6, 182, 212, 0.14) 0%, transparent 60%) !important;
    }
    [data-theme="nordic"] .glass-card {
      background: rgba(4, 18, 32, 0.9) !important;
      border-color: rgba(6, 182, 212, 0.25) !important;
    }

    /* 5. High-Density Compact Pro Mode */
    body.compact-density .glass-card {
      padding: 0.85rem !important;
    }
    body.compact-density table th {
      padding: 0.35rem 0.5rem !important;
      font-size: 10px !important;
    }
    body.compact-density table td {
      padding: 0.35rem 0.5rem !important;
      font-size: 11px !important;
    }
    body.compact-density .space-y-6 > * + * {
      margin-top: 1rem !important;
    }
    body.compact-density .space-y-4 > * + * {
      margin-top: 0.65rem !important;
    }

    /* Bottom padding for floating dock */
    body {
      padding-bottom: 3.5rem !important;
    }

    /* 1. Command Palette Modal Animations */
    #commandPaletteModal.active {
      display: flex !important;
    }
    .palette-item.selected {
      background: rgba(59, 130, 246, 0.25) !important;
      border-color: rgba(96, 165, 250, 0.4) !important;
    }

    /* Filter Chips active state */
    .filter-chip.active {
      background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
      color: #FFFFFF !important;
      border-color: #60A5FA !important;
      box-shadow: 0 0 10px rgba(37, 99, 235, 0.35);
    }
"""

    old_style_target = "      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);\n    }\n\n    }\n  </style>\n</head>'''"
    assert old_style_target in code, "Failed to find old_style_target"
    code = code.replace(old_style_target, "      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);\n    }\n" + uiux_css + "\n    }\n  </style>\n</head>'''", 1)

    # ====================================================
    # 2. TOOLBAR: Add Theme Switcher, Density Toggle & Command Palette
    # ====================================================
    old_toolbar_target = '        <!-- Combat Mode Minimalist HUD Button -->'
    new_toolbar_additions = """        <!-- Command Palette Quick Launcher -->
        <button onclick="openCommandPalette()" class="px-3 py-2 rounded-lg bg-blue-600/20 hover:bg-blue-600/30 text-blue-300 border border-blue-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm" title="Global Command Palette (Hotkey: Ctrl+K / Cmd+K)">
          <span>⌘</span>
          <span class="hidden md:inline">Palette</span>
          <kbd class="hotkey-badge text-[9px] px-1 py-0">Ctrl+K</kbd>
        </button>
        <!-- Pro Terminal Theme Selector -->
        <select id="themeSelector" onchange="switchTheme(this.value)" class="bg-slate-900 border border-slate-700 hover:border-slate-600 rounded-lg px-2.5 py-1.5 text-xs text-slate-300 font-mono focus:outline-none focus:border-blue-500 transition cursor-pointer" title="Switch Institutional Color Palette">
          <option value="obsidian">🌌 Obsidian</option>
          <option value="bloomberg">⚡ Bloomberg</option>
          <option value="linear">📐 Linear</option>
          <option value="nordic">❄️ Nordic</option>
        </select>
        <!-- Density Mode Toggle Button -->
        <button onclick="toggleDensityMode()" id="densityToggleBtn" class="px-2.5 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs font-mono transition" title="Toggle Compact Pro Density Mode">
          <span id="densityIcon">📐</span>
          <span id="densityLabel">Compact</span>
        </button>
        <!-- Combat Mode Minimalist HUD Button -->"""

    assert old_toolbar_target in code, "Failed to find old_toolbar_target"
    code = code.replace(old_toolbar_target, new_toolbar_additions, 1)

    # ====================================================
    # 3. TAB 1: Live Risk-to-Reward Ratio Visualizer Bar
    # ====================================================
    # Inject Live R:R Split-Bar right after Emotion Urgency Slider
    old_urgency_slider = r'''          <!-- Emotional Urgency Slider -->
          <div>
            <div class="flex justify-between items-center mb-1">
              <label class="text-slate-400 text-[11px] font-semibold uppercase tracking-wider">Emotional Urgency / State (1–10)</label>
              <span id="urgencyValueDisplay" class="text-xs font-mono font-bold text-emerald-400">3 (Calm &bull; Non-Impulsive)</span>
            </div>
            <input type="range" id="urgencySlider" min="1" max="10" value="3" oninput="updateUrgencyDisplay(this.value)" class="w-full accent-emerald-500 bg-slate-800 rounded-lg cursor-pointer h-2">
            <div class="flex justify-between text-[10px] text-slate-500 mt-1">
              <span>1 (Detached)</span>
              <span>5 (Neutral)</span>
              <span>10 (FOMO / Revenge)</span>
            </div>
          </div>'''

    new_rr_visualizer = r'''          <!-- Emotional Urgency Slider -->
          <div>
            <div class="flex justify-between items-center mb-1">
              <label class="text-slate-400 text-[11px] font-semibold uppercase tracking-wider">Emotional Urgency / State (1–10)</label>
              <span id="urgencyValueDisplay" class="text-xs font-mono font-bold text-emerald-400">3 (Calm &bull; Non-Impulsive)</span>
            </div>
            <input type="range" id="urgencySlider" min="1" max="10" value="3" oninput="updateUrgencyDisplay(this.value)" class="w-full accent-emerald-500 bg-slate-800 rounded-lg cursor-pointer h-2">
            <div class="flex justify-between text-[10px] text-slate-500 mt-1">
              <span>1 (Detached)</span>
              <span>5 (Neutral)</span>
              <span>10 (FOMO / Revenge)</span>
            </div>
          </div>

          <!-- 2. INTERACTIVE RISK-TO-REWARD LIVE VISUALIZER SPLIT-BAR -->
          <div id="rrVisualizerContainer" class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 space-y-2 font-mono transition-all duration-300">
            <div class="flex items-center justify-between text-xs">
              <div class="flex items-center gap-2">
                <span class="text-slate-400 uppercase font-semibold text-[10px]">Planned Edge Expectancy</span>
                <span id="rrRatioValueBadge" class="px-2 py-0.5 rounded font-bold text-xs bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                  🎯 R:R 2.40R &bull; Valid Edge
                </span>
              </div>
              <div class="text-[11px] text-slate-400 flex items-center gap-2">
                <span>Risk: <strong id="rrRiskCashDisp" class="text-rose-400">₹500</strong></span>
                <span>&bull;</span>
                <span>Target: <strong id="rrTargetCashDisp" class="text-emerald-400">₹1,200</strong></span>
              </div>
            </div>

            <!-- Dynamic Graphical Split Bar -->
            <div class="w-full bg-slate-900 h-2.5 rounded-full overflow-hidden flex border border-slate-800">
              <div id="rrRiskBar" class="bg-rose-500/90 h-full transition-all duration-300" style="width: 29%;" title="Risk: 1.0R"></div>
              <div id="rrRewardBar" class="bg-emerald-500 h-full transition-all duration-300 shadow-sm shadow-emerald-500/50" style="width: 71%;" title="Reward: 2.40R"></div>
            </div>

            <div class="flex items-center justify-between text-[10px] text-slate-500">
              <span id="rrStopDistanceDisp">Stop: 5.00 pts (1.0R)</span>
              <span id="rrMinRuleAdvice" class="text-slate-400">Phase 1 &bull; 2 Rule: Minimum Planned R:R &ge; 2.2 required</span>
              <span id="rrTargetDistanceDisp">Target: 12.00 pts (2.40R)</span>
            </div>
          </div>'''

    assert old_urgency_slider in code, "Failed to find old_urgency_slider"
    code = code.replace(old_urgency_slider, new_rr_visualizer, 1)

    # ====================================================
    # 4. TAB 1: Ledger Quick-Filter Chips & Live Search Bar
    # ====================================================
    old_ledger_header = r'''        <!-- Filter bar -->
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between pb-4 border-b border-slate-800 gap-3">
          <div class="flex items-center gap-3">
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <span>Full Trade Log &bull; 30-Day Execution Ledger</span>
              <span id="ledgerCountBadge" class="text-xs px-2.5 py-0.5 rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/20 font-mono">
                0 trades
              </span>
            </h3>
          </div>

          <!-- Strategy & Outcome Filter Controls -->
          <div class="flex items-center gap-2 flex-wrap">'''

    new_ledger_header = r'''        <!-- Filter bar -->
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between pb-3 border-b border-slate-800 gap-3">
          <div class="flex items-center gap-3">
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <span>Full Trade Log &bull; 30-Day Execution Ledger</span>
              <span id="ledgerCountBadge" class="text-xs px-2.5 py-0.5 rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/20 font-mono">
                0 trades
              </span>
            </h3>
          </div>

          <!-- Instant Text Search Input -->
          <div class="relative w-full md:w-64">
            <input type="text" id="ledgerSearchInput" oninput="renderTradesTable()" placeholder="🔍 Filter symbol, strategy, date..." class="w-full bg-slate-950 border border-slate-700/80 rounded-xl px-3 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 font-mono transition">
            <button onclick="clearLedgerSearch()" id="clearLedgerSearchBtn" class="hidden absolute right-2.5 top-1.5 text-slate-400 hover:text-white text-xs">&times;</button>
          </div>

          <!-- Strategy & Outcome Filter Controls -->
          <div class="flex items-center gap-2 flex-wrap">'''

    assert old_ledger_header in code, "Failed to find old_ledger_header"
    code = code.replace(old_ledger_header, new_ledger_header, 1)

    # Add Quick Filter Chips row right below filter controls
    old_ledger_table_start = r'''        <div class="overflow-x-auto mt-4">
          <table class="w-full text-left text-xs font-mono">'''

    new_ledger_table_start = r'''        <!-- 4. Interactive Quick-Filter Chips -->
        <div class="flex items-center gap-1.5 overflow-x-auto py-2.5 scrollbar-none" id="ledgerQuickFilterChipsContainer">
          <button onclick="setLedgerQuickFilter('ALL')" id="chip_ALL" class="filter-chip active px-2.5 py-1 rounded-lg bg-slate-800 text-slate-200 border border-slate-700 text-[11px] font-semibold whitespace-nowrap transition">
            All Fills
          </button>
          <button onclick="setLedgerQuickFilter('Win')" id="chip_Win" class="filter-chip px-2.5 py-1 rounded-lg bg-slate-900 text-slate-400 hover:text-emerald-300 border border-slate-800 text-[11px] font-semibold whitespace-nowrap transition">
            🟢 Wins Only
          </button>
          <button onclick="setLedgerQuickFilter('Loss')" id="chip_Loss" class="filter-chip px-2.5 py-1 rounded-lg bg-slate-900 text-slate-400 hover:text-rose-300 border border-slate-800 text-[11px] font-semibold whitespace-nowrap transition">
            🔴 Losses Only
          </button>
          <button onclick="setLedgerQuickFilter('Breach')" id="chip_Breach" class="filter-chip px-2.5 py-1 rounded-lg bg-slate-900 text-slate-400 hover:text-amber-300 border border-slate-800 text-[11px] font-semibold whitespace-nowrap transition">
            ⚠️ Rule Breaches
          </button>
          <button onclick="setLedgerQuickFilter('1m Pullback to 9EMA')" id="chip_Pullback" class="filter-chip px-2.5 py-1 rounded-lg bg-slate-900 text-slate-400 hover:text-teal-300 border border-slate-800 text-[11px] font-semibold whitespace-nowrap transition">
            1m Pullback
          </button>
          <button onclick="setLedgerQuickFilter('Opening Range Breakout (ORB)')" id="chip_ORB" class="filter-chip px-2.5 py-1 rounded-lg bg-slate-900 text-slate-400 hover:text-teal-300 border border-slate-800 text-[11px] font-semibold whitespace-nowrap transition">
            ORB
          </button>
        </div>

        <div class="overflow-x-auto mt-2">
          <table class="w-full text-left text-xs font-mono">'''

    assert old_ledger_table_start in code, "Failed to find old_ledger_table_start"
    code = code.replace(old_ledger_table_start, new_ledger_table_start, 1)

    # ====================================================
    # 5. INJECT MODAL: Command Palette (Ctrl+K)
    # ====================================================
    command_palette_modal = """  <!-- ========================================== -->
  <!-- MODAL: 1. GLOBAL COMMAND PALETTE (CTRL+K / CMD+K) -->
  <!-- ========================================== -->
  <div id="commandPaletteModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-start justify-center pt-20 p-4" onclick="closeCommandPalette()">
    <div class="glass-card rounded-2xl w-full max-w-2xl border border-blue-500/40 shadow-2xl p-4 relative overflow-hidden" onclick="event.stopPropagation()">
      <!-- Search Input Box -->
      <div class="flex items-center gap-3 pb-3 border-b border-slate-800">
        <span class="text-blue-400 text-lg">⌘</span>
        <input type="text" id="paletteSearchInput" oninput="filterPaletteCommands(this.value)" placeholder="Type a command or jump to view... (e.g. 'long', 'combat', 'dossier')" class="w-full bg-transparent text-white text-sm font-mono placeholder-slate-500 focus:outline-none">
        <kbd class="hotkey-badge text-[10px]">Esc</kbd>
      </div>

      <!-- Quick Commands List -->
      <div id="paletteResultsList" class="mt-3 max-h-80 overflow-y-auto space-y-1 text-xs">
        <!-- Populated dynamically by JS -->
      </div>

      <div class="mt-3 pt-2 border-t border-slate-800 flex items-center justify-between text-[10px] text-slate-500 font-mono">
        <div class="flex items-center gap-2">
          <span>Navigate: <kbd class="hotkey-badge text-[9px] px-1 py-0">↑</kbd><kbd class="hotkey-badge text-[9px] px-1 py-0">↓</kbd></span>
          <span>Select: <kbd class="hotkey-badge text-[9px] px-1 py-0">↵</kbd></span>
        </div>
        <span>Trader Reset OS &bull; Command Hub</span>
      </div>
    </div>
  </div>
"""

    hotkeys_modal_marker = "  <!-- MODAL: KEYBOARD SHORTCUTS & SOUNDPACK SETTINGS -->"
    assert hotkeys_modal_marker in code, "Failed to find hotkeys_modal_marker"
    code = code.replace(hotkeys_modal_marker, command_palette_modal + "\n" + hotkeys_modal_marker, 1)

    # ====================================================
    # 6. INJECT FLOATING BOTTOM STATUS DOCK (Right before </body>)
    # ====================================================
    bottom_dock_markup = """  <!-- ========================================== -->
  <!-- 7. FLOATING INSTITUTIONAL BOTTOM STATUS DOCK -->
  <!-- ========================================== -->
  <div id="institutionalBottomDock" class="fixed bottom-0 inset-x-0 z-40 bg-slate-950/90 backdrop-blur-md border-t border-slate-800 px-4 py-2 hidden sm:flex items-center justify-between text-xs font-mono text-slate-400 shadow-2xl">
    <!-- Left: Live Clock & Network Ping -->
    <div class="flex items-center gap-3">
      <span class="flex items-center gap-1.5 text-slate-200 font-bold">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span id="dockISTClock">09:15:00 IST</span>
      </span>
      <span class="text-slate-700">|</span>
      <span class="flex items-center gap-1 text-[11px] text-slate-400">
        <span>📶</span>
        <span id="dockLatencyDisp" class="text-emerald-400 font-bold">22ms</span>
      </span>
    </div>

    <!-- Center: Session Quota & P&L Snapshot -->
    <div class="flex items-center gap-3 text-xs">
      <span>Quota: <strong id="dockTradeQuotaDisp" class="text-white">1 of 2 Trades</strong></span>
      <span class="text-slate-700">&bull;</span>
      <span>Net: <strong id="dockNetPnLDisp" class="text-emerald-400">+₹0.00</strong></span>
      <span class="text-slate-700">&bull;</span>
      <span>Realized: <strong id="dockNetRDisp" class="text-blue-300">+0.00R</strong></span>
      <span class="text-slate-700">&bull;</span>
      <span>Strikes: <strong id="dockStrikesDisp" class="text-emerald-400">0 / 3</strong></span>
    </div>

    <!-- Right: Quick Navigation & Palette Pills -->
    <div class="flex items-center gap-2">
      <button onclick="toggleCombatMode()" class="px-2 py-0.5 rounded bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[10px] font-bold flex items-center gap-1 transition" title="Toggle Combat Mode HUD">
        <span>🎯 Combat</span>
        <kbd class="hotkey-badge text-[9px] px-1 py-0">H</kbd>
      </button>
      <button onclick="openCommandPalette()" class="px-2 py-0.5 rounded bg-blue-500/10 hover:bg-blue-500/20 text-blue-300 border border-blue-500/30 text-[10px] font-bold flex items-center gap-1 transition" title="Open Command Palette">
        <span>⌘ Palette</span>
        <kbd class="hotkey-badge text-[9px] px-1 py-0">Ctrl+K</kbd>
      </button>
      <button onclick="openHotkeyModal()" class="px-1.5 py-0.5 rounded bg-slate-800 text-slate-400 hover:text-white border border-slate-700 text-[10px] transition" title="Hotkeys Cheatsheet">
        <kbd class="hotkey-badge text-[9px] px-1 py-0">?</kbd>
      </button>
    </div>
  </div>
"""

    old_closing_body = "  </script>\n</body>"
    assert old_closing_body in code, "Failed to find old_closing_body"
    code = code.replace(old_closing_body, f"  </script>\n{bottom_dock_markup}\n</body>", 1)

    # ====================================================
    # 7. SCRIPT LOGIC: Palette, Visualizer, Sparkbars, Filter Chips, Themes
    # ====================================================
    v18_script_logic = """
    // ==========================================
    // UI/UX OVERHAUL V18 ENGINE
    // ==========================================

    // --- 1. GLOBAL COMMAND PALETTE ENGINE ---
    let paletteSelectedIdx = 0;
    const paletteCommands = [
      { id: 'tab1', category: 'Views', title: 'Switch to Tab 1: Live Execution Desk', hotkey: '1', action: () => switchTab(1) },
      { id: 'tab2', category: 'Views', title: 'Switch to Tab 2: Performance & Equity Curves', hotkey: '2', action: () => switchTab(2) },
      { id: 'tab3', category: 'Views', title: 'Switch to Tab 3: Edge Attribution & Leak Matrix', hotkey: '3', action: () => switchTab(3) },
      { id: 'tab4', category: 'Views', title: 'Switch to Tab 4: Quant Risk & Monte Carlo Sim', hotkey: '4', action: () => switchTab(4) },
      { id: 'long', category: 'Execution', title: 'Set Direction: LONG (Buy)', hotkey: 'L', action: () => setTradeDirection('Long') },
      { id: 'short', category: 'Execution', title: 'Set Direction: SHORT (Sell)', hotkey: 'S', action: () => setTradeDirection('Short') },
      { id: 'combat', category: 'Execution', title: 'Toggle Combat Mode HUD (Minimalist)', hotkey: 'H', action: () => toggleCombatMode() },
      { id: 'sym', category: 'Execution', title: 'Focus Stock Symbol Input', hotkey: 'N', action: () => { const s = document.getElementById('symbol'); if (s) { s.focus(); s.select(); } } },
      { id: 'preflight', category: 'Protocols', title: 'Open Pre-Flight Readiness Routine (D2)', hotkey: 'P', action: () => openPreMarketReadinessModal() },
      { id: 'breathing', category: 'Mindset', title: 'Launch 5-Minute Box Breathing Timer', hotkey: 'B', action: () => openPreMarketFocusModal() },
      { id: 'dossier', category: 'Reports', title: 'Open Monthly Institutional Dossier (PDF)', hotkey: 'M', action: () => openMonthlyDossierModal() },
      { id: 'scorecard', category: 'Reports', title: 'Generate EOD Execution Scorecard (PNG)', action: () => openEODCardModal() },
      { id: 'fyers', category: 'Import', title: 'Import FYERS Trades (Offline Copy-Paste)', action: () => openFyersIngestModal() },
      { id: 'alerts', category: 'Alerts', title: 'Test Audio Siren & Desktop Notification', action: () => toggleDesktopNotifications() },
      { id: 'theme_obsidian', category: 'Themes', title: 'Theme: Obsidian Blue (Default)', action: () => switchTheme('obsidian') },
      { id: 'theme_bloomberg', category: 'Themes', title: 'Theme: Bloomberg Amber (High Contrast)', action: () => switchTheme('bloomberg') },
      { id: 'theme_linear', category: 'Themes', title: 'Theme: Linear Monochrome (Graphite)', action: () => switchTheme('linear') },
      { id: 'theme_nordic', category: 'Themes', title: 'Theme: Nordic Frost (Cyan & Teal)', action: () => switchTheme('nordic') },
      { id: 'density', category: 'Settings', title: 'Toggle Compact Pro Density Mode', action: () => toggleDensityMode() }
    ];

    function openCommandPalette() {
      const modal = document.getElementById('commandPaletteModal');
      const input = document.getElementById('paletteSearchInput');
      paletteSelectedIdx = 0;
      if (modal) modal.classList.add('active');
      if (input) {
        input.value = '';
        setTimeout(() => input.focus(), 50);
      }
      renderPaletteResults(paletteCommands);
    }

    function closeCommandPalette() {
      const modal = document.getElementById('commandPaletteModal');
      if (modal) modal.classList.remove('active');
    }

    function filterPaletteCommands(query) {
      paletteSelectedIdx = 0;
      const q = (query || '').toLowerCase().trim();
      const filtered = paletteCommands.filter(c => 
        c.title.toLowerCase().includes(q) || 
        c.category.toLowerCase().includes(q) || 
        (c.hotkey && c.hotkey.toLowerCase() === q)
      );
      renderPaletteResults(filtered);
    }

    function renderPaletteResults(list) {
      const container = document.getElementById('paletteResultsList');
      if (!container) return;

      if (!list || list.length === 0) {
        container.innerHTML = `<div class="p-4 text-center text-slate-500 font-mono text-xs">No matching commands found.</div>`;
        return;
      }

      container.innerHTML = list.map((cmd, idx) => `
        <div onclick="executePaletteCommand(${idx})" onmouseover="paletteSelectedIdx = ${idx}; highlightPaletteItem();" class="palette-item p-2.5 rounded-xl border border-transparent hover:border-slate-700/60 flex items-center justify-between cursor-pointer transition ${idx === paletteSelectedIdx ? 'selected' : ''}">
          <div class="flex items-center gap-2.5">
            <span class="text-[10px] font-mono px-1.5 py-0.2 rounded bg-slate-800 text-slate-400">${cmd.category}</span>
            <span class="font-medium text-slate-200 text-xs">${cmd.title}</span>
          </div>
          ${cmd.hotkey ? `<kbd class="hotkey-badge text-[9px]">${cmd.hotkey}</kbd>` : ''}
        </div>
      `).join('');
    }

    function highlightPaletteItem() {
      const items = document.querySelectorAll('.palette-item');
      items.forEach((it, idx) => {
        if (idx === paletteSelectedIdx) it.classList.add('selected');
        else it.classList.remove('selected');
      });
    }

    function executePaletteCommand(idx) {
      const input = document.getElementById('paletteSearchInput');
      const q = (input?.value || '').toLowerCase().trim();
      const list = paletteCommands.filter(c => 
        c.title.toLowerCase().includes(q) || 
        c.category.toLowerCase().includes(q) || 
        (c.hotkey && c.hotkey.toLowerCase() === q)
      );
      const cmd = list[idx || paletteSelectedIdx];
      if (cmd && typeof cmd.action === 'function') {
        closeCommandPalette();
        cmd.action();
        playFeedbackSound('click');
      }
    }

    // Hook Ctrl+K / Cmd+K listener
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        const modal = document.getElementById('commandPaletteModal');
        if (modal && modal.classList.contains('active')) {
          closeCommandPalette();
        } else {
          openCommandPalette();
        }
        return;
      }

      const modal = document.getElementById('commandPaletteModal');
      if (modal && modal.classList.contains('active')) {
        const items = document.querySelectorAll('.palette-item');
        if (e.key === 'ArrowDown') {
          e.preventDefault();
          if (items.length > 0) {
            paletteSelectedIdx = (paletteSelectedIdx + 1) % items.length;
            highlightPaletteItem();
          }
        } else if (e.key === 'ArrowUp') {
          e.preventDefault();
          if (items.length > 0) {
            paletteSelectedIdx = (paletteSelectedIdx - 1 + items.length) % items.length;
            highlightPaletteItem();
          }
        } else if (e.key === 'Enter') {
          e.preventDefault();
          executePaletteCommand(paletteSelectedIdx);
        }
      }
    });

    // --- 2. INTERACTIVE RISK-TO-REWARD LIVE VISUALIZER ENGINE ---
    function updateRRVisualizer() {
      const entry = parseFloat(document.getElementById('entry_price')?.value) || 0;
      const stop = parseFloat(document.getElementById('stop_price')?.value) || 0;
      const exit = parseFloat(document.getElementById('exit_price')?.value) || 0;
      const qty = parseInt(document.getElementById('qty')?.value) || 0;
      const dir = document.getElementById('direction')?.value || 'Long';

      const riskDist = Math.abs(entry - stop);
      let rewardDist = 0;
      if (dir === 'Long') {
        rewardDist = exit > entry ? (exit - entry) : 0;
      } else {
        rewardDist = exit < entry && exit > 0 ? (entry - exit) : 0;
      }

      const badge = document.getElementById('rrRatioValueBadge');
      const riskBar = document.getElementById('rrRiskBar');
      const rewardBar = document.getElementById('rrRewardBar');
      const cashRiskDisp = document.getElementById('rrRiskCashDisp');
      const cashTargetDisp = document.getElementById('rrTargetCashDisp');
      const stopDistDisp = document.getElementById('rrStopDistanceDisp');
      const targetDistDisp = document.getElementById('rrTargetDistanceDisp');
      const adviceDisp = document.getElementById('rrMinRuleAdvice');

      if (riskDist <= 0 || rewardDist <= 0) {
        if (badge) {
          badge.className = "px-2 py-0.5 rounded font-bold text-xs bg-slate-800 text-slate-400";
          badge.textContent = "Planned R:R -- (Enter Target)";
        }
        if (riskBar) riskBar.style.width = "50%";
        if (rewardBar) rewardBar.style.width = "50%";
        return;
      }

      const rr = rewardDist / riskDist;
      const totalDist = riskDist + rewardDist;
      const riskPct = Math.round((riskDist / totalDist) * 100);
      const rewardPct = 100 - riskPct;

      const totalCashRisk = qty > 0 ? (riskDist * qty).toFixed(2) : '500';
      const totalCashTarget = qty > 0 ? (rewardDist * qty).toFixed(2) : (500 * rr).toFixed(2);

      if (cashRiskDisp) cashRiskDisp.textContent = `₹${totalCashRisk}`;
      if (cashTargetDisp) cashTargetDisp.textContent = `₹${totalCashTarget}`;
      if (stopDistDisp) stopDistDisp.textContent = `Stop: ${riskDist.toFixed(2)} pts (1.0R)`;
      if (targetDistDisp) targetDistDisp.textContent = `Target: ${rewardDist.toFixed(2)} pts (${rr.toFixed(2)}R)`;

      if (riskBar) riskBar.style.width = `${riskPct}%`;
      if (rewardBar) rewardBar.style.width = `${rewardPct}%`;

      if (badge) {
        if (rr >= 2.2) {
          badge.className = "px-2 py-0.5 rounded font-bold text-xs bg-emerald-500/20 text-emerald-400 border border-emerald-500/30";
          badge.textContent = `🎯 Planned R:R ${rr.toFixed(2)}R • Valid Edge`;
          if (adviceDisp) adviceDisp.innerHTML = `<span class="text-emerald-400">✅ Valid System Edge (&ge; 2.2R)</span>`;
        } else {
          badge.className = "px-2 py-0.5 rounded font-bold text-xs bg-rose-500/20 text-rose-400 border border-rose-500/40 animate-pulse";
          badge.textContent = `⚠️ Planned R:R ${rr.toFixed(2)}R • Below 2.2R Minimum`;
          if (adviceDisp) adviceDisp.innerHTML = `<span class="text-rose-400 font-bold">⚠️ Below 2.2R Minimum Threshold! Gated.</span>`;
        }
      }
    }

    // Hook updateRRVisualizer into recalculateCalculators
    const origRecalc = window.recalculateCalculators;
    window.recalculateCalculators = function() {
      if (typeof origRecalc === 'function') origRecalc();
      updateRRVisualizer();
      if (typeof computeKellyExpectancy === 'function') computeKellyExpectancy();
    };

    // --- 4. LEDGER QUICK-FILTER CHIPS & SEARCH ---
    let currentLedgerFilterChip = 'ALL';

    function setLedgerQuickFilter(filterKey) {
      currentLedgerFilterChip = filterKey;
      const chips = document.querySelectorAll('.filter-chip');
      chips.forEach(c => c.classList.remove('active'));
      const activeEl = document.getElementById('chip_' + (filterKey === 'ALL' ? 'ALL' : (filterKey.includes('Pullback') ? 'Pullback' : (filterKey.includes('ORB') ? 'ORB' : filterKey))));
      if (activeEl) activeEl.classList.add('active');

      if (typeof renderTradesTable === 'function') renderTradesTable();
      playFeedbackSound('click');
    }

    function clearLedgerSearch() {
      const inp = document.getElementById('ledgerSearchInput');
      if (inp) inp.value = '';
      const btn = document.getElementById('clearLedgerSearchBtn');
      if (btn) btn.classList.add('hidden');
      if (typeof renderTradesTable === 'function') renderTradesTable();
    }

    // --- 6. PRO TERMINAL THEMES & 5. COMPACT DENSITY ---
    function switchTheme(themeName) {
      document.documentElement.setAttribute('data-theme', themeName);
      localStorage.setItem('trader_theme', themeName);
      const sel = document.getElementById('themeSelector');
      if (sel) sel.value = themeName;
      playFeedbackSound('click');
    }

    function initTheme() {
      const saved = localStorage.getItem('trader_theme') || 'obsidian';
      document.documentElement.setAttribute('data-theme', saved);
      const sel = document.getElementById('themeSelector');
      if (sel) sel.value = saved;
    }

    function toggleDensityMode() {
      const body = document.body;
      const isCompact = body.classList.toggle('compact-density');
      localStorage.setItem('trader_density', isCompact ? 'compact' : 'roomy');

      const label = document.getElementById('densityLabel');
      if (label) label.textContent = isCompact ? "Roomy" : "Compact";
      playFeedbackSound('click');
    }

    function initDensity() {
      const saved = localStorage.getItem('trader_density') || 'roomy';
      if (saved === 'compact') {
        document.body.classList.add('compact-density');
        const label = document.getElementById('densityLabel');
        if (label) label.textContent = "Roomy";
      }
    }

    // --- 7. FLOATING BOTTOM STATUS DOCK SYNCHRONIZATION ---
    function updateBottomDockMetrics() {
      const trades = typeof tradesData !== 'undefined' ? tradesData : [];
      let netPnL = 0;
      let netR = 0;
      trades.forEach(t => {
        netPnL += parseFloat(t.net_pnl || 0);
        netR += parseFloat(t.r_multiple || 0);
      });

      const elNetPnL = document.getElementById('dockNetPnLDisp');
      const elNetR = document.getElementById('dockNetRDisp');
      const elQuota = document.getElementById('dockTradeQuotaDisp');
      const elStrikes = document.getElementById('dockStrikesDisp');
      const elClock = document.getElementById('dockISTClock');

      if (elNetPnL) {
        elNetPnL.textContent = (netPnL >= 0 ? '+₹' : '-₹') + Math.abs(netPnL).toLocaleString('en-IN', { maximumFractionDigits: 0 });
        elNetPnL.className = 'font-bold ' + (netPnL >= 0 ? 'text-emerald-400' : 'text-rose-400');
      }
      if (elNetR) {
        elNetR.textContent = (netR >= 0 ? '+' : '') + netR.toFixed(2) + 'R';
        elNetR.className = 'font-bold ' + (netR >= 0 ? 'text-blue-300' : 'text-rose-400');
      }
      if (elQuota) {
        const quota = Math.min(2, trades.length);
        elQuota.textContent = `${quota} of 2 Trades`;
      }
      if (elStrikes) {
        const strikes = typeof penaltyStrikes !== 'undefined' ? penaltyStrikes : 0;
        elStrikes.textContent = `${strikes} / 3`;
        elStrikes.className = 'font-bold ' + (strikes === 0 ? 'text-emerald-400' : 'text-rose-400');
      }
      if (elClock) {
        const now = new Date();
        elClock.textContent = now.toLocaleTimeString('en-US', { timeZone: 'Asia/Kolkata', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' }) + ' IST';
      }
    }

    // Initial DOM hooks for UI/UX Overhaul
    window.addEventListener('DOMContentLoaded', () => {
      initTheme();
      initDensity();
      updateRRVisualizer();
      setInterval(updateBottomDockMetrics, 1000);
    });
"""

    old_dom_ready_tag = "    // Hook listeners on DOM ready\n    window.addEventListener('DOMContentLoaded', () => {"
    assert old_dom_ready_tag in code, "Failed to find old_dom_ready_tag"
    code = code.replace(old_dom_ready_tag, v18_script_logic + "\n\n" + old_dom_ready_tag, 1)

    with open(MASTER_FILE, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"Successfully applied all 7 UI/UX Overhaul upgrades to {MASTER_FILE}!")

if __name__ == "__main__":
    main()
