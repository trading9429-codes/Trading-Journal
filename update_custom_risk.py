"""
Update script to add Custom Risk Amount Option to build_dashboard_v6.py.
"""

with open('/home/sunny/.gemini/antigravity/scratch/trader-reset-system/build_dashboard_v6.py', 'r') as f:
    text = f.read()

# 1. Update HTML calibration strip
old_html = '''          <!-- Position Sizing Calibration Strip -->
          <div class="bg-blue-950/20 border border-blue-500/20 rounded-xl p-3 flex flex-col md:flex-row items-center justify-between gap-3 text-xs">
            <div class="flex items-center gap-2 flex-wrap">
              <span class="text-blue-300 font-bold uppercase text-[10px]">Position Sizer Engine:</span>
              <button type="button" onclick="setRiskMode(0.0025)" id="riskMode_025" class="risk-mode-btn px-2.5 py-1 rounded-lg bg-blue-600 text-white font-bold text-[11px]">0.25% (₹500)</button>
              <button type="button" onclick="setRiskMode(0.0050)" id="riskMode_050" class="risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]">0.50% (₹1,000)</button>
              <span class="text-slate-500">|</span>
              <span class="text-slate-400">Risk Amount:</span>
              <span id="calculatedRiskAmountDisp" class="font-mono font-bold text-white">₹500.00</span>
            </div>'''

new_html = '''          <!-- Position Sizing Calibration Strip with Custom Risk Amount -->
          <div class="bg-blue-950/20 border border-blue-500/20 rounded-xl p-3 flex flex-col md:flex-row items-center justify-between gap-3 text-xs">
            <div class="flex items-center gap-2 flex-wrap">
              <span class="text-blue-300 font-bold uppercase text-[10px]">Position Sizer:</span>
              <button type="button" onclick="setRiskMode(0.0025)" id="riskMode_025" class="risk-mode-btn px-2.5 py-1 rounded-lg bg-blue-600 text-white font-bold text-[11px]">0.25% (₹500)</button>
              <button type="button" onclick="setRiskMode(0.0050)" id="riskMode_050" class="risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]">0.50% (₹1,000)</button>
              <button type="button" onclick="setRiskMode('custom')" id="riskMode_custom" class="risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]">Custom ₹</button>
              
              <!-- Custom Rupee Risk Input -->
              <div id="customRiskContainer" class="hidden items-center gap-1 bg-slate-900 border border-slate-700 rounded-lg px-2 py-0.5">
                <span class="text-slate-400 font-mono text-xs">₹</span>
                <input type="number" id="customRiskInput" step="50" min="50" value="500" oninput="onCustomRiskChange(this.value)" class="w-20 bg-transparent text-white font-mono text-xs font-bold focus:outline-none" placeholder="Risk ₹">
              </div>

              <span class="text-slate-500">|</span>
              <span class="text-slate-400">Risk Capital:</span>
              <span id="calculatedRiskAmountDisp" class="font-mono font-bold text-white">₹500.00</span>
              <span id="riskPctBadge" class="text-[10px] text-blue-400 font-mono">(0.25%)</span>
            </div>'''

assert old_html in text, "old_html not found"
text = text.replace(old_html, new_html)

# 2. Update state variables
old_state = '''    let pendingFyersTrades = [];
    let riskModePercent = 0.0025;
    let isIndisciplineSimActive = false;'''

new_state = '''    let pendingFyersTrades = [];
    let riskModeType = 'percent'; // 'percent' or 'custom'
    let riskModePercent = 0.0025;
    let customRiskAmount = 500;
    let isIndisciplineSimActive = false;'''

assert old_state in text, "old_state not found"
text = text.replace(old_state, new_state)

# 3. Update setRiskMode and autoApplyPositionSize
old_sizer_fn = '''    // --- 1-Click Position Sizing Engine ---
    function setRiskMode(pct) {
      riskModePercent = pct;
      const btn025 = document.getElementById('riskMode_025');
      const btn050 = document.getElementById('riskMode_050');

      if (pct === 0.0025) {
        btn025.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-blue-600 text-white font-bold text-[11px]';
        btn050.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
      } else {
        btn050.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-blue-600 text-white font-bold text-[11px]';
        btn025.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
      }
      recalculateCalculators();
    }

    function autoApplyPositionSize() {
      const entry = parseFloat(document.getElementById('entry_price').value) || 0;
      const stop = parseFloat(document.getElementById('stop_price').value) || 0;
      if (entry <= 0 || stop <= 0) {
        alert("Enter Entry Price and Stop Loss first to calculate position size.");
        return;
      }
      const riskPerShare = Math.abs(entry - stop);
      if (riskPerShare <= 0) return;

      const riskAmt = startingCapital * riskModePercent;
      const maxShares = Math.max(1, Math.floor(riskAmt / riskPerShare));
      document.getElementById('qty').value = maxShares;
      recalculateCalculators();
    }'''

new_sizer_fn = '''    // --- 1-Click Position Sizing Engine with Custom Risk Support ---
    function setRiskMode(mode) {
      const btn025 = document.getElementById('riskMode_025');
      const btn050 = document.getElementById('riskMode_050');
      const btnCust = document.getElementById('riskMode_custom');
      const custContainer = document.getElementById('customRiskContainer');

      if (mode === 0.0025) {
        riskModeType = 'percent';
        riskModePercent = 0.0025;
        btn025.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-blue-600 text-white font-bold text-[11px]';
        btn050.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
        btnCust.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
        custContainer.classList.add('hidden');
        custContainer.classList.remove('flex');
      } else if (mode === 0.0050) {
        riskModeType = 'percent';
        riskModePercent = 0.0050;
        btn050.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-blue-600 text-white font-bold text-[11px]';
        btn025.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
        btnCust.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
        custContainer.classList.add('hidden');
        custContainer.classList.remove('flex');
      } else if (mode === 'custom') {
        riskModeType = 'custom';
        btnCust.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-blue-600 text-white font-bold text-[11px]';
        btn025.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
        btn050.className = 'risk-mode-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-[11px]';
        custContainer.classList.remove('hidden');
        custContainer.classList.add('flex');
        const inputVal = parseFloat(document.getElementById('customRiskInput').value);
        if (inputVal > 0) customRiskAmount = inputVal;
      }
      recalculateCalculators();
    }

    function onCustomRiskChange(val) {
      const num = parseFloat(val);
      if (num > 0) {
        customRiskAmount = num;
        recalculateCalculators();
      }
    }

    function autoApplyPositionSize() {
      const entry = parseFloat(document.getElementById('entry_price').value) || 0;
      const stop = parseFloat(document.getElementById('stop_price').value) || 0;
      if (entry <= 0 || stop <= 0) {
        alert("Enter Entry Price and Stop Loss first to calculate position size.");
        return;
      }
      const riskPerShare = Math.abs(entry - stop);
      if (riskPerShare <= 0) return;

      const riskAmt = riskModeType === 'custom' ? customRiskAmount : (startingCapital * riskModePercent);
      const maxShares = Math.max(1, Math.floor(riskAmt / riskPerShare));
      document.getElementById('qty').value = maxShares;
      recalculateCalculators();
    }'''

assert old_sizer_fn in text, "old_sizer_fn not found"
text = text.replace(old_sizer_fn, new_sizer_fn)

# 4. Update recalculateCalculators
old_recalc_risk = '''      const riskAmt = startingCapital * riskModePercent;
      document.getElementById('calculatedRiskAmountDisp').textContent = `₹${riskAmt.toFixed(2)}`;'''

new_recalc_risk = '''      const riskAmt = riskModeType === 'custom' ? customRiskAmount : (startingCapital * riskModePercent);
      document.getElementById('calculatedRiskAmountDisp').textContent = `₹${riskAmt.toFixed(2)}`;
      const effPct = startingCapital > 0 ? ((riskAmt / startingCapital) * 100).toFixed(2) : '0.00';
      const pctBadge = document.getElementById('riskPctBadge');
      if (pctBadge) pctBadge.textContent = `(${effPct}%)`;'''

assert old_recalc_risk in text, "old_recalc_risk not found"
text = text.replace(old_recalc_risk, new_recalc_risk)

# 5. Update renderTopCapitalHeader to update button rupee amounts dynamically
old_cap_fn = '''    function renderTopCapitalHeader() {
      document.getElementById('headerStartingCapDisplay').textContent = `₹${startingCapital.toLocaleString('en-IN')}`;
      const totalNetPnL = tradesData.reduce((acc, t) => acc + (parseFloat(t.net_pnl) || 0), 0);
      const currentCap = startingCapital + totalNetPnL;
      const curDisp = document.getElementById('headerCurrentCapDisplay');
      curDisp.textContent = `₹${Math.round(currentCap).toLocaleString('en-IN')}`;
      if (totalNetPnL >= 0) {
        curDisp.className = 'font-bold font-mono text-emerald-400';
      } else {
        curDisp.className = 'font-bold font-mono text-rose-400';
      }
    }'''

new_cap_fn = '''    function renderTopCapitalHeader() {
      document.getElementById('headerStartingCapDisplay').textContent = `₹${startingCapital.toLocaleString('en-IN')}`;
      const totalNetPnL = tradesData.reduce((acc, t) => acc + (parseFloat(t.net_pnl) || 0), 0);
      const currentCap = startingCapital + totalNetPnL;
      const curDisp = document.getElementById('headerCurrentCapDisplay');
      curDisp.textContent = `₹${Math.round(currentCap).toLocaleString('en-IN')}`;
      if (totalNetPnL >= 0) {
        curDisp.className = 'font-bold font-mono text-emerald-400';
      } else {
        curDisp.className = 'font-bold font-mono text-rose-400';
      }

      // Update button quick risk rupee amounts
      const btn025 = document.getElementById('riskMode_025');
      const btn050 = document.getElementById('riskMode_050');
      if (btn025) btn025.textContent = `0.25% (₹${Math.round(startingCapital * 0.0025).toLocaleString('en-IN')})`;
      if (btn050) btn050.textContent = `0.50% (₹${Math.round(startingCapital * 0.0050).toLocaleString('en-IN')})`;
    }'''

assert old_cap_fn in text, "old_cap_fn not found"
text = text.replace(old_cap_fn, new_cap_fn)

# 6. Update submitTrade risk_percent assignment
old_submit_risk = '''        risk_percent: riskModePercent,
        risk_amount: totalRisk,'''

new_submit_risk = '''        risk_percent: parseFloat((totalRisk / startingCapital).toFixed(4)),
        risk_amount: totalRisk,'''

assert old_submit_risk in text, "old_submit_risk not found"
text = text.replace(old_submit_risk, new_submit_risk)

with open('/home/sunny/.gemini/antigravity/scratch/trader-reset-system/build_dashboard_v6.py', 'w') as f:
    f.write(text)

print("build_dashboard_v6.py successfully updated with Custom Risk Amount option.")
