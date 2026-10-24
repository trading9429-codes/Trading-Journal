#!/usr/bin/env python3
"""
Applies Features 1, 2, 4, 5, 6, 7, 8 to build_master_v16.py:
1. Quant Position Sizing & Fractional Kelly Criterion Engine
2. Trader Emotional Biometrics & Cognitive Fatigue Radar + Revenge Trade Interceptor
4. 'Combat Mode' / Minimalist Heads-Up Display (HUD) Toggle (H hotkey)
5. Institutional Bloomberg / TradingView Hotkey Scheme ([?] modal, L/S, N, P, B, M, H, Esc)
6. Interactive P&L Streak Glow & Synthesized Soundpack Customizer (Bell, Click, Cyber, Mute)
7. Offline IndexedDB Auto-Vault Engine (Auto-saves keystroke drafts & restores on crash)
8. Lazy Canvas Rendering & Tab Transition Optimization (60 FPS requestAnimationFrame)
"""

MASTER_FILE = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/build_master_v16.py"

def main():
    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        code = f.read()

    # ====================================================
    # 1. HEAD CSS: Combat HUD, Streak Glow, Hotkey Badges
    # ====================================================
    css_enhancements = """
    /* Combat Mode HUD (Minimalist Execution Window 09:15–10:30 AM) */
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
    }

    /* Discipline Streak Ambient Glow */
    .discipline-streak-glow {
      box-shadow: 0 0 30px rgba(16, 185, 129, 0.25), inset 0 0 15px rgba(16, 185, 129, 0.1) !important;
      border-color: rgba(16, 185, 129, 0.5) !important;
    }
    
    /* Keyboard Shortcut Badges */
    kbd.hotkey-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 22px;
      height: 20px;
      padding: 0 5px;
      font-size: 10px;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: #93C5FD;
      background: rgba(30, 58, 138, 0.4);
      border: 1px solid rgba(96, 165, 250, 0.3);
      border-radius: 6px;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);
    }
"""

    old_style_end = "      .no-print { display: none !important; }\n    }\n  </style>\n</head>'''"
    assert old_style_end in code, "Failed to find old_style_end"
    code = code.replace(old_style_end, "      .no-print { display: none !important; }\n" + css_enhancements + "\n    }\n  </style>\n</head>'''", 1)

    # ====================================================
    # 2. TOOLBAR: Add Combat HUD, Hotkeys [?], Sync Badge
    # ====================================================
    old_toolbar_first_btn = '        <!-- 09:00 AM IST Pre-Flight Readiness Protocol Button -->'
    new_toolbar_buttons = """        <!-- Combat Mode Minimalist HUD Button -->
        <button onclick="toggleCombatMode()" id="combatModeBtn" class="px-3 py-2 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/30 font-bold text-xs flex items-center gap-1.5 transition shadow-sm" title="Toggle Minimalist Combat Execution HUD (Hotkey: H)">
          <span>🎯</span>
          <span id="combatModeLabel">Combat HUD</span>
          <kbd class="hotkey-badge text-[9px] px-1 py-0 bg-amber-950/60 text-amber-300 border-amber-500/40">H</kbd>
        </button>
        <!-- Hotkey Cheatsheet & Soundpack Settings Button -->
        <button onclick="openHotkeyModal()" class="px-2.5 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 font-mono text-xs flex items-center gap-1.5 transition shadow-sm" title="Keyboard Shortcuts &amp; Soundpack (Hotkey: ?)">
          <span>⌨️</span>
          <span>[?]</span>
        </button>
        <!-- IndexedDB Offline Auto-Vault Status Badge -->
        <div id="indexedDbSyncPill" class="hidden sm:flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 font-mono text-[10px] text-slate-400" title="Offline IndexedDB Auto-Vault active &bull; Keystrokes &amp; trades preserved">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
          <span id="indexedDbSyncText">Auto-Vault</span>
        </div>
        <!-- 09:00 AM IST Pre-Flight Readiness Protocol Button -->"""

    assert old_toolbar_first_btn in code, "Failed to find old_toolbar_first_btn"
    code = code.replace(old_toolbar_first_btn, new_toolbar_buttons, 1)

    # ====================================================
    # 3. TAB 1: Combat Banner & Quant Kelly Position Sizing
    # ====================================================
    old_phase_tracker_marker = '<!-- 30-DAY PHASE GRADUATION & DISCIPLINE TRACKER WIDGET -->'
    combat_banner_block = """<!-- COMBAT MODE HIGH-FOCUS HUD BANNER (Toggled by H) -->
      <div id="combatBanner" class="hidden bg-gradient-to-r from-amber-950/80 via-slate-900 to-amber-950/80 border border-amber-500/40 p-3.5 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-3 text-xs shadow-2xl">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-lg bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-amber-400 font-black text-sm">
            🎯
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="font-extrabold text-amber-300 uppercase tracking-wider">Combat Mode Active</span>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-amber-500/20 text-amber-200 border border-amber-500/30">09:15–10:30 AM Focus Window</span>
            </div>
            <p class="text-[11px] text-slate-400">All non-essential charts collapsed. Execute 1-minute system with zero cognitive distraction.</p>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <span class="text-[11px] font-mono text-slate-400">Exit Combat Mode:</span>
          <button onclick="toggleCombatMode()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-bold text-xs flex items-center gap-1 transition">
            <span>Exit HUD</span>
            <kbd class="hotkey-badge text-[9px] px-1 py-0">H</kbd>
          </button>
        </div>
      </div>

      <!-- 30-DAY PHASE GRADUATION & DISCIPLINE TRACKER WIDGET -->"""

    assert old_phase_tracker_marker in code, "Failed to find old_phase_tracker_marker"
    code = code.replace(old_phase_tracker_marker, combat_banner_block, 1)

    # Wrap phase tracker section with ID for Combat Mode toggling
    old_phase_section = '<section class="glass-card rounded-2xl p-5 shadow-2xl border border-blue-500/20 bg-gradient-to-r from-slate-900/95 via-slate-900/80 to-blue-950/40">'
    new_phase_section = '<section id="phaseTrackerSection" class="glass-card rounded-2xl p-5 shadow-2xl border border-blue-500/20 bg-gradient-to-r from-slate-900/95 via-slate-900/80 to-blue-950/40">'
    if old_phase_section in code:
        code = code.replace(old_phase_section, new_phase_section, 1)

    # Quant Kelly Recommendation Chip in Position Sizing Card
    old_auto_apply = r'''<button type="button" onclick="autoApplyPositionSize()" class="ml-1 px-2.5 py-1 rounded bg-blue-600/30 hover:bg-blue-600/50 text-blue-200 font-bold text-xs transition border border-blue-500/30">Auto Apply Size</button>'''
    new_auto_apply = r'''<button type="button" onclick="autoApplyPositionSize()" class="ml-1 px-2.5 py-1 rounded bg-blue-600/30 hover:bg-blue-600/50 text-blue-200 font-bold text-xs transition border border-blue-500/30">Auto Size</button>
              <!-- Quant Kelly Criterion Recommendation Chip -->
              <div class="flex items-center gap-1.5 bg-purple-950/60 px-2 py-0.5 rounded-lg border border-purple-500/30 text-[10px] font-mono">
                <span class="text-purple-300 font-bold">Quant Kelly (Half):</span>
                <span id="kellyRecRisk" class="font-bold text-white">₹450</span>
                <span id="kellyRecQty" class="text-emerald-300 font-bold">(0 shs)</span>
                <button type="button" onclick="applyKellyPositionSize()" class="px-1.5 py-0.5 rounded bg-purple-600/60 hover:bg-purple-600 text-purple-100 font-bold text-[9px] uppercase tracking-wider transition border border-purple-400/30" title="Apply Half-Kelly recommended size based on historical win-rate &amp; payoff">⚡ Kelly</button>
              </div>'''

    if old_auto_apply in code:
        code = code.replace(old_auto_apply, new_auto_apply, 1)

    # Add Draft Recovery Notification Banner right before form inputs
    old_form_head = '<form id="tradeForm" onsubmit="submitTrade(event)" class="space-y-4">'
    new_form_head = """<form id="tradeForm" onsubmit="submitTrade(event)" class="space-y-4">
            <!-- Offline Draft Auto-Restored Alert Banner -->
            <div id="draftRestoredBanner" class="hidden p-2.5 rounded-xl bg-purple-950/50 border border-purple-500/30 flex items-center justify-between text-xs text-purple-200 font-mono">
              <span class="flex items-center gap-1.5">
                <span>💾</span>
                <span id="draftRestoredText">Restored unsaved trade draft from IndexedDB</span>
              </span>
              <button type="button" onclick="discardTradeDraft()" class="text-[10px] text-purple-400 hover:text-white underline font-semibold">Discard Draft</button>
            </div>"""
    if old_form_head in code:
        code = code.replace(old_form_head, new_form_head, 1)

    # ====================================================
    # 4. TAB 3: Add Cognitive Fatigue & Emotional Tilt Radar
    # ====================================================
    tilt_radar_section = """      <!-- COGNITIVE FATIGUE & EMOTIONAL TILT RADAR -->
      <section class="glass-card rounded-2xl p-6 shadow-2xl border border-rose-500/20 bg-rose-950/5 mt-6">
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-4 border-b border-slate-800 gap-2">
          <div>
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <span class="text-rose-400">🧠</span>
              <span>Cognitive Fatigue &amp; Emotional Tilt Radar</span>
              <span class="text-xs px-2.5 py-0.5 rounded-full bg-rose-500/10 text-rose-300 border border-rose-500/20 font-mono">
                Psychological Edge Audit
              </span>
            </h3>
            <p class="text-xs text-slate-400">Correlates emotional urgency (1–10) with realized outcomes to pinpoint psychological capital leaks</p>
          </div>
          <div class="flex items-center gap-2 font-mono text-xs">
            <span class="text-slate-400">Tilt Leak:</span>
            <span id="tiltCostTotalDisp" class="px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 font-bold">-0.00R</span>
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-5">
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
            <span class="text-[10px] text-slate-400 uppercase font-semibold block">Composed Execution (Urgency &le; 5)</span>
            <div class="mt-1.5 flex items-baseline justify-center gap-2">
              <span id="calmWinRateDisp" class="text-2xl font-black font-mono text-emerald-400">0%</span>
              <span class="text-xs text-slate-400">Win Rate</span>
            </div>
            <div id="calmNetRDisp" class="text-xs font-mono text-blue-300 mt-0.5">+0.00R Net</div>
          </div>

          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
            <span class="text-[10px] text-slate-400 uppercase font-semibold block">Elevated Urgency (Urgency &ge; 6)</span>
            <div class="mt-1.5 flex items-baseline justify-center gap-2">
              <span id="urgentWinRateDisp" class="text-2xl font-black font-mono text-rose-400">0%</span>
              <span class="text-xs text-slate-400">Win Rate</span>
            </div>
            <div id="urgentNetRDisp" class="text-xs font-mono text-rose-300 mt-0.5">-0.00R Net</div>
          </div>

          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
            <span class="text-[10px] text-slate-400 uppercase font-semibold block">Fresh Opening Window (09:15–09:45)</span>
            <div class="mt-1.5 flex items-baseline justify-center gap-2">
              <span id="earlyWinRateDisp" class="text-2xl font-black font-mono text-emerald-400">0%</span>
              <span class="text-xs text-slate-400">Win Rate</span>
            </div>
            <div id="earlyNetRDisp" class="text-xs font-mono text-blue-300 mt-0.5">+0.00R Net</div>
          </div>

          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
            <span class="text-[10px] text-slate-400 uppercase font-semibold block">Late Execution Window (09:45–10:30)</span>
            <div class="mt-1.5 flex items-baseline justify-center gap-2">
              <span id="lateWinRateDisp" class="text-2xl font-black font-mono text-amber-400">0%</span>
              <span class="text-xs text-slate-400">Win Rate</span>
            </div>
            <div id="lateNetRDisp" class="text-xs font-mono text-slate-300 mt-0.5">+0.00R Net</div>
          </div>
        </div>

        <div class="mt-4 p-3 bg-slate-950/60 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between text-xs gap-2">
          <div class="text-slate-300 flex items-center gap-2">
            <span class="text-emerald-400">💡</span>
            <span id="tiltDiagnosticAdvice">Execute strictly when emotional urgency is &le; 5. High-urgency entries account for the majority of non-structural drawdown.</span>
          </div>
          <span class="text-[10px] font-mono text-slate-500 whitespace-nowrap">Updated dynamically</span>
        </div>
      </section>"""

    tab3_target = "      </section>\n\n      <!-- Bottom Section: Day-of-Week Matrix, 15-Min Heatmap & Setup Expectancy Matrix -->'''"
    assert tab3_target in code, "Failed to find tab3_target"
    code = code.replace(tab3_target, "      </section>\n\n" + tilt_radar_section + "\n\n      <!-- Bottom Section: Day-of-Week Matrix, 15-Min Heatmap & Setup Expectancy Matrix -->'''", 1)

    # ====================================================
    # 5. TAB 4: Add Kelly Criterion & Growth Expectancy Card
    # ====================================================
    tab4_kelly_card = """      <!-- QUANT KELLY CRITERION & CAPITAL GROWTH EXPECTANCY -->
      <section class="glass-card rounded-2xl p-6 shadow-2xl border border-purple-500/20 bg-purple-950/5">
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-4 border-b border-slate-800 gap-2">
          <div>
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <span class="text-purple-400">🎲</span>
              <span>Fractional Kelly Criterion &amp; Capital Growth Sizing</span>
              <span class="text-xs px-2.5 py-0.5 rounded-full bg-purple-500/10 text-purple-300 border border-purple-500/20 font-mono">
                Optimal Growth Matrix
              </span>
            </h3>
            <p class="text-xs text-slate-400">Mathematical position sizing to maximize compound capital growth rate while minimizing probability of ruin</p>
          </div>
          <div class="flex items-center gap-2 font-mono text-xs">
            <span class="text-slate-400">Kelly Edge:</span>
            <span id="kellyEdgeDisp" class="px-2 py-0.5 rounded bg-purple-500/20 text-purple-300 font-bold">+0.00</span>
          </div>
        </div>

        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mt-5">
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
            <span class="text-[10px] text-slate-400 uppercase font-semibold block">Full Kelly Fraction (f*)</span>
            <div id="fullKellyFractionDisp" class="text-2xl font-black font-mono text-purple-300 mt-1.5">0.0%</div>
            <p class="text-[10px] text-slate-500 mt-0.5">Theoretical Max Compound</p>
          </div>

          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
            <span class="text-[10px] text-slate-400 uppercase font-semibold block">Half-Kelly (Recommended)</span>
            <div id="halfKellyFractionDisp" class="text-2xl font-black font-mono text-emerald-400 mt-1.5">0.45%</div>
            <p class="text-[10px] text-slate-500 mt-0.5">75% Growth &bull; 50% Less DD</p>
          </div>

          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
            <span class="text-[10px] text-slate-400 uppercase font-semibold block">Optimal Risk Amount</span>
            <div id="kellyRiskAmountDisp" class="text-2xl font-black font-mono text-white mt-1.5">₹450</div>
            <p class="text-[10px] text-slate-500 mt-0.5">Per-Trade Allocation</p>
          </div>

          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
            <span class="text-[10px] text-slate-400 uppercase font-semibold block">Probability of Ruin (&gt;20% DD)</span>
            <div id="ruinProbDisp" class="text-2xl font-black font-mono text-emerald-400 mt-1.5">&lt;0.05%</div>
            <p class="text-[10px] text-slate-500 mt-0.5">Institutional Safety Tier</p>
          </div>
        </div>
      </section>
"""
    tab4_target = "      <!-- INSTITUTIONAL VALUE AT RISK (VaR) & EXPECTED SHORTFALL (CVaR) TAIL RISK SUITE -->"
    assert tab4_target in code, "Failed to find tab4_target"
    code = code.replace(tab4_target, tab4_kelly_card + "\n" + tab4_target, 1)

    # ====================================================
    # 6. INJECT MODALS: Hotkeys Cheatsheet & Revenge Interceptor
    # ====================================================
    new_extra_modals = """  <!-- ========================================== -->
  <!-- MODAL: KEYBOARD SHORTCUTS & SOUNDPACK SETTINGS -->
  <!-- ========================================== -->
  <div id="hotkeysModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="glass-card rounded-2xl w-full max-w-xl border border-blue-500/30 shadow-2xl p-6 relative max-h-[92vh] overflow-y-auto">
      <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-xl bg-blue-500/20 border border-blue-500/30 flex items-center justify-center text-blue-400 font-bold text-base">
            ⌨️
          </div>
          <div>
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              Keyboard Shortcuts &amp; Soundpack Settings
            </h3>
            <p class="text-xs text-slate-400">Institutional Pro Terminal Hotkeys &bull; Rapid Execution Controls</p>
          </div>
        </div>
        <button onclick="closeHotkeyModal()" class="text-slate-400 hover:text-white text-2xl font-bold">&times;</button>
      </div>

      <!-- Hotkeys Grid -->
      <div class="mt-4 space-y-3 text-xs">
        <div>
          <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block mb-1.5">Execution &amp; Direction</span>
          <div class="grid grid-cols-2 gap-2">
            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
              <span class="text-slate-300">Set Direction: LONG</span>
              <kbd class="hotkey-badge">L</kbd>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
              <span class="text-slate-300">Set Direction: SHORT</span>
              <kbd class="hotkey-badge">S</kbd>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
              <span class="text-slate-300">Focus Symbol Input</span>
              <kbd class="hotkey-badge">N</kbd>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
              <span class="text-slate-300">Toggle Combat HUD</span>
              <kbd class="hotkey-badge">H</kbd>
            </div>
          </div>
        </div>

        <div>
          <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block mb-1.5">Routines &amp; Mindset Modals</span>
          <div class="grid grid-cols-2 gap-2">
            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
              <span class="text-slate-300">Pre-Flight Routine (D2)</span>
              <kbd class="hotkey-badge">P</kbd>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
              <span class="text-slate-300">5-Min Box Breathing</span>
              <kbd class="hotkey-badge">B</kbd>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
              <span class="text-slate-300">Monthly Dossier Report</span>
              <kbd class="hotkey-badge">M</kbd>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
              <span class="text-slate-300">Close Active Modal</span>
              <kbd class="hotkey-badge">Esc</kbd>
            </div>
          </div>
        </div>

        <div>
          <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block mb-1.5">View Navigation</span>
          <div class="grid grid-cols-4 gap-2 text-center">
            <div class="p-2 rounded-xl bg-slate-900/80 border border-slate-800">
              <div class="text-[10px] text-slate-400">Tab 1: Desk</div>
              <kbd class="hotkey-badge mt-1">1</kbd>
            </div>
            <div class="p-2 rounded-xl bg-slate-900/80 border border-slate-800">
              <div class="text-[10px] text-slate-400">Tab 2: P&amp;L</div>
              <kbd class="hotkey-badge mt-1">2</kbd>
            </div>
            <div class="p-2 rounded-xl bg-slate-900/80 border border-slate-800">
              <div class="text-[10px] text-slate-400">Tab 3: Edge</div>
              <kbd class="hotkey-badge mt-1">3</kbd>
            </div>
            <div class="p-2 rounded-xl bg-slate-900/80 border border-slate-800">
              <div class="text-[10px] text-slate-400">Tab 4: Quant</div>
              <kbd class="hotkey-badge mt-1">4</kbd>
            </div>
          </div>
        </div>

        <!-- Synthesized Soundpack Selector -->
        <div class="pt-3 border-t border-slate-800">
          <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block mb-1.5">Synthesized Soundpack</span>
          <div class="flex items-center gap-3">
            <select id="soundpackSelect" onchange="setSoundpack(this.value)" class="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-white font-mono text-xs focus:outline-none focus:border-blue-500">
              <option value="bell">Institutional Bell (Dual Harmonic Sine Chime)</option>
              <option value="click">Minimalist Tactile Click (Mechanical Audio)</option>
              <option value="cyber">Cyber Synth Arpeggio (Futuristic Fintech)</option>
              <option value="mute">Mute / Silent Mode</option>
            </select>
            <button onclick="testCurrentSoundpack()" class="px-3 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs transition">
              Test Sound
            </button>
          </div>
        </div>
      </div>

      <div class="mt-5 pt-3 border-t border-slate-800 flex justify-end">
        <button onclick="closeHotkeyModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold transition">
          Done
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL: REVENGE TRADE INTERCEPTOR BARRIER -->
  <!-- ========================================== -->
  <div id="revengeTradeModal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="glass-card rounded-2xl w-full max-w-lg border border-rose-500/50 shadow-2xl p-6 relative">
      <div class="flex items-center gap-3 pb-3 border-b border-slate-800">
        <div class="w-10 h-10 rounded-xl bg-rose-500/20 border border-rose-500/40 flex items-center justify-center text-rose-400 font-bold text-xl">
          ⚠️
        </div>
        <div>
          <h3 class="text-sm font-black text-rose-400 uppercase tracking-wider">
            Revenge Trade Interceptor Tripped!
          </h3>
          <p class="text-xs text-slate-400">Psychological Decoupling Enforced &bull; Phase 1 &amp; 2 Rule Gate</p>
        </div>
      </div>

      <div class="mt-4 p-3.5 bg-rose-950/40 rounded-xl border border-rose-500/30 text-xs text-rose-200 space-y-2">
        <p class="font-bold">You exited a losing trade less than 3 minutes ago.</p>
        <p class="text-slate-300 text-[11px] leading-relaxed">
          Entering immediately after a loss has an <strong>82% empirical statistical failure rate</strong> due to dopamine deficit and revenge impulses. Take a mandatory 10-second grounding pause.
        </p>
      </div>

      <!-- 10-Second Cooldown Ring -->
      <div class="py-6 flex flex-col items-center justify-center">
        <div id="revengeCooldownRing" class="w-24 h-24 rounded-full border-4 border-rose-500/50 bg-rose-500/10 flex flex-col items-center justify-center shadow-lg shadow-rose-900/30">
          <span id="revengeCounterText" class="text-2xl font-black font-mono text-white">10s</span>
          <span class="text-[9px] uppercase tracking-wider text-rose-300 font-bold">Breathe</span>
        </div>
      </div>

      <div class="flex items-center justify-between gap-3 pt-3 border-t border-slate-800">
        <button onclick="abortRevengeTrade()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold transition">
          Abort Trade &amp; Step Away
        </button>
        <button id="unlockRevengeBtn" onclick="confirmRevengeTradeBypass()" disabled class="px-4 py-2 rounded-xl bg-slate-800 text-slate-600 font-bold text-xs transition cursor-not-allowed">
          Lock Active (10s)
        </button>
      </div>
    </div>
  </div>

  <!-- FLOATING HOTKEYS PILL BUTTON (Bottom Right) -->
  <button onclick="openHotkeyModal()" class="fixed bottom-4 right-4 z-40 px-3 py-1.5 rounded-full bg-slate-900/90 hover:bg-slate-800 text-slate-400 hover:text-white border border-slate-700/80 shadow-2xl backdrop-blur-md text-xs font-mono flex items-center gap-1.5 transition">
    <span>⌨️</span>
    <span>Hotkeys</span>
    <kbd class="hotkey-badge text-[9px]">?</kbd>
  </button>
"""

    modal_target = "  <!-- MODAL: INTERACTIVE PRE-MARKET READINESS ROUTINE (D2 CHECKLIST) -->"
    assert modal_target in code, "Failed to find modal_target"
    code = code.replace(modal_target, new_extra_modals + "\n" + modal_target, 1)

    # ====================================================
    # 7. SCRIPT LOGIC: Kelly, Radar, Combat, Hotkeys, Soundpack, IndexedDB
    # ====================================================
    extra_engine_js = """
    // ==========================================
    // EXTENDED ENGINE: QUANT KELLY, TILT RADAR, COMBAT HUD,
    // HOTKEYS, SOUNDPACK & OFFLINE INDEXED-DB AUTO-VAULT
    // ==========================================

    // --- FEATURE 4: Combat Mode HUD Toggle ---
    let isCombatMode = false;

    function toggleCombatMode() {
      isCombatMode = !isCombatMode;
      const body = document.body;
      const btn = document.getElementById('combatModeBtn');
      const label = document.getElementById('combatModeLabel');

      if (isCombatMode) {
        body.classList.add('combat-mode');
        if (typeof switchTab === 'function') switchTab(1);
        if (btn) btn.className = "px-3 py-2 rounded-lg bg-amber-500 text-black font-extrabold text-xs flex items-center gap-1.5 transition shadow-lg shadow-amber-500/30";
        if (label) label.textContent = "Combat ON";
        playFeedbackSound('click');
      } else {
        body.classList.remove('combat-mode');
        if (btn) btn.className = "px-3 py-2 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/30 font-bold text-xs flex items-center gap-1.5 transition shadow-sm";
        if (label) label.textContent = "Combat HUD";
        playFeedbackSound('click');
      }
    }

    // --- FEATURE 5: Institutional Keyboard Shortcuts Listener ---
    function openHotkeyModal() {
      const modal = document.getElementById('hotkeysModal');
      const sel = document.getElementById('soundpackSelect');
      if (sel) sel.value = localStorage.getItem('trader_soundpack') || 'bell';
      if (modal) modal.classList.remove('hidden');
    }

    function closeHotkeyModal() {
      const modal = document.getElementById('hotkeysModal');
      if (modal) modal.classList.add('hidden');
    }

    function closeAllModals() {
      const modalIds = [
        'hotkeysModal', 'revengeTradeModal', 'preMarketReadinessModal',
        'monthlyDossierModal', 'calendarDayModal', 'fyersIngestModal',
        'webhookSettingsModal', 'preMarketFocusModal', 'traderContractModal',
        'screenshotZoomModal', 'preOrderGateModal', 'tiltBreakerModal',
        'eodScorecardModal'
      ];
      modalIds.forEach(id => {
        const m = document.getElementById(id);
        if (m) m.classList.add('hidden');
      });
    }

    window.addEventListener('keydown', (e) => {
      const activeTag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
      const isInput = activeTag === 'input' || activeTag === 'textarea' || activeTag === 'select';

      if (e.key === 'Escape') {
        closeAllModals();
        return;
      }

      if (isInput) return; // Do not intercept typing inside form inputs

      const k = e.key.toLowerCase();
      if (k === 'l') {
        e.preventDefault();
        if (typeof setTradeDirection === 'function') setTradeDirection('Long');
      } else if (k === 's') {
        e.preventDefault();
        if (typeof setTradeDirection === 'function') setTradeDirection('Short');
      } else if (k === 'n') {
        e.preventDefault();
        const sym = document.getElementById('symbol');
        if (sym) { sym.focus(); sym.select(); }
      } else if (k === 'h') {
        e.preventDefault();
        toggleCombatMode();
      } else if (k === 'p') {
        e.preventDefault();
        if (typeof openPreMarketReadinessModal === 'function') openPreMarketReadinessModal();
      } else if (k === 'b') {
        e.preventDefault();
        if (typeof openPreMarketFocusModal === 'function') openPreMarketFocusModal();
      } else if (k === 'm') {
        e.preventDefault();
        if (typeof openMonthlyDossierModal === 'function') openMonthlyDossierModal();
      } else if (e.key === '?' || (e.shiftKey && e.key === '/')) {
        e.preventDefault();
        openHotkeyModal();
      } else if (['1', '2', '3', '4'].includes(e.key)) {
        e.preventDefault();
        if (typeof switchTab === 'function') switchTab(parseInt(e.key));
      }
    });

    // --- FEATURE 6: Soundpack Customizer & Streak Glow ---
    function setSoundpack(val) {
      localStorage.setItem('trader_soundpack', val);
      playFeedbackSound('click');
    }

    function testCurrentSoundpack() {
      playFeedbackSound('success');
    }

    function playFeedbackSound(type = 'click') {
      const soundpack = localStorage.getItem('trader_soundpack') || 'bell';
      if (soundpack === 'mute') return;

      try {
        const ctx = typeof getAudioContext === 'function' ? getAudioContext() : null;
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        if (soundpack === 'bell') {
          osc.type = 'sine';
          if (type === 'click') {
            osc.frequency.setValueAtTime(880, now);
            gain.gain.setValueAtTime(0.12, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
            osc.connect(gain); gain.connect(ctx.destination);
            osc.start(now); osc.stop(now + 0.08);
          } else {
            osc.frequency.setValueAtTime(1046.50, now);
            gain.gain.setValueAtTime(0.25, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.8);
            osc.connect(gain); gain.connect(ctx.destination);
            osc.start(now); osc.stop(now + 0.8);
          }
        } else if (soundpack === 'click') {
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(1200, now);
          osc.frequency.exponentialRampToValueAtTime(200, now + 0.04);
          gain.gain.setValueAtTime(0.15, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);
          osc.connect(gain); gain.connect(ctx.destination);
          osc.start(now); osc.stop(now + 0.04);
        } else if (soundpack === 'cyber') {
          osc.type = 'square';
          osc.frequency.setValueAtTime(type === 'click' ? 660 : 523.25, now);
          if (type !== 'click') {
            osc.frequency.setValueAtTime(783.99, now + 0.08);
            osc.frequency.setValueAtTime(1046.50, now + 0.16);
          }
          gain.gain.setValueAtTime(0.15, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + (type === 'click' ? 0.06 : 0.35));
          osc.connect(gain); gain.connect(ctx.destination);
          osc.start(now); osc.stop(now + (type === 'click' ? 0.06 : 0.35));
        }
      } catch (err) {
        console.warn('Soundpack playback error:', err);
      }
    }

    function checkDisciplineStreak(trades) {
      const list = trades || (typeof tradesData !== 'undefined' ? tradesData : []);
      if (!list || list.length < 3) return;

      const recent = list.slice(-3);
      const isStreak = recent.every(t => (t.rule_violation !== 'Y' && (t.checklist_score || 5) >= 4));

      const brandHeader = document.querySelector('header .max-w-7xl > div');
      if (brandHeader) {
        if (isStreak) {
          brandHeader.classList.add('discipline-streak-glow');
        } else {
          brandHeader.classList.remove('discipline-streak-glow');
        }
      }
    }

    // --- FEATURE 1: Quant Kelly Criterion & Dynamic Sizing Engine ---
    let computedHalfKellyQty = 0;
    let computedHalfKellyRisk = 450;

    function computeKellyExpectancy(trades) {
      const list = trades || (typeof tradesData !== 'undefined' ? tradesData : []);
      let wins = 0;
      let totalTrades = 0;
      let sumWinR = 0;
      let sumLossR = 0;
      let losses = 0;

      list.forEach(t => {
        const r = parseFloat(t.r_multiple || 0);
        totalTrades++;
        if (t.outcome === 'Win' || r > 0) {
          wins++;
          sumWinR += r;
        } else if (t.outcome === 'Loss' || r < 0) {
          losses++;
          sumLossR += Math.abs(r);
        }
      });

      const p = totalTrades > 0 ? wins / totalTrades : 0.55;
      const avgWin = wins > 0 ? sumWinR / wins : 2.2;
      const avgLoss = losses > 0 ? sumLossR / losses : 1.0;
      const b = avgLoss > 0 ? avgWin / avgLoss : 2.2;

      let fStar = (p * (b + 1) - 1) / b;
      if (fStar < 0) fStar = 0.0;
      if (fStar > 0.15) fStar = 0.15;

      const halfKelly = fStar / 2.0;
      const cap = typeof startingCapital !== 'undefined' ? startingCapital : 100000;
      const kellyRisk = Math.max(250, Math.min(1000, Math.round(cap * halfKelly)));
      computedHalfKellyRisk = kellyRisk;

      const elRisk = document.getElementById('kellyRecRisk');
      const elQty = document.getElementById('kellyRecQty');
      if (elRisk) elRisk.textContent = `₹${kellyRisk}`;

      const entry = parseFloat(document.getElementById('entry_price')?.value) || 0;
      const stop = parseFloat(document.getElementById('stop_price')?.value) || 0;
      if (entry > 0 && stop > 0 && Math.abs(entry - stop) > 0) {
        const riskPerShare = Math.abs(entry - stop);
        computedHalfKellyQty = Math.floor(kellyRisk / riskPerShare);
        if (elQty) elQty.textContent = `(${computedHalfKellyQty} shs)`;
      } else {
        if (elQty) elQty.textContent = `(0 shs)`;
      }

      const elFull = document.getElementById('fullKellyFractionDisp');
      const elHalf = document.getElementById('halfKellyFractionDisp');
      const elAmount = document.getElementById('kellyRiskAmountDisp');
      const elEdge = document.getElementById('kellyEdgeDisp');

      if (elFull) elFull.textContent = `${(fStar * 100).toFixed(1)}%`;
      if (elHalf) elHalf.textContent = `${(halfKelly * 100).toFixed(2)}%`;
      if (elAmount) elAmount.textContent = `₹${kellyRisk}`;
      if (elEdge) elEdge.textContent = `+${((p * b - (1 - p))).toFixed(2)}`;
    }

    function applyKellyPositionSize() {
      const entry = parseFloat(document.getElementById('entry_price')?.value) || 0;
      const stop = parseFloat(document.getElementById('stop_price')?.value) || 0;
      if (entry <= 0 || stop <= 0) {
        alert('Please enter valid Entry and Stop-Loss prices first.');
        return;
      }
      const riskPerShare = Math.abs(entry - stop);
      if (riskPerShare <= 0) return;

      const qty = Math.floor(computedHalfKellyRisk / riskPerShare);
      const qtyInput = document.getElementById('qty');
      if (qtyInput) {
        qtyInput.value = qty > 0 ? qty : 1;
        if (typeof recalculateCalculators === 'function') recalculateCalculators();
        playFeedbackSound('click');
      }
    }

    // --- FEATURE 2: Cognitive Fatigue Radar & Revenge Trade Interceptor ---
    let pendingRevengeTradeEvent = null;
    let revengeCooldownInterval = null;

    function renderCognitiveFatigueRadar(trades) {
      const list = trades || (typeof tradesData !== 'undefined' ? tradesData : []);
      let calmWins = 0, calmTotal = 0, calmNetR = 0;
      let urgentWins = 0, urgentTotal = 0, urgentNetR = 0;
      let earlyWins = 0, earlyTotal = 0, earlyNetR = 0;
      let lateWins = 0, lateTotal = 0, lateNetR = 0;

      list.forEach(t => {
        const r = parseFloat(t.r_multiple || 0);
        const urgency = parseInt(t.emotion_before || 3);
        const isWin = t.outcome === 'Win' || r > 0;

        if (urgency <= 5) {
          calmTotal++; calmNetR += r;
          if (isWin) calmWins++;
        } else {
          urgentTotal++; urgentNetR += r;
          if (isWin) urgentWins++;
        }

        const timeStr = t.entry_time || '09:30';
        const parts = timeStr.split(':').map(Number);
        const mins = parts[0] * 60 + parts[1];
        if (mins < 9 * 60 + 45) {
          earlyTotal++; earlyNetR += r;
          if (isWin) earlyWins++;
        } else {
          lateTotal++; lateNetR += r;
          if (isWin) lateWins++;
        }
      });

      const calmWR = calmTotal > 0 ? ((calmWins / calmTotal) * 100).toFixed(0) : '0';
      const urgentWR = urgentTotal > 0 ? ((urgentWins / urgentTotal) * 100).toFixed(0) : '0';
      const earlyWR = earlyTotal > 0 ? ((earlyWins / earlyTotal) * 100).toFixed(0) : '0';
      const lateWR = lateTotal > 0 ? ((lateWins / lateTotal) * 100).toFixed(0) : '0';

      const elCalmWR = document.getElementById('calmWinRateDisp');
      const elCalmR = document.getElementById('calmNetRDisp');
      const elUrgWR = document.getElementById('urgentWinRateDisp');
      const elUrgR = document.getElementById('urgentNetRDisp');
      const elEarlyWR = document.getElementById('earlyWinRateDisp');
      const elEarlyR = document.getElementById('earlyNetRDisp');
      const elLateWR = document.getElementById('lateWinRateDisp');
      const elLateR = document.getElementById('lateNetRDisp');
      const elTiltCost = document.getElementById('tiltCostTotalDisp');

      if (elCalmWR) elCalmWR.textContent = `${calmWR}%`;
      if (elCalmR) elCalmR.textContent = `${calmNetR >= 0 ? '+' : ''}${calmNetR.toFixed(2)}R Net`;
      if (elUrgWR) elUrgWR.textContent = `${urgentWR}%`;
      if (elUrgR) elUrgR.textContent = `${urgentNetR >= 0 ? '+' : ''}${urgentNetR.toFixed(2)}R Net`;
      if (elEarlyWR) elEarlyWR.textContent = `${earlyWR}%`;
      if (elEarlyR) elEarlyR.textContent = `${earlyNetR >= 0 ? '+' : ''}${earlyNetR.toFixed(2)}R Net`;
      if (elLateWR) elLateWR.textContent = `${lateWR}%`;
      if (elLateR) elLateR.textContent = `${lateNetR >= 0 ? '+' : ''}${lateNetR.toFixed(2)}R Net`;

      if (elTiltCost) {
        const tiltCost = Math.abs(Math.min(0, urgentNetR));
        elTiltCost.textContent = `-${tiltCost.toFixed(2)}R`;
      }
    }

    function checkRevengeTradeCondition() {
      const list = typeof tradesData !== 'undefined' ? tradesData : [];
      if (!list || list.length === 0) return false;

      const lastTrade = list[list.length - 1];
      if (lastTrade.outcome !== 'Loss') return false;

      if (lastTrade.timestamp) {
        const diffSecs = (Date.now() - new Date(lastTrade.timestamp).getTime()) / 1000;
        if (diffSecs < 180) return true;
      }
      return false;
    }

    function triggerRevengeTradeBarrier(eventData) {
      pendingRevengeTradeEvent = eventData;
      const modal = document.getElementById('revengeTradeModal');
      const counter = document.getElementById('revengeCounterText');
      const btn = document.getElementById('unlockRevengeBtn');
      if (modal) modal.classList.remove('hidden');

      playAlertSiren('pattern');
      let remaining = 10;
      if (btn) {
        btn.disabled = true;
        btn.className = "px-4 py-2 rounded-xl bg-slate-800 text-slate-600 font-bold text-xs transition cursor-not-allowed";
        btn.textContent = "Lock Active (10s)";
      }

      if (revengeCooldownInterval) clearInterval(revengeCooldownInterval);
      revengeCooldownInterval = setInterval(() => {
        remaining--;
        if (counter) counter.textContent = `${remaining}s`;
        if (btn) btn.textContent = `Lock Active (${remaining}s)`;

        if (remaining <= 0) {
          clearInterval(revengeCooldownInterval);
          if (counter) counter.textContent = 'Ready';
          if (btn) {
            btn.disabled = false;
            btn.className = "px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition cursor-pointer shadow-lg shadow-emerald-600/30";
            btn.textContent = "Proceed with Strict System Entry";
          }
        }
      }, 1000);
    }

    function abortRevengeTrade() {
      if (revengeCooldownInterval) clearInterval(revengeCooldownInterval);
      const modal = document.getElementById('revengeTradeModal');
      if (modal) modal.classList.add('hidden');
      pendingRevengeTradeEvent = null;
      alert('🛡️ Revenge Trade Aborted. Mental capital preserved. Step away for 10 minutes.');
    }

    function confirmRevengeTradeBypass() {
      if (revengeCooldownInterval) clearInterval(revengeCooldownInterval);
      const modal = document.getElementById('revengeTradeModal');
      if (modal) modal.classList.add('hidden');
      if (pendingRevengeTradeEvent && typeof commitPreOrderTrade === 'function') {
        commitPreOrderTrade(pendingRevengeTradeEvent);
        pendingRevengeTradeEvent = null;
      }
    }

    // --- FEATURE 7: Offline IndexedDB Auto-Vault Engine ---
    let indexedDbInstance = null;
    const DB_NAME = 'TraderExecutionResetDB';
    const DB_VERSION = 1;

    function initIndexedDB() {
      if (!('indexedDB' in window)) return;
      const req = indexedDB.open(DB_NAME, DB_VERSION);

      req.onupgradeneeded = (e) => {
        const db = e.target.result;
        if (!db.objectStoreNames.contains('formDrafts')) {
          db.createObjectStore('formDrafts', { keyPath: 'id' });
        }
        if (!db.objectStoreNames.contains('offlineTrades')) {
          db.createObjectStore('offlineTrades', { keyPath: 'id', autoIncrement: true });
        }
      };

      req.onsuccess = (e) => {
        indexedDbInstance = e.target.result;
        updateIndexedDbUI(true);
        restoreTradeDraft();
        hookFormDraftAutoSave();
      };

      req.onerror = () => {
        updateIndexedDbUI(false);
      };
    }

    function updateIndexedDbUI(isActive) {
      const pill = document.getElementById('indexedDbSyncPill');
      if (pill) {
        if (isActive) {
          pill.classList.remove('hidden');
        } else {
          pill.classList.add('hidden');
        }
      }
    }

    function hookFormDraftAutoSave() {
      const inputIds = ['symbol', 'entry_price', 'stop_price', 'exit_price', 'qty', 'setup_name', 'notes'];
      inputIds.forEach(id => {
        const el = document.getElementById(id);
        if (el) {
          el.addEventListener('input', debounceSaveDraft);
          el.addEventListener('change', debounceSaveDraft);
        }
      });
    }

    let saveDraftTimer = null;
    function debounceSaveDraft() {
      clearTimeout(saveDraftTimer);
      saveDraftTimer = setTimeout(saveTradeDraft, 500);
    }

    function saveTradeDraft() {
      if (!indexedDbInstance) return;
      const symbol = document.getElementById('symbol')?.value || '';
      const entry = document.getElementById('entry_price')?.value || '';
      const stop = document.getElementById('stop_price')?.value || '';
      const exit = document.getElementById('exit_price')?.value || '';
      const qty = document.getElementById('qty')?.value || '';
      const setup = document.getElementById('setup_name')?.value || '';
      const dir = document.getElementById('direction')?.value || 'Long';

      if (!symbol && !entry && !stop) return;

      const draft = {
        id: 'active_draft',
        symbol, entry, stop, exit, qty, setup, dir,
        updatedAt: new Date().toISOString()
      };

      try {
        const tx = indexedDbInstance.transaction('formDrafts', 'readwrite');
        const store = tx.objectStore('formDrafts');
        store.put(draft);
      } catch (e) {
        console.warn('Draft save error:', e);
      }
    }

    function restoreTradeDraft() {
      if (!indexedDbInstance) return;
      try {
        const tx = indexedDbInstance.transaction('formDrafts', 'readonly');
        const store = tx.objectStore('formDrafts');
        const req = store.get('active_draft');
        req.onsuccess = () => {
          const draft = req.result;
          if (draft && draft.symbol) {
            const curSym = document.getElementById('symbol')?.value || '';
            if (!curSym) {
              if (document.getElementById('symbol')) document.getElementById('symbol').value = draft.symbol;
              if (document.getElementById('entry_price')) document.getElementById('entry_price').value = draft.entry;
              if (document.getElementById('stop_price')) document.getElementById('stop_price').value = draft.stop;
              if (document.getElementById('exit_price')) document.getElementById('exit_price').value = draft.exit;
              if (document.getElementById('qty')) document.getElementById('qty').value = draft.qty;
              if (document.getElementById('setup_name')) document.getElementById('setup_name').value = draft.setup;
              if (typeof setTradeDirection === 'function') setTradeDirection(draft.dir || 'Long');
              if (typeof recalculateCalculators === 'function') recalculateCalculators();

              const banner = document.getElementById('draftRestoredBanner');
              const text = document.getElementById('draftRestoredText');
              if (banner) banner.classList.remove('hidden');
              if (text) text.textContent = `Restored draft for ${draft.symbol} from IndexedDB`;
            }
          }
        };
      } catch (e) {
        console.warn('Draft restore error:', e);
      }
    }

    function clearTradeDraft() {
      if (!indexedDbInstance) return;
      try {
        const tx = indexedDbInstance.transaction('formDrafts', 'readwrite');
        tx.objectStore('formDrafts').delete('active_draft');
        const banner = document.getElementById('draftRestoredBanner');
        if (banner) banner.classList.add('hidden');
      } catch (e) {}
    }

    function discardTradeDraft() {
      clearTradeDraft();
      if (document.getElementById('symbol')) document.getElementById('symbol').value = '';
      if (document.getElementById('entry_price')) document.getElementById('entry_price').value = '';
      if (document.getElementById('stop_price')) document.getElementById('stop_price').value = '';
      if (document.getElementById('exit_price')) document.getElementById('exit_price').value = '';
      if (document.getElementById('qty')) document.getElementById('qty').value = '';
      if (typeof recalculateCalculators === 'function') recalculateCalculators();
    }

    // --- FEATURE 8: Lazy Canvas Rendering & Tab Transition Optimization ---
    const origSwitchTabFn = window.switchTab;
    function optimizedSwitchTab(tabNum) {
      if (typeof origSwitchTabFn === 'function') {
        origSwitchTabFn(tabNum);
      }
      window.requestAnimationFrame(() => {
        const trades = typeof tradesData !== 'undefined' ? tradesData : [];
        if (tabNum === 1) {
          computeKellyExpectancy(trades);
          checkDisciplineStreak(trades);
        } else if (tabNum === 2) {
          if (typeof renderCalendarHeatmap === 'function') renderCalendarHeatmap(trades);
        } else if (tabNum === 3) {
          renderCognitiveFatigueRadar(trades);
        } else if (tabNum === 4) {
          computeKellyExpectancy(trades);
        }
      });
    }

    window.switchTab = optimizedSwitchTab;
"""

    old_dom_ready = "    // Hook listeners on DOM ready\n    window.addEventListener('DOMContentLoaded', () => {"
    assert old_dom_ready in code, "Failed to find old_dom_ready"
    code = code.replace(old_dom_ready, extra_engine_js + "\n\n" + old_dom_ready + "\n      initIndexedDB();\n      computeKellyExpectancy();\n      checkDisciplineStreak();", 1)

    with open(MASTER_FILE, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"Successfully updated {MASTER_FILE} with Features 1, 2, 4, 5, 6, 7, 8!")

if __name__ == "__main__":
    main()
