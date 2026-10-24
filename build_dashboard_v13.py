#!/usr/bin/env python3
"""
Builder for Trader Execution Reset System Command Center v13 (Institutional UI/UX Overhaul).
Applies:
1. Modern Fintech / Linear Theme (Inter + JetBrains Mono typography, Obsidian dark glassmorphism)
2. Interactive Direction Switchers (Big visual LONG/SHORT buttons instead of basic select)
3. Streamlined Docked Header & Grouped Action Bars
4. Sleek Form Inputs with Focus Rings & Floating Metric Pills
5. Elegant Chart.js Visuals with Custom Gradients & Frosted Glass Cards
"""

import os
import re

SRC_PATH = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html"
OUT_PUBLIC = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/public/index.html"
OUT_DELIV = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html"
OUT_BRAIN = "/home/sunny/.gemini/antigravity/brain/85803015-3567-4584-af28-ca9d6eed9423/trader_dashboard.html"

def build_v13():
    with open(SRC_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Inject Inter and JetBrains Mono Google Fonts in <head>
    google_fonts = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">"""

    if "family=JetBrains+Mono" not in content:
        content = content.replace("<head>", f"<head>\n{google_fonts}", 1)

    # 2. Upgrade Tailwind Configuration & Custom Modern CSS
    tailwind_cfg_old = r"""  <script>
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
  </script>"""

    tailwind_cfg_new = r"""  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
            mono: ['JetBrains Mono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace']
          },
          colors: {
            obsidian: '#060913',
            surface: '#0B1120',
            surfaceLighter: '#10172A',
            borderSubtle: 'rgba(255, 255, 255, 0.08)',
            borderHighlight: 'rgba(59, 130, 246, 0.35)',
            brand: { 50: '#f0fdf4', 500: '#10b981', 600: '#059669', 700: '#047857' }
          }
        }
      }
    }
  </script>"""

    if tailwind_cfg_old in content:
        content = content.replace(tailwind_cfg_old, tailwind_cfg_new, 1)

    # 3. Upgrade Global Styles for Obsidian Glassmorphism, Glows, and Silky Typography
    old_style_block = """  <style>
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
  </style>"""

    new_style_block = """  <style>
    body {
      background-color: #060913;
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(30, 58, 138, 0.12) 0%, transparent 60%),
        radial-gradient(circle at 100% 100%, rgba(16, 185, 129, 0.05) 0%, transparent 40%);
      background-attachment: fixed;
      color: #F1F5F9;
      font-family: 'Inter', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      letter-spacing: -0.01em;
    }
    .font-mono { font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, monospace !important; }
    .glass-card {
      background: rgba(11, 17, 32, 0.88);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.08);
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.6);
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .glass-card:hover {
      border-color: rgba(255, 255, 255, 0.14);
    }
    .glass-card-interactive:hover {
      border-color: rgba(59, 130, 246, 0.4);
      transform: translateY(-2px);
      box-shadow: 0 25px 50px -12px rgba(30, 58, 138, 0.25);
    }
    ::-webkit-scrollbar { width: 5px; height: 5px; }
    ::-webkit-scrollbar-track { background: #060913; }
    ::-webkit-scrollbar-thumb { background: #1E293B; border-radius: 9999px; }
    ::-webkit-scrollbar-thumb:hover { background: #334155; }
    
    .tab-btn.active {
      background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
      color: #ffffff;
      border-color: #3B82F6;
      box-shadow: 0 4px 20px rgba(37, 99, 235, 0.35);
    }
    .tab-btn:not(.active) {
      background: rgba(11, 17, 32, 0.6);
      color: #94A3B8;
      border-color: rgba(255, 255, 255, 0.06);
    }
    .tab-btn:not(.active):hover {
      background: rgba(17, 24, 39, 0.9);
      color: #F8FAFC;
      border-color: rgba(255, 255, 255, 0.12);
    }

    /* Direction Segmented Switchers */
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
      background: #0B1120;
      color: #94A3B8;
      border-color: rgba(255, 255, 255, 0.08);
    }

    /* Risk Mode Chips */
    .risk-mode-btn.active {
      background: #2563EB !important;
      color: #FFFFFF !important;
      border-color: #3B82F6 !important;
      box-shadow: 0 0 12px rgba(37, 99, 235, 0.35);
    }

    @media print {
      body * { visibility: hidden; }
      #weeklyReviewModalContent, #weeklyReviewModalContent * { visibility: visible; }
      #weeklyReviewModalContent { position: absolute; left: 0; top: 0; width: 100%; background: white !important; color: black !important; }
    }
  </style>"""

    if old_style_block in content:
        content = content.replace(old_style_block, new_style_block, 1)

    # 4. Replace basic Direction <select> in Trade Logger with Interactive Segmented Buttons (🟢 LONG / 🔴 SHORT)
    old_direction_select = """              <label class="block text-slate-400 text-[11px] font-semibold uppercase tracking-wider mb-1">Direction</label>
              <select id="direction" onchange="recalculateCalculators()" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-2.5 py-1.5 text-white text-xs font-semibold">
                <option value="Long">🟢 Long (Buy)</option>
                <option value="Short">🔴 Short (Sell)</option>
              </select>"""

    new_direction_select = """              <label class="block text-slate-400 text-[11px] font-semibold uppercase tracking-wider mb-1">Direction</label>
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
              </div>"""

    if old_direction_select in content:
        content = content.replace(old_direction_select, new_direction_select, 1)

    # 5. Add JS helper for interactive Direction switcher and Smooth Chart.js Theme Defaults
    direction_js = """
    // --- Interactive Direction Switcher UX ---
    function setTradeDirection(dir) {
      const input = document.getElementById('direction');
      const btnLong = document.getElementById('dirBtnLong');
      const btnShort = document.getElementById('dirBtnShort');
      if (input) input.value = dir;

      if (dir === 'Long') {
        if (btnLong) { btnLong.className = "dir-toggle-btn active-long py-1.5 px-3 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition"; }
        if (btnShort) { btnShort.className = "dir-toggle-btn py-1.5 px-3 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition"; }
      } else {
        if (btnLong) { btnLong.className = "dir-toggle-btn py-1.5 px-3 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition"; }
        if (btnShort) { btnShort.className = "dir-toggle-btn active-short py-1.5 px-3 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 transition"; }
      }
      recalculateCalculators();
    }

    // Chart.js Global Theme Calibration (Linear/TradingView Dark Aesthetic)
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
    """

    assert "  </script>" in content, "Failed to find closing script tag"
    content = content.replace("  </script>", f"{direction_js}\n  </script>", 1)

    # Write files
    for path in [OUT_PUBLIC, OUT_DELIV, OUT_BRAIN]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully generated v13: {path} ({len(content)} bytes)")

if __name__ == "__main__":
    build_v13()
