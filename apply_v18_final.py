#!/usr/bin/env python3
"""
Applies all 7 UI/UX and feature enhancements to build_master_v16.py:
1. Command Palette (Ctrl+K / Cmd+K)
2. Interactive Risk-to-Reward Live Visualizer Split-Bar
3. Visual P&L R-Multiple Sparkbars in Trade Ledger
4. Quick-Filter Chips & Instant Ledger Search + Column Sorting
5. High-Density Compact Pro Mode Toggle
6. High-Impact Pro Terminal Accent Theme Switcher (Obsidian, Bloomberg, Linear, Nordic)
   - FIX: Correctly closes @media print so all screen theme CSS rules apply!
7. Floating Institutional Bottom Status Dock
8. Complete Combat Mode HUD (IDs bound to execution form, ledger, and dropzone)
"""

import sys
import os

MASTER_FILE = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/build_master_v16.py"
BACKUP_FILE = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/build_master_v16.py.bak_uiux"

def build():
    # Read from clean backup
    with open(BACKUP_FILE, "r", encoding="utf-8") as f:
        code = f.read()

    # =========================================================================
    # FIX: Properly close @media print in new_head
    # =========================================================================
    unclosed_print_target = '      .no-print { display: none !important; }\n'
    assert unclosed_print_target in code, "Failed to find unclosed_print_target"
    code = code.replace(unclosed_print_target, '      .no-print { display: none !important; }\n    }\n', 1)

    # =========================================================================
    # 0. COMBAT MODE HUD CSS: High-focus styling, border animation & element hiding
    # =========================================================================
    old_combat_css = """    /* Combat Mode HUD (Minimalist Execution Window 09:15–10:30 AM) */
    body.combat-mode #tabSelectorContainer,
    body.combat-mode #phaseTrackerSection,
    body.combat-mode #tabContent2,
    body.combat-mode #tabContent3,
    body.combat-mode #tabContent4,
    body.combat-mode #tradesLedgerSection,
    body.combat-mode #screenshotDropzoneContainer {
      display: none !important;
    }
    body.combat-mode #combatBanner {
      display: flex !important;
    }
    body.combat-mode #executionFormCard {
      max-width: 850px;
      margin: 0 auto;
      border: 1px solid rgba(245, 158, 11, 0.4) !important;
      box-shadow: 0 0 35px rgba(245, 158, 11, 0.15) !important;
    }"""

    new_combat_css = """    /* Combat Mode HUD (Minimalist Execution Window 09:15–10:30 AM) */
    body.combat-mode #phaseTrackerSection,
    body.combat-mode #tradesLedgerSection,
    body.combat-mode #screenshotDropzoneContainer,
    body.combat-mode #tabContent2,
    body.combat-mode #tabContent3,
    body.combat-mode #tabContent4 {
      display: none !important;
    }
    body.combat-mode #combatBanner {
      display: flex !important;
    }
    body.combat-mode #executionFormCard {
      max-width: 900px;
      margin: 0 auto !important;
      border: 2px solid rgba(245, 158, 11, 0.6) !important;
      box-shadow: 0 0 45px rgba(245, 158, 11, 0.25), inset 0 0 20px rgba(245, 158, 11, 0.05) !important;
      animation: combatPulse 3s infinite ease-in-out;
    }
    @keyframes combatPulse {
      0%, 100% { border-color: rgba(245, 158, 11, 0.6); }
      50% { border-color: rgba(251, 191, 36, 0.95); }
    }"""

    assert old_combat_css in code, "Failed to find old_combat_css"
    code = code.replace(old_combat_css, new_combat_css, 1)

    # =========================================================================
    # 1. HEAD CSS: Comprehensive High-Impact Themes, Compact Density, Dock
    # =========================================================================
    v18_css = """
    /* ==================================================== */
    /* UI/UX OVERHAUL V18: STYLES, THEMES & DENSITY MODES  */
    /* ==================================================== */

    /* 6. Complete High-Impact Pro Terminal Accent Themes */

    /* --- BLOOMBERG AMBER THEME --- */
    html[data-theme="bloomberg"],
    body[data-theme="bloomberg"],
    [data-theme="bloomberg"] body {
      background-color: #000000 !important;
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(245, 158, 11, 0.25) 0%, transparent 65%),
        radial-gradient(circle at 100% 100%, rgba(217, 119, 6, 0.15) 0%, transparent 50%) !important;
      color: #FDF6B2 !important;
    }
    [data-theme="bloomberg"] header {
      background: rgba(10, 8, 2, 0.98) !important;
      border-bottom-color: rgba(245, 158, 11, 0.4) !important;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.9) !important;
    }
    [data-theme="bloomberg"] .glass-card,
    [data-theme="bloomberg"] [class*="glass-card"] {
      background-color: rgba(15, 11, 3, 0.96) !important;
      background-image: none !important;
      border-color: rgba(245, 158, 11, 0.3) !important;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.85), 0 0 15px rgba(245, 158, 11, 0.08) !important;
    }
    [data-theme="bloomberg"] #institutionalBottomDock {
      background: rgba(10, 8, 2, 0.98) !important;
      border-top-color: rgba(245, 158, 11, 0.4) !important;
    }
    [data-theme="bloomberg"] h1,
    [data-theme="bloomberg"] h2,
    [data-theme="bloomberg"] h3,
    [data-theme="bloomberg"] h4 {
      color: #FCD34D !important;
    }
    [data-theme="bloomberg"] .text-blue-400,
    [data-theme="bloomberg"] .text-blue-300,
    [data-theme="bloomberg"] .text-blue-500,
    [data-theme="bloomberg"] .text-sky-400,
    [data-theme="bloomberg"] .text-sky-300 {
      color: #F59E0B !important;
    }
    [data-theme="bloomberg"] .bg-blue-600,
    [data-theme="bloomberg"] .bg-blue-500 {
      background-color: #D97706 !important;
      border-color: #F59E0B !important;
      color: #000000 !important;
      font-weight: 700 !important;
    }
    [data-theme="bloomberg"] .border-blue-500,
    [data-theme="bloomberg"] .border-blue-500\\/30,
    [data-theme="bloomberg"] .border-blue-500\\/20,
    [data-theme="bloomberg"] .border-blue-500\\/60,
    [data-theme="bloomberg"] .border-slate-800,
    [data-theme="bloomberg"] .border-slate-700 {
      border-color: rgba(245, 158, 11, 0.28) !important;
    }
    [data-theme="bloomberg"] .bg-slate-900,
    [data-theme="bloomberg"] .bg-slate-950,
    [data-theme="bloomberg"] .bg-slate-900\\/80,
    [data-theme="bloomberg"] .bg-slate-950\\/80,
    [data-theme="bloomberg"] .bg-slate-950\\/90 {
      background-color: #0E0A02 !important;
    }
    [data-theme="bloomberg"] .bg-slate-800 {
      background-color: #1F1604 !important;
    }
    [data-theme="bloomberg"] input,
    [data-theme="bloomberg"] select,
    [data-theme="bloomberg"] textarea {
      background-color: #0A0701 !important;
      border-color: rgba(245, 158, 11, 0.4) !important;
      color: #FEF3C7 !important;
    }
    [data-theme="bloomberg"] input:focus,
    [data-theme="bloomberg"] select:focus,
    [data-theme="bloomberg"] textarea:focus {
      border-color: #F59E0B !important;
      box-shadow: 0 0 0 2px rgba(245, 158, 11, 0.35) !important;
    }
    [data-theme="bloomberg"] table thead tr,
    [data-theme="bloomberg"] table thead {
      background-color: #160F03 !important;
      color: #FCD34D !important;
    }
    [data-theme="bloomberg"] .filter-chip.active {
      background: linear-gradient(135deg, #D97706 0%, #B45309 100%) !important;
      color: #000000 !important;
      border-color: #FCD34D !important;
      font-weight: 800 !important;
      box-shadow: 0 0 12px rgba(245, 158, 11, 0.45) !important;
    }
    [data-theme="bloomberg"] kbd.hotkey-badge {
      color: #FCD34D !important;
      background: rgba(245, 158, 11, 0.2) !important;
      border-color: rgba(245, 158, 11, 0.45) !important;
    }

    /* --- LINEAR MONOCHROME THEME --- */
    html[data-theme="linear"],
    body[data-theme="linear"],
    [data-theme="linear"] body {
      background-color: #080A0D !important;
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(255, 255, 255, 0.1) 0%, transparent 60%),
        radial-gradient(circle at 100% 100%, rgba(148, 163, 184, 0.06) 0%, transparent 45%) !important;
      color: #E2E8F0 !important;
    }
    [data-theme="linear"] header {
      background: rgba(12, 15, 20, 0.98) !important;
      border-bottom-color: rgba(255, 255, 255, 0.16) !important;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7) !important;
    }
    [data-theme="linear"] .glass-card,
    [data-theme="linear"] [class*="glass-card"] {
      background-color: rgba(14, 18, 24, 0.94) !important;
      background-image: none !important;
      border-color: rgba(255, 255, 255, 0.14) !important;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.75) !important;
    }
    [data-theme="linear"] #institutionalBottomDock {
      background: rgba(12, 15, 20, 0.98) !important;
      border-top-color: rgba(255, 255, 255, 0.16) !important;
    }
    [data-theme="linear"] h1,
    [data-theme="linear"] h2,
    [data-theme="linear"] h3,
    [data-theme="linear"] h4 {
      color: #FFFFFF !important;
    }
    [data-theme="linear"] .text-blue-400,
    [data-theme="linear"] .text-blue-300,
    [data-theme="linear"] .text-blue-500 {
      color: #F8FAFC !important;
    }
    [data-theme="linear"] .bg-blue-600,
    [data-theme="linear"] .bg-blue-500 {
      background-color: #FFFFFF !important;
      color: #080A0D !important;
      border-color: #CBD5E1 !important;
      font-weight: 700 !important;
    }
    [data-theme="linear"] .border-blue-500,
    [data-theme="linear"] .border-blue-500\\/30,
    [data-theme="linear"] .border-blue-500\\/20,
    [data-theme="linear"] .border-blue-500\\/60,
    [data-theme="linear"] .border-slate-800,
    [data-theme="linear"] .border-slate-700 {
      border-color: rgba(255, 255, 255, 0.14) !important;
    }
    [data-theme="linear"] .bg-slate-900,
    [data-theme="linear"] .bg-slate-950,
    [data-theme="linear"] .bg-slate-900\\/80,
    [data-theme="linear"] .bg-slate-950\\/80,
    [data-theme="linear"] .bg-slate-950\\/90 {
      background-color: #10141A !important;
    }
    [data-theme="linear"] .bg-slate-800 {
      background-color: #1C232D !important;
    }
    [data-theme="linear"] input,
    [data-theme="linear"] select,
    [data-theme="linear"] textarea {
      background-color: #0C0F14 !important;
      border-color: rgba(255, 255, 255, 0.18) !important;
      color: #FFFFFF !important;
    }
    [data-theme="linear"] input:focus,
    [data-theme="linear"] select:focus,
    [data-theme="linear"] textarea:focus {
      border-color: #FFFFFF !important;
      box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.25) !important;
    }
    [data-theme="linear"] table thead tr,
    [data-theme="linear"] table thead {
      background-color: #161C24 !important;
      color: #F8FAFC !important;
    }
    [data-theme="linear"] .filter-chip.active {
      background: #FFFFFF !important;
      color: #080A0D !important;
      border-color: #E2E8F0 !important;
      font-weight: 800 !important;
      box-shadow: 0 0 12px rgba(255, 255, 255, 0.35) !important;
    }
    [data-theme="linear"] kbd.hotkey-badge {
      color: #F8FAFC !important;
      background: rgba(255, 255, 255, 0.12) !important;
      border-color: rgba(255, 255, 255, 0.3) !important;
    }

    /* --- NORDIC FROST THEME --- */
    html[data-theme="nordic"],
    body[data-theme="nordic"],
    [data-theme="nordic"] body {
      background-color: #020C16 !important;
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(6, 182, 212, 0.26) 0%, transparent 65%),
        radial-gradient(circle at 100% 100%, rgba(20, 184, 166, 0.15) 0%, transparent 45%) !important;
      color: #E0F2FE !important;
    }
    [data-theme="nordic"] header {
      background: rgba(3, 16, 28, 0.98) !important;
      border-bottom-color: rgba(6, 182, 212, 0.4) !important;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.8) !important;
    }
    [data-theme="nordic"] .glass-card,
    [data-theme="nordic"] [class*="glass-card"] {
      background-color: rgba(4, 20, 36, 0.95) !important;
      background-image: none !important;
      border-color: rgba(6, 182, 212, 0.32) !important;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.85), 0 0 15px rgba(6, 182, 212, 0.1) !important;
    }
    [data-theme="nordic"] #institutionalBottomDock {
      background: rgba(3, 16, 28, 0.98) !important;
      border-top-color: rgba(6, 182, 212, 0.4) !important;
    }
    [data-theme="nordic"] h1,
    [data-theme="nordic"] h2,
    [data-theme="nordic"] h3,
    [data-theme="nordic"] h4 {
      color: #67E8F9 !important;
    }
    [data-theme="nordic"] .text-blue-400,
    [data-theme="nordic"] .text-blue-300,
    [data-theme="nordic"] .text-blue-500 {
      color: #22D3EE !important;
    }
    [data-theme="nordic"] .bg-blue-600,
    [data-theme="nordic"] .bg-blue-500 {
      background-color: #0891B2 !important;
      color: #FFFFFF !important;
      border-color: #22D3EE !important;
      font-weight: 700 !important;
    }
    [data-theme="nordic"] .border-blue-500,
    [data-theme="nordic"] .border-blue-500\\/30,
    [data-theme="nordic"] .border-blue-500\\/20,
    [data-theme="nordic"] .border-blue-500\\/60,
    [data-theme="nordic"] .border-slate-800,
    [data-theme="nordic"] .border-slate-700 {
      border-color: rgba(6, 182, 212, 0.28) !important;
    }
    [data-theme="nordic"] .bg-slate-900,
    [data-theme="nordic"] .bg-slate-950,
    [data-theme="nordic"] .bg-slate-900\\/80,
    [data-theme="nordic"] .bg-slate-950\\/80,
    [data-theme="nordic"] .bg-slate-950\\/90 {
      background-color: #041A2E !important;
    }
    [data-theme="nordic"] .bg-slate-800 {
      background-color: #0C2844 !important;
    }
    [data-theme="nordic"] input,
    [data-theme="nordic"] select,
    [data-theme="nordic"] textarea {
      background-color: #031628 !important;
      border-color: rgba(6, 182, 212, 0.4) !important;
      color: #E0F2FE !important;
    }
    [data-theme="nordic"] input:focus,
    [data-theme="nordic"] select:focus,
    [data-theme="nordic"] textarea:focus {
      border-color: #06B6D4 !important;
      box-shadow: 0 0 0 2px rgba(6, 182, 212, 0.35) !important;
    }
    [data-theme="nordic"] table thead tr,
    [data-theme="nordic"] table thead {
      background-color: #07243E !important;
      color: #67E8F9 !important;
    }
    [data-theme="nordic"] .filter-chip.active {
      background: linear-gradient(135deg, #0891B2 0%, #06B6D4 100%) !important;
      color: #FFFFFF !important;
      border-color: #67E8F9 !important;
      font-weight: 800 !important;
      box-shadow: 0 0 12px rgba(6, 182, 212, 0.5) !important;
    }
    [data-theme="nordic"] kbd.hotkey-badge {
      color: #67E8F9 !important;
      background: rgba(6, 182, 212, 0.2) !important;
      border-color: rgba(6, 182, 212, 0.45) !important;
    }

    /* --- OBSIDIAN BLUE (DEFAULT) --- */
    html[data-theme="obsidian"],
    body[data-theme="obsidian"],
    [data-theme="obsidian"] body {
      background-color: #060913 !important;
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(30, 58, 138, 0.18) 0%, transparent 65%),
        radial-gradient(circle at 100% 100%, rgba(16, 185, 129, 0.08) 0%, transparent 45%) !important;
      color: #F1F5F9 !important;
    }

    /* 5. High-Density Compact Pro Density Mode */
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
    body.compact-density .space-y-5 > * + * {
      margin-top: 0.75rem !important;
    }
    body.compact-density .space-y-4 > * + * {
      margin-top: 0.65rem !important;
    }

    /* 7. Bottom clearance for institutional dock */
    body {
      padding-bottom: 3.75rem !important;
    }

    /* 1. Command Palette Modal Animations */
    #commandPaletteModal.active {
      display: flex !important;
    }
    .palette-item.selected {
      background: rgba(59, 130, 246, 0.25) !important;
      border-color: rgba(96, 165, 250, 0.45) !important;
    }

    /* 4. Filter Chips active state */
    .filter-chip.active {
      background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
      color: #FFFFFF !important;
      border-color: #60A5FA !important;
      box-shadow: 0 0 10px rgba(37, 99, 235, 0.35);
    }
"""

    old_style_target = "      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);\n    }\n\n    }\n  </style>\n</head>'''"
    assert old_style_target in code, "Failed to find old_style_target"
    code = code.replace(old_style_target, "      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);\n    }\n" + v18_css + "\n  </style>\n</head>'''", 1)

    # =========================================================================
    # 2. TOOLBAR: Add Palette Quick Pill, Theme Switcher & Density Toggle
    # =========================================================================
    old_toolbar_target = '        <!-- Combat Mode Minimalist HUD Button -->'
    new_toolbar_additions = """        <!-- Command Palette Quick Launcher -->
        <button onclick="openCommandPalette()" class="px-3 py-2 rounded-lg bg-blue-600/20 hover:bg-blue-600/30 text-blue-300 border border-blue-500/30 font-medium text-xs flex items-center gap-1.5 transition shadow-sm cursor-pointer" title="Global Command Palette (Hotkey: Ctrl+K / Cmd+K)">
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
        <button onclick="toggleDensityMode()" id="densityToggleBtn" class="px-2.5 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs font-mono transition cursor-pointer" title="Toggle Compact Pro Density Mode">
          <span id="densityIcon">📐</span>
          <span id="densityLabel">Compact</span>
        </button>
        <!-- Combat Mode Minimalist HUD Button -->"""
    assert old_toolbar_target in code, "Failed to find old_toolbar_target"
    code = code.replace(old_toolbar_target, new_toolbar_additions, 1)

    # =========================================================================
    # 3. TAB 1: FORM - Interactive Risk-to-Reward Live Visualizer Split-Bar
    # =========================================================================
    rr_visualizer_markup = """          <!-- 2. INTERACTIVE RISK-TO-REWARD LIVE VISUALIZER SPLIT-BAR -->
          <div id="rrVisualizerContainer" class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 space-y-2 font-mono transition-all duration-300">
            <div class="flex items-center justify-between text-xs">
              <div class="flex items-center gap-2">
                <span class="text-slate-400 uppercase font-semibold text-[10px]">Planned Edge Expectancy</span>
                <span id="rrRatioValueBadge" class="px-2 py-0.5 rounded font-bold text-xs bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                  🎯 Planned R:R 2.40R &bull; Valid Edge
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
          </div>
"""

    old_preflight_marker = "          <!-- MAE & MFE Excursion Inputs (Exit Efficiency & Stop Leak Diagnostics) -->"
    assert old_preflight_marker in code, "Failed to find old_preflight_marker"
    code = code.replace(old_preflight_marker, rr_visualizer_markup + "\n" + old_preflight_marker, 1)

    # In Step 7 dropzone: bind id="screenshotDropzoneContainer"
    old_dropzone_container = '<div class="bg-slate-900/50 p-3.5 rounded-xl border border-dashed border-slate-700 hover:border-blue-500/60 transition">'
    assert old_dropzone_container in code, "Failed to find old_dropzone_container"
    code = code.replace(old_dropzone_container, '<div id="screenshotDropzoneContainer" class="bg-slate-900/50 p-3.5 rounded-xl border border-dashed border-slate-700 hover:border-blue-500/60 transition">', 1)

    # =========================================================================
    # 4. TAB 1: LEDGER - Quick-Filter Chips & Instant Search & Column Sorting
    # =========================================================================
    code_insertion_marker = '    assert old_ledger_filters in content, "Failed to find old_ledger_filters"\n    content = content.replace(old_ledger_filters, new_ledger_filters, 1)'
    assert code_insertion_marker in code, "Failed to find code_insertion_marker"

    chips_injection = """    assert old_ledger_filters in content, "Failed to find old_ledger_filters"
    content = content.replace(old_ledger_filters, new_ledger_filters, 1)

    # 8.1 ATTACH COMBAT HUD CARD IDs (executionFormCard and tradesLedgerSection)
    old_form_card_header = r'''<section class="glass-card rounded-2xl p-6 shadow-2xl relative overflow-hidden">
        <div class="flex flex-col md:flex-row md:items-center justify-between pb-4 border-b border-slate-800/80 gap-3">'''
    new_form_card_header = r'''<section id="executionFormCard" class="glass-card rounded-2xl p-6 shadow-2xl relative overflow-hidden">
        <div class="flex flex-col md:flex-row md:items-center justify-between pb-4 border-b border-slate-800/80 gap-3">'''
    assert old_form_card_header in content, "Failed to find old_form_card_header"
    content = content.replace(old_form_card_header, new_form_card_header, 1)

    old_ledger_card = r'''      <!-- Active Trades Ledger & Filters -->
      <section class="glass-card rounded-2xl p-6 shadow-2xl">'''
    new_ledger_card = r'''      <!-- Active Trades Ledger & Filters -->
      <section id="tradesLedgerSection" class="glass-card rounded-2xl p-6 shadow-2xl">'''
    assert old_ledger_card in content, "Failed to find old_ledger_card"
    content = content.replace(old_ledger_card, new_ledger_card, 1)

    # 8.2 INJECT QUICK FILTER CHIPS ABOVE TABLE
    old_table_container = r'''        <!-- Scrollable Responsive Trades Table -->
        <div class="overflow-x-auto mt-4 rounded-xl border border-slate-800">'''
    new_table_container = r'''        <!-- 4. Interactive Quick-Filter Chips -->
        <div class="flex items-center gap-1.5 overflow-x-auto py-2.5 scrollbar-none" id="ledgerQuickFilterChipsContainer">
          <button type="button" onclick="setLedgerQuickFilter('ALL')" id="chip_ALL" class="filter-chip active px-2.5 py-1 rounded-lg bg-blue-600 text-white border border-blue-500 text-[11px] font-semibold whitespace-nowrap transition cursor-pointer">
            All Fills
          </button>
          <button type="button" onclick="setLedgerQuickFilter('Win')" id="chip_Win" class="filter-chip px-2.5 py-1 rounded-lg bg-slate-900 text-slate-400 hover:text-emerald-300 border border-slate-800 text-[11px] font-semibold whitespace-nowrap transition cursor-pointer">
            🟢 Wins
          </button>
          <button type="button" onclick="setLedgerQuickFilter('Loss')" id="chip_Loss" class="filter-chip px-2.5 py-1 rounded-lg bg-slate-900 text-slate-400 hover:text-rose-300 border border-slate-800 text-[11px] font-semibold whitespace-nowrap transition cursor-pointer">
            🔴 Losses
          </button>
          <button type="button" onclick="setLedgerQuickFilter('Breach')" id="chip_Breach" class="filter-chip px-2.5 py-1 rounded-lg bg-slate-900 text-slate-400 hover:text-amber-300 border border-slate-800 text-[11px] font-semibold whitespace-nowrap transition cursor-pointer">
            ⚠️ Rule Breaches
          </button>
          <button type="button" onclick="setLedgerQuickFilter('1m Pullback to 9EMA')" id="chip_Pullback" class="filter-chip px-2.5 py-1 rounded-lg bg-slate-900 text-slate-400 hover:text-teal-300 border border-slate-800 text-[11px] font-semibold whitespace-nowrap transition cursor-pointer">
            1m Pullback
          </button>
          <button type="button" onclick="setLedgerQuickFilter('Opening Range Breakout (ORB)')" id="chip_ORB" class="filter-chip px-2.5 py-1 rounded-lg bg-slate-900 text-slate-400 hover:text-teal-300 border border-slate-800 text-[11px] font-semibold whitespace-nowrap transition cursor-pointer">
            ORB Breakout
          </button>
        </div>

        <!-- Scrollable Responsive Trades Table -->
        <div class="overflow-x-auto mt-2 rounded-xl border border-slate-800">'''
    assert old_table_container in content, "Failed to find old_table_container"
    content = content.replace(old_table_container, new_table_container, 1)

    # 8.3 MAKE TABLE HEADERS INTERACTIVE & SORTABLE
    old_table_headers = r'''              <tr class="bg-slate-900/90 text-slate-400 uppercase text-[10px] font-bold tracking-wider border-b border-slate-800">
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
                <th class="py-3 px-3 text-center">Realized R</th>'''
    new_table_headers = r'''              <tr class="bg-slate-900/90 text-slate-400 uppercase text-[10px] font-bold tracking-wider border-b border-slate-800 select-none">
                <th class="py-3 px-3 cursor-pointer hover:text-white transition" onclick="sortLedgerBy('id')" title="Click to sort by ID">Trade ID <span id="sort_arrow_id">↕</span></th>
                <th class="py-3 px-3 cursor-pointer hover:text-white transition" onclick="sortLedgerBy('date')" title="Click to sort by Date">Date &bull; Time <span id="sort_arrow_date">↕</span></th>
                <th class="py-3 px-3 cursor-pointer hover:text-white transition" onclick="sortLedgerBy('symbol')" title="Click to sort by Symbol">Symbol <span id="sort_arrow_symbol">↕</span></th>
                <th class="py-3 px-3">Side</th>
                <th class="py-3 px-3 text-right cursor-pointer hover:text-white transition" onclick="sortLedgerBy('entry_price')" title="Click to sort by Entry Price">Entry <span id="sort_arrow_entry_price">↕</span></th>
                <th class="py-3 px-3 text-right">Stop</th>
                <th class="py-3 px-3 text-right">Exit</th>
                <th class="py-3 px-3 text-right">Qty</th>
                <th class="py-3 px-3 text-center cursor-pointer hover:text-white transition" onclick="sortLedgerBy('rr_planned')" title="Click to sort by Planned RR">Planned RR <span id="sort_arrow_rr_planned">↕</span></th>
                <th class="py-3 px-3 text-right">Costs</th>
                <th class="py-3 px-3 text-right cursor-pointer hover:text-white transition" onclick="sortLedgerBy('net_pnl')" title="Click to sort by Net P&L">Net P&amp;L <span id="sort_arrow_net_pnl">↕</span></th>
                <th class="py-3 px-3 text-center cursor-pointer hover:text-white transition" onclick="sortLedgerBy('r_multiple')" title="Click to sort by Realized R">Realized R <span id="sort_arrow_r_multiple">↕</span></th>'''
    assert old_table_headers in content, "Failed to find old_table_headers"
    content = content.replace(old_table_headers, new_table_headers, 1)"""

    code = code.replace(code_insertion_marker, chips_injection, 1)

    # =========================================================================
    # 5. TRADE TABLE ROW: Visual P&L R-Multiple Sparkbars in Realized R column
    # =========================================================================
    old_outcome_cell_marker = "    # Outcome cell in renderTradesTable to include Execution Grade badge"
    assert old_outcome_cell_marker in code, "Failed to find old_outcome_cell_marker"

    sparkbar_injection = """    # 3. Visual P&L R-Multiple Sparkbar in Realized R column
    old_realized_r_cell = r'''            <td class="py-2.5 px-3 text-center font-mono font-bold ${realizedR >= 0 ? 'text-emerald-400' : 'text-rose-400'}">
              ${realizedR >= 0 ? '+' : ''}${realizedR}R
            </td>'''
    new_realized_r_cell = r'''            <td class="py-2.5 px-3 text-center font-mono">
              <div class="flex flex-col items-center gap-1">
                <span class="font-bold text-[11px] ${realizedR >= 0 ? 'text-emerald-400' : 'text-rose-400'}">
                  ${realizedR >= 0 ? '+' : ''}${realizedR}R
                </span>
                <div class="w-14 bg-slate-900 rounded-full h-1.5 overflow-hidden flex border border-slate-800" title="Realized: ${realizedR}R">
                  ${realizedR >= 0 
                    ? `<div class="bg-emerald-500 h-full rounded-full transition-all" style="width: ${Math.min(100, Math.max(12, (realizedR / 3.0) * 100))}%"></div>` 
                    : (t.rule_violation === 'Y' 
                        ? `<div class="bg-amber-500 h-full rounded-full transition-all" style="width: ${Math.min(100, Math.max(12, (Math.abs(realizedR) / 1.5) * 100))}%"></div>`
                        : `<div class="bg-rose-500 h-full rounded-full transition-all" style="width: ${Math.min(100, Math.max(12, (Math.abs(realizedR) / 1.5) * 100))}%"></div>`
                      )
                  }
                </div>
              </div>
            </td>'''
    assert old_realized_r_cell in content, "Failed to find old_realized_r_cell"
    content = content.replace(old_realized_r_cell, new_realized_r_cell, 1)

    # Outcome cell in renderTradesTable to include Execution Grade badge"""

    code = code.replace(old_outcome_cell_marker, sparkbar_injection, 1)

    # =========================================================================
    # 6. ENHANCE LEDGER FILTER SCRIPT: Support quick filter chips & column sorting
    # =========================================================================
    old_table_filter_block = """    # Update ledger filter for strategy
    old_table_filter = r'''      const outcomeFilter = document.getElementById('outcomeFilter').value;

      let filtered = [...tradesData];'''

    new_table_filter = r'''      const outcomeFilter = document.getElementById('outcomeFilter').value;
      const strategyElem = document.getElementById('strategyFilter');
      const strategyVal = strategyElem ? strategyElem.value : 'ALL';

      let filtered = [...tradesData];
      if (strategyVal !== 'ALL') {
        filtered = filtered.filter(t => (t.setup_name || '') === strategyVal);
      }'''"""

    new_table_filter_block = """    # Update ledger filter for strategy, quick chips & column sorting
    old_table_filter = r'''      const outcomeFilter = document.getElementById('outcomeFilter').value;

      let filtered = [...tradesData];'''

    new_table_filter = r'''      const outcomeFilter = document.getElementById('outcomeFilter').value;
      const strategyElem = document.getElementById('strategyFilter');
      const strategyVal = strategyElem ? strategyElem.value : 'ALL';

      let filtered = [...tradesData];
      if (strategyVal !== 'ALL') {
        filtered = filtered.filter(t => (t.setup_name || '') === strategyVal);
      }

      // Quick Filter Chips Integration
      if (typeof currentLedgerFilterChip !== 'undefined' && currentLedgerFilterChip !== 'ALL') {
        if (currentLedgerFilterChip === 'Win') {
          filtered = filtered.filter(t => t.outcome === 'Win');
        } else if (currentLedgerFilterChip === 'Loss') {
          filtered = filtered.filter(t => t.outcome === 'Loss');
        } else if (currentLedgerFilterChip === 'Breach') {
          filtered = filtered.filter(t => t.rule_violation === 'Y' || (typeof t.checklist_score !== 'undefined' && t.checklist_score < 4));
        } else {
          filtered = filtered.filter(t => (t.setup_name || '') === currentLedgerFilterChip);
        }
      }

      // Column Sorting Integration
      if (typeof currentLedgerSortCol !== 'undefined' && currentLedgerSortCol) {
        filtered.sort((a, b) => {
          let valA = a[currentLedgerSortCol];
          let valB = b[currentLedgerSortCol];
          if (['net_pnl', 'r_multiple', 'entry_price', 'rr_planned', 'qty', 'costs'].includes(currentLedgerSortCol)) {
            valA = parseFloat(valA || 0);
            valB = parseFloat(valB || 0);
          } else {
            valA = String(valA || '').toLowerCase();
            valB = String(valB || '').toLowerCase();
          }
          if (valA < valB) return currentLedgerSortAsc ? -1 : 1;
          if (valA > valB) return currentLedgerSortAsc ? 1 : -1;
          return 0;
        });
      }'''"""

    assert old_table_filter_block in code, "Failed to find old_table_filter_block"
    code = code.replace(old_table_filter_block, new_table_filter_block, 1)

    # =========================================================================
    # 7. INJECT MODAL: Command Palette (Ctrl+K / Cmd+K)
    # =========================================================================
    command_palette_modal = """  <!-- ========================================== -->
  <!-- MODAL: 1. GLOBAL COMMAND PALETTE (CTRL+K / CMD+K) -->
  <!-- ========================================== -->
  <div id="commandPaletteModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-start justify-center pt-20 p-4" onclick="closeCommandPalette()">
    <div class="glass-card rounded-2xl w-full max-w-2xl border border-blue-500/40 shadow-2xl p-4 relative overflow-hidden" onclick="event.stopPropagation()">
      <!-- Search Input Box -->
      <div class="flex items-center gap-3 pb-3 border-b border-slate-800">
        <span class="text-blue-400 text-lg">⌘</span>
        <input type="text" id="paletteSearchInput" oninput="filterPaletteCommands(this.value)" placeholder="Type a command or jump to view... (e.g. 'long', 'combat', 'dossier', 'theme')" class="w-full bg-transparent text-white text-sm font-mono placeholder-slate-500 focus:outline-none">
        <kbd class="hotkey-badge text-[10px]">Esc</kbd>
      </div>

      <!-- Quick Commands List -->
      <div id="paletteResultsList" class="mt-3 max-h-80 overflow-y-auto space-y-1 text-xs">
        <!-- Populated dynamically by JS -->
      </div>

      <div class="mt-3 pt-2 border-t border-slate-800 flex items-center justify-between text-[10px] text-slate-500 font-mono">
        <div class="flex items-center gap-2">
          <span>Navigate: <kbd class="hotkey-badge text-[9px] px-1 py-0">↑</kbd><kbd class="hotkey-badge text-[9px] px-1 py-0">↓</kbd></span>
          <span>Execute: <kbd class="hotkey-badge text-[9px] px-1 py-0">↵</kbd></span>
        </div>
        <span>Trader Reset OS &bull; Command Hub</span>
      </div>
    </div>
  </div>
"""

    old_modals_start = "all_modals_markup = r'''  <!-- ========================================== -->"
    assert old_modals_start in code, "Failed to find old_modals_start"
    code = code.replace(old_modals_start, "all_modals_markup = r'''" + command_palette_modal + "\n  <!-- ========================================== -->", 1)

    # =========================================================================
    # 8. SCRIPT LOGIC: Palette Engine, Visualizer, Quick Chips, Dynamic Themes, Dock, Combat HUD
    # =========================================================================
    v18_script_logic = """
    // ==========================================
    // UI/UX OVERHAUL V18 JAVASCRIPT ENGINE
    // ==========================================

    // --- 0. ENHANCED COMBAT HUD TOGGLE ---
    const origToggleCombatMode = window.toggleCombatMode;
    window.toggleCombatMode = function() {
      if (typeof origToggleCombatMode === 'function') {
        origToggleCombatMode();
      } else {
        isCombatMode = !isCombatMode;
        if (isCombatMode) {
          document.body.classList.add('combat-mode');
          if (typeof switchTab === 'function') switchTab(1);
        } else {
          document.body.classList.remove('combat-mode');
        }
      }

      // Synchronize all HUD buttons & pills
      const btn = document.getElementById('combatModeBtn');
      const label = document.getElementById('combatModeLabel');
      const dockBtn = document.getElementById('dockCombatBtn');

      if (document.body.classList.contains('combat-mode')) {
        if (btn) btn.className = "px-3 py-2 rounded-lg bg-amber-500 text-black font-extrabold text-xs flex items-center gap-1.5 transition shadow-lg shadow-amber-500/40 ring-2 ring-amber-400 cursor-pointer";
        if (label) label.textContent = "Exit Combat";
        if (dockBtn) {
          dockBtn.className = "px-2 py-0.5 rounded bg-amber-500 text-black border border-amber-400 text-[10px] font-extrabold flex items-center gap-1 transition cursor-pointer";
        }
      } else {
        if (btn) btn.className = "px-3 py-2 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/30 font-bold text-xs flex items-center gap-1.5 transition shadow-sm cursor-pointer";
        if (label) label.textContent = "Combat HUD";
        if (dockBtn) {
          dockBtn.className = "px-2 py-0.5 rounded bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[10px] font-bold flex items-center gap-1 transition cursor-pointer";
        }
      }
    };

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
            <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-800 text-slate-400">${cmd.category}</span>
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
      const targetIdx = idx !== undefined ? idx : paletteSelectedIdx;
      const cmd = list[targetIdx];
      if (cmd && typeof cmd.action === 'function') {
        closeCommandPalette();
        cmd.action();
        playFeedbackSound('click');
      }
    }

    // Global Keydown Listener for Ctrl+K / Cmd+K and Palette Arrow Navigation
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
        } else if (e.key === 'Escape') {
          e.preventDefault();
          closeCommandPalette();
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

    // Wrap recalculateCalculators to update RR visualizer
    const origRecalculateCalculators = window.recalculateCalculators;
    window.recalculateCalculators = function() {
      if (typeof origRecalculateCalculators === 'function') origRecalculateCalculators();
      updateRRVisualizer();
      if (typeof computeKellyExpectancy === 'function') computeKellyExpectancy();
    };

    // --- 4. QUICK FILTER CHIPS & SORTING ENGINE ---
    let currentLedgerFilterChip = 'ALL';
    let currentLedgerSortCol = 'id';
    let currentLedgerSortAsc = false;

    function setLedgerQuickFilter(filterKey) {
      currentLedgerFilterChip = filterKey;
      const chips = document.querySelectorAll('.filter-chip');
      chips.forEach(c => {
        c.classList.remove('active', 'bg-blue-600', 'text-white');
        c.classList.add('bg-slate-900', 'text-slate-400');
      });

      const chipId = 'chip_' + (filterKey === 'ALL' ? 'ALL' : (filterKey.includes('Pullback') ? 'Pullback' : (filterKey.includes('ORB') ? 'ORB' : filterKey)));
      const activeEl = document.getElementById(chipId);
      if (activeEl) {
        activeEl.classList.remove('bg-slate-900', 'text-slate-400');
        activeEl.classList.add('active', 'bg-blue-600', 'text-white');
      }

      if (typeof renderTradesTable === 'function') renderTradesTable();
      playFeedbackSound('click');
    }

    function sortLedgerBy(col) {
      if (currentLedgerSortCol === col) {
        currentLedgerSortAsc = !currentLedgerSortAsc;
      } else {
        currentLedgerSortCol = col;
        currentLedgerSortAsc = (col === 'symbol' || col === 'date') ? true : false;
      }

      // Update sort arrow indicators
      const cols = ['id', 'date', 'symbol', 'entry_price', 'rr_planned', 'net_pnl', 'r_multiple'];
      cols.forEach(c => {
        const arrowEl = document.getElementById(`sort_arrow_${c}`);
        if (arrowEl) {
          if (c === currentLedgerSortCol) {
            arrowEl.textContent = currentLedgerSortAsc ? '▲' : '▼';
            arrowEl.className = 'text-blue-400 font-bold';
          } else {
            arrowEl.textContent = '↕';
            arrowEl.className = 'text-slate-600';
          }
        }
      });

      if (typeof renderTradesTable === 'function') renderTradesTable();
      playFeedbackSound('click');
    }

    // --- 6. PRO TERMINAL THEMES & 5. COMPACT DENSITY ---
    function switchTheme(themeName) {
      if (!themeName) themeName = 'obsidian';
      document.documentElement.setAttribute('data-theme', themeName);
      if (document.body) {
        document.body.setAttribute('data-theme', themeName);
      }
      localStorage.setItem('trader_theme', themeName);
      const sel = document.getElementById('themeSelector');
      if (sel) sel.value = themeName;
      if (typeof playFeedbackSound === 'function') playFeedbackSound('click');
    }

    function initTheme() {
      const saved = localStorage.getItem('trader_theme') || 'obsidian';
      document.documentElement.setAttribute('data-theme', saved);
      if (document.body) {
        document.body.setAttribute('data-theme', saved);
      }
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
        const count = trades.length;
        if (count >= 2) {
          elQuota.textContent = `2/2 Trades (Locked)`;
          elQuota.className = 'text-amber-400 font-bold';
        } else {
          elQuota.textContent = `${count} of 2 Trades`;
          elQuota.className = 'text-white font-bold';
        }
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
"""

    old_dom_ready = "    // Hook listeners on DOM ready\n    window.addEventListener('DOMContentLoaded', () => {"
    assert old_dom_ready in code, "Failed to find old_dom_ready"

    dom_ready_additions = """      initTheme();
      initDensity();
      updateRRVisualizer();
      updateBottomDockMetrics();
      setInterval(updateBottomDockMetrics, 1000);
"""

    code = code.replace(old_dom_ready, v18_script_logic + "\n\n" + old_dom_ready + "\n" + dom_ready_additions, 1)

    # =========================================================================
    # 9. FLOATING BOTTOM STATUS DOCK MARKUP (Injected right before </body>)
    # =========================================================================
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
      <span class="flex items-center gap-1 text-[11px] text-slate-400" title="Low-Latency Execution Engine Status">
        <span>📶</span>
        <span id="dockLatencyDisp" class="text-emerald-400 font-bold">18ms</span>
      </span>
    </div>

    <!-- Center: Session Quota & P&L Snapshot -->
    <div class="flex items-center gap-3 text-xs">
      <span>Quota: <strong id="dockTradeQuotaDisp" class="text-white font-bold">1 of 2 Trades</strong></span>
      <span class="text-slate-700">&bull;</span>
      <span>Net: <strong id="dockNetPnLDisp" class="text-emerald-400 font-bold">+₹0</strong></span>
      <span class="text-slate-700">&bull;</span>
      <span>Realized: <strong id="dockNetRDisp" class="text-blue-300 font-bold">+0.00R</strong></span>
      <span class="text-slate-700">&bull;</span>
      <span>Strikes: <strong id="dockStrikesDisp" class="text-emerald-400 font-bold">0 / 3</strong></span>
    </div>

    <!-- Right: Quick Navigation & Palette Pills -->
    <div class="flex items-center gap-2">
      <button onclick="toggleCombatMode()" id="dockCombatBtn" class="px-2 py-0.5 rounded bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[10px] font-bold flex items-center gap-1 transition cursor-pointer" title="Toggle Combat Mode HUD (Hotkey: H)">
        <span>🎯 Combat</span>
        <kbd class="hotkey-badge text-[9px] px-1 py-0">H</kbd>
      </button>
      <button onclick="openCommandPalette()" class="px-2 py-0.5 rounded bg-blue-500/10 hover:bg-blue-500/20 text-blue-300 border border-blue-500/30 text-[10px] font-bold flex items-center gap-1 transition cursor-pointer" title="Open Command Palette (Hotkey: Ctrl+K / Cmd+K)">
        <span>⌘ Palette</span>
        <kbd class="hotkey-badge text-[9px] px-1 py-0">Ctrl+K</kbd>
      </button>
      <button onclick="openHotkeyModal()" class="px-1.5 py-0.5 rounded bg-slate-800 text-slate-400 hover:text-white border border-slate-700 text-[10px] transition cursor-pointer" title="Hotkeys Cheatsheet (Hotkey: ?)">
        <kbd class="hotkey-badge text-[9px] px-1 py-0">?</kbd>
      </button>
    </div>
  </div>
"""

    old_closing_script_target = r'content = content.replace("  </script>\n</body>", f"{master_script_extension}\n  </script>\n</body>", 1)'
    assert old_closing_script_target in code, "Failed to find old_closing_script_target"

    dock_replacement_code = r'''bottom_dock_markup = """''' + bottom_dock_markup + r'''"""
    content = content.replace("  </script>\n</body>", f"{master_script_extension}\n  </script>\n" + bottom_dock_markup + "\n</body>", 1)'''

    code = code.replace(old_closing_script_target, dock_replacement_code, 1)

    # Save to MASTER_FILE
    with open(MASTER_FILE, "w", encoding="utf-8") as f:
        f.write(code)

    print("Successfully transformed build_master_v16.py with Combat HUD IDs, fixed CSS hierarchy and complete high-impact theme system!")

if __name__ == "__main__":
    build()
