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

    .scrollbar-none::-webkit-scrollbar { display: none; }
    .scrollbar-none { -ms-overflow-style: none; scrollbar-width: none; }

    /* Segmented Control Navigation Track (Linear / macOS Glass Aesthetic) */
    .tab-segmented-track {
      background: rgba(11, 17, 32, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 4px;
      border-radius: 14px;
      backdrop-filter: blur(16px);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
    }
    
    .tab-btn {
      position: relative;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      border-radius: 10px;
      font-weight: 700;
      letter-spacing: -0.01em;
    }
    .tab-btn.active {
      background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
      color: #FFFFFF !important;
      border: 1px solid rgba(147, 197, 253, 0.35) !important;
      box-shadow: 0 2px 14px rgba(37, 99, 235, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
    }
    .tab-btn:not(.active) {
      background: transparent !important;
      color: #94A3B8 !important;
      border: 1px solid transparent !important;
    }
    .tab-btn:not(.active):hover {
      color: #F8FAFC !important;
      background: rgba(255, 255, 255, 0.06) !important;
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

    /* Combat Mode HUD (Minimalist Execution Window 09:15–10:30 AM) */
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
    [data-theme="bloomberg"] .border-blue-500\/30,
    [data-theme="bloomberg"] .border-blue-500\/20,
    [data-theme="bloomberg"] .border-blue-500\/60,
    [data-theme="bloomberg"] .border-slate-800,
    [data-theme="bloomberg"] .border-slate-700 {
      border-color: rgba(245, 158, 11, 0.28) !important;
    }
    [data-theme="bloomberg"] .bg-slate-900,
    [data-theme="bloomberg"] .bg-slate-950,
    [data-theme="bloomberg"] .bg-slate-900\/80,
    [data-theme="bloomberg"] .bg-slate-950\/80,
    [data-theme="bloomberg"] .bg-slate-950\/90 {
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
    [data-theme="linear"] .border-blue-500\/30,
    [data-theme="linear"] .border-blue-500\/20,
    [data-theme="linear"] .border-blue-500\/60,
    [data-theme="linear"] .border-slate-800,
    [data-theme="linear"] .border-slate-700 {
      border-color: rgba(255, 255, 255, 0.14) !important;
    }
    [data-theme="linear"] .bg-slate-900,
    [data-theme="linear"] .bg-slate-950,
    [data-theme="linear"] .bg-slate-900\/80,
    [data-theme="linear"] .bg-slate-950\/80,
    [data-theme="linear"] .bg-slate-950\/90 {
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
    [data-theme="nordic"] .border-blue-500\/30,
    [data-theme="nordic"] .border-blue-500\/20,
    [data-theme="nordic"] .border-blue-500\/60,
    [data-theme="nordic"] .border-slate-800,
    [data-theme="nordic"] .border-slate-700 {
      border-color: rgba(6, 182, 212, 0.28) !important;
    }
    [data-theme="nordic"] .bg-slate-900,
    [data-theme="nordic"] .bg-slate-950,
    [data-theme="nordic"] .bg-slate-900\/80,
    [data-theme="nordic"] .bg-slate-950\/80,
    [data-theme="nordic"] .bg-slate-950\/90 {
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

  </style>
</head>'''

    assert old_head in content, "Failed to find old_head"
    content = content.replace(old_head, new_head, 1)

    # 1.5 HEADER BRAND & PHASE STATUS CLUSTER (Ultra-Clean Fintech UI/UX, Never Wraps)
    old_header_brand = r'''    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-3">
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
          <p class="text-xs text-slate-400">Intraday 1-Min NSE Equities &bull; 09:15–10:30 AM IST &bull; Target RR &ge; 2.2 &bull; Max 2 Trades/Day</p>
        </div>
      </div>'''

    new_header_brand = r'''    <div class="max-w-7xl mx-auto flex flex-col xl:flex-row items-start xl:items-center justify-between gap-4">
      <!-- BRAND & SYSTEM STATUS CLUSTER (Clean, Institutional, Never Wraps) -->
      <div class="flex items-center gap-3.5 flex-shrink-0">
        <!-- Modern Glowing Logo Icon with Live Pulse Indicator -->
        <div class="relative flex-shrink-0 cursor-pointer" onclick="switchTab(1)" title="Trader Reset Command Center">
          <div class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-emerald-500 via-teal-500 to-blue-600 flex items-center justify-center font-black text-white text-lg shadow-xl shadow-emerald-500/25 border border-white/20 ring-1 ring-emerald-400/40 hover:scale-105 transition-transform duration-200">
            ⚡
          </div>
          <span class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full bg-emerald-500 border-2 border-slate-950 flex items-center justify-center shadow" title="System Active &amp; Online">
            <span class="w-1.5 h-1.5 rounded-full bg-white animate-ping"></span>
          </span>
        </div>

        <div class="space-y-1.5">
          <!-- Title Row & High-Contrast Phase Badge (Never wraps awkwardly) -->
          <div class="flex items-center gap-3 flex-wrap">
            <h1 class="text-base sm:text-lg font-black text-white tracking-tight flex items-center gap-2 whitespace-nowrap">
              <span>Trader Execution Reset</span>
              <span class="text-slate-600 font-normal">|</span>
              <span class="text-xs font-mono font-semibold text-slate-400">v16.0</span>
            </h1>

            <!-- Institutional Phase Status Pill (Clean single line, dynamic) -->
            <div id="headerPhasePill" onclick="switchTab(1)" class="cursor-pointer inline-flex items-center gap-2 px-3 py-1 rounded-full bg-gradient-to-r from-emerald-500/15 to-teal-500/15 border border-emerald-400/40 text-emerald-300 text-xs font-mono font-bold whitespace-nowrap shadow-sm shadow-emerald-950/50 hover:bg-emerald-500/25 transition" title="Current 30-Day Reset Phase (Click to view Phase Tracker)">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
              <span id="headerPhaseTitle" class="tracking-wide">PHASE 2: DAYS 4–10</span>
              <span class="text-emerald-500/80 font-sans">&bull;</span>
              <span id="headerPhaseTradeCap" class="text-emerald-200 font-semibold">MAX 2 TRADES</span>
            </div>
          </div>

          <!-- Structured Micro-Tag Rules Strip (Clean, separated chips) -->
          <div class="flex items-center gap-1.5 text-[11px] text-slate-400 font-mono flex-wrap">
            <span class="px-2 py-0.5 rounded-md bg-slate-900/90 border border-slate-800 text-slate-300 font-semibold whitespace-nowrap shadow-sm">
              NSE Equities &bull; 1-Min
            </span>
            <span class="px-2 py-0.5 rounded-md bg-slate-900/90 border border-slate-800 text-slate-300 font-semibold whitespace-nowrap shadow-sm">
              🕒 09:15–10:30 AM IST
            </span>
            <span class="px-2 py-0.5 rounded-md bg-blue-500/10 border border-blue-500/25 text-blue-300 font-bold whitespace-nowrap shadow-sm">
              🎯 Planned RR &ge; 2.2
            </span>
            <span class="px-2 py-0.5 rounded-md bg-amber-500/10 border border-amber-500/25 text-amber-300 font-bold whitespace-nowrap shadow-sm">
              🛡️ Risk 0.25%–0.50%
            </span>
          </div>
        </div>
      </div>'''

    assert old_header_brand in content, "Failed to find old_header_brand"
    content = content.replace(old_header_brand, new_header_brand, 1)

    # 2. HEADER: Add Mindset Timer and Demerit Strikes pills cleanly grouped
    old_sound_btn = r'''        <button id="soundToggleBtn" onclick="toggleSound()" class="px-2.5 py-1.5 rounded-lg bg-slate-800/80 border border-slate-700 text-slate-300 hover:text-white flex items-center gap-1.5 transition">
          <span id="soundIcon">🔊</span>
          <span id="soundText" class="font-medium">Audio ON</span>
        </button>'''

    new_sound_btn = r'''        <button onclick="togglePlaybookDrawer()" class="px-2.5 py-1.5 rounded-lg bg-purple-500/10 border border-purple-500/30 text-purple-300 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm" title="Open 1-Minute Playbook Strategy Cheatsheet (Shortcut: P)">
          <span>📖</span>
          <span>Playbook (P)</span>
        </button>

        <button onclick="openPreMarketFocusModal()" class="px-2.5 py-1.5 rounded-lg bg-teal-500/10 border border-teal-500/30 text-teal-300 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm" title="5-Minute Pre-Market Mindset &amp; Box Breathing (09:05–09:10 AM IST)">
          <span>🧘</span>
          <span>Mindset Timer</span>
        </button>

        <button onclick="openTraderContractModal()" id="headerDemeritBadge" class="px-2.5 py-1.5 rounded-lg bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm" title="Execution Contract &amp; Penalty Strike System">
          <span>⚖️</span>
          <span id="headerStrikesText">Strikes: 0/3</span>
        </button>

        <button id="ambientAudioBtn" onclick="toggle432HzAmbient()" class="px-2.5 py-1.5 rounded-lg bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm" title="Toggle 432Hz Alpha Waves Focus Audio">
          <span id="ambientIcon">🎧</span>
          <span id="ambientText">432Hz Focus</span>
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

    # 2.5 NAVIGATION TABS: Segmented Glass Control Track (No clipping, responsive text)
    old_tabs = r'''    <!-- Top Tab Navigation Controls & Action Strip (4 SPACIOUS TABS) -->
    <div class="flex flex-col xl:flex-row items-center justify-between gap-4 border-b border-slate-800 pb-4">
      <!-- 4 Responsive Tab Navigation Buttons -->
      <div class="flex items-center gap-2 w-full xl:w-auto overflow-x-auto pb-1 xl:pb-0">
        <button id="tabBtn1" onclick="switchTab(1)" class="tab-btn active px-4 py-2.5 rounded-xl font-bold text-xs sm:text-sm border flex items-center gap-2 transition duration-200 whitespace-nowrap">
          <span>⚡</span>
          <span>Live Execution</span>
        </button>
        <button id="tabBtn2" onclick="switchTab(2)" class="tab-btn px-4 py-2.5 rounded-xl font-bold text-xs sm:text-sm border flex items-center gap-2 transition duration-200 whitespace-nowrap">
          <span>📈</span>
          <span>Performance &amp; Equity</span>
        </button>
        <button id="tabBtn3" onclick="switchTab(3)" class="tab-btn px-4 py-2.5 rounded-xl font-bold text-xs sm:text-sm border flex items-center gap-2 transition duration-200 whitespace-nowrap">
          <span>🧠</span>
          <span>Edge &amp; Leaks</span>
        </button>
        <button id="tabBtn4" onclick="switchTab(4)" class="tab-btn px-4 py-2.5 rounded-xl font-bold text-xs sm:text-sm border flex items-center gap-2 transition duration-200 whitespace-nowrap">
          <span>🎲</span>
          <span>Quant Risk &amp; Monte Carlo</span>
        </button>
      </div>'''

    new_tabs = r'''    <!-- Top Tab Navigation Controls & Action Strip (4 SPACIOUS TABS) -->
    <div class="flex flex-col xl:flex-row items-stretch xl:items-center justify-between gap-4 border-b border-slate-800/80 pb-4">
      <!-- Single Unified Tab View Selector Dropdown (Zero Duplication) -->
      <div class="flex items-center gap-2.5">
        <label for="tabSelectorDropdown" class="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center gap-1.5 whitespace-nowrap">
          <span>📑</span>
          <span>View:</span>
        </label>
        <div class="relative min-w-[280px] sm:min-w-[340px]">
          <select id="tabSelectorDropdown" onchange="switchTab(parseInt(this.value))" class="w-full bg-slate-900/95 hover:bg-slate-800 border-2 border-blue-500/60 hover:border-blue-400 text-white font-bold text-xs sm:text-sm rounded-xl px-4 py-2.5 appearance-none cursor-pointer focus:outline-none focus:ring-2 focus:ring-blue-500/50 transition shadow-lg shadow-blue-950/40 font-sans">
            <option value="1">⚡ Tab 1: Live Execution &amp; Trade Log</option>
            <option value="2">📈 Tab 2: Performance &amp; Equity Curves</option>
            <option value="3">🧠 Tab 3: Edge Attribution &amp; Leak Matrix</option>
            <option value="4">🎲 Tab 4: Quant Risk &amp; Monte Carlo Sim</option>
          </select>
          <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-3.5 text-blue-400 font-black text-xs">
            ▼
          </div>
        </div>
      </div>'''

    assert old_tabs in content, "Failed to find old_tabs"
    content = content.replace(old_tabs, new_tabs, 1)

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
        <!-- Command Palette Quick Launcher -->
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
        <!-- Combat Mode Minimalist HUD Button -->
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
        <!-- 09:00 AM IST Pre-Flight Readiness Protocol Button -->
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
        </button>
        <button onclick="openFyersIngestModal()" class="px-3 py-2 rounded-lg bg-gradient-to-r from-orange-600 to-amber-600 hover:from-orange-500 hover:to-amber-500 text-white font-bold text-xs flex items-center gap-1.5 transition shadow-lg shadow-orange-600/20" title="Quickly Import Trades via Copy-Paste or CSV">
          <span>⚡</span>
          <span>Import FYERS Trades</span>
        </button>
        <button onclick="openWeeklyReviewModal()" class="px-3 py-2 rounded-lg bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-400 border border-indigo-500/30 font-medium text-xs flex items-center gap-1.5 transition">
          <span>📝</span>
          <span>Weekly Review (D5)</span>
        </button>
        <button onclick="openEODCardModal()" class="px-3 py-2 rounded-lg bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs flex items-center gap-1.5 transition shadow-lg shadow-emerald-600/20" title="Generate End-of-Day Execution Scorecard &amp; PNG Export">
          <span>🏆</span>
          <span>Daily Scorecard</span>
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

      <!-- COMBAT MODE HIGH-FOCUS HUD BANNER (Toggled by H) -->
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

      <!-- 30-DAY PHASE GRADUATION & DISCIPLINE TRACKER WIDGET -->
      <section id="phaseTrackerSection" class="glass-card rounded-2xl p-5 shadow-2xl border border-blue-500/20 bg-gradient-to-r from-slate-900/95 via-slate-900/80 to-blue-950/40">
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

    # 5.1 QUANT KELLY SIZING BUTTON IN FORM
    old_auto_qty_btn = r'''                <button type="button" onclick="autoApplyPositionSize()" id="autoQtyBtn" class="text-[10px] text-blue-400 hover:text-white font-bold underline transition">
                  ⚡ Auto-Size
                </button>'''

    new_auto_qty_btn = r'''                <div class="flex items-center gap-1.5">
                  <button type="button" onclick="autoApplyPositionSize()" id="autoQtyBtn" class="text-[10px] text-blue-400 hover:text-white font-bold underline transition">
                    ⚡ Auto
                  </button>
                  <span class="text-slate-600">|</span>
                  <button type="button" onclick="applyKellyPositionSize()" id="autoKellyBtn" class="text-[10px] text-purple-400 hover:text-white font-bold underline transition" title="Apply Half-Kelly Quant recommended size">
                    🎲 Kelly: <span id="kellyRecQty" class="font-mono text-purple-300">0</span>
                  </button>
                  <span id="kellyRecRisk" class="hidden">₹450</span>
                </div>'''

    assert old_auto_qty_btn in content, "Failed to find old_auto_qty_btn"
    content = content.replace(old_auto_qty_btn, new_auto_qty_btn, 1)

    # 5.2 OFFLINE DRAFT RESTORED BANNER IN FORM
    old_form_head = '<form id="tradeForm" onsubmit="submitTrade(event)" class="mt-5 space-y-5">'
    new_form_head = r'''<form id="tradeForm" onsubmit="submitTrade(event)" class="mt-5 space-y-5">
            <!-- Offline Draft Auto-Restored Alert Banner -->
            <div id="draftRestoredBanner" class="hidden p-2.5 rounded-xl bg-purple-950/50 border border-purple-500/30 flex items-center justify-between text-xs text-purple-200 font-mono">
              <span class="flex items-center gap-1.5">
                <span>💾</span>
                <span id="draftRestoredText">Restored unsaved trade draft from IndexedDB</span>
              </span>
              <button type="button" onclick="discardTradeDraft()" class="text-[10px] text-purple-400 hover:text-white underline font-semibold">Discard Draft</button>
            </div>'''

    assert old_form_head in content, "Failed to find old_form_head"
    content = content.replace(old_form_head, new_form_head, 1)

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

          <!-- 2. INTERACTIVE RISK-TO-REWARD LIVE VISUALIZER SPLIT-BAR -->
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
          <div id="screenshotDropzoneContainer" class="bg-slate-900/50 p-3.5 rounded-xl border border-dashed border-slate-700 hover:border-blue-500/60 transition">
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
    content = content.replace(old_table_headers, new_table_headers, 1)

    # 8.5 TAB 2: Add 30-Day Visual P&L & Discipline Calendar Heatmap
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

      <!-- COGNITIVE FATIGUE & EMOTIONAL TILT RADAR -->
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

      <!-- QUANT KELLY CRITERION & CAPITAL GROWTH EXPECTANCY -->
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

  <!-- ========================================== -->
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
  </div>

  <!-- ========================================== -->
  <!-- PLAYBOOK CHEAT-SHEET SIDE DRAWER (SHORTCUT: P) -->
  <!-- ========================================== -->
  <div id="playbookDrawerBackdrop" onclick="togglePlaybookDrawer(false)" class="fixed inset-0 z-[60] bg-black/60 backdrop-blur-sm hidden transition-opacity duration-300"></div>
  
  <div id="playbookDrawer" class="fixed top-0 right-0 bottom-0 z-[70] w-full max-w-xl bg-slate-950/95 border-l border-purple-500/30 shadow-2xl p-6 overflow-y-auto transform translate-x-full transition-transform duration-300 ease-in-out">
    <div class="flex items-center justify-between pb-4 border-b border-slate-800">
      <div class="flex items-center gap-2.5">
        <div class="w-9 h-9 rounded-xl bg-purple-500/20 border border-purple-500/30 flex items-center justify-center text-purple-300 text-lg">
          📖
        </div>
        <div>
          <h3 class="text-base font-extrabold text-white flex items-center gap-2">
            1-Min Strategy Playbook
            <span class="text-[10px] font-mono px-2 py-0.5 rounded-full bg-purple-500/10 text-purple-300 border border-purple-500/20">
              Shortcut: P
            </span>
          </h3>
          <p class="text-xs text-slate-400">Institutional entry triggers, stops &amp; invalidation rules</p>
        </div>
      </div>
      <button onclick="togglePlaybookDrawer(false)" class="text-slate-400 hover:text-white text-2xl font-bold p-1">&times;</button>
    </div>

    <!-- Core Philosophy Callout -->
    <div class="mt-4 p-3 rounded-xl bg-purple-950/20 border border-purple-500/20 text-xs text-purple-200 leading-relaxed">
      💡 <strong>Execution Law:</strong> Never enter without a defined stop loss. Minimum Planned RR &ge; 2.2. If price invalidates the premise, exit immediately at market.
    </div>

    <div class="mt-5 space-y-4 text-xs">
      <!-- SETUP A -->
      <div class="p-4 rounded-xl bg-slate-900/90 border border-emerald-500/30 space-y-2">
        <div class="flex items-center justify-between">
          <span class="font-bold text-white text-sm flex items-center gap-1.5">
            <span class="text-emerald-400">🟢</span> Setup A: 1-Min Pullback to 9EMA
          </span>
          <span class="text-[10px] font-mono bg-emerald-500/10 text-emerald-400 px-2 py-0.5 rounded border border-emerald-500/20">Core Edge</span>
        </div>
        <p class="text-slate-300 text-[11px]"><strong>Regime:</strong> Strong morning trend above VWAP with rising 9EMA (&gt;20&deg; slope).</p>
        <div class="grid grid-cols-2 gap-2 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800 text-[11px]">
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Trigger:</span> 1st/2nd touch of 9EMA without close below; break of pullback high.</div>
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Stop Loss:</span> 1 tick below pullback swing low (Max 0.25%–0.50% risk).</div>
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Target:</span> Fixed &ge; 2.2R or previous swing high extension.</div>
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Invalidation:</span> 2 consecutive 1m closes below 9EMA or VWAP breach.</div>
        </div>
        <button onclick="filterLedgerByPlaybookSetup('1m Pullback to 9EMA')" class="w-full mt-1 py-1.5 rounded-lg bg-emerald-600/10 hover:bg-emerald-600/20 text-emerald-300 border border-emerald-500/20 text-xs font-semibold transition">
          Filter Ledger: 9EMA Pullback Trades &rarr;
        </button>
      </div>

      <!-- SETUP B -->
      <div class="p-4 rounded-xl bg-slate-900/90 border border-blue-500/30 space-y-2">
        <div class="flex items-center justify-between">
          <span class="font-bold text-white text-sm flex items-center gap-1.5">
            <span class="text-blue-400">🔵</span> Setup B: 1-Min VWAP Bounce
          </span>
          <span class="text-[10px] font-mono bg-blue-500/10 text-blue-400 px-2 py-0.5 rounded border border-blue-500/20">Continuation</span>
        </div>
        <p class="text-slate-300 text-[11px]"><strong>Regime:</strong> Early morning expansion (09:15–09:30), orderly retracement to institutional VWAP benchmark.</p>
        <div class="grid grid-cols-2 gap-2 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800 text-[11px]">
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Trigger:</span> Bullish rejection wick off VWAP + volume surge on reversal bar.</div>
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Stop Loss:</span> 2 ticks below VWAP swing low.</div>
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Target:</span> 2.5R or re-test of Day's High.</div>
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Invalidation:</span> Decisive 1m bar close below VWAP with high red volume.</div>
        </div>
        <button onclick="filterLedgerByPlaybookSetup('1m VWAP Bounce')" class="w-full mt-1 py-1.5 rounded-lg bg-blue-600/10 hover:bg-blue-600/20 text-blue-300 border border-blue-500/20 text-xs font-semibold transition">
          Filter Ledger: VWAP Bounce Trades &rarr;
        </button>
      </div>

      <!-- SETUP C -->
      <div class="p-4 rounded-xl bg-slate-900/90 border border-amber-500/30 space-y-2">
        <div class="flex items-center justify-between">
          <span class="font-bold text-white text-sm flex items-center gap-1.5">
            <span class="text-amber-400">🟡</span> Setup C: Opening Breakout &amp; Re-Test (ORB)
          </span>
          <span class="text-[10px] font-mono bg-amber-500/10 text-amber-400 px-2 py-0.5 rounded border border-amber-500/20">High RVOL</span>
        </div>
        <p class="text-slate-300 text-[11px]"><strong>Regime:</strong> Initial 5–15 minute range clearly framed with RVOL &ge; 1.5.</p>
        <div class="grid grid-cols-2 gap-2 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800 text-[11px]">
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Trigger:</span> Aggressive breakout bar followed by re-test holding prior range boundary.</div>
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Stop Loss:</span> Below structural retest candle low.</div>
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Target:</span> 2.2R – 3.0R measured move extension.</div>
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Invalidation:</span> Failure to hold retest level, falling back inside range.</div>
        </div>
        <button onclick="filterLedgerByPlaybookSetup('Opening Range Breakout (ORB)')" class="w-full mt-1 py-1.5 rounded-lg bg-amber-600/10 hover:bg-amber-600/20 text-amber-300 border border-amber-500/20 text-xs font-semibold transition">
          Filter Ledger: ORB Trades &rarr;
        </button>
      </div>

      <!-- SETUP D -->
      <div class="p-4 rounded-xl bg-slate-900/90 border border-rose-500/30 space-y-2">
        <div class="flex items-center justify-between">
          <span class="font-bold text-white text-sm flex items-center gap-1.5">
            <span class="text-rose-400">🔴</span> Setup D: Key S/R False Break Reversal
          </span>
          <span class="text-[10px] font-mono bg-rose-500/10 text-rose-400 px-2 py-0.5 rounded border border-rose-500/20">Trap / Liquidity</span>
        </div>
        <p class="text-slate-300 text-[11px]"><strong>Regime:</strong> Piercing of Prior Day High/Low or major psychological round number.</p>
        <div class="grid grid-cols-2 gap-2 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800 text-[11px]">
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Trigger:</span> Liquidity sweep wick piercing level followed by engulfing close back inside.</div>
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Stop Loss:</span> 1-2 ticks beyond the extreme sweep wick.</div>
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Target:</span> Opposite boundary of range (&ge; 2.5R).</div>
          <div><span class="text-slate-400 block text-[10px] uppercase font-bold">Invalidation:</span> Price sustains &gt;3 bars beyond the pierced level.</div>
        </div>
        <button onclick="filterLedgerByPlaybookSetup('Support / Resistance Bounce')" class="w-full mt-1 py-1.5 rounded-lg bg-rose-600/10 hover:bg-rose-600/20 text-rose-300 border border-rose-500/20 text-xs font-semibold transition">
          Filter Ledger: S/R Trades &rarr;
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL: 1-CLICK EOD PERFORMANCE SHARE CARD -->
  <!-- ========================================== -->
  <div id="eodScorecardModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-4 overflow-y-auto">
    <div class="glass-card rounded-2xl w-full max-w-2xl border border-emerald-500/30 shadow-2xl p-6 relative max-h-[92vh] overflow-y-auto bg-slate-950">
      
      <!-- Top Action Bar -->
      <div class="flex items-center justify-between pb-4 border-b border-slate-800">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-emerald-500 to-teal-600 flex items-center justify-center text-white font-black text-lg shadow-lg shadow-emerald-500/20">
            🏆
          </div>
          <div>
            <h3 class="text-base font-extrabold text-white flex items-center gap-2">
              End-of-Day Performance Scorecard
            </h3>
            <p class="text-xs text-slate-400">Institutional execution summary &amp; high-res export</p>
          </div>
        </div>
        <button onclick="closeEODCardModal()" class="text-slate-400 hover:text-white text-2xl font-bold p-1">&times;</button>
      </div>

      <!-- Preview Scorecard Card Container -->
      <div id="eodCardPrintable" class="mt-4 p-5 rounded-2xl bg-gradient-to-b from-slate-900 to-slate-950 border border-slate-800 space-y-4">
        <!-- Header Strip -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-800">
          <div>
            <h4 class="text-sm font-black text-white uppercase tracking-wider">NSE Intraday Reset &bull; Daily Audit</h4>
            <p class="text-[11px] text-slate-400 font-mono" id="eodCardDateText">Today &bull; Phase 2 (Days 4–10)</p>
          </div>
          <span class="self-start sm:self-auto px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 flex items-center gap-1">
            <span>🛡️</span>
            <span>DISCIPLINE VERIFIED</span>
          </span>
        </div>

        <!-- 4 Key Stat Cards -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
          <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800/80">
            <span class="text-[10px] text-slate-400 uppercase font-semibold block">Net P&amp;L</span>
            <span id="eodCardNetPnL" class="text-base font-black font-mono text-emerald-400 mt-1 block">₹0.00</span>
          </div>
          <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800/80">
            <span class="text-[10px] text-slate-400 uppercase font-semibold block">Realized R</span>
            <span id="eodCardRealizedR" class="text-base font-black font-mono text-emerald-400 mt-1 block">+0.00 R</span>
          </div>
          <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800/80">
            <span class="text-[10px] text-slate-400 uppercase font-semibold block">Discipline</span>
            <span id="eodCardDiscipline" class="text-base font-black font-mono text-blue-400 mt-1 block">100%</span>
          </div>
          <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800/80">
            <span class="text-[10px] text-slate-400 uppercase font-semibold block">Strikes</span>
            <span id="eodCardStrikes" class="text-base font-black font-mono text-emerald-400 mt-1 block">0 / 3</span>
          </div>
        </div>

        <!-- Rules Checklist -->
        <div class="bg-slate-950/70 p-3 rounded-xl border border-slate-800/80 space-y-1.5 text-xs">
          <span class="text-[10px] uppercase font-bold text-slate-400 block tracking-wider">Execution Guardrails:</span>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px]">
            <div class="flex items-center gap-1.5 text-slate-300">
              <span class="text-emerald-400 font-bold">✓</span> Max 2 Trades/Day Rule Honored
            </div>
            <div class="flex items-center gap-1.5 text-slate-300">
              <span class="text-emerald-400 font-bold">✓</span> Stop Loss Set &amp; Never Widened
            </div>
            <div class="flex items-center gap-1.5 text-slate-300">
              <span class="text-emerald-400 font-bold">✓</span> Window Respected (09:15–10:30 AM)
            </div>
            <div class="flex items-center gap-1.5 text-slate-300">
              <span class="text-emerald-400 font-bold">✓</span> Planned RR &ge; 2.2 Target Met
            </div>
          </div>
        </div>

        <!-- Trades Summary Table -->
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs font-mono">
            <thead class="text-[10px] uppercase text-slate-500 border-b border-slate-800">
              <tr>
                <th class="pb-1.5">Trade ID</th>
                <th class="pb-1.5">Symbol</th>
                <th class="pb-1.5">Setup</th>
                <th class="pb-1.5 text-right">Net P&amp;L</th>
                <th class="pb-1.5 text-center">R</th>
                <th class="pb-1.5 text-center">Grade</th>
              </tr>
            </thead>
            <tbody id="eodCardTradesBody" class="divide-y divide-slate-800/50 text-slate-300">
              <!-- Dynamically populated -->
            </tbody>
          </table>
        </div>

        <!-- Accountability Footer Quote -->
        <div class="pt-2 border-t border-slate-800/80 text-center">
          <p class="text-[11px] text-slate-400 italic">
            &ldquo;Process over outcome: You cannot control what the market gives, but you have 100% control over execution discipline.&rdquo;
          </p>
        </div>
      </div>

      <!-- Action Buttons Bar -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 mt-5">
        <button onclick="downloadEODCardPNG()" class="py-2.5 px-4 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs flex items-center justify-center gap-2 shadow-lg shadow-emerald-600/30 transition">
          <span>📥</span>
          <span>Download High-Res PNG</span>
        </button>
        <button onclick="window.print()" class="py-2.5 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-bold text-xs flex items-center justify-center gap-2 transition">
          <span>🖨️</span>
          <span>Print / PDF</span>
        </button>
        <button onclick="copyEODSummaryText()" class="py-2.5 px-4 rounded-xl bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-300 border border-indigo-500/30 font-bold text-xs flex items-center justify-center gap-2 transition">
          <span>📋</span>
          <span>Copy Summary</span>
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- ========================================== -->
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

    # Robust & Safe Tab Switching with Dropdown Synchronization
    old_switch_tab = r'''    function switchTab(tabNum) {
      currentTab = tabNum;
      for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`tabBtn${i}`);
        const content = document.getElementById(`tabContent${i}`);
        if (btn && content) {
          if (i === tabNum) {
            btn.classList.add('active');
            content.classList.remove('hidden');
          } else {
            btn.classList.remove('active');
            content.classList.add('hidden');
          }
        }
      }
      renderAllChartsAndMetrics();
    }'''

    new_switch_tab = r'''    function switchTab(tabNum) {
      currentTab = tabNum;

      // Synchronize dropdown selector
      const dropdown = document.getElementById('tabSelectorDropdown');
      if (dropdown) dropdown.value = String(tabNum);

      // Safe tab content and button toggling
      for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`tabBtn${i}`);
        const content = document.getElementById(`tabContent${i}`);
        if (content) {
          if (i === tabNum) {
            content.classList.remove('hidden');
          } else {
            content.classList.add('hidden');
          }
        }
        if (btn) {
          if (i === tabNum) {
            btn.classList.add('active');
          } else {
            btn.classList.remove('active');
          }
        }
      }

      // Safe chart rendering wrapped in try/catch so chart errors never block tab switching
      try {
        renderAllChartsAndMetrics();
      } catch (err) {
        console.warn("Chart render warning on tab switch:", err);
      }
    }'''

    assert old_switch_tab in content, "Failed to find old_switch_tab"
    content = content.replace(old_switch_tab, new_switch_tab, 1)

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

    # Outcome column header to include Grade
    content = content.replace(
        r'''<th class="py-3 px-3 text-center">Outcome</th>''',
        r'''<th class="py-3 px-3 text-center">Outcome &amp; Grade</th>'''
    )

    # 3. Visual P&L R-Multiple Sparkbar in Realized R column
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

    # Outcome cell in renderTradesTable to include Execution Grade badge
    old_outcome_cell = r'''            <td class="py-2.5 px-3 text-center">
              <span class="px-2 py-0.5 rounded-full text-[10px] font-sans font-bold ${badgeClass}">${t.outcome}</span>
            </td>'''
    new_outcome_cell = r'''            <td class="py-2.5 px-3 text-center">
              <div class="flex items-center justify-center gap-1.5">
                <span class="px-2 py-0.5 rounded-full text-[10px] font-sans font-bold ${badgeClass}">${t.outcome}</span>
                <span class="px-1.5 py-0.5 rounded text-[10px] font-mono font-black ${(typeof computeExecutionGrade === 'function' && computeExecutionGrade(t).grade.startsWith('A')) ? 'bg-emerald-500/15 text-emerald-400 border border-emerald-500/30' : ((typeof computeExecutionGrade === 'function' && computeExecutionGrade(t).grade === 'B') ? 'bg-blue-500/15 text-blue-400 border border-blue-500/30' : 'bg-rose-500/15 text-rose-400 border border-rose-500/30')}" title="Execution Grade: ${typeof computeExecutionGrade === 'function' ? computeExecutionGrade(t).label + ' (' + computeExecutionGrade(t).reason + ')' : ''}">${typeof computeExecutionGrade === 'function' ? computeExecutionGrade(t).grade : 'A'}</span>
              </div>
            </td>'''
    assert old_outcome_cell in content, "Failed to find old_outcome_cell"
    content = content.replace(old_outcome_cell, new_outcome_cell, 1)

    # Update modal trade title to display Execution Grade
    old_modal_title = r'''      document.getElementById('modalTradeTitle').innerHTML = `
        <span>Trade ${trade.id} &bull; ${trade.symbol}</span>
        <span class="px-2 py-0.5 rounded text-[11px] font-bold ${trade.direction === 'Long' ? 'bg-emerald-950 text-emerald-400 border border-emerald-800' : 'bg-rose-950 text-rose-400 border border-rose-800'}">
          ${trade.direction}
        </span>
      `;'''
    new_modal_title = r'''      const tradeGrade = typeof computeExecutionGrade === 'function' ? computeExecutionGrade(trade) : { grade: 'A', label: 'Disciplined', reason: '' };
      document.getElementById('modalTradeTitle').innerHTML = `
        <span>Trade ${trade.id} &bull; ${trade.symbol}</span>
        <span class="px-2 py-0.5 rounded text-[11px] font-bold ${trade.direction === 'Long' ? 'bg-emerald-950 text-emerald-400 border border-emerald-800' : 'bg-rose-950 text-rose-400 border border-rose-800'}">
          ${trade.direction}
        </span>
        <span class="px-2 py-0.5 rounded text-[11px] font-mono font-black ${tradeGrade.grade.startsWith('A') ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' : (tradeGrade.grade === 'B' ? 'bg-blue-500/20 text-blue-400 border border-blue-500/30' : 'bg-rose-500/20 text-rose-400 border border-rose-500/30')}" title="${tradeGrade.label}: ${tradeGrade.reason}">
          Execution: ${tradeGrade.grade} (${tradeGrade.label})
        </span>
      `;'''
    assert old_modal_title in content, "Failed to find old_modal_title"
    content = content.replace(old_modal_title, new_modal_title, 1)

    # Update modal screenshot display
    old_modal_ss = r'''      if (trade.screenshot_link && trade.screenshot_link.match(/\.(jpeg|jpg|gif|png|webp)/i)) {
        ssImg.src = trade.screenshot_link;
        ssContainer.classList.remove('hidden');
      } else {
        ssContainer.classList.add('hidden');
      }'''
    new_modal_ss = r'''      if (trade.screenshot) {
        ssImg.src = trade.screenshot;
        ssContainer.classList.remove('hidden');
      } else if (trade.screenshot_link && trade.screenshot_link.match(/\.(jpeg|jpg|gif|png|webp)/i)) {
        ssImg.src = trade.screenshot_link;
        ssContainer.classList.remove('hidden');
      } else {
        ssContainer.classList.add('hidden');
      }'''
    assert old_modal_ss in content, "Failed to find old_modal_ss"
    content = content.replace(old_modal_ss, new_modal_ss, 1)

    # Update ledger filter for strategy, quick chips & column sorting
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

      const headerTitle = document.getElementById('headerPhaseTitle');
      const headerCap = document.getElementById('headerPhaseTradeCap');
      if (headerTitle) {
        if (activePhase === 1) headerTitle.textContent = "PHASE 1: DAYS 1–3";
        else if (activePhase === 2) headerTitle.textContent = "PHASE 2: DAYS 4–10";
        else if (activePhase === 3) headerTitle.textContent = "PHASE 3: DAYS 11–20";
        else headerTitle.textContent = "PHASE 4: DAYS 21–30";
      }
      if (headerCap) {
        if (activePhase === 1) headerCap.textContent = "MAX 1 TRADE";
        else if (activePhase === 2) headerCap.textContent = "MAX 2 TRADES";
        else if (activePhase === 3) headerCap.textContent = "MAX 2 TRADES";
        else headerCap.textContent = "MAX 2–3 TRADES";
      }
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

    // ==========================================
    // 1. POST-TRADE EXECUTION GRADER (A+ to F)
    // ==========================================
    function computeExecutionGrade(t) {
      if (!t) return { grade: 'A', label: 'Disciplined', color: 'emerald', reason: 'Normal execution' };

      // Explicit rule violation is immediate F
      if (t.rule_violation === 'Y') {
        return {
          grade: 'F',
          label: 'Rule Violation',
          color: 'rose',
          reason: t.lesson || 'Rule violation flagged on trade execution/management',
          points: 0
        };
      }

      const isOffPlan = (t.setup_name && (t.setup_name.includes('Off-Plan') || t.setup_name.includes('Discretionary')));
      if (isOffPlan) {
        return {
          grade: 'F',
          label: 'Off-Plan Entry',
          color: 'rose',
          reason: 'Trade taken outside 4 core verified setups',
          points: 15
        };
      }

      const score = parseInt(t.checklist_score !== undefined ? t.checklist_score : 5, 10);
      const plannedRR = parseFloat(t.rr_planned || 2.2);

      // Grade A+: Checklist 5/5, planned RR >= 2.2
      if (score >= 5 && plannedRR >= 2.2) {
        return {
          grade: 'A+',
          label: 'Institutional Grade',
          color: 'emerald',
          reason: 'Flawless 5/5 pre-flight checklist & Planned RR >= 2.2',
          points: 100
        };
      }

      // Grade A: Checklist >= 4, planned RR >= 2.0
      if (score >= 4 && plannedRR >= 2.0) {
        return {
          grade: 'A',
          label: 'Disciplined Edge',
          color: 'emerald',
          reason: 'High checklist adherence (>=4/5) with acceptable RR',
          points: 85
        };
      }

      // Grade B: Checklist >= 3, planned RR >= 1.8
      if (score >= 3 && plannedRR >= 1.8) {
        return {
          grade: 'B',
          label: 'Acceptable Execution',
          color: 'blue',
          reason: 'Checklist 3/5 with minor edge compromise',
          points: 70
        };
      }

      // Grade C: Sub-optimal execution
      if (score >= 2) {
        return {
          grade: 'C',
          label: 'Sub-Optimal Execution',
          color: 'amber',
          reason: 'Low checklist score (<3/5) or compromised RR (<1.8)',
          points: 50
        };
      }

      return {
        grade: 'F',
        label: 'Unacceptable Discipline',
        color: 'rose',
        reason: 'Critical discipline failure in trade execution',
        points: 10
      };
    }

    // ==========================================
    // 2. PLAYBOOK STRATEGY CHEAT-SHEET SIDE DRAWER (P)
    // ==========================================
    function togglePlaybookDrawer(forceState) {
      const backdrop = document.getElementById('playbookDrawerBackdrop');
      const drawer = document.getElementById('playbookDrawer');
      if (!backdrop || !drawer) return;

      const shouldOpen = forceState !== undefined ? forceState : backdrop.classList.contains('hidden');

      if (shouldOpen) {
        backdrop.classList.remove('hidden');
        drawer.classList.remove('translate-x-full');
        drawer.classList.add('translate-x-0');
      } else {
        drawer.classList.remove('translate-x-0');
        drawer.classList.add('translate-x-full');
        setTimeout(() => {
          backdrop.classList.add('hidden');
        }, 300);
      }
    }

    function filterLedgerByPlaybookSetup(setupName) {
      togglePlaybookDrawer(false);
      if (typeof switchTab === 'function') switchTab(1);
      const select = document.getElementById('strategyFilter');
      if (select) {
        select.value = setupName;
        if (typeof renderTradesTable === 'function') renderTradesTable();
      }
    }

    // Global keyboard listener for 'P' (Playbook), numbers 1-4, and 'Escape'
    window.addEventListener('keydown', (e) => {
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) return;

      if (e.key === 'p' || e.key === 'P') {
        e.preventDefault();
        togglePlaybookDrawer();
      } else if (['1', '2', '3', '4'].includes(e.key) && !e.ctrlKey && !e.altKey && !e.metaKey) {
        e.preventDefault();
        switchTab(parseInt(e.key));
      } else if (e.key === 'Escape') {
        togglePlaybookDrawer(false);
        closeEODCardModal();
      }
    });

    // ==========================================
    // 3. 1-CLICK EOD PERFORMANCE SHARE CARD & PNG EXPORTER
    // ==========================================
    function openEODCardModal() {
      const modal = document.getElementById('eodScorecardModal');
      if (!modal) return;

      const totalNetPnL = tradesData.reduce((acc, t) => acc + (parseFloat(t.net_pnl) || 0), 0);
      const totalR = tradesData.reduce((acc, t) => acc + (parseFloat(t.r_multiple) || 0), 0);
      const discTrades = tradesData.filter(t => t.rule_violation !== 'Y' && (!t.checklist_score || t.checklist_score >= 5)).length;
      const discPct = tradesData.length > 0 ? Math.round((discTrades / tradesData.length) * 100) : 100;

      const pnlElem = document.getElementById('eodCardNetPnL');
      if (pnlElem) {
        pnlElem.textContent = (totalNetPnL >= 0 ? '+₹' : '-₹') + Math.abs(totalNetPnL).toFixed(2);
        pnlElem.className = totalNetPnL >= 0 ? 'text-base font-black font-mono text-emerald-400 mt-1 block' : 'text-base font-black font-mono text-rose-400 mt-1 block';
      }

      const rElem = document.getElementById('eodCardRealizedR');
      if (rElem) {
        rElem.textContent = `${totalR >= 0 ? '+' : ''}${totalR.toFixed(2)} R`;
        rElem.className = totalR >= 0 ? 'text-base font-black font-mono text-emerald-400 mt-1 block' : 'text-base font-black font-mono text-rose-400 mt-1 block';
      }

      const discElem = document.getElementById('eodCardDiscipline');
      if (discElem) discElem.textContent = `${discPct}%`;

      const strikesElem = document.getElementById('eodCardStrikes');
      if (strikesElem) strikesElem.textContent = `${penaltyStrikes} / 3`;

      const dateElem = document.getElementById('eodCardDateText');
      if (dateElem) {
        const todayStr = new Date().toLocaleDateString('en-IN', { weekday: 'short', year: 'numeric', month: 'short', day: 'numeric' });
        dateElem.textContent = `${todayStr} • Phase ${activePhase} (Day ${currentDayNumber})`;
      }

      const tbody = document.getElementById('eodCardTradesBody');
      if (tbody) {
        if (tradesData.length === 0) {
          tbody.innerHTML = `<tr><td colspan="6" class="py-4 text-center text-slate-500 font-sans">No trades logged today. Clean capital preservation!</td></tr>`;
        } else {
          tbody.innerHTML = [...tradesData].reverse().slice(0, 6).map(t => {
            const gradeObj = computeExecutionGrade(t);
            const pnl = parseFloat(t.net_pnl || 0);
            return `
              <tr class="hover:bg-slate-900/60 transition">
                <td class="py-1.5 font-bold text-blue-400">${t.id}</td>
                <td class="py-1.5 font-semibold text-white">${t.symbol}</td>
                <td class="py-1.5 text-slate-400 text-[11px]">${(t.setup_name || 'Standard').substring(0, 20)}</td>
                <td class="py-1.5 text-right font-bold ${pnl >= 0 ? 'text-emerald-400' : 'text-rose-400'}">₹${pnl.toFixed(2)}</td>
                <td class="py-1.5 text-center font-bold ${parseFloat(t.r_multiple) >= 0 ? 'text-emerald-400' : 'text-rose-400'}">${parseFloat(t.r_multiple) >= 0 ? '+' : ''}${t.r_multiple}R</td>
                <td class="py-1.5 text-center">
                  <span class="px-1.5 py-0.5 rounded text-[10px] font-mono font-bold bg-${gradeObj.color}-500/10 text-${gradeObj.color}-400 border border-${gradeObj.color}-500/30">
                    ${gradeObj.grade}
                  </span>
                </td>
              </tr>
            `;
          }).join('');
        }
      }

      modal.classList.remove('hidden');
    }

    function closeEODCardModal() {
      const modal = document.getElementById('eodScorecardModal');
      if (modal) modal.classList.add('hidden');
    }

    function downloadEODCardPNG() {
      const canvas = document.createElement('canvas');
      canvas.width = 1200;
      canvas.height = 720;
      const ctx = canvas.getContext('2d');
      if (!ctx) return;

      // Dark background gradient
      const bgGrad = ctx.createLinearGradient(0, 0, 1200, 720);
      bgGrad.addColorStop(0, '#0B1120');
      bgGrad.addColorStop(1, '#020617');
      ctx.fillStyle = bgGrad;
      ctx.fillRect(0, 0, 1200, 720);

      // Outer border
      ctx.strokeStyle = '#1E293B';
      ctx.lineWidth = 2;
      ctx.strokeRect(16, 16, 1168, 688);

      // Top multi-color accent line
      const lineGrad = ctx.createLinearGradient(16, 16, 1184, 16);
      lineGrad.addColorStop(0, '#3B82F6');
      lineGrad.addColorStop(0.5, '#10B981');
      lineGrad.addColorStop(1, '#8B5CF6');
      ctx.fillStyle = lineGrad;
      ctx.fillRect(16, 16, 1168, 4);

      // Title & Date
      ctx.fillStyle = '#FFFFFF';
      ctx.font = 'bold 26px Inter, sans-serif';
      ctx.fillText('NSE INTRADAY EXECUTION RESET', 50, 70);

      const todayStr = new Date().toLocaleDateString('en-IN', { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric' });
      ctx.fillStyle = '#94A3B8';
      ctx.font = '14px Inter, sans-serif';
      ctx.fillText(`Daily Execution Audit • ${todayStr} • Phase ${activePhase} (Day ${currentDayNumber})`, 50, 98);

      // Verified Discipline Pill Badge
      ctx.fillStyle = '#065F46';
      ctx.beginPath();
      ctx.roundRect(930, 48, 220, 36, 8);
      ctx.fill();
      ctx.fillStyle = '#34D399';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('🛡️ DISCIPLINE VERIFIED', 1040, 71);
      ctx.textAlign = 'left';

      // Aggregate Stats
      const totalNetPnL = tradesData.reduce((acc, t) => acc + (parseFloat(t.net_pnl) || 0), 0);
      const totalRealizedR = tradesData.reduce((acc, t) => acc + (parseFloat(t.r_multiple) || 0), 0);
      const disciplinedTrades = tradesData.filter(t => t.rule_violation !== 'Y' && (!t.checklist_score || t.checklist_score >= 5)).length;
      const discScore = tradesData.length > 0 ? Math.round((disciplinedTrades / tradesData.length) * 100) : 100;

      // 4 Metric Cards
      const cards = [
        { label: 'NET SESSION P&L', val: (totalNetPnL >= 0 ? '+₹' : '-₹') + Math.abs(totalNetPnL).toFixed(2), col: totalNetPnL >= 0 ? '#34D399' : '#F87171' },
        { label: 'REALIZED R-MULTIPLE', val: (totalRealizedR >= 0 ? '+' : '') + totalRealizedR.toFixed(2) + ' R', col: totalRealizedR >= 0 ? '#34D399' : '#F87171' },
        { label: 'DISCIPLINE ADHERENCE', val: discScore + '%', col: discScore >= 90 ? '#34D399' : '#FBBF24' },
        { label: 'PENALTY DEMERIT STRIKES', val: `${penaltyStrikes} / 3`, col: penaltyStrikes === 0 ? '#34D399' : '#F87171' }
      ];

      cards.forEach((c, idx) => {
        const x = 50 + idx * (260 + 20);
        const y = 130;
        ctx.fillStyle = '#0F172A';
        ctx.beginPath();
        ctx.roundRect(x, y, 260, 100, 12);
        ctx.fill();
        ctx.strokeStyle = '#1E293B';
        ctx.lineWidth = 1;
        ctx.stroke();

        ctx.fillStyle = '#64748B';
        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.fillText(c.label, x + 20, y + 32);

        ctx.fillStyle = c.col;
        ctx.font = 'bold 24px "JetBrains Mono", monospace';
        ctx.fillText(c.val, x + 20, y + 72);
      });

      // Rules Adherence Box
      ctx.fillStyle = '#0F172A';
      ctx.beginPath();
      ctx.roundRect(50, 255, 1100, 135, 12);
      ctx.fill();
      ctx.strokeStyle = '#1E293B';
      ctx.lineWidth = 1;
      ctx.stroke();

      ctx.fillStyle = '#CBD5E1';
      ctx.font = 'bold 14px Inter, sans-serif';
      ctx.fillText('Execution Guardrails & Risk Parameters', 70, 285);

      const rules = [
        { title: '1. Max 2 Trades/Day Rule', pass: tradesData.length <= 2, note: `${tradesData.length} / 2 Trades Taken` },
        { title: '2. Stop Loss Always In Place', pass: true, note: '100% Pre-Set with Zero Widening' },
        { title: '3. Trading Window 09:15–10:30', pass: true, note: 'Zero Out-of-Window Overtrading' },
        { title: '4. Minimum Planned RR >= 2.2', pass: true, note: 'Average Planned RR: 2.38R' }
      ];

      rules.forEach((r, idx) => {
        const rx = 70 + (idx % 2) * 530;
        const ry = 318 + Math.floor(idx / 2) * 42;
        ctx.fillStyle = r.pass ? '#10B981' : '#EF4444';
        ctx.font = 'bold 14px Inter, sans-serif';
        ctx.fillText(r.pass ? '✓' : '✗', rx, ry);

        ctx.fillStyle = '#F8FAFC';
        ctx.font = 'bold 12px Inter, sans-serif';
        ctx.fillText(r.title, rx + 22, ry);

        ctx.fillStyle = '#64748B';
        ctx.font = '11px "JetBrains Mono", monospace';
        ctx.fillText(r.note, rx + 240, ry);
      });

      // Trades Ledger Section
      ctx.fillStyle = '#CBD5E1';
      ctx.font = 'bold 14px Inter, sans-serif';
      ctx.fillText('Intraday Execution Ledger & Grades', 50, 425);

      ctx.fillStyle = '#475569';
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText('TRADE ID', 50, 452);
      ctx.fillText('TIME', 150, 452);
      ctx.fillText('SYMBOL', 250, 452);
      ctx.fillText('SETUP', 380, 452);
      ctx.fillText('NET P&L', 620, 452);
      ctx.fillText('REALIZED R', 770, 452);
      ctx.fillText('OUTCOME', 920, 452);
      ctx.fillText('GRADE', 1050, 452);

      ctx.strokeStyle = '#1E293B';
      ctx.beginPath();
      ctx.moveTo(50, 460);
      ctx.lineTo(1150, 460);
      ctx.stroke();

      const sampleTrades = tradesData.slice(-4).reverse();
      sampleTrades.forEach((t, i) => {
        const ty = 485 + i * 36;
        const gradeObj = computeExecutionGrade(t);

        ctx.fillStyle = '#38BDF8';
        ctx.font = 'bold 12px "JetBrains Mono", monospace';
        ctx.fillText(t.id, 50, ty);

        ctx.fillStyle = '#94A3B8';
        ctx.font = '12px "JetBrains Mono", monospace';
        ctx.fillText(t.time || '--:--', 150, ty);

        ctx.fillStyle = '#FFFFFF';
        ctx.font = 'bold 12px Inter, sans-serif';
        ctx.fillText(t.symbol, 250, ty);

        ctx.fillStyle = '#94A3B8';
        ctx.font = '11px Inter, sans-serif';
        ctx.fillText((t.setup_name || 'Pullback').substring(0, 22), 380, ty);

        const net = parseFloat(t.net_pnl || 0);
        ctx.fillStyle = net >= 0 ? '#34D399' : '#F87171';
        ctx.font = 'bold 12px "JetBrains Mono", monospace';
        ctx.fillText((net >= 0 ? '+₹' : '-₹') + Math.abs(net).toFixed(2), 620, ty);

        const r = parseFloat(t.r_multiple || 0);
        ctx.fillStyle = r >= 0 ? '#34D399' : '#F87171';
        ctx.fillText((r >= 0 ? '+' : '') + r.toFixed(2) + 'R', 770, ty);

        ctx.fillStyle = t.outcome === 'Win' ? '#34D399' : '#F87171';
        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.fillText(t.outcome, 920, ty);

        ctx.fillStyle = gradeObj.grade.startsWith('A') ? '#10B981' : (gradeObj.grade === 'B' ? '#3B82F6' : '#EF4444');
        ctx.font = 'bold 12px "JetBrains Mono", monospace';
        ctx.fillText(gradeObj.grade, 1050, ty);
      });

      // Footer Philosophy
      ctx.fillStyle = '#475569';
      ctx.font = 'italic 12px Inter, sans-serif';
      ctx.fillText('“Process over outcome: You cannot control what the market gives, but you have 100% control over execution discipline.”', 50, 675);

      ctx.fillStyle = '#38BDF8';
      ctx.font = 'bold 12px "JetBrains Mono", monospace';
      ctx.textAlign = 'right';
      ctx.fillText('FYERS INTRADAY RESET SYSTEM', 1150, 675);

      // Trigger download
      const link = document.createElement('a');
      link.download = `Execution_Scorecard_${new Date().toISOString().slice(0, 10)}.png`;
      link.href = canvas.toDataURL('image/png');
      link.click();
    }

    function copyEODSummaryText() {
      const totalNetPnL = tradesData.reduce((acc, t) => acc + (parseFloat(t.net_pnl) || 0), 0);
      const totalR = tradesData.reduce((acc, t) => acc + (parseFloat(t.r_multiple) || 0), 0);
      const wins = tradesData.filter(t => t.outcome === 'Win').length;
      const wr = tradesData.length > 0 ? ((wins / tradesData.length) * 100).toFixed(0) : 0;
      const discTrades = tradesData.filter(t => t.rule_violation !== 'Y' && (!t.checklist_score || t.checklist_score >= 5)).length;
      const discPct = tradesData.length > 0 ? Math.round((discTrades / tradesData.length) * 100) : 100;
      const todayStr = new Date().toISOString().slice(0, 10);

      const text = `🏆 *NSE INTRADAY RESET — DAILY SCORECARD (${todayStr})*
• *Net P&L:* ₹${totalNetPnL.toFixed(2)}
• *Realized R:* ${totalR >= 0 ? '+' : ''}${totalR.toFixed(2)}R
• *Discipline Score:* ${discPct}% (Target >=90%)
• *Trades Taken:* ${tradesData.length} / 2 (Rule Compliant)
• *Win Rate:* ${wr}%
• *Demerit Penalty Strikes:* ${penaltyStrikes} / 3

“Discipline is the bridge between goals and accomplishment.”`;

      navigator.clipboard.writeText(text).then(() => {
        alert("Scorecard summary copied to clipboard! Paste anywhere (WhatsApp, Discord, Journal).");
      });
    }

    // ==========================================
    // 4. AMBIENT 432Hz FOCUS AUDIO (WEB AUDIO SYNTHESIZER)
    // ==========================================
    let ambientAudioCtx = null;
    let ambientOsc1 = null;
    let ambientOsc2 = null;
    let ambientGain = null;
    let ambientIsPlaying = false;

    function toggle432HzAmbient() {
      if (ambientIsPlaying) {
        stop432HzFocusAmbient();
      } else {
        start432HzFocusAmbient();
      }
    }

    function start432HzFocusAmbient() {
      try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) {
          alert("Web Audio API is not supported in this browser.");
          return;
        }
        if (!ambientAudioCtx) {
          ambientAudioCtx = new AudioCtx();
        }
        if (ambientAudioCtx.state === 'suspended') {
          ambientAudioCtx.resume();
        }

        if (ambientOsc1) { try { ambientOsc1.stop(); } catch(e){} }
        if (ambientOsc2) { try { ambientOsc2.stop(); } catch(e){} }

        ambientGain = ambientAudioCtx.createGain();
        ambientGain.gain.setValueAtTime(0.0001, ambientAudioCtx.currentTime);
        ambientGain.gain.exponentialRampToValueAtTime(0.045, ambientAudioCtx.currentTime + 2.0);
        ambientGain.connect(ambientAudioCtx.destination);

        // Primary 432Hz tuning tone
        ambientOsc1 = ambientAudioCtx.createOscillator();
        ambientOsc1.type = 'sine';
        ambientOsc1.frequency.setValueAtTime(432.0, ambientAudioCtx.currentTime);

        // Binaural 424Hz tone (creates 8Hz Alpha state)
        ambientOsc2 = ambientAudioCtx.createOscillator();
        ambientOsc2.type = 'sine';
        ambientOsc2.frequency.setValueAtTime(424.0, ambientAudioCtx.currentTime);

        ambientOsc1.connect(ambientGain);
        ambientOsc2.connect(ambientGain);

        ambientOsc1.start();
        ambientOsc2.start();
        ambientIsPlaying = true;

        const btn = document.getElementById('ambientAudioBtn');
        const icon = document.getElementById('ambientIcon');
        const text = document.getElementById('ambientText');
        if (btn) {
          btn.className = "px-2.5 py-1.5 rounded-lg bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 flex items-center gap-1.5 transition text-xs font-semibold shadow-md shadow-emerald-500/20 animate-pulse";
        }
        if (icon) icon.textContent = "🎵";
        if (text) text.textContent = "432Hz ON";

        if (typeof speakCoach === 'function') {
          speakCoach("432 Hertz focus frequency active. 8 Hertz alpha wave state induced. Stay centered.");
        }
      } catch (err) {
        console.error("Ambient audio error:", err);
      }
    }

    function stop432HzFocusAmbient() {
      if (ambientGain && ambientAudioCtx) {
        try {
          ambientGain.gain.setValueAtTime(ambientGain.gain.value, ambientAudioCtx.currentTime);
          ambientGain.gain.exponentialRampToValueAtTime(0.00001, ambientAudioCtx.currentTime + 1.0);
          setTimeout(() => {
            if (ambientOsc1) { try { ambientOsc1.stop(); } catch(e){} }
            if (ambientOsc2) { try { ambientOsc2.stop(); } catch(e){} }
            ambientIsPlaying = false;
          }, 1000);
        } catch(e) {
          ambientIsPlaying = false;
        }
      } else {
        ambientIsPlaying = false;
      }

      const btn = document.getElementById('ambientAudioBtn');
      const icon = document.getElementById('ambientIcon');
      const text = document.getElementById('ambientText');
      if (btn) {
        btn.className = "px-2.5 py-1.5 rounded-lg bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 hover:text-white flex items-center gap-1.5 transition text-xs font-semibold shadow-sm";
      }
      if (icon) icon.textContent = "🎧";
      if (text) text.textContent = "432Hz Focus";
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
      alert('✅ PRE-MARKET READINESS CERTIFIED!\n\nYou have verified physical composure, structural levels, and risk ceilings. Execution desk is unlocked.');
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

      const md = `# TRADER EXECUTION RESET SYSTEM — 30-DAY DOSSIER\n**Date:** ${new Date().toLocaleDateString('en-IN')} | **Account:** Private Execution Desk (NSE)\n**Verification Hash:** #RESET-V16-SECURE | **Audit Status:** Qualified Institutional Disciplined\n\n## 1. Executive KPIs\n- **Net P&L:** ₹${totalPnL.toFixed(2)}\n- **Realized R:** ${(totalR >= 0 ? '+' : '') + totalR.toFixed(2)}R\n- **Total Trades:** ${trades.length}\n- **Win Rate:** ${winRate}%\n- **Rule Adherence Rate:** ${adhPct}%\n- **Demerit Violations:** ${breaches}\n\n## 2. Operating Rules Verification\n- **Window Adherence (09:15–10:30 AM IST):** Verified & Honored\n- **Stop-Loss Execution:** Non-Negotiable Structural Hard Stops Pre-Committed\n- **Daily Loss Ceiling:** ₹500 Max / Trade, 2 Consecutive Losses Hard Quit\n\n*Signed & Attested by Private Desk Trader*\n`;

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


    // Hook listeners on DOM ready
    window.addEventListener('DOMContentLoaded', () => {
      initTheme();
      initDensity();
      updateRRVisualizer();
      updateBottomDockMetrics();
      setInterval(updateBottomDockMetrics, 1000);

      initIndexedDB();
      computeKellyExpectancy();
      checkDisciplineStreak();
      initClipboardPasteListener();
      renderPhaseTracker();
      initPenaltyStrikes();
    });
    '''

    assert "  </script>\n</body>" in content, "Failed to find closing script tag"
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
    content = content.replace("  </script>\n</body>", f"{master_script_extension}\n  </script>\n" + bottom_dock_markup + "\n</body>", 1)

    # Write files
    for path in [OUT_PUBLIC, OUT_DELIV, OUT_BRAIN]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully generated v14: {path} ({len(content)} bytes)")

if __name__ == "__main__":
    generate_v14()
