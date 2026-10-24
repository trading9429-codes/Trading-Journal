import zipfile
import html
import os
import subprocess

def col_letter(col_idx):
    result = ""
    while col_idx > 0:
        col_idx, remainder = divmod(col_idx - 1, 26)
        result = chr(65 + remainder) + result
    return result

def escape_xml(s):
    if s is None:
        return ""
    return html.escape(str(s))

def make_cell(ref, val=None, formula=None, style_id=None, cell_type=None):
    s_attr = f' s="{style_id}"' if style_id is not None else ""
    if formula is not None:
        f_xml = f'<f>{escape_xml(formula)}</f>'
        if cell_type == "str" or (cell_type is None and isinstance(val, str)):
            v_xml = f'<v>{escape_xml(val)}</v>' if val is not None else '<v></v>'
            return f'<c r="{ref}"{s_attr} t="str">{f_xml}{v_xml}</c>'
        else:
            v_xml = f'<v>{escape_xml(val)}</v>' if val is not None else '<v></v>'
            return f'<c r="{ref}"{s_attr}>{f_xml}{v_xml}</c>'
    elif val is None or val == "":
        return f'<c r="{ref}"{s_attr}/>'
    elif cell_type == "s" or isinstance(val, str):
        return f'<c r="{ref}"{s_attr} t="inlineStr"><is><t>{escape_xml(val)}</t></is></c>'
    elif isinstance(val, (int, float)):
        return f'<c r="{ref}"{s_attr}><v>{val}</v></c>'
    else:
        return f'<c r="{ref}"{s_attr} t="inlineStr"><is><t>{escape_xml(str(val))}</t></is></c>'

styles_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <numFmts count="4">
    <numFmt numFmtId="164" formatCode="yyyy-mm-dd"/>
    <numFmt numFmtId="165" formatCode="0.0%"/>
    <numFmt numFmtId="166" formatCode="#,##0.00"/>
    <numFmt numFmtId="167" formatCode="0.00"/>
  </numFmts>
  <fonts count="6">
    <font><sz val="11"/><name val="Calibri"/><color theme="1"/></font>
    <font><b/><sz val="11"/><name val="Calibri"/><color rgb="FFFFFFFF"/></font>
    <font><b/><sz val="11"/><name val="Calibri"/><color theme="1"/></font>
    <font><b/><sz val="11"/><name val="Calibri"/><color rgb="FF9C0006"/></font>
    <font><b/><sz val="11"/><name val="Calibri"/><color rgb="FF006100"/></font>
    <font><b/><sz val="11"/><name val="Calibri"/><color rgb="FF9C6500"/></font>
  </fonts>
  <fills count="7">
    <fill><patternFill fillType="none"/></fill>
    <fill><patternFill fillType="gray125"/></fill>
    <fill><patternFill fillType="solid"><fgColor rgb="FF1F497D"/><bgColor indexed="64"/></patternFill></fill>
    <fill><patternFill fillType="solid"><fgColor rgb="FFFFC7CE"/><bgColor indexed="64"/></patternFill></fill>
    <fill><patternFill fillType="solid"><fgColor rgb="FFC6EFCE"/><bgColor indexed="64"/></patternFill></fill>
    <fill><patternFill fillType="solid"><fgColor rgb="FFFFEB9C"/><bgColor indexed="64"/></patternFill></fill>
    <fill><patternFill fillType="solid"><fgColor rgb="FFF2F2F2"/><bgColor indexed="64"/></patternFill></fill>
  </fills>
  <borders count="2">
    <border><left/><right/><top/><bottom/><diagonal/></border>
    <border>
      <left style="thin"><color rgb="FFD9D9D9"/></left>
      <right style="thin"><color rgb="FFD9D9D9"/></right>
      <top style="thin"><color rgb="FFD9D9D9"/></top>
      <bottom style="thin"><color rgb="FFD9D9D9"/></bottom>
      <diagonal/>
    </border>
  </borders>
  <cellStyleXfs count="1">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0"/>
  </cellStyleXfs>
  <cellXfs count="10">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1"/>
    <xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center" wrapText="1"/>
    </xf>
    <xf numFmtId="164" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <xf numFmtId="165" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="right" vertical="center"/>
    </xf>
    <xf numFmtId="166" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="right" vertical="center"/>
    </xf>
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <xf numFmtId="167" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="right" vertical="center"/>
    </xf>
    <xf numFmtId="0" fontId="2" fillId="0" borderId="1" xfId="0" applyFont="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="2" fillId="6" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="2" fillId="0" borderId="1" xfId="0" applyFont="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
  </cellXfs>
  <dxfs count="4">
    <dxf>
      <font><color rgb="FF9C0006"/><b/></font>
      <fill><patternFill><bgColor rgb="FFFFC7CE"/></patternFill></fill>
    </dxf>
    <dxf>
      <font><color rgb="FF006100"/><b/></font>
      <fill><patternFill><bgColor rgb="FFC6EFCE"/></patternFill></fill>
    </dxf>
    <dxf>
      <font><color rgb="FF9C6500"/><b/></font>
      <fill><patternFill><bgColor rgb="FFFFEB9C"/></patternFill></fill>
    </dxf>
    <dxf>
      <fill><patternFill><bgColor rgb="FFF2F2F2"/></patternFill></fill>
    </dxf>
  </dxfs>
</styleSheet>"""

def build_sheet_xml(headers, rows, max_rows=50, data_validations_xml="", conditional_formatting_xml="", col_widths=None):
    num_cols = len(headers)
    max_col_letter = col_letter(num_cols)
    total_rows = max(len(rows) + 1, max_rows)
    dimension = f"A1:{max_col_letter}{total_rows}"
    
    xml_parts = []
    xml_parts.append('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
    xml_parts.append('<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">')
    xml_parts.append(f'<dimension ref="{dimension}"/>')
    xml_parts.append('<sheetViews><sheetView tabSelected="1" workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>')
    xml_parts.append('<sheetFormatPr defaultRowHeight="20"/>')
    
    if col_widths:
        xml_parts.append('<cols>')
        for c_idx, width in col_widths.items():
            xml_parts.append(f'<col min="{c_idx}" max="{c_idx}" width="{width}" customWidth="1"/>')
        xml_parts.append('</cols>')
        
    xml_parts.append('<sheetData>')
    
    header_cells = []
    for c_idx, h in enumerate(headers, 1):
        ref = f"{col_letter(c_idx)}1"
        header_cells.append(make_cell(ref, val=h, style_id=1, cell_type="s"))
    xml_parts.append(f'<row r="1" ht="28" customHeight="1">{"".join(header_cells)}</row>')
    
    for r_idx, row_data in enumerate(rows, 2):
        row_cells = []
        for c_idx, cell_spec in enumerate(row_data, 1):
            ref = f"{col_letter(c_idx)}{r_idx}"
            val = cell_spec.get("val")
            f = cell_spec.get("f")
            s = cell_spec.get("s", 0)
            t = cell_spec.get("t")
            row_cells.append(make_cell(ref, val=val, formula=f, style_id=s, cell_type=t))
        xml_parts.append(f'<row r="{r_idx}" ht="20">{"".join(row_cells)}</row>')
        
    xml_parts.append('</sheetData>')
    if conditional_formatting_xml:
        xml_parts.append(conditional_formatting_xml)
    if data_validations_xml:
        xml_parts.append(data_validations_xml)
    xml_parts.append('</worksheet>')
    return "".join(xml_parts)

# 1. Trade_Log
trade_headers = [
    "Trade_ID","Date","Day","Entry_Time","Symbol","Direction","Setup_Name","Scanner_Alert_Time",
    "HTF_Context_OK","Entry_Planned_NoChase","Stop_Defined_Before_Entry","RR_Planned","Risk_Percent",
    "Risk_Amount","Entry_Price","Stop_Price","Exit_Price","Qty","Gross_PnL","Costs","Net_PnL",
    "R_Multiple","Outcome","Checklist_Score_0to5","Rule_Violation","Violation_Type",
    "Emotion_Before_1to10","Emotion_During_1to10","Emotion_After_1to10","Trade_Valid","Lesson","Screenshot_Link"
]

# Costs calculation: 0.11% of turnover = 0.0011 * (Entry_Price * Qty + Exit_Price * Qty)
# Row 2 (T-001): RELIANCE Long. Entry 2500, Stop 2495 (Risk 5 pts), RR 2.2 -> Target 2511 (11 pts reward). Qty 100.
# Turnover: 2500*100 + 2511*100 = 501,100.
# Costs: ROUND(0.0011 * 501,100, 2) = 551.21.
# Gross PnL: (2511 - 2500) * 100 = 1100.00.
# Net PnL: 1100.00 - 551.21 = 548.79.
# Risk: ABS(2500-2495)*100 = 500.00.
# R_Multiple: 548.79 / 500 = 1.10. Outcome: Win.

# Row 3 (T-002): TCS Short. Entry 3500, Stop 3510 (Risk 10 pts), RR 2.2 -> Target 3478. Exit 3510 (Stopped out). Qty 50.
# Turnover: 3500*50 + 3510*50 = 350,500.
# Costs: ROUND(0.0011 * 350,500, 2) = 385.55.
# Gross PnL: (3500 - 3510) * 50 = -500.00.
# Net PnL: -500.00 - 385.55 = -885.55.
# Risk: ABS(3500-3510)*50 = 500.00.
# R_Multiple: -885.55 / 500 = -1.77. Outcome: Loss.

# Row 4 (T-003): INFY Long. Entry 1450, Stop 1445 (Risk 5 pts), RR 2.2 -> Target 1461. Qty 100.
# Turnover: 1450*100 + 1461*100 = 291,100.
# Costs: ROUND(0.0011 * 291,100, 2) = 320.21.
# Gross PnL: (1461 - 1450) * 100 = 1100.00.
# Net PnL: 1100.00 - 320.21 = 779.79.
# Risk: ABS(1450-1445)*100 = 500.00.
# R_Multiple: 779.79 / 500 = 1.56. Outcome: Win.

trade_rows = []

trade_rows.append([
    {"val": "T-001 [EXAMPLE]", "s": 5}, # A
    {"val": "2026-10-20", "s": 2}, # B
    {"f": 'IF(B2="","",TEXT(B2,"ddd"))', "val": "Tue", "s": 5}, # C
    {"val": "09:25", "s": 5}, # D (inside 09:15-10:30)
    {"val": "RELIANCE", "s": 5}, # E
    {"val": "Long", "s": 5}, # F
    {"val": "1m Pullback to 9EMA", "s": 0}, # G
    {"val": "09:23", "s": 5}, # H
    {"val": "Y", "s": 5}, # I
    {"val": "Y", "s": 5}, # J
    {"val": "Y", "s": 5}, # K
    {"val": 2.2, "s": 6}, # L
    {"val": 0.0025, "s": 3}, # M
    {"f": 'IF(OR(O2="",P2="",R2=""),"",ABS(O2-P2)*R2)', "val": 500.0, "s": 4}, # N
    {"val": 2500.0, "s": 4}, # O
    {"val": 2495.0, "s": 4}, # P
    {"val": 2511.0, "s": 4}, # Q
    {"val": 100, "s": 0}, # R
    {"f": 'IF(OR(O2="",Q2="",R2=""),"",IF(F2="Long",(Q2-O2)*R2,(O2-Q2)*R2))', "val": 1100.0, "s": 4}, # S
    {"f": 'IF(OR(O2="",Q2="",R2=""),"",ROUND(0.0011*(O2*R2+Q2*R2),2))', "val": 551.21, "s": 4}, # T (Turnover 0.11%)
    {"f": 'IF(S2="","",S2-T2)', "val": 548.79, "s": 4}, # U
    {"f": 'IF(OR(N2="",N2=0,U2=""),"",U2/N2)', "val": 1.10, "s": 6}, # V
    {"f": 'IF(U2="","",IF(U2>0,"Win",IF(U2<0,"Loss","BE")))', "val": "Win", "s": 5}, # W
    {"val": 5, "s": 5}, # X
    {"val": "N", "s": 5}, # Y
    {"val": "None", "s": 5}, # Z
    {"val": 2, "s": 5}, # AA
    {"val": 3, "s": 5}, # AB
    {"val": 2, "s": 5}, # AC
    {"f": 'IF(OR(X2="",Y2=""),"",IF(AND(X2>=5,Y2="N"),"Y","N"))', "val": "Y", "s": 5}, # AD
    {"val": "Followed plan, entry at limit, patient exit at 2.2R target.", "s": 0}, # AE
    {"val": "https://tradingview.com/x/example1", "s": 0} # AF
])

trade_rows.append([
    {"val": "T-002 [EXAMPLE]", "s": 5}, # A
    {"val": "2026-10-20", "s": 2}, # B
    {"f": 'IF(B3="","",TEXT(B3,"ddd"))', "val": "Tue", "s": 5}, # C
    {"val": "10:05", "s": 5}, # D (inside 09:15-10:30)
    {"val": "TCS", "s": 5}, # E
    {"val": "Short", "s": 5}, # F
    {"val": "1m Breakdown Re-test", "s": 0}, # G
    {"val": "10:02", "s": 5}, # H
    {"val": "Y", "s": 5}, # I
    {"val": "Y", "s": 5}, # J
    {"val": "Y", "s": 5}, # K
    {"val": 2.2, "s": 6}, # L
    {"val": 0.0025, "s": 3}, # M
    {"f": 'IF(OR(O3="",P3="",R3=""),"",ABS(O3-P3)*R3)', "val": 500.0, "s": 4}, # N
    {"val": 3500.0, "s": 4}, # O
    {"val": 3510.0, "s": 4}, # P
    {"val": 3510.0, "s": 4}, # Q
    {"val": 50, "s": 0}, # R
    {"f": 'IF(OR(O3="",Q3="",R3=""),"",IF(F3="Long",(Q3-O3)*R3,(O3-Q3)*R3))', "val": -500.0, "s": 4}, # S
    {"f": 'IF(OR(O3="",Q3="",R3=""),"",ROUND(0.0011*(O3*R3+Q3*R3),2))', "val": 385.55, "s": 4}, # T (Turnover 0.11%)
    {"f": 'IF(S3="","",S3-T3)', "val": -885.55, "s": 4}, # U
    {"f": 'IF(OR(N3="",N3=0,U3=""),"",U3/N3)', "val": -1.77, "s": 6}, # V
    {"f": 'IF(U3="","",IF(U3>0,"Win",IF(U3<0,"Loss","BE")))', "val": "Loss", "s": 5}, # W
    {"val": 5, "s": 5}, # X
    {"val": "N", "s": 5}, # Y
    {"val": "None", "s": 5}, # Z
    {"val": 3, "s": 5}, # AA
    {"val": 4, "s": 5}, # AB
    {"val": 3, "s": 5}, # AC
    {"f": 'IF(OR(X3="",Y3=""),"",IF(AND(X3>=5,Y3="N"),"Y","N"))', "val": "Y", "s": 5}, # AD
    {"val": "Setup failed normally; respected stop without hesitation; entered 30m cooldown.", "s": 0}, # AE
    {"val": "https://tradingview.com/x/example2", "s": 0} # AF
])

trade_rows.append([
    {"val": "T-003 [EXAMPLE]", "s": 5}, # A
    {"val": "2026-10-21", "s": 2}, # B
    {"f": 'IF(B4="","",TEXT(B4,"ddd"))', "val": "Wed", "s": 5}, # C
    {"val": "09:40", "s": 5}, # D (inside 09:15-10:30)
    {"val": "INFY", "s": 5}, # E
    {"val": "Long", "s": 5}, # F
    {"val": "1m Momentum Breakout", "s": 0}, # G
    {"val": "09:38", "s": 5}, # H
    {"val": "Y", "s": 5}, # I
    {"val": "Y", "s": 5}, # J
    {"val": "Y", "s": 5}, # K
    {"val": 2.2, "s": 6}, # L
    {"val": 0.0025, "s": 3}, # M
    {"f": 'IF(OR(O4="",P4="",R4=""),"",ABS(O4-P4)*R4)', "val": 500.0, "s": 4}, # N
    {"val": 1450.0, "s": 4}, # O
    {"val": 1445.0, "s": 4}, # P
    {"val": 1461.0, "s": 4}, # Q
    {"val": 100, "s": 0}, # R
    {"f": 'IF(OR(O4="",Q4="",R4=""),"",IF(F4="Long",(Q4-O4)*R4,(O4-Q4)*R4))', "val": 1100.0, "s": 4}, # S
    {"f": 'IF(OR(O4="",Q4="",R4=""),"",ROUND(0.0011*(O4*R4+Q4*R4),2))', "val": 320.21, "s": 4}, # T (Turnover 0.11%)
    {"f": 'IF(S4="","",S4-T4)', "val": 779.79, "s": 4}, # U
    {"f": 'IF(OR(N4="",N4=0,U4=""),"",U4/N4)', "val": 1.56, "s": 6}, # V
    {"f": 'IF(U4="","",IF(U4>0,"Win",IF(U4<0,"Loss","BE")))', "val": "Win", "s": 5}, # W
    {"val": 5, "s": 5}, # X
    {"val": "N", "s": 5}, # Y
    {"val": "None", "s": 5}, # Z
    {"val": 2, "s": 5}, # AA
    {"val": 3, "s": 5}, # AB
    {"val": 2, "s": 5}, # AC
    {"f": 'IF(OR(X4="",Y4=""),"",IF(AND(X4>=5,Y4="N"),"Y","N"))', "val": "Y", "s": 5}, # AD
    {"val": "Good patience waiting for bar close confirmation. Exited at 2.2R target.", "s": 0}, # AE
    {"val": "https://tradingview.com/x/example3", "s": 0} # AF
])

for r in range(5, 51):
    trade_rows.append([
        {"val": "", "s": 5}, # A
        {"val": "", "s": 2}, # B
        {"f": f'IF(B{r}="","",TEXT(B{r},"ddd"))', "val": "", "s": 5}, # C
        {"val": "", "s": 5}, # D
        {"val": "", "s": 5}, # E
        {"val": "", "s": 5}, # F
        {"val": "", "s": 0}, # G
        {"val": "", "s": 5}, # H
        {"val": "", "s": 5}, # I
        {"val": "", "s": 5}, # J
        {"val": "", "s": 5}, # K
        {"val": "", "s": 6}, # L
        {"val": "", "s": 3}, # M
        {"f": f'IF(OR(O{r}="",P{r}="",R{r}=""),"",ABS(O{r}-P{r})*R{r})', "val": "", "s": 4}, # N
        {"val": "", "s": 4}, # O
        {"val": "", "s": 4}, # P
        {"val": "", "s": 4}, # Q
        {"val": "", "s": 0}, # R
        {"f": f'IF(OR(O{r}="",Q{r}="",R{r}=""),"",IF(F{r}="Long",(Q{r}-O{r})*R{r},(O{r}-Q{r})*R{r}))', "val": "", "s": 4}, # S
        {"f": f'IF(OR(O{r}="",Q{r}="",R{r}=""),"",ROUND(0.0011*(O{r}*R{r}+Q{r}*R{r}),2))', "val": "", "s": 4}, # T (Turnover 0.11%)
        {"f": f'IF(S{r}="","",S{r}-T{r})', "val": "", "s": 4}, # U
        {"f": f'IF(OR(N{r}="",N{r}=0,U{r}=""),"",U{r}/N{r})', "val": "", "s": 6}, # V
        {"f": f'IF(U{r}="","",IF(U{r}>0,"Win",IF(U{r}<0,"Loss","BE")))', "val": "", "s": 5}, # W
        {"val": "", "s": 5}, # X
        {"val": "", "s": 5}, # Y
        {"val": "", "s": 5}, # Z
        {"val": "", "s": 5}, # AA
        {"val": "", "s": 5}, # AB
        {"val": "", "s": 5}, # AC
        {"f": f'IF(OR(X{r}="",Y{r}=""),"",IF(AND(X{r}>=5,Y{r}="N"),"Y","N"))', "val": "", "s": 5}, # AD
        {"val": "", "s": 0}, # AE
        {"val": "", "s": 0} # AF
    ])

trade_cf_xml = """<conditionalFormatting sqref="Y2:Y50">
  <cfRule type="cellIs" dxfId="0" priority="1" operator="equal">
    <formula>&quot;Y&quot;</formula>
  </cfRule>
</conditionalFormatting>
<conditionalFormatting sqref="X2:X50">
  <cfRule type="cellIs" dxfId="2" priority="2" operator="lessThan">
    <formula>5</formula>
  </cfRule>
</conditionalFormatting>
<conditionalFormatting sqref="W2:W50">
  <cfRule type="cellIs" dxfId="0" priority="3" operator="equal">
    <formula>&quot;Loss&quot;</formula>
  </cfRule>
  <cfRule type="cellIs" dxfId="1" priority="4" operator="equal">
    <formula>&quot;Win&quot;</formula>
  </cfRule>
</conditionalFormatting>"""

trade_dv_xml = """<dataValidations count="6">
  <dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1" sqref="F2:F50">
    <formula1>&quot;Long,Short&quot;</formula1>
  </dataValidation>
  <dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1" sqref="I2:K50 Y2:Y50">
    <formula1>&quot;Y,N&quot;</formula1>
  </dataValidation>
  <dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1" sqref="W2:W50">
    <formula1>&quot;Win,Loss,BE&quot;</formula1>
  </dataValidation>
  <dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1" sqref="X2:X50">
    <formula1>&quot;0,1,2,3,4,5&quot;</formula1>
  </dataValidation>
  <dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1" sqref="Z2:Z50">
    <formula1>&quot;None,Overtrading,Revenge,FOMO/Chase,No Stop,Moved Stop,Averaged Down,Outside Window,Other&quot;</formula1>
  </dataValidation>
  <dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1" sqref="AA2:AC50">
    <formula1>&quot;1,2,3,4,5,6,7,8,9,10&quot;</formula1>
  </dataValidation>
</dataValidations>"""

trade_widths = {
    1: 18, 2: 13, 3: 8, 4: 12, 5: 12, 6: 11, 7: 24, 8: 18,
    9: 17, 10: 22, 11: 24, 12: 13, 13: 13, 14: 14, 15: 13, 16: 13,
    17: 13, 18: 10, 19: 13, 20: 12, 21: 13, 22: 12, 23: 11, 24: 21,
    25: 15, 26: 22, 27: 21, 28: 21, 29: 20, 30: 13, 31: 40, 32: 30
}

sheet1_xml = build_sheet_xml(trade_headers, trade_rows, max_rows=50,
                             data_validations_xml=trade_dv_xml,
                             conditional_formatting_xml=trade_cf_xml,
                             col_widths=trade_widths)

# 2. Daily_Scorecard
# Day 1 (2026-10-20): Net PnL = 548.79 - 885.55 = -336.76. Daily R = 1.10 - 1.77 = -0.67R.
# Day 2 (2026-10-21): Net PnL = +779.79. Daily R = +1.56R.

daily_headers = [
    "Date","Trades_Taken","Max_Trades_Allowed","Losses","Max_Losses_Allowed",
    "Daily_Net_PnL","Daily_R","Checklist_Trades_5of5","Rule_Violations",
    "Adherence_Score_0to5","Adherence_Pct","Hit_Daily_Loss_Limit","Stopped_After_2_Losses","Notes"
]

daily_rows = []
daily_rows.append([
    {"val": "2026-10-20", "s": 2}, # A
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A2)', "val": 2, "s": 5}, # B
    {"val": 2, "s": 5}, # C
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A2,Trade_Log!$W:$W,"Loss")', "val": 1, "s": 5}, # D
    {"val": 2, "s": 5}, # E
    {"f": 'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,$A2)', "val": -336.76, "s": 4}, # F
    {"f": 'SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,$A2)', "val": -0.67, "s": 6}, # G
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A2,Trade_Log!$X:$X,5)', "val": 2, "s": 5}, # H
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A2,Trade_Log!$Y:$Y,"Y")', "val": 0, "s": 5}, # I
    {"val": 5, "s": 5}, # J
    {"f": 'IF(J2="","",J2/5)', "val": 1.0, "s": 3}, # K
    {"val": "N", "s": 5}, # L
    {"val": "N", "s": 5}, # M
    {"val": "[EXAMPLE] 09:15-10:30 window followed. 1 win, 1 loss. Respected 30m cooldown.", "s": 0} # N
])

daily_rows.append([
    {"val": "2026-10-21", "s": 2}, # A
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A3)', "val": 1, "s": 5}, # B
    {"val": 2, "s": 5}, # C
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A3,Trade_Log!$W:$W,"Loss")', "val": 0, "s": 5}, # D
    {"val": 2, "s": 5}, # E
    {"f": 'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,$A3)', "val": 779.79, "s": 4}, # F
    {"f": 'SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,$A3)', "val": 1.56, "s": 6}, # G
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A3,Trade_Log!$X:$X,5)', "val": 1, "s": 5}, # H
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A3,Trade_Log!$Y:$Y,"Y")', "val": 0, "s": 5}, # I
    {"val": 5, "s": 5}, # J
    {"f": 'IF(J3="","",J3/5)', "val": 1.0, "s": 3}, # K
    {"val": "N", "s": 5}, # L
    {"val": "N", "s": 5}, # M
    {"val": "[EXAMPLE] Single A+ trade taken within 09:15-10:30 window. Platform closed.", "s": 0} # N
])

for r in range(4, 36):
    daily_rows.append([
        {"val": "", "s": 2}, # A
        {"f": f'COUNTIFS(Trade_Log!$B:$B,$A{r})', "val": "", "s": 5}, # B
        {"val": 2, "s": 5}, # C
        {"f": f'COUNTIFS(Trade_Log!$B:$B,$A{r},Trade_Log!$W:$W,"Loss")', "val": "", "s": 5}, # D
        {"val": 2, "s": 5}, # E
        {"f": f'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,$A{r})', "val": "", "s": 4}, # F
        {"f": f'SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,$A{r})', "val": "", "s": 6}, # G
        {"f": f'COUNTIFS(Trade_Log!$B:$B,$A{r},Trade_Log!$X:$X,5)', "val": "", "s": 5}, # H
        {"f": f'COUNTIFS(Trade_Log!$B:$B,$A{r},Trade_Log!$Y:$Y,"Y")', "val": "", "s": 5}, # I
        {"val": "", "s": 5}, # J
        {"f": f'IF(J{r}="","",J{r}/5)', "val": "", "s": 3}, # K
        {"val": "", "s": 5}, # L
        {"val": "", "s": 5}, # M
        {"val": "", "s": 0} # N
    ])

daily_cf_xml = """<conditionalFormatting sqref="K2:K35">
  <cfRule type="cellIs" dxfId="0" priority="1" operator="lessThan">
    <formula>0.9</formula>
  </cfRule>
  <cfRule type="cellIs" dxfId="1" priority="2" operator="greaterThanOrEqual">
    <formula>0.95</formula>
  </cfRule>
</conditionalFormatting>"""

daily_dv_xml = """<dataValidations count="1">
  <dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1" sqref="L2:M35">
    <formula1>&quot;Y,N&quot;</formula1>
  </dataValidation>
</dataValidations>"""

daily_widths = {
    1: 13, 2: 14, 3: 19, 4: 10, 5: 19, 6: 15, 7: 11,
    8: 22, 9: 16, 10: 22, 11: 15, 12: 20, 13: 23, 14: 45
}

sheet2_xml = build_sheet_xml(daily_headers, daily_rows, max_rows=35,
                             data_validations_xml=daily_dv_xml,
                             conditional_formatting_xml=daily_cf_xml,
                             col_widths=daily_widths)

# 3. Weekly_Review
# Week 2026-10-19 to 2026-10-23:
# Total trades: 3. Wins: 2. Losses: 1. Win Rate: 66.7%.
# Net PnL: 548.79 - 885.55 + 779.79 = 443.03.
# Net Avg_R: (1.10 - 1.77 + 1.56) / 3 = 0.30R.
# Expectancy_R: 0.30R. Adherence: 100%. Violations: 0. Revenge: 0.

weekly_headers = [
    "Week_Start","Week_End","Trades","Wins","Losses","Win_Rate","Net_PnL","Avg_R",
    "Expectancy_R","Checklist_Adherence_Pct","Violations","Revenge_Trades",
    "Best_Time_Window","Worst_Time_Window","Top_Mistake","Rule_To_Tighten"
]

weekly_rows = []
weekly_rows.append([
    {"val": "2026-10-19", "s": 2}, # A
    {"val": "2026-10-23", "s": 2}, # B
    {"f": 'COUNTIFS(Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2)', "val": 3, "s": 5}, # C
    {"f": 'COUNTIFS(Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2,Trade_Log!$W:$W,"Win")', "val": 2, "s": 5}, # D
    {"f": 'COUNTIFS(Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2,Trade_Log!$W:$W,"Loss")', "val": 1, "s": 5}, # E
    {"f": 'IF(C2=0,"",D2/C2)', "val": 0.667, "s": 3}, # F
    {"f": 'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2)', "val": 443.03, "s": 4}, # G
    {"f": 'IFERROR(AVERAGEIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2),"")', "val": 0.30, "s": 6}, # H
    {"f": 'IF(C2=0,"",SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2)/C2)', "val": 0.30, "s": 6}, # I
    {"f": 'IF(C2=0,"",COUNTIFS(Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2,Trade_Log!$X:$X,5)/C2)', "val": 1.0, "s": 3}, # J
    {"f": 'COUNTIFS(Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2,Trade_Log!$Y:$Y,"Y")', "val": 0, "s": 5}, # K
    {"f": 'COUNTIFS(Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2,Trade_Log!$Z:$Z,"Revenge")', "val": 0, "s": 5}, # L
    {"val": "09:15-10:00", "s": 5}, # M
    {"val": "None", "s": 5}, # N
    {"val": "[EXAMPLE] None (100% adherence to 09:15-10:30 window)", "s": 0}, # O
    {"val": "Maintain RR >= 2.2 and 30-min cooldown after any loss", "s": 0} # P
])

for r in range(3, 10):
    weekly_rows.append([
        {"val": "", "s": 2}, # A
        {"val": "", "s": 2}, # B
        {"f": f'COUNTIFS(Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r})', "val": "", "s": 5}, # C
        {"f": f'COUNTIFS(Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r},Trade_Log!$W:$W,"Win")', "val": "", "s": 5}, # D
        {"f": f'COUNTIFS(Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r},Trade_Log!$W:$W,"Loss")', "val": "", "s": 5}, # E
        {"f": f'IF(C{r}=0,"",D{r}/C{r})', "val": "", "s": 3}, # F
        {"f": f'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r})', "val": "", "s": 4}, # G
        {"f": f'IFERROR(AVERAGEIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r}),"")', "val": "", "s": 6}, # H
        {"f": f'IF(C{r}=0,"",SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r})/C{r})', "val": "", "s": 6}, # I
        {"f": f'IF(C{r}=0,"",COUNTIFS(Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r},Trade_Log!$X:$X,5)/C{r})', "val": "", "s": 3}, # J
        {"f": f'COUNTIFS(Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r},Trade_Log!$Y:$Y,"Y")', "val": "", "s": 5}, # K
        {"f": f'COUNTIFS(Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r},Trade_Log!$Z:$Z,"Revenge")', "val": "", "s": 5}, # L
        {"val": "", "s": 5}, # M
        {"val": "", "s": 5}, # N
        {"val": "", "s": 0}, # O
        {"val": "", "s": 0} # P
    ])

weekly_cf_xml = """<conditionalFormatting sqref="J2:J10">
  <cfRule type="cellIs" dxfId="0" priority="1" operator="lessThan">
    <formula>0.9</formula>
  </cfRule>
</conditionalFormatting>"""

weekly_widths = {
    1: 13, 2: 13, 3: 10, 4: 10, 5: 10, 6: 12, 7: 14, 8: 10,
    9: 14, 10: 23, 11: 12, 12: 16, 13: 18, 14: 18, 15: 35, 16: 35
}

sheet3_xml = build_sheet_xml(weekly_headers, weekly_rows, max_rows=10,
                             conditional_formatting_xml=weekly_cf_xml,
                             col_widths=weekly_widths)

# 4. Journal
journal_headers = [
    "Date","Trade_ID","Symbol","Setup","What_I_Saw","Why_I_Entered",
    "Emotion_Before","Emotion_During","Emotion_After","Rule_Violation",
    "What_I_Did_Well","What_Ill_Do_Differently","Screenshot_Link"
]

journal_rows = []
journal_rows.append([
    {"val": "2026-10-20", "s": 2}, # A
    {"val": "T-001 [EXAMPLE]", "s": 5}, # B
    {"val": "RELIANCE", "s": 5}, # C
    {"val": "1m Pullback to 9EMA", "s": 0}, # D
    {"val": "15m bullish trend. 1m scanner alert at 09:23 inside 09:15-10:30 window. Flag pullback to 9EMA with low volume.", "s": 0}, # E
    {"val": "Bullish pinbar rejection at 9EMA. Limit order placed at 2500, stop 2495 (5 pts risk), target 2511 (2.2R).", "s": 0}, # F
    {"val": 2, "s": 5}, # G
    {"val": 3, "s": 5}, # H
    {"val": 2, "s": 5}, # I
    {"val": "N", "s": 5}, # J
    {"val": "Waited for limit order fill. Respected 2.2R target. Did not market chase.", "s": 0}, # K
    {"val": "Trail stop to breakeven after 1.5R reached.", "s": 0}, # L
    {"val": "https://tradingview.com/x/example1", "s": 0} # M
])

journal_rows.append([
    {"val": "2026-10-20", "s": 2}, # A
    {"val": "T-002 [EXAMPLE]", "s": 5}, # B
    {"val": "TCS", "s": 5}, # C
    {"val": "1m Breakdown Re-test", "s": 0}, # D
    {"val": "15m downward structure. 1m scanner alerted breakdown at 10:02 inside window. Retest of 3500 level.", "s": 0}, # E
    {"val": "Bearish engulfing on 1m. Stop at 3510 (10 pts), target 3478 (2.2R).", "s": 0}, # F
    {"val": 3, "s": 5}, # G
    {"val": 4, "s": 5}, # H
    {"val": 3, "s": 5}, # I
    {"val": "N", "s": 5}, # J
    {"val": "Accepted loss immediately at stop without widening. Walked away for 30m cooldown.", "s": 0}, # K
    {"val": "Verify sectoral index (IT) alignment before shorting stock.", "s": 0}, # L
    {"val": "https://tradingview.com/x/example2", "s": 0} # M
])

for r in range(4, 30):
    journal_rows.append([
        {"val": "", "s": 2}, # A
        {"val": "", "s": 5}, # B
        {"val": "", "s": 5}, # C
        {"val": "", "s": 0}, # D
        {"val": "", "s": 0}, # E
        {"val": "", "s": 0}, # F
        {"val": "", "s": 5}, # G
        {"val": "", "s": 5}, # H
        {"val": "", "s": 5}, # I
        {"val": "", "s": 5}, # J
        {"val": "", "s": 0}, # K
        {"val": "", "s": 0}, # L
        {"val": "", "s": 0} # M
    ])

journal_widths = {
    1: 13, 2: 18, 3: 12, 4: 22, 5: 35, 6: 35,
    7: 15, 8: 15, 9: 15, 10: 15, 11: 35, 12: 35, 13: 30
}

journal_dv_xml = """<dataValidations count="2">
  <dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1" sqref="J2:J30">
    <formula1>&quot;Y,N&quot;</formula1>
  </dataValidation>
  <dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1" sqref="G2:I30">
    <formula1>&quot;1,2,3,4,5,6,7,8,9,10&quot;</formula1>
  </dataValidation>
</dataValidations>"""

sheet4_xml = build_sheet_xml(journal_headers, journal_rows, max_rows=30,
                             data_validations_xml=journal_dv_xml,
                             col_widths=journal_widths)

content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet3.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet4.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
</Types>"""

root_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>"""

wb_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet3.xml"/>
  <Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet4.xml"/>
  <Relationship Id="rId5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

workbook_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="Trade_Log" sheetId="1" r:id="rId1"/>
    <sheet name="Daily_Scorecard" sheetId="2" r:id="rId2"/>
    <sheet name="Weekly_Review" sheetId="3" r:id="rId3"/>
    <sheet name="Journal" sheetId="4" r:id="rId4"/>
  </sheets>
</workbook>"""

out_path = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D3_Tracking_Spreadsheet.xlsx"
with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml', content_types)
    z.writestr('_rels/.rels', root_rels)
    z.writestr('xl/_rels/workbook.xml.rels', wb_rels)
    z.writestr('xl/workbook.xml', workbook_xml)
    z.writestr('xl/styles.xml', styles_xml)
    z.writestr('xl/worksheets/sheet1.xml', sheet1_xml)
    z.writestr('xl/worksheets/sheet2.xml', sheet2_xml)
    z.writestr('xl/worksheets/sheet3.xml', sheet3_xml)
    z.writestr('xl/worksheets/sheet4.xml', sheet4_xml)

print(f"Spreadsheet generated successfully at: {out_path}")
