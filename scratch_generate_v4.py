with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/public/index.html", "r") as f:
    html = f.read()

# 1. Add hidden file input right after body start
file_input_html = """<body class="min-h-screen pb-16">
  <!-- Hidden File Input for CSV / JSON Bulk Import -->
  <input type="file" id="csvFileInput" accept=".csv,.json,text/csv,application/json" class="hidden" onchange="handleFileImport(event)">"""

html = html.replace('<body class="min-h-screen pb-16">', file_input_html)

# 2. Update the toolbar above Trade History Log Table
old_toolbar = """        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div>
            <h2 class="text-base font-extrabold text-white uppercase tracking-wider flex items-center gap-2">
              <span>📋</span> Trade Execution Journal & History Log
            </h2>
            <p class="text-xs text-slate-400 mt-0.5">Direct 1:1 mapping with `Quick_Log` & `Trade_Log` tabs in Excel.</p>
          </div>
          <div class="flex items-center gap-2">
            <button type="button" onclick="clearExamples()" class="px-3 py-1.5 rounded-lg bg-rose-500/10 hover:bg-rose-500/20 text-rose-400 border border-rose-500/30 text-xs font-bold transition">
              🗑️ Clear Examples
            </button>
            <button type="button" onclick="reloadDefaults()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold transition">
              🔄 Reload Benchmark Seed
            </button>
          </div>
        </div>"""

new_toolbar = """        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div>
            <h2 class="text-base font-extrabold text-white uppercase tracking-wider flex items-center gap-2">
              <span>📋</span> Trade Execution Journal & History Log
            </h2>
            <p class="text-xs text-slate-400 mt-0.5">Direct 1:1 mapping with `Quick_Log` & `Trade_Log` tabs in Excel • Bulk Import & Export enabled.</p>
          </div>
          <div class="flex items-center gap-2 flex-wrap">
            <button type="button" onclick="triggerImport()" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition flex items-center gap-1.5 shadow-sm shadow-emerald-600/30">
              <span>📥</span> Import Trades (CSV)
            </button>
            <button type="button" onclick="downloadSampleTemplate()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-emerald-500/30 text-xs font-bold transition flex items-center gap-1.5">
              <span>📄</span> Sample CSV
            </button>
            <button type="button" onclick="exportTradesCSV()" class="px-3 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold transition flex items-center gap-1.5 shadow-sm shadow-blue-600/30">
              <span>📤</span> Export All (CSV)
            </button>
            <button type="button" onclick="copyAllExcelTSV()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs font-bold transition flex items-center gap-1.5">
              <span>📋</span> Copy TSV
            </button>
            <button type="button" onclick="clearExamples()" class="px-3 py-1.5 rounded-lg bg-rose-500/10 hover:bg-rose-500/20 text-rose-400 border border-rose-500/30 text-xs font-bold transition">
              🗑️ Clear
            </button>
            <button type="button" onclick="reloadDefaults()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold transition">
              🔄 Reset
            </button>
          </div>
        </div>

        <!-- Import Helper Info Capsule -->
        <div class="mt-3 p-3 rounded-xl bg-slate-900/60 border border-slate-800/80 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-[11px] font-mono text-slate-400">
          <div class="flex items-center gap-2">
            <span class="text-blue-400 font-bold">💡 Import Spec:</span>
            <span>Columns supported: <code class="text-slate-300">Symbol, Direction, Entry_Price, Stop_Price, Target_Price, Exit_Price, Qty</code></span>
          </div>
          <span class="text-emerald-400">Auto-computes Planned RR, FYERS charges, Net P&L & Net R if omitted!</span>
        </div>"""

html = html.replace(old_toolbar, new_toolbar)

# 3. Add JS functions for Bulk Import, Sample Download, and Export
js_additions = """    // ==========================================
    // BULK IMPORT & EXPORT SUITE
    // ==========================================
    function triggerImport() {
      document.getElementById('csvFileInput').click();
    }

    function downloadSampleTemplate() {
      const csvContent = "Trade_ID,Date,Time,Symbol,Direction,Entry_Price,Stop_Price,Target_Price,Exit_Price,Qty,Checklist_Score,Rule_Violation,Lesson\\n" +
        "T-001,2026-10-20,09:25,RELIANCE,Long,2500.00,2495.00,2511.00,2511.00,100,5,N,\\\"Patient entry on 9EMA pullback; exit at 2.2R target.\\\"\\n" +
        "T-002,2026-10-20,10:05,TCS,Short,3500.00,3510.00,3478.00,3510.00,50,5,N,\\\"Respected stop loss immediately; entered 30m cooldown.\\\"\\n" +
        "T-003,2026-10-21,09:40,INFY,Long,1450.00,1445.00,1461.00,1461.00,100,5,N,\\\"1m momentum breakout confirmed by 5m trend; target hit.\\\"\\n" +
        "T-004,2026-10-22,09:30,SBIN,Long,780.00,778.00,784.50,784.50,250,5,N,\\\"Clean opening breakout re-test; target 2.25R captured.\\\"\\n" +
        "T-005,2026-10-22,10:15,HDFCBANK,Short,1680.00,1685.00,1668.00,1685.00,100,5,N,\\\"Setup failed normally; respected stop without revenge trading.\\\"\\n";

      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'sample_trades_import.csv';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function exportTradesCSV() {
      if (tradesData.length === 0) {
        alert("No trades available to export.");
        return;
      }
      const headers = [
        "Trade_ID", "Date", "Time", "Symbol", "Direction",
        "Entry_Price", "Stop_Price", "Target_Price", "Exit_Price", "Qty",
        "Planned_RR", "FYERS_Costs", "Net_PnL", "Realized_R", "Outcome",
        "Checklist_Score", "Rule_Violation", "Lesson"
      ];

      const rows = tradesData.map(t => [
        t.id,
        t.date,
        t.time,
        t.symbol,
        t.direction,
        Number(t.entry_price).toFixed(2),
        Number(t.stop_price).toFixed(2),
        Number(t.target_price || (t.entry_price + 2.2 * Math.abs(t.entry_price - t.stop_price))).toFixed(2),
        Number(t.exit_price).toFixed(2),
        t.qty,
        Number(t.rr_planned).toFixed(2),
        Number(t.costs).toFixed(2),
        Number(t.net_pnl).toFixed(2),
        Number(t.r_multiple).toFixed(2),
        t.outcome,
        t.checklist_score,
        t.rule_violation || 'N',
        `"${(t.lesson || '').replace(/"/g, '""')}"`
      ]);

      const csvString = [headers.join(','), ...rows.map(r => r.join(','))].join('\\n');
      const blob = new Blob([csvString], { type: 'text/csv;charset=utf-8;' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      const today = new Date().toISOString().split('T')[0];
      link.download = `trades_export_${today}.csv`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function copyAllExcelTSV() {
      if (tradesData.length === 0) {
        alert("No trades to copy.");
        return;
      }
      const lines = tradesData.map(t => {
        const tgt = t.target_price || (t.entry_price + 2.2 * Math.abs(t.entry_price - t.stop_price));
        return `${t.id}\\t${t.date}\\t${t.time}\\t${t.symbol}\\t${t.direction}\\t${t.entry_price}\\t${t.stop_price}\\t${tgt.toFixed(2)}\\t${t.exit_price}\\t${t.qty}`;
      });
      navigator.clipboard.writeText(lines.join('\\n')).then(() => {
        alert(`📋 Copied all ${tradesData.length} trades in Excel Quick_Log TSV format! Switch to Excel and paste into Column A.`);
      });
    }

    function handleFileImport(e) {
      const file = e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(evt) {
        try {
          const content = evt.target.result;
          if (file.name.endsWith('.json')) {
            const parsed = JSON.parse(content);
            if (Array.isArray(parsed)) {
              applyImportedTrades(parsed);
              return;
            }
          }
          parseCSVAndImport(content);
        } catch(err) {
          alert("Error parsing file: " + err.message);
        } finally {
          e.target.value = '';
        }
      };
      reader.readAsText(file);
    }

    function parseCSVAndImport(csvText) {
      const lines = csvText.split(/\\r\\n|\\n/).filter(line => line.trim() !== '');
      if (lines.length < 2) {
        alert("CSV must contain a header row and at least one trade row.");
        return;
      }

      const rawHeaders = lines[0].split(',').map(h => h.trim().toLowerCase().replace(/['"]/g, ''));
      const findCol = (...names) => {
        for (let name of names) {
          const idx = rawHeaders.indexOf(name.toLowerCase());
          if (idx !== -1) return idx;
        }
        return -1;
      };

      const colId = findCol('trade_id', 'id');
      const colDate = findCol('date');
      const colTime = findCol('time', 'entry_time');
      const colSymbol = findCol('symbol', 'ticker');
      const colDir = findCol('direction', 'side', 'type');
      const colEntry = findCol('entry_price', 'entry', 'buy_price');
      const colStop = findCol('stop_price', 'stop', 'sl');
      const colTarget = findCol('target_price', 'target', 'tgt');
      const colExit = findCol('exit_price', 'exit', 'sell_price');
      const colQty = findCol('qty', 'quantity', 'size');
      const colScore = findCol('checklist_score', 'score');
      const colViol = findCol('rule_violation', 'violation');
      const colLesson = findCol('lesson', 'notes');

      if (colSymbol === -1 || colEntry === -1 || colStop === -1) {
        alert("CSV missing required columns: Symbol, Entry_Price, and Stop_Price are mandatory.");
        return;
      }

      const parsedTrades = [];
      const today = new Date().toISOString().split('T')[0];

      for (let i = 1; i < lines.length; i++) {
        const line = lines[i];
        const cells = [];
        let current = '';
        let inQuotes = false;
        for (let c = 0; c < line.length; c++) {
          const char = line[c];
          if (char === '"') inQuotes = !inQuotes;
          else if (char === ',' && !inQuotes) {
            cells.push(current.trim());
            current = '';
          } else current += char;
        }
        cells.push(current.trim());

        if (cells.length < 3) continue;

        const symbol = (colSymbol !== -1 ? cells[colSymbol] : '').toUpperCase().replace(/['"]/g, '').trim();
        const entry = parseFloat(colEntry !== -1 ? cells[colEntry] : 0);
        const stop = parseFloat(colStop !== -1 ? cells[colStop] : 0);

        if (!symbol || isNaN(entry) || isNaN(stop) || entry === stop) continue;

        const dirRaw = colDir !== -1 ? cells[colDir].toLowerCase() : (entry > stop ? 'long' : 'short');
        const direction = dirRaw.includes('short') || dirRaw === 's' ? 'Short' : 'Long';
        const risk = Math.abs(entry - stop);

        let target = colTarget !== -1 ? parseFloat(cells[colTarget]) : 0;
        if (isNaN(target) || target === 0) {
          target = direction === 'Long' ? (entry + 2.2 * risk) : (entry - 2.2 * risk);
        }

        let exit = colExit !== -1 ? parseFloat(cells[colExit]) : target;
        if (isNaN(exit)) exit = target;

        let qty = colQty !== -1 ? parseInt(cells[colQty]) : 100;
        if (isNaN(qty) || qty <= 0) qty = 100;

        const dateStr = (colDate !== -1 && cells[colDate]) ? cells[colDate].replace(/['"]/g, '') : today;
        const timeStr = (colTime !== -1 && cells[colTime]) ? cells[colTime].replace(/['"]/g, '') : '09:30';
        const score = colScore !== -1 ? parseInt(cells[colScore]) || 5 : 5;
        const viol = colViol !== -1 ? (cells[colViol].toUpperCase().startsWith('Y') ? 'Y' : 'N') : 'N';
        const lesson = colLesson !== -1 ? cells[colLesson].replace(/^"|"$/g, '') : 'Bulk imported trade';

        // Calculations
        const plannedReward = Math.abs(target - entry);
        const plannedRR = Math.round((plannedReward / risk) * 100) / 100;
        const charges = calculateFyersCharges(entry, exit, qty, direction);

        const realizedReward = direction === 'Long' ? (exit - entry) : (entry - exit);
        const grossPnL = Math.round(realizedReward * qty * 100) / 100;
        const netPnL = Math.round((grossPnL - charges.totalCosts) * 100) / 100;
        const totalRisk = risk * qty;
        const netR = totalRisk > 0 ? Math.round((netPnL / totalRisk) * 100) / 100 : 0;
        const outcome = netPnL > 0 ? 'Win' : (netPnL < 0 ? 'Loss' : 'BE');

        const tradeId = (colId !== -1 && cells[colId]) ? cells[colId].replace(/['"]/g, '') : `T-${String(tradesData.length + parsedTrades.length + 1).padStart(3, '0')}`;

        parsedTrades.push({
          id: tradeId,
          date: dateStr,
          time: timeStr,
          symbol: symbol,
          direction: direction,
          entry_price: entry,
          stop_price: stop,
          target_price: target,
          exit_price: exit,
          qty: qty,
          rr_planned: plannedRR,
          costs: charges.totalCosts,
          net_pnl: netPnL,
          r_multiple: netR,
          outcome: outcome,
          checklist_score: score,
          rule_violation: viol,
          lesson: lesson
        });
      }

      if (parsedTrades.length === 0) {
        alert("Could not parse any valid trades from CSV.");
        return;
      }

      applyImportedTrades(parsedTrades);
    }

    function applyImportedTrades(newTradesList) {
      const isAppend = confirm(`Found ${newTradesList.length} valid trades in file.\\n\\nClick 'OK' to APPEND to existing trades.\\nClick 'Cancel' to REPLACE all current trades.`);

      if (isAppend) {
        tradesData.push(...newTradesList);
      } else {
        tradesData = newTradesList;
      }

      renderTradeTable();
      renderTopCapitalHeader();
      renderAnalyticsView();

      // Sync with server if available
      try {
        fetch('/api/trades/bulk', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(tradesData)
        }).catch(() => {});
      } catch(err) {}

      alert(`🎉 Successfully ${isAppend ? 'appended' : 'imported'} ${newTradesList.length} trades! All metrics, charts, and distributions are updated.`);
    }
"""

html = html.replace('function copyExcelRow() {', js_additions + '\n    function copyExcelRow() {')

# Write to all 3 targets
with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/web/public/index.html", "w") as f:
    f.write(html)

with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html", "w") as f:
    f.write(html)

with open("/home/sunny/.gemini/antigravity/brain/85803015-3567-4584-af28-ca9d6eed9423/trader_dashboard.html", "w") as f:
    f.write(html)

print("Updated HTML with Bulk Import, Sample CSV Template Download, and Export features successfully.")
