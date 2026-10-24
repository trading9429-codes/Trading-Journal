import re

with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/build_v2_system.py", "r") as f:
    code = f.read()

# 1. Update Dashboard
code = code.replace(
    '{"ref": "B2", "val": "NSE Equities 1m | Window: 09:15–10:30 AM IST | Risk: 0.25%–0.50% | Min RR: 2.2 | Friction: 0.11% Turnover", "s": 11}',
    '{"ref": "B2", "val": "NSE Equities 1m | Window: 09:15–10:30 AM IST | Risk: 0.25%–0.50% | Min RR: ≥ 2.2 | FYERS Brokerage & Taxes", "s": 11}'
)
code = code.replace(
    '{"ref": "F5", "f": "SUM(Trade_Log!U2:U50)", "val": 443.03, "s": 14}',
    '{"ref": "F5", "f": "SUM(Trade_Log!U2:U50)", "val": 1358.05, "s": 14}'
)
code = code.replace(
    '{"ref": "F6", "val": "Net of 0.11% Turnover Friction & Taxes", "s": 16}',
    '{"ref": "F6", "val": "Net of FYERS Brokerage & Statutory Taxes (STT, GST, Exch, SEBI, Stamp)", "s": 16}'
)
code = code.replace(
    '{"ref": "B9", "f": \'IFERROR(AVERAGE(Trade_Log!V2:V50),0)\', "val": 0.30, "s": 18}',
    '{"ref": "B9", "f": \'IFERROR(AVERAGE(Trade_Log!V2:V50),0)\', "val": 0.90, "s": 18}'
)
code = code.replace(
    '{"ref": "F24", "f": "Weekly_Review!G2", "val": 443.03, "s": 4}',
    '{"ref": "F24", "f": "Weekly_Review!G2", "val": 1358.05, "s": 4}'
)
code = code.replace(
    '{"ref": "G24", "f": "Weekly_Review!I2", "val": 0.30, "s": 19}',
    '{"ref": "G24", "f": "Weekly_Review!I2", "val": 0.90, "s": 19}'
)

# 2. Update Quick Log
old_quick_section = """# ==========================================
# 1. QUICK_LOG TAB (Effortless 6-Field Entry)
# ==========================================
quick_headers = [
    "Trade_ID","Date","Time","Symbol","Direction","Entry_Price","Stop_Price","Exit_Price","Qty",
    "Target_RR","Friction_0.11%","Net_PnL","Net_R","Outcome","Valid_5of5"
]

quick_widths = {
    1: 16, 2: 13, 3: 11, 4: 12, 5: 11, 6: 13, 7: 13, 8: 13, 9: 10,
    10: 13, 11: 14, 12: 14, 13: 12, 14: 11, 15: 14
}

# Style map for headers: Cols 2..9 are Action Blue (24), others are Dark Navy (1)
quick_header_map = {
    1: 1, 2: 24, 3: 24, 4: 24, 5: 24, 6: 24, 7: 24, 8: 24, 9: 24,
    10: 25, 11: 25, 12: 25, 13: 25, 14: 25, 15: 25
}

quick_custom_top = {
    1: {
        "height": 30,
        "cells": [
            {"ref": "A1", "val": "⚡ QUICK LOG: Fill ONLY the Blue Columns (B to I). All calculations, friction & R-multiples are 100% automated!", "s": 17}
        ]
    }
}

quick_rows = []
# Seed 1
quick_rows.append([
    {"val": "T-001 [EXAMPLE]", "s": 5},
    {"val": "2026-10-20", "s": 26},
    {"val": "09:25", "s": 26},
    {"val": "RELIANCE", "s": 26},
    {"val": "Long", "s": 26},
    {"val": 2500.0, "s": 27},
    {"val": 2495.0, "s": 27},
    {"val": 2511.0, "s": 27},
    {"val": 100, "s": 26},
    {"f": 'IF(OR(F3="",G3=""),"",ROUND(ABS(H3-F3)/ABS(F3-G3),2))', "val": 2.20, "s": 6},
    {"f": 'IF(OR(F3="",H3="",I3=""),"",ROUND(0.0011*(F3*I3+H3*I3),2))', "val": 551.21, "s": 4},
    {"f": 'IF(OR(F3="",H3="",I3=""),"",IF(E3="Long",(H3-F3)*I3,(F3-H3)*I3)-K3)', "val": 548.79, "s": 4},
    {"f": 'IF(OR(F3="",G3="",I3="",L3=""),"",ROUND(L3/(ABS(F3-G3)*I3),2))', "val": 1.10, "s": 19},
    {"f": 'IF(L3="","",IF(L3>0,"Win",IF(L3<0,"Loss","BE")))', "val": "Win", "s": 5},
    {"f": 'IF(J3="","",IF(J3>=2.2,"Y (5/5)","N (<2.2R)"))', "val": "Y (5/5)", "s": 5}
])

# Seed 2
quick_rows.append([
    {"val": "T-002 [EXAMPLE]", "s": 5},
    {"val": "2026-10-20", "s": 26},
    {"val": "10:05", "s": 26},
    {"val": "TCS", "s": 26},
    {"val": "Short", "s": 26},
    {"val": 3500.0, "s": 27},
    {"val": 3510.0, "s": 27},
    {"val": 3510.0, "s": 27},
    {"val": 50, "s": 26},
    {"f": 'IF(OR(F4="",G4=""),"",ROUND(ABS(H4-F4)/ABS(F4-G4),2))', "val": 2.20, "s": 6},
    {"f": 'IF(OR(F4="",H4="",I4=""),"",ROUND(0.0011*(F4*I4+H4*I4),2))', "val": 385.55, "s": 4},
    {"f": 'IF(OR(F4="",H4="",I4=""),"",IF(E4="Long",(H4-F4)*I4,(F4-H4)*I4)-K4)', "val": -885.55, "s": 4},
    {"f": 'IF(OR(F4="",G4="",I4="",L4=""),"",ROUND(L4/(ABS(F4-G4)*I4),2))', "val": -1.77, "s": 19},
    {"f": 'IF(L4="","",IF(L4>0,"Win",IF(L4<0,"Loss","BE")))', "val": "Loss", "s": 5},
    {"f": 'IF(J4="","",IF(J4>=2.2,"Y (5/5)","N (<2.2R)"))', "val": "Y (5/5)", "s": 5}
])

# Seed 3
quick_rows.append([
    {"val": "T-003 [EXAMPLE]", "s": 5},
    {"val": "2026-10-21", "s": 26},
    {"val": "09:40", "s": 26},
    {"val": "INFY", "s": 26},
    {"val": "Long", "s": 26},
    {"val": 1450.0, "s": 27},
    {"val": 1445.0, "s": 27},
    {"val": 1461.0, "s": 27},
    {"val": 100, "s": 26},
    {"f": 'IF(OR(F5="",G5=""),"",ROUND(ABS(H5-F5)/ABS(F5-G5),2))', "val": 2.20, "s": 6},
    {"f": 'IF(OR(F5="",H5="",I5=""),"",ROUND(0.0011*(F5*I5+H5*I5),2))', "val": 320.21, "s": 4},
    {"f": 'IF(OR(F5="",H5="",I5=""),"",IF(E5="Long",(H5-F5)*I5,(F5-H5)*I5)-K5)', "val": 779.79, "s": 4},
    {"f": 'IF(OR(F5="",G5="",I5="",L5=""),"",ROUND(L5/(ABS(F5-G5)*I5),2))', "val": 1.56, "s": 19},
    {"f": 'IF(L5="","",IF(L5>0,"Win",IF(L5<0,"Loss","BE")))', "val": "Win", "s": 5},
    {"f": 'IF(J5="","",IF(J5>=2.2,"Y (5/5)","N (<2.2R)"))', "val": "Y (5/5)", "s": 5}
])

# Pre-populate empty rows 6..50 with formulas
for r in range(6, 51):
    quick_rows.append([
        {"val": f"T-{r-2:03d}", "s": 5},
        {"val": "", "s": 26},
        {"val": "", "s": 26},
        {"val": "", "s": 26},
        {"val": "", "s": 26},
        {"val": "", "s": 27},
        {"val": "", "s": 27},
        {"val": "", "s": 27},
        {"val": "", "s": 26},
        {"f": f'IF(OR(F{r}="",G{r}=""),"",ROUND(ABS(H{r}-F{r})/ABS(F{r}-G{r}),2))', "val": "", "s": 6},
        {"f": f'IF(OR(F{r}="",H{r}="",I{r}=""),"",ROUND(0.0011*(F{r}*I{r}+H{r}*I{r}),2))', "val": "", "s": 4},
        {"f": f'IF(OR(F{r}="",H{r}="",I{r}=""),"",IF(E{r}="Long",(H{r}-F{r})*I{r},(F{r}-H{r})*I{r})-K{r})', "val": "", "s": 4},
        {"f": f'IF(OR(F{r}="",G{r}="",I{r}="",L{r}=""),"",ROUND(L{r}/(ABS(F{r}-G{r})*I{r}),2))', "val": "", "s": 19},
        {"f": f'IF(L{r}="","",IF(L{r}>0,"Win",IF(L{r}<0,"Loss","BE")))', "val": "", "s": 5},
        {"f": f'IF(J{r}="","",IF(J{r}>=2.2,"Y (5/5)","N (<2.2R)"))', "val": "", "s": 5}
    ])

quick_dv_xml = \"\"\"<dataValidations count="1">
  <dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1" sqref="E3:E50">
    <formula1>&quot;Long,Short&quot;</formula1>
  </dataValidation>
</dataValidations>\"\"\"

quick_cf_xml = \"\"\"<conditionalFormatting sqref="N3:N50">
  <cfRule type="cellIs" dxfId="0" priority="1" operator="equal">
    <formula>&quot;Loss&quot;</formula>
  </cfRule>
  <cfRule type="cellIs" dxfId="1" priority="2" operator="equal">
    <formula>&quot;Win&quot;</formula>
  </cfRule>
</conditionalFormatting>\"\"\""""

new_quick_section = """# ==========================================
# 1. QUICK_LOG TAB (Effortless 7-Field Fast Entry)
# ==========================================
quick_headers = [
    "Trade_ID","Date","Time","Symbol","Direction","Entry_Price","Stop_Price","Target_Price","Exit_Price","Qty",
    "Planned_RR","FYERS_Costs","Net_PnL","Net_R","Outcome","Valid_5of5"
]

quick_widths = {
    1: 16, 2: 13, 3: 11, 4: 12, 5: 11, 6: 13, 7: 13, 8: 13, 9: 13, 10: 10,
    11: 13, 12: 14, 13: 14, 14: 12, 15: 11, 16: 14
}

# Style map for headers: Cols 2..10 are Action Blue (24), others are Dark Navy (1) / Slate (25)
quick_header_map = {
    1: 1, 2: 24, 3: 24, 4: 24, 5: 24, 6: 24, 7: 24, 8: 24, 9: 24, 10: 24,
    11: 25, 12: 25, 13: 25, 14: 25, 15: 25, 16: 25
}

quick_custom_top = {
    1: {
        "height": 30,
        "cells": [
            {"ref": "A1", "val": "⚡ QUICK LOG: Fill ONLY the Blue Columns (B to J). All calculations, FYERS statutory charges & R-multiples are 100% automated!", "s": 17}
        ]
    }
}

quick_rows = []
# Seed 1
quick_rows.append([
    {"val": "T-001 [EXAMPLE]", "s": 5},
    {"val": "2026-10-20", "s": 26},
    {"val": "09:25", "s": 26},
    {"val": "RELIANCE", "s": 26},
    {"val": "Long", "s": 26},
    {"val": 2500.0, "s": 27},
    {"val": 2495.0, "s": 27},
    {"val": 2511.0, "s": 27},
    {"val": 2511.0, "s": 27},
    {"val": 100, "s": 26},
    {"f": 'IF(OR(F3="",G3="",H3=""),"",ROUND(ABS(H3-F3)/ABS(F3-G3),2))', "val": 2.20, "s": 6},
    {"f": 'IF(OR(F3="",I3="",J3=""),"",ROUND((MIN(IF(E3="Long",F3*J3,I3*J3)*0.0003,20)+MIN(IF(E3="Long",I3*J3,F3*J3)*0.0003,20))*1.18+IF(E3="Long",I3*J3,F3*J3)*0.00025+IF(E3="Long",F3*J3,I3*J3)*0.00003+(F3+I3)*J3*0.000035164,2))', "val": 135.10, "s": 4},
    {"f": 'IF(OR(F3="",I3="",J3=""),"",IF(E3="Long",(I3-F3)*J3,(F3-I3)*J3)-L3)', "val": 964.90, "s": 4},
    {"f": 'IF(OR(F3="",G3="",J3="",M3=""),"",ROUND(M3/(ABS(F3-G3)*J3),2))', "val": 1.93, "s": 19},
    {"f": 'IF(M3="","",IF(M3>0,"Win",IF(M3<0,"Loss","BE")))', "val": "Win", "s": 5},
    {"f": 'IF(K3="","",IF(K3>=2.2,"Y (5/5)","N (<2.2R)"))', "val": "Y (5/5)", "s": 5}
])

# Seed 2
quick_rows.append([
    {"val": "T-002 [EXAMPLE]", "s": 5},
    {"val": "2026-10-20", "s": 26},
    {"val": "10:05", "s": 26},
    {"val": "TCS", "s": 26},
    {"val": "Short", "s": 26},
    {"val": 3500.0, "s": 27},
    {"val": 3510.0, "s": 27},
    {"val": 3478.0, "s": 27},
    {"val": 3510.0, "s": 27},
    {"val": 50, "s": 26},
    {"f": 'IF(OR(F4="",G4="",H4=""),"",ROUND(ABS(H4-F4)/ABS(F4-G4),2))', "val": 2.20, "s": 6},
    {"f": 'IF(OR(F4="",I4="",J4=""),"",ROUND((MIN(IF(E4="Long",F4*J4,I4*J4)*0.0003,20)+MIN(IF(E4="Long",I4*J4,F4*J4)*0.0003,20))*1.18+IF(E4="Long",I4*J4,F4*J4)*0.00025+IF(E4="Long",F4*J4,I4*J4)*0.00003+(F4+I4)*J4*0.000035164,2))', "val": 108.54, "s": 4},
    {"f": 'IF(OR(F4="",I4="",J4=""),"",IF(E4="Long",(I4-F4)*J4,(F4-I4)*J4)-L4)', "val": -608.54, "s": 4},
    {"f": 'IF(OR(F4="",G4="",J4="",M4=""),"",ROUND(M4/(ABS(F4-G4)*J4),2))', "val": -1.22, "s": 19},
    {"f": 'IF(M4="","",IF(M4>0,"Win",IF(M4<0,"Loss","BE")))', "val": "Loss", "s": 5},
    {"f": 'IF(K4="","",IF(K4>=2.2,"Y (5/5)","N (<2.2R)"))', "val": "Y (5/5)", "s": 5}
])

# Seed 3
quick_rows.append([
    {"val": "T-003 [EXAMPLE]", "s": 5},
    {"val": "2026-10-21", "s": 26},
    {"val": "09:40", "s": 26},
    {"val": "INFY", "s": 26},
    {"val": "Long", "s": 26},
    {"val": 1450.0, "s": 27},
    {"val": 1445.0, "s": 27},
    {"val": 1461.0, "s": 27},
    {"val": 1461.0, "s": 27},
    {"val": 100, "s": 26},
    {"f": 'IF(OR(F5="",G5="",H5=""),"",ROUND(ABS(H5-F5)/ABS(F5-G5),2))', "val": 2.20, "s": 6},
    {"f": 'IF(OR(F5="",I5="",J5=""),"",ROUND((MIN(IF(E5="Long",F5*J5,I5*J5)*0.0003,20)+MIN(IF(E5="Long",I5*J5,F5*J5)*0.0003,20))*1.18+IF(E5="Long",I5*J5,F5*J5)*0.00025+IF(E5="Long",F5*J5,I5*J5)*0.00003+(F5+I5)*J5*0.000035164,2))', "val": 98.31, "s": 4},
    {"f": 'IF(OR(F5="",I5="",J5=""),"",IF(E5="Long",(I5-F5)*J5,(F5-I5)*J5)-L5)', "val": 1001.69, "s": 4},
    {"f": 'IF(OR(F5="",G5="",J5="",M5=""),"",ROUND(M5/(ABS(F5-G5)*J5),2))', "val": 2.00, "s": 19},
    {"f": 'IF(M5="","",IF(M5>0,"Win",IF(M5<0,"Loss","BE")))', "val": "Win", "s": 5},
    {"f": 'IF(K5="","",IF(K5>=2.2,"Y (5/5)","N (<2.2R)"))', "val": "Y (5/5)", "s": 5}
])

# Pre-populate empty rows 6..50 with formulas
for r in range(6, 51):
    quick_rows.append([
        {"val": f"T-{r-2:03d}", "s": 5},
        {"val": "", "s": 26},
        {"val": "", "s": 26},
        {"val": "", "s": 26},
        {"val": "", "s": 26},
        {"val": "", "s": 27},
        {"val": "", "s": 27},
        {"val": "", "s": 27},
        {"val": "", "s": 27},
        {"val": "", "s": 26},
        {"f": f'IF(OR(F{r}="",G{r}="",H{r}=""),"",ROUND(ABS(H{r}-F{r})/ABS(F{r}-G{r}),2))', "val": "", "s": 6},
        {"f": f'IF(OR(F{r}="",I{r}="",J{r}=""),"",ROUND((MIN(IF(E{r}="Long",F{r}*J{r},I{r}*J{r})*0.0003,20)+MIN(IF(E{r}="Long",I{r}*J{r},F{r}*J{r})*0.0003,20))*1.18+IF(E{r}="Long",I{r}*J{r},F{r}*J{r})*0.00025+IF(E{r}="Long",F{r}*J{r},I{r}*J{r})*0.00003+(F{r}+I{r})*J{r}*0.000035164,2))', "val": "", "s": 4},
        {"f": f'IF(OR(F{r}="",I{r}="",J{r}=""),"",IF(E{r}="Long",(I{r}-F{r})*J{r},(F{r}-I{r})*J{r})-L{r})', "val": "", "s": 4},
        {"f": f'IF(OR(F{r}="",G{r}="",J{r}="",M{r}=""),"",ROUND(M{r}/(ABS(F{r}-G{r})*J{r}),2))', "val": "", "s": 19},
        {"f": f'IF(M{r}="","",IF(M{r}>0,"Win",IF(M{r}<0,"Loss","BE")))', "val": "", "s": 5},
        {"f": f'IF(K{r}="","",IF(K{r}>=2.2,"Y (5/5)","N (<2.2R)"))', "val": "", "s": 5}
    ])

quick_dv_xml = \"\"\"<dataValidations count="1">
  <dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1" sqref="E3:E50">
    <formula1>&quot;Long,Short&quot;</formula1>
  </dataValidation>
</dataValidations>\"\"\"

quick_cf_xml = \"\"\"<conditionalFormatting sqref="O3:O50">
  <cfRule type="cellIs" dxfId="0" priority="1" operator="equal">
    <formula>&quot;Loss&quot;</formula>
  </cfRule>
  <cfRule type="cellIs" dxfId="1" priority="2" operator="equal">
    <formula>&quot;Win&quot;</formula>
  </cfRule>
</conditionalFormatting>\"\"\""""

if old_quick_section in code:
    code = code.replace(old_quick_section, new_quick_section)
    print("Replaced quick section successfully.")
else:
    print("Warning: old_quick_section not matched exactly!")

# 3. Update Trade_Log Tab Costs & Net PnL
code = code.replace(
    '{"f": \'IF(OR(O2="",Q2="",R2=""),"",ROUND(0.0011*(O2*R2+Q2*R2),2))\', "val": 551.21, "s": 4},\n    {"f": \'IF(S2="","",S2-T2)\', "val": 548.79, "s": 4},\n    {"f": \'IF(OR(N2="",N2=0,U2=""),"",U2/N2)\', "val": 1.10, "s": 6},',
    '{"f": \'IF(OR(O2="",Q2="",R2=""),"",ROUND((MIN(IF(F2="Long",O2*R2,Q2*R2)*0.0003,20)+MIN(IF(F2="Long",Q2*R2,O2*R2)*0.0003,20))*1.18+IF(F2="Long",Q2*R2,O2*R2)*0.00025+IF(F2="Long",O2*R2,Q2*R2)*0.00003+(O2+Q2)*R2*0.000035164,2))\', "val": 135.10, "s": 4},\n    {"f": \'IF(S2="","",S2-T2)\', "val": 964.90, "s": 4},\n    {"f": \'IF(OR(N2="",N2=0,U2=""),"",U2/N2)\', "val": 1.93, "s": 6},'
)

code = code.replace(
    '{"f": \'IF(OR(O3="",Q3="",R3=""),"",ROUND(0.0011*(O3*R3+Q3*R3),2))\', "val": 385.55, "s": 4},\n    {"f": \'IF(S3="","",S3-T3)\', "val": -885.55, "s": 4},\n    {"f": \'IF(OR(N3="",N3=0,U3=""),"",U3/N3)\', "val": -1.77, "s": 6},',
    '{"f": \'IF(OR(O3="",Q3="",R3=""),"",ROUND((MIN(IF(F3="Long",O3*R3,Q3*R3)*0.0003,20)+MIN(IF(F3="Long",Q3*R3,O3*R3)*0.0003,20))*1.18+IF(F3="Long",Q3*R3,O3*R3)*0.00025+IF(F3="Long",O3*R3,Q3*R3)*0.00003+(O3+Q3)*R3*0.000035164,2))\', "val": 108.54, "s": 4},\n    {"f": \'IF(S3="","",S3-T3)\', "val": -608.54, "s": 4},\n    {"f": \'IF(OR(N3="",N3=0,U3=""),"",U3/N3)\', "val": -1.22, "s": 6},'
)

code = code.replace(
    '{"f": \'IF(OR(O4="",Q4="",R4=""),"",ROUND(0.0011*(O4*R4+Q4*R4),2))\', "val": 320.21, "s": 4},\n    {"f": \'IF(S4="","",S4-T4)\', "val": 779.79, "s": 4},\n    {"f": \'IF(OR(N4="",N4=0,U4=""),"",U4/N4)\', "val": 1.56, "s": 6},',
    '{"f": \'IF(OR(O4="",Q4="",R4=""),"",ROUND((MIN(IF(F4="Long",O4*R4,Q4*R4)*0.0003,20)+MIN(IF(F4="Long",Q4*R4,O4*R4)*0.0003,20))*1.18+IF(F4="Long",Q4*R4,O4*R4)*0.00025+IF(F4="Long",O4*R4,Q4*R4)*0.00003+(O4+Q4)*R4*0.000035164,2))\', "val": 98.31, "s": 4},\n    {"f": \'IF(S4="","",S4-T4)\', "val": 1001.69, "s": 4},\n    {"f": \'IF(OR(N4="",N4=0,U4=""),"",U4/N4)\', "val": 2.00, "s": 6},'
)

code = code.replace(
    '{"f": f\'IF(OR(O{r}="",Q{r}="",R{r}=""),"",ROUND(0.0011*(O{r}*R{r}+Q{r}*R{r}),2))\', "val": "", "s": s_curr},',
    '{"f": f\'IF(OR(O{r}="",Q{r}="",R{r}=""),"",ROUND((MIN(IF(F{r}="Long",O{r}*R{r},Q{r}*R{r})*0.0003,20)+MIN(IF(F{r}="Long",Q{r}*R{r},O{r}*R{r})*0.0003,20))*1.18+IF(F{r}="Long",Q{r}*R{r},O{r}*R{r})*0.00025+IF(F{r}="Long",O{r}*R{r},Q{r}*R{r})*0.00003+(O{r}+Q{r})*R{r}*0.000035164,2))\', "val": "", "s": s_curr},'
)

# 4. Update Daily Scorecard seed rows
code = code.replace(
    '{"f": \'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,$A2)\', "val": -336.76, "s": 4},\n    {"f": \'SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,$A2)\', "val": -0.67, "s": 6},',
    '{"f": \'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,$A2)\', "val": 356.36, "s": 4},\n    {"f": \'SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,$A2)\', "val": 0.71, "s": 6},'
)
code = code.replace(
    '{"f": \'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,$A3)\', "val": 779.79, "s": 4},\n    {"f": \'SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,$A3)\', "val": 1.56, "s": 6},',
    '{"f": \'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,$A3)\', "val": 1001.69, "s": 4},\n    {"f": \'SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,$A3)\', "val": 2.00, "s": 6},'
)

# 5. Update Weekly Review seed row
code = code.replace(
    '{"f": \'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2)\', "val": 443.03, "s": 4},\n    {"f": \'IFERROR(AVERAGEIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2),"")\', "val": 0.30, "s": 6},\n    {"f": \'IF(C2=0,"",SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2)/C2)\', "val": 0.30, "s": 6},',
    '{"f": \'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2)\', "val": 1358.05, "s": 4},\n    {"f": \'IFERROR(AVERAGEIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2),"")\', "val": 0.90, "s": 6},\n    {"f": \'IF(C2=0,"",SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2)/C2)\', "val": 0.90, "s": 6},'
)

with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/build_v2_system.py", "w") as f:
    f.write(code)

print("Updated build_v2_system.py successfully.")
