import zipfile
import html
import os

class SharedStringsTable:
    def __init__(self):
        self.strings = []
        self.str_to_idx = {}
        
    def get_index(self, s):
        if s is None:
            s = ""
        s = str(s)
        if s in self.str_to_idx:
            return self.str_to_idx[s]
        idx = len(self.strings)
        self.strings.append(s)
        self.str_to_idx[s] = idx
        return idx
        
    def to_xml(self):
        parts = [
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
            f'<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="{len(self.strings)}" uniqueCount="{len(self.strings)}">'
        ]
        for s in self.strings:
            escaped = html.escape(s)
            parts.append(f'<si><t>{escaped}</t></si>')
        parts.append('</sst>')
        return "".join(parts)

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

def make_cell(ref, val=None, formula=None, style_id=None, cell_type=None, sst=None):
    s_attr = f' s="{style_id}"' if style_id is not None else ""
    if formula is not None:
        f_xml = f'<f>{escape_xml(formula)}</f>'
        if cell_type == "str" or (cell_type is None and isinstance(val, str) and val != ""):
            v_xml = f'<v>{escape_xml(val)}</v>' if val is not None else '<v></v>'
            return f'<c r="{ref}"{s_attr} t="str">{f_xml}{v_xml}</c>'
        else:
            v_xml = f'<v>{escape_xml(val)}</v>' if val is not None else '<v></v>'
            return f'<c r="{ref}"{s_attr}>{f_xml}{v_xml}</c>'
    elif val is None or val == "":
        return f'<c r="{ref}"{s_attr}/>'
    elif cell_type == "s" or isinstance(val, str):
        if sst is not None:
            s_idx = sst.get_index(val)
            return f'<c r="{ref}"{s_attr} t="s"><v>{s_idx}</v></c>'
        else:
            return f'<c r="{ref}"{s_attr} t="inlineStr"><is><t>{escape_xml(val)}</t></is></c>'
    elif isinstance(val, (int, float)):
        return f'<c r="{ref}"{s_attr}><v>{val}</v></c>'
    else:
        if sst is not None:
            s_idx = sst.get_index(str(val))
            return f'<c r="{ref}"{s_attr} t="s"><v>{s_idx}</v></c>'
        else:
            return f'<c r="{ref}"{s_attr} t="inlineStr"><is><t>{escape_xml(str(val))}</t></is></c>'

styles_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <numFmts count="6">
    <numFmt numFmtId="164" formatCode="yyyy-mm-dd"/>
    <numFmt numFmtId="165" formatCode="0.0%"/>
    <numFmt numFmtId="166" formatCode="₹#,##0.00"/>
    <numFmt numFmtId="167" formatCode="0.00"/>
    <numFmt numFmtId="168" formatCode="0.00&quot; R&quot;"/>
    <numFmt numFmtId="169" formatCode="#,##0"/>
  </numFmts>
  <fonts count="14">
    <!-- 0: Standard normal -->
    <font><sz val="10"/><name val="Segoe UI"/><color rgb="FF1E293B"/></font>
    <!-- 1: Header (Dark Navy bold white) -->
    <font><b/><sz val="10.5"/><name val="Segoe UI"/><color rgb="FFFFFFFF"/></font>
    <!-- 2: Bold Normal -->
    <font><b/><sz val="10"/><name val="Segoe UI"/><color rgb="FF0F172A"/></font>
    <!-- 3: Red Bold -->
    <font><b/><sz val="10"/><name val="Segoe UI"/><color rgb="FF991B1B"/></font>
    <!-- 4: Green Bold -->
    <font><b/><sz val="10"/><name val="Segoe UI"/><color rgb="FF065F46"/></font>
    <!-- 5: Orange Bold -->
    <font><b/><sz val="10"/><name val="Segoe UI"/><color rgb="FF92400E"/></font>
    <!-- 6: Title font (16pt bold navy) -->
    <font><b/><sz val="16"/><name val="Segoe UI"/><color rgb="FF0F172A"/></font>
    <!-- 7: Subtitle font (10pt slate) -->
    <font><sz val="10"/><name val="Segoe UI"/><color rgb="FF64748B"/></font>
    <!-- 8: Card Title font (9pt bold slate uppercase) -->
    <font><b/><sz val="9"/><name val="Segoe UI"/><color rgb="FF475569"/></font>
    <!-- 9: Card Metric Large (18pt bold navy) -->
    <font><b/><sz val="18"/><name val="Segoe UI"/><color rgb="FF0F172A"/></font>
    <!-- 10: Card Subtext (8.5pt muted) -->
    <font><sz val="8.5"/><name val="Segoe UI"/><color rgb="FF64748B"/></font>
    <!-- 11: Section Header (12pt bold navy) -->
    <font><b/><sz val="12"/><name val="Segoe UI"/><color rgb="FF1E293B"/></font>
    <!-- 12: Fast Entry Input Header (Bright Blue bold white) -->
    <font><b/><sz val="11"/><name val="Segoe UI"/><color rgb="FFFFFFFF"/></font>
    <!-- 13: Auto-Calc Header (Muted Gray italic) -->
    <font><sz val="9.5"/><name val="Segoe UI"/><color rgb="FF64748B"/></font>
  </fonts>
  <fills count="12">
    <fill><patternFill fillType="none"/></fill>
    <fill><patternFill fillType="gray125"/></fill>
    <!-- 2: Dark Navy Header Fill (#0F172A) -->
    <fill><patternFill fillType="solid"><fgColor rgb="FF0F172A"/></patternFill></fill>
    <!-- 3: Slate Subheader Fill (#1E293B) -->
    <fill><patternFill fillType="solid"><fgColor rgb="FF1E293B"/></patternFill></fill>
    <!-- 4: Card Background Fill (#F8FAFC) -->
    <fill><patternFill fillType="solid"><fgColor rgb="FFF8FAFC"/></patternFill></fill>
    <!-- 5: Soft Red Fill (#FEE2E2) -->
    <fill><patternFill fillType="solid"><fgColor rgb="FFFEE2E2"/></patternFill></fill>
    <!-- 6: Soft Green Fill (#D1FAE5) -->
    <fill><patternFill fillType="solid"><fgColor rgb="FFD1FAE5"/></patternFill></fill>
    <!-- 7: Soft Orange Fill (#FEF3C7) -->
    <fill><patternFill fillType="solid"><fgColor rgb="FFFEF3C7"/></patternFill></fill>
    <!-- 8: Fast Entry Action Blue Fill (#2563EB) -->
    <fill><patternFill fillType="solid"><fgColor rgb="FF2563EB"/></patternFill></fill>
    <!-- 9: Light Slate (#F1F5F9) -->
    <fill><patternFill fillType="solid"><fgColor rgb="FFF1F5F9"/></patternFill></fill>
    <!-- 10: Auto-Calc Gray Fill (#E2E8F0) -->
    <fill><patternFill fillType="solid"><fgColor rgb="FFE2E8F0"/></patternFill></fill>
    <!-- 11: Soft Highlight Input Fill (#EFF6FF) -->
    <fill><patternFill fillType="solid"><fgColor rgb="FFEFF6FF"/></patternFill></fill>
  </fills>
  <borders count="4">
    <border><left/><right/><top/><bottom/><diagonal/></border>
    <border>
      <left style="thin"><color rgb="FFE2E8F0"/></left>
      <right style="thin"><color rgb="FFE2E8F0"/></right>
      <top style="thin"><color rgb="FFE2E8F0"/></top>
      <bottom style="thin"><color rgb="FFE2E8F0"/></bottom>
    </border>
    <border>
      <left style="medium"><color rgb="FFCBD5E1"/></left>
      <right style="medium"><color rgb="FFCBD5E1"/></right>
      <top style="medium"><color rgb="FFCBD5E1"/></top>
      <bottom style="medium"><color rgb="FFCBD5E1"/></bottom>
    </border>
    <border>
      <left style="thin"><color rgb="FFE2E8F0"/></left>
      <right style="thin"><color rgb="FFE2E8F0"/></right>
      <top style="medium"><color rgb="FF3B82F6"/></top>
      <bottom style="thin"><color rgb="FFE2E8F0"/></bottom>
    </border>
  </borders>
  <cellStyleXfs count="1">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0"/>
  </cellStyleXfs>
  <cellXfs count="28">
    <!-- 0: Standard normal -->
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyFont="1" applyBorder="1"/>
    <!-- 1: Modern Table Header (Dark Navy #0F172A, White Bold) -->
    <xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center" wrapText="1"/>
    </xf>
    <!-- 2: Date format (YYYY-MM-DD) -->
    <xf numFmtId="164" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <!-- 3: Percentage format (0.0%) -->
    <xf numFmtId="165" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="right" vertical="center"/>
    </xf>
    <!-- 4: Currency (₹#,##0.00) -->
    <xf numFmtId="166" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="right" vertical="center"/>
    </xf>
    <!-- 5: Center normal -->
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <!-- 6: Decimal 2 places (0.00) -->
    <xf numFmtId="167" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="right" vertical="center"/>
    </xf>
    <!-- 7: Bold Normal -->
    <xf numFmtId="0" fontId="2" fillId="0" borderId="1" xfId="0" applyFont="1" applyBorder="1"/>
    <!-- 8: Subheader Fill Slate -->
    <xf numFmtId="0" fontId="1" fillId="3" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1"/>
    <!-- 9: Center Bold -->
    <xf numFmtId="0" fontId="2" fillId="0" borderId="1" xfId="0" applyFont="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <!-- 10: Dashboard Title (16pt Navy) -->
    <xf numFmtId="0" fontId="6" fillId="0" borderId="0" xfId="0" applyFont="1" applyAlignment="1">
      <alignment horizontal="left" vertical="center"/>
    </xf>
    <!-- 11: Dashboard Subtitle -->
    <xf numFmtId="0" fontId="7" fillId="0" borderId="0" xfId="0" applyFont="1" applyAlignment="1">
      <alignment horizontal="left" vertical="center"/>
    </xf>
    <!-- 12: Widget Card Header (Small Caps Slate) -->
    <xf numFmtId="0" fontId="8" fillId="4" borderId="3" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <!-- 13: Widget Card Metric (18pt Bold Navy) -->
    <xf numFmtId="0" fontId="9" fillId="4" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <!-- 14: Widget Card Metric Currency -->
    <xf numFmtId="166" fontId="9" fillId="4" borderId="1" xfId="0" applyNumberFormat="1" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <!-- 15: Widget Card Metric Percentage -->
    <xf numFmtId="165" fontId="9" fillId="4" borderId="1" xfId="0" applyNumberFormat="1" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <!-- 16: Widget Card Subtext -->
    <xf numFmtId="0" fontId="10" fillId="4" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <!-- 17: Dashboard Section Header (12pt Navy bold with slate fill) -->
    <xf numFmtId="0" fontId="11" fillId="9" borderId="2" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="left" vertical="center"/>
    </xf>
    <!-- 18: Card Metric R multiple (18pt) -->
    <xf numFmtId="168" fontId="9" fillId="4" borderId="1" xfId="0" applyNumberFormat="1" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <!-- 19: R multiple format 2 decimal (0.00 R) normal text -->
    <xf numFmtId="168" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="right" vertical="center"/>
    </xf>
    <!-- 20: Table Alt Row (Zebra) -->
    <xf numFmtId="0" fontId="0" fillId="4" borderId="1" xfId="0" applyFill="1" applyBorder="1"/>
    <!-- 21: Table Alt Row Date -->
    <xf numFmtId="164" fontId="0" fillId="4" borderId="1" xfId="0" applyNumberFormat="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <!-- 22: Table Alt Row Currency -->
    <xf numFmtId="166" fontId="0" fillId="4" borderId="1" xfId="0" applyNumberFormat="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="right" vertical="center"/>
    </xf>
    <!-- 23: Table Alt Row Center -->
    <xf numFmtId="0" fontId="0" fillId="4" borderId="1" xfId="0" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <!-- 24: FAST ENTRY Action Blue Header (#2563EB) -->
    <xf numFmtId="0" fontId="12" fillId="8" borderId="2" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center" wrapText="1"/>
    </xf>
    <!-- 25: AUTO-CALC Header Muted (#E2E8F0) -->
    <xf numFmtId="0" fontId="13" fillId="10" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center" wrapText="1"/>
    </xf>
    <!-- 26: Fast Entry Input Cell Highlight (#EFF6FF) -->
    <xf numFmtId="0" fontId="2" fillId="11" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <!-- 27: Fast Entry Input Price Cell Highlight (#EFF6FF) -->
    <xf numFmtId="166" fontId="2" fillId="11" borderId="1" xfId="0" applyNumberFormat="1" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="right" vertical="center"/>
    </xf>
  </cellXfs>
  <dxfs count="4">
    <dxf>
      <font><color rgb="FF991B1B"/><b/></font>
      <fill><patternFill><bgColor rgb="FFFEE2E2"/></patternFill></fill>
    </dxf>
    <dxf>
      <font><color rgb="FF065F46"/><b/></font>
      <fill><patternFill><bgColor rgb="FFD1FAE5"/></patternFill></fill>
    </dxf>
    <dxf>
      <font><color rgb="FF92400E"/><b/></font>
      <fill><patternFill><bgColor rgb="FFFEF3C7"/></patternFill></fill>
    </dxf>
    <dxf>
      <fill><patternFill><bgColor rgb="FFF8FAFC"/></patternFill></fill>
    </dxf>
  </dxfs>
</styleSheet>"""

sst = SharedStringsTable()

def build_sheet_xml(headers, rows, max_rows=50, data_validations_xml="", conditional_formatting_xml="", col_widths=None, freeze_panes=True, custom_top_rows=None, drawing_rId=None, header_style_map=None):
    num_cols = len(headers) if headers else 16
    max_col_letter = col_letter(num_cols)
    total_rows = max(len(rows) + (1 if headers else 0), max_rows)
    dimension = f"A1:{max_col_letter}{total_rows}"
    
    xml_parts = []
    xml_parts.append('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
    xml_parts.append('<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">')
    xml_parts.append(f'<dimension ref="{dimension}"/>')
    
    if freeze_panes:
        split_r = (max(custom_top_rows.keys()) if custom_top_rows else 1)
        top_left = f"A{split_r + 1}"
        xml_parts.append(f'<sheetViews><sheetView tabSelected="1" workbookViewId="0"><pane ySplit="{split_r}" topLeftCell="{top_left}" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>')
    else:
        xml_parts.append('<sheetViews><sheetView tabSelected="1" workbookViewId="0"/></sheetViews>')
        
    xml_parts.append('<sheetFormatPr defaultRowHeight="20"/>')
    
    if col_widths:
        xml_parts.append('<cols>')
        for c_idx, width in col_widths.items():
            xml_parts.append(f'<col min="{c_idx}" max="{c_idx}" width="{width}" customWidth="1"/>')
        xml_parts.append('</cols>')
        
    xml_parts.append('<sheetData>')
    
    start_r = 1
    if custom_top_rows:
        for r_num, row_info in custom_top_rows.items():
            height = row_info.get("height", 22)
            cells = row_info.get("cells", [])
            c_xmls = []
            for c_spec in cells:
                ref = c_spec.get("ref")
                val = c_spec.get("val")
                f = c_spec.get("f")
                s = c_spec.get("s", 0)
                t = c_spec.get("t")
                c_xmls.append(make_cell(ref, val=val, formula=f, style_id=s, cell_type=t, sst=sst))
            xml_parts.append(f'<row r="{r_num}" ht="{height}" customHeight="1">{"".join(c_xmls)}</row>')
            start_r = max(start_r, r_num + 1)
            
    if headers:
        header_cells = []
        for c_idx, h in enumerate(headers, 1):
            ref = f"{col_letter(c_idx)}{start_r}"
            s_id = header_style_map.get(c_idx, 1) if header_style_map else 1
            header_cells.append(make_cell(ref, val=h, style_id=s_id, cell_type="s", sst=sst))
        xml_parts.append(f'<row r="{start_r}" ht="28" customHeight="1">{"".join(header_cells)}</row>')
        start_r += 1
        
    for r_offset, row_data in enumerate(rows):
        r_idx = start_r + r_offset
        row_cells = []
        for c_idx, cell_spec in enumerate(row_data, 1):
            ref = f"{col_letter(c_idx)}{r_idx}"
            val = cell_spec.get("val")
            f = cell_spec.get("f")
            s = cell_spec.get("s", 0)
            t = cell_spec.get("t")
            row_cells.append(make_cell(ref, val=val, formula=f, style_id=s, cell_type=t, sst=sst))
        xml_parts.append(f'<row r="{r_idx}" ht="20">{"".join(row_cells)}</row>')
        
    xml_parts.append('</sheetData>')
    if conditional_formatting_xml:
        xml_parts.append(conditional_formatting_xml)
    if data_validations_xml:
        xml_parts.append(data_validations_xml)
    if drawing_rId:
        xml_parts.append(f'<drawing r:id="{drawing_rId}"/>')
    xml_parts.append('</worksheet>')
    return "".join(xml_parts)

# ==========================================
# 0. DASHBOARD TAB
# ==========================================
dash_widths = {
    1: 4, 2: 22, 3: 16, 4: 16, 5: 4, 6: 22, 7: 18, 8: 18, 9: 4, 10: 22, 11: 18, 12: 18
}

dash_custom_rows = {
    1: {
        "height": 34,
        "cells": [
            {"ref": "B1", "val": "TRADER EXECUTION RESET SYSTEM — VISUAL COMMAND CENTER", "s": 10},
        ]
    },
    2: {
        "height": 18,
        "cells": [
            {"ref": "B2", "val": "NSE Equities 1m | Window: 09:15–10:30 AM IST | Starting Capital: ₹2,00,000 | Risk: 0.25% (₹500) | Min RR: ≥ 2.2 | FYERS Charges", "s": 11},
        ]
    },
    # Top KPI Cards
    4: {
        "height": 18,
        "cells": [
            {"ref": "B4", "val": "STARTING & CURRENT CAPITAL", "s": 12},
            {"ref": "C4", "val": "", "s": 12},
            {"ref": "D4", "val": "", "s": 12},
            {"ref": "F4", "val": "CUMULATIVE NET P&L", "s": 12},
            {"ref": "G4", "val": "", "s": 12},
            {"ref": "H4", "val": "", "s": 12},
            {"ref": "J4", "val": "CHECKLIST ADHERENCE", "s": 12},
            {"ref": "K4", "val": "", "s": 12},
            {"ref": "L4", "val": "", "s": 12},
        ]
    },
    5: {
        "height": 30,
        "cells": [
            {"ref": "B5", "val": "₹2,01,358.05 (+0.68%)", "s": 13},
            {"ref": "C5", "val": "", "s": 13},
            {"ref": "D5", "val": "", "s": 13},
            {"ref": "F5", "f": "SUM(Trade_Log!U2:U50)", "val": 1358.05, "s": 14},
            {"ref": "G5", "val": "", "s": 14},
            {"ref": "H5", "val": "", "s": 14},
            {"ref": "J5", "f": 'IF(COUNTA(Trade_Log!B2:B50)=0,0,COUNTIF(Trade_Log!X2:X50,5)/COUNTA(Trade_Log!B2:B50))', "val": 1.0, "s": 15},
            {"ref": "K5", "val": "", "s": 15},
            {"ref": "L5", "val": "", "s": 15},
        ]
    },
    6: {
        "height": 18,
        "cells": [
            {"ref": "B6", "val": "Starting Capital: ₹2,00,000 | Risk: ₹500 (0.25%)", "s": 16},
            {"ref": "C6", "val": "", "s": 16},
            {"ref": "D6", "val": "", "s": 16},
            {"ref": "F6", "val": "Net of FYERS Brokerage & Statutory Taxes (STT, GST, Exch, SEBI, Stamp)", "s": 16},
            {"ref": "G6", "val": "", "s": 16},
            {"ref": "H6", "val": "", "s": 16},
            {"ref": "J6", "val": "Target: ≥ 95% | Below 90% = Demotion", "s": 16},
            {"ref": "K6", "val": "", "s": 16},
            {"ref": "L6", "val": "", "s": 16},
        ]
    },
    8: {
        "height": 18,
        "cells": [
            {"ref": "B8", "val": "AVERAGE NET R / TRADE", "s": 12},
            {"ref": "C8", "val": "", "s": 12},
            {"ref": "D8", "val": "", "s": 12},
            {"ref": "F8", "val": "WIN RATE % (TRADES)", "s": 12},
            {"ref": "G8", "val": "", "s": 12},
            {"ref": "H8", "val": "", "s": 12},
            {"ref": "J8", "val": "DISCIPLINE LEAK DETECTOR", "s": 12},
            {"ref": "K8", "val": "", "s": 12},
            {"ref": "L8", "val": "", "s": 12},
        ]
    },
    9: {
        "height": 30,
        "cells": [
            {"ref": "B9", "f": 'IFERROR(AVERAGE(Trade_Log!V2:V50),0)', "val": 0.90, "s": 18},
            {"ref": "C9", "val": "", "s": 18},
            {"ref": "D9", "val": "", "s": 18},
            {"ref": "F9", "f": 'IF(COUNTA(Trade_Log!B2:B50)=0,0,COUNTIF(Trade_Log!W2:W50,"Win")/COUNTA(Trade_Log!B2:B50))', "val": 0.667, "s": 15},
            {"ref": "G9", "val": "", "s": 15},
            {"ref": "H9", "val": "", "s": 15},
            {"ref": "J9", "f": 'COUNTIF(Trade_Log!Y2:Y50,"Y") + COUNTIF(Trade_Log!Z2:Z50,"Revenge")', "val": 0, "s": 13},
            {"ref": "K9", "val": "", "s": 13},
            {"ref": "L9", "val": "", "s": 13},
        ]
    },
    10: {
        "height": 18,
        "cells": [
            {"ref": "B10", "val": "Mathematical Expectancy After Friction", "s": 16},
            {"ref": "C10", "val": "", "s": 16},
            {"ref": "D10", "val": "", "s": 16},
            {"ref": "F10", "val": "Quality 5/5 Execution > Quantity", "s": 16},
            {"ref": "G10", "val": "", "s": 16},
            {"ref": "H10", "val": "", "s": 16},
            {"ref": "J10", "val": "Zero Tolerance for Rule Violations", "s": 16},
            {"ref": "K10", "val": "", "s": 16},
            {"ref": "L10", "val": "", "s": 16},
        ]
    },
    # Section Header: Operational Rules
    12: {
        "height": 24,
        "cells": [
            {"ref": "B12", "val": "EXECUTION BOUNDARIES", "s": 17},
            {"ref": "C12", "val": "", "s": 17},
            {"ref": "D12", "val": "", "s": 17},
            {"ref": "F12", "val": "WIN / LOSS PIE CHART & STATS", "s": 17},
            {"ref": "G12", "val": "", "s": 17},
            {"ref": "H12", "val": "", "s": 17},
            {"ref": "J12", "val": "", "s": 17},
            {"ref": "K12", "val": "", "s": 17},
            {"ref": "L12", "val": "", "s": 17},
        ]
    },
    13: {
        "height": 20,
        "cells": [
            {"ref": "B13", "val": "Trading Window", "s": 7},
            {"ref": "C13", "val": "09:15 to 10:30 AM IST", "s": 9},
            {"ref": "D13", "val": "Locked at 10:30", "s": 0},
            {"ref": "F13", "val": "Wins", "s": 7},
            {"ref": "G13", "f": 'COUNTIF(Trade_Log!W2:W50,"Win")', "val": 2, "s": 5},
            {"ref": "H13", "val": "66.7%", "s": 3},
        ]
    },
    14: {
        "height": 20,
        "cells": [
            {"ref": "B14", "val": "Minimum Planned RR", "s": 7},
            {"ref": "C14", "val": "≥ 2.2 RR", "s": 9},
            {"ref": "D14", "val": "Strict technical target", "s": 0},
            {"ref": "F14", "val": "Losses", "s": 7},
            {"ref": "G14", "f": 'COUNTIF(Trade_Log!W2:W50,"Loss")', "val": 1, "s": 5},
            {"ref": "H14", "val": "33.3%", "s": 3},
        ]
    },
    15: {
        "height": 20,
        "cells": [
            {"ref": "B15", "val": "Broker Kill Switch", "s": 7},
            {"ref": "C15", "val": "ACTIVE / ENFORCED", "s": 9},
            {"ref": "D15", "val": "Locks on 2 losses / 2R", "s": 0},
            {"ref": "F15", "val": "Breakeven", "s": 7},
            {"ref": "G15", "f": 'COUNTIF(Trade_Log!W2:W50,"BE")', "val": 0, "s": 5},
            {"ref": "H15", "val": "0.0%", "s": 3},
        ]
    },
    16: {
        "height": 20,
        "cells": [
            {"ref": "B16", "val": "Loss Cooldown", "s": 7},
            {"ref": "C16", "val": "30 MINUTES", "s": 9},
            {"ref": "D16", "val": "Physical break away", "s": 0},
            {"ref": "F16", "val": "Total Trades", "s": 7},
            {"ref": "G16", "f": 'COUNTA(Trade_Log!B2:B50)', "val": 3, "s": 5},
            {"ref": "H16", "val": "100.0%", "s": 3},
        ]
    },
    17: {
        "height": 20,
        "cells": [
            {"ref": "B17", "val": "Turnover Friction", "s": 7},
            {"ref": "C17", "val": "0.11% OF TURNOVER", "s": 9},
            {"ref": "D17", "val": "Automated in col T", "s": 0},
            {"ref": "F17", "val": "Total Friction", "s": 7},
            {"ref": "G17", "f": 'SUM(Trade_Log!T2:T50)', "val": 1256.97, "s": 4},
            {"ref": "H17", "val": "0.11%", "s": 3},
        ]
    },
    18: {
        "height": 20,
        "cells": [
            {"ref": "B18", "val": "Order Execution", "s": 7},
            {"ref": "C18", "val": "LIMIT ORDERS ONLY", "s": 9},
            {"ref": "D18", "val": "Zero market chasing", "s": 0},
            {"ref": "F18", "val": "Gross P&L", "s": 7},
            {"ref": "G18", "f": 'SUM(Trade_Log!S2:S50)', "val": 1700.00, "s": 4},
            {"ref": "H18", "val": "Gross", "s": 0},
        ]
    },
    20: {
        "height": 24,
        "cells": [
            {"ref": "B20", "val": "RECENT PERFORMANCE AUDIT (DAILY SCORECARD ROLLUP)", "s": 17},
            {"ref": "C20", "val": "", "s": 17},
            {"ref": "D20", "val": "", "s": 17},
            {"ref": "F20", "val": "", "s": 17},
            {"ref": "G20", "val": "", "s": 17},
            {"ref": "H20", "val": "", "s": 17},
            {"ref": "J20", "val": "", "s": 17},
            {"ref": "K20", "val": "", "s": 17},
            {"ref": "L20", "val": "", "s": 17},
        ]
    },
    21: {
        "height": 22,
        "cells": [
            {"ref": "B21", "val": "Date", "s": 1},
            {"ref": "C21", "val": "Trades", "s": 1},
            {"ref": "D21", "val": "Losses", "s": 1},
            {"ref": "F21", "val": "Daily Net P&L", "s": 1},
            {"ref": "G21", "val": "Daily Net R", "s": 1},
            {"ref": "H21", "val": "5/5 Checklist Trades", "s": 1},
            {"ref": "J21", "val": "Rule Violations", "s": 1},
            {"ref": "K21", "val": "Adherence %", "s": 1},
            {"ref": "L21", "val": "Status", "s": 1},
        ]
    },
    22: {
        "height": 20,
        "cells": [
            {"ref": "B22", "f": "Daily_Scorecard!A2", "val": "2026-10-20", "s": 2},
            {"ref": "C22", "f": "Daily_Scorecard!B2", "val": 2, "s": 5},
            {"ref": "D22", "f": "Daily_Scorecard!D2", "val": 1, "s": 5},
            {"ref": "F22", "f": "Daily_Scorecard!F2", "val": -336.76, "s": 4},
            {"ref": "G22", "f": "Daily_Scorecard!G2", "val": -0.67, "s": 19},
            {"ref": "H22", "f": "Daily_Scorecard!H2", "val": 2, "s": 5},
            {"ref": "J22", "f": "Daily_Scorecard!I2", "val": 0, "s": 5},
            {"ref": "K22", "f": "Daily_Scorecard!K2", "val": 1.0, "s": 3},
            {"ref": "L22", "val": "PASS (100%)", "s": 9},
        ]
    },
    23: {
        "height": 20,
        "cells": [
            {"ref": "B23", "f": "Daily_Scorecard!A3", "val": "2026-10-21", "s": 2},
            {"ref": "C23", "f": "Daily_Scorecard!B3", "val": 1, "s": 5},
            {"ref": "D23", "f": "Daily_Scorecard!D3", "val": 0, "s": 5},
            {"ref": "F23", "f": "Daily_Scorecard!F3", "val": 779.79, "s": 4},
            {"ref": "G23", "f": "Daily_Scorecard!G3", "val": 1.56, "s": 19},
            {"ref": "H23", "f": "Daily_Scorecard!H3", "val": 1, "s": 5},
            {"ref": "J23", "f": "Daily_Scorecard!I3", "val": 0, "s": 5},
            {"ref": "K23", "f": "Daily_Scorecard!K3", "val": 1.0, "s": 3},
            {"ref": "L23", "val": "PASS (100%)", "s": 9},
        ]
    },
    24: {
        "height": 20,
        "cells": [
            {"ref": "B24", "val": "Weekly Rollup", "s": 7},
            {"ref": "C24", "f": "Weekly_Review!C2", "val": 3, "s": 5},
            {"ref": "D24", "f": "Weekly_Review!E2", "val": 1, "s": 5},
            {"ref": "F24", "f": "Weekly_Review!G2", "val": 1358.05, "s": 4},
            {"ref": "G24", "f": "Weekly_Review!I2", "val": 0.90, "s": 19},
            {"ref": "H24", "val": "3", "s": 5},
            {"ref": "J24", "f": "Weekly_Review!K2", "val": 0, "s": 5},
            {"ref": "K24", "f": "Weekly_Review!J2", "val": 1.0, "s": 3},
            {"ref": "L24", "val": "ON TRACK FOR GRADUATION", "s": 9},
        ]
    }
}

sheet0_xml = build_sheet_xml(headers=None, rows=[], max_rows=25,
                             col_widths=dash_widths,
                             freeze_panes=False,
                             custom_top_rows=dash_custom_rows,
                             drawing_rId="rId1")

# ==========================================
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

quick_dv_xml = """<dataValidations count="1">
  <dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1" sqref="E3:E50">
    <formula1>&quot;Long,Short&quot;</formula1>
  </dataValidation>
</dataValidations>"""

quick_cf_xml = """<conditionalFormatting sqref="O3:O50">
  <cfRule type="cellIs" dxfId="0" priority="1" operator="equal">
    <formula>&quot;Loss&quot;</formula>
  </cfRule>
  <cfRule type="cellIs" dxfId="1" priority="2" operator="equal">
    <formula>&quot;Win&quot;</formula>
  </cfRule>
</conditionalFormatting>"""

sheet_quick_xml = build_sheet_xml(headers=quick_headers, rows=quick_rows, max_rows=50,
                                  col_widths=quick_widths,
                                  freeze_panes=True,
                                  custom_top_rows=quick_custom_top,
                                  header_style_map=quick_header_map,
                                  data_validations_xml=quick_dv_xml,
                                  conditional_formatting_xml=quick_cf_xml)

# ==========================================
# 2. TRADE_LOG TAB (Full Master Log)
# ==========================================
trade_headers = [
    "Trade_ID","Date","Day","Entry_Time","Symbol","Direction","Setup_Name","Scanner_Alert_Time",
    "HTF_Context_OK","Entry_Planned_NoChase","Stop_Defined_Before_Entry","RR_Planned","Risk_Percent",
    "Risk_Amount","Entry_Price","Stop_Price","Exit_Price","Qty","Gross_PnL","Costs","Net_PnL",
    "R_Multiple","Outcome","Checklist_Score_0to5","Rule_Violation","Violation_Type",
    "Emotion_Before_1to10","Emotion_During_1to10","Emotion_After_1to10","Trade_Valid","Lesson","Screenshot_Link"
]

# Highlight Input columns in Trade_Log
trade_header_map = {
    1: 1, 2: 24, 3: 25, 4: 24, 5: 24, 6: 24, 7: 1, 8: 1,
    9: 1, 10: 1, 11: 1, 12: 25, 13: 25, 14: 25, 15: 24, 16: 24,
    17: 24, 18: 24, 19: 25, 20: 25, 21: 25, 22: 25, 23: 25, 24: 1,
    25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 25, 31: 1, 32: 1
}

trade_rows = []

# Seed 1
trade_rows.append([
    {"val": "T-001 [EXAMPLE]", "s": 5},
    {"val": "2026-10-20", "s": 2},
    {"f": 'IF(B2="","",TEXT(B2,"ddd"))', "val": "Tue", "s": 5},
    {"val": "09:25", "s": 5},
    {"val": "RELIANCE", "s": 5},
    {"val": "Long", "s": 5},
    {"val": "1m Pullback to 9EMA", "s": 0},
    {"val": "09:23", "s": 5},
    {"val": "Y", "s": 5},
    {"val": "Y", "s": 5},
    {"val": "Y", "s": 5},
    {"val": 2.2, "s": 6},
    {"val": 0.0025, "s": 3},
    {"f": 'IF(OR(O2="",P2="",R2=""),"",ABS(O2-P2)*R2)', "val": 500.0, "s": 4},
    {"val": 2500.0, "s": 4},
    {"val": 2495.0, "s": 4},
    {"val": 2511.0, "s": 4},
    {"val": 100, "s": 0},
    {"f": 'IF(OR(O2="",Q2="",R2=""),"",IF(F2="Long",(Q2-O2)*R2,(O2-Q2)*R2))', "val": 1100.0, "s": 4},
    {"f": 'IF(OR(O2="",Q2="",R2=""),"",ROUND((MIN(IF(F2="Long",O2*R2,Q2*R2)*0.0003,20)+MIN(IF(F2="Long",Q2*R2,O2*R2)*0.0003,20))*1.18+IF(F2="Long",Q2*R2,O2*R2)*0.00025+IF(F2="Long",O2*R2,Q2*R2)*0.00003+(O2+Q2)*R2*0.000035164,2))', "val": 135.10, "s": 4},
    {"f": 'IF(S2="","",S2-T2)', "val": 964.90, "s": 4},
    {"f": 'IF(OR(N2="",N2=0,U2=""),"",U2/N2)', "val": 1.93, "s": 6},
    {"f": 'IF(U2="","",IF(U2>0,"Win",IF(U2<0,"Loss","BE")))', "val": "Win", "s": 5},
    {"val": 5, "s": 5},
    {"val": "N", "s": 5},
    {"val": "None", "s": 5},
    {"val": 2, "s": 5},
    {"val": 3, "s": 5},
    {"val": 2, "s": 5},
    {"f": 'IF(OR(X2="",Y2=""),"",IF(AND(X2>=5,Y2="N"),"Y","N"))', "val": "Y", "s": 5},
    {"val": "Followed plan, entry at limit, patient exit at 2.2R target.", "s": 0},
    {"val": "https://tradingview.com/x/example1", "s": 0}
])

# Seed 2
trade_rows.append([
    {"val": "T-002 [EXAMPLE]", "s": 5},
    {"val": "2026-10-20", "s": 2},
    {"f": 'IF(B3="","",TEXT(B3,"ddd"))', "val": "Tue", "s": 5},
    {"val": "10:05", "s": 5},
    {"val": "TCS", "s": 5},
    {"val": "Short", "s": 5},
    {"val": "1m Breakdown Re-test", "s": 0},
    {"val": "10:02", "s": 5},
    {"val": "Y", "s": 5},
    {"val": "Y", "s": 5},
    {"val": "Y", "s": 5},
    {"val": 2.2, "s": 6},
    {"val": 0.0025, "s": 3},
    {"f": 'IF(OR(O3="",P3="",R3=""),"",ABS(O3-P3)*R3)', "val": 500.0, "s": 4},
    {"val": 3500.0, "s": 4},
    {"val": 3510.0, "s": 4},
    {"val": 3510.0, "s": 4},
    {"val": 50, "s": 0},
    {"f": 'IF(OR(O3="",Q3="",R3=""),"",IF(F3="Long",(Q3-O3)*R3,(O3-Q3)*R3))', "val": -500.0, "s": 4},
    {"f": 'IF(OR(O3="",Q3="",R3=""),"",ROUND((MIN(IF(F3="Long",O3*R3,Q3*R3)*0.0003,20)+MIN(IF(F3="Long",Q3*R3,O3*R3)*0.0003,20))*1.18+IF(F3="Long",Q3*R3,O3*R3)*0.00025+IF(F3="Long",O3*R3,Q3*R3)*0.00003+(O3+Q3)*R3*0.000035164,2))', "val": 108.54, "s": 4},
    {"f": 'IF(S3="","",S3-T3)', "val": -608.54, "s": 4},
    {"f": 'IF(OR(N3="",N3=0,U3=""),"",U3/N3)', "val": -1.22, "s": 6},
    {"f": 'IF(U3="","",IF(U3>0,"Win",IF(U3<0,"Loss","BE")))', "val": "Loss", "s": 5},
    {"val": 5, "s": 5},
    {"val": "N", "s": 5},
    {"val": "None", "s": 5},
    {"val": 3, "s": 5},
    {"val": 4, "s": 5},
    {"val": 3, "s": 5},
    {"f": 'IF(OR(X3="",Y3=""),"",IF(AND(X3>=5,Y3="N"),"Y","N"))', "val": "Y", "s": 5},
    {"val": "Setup failed normally; respected stop without hesitation; entered 30m cooldown.", "s": 0},
    {"val": "https://tradingview.com/x/example2", "s": 0}
])

# Seed 3
trade_rows.append([
    {"val": "T-003 [EXAMPLE]", "s": 5},
    {"val": "2026-10-21", "s": 2},
    {"f": 'IF(B4="","",TEXT(B4,"ddd"))', "val": "Wed", "s": 5},
    {"val": "09:40", "s": 5},
    {"val": "INFY", "s": 5},
    {"val": "Long", "s": 5},
    {"val": "1m Momentum Breakout", "s": 0},
    {"val": "09:38", "s": 5},
    {"val": "Y", "s": 5},
    {"val": "Y", "s": 5},
    {"val": "Y", "s": 5},
    {"val": 2.2, "s": 6},
    {"val": 0.0025, "s": 3},
    {"f": 'IF(OR(O4="",P4="",R4=""),"",ABS(O4-P4)*R4)', "val": 500.0, "s": 4},
    {"val": 1450.0, "s": 4},
    {"val": 1445.0, "s": 4},
    {"val": 1461.0, "s": 4},
    {"val": 100, "s": 0},
    {"f": 'IF(OR(O4="",Q4="",R4=""),"",IF(F4="Long",(Q4-O4)*R4,(O4-Q4)*R4))', "val": 1100.0, "s": 4},
    {"f": 'IF(OR(O4="",Q4="",R4=""),"",ROUND((MIN(IF(F4="Long",O4*R4,Q4*R4)*0.0003,20)+MIN(IF(F4="Long",Q4*R4,O4*R4)*0.0003,20))*1.18+IF(F4="Long",Q4*R4,O4*R4)*0.00025+IF(F4="Long",O4*R4,Q4*R4)*0.00003+(O4+Q4)*R4*0.000035164,2))', "val": 98.31, "s": 4},
    {"f": 'IF(S4="","",S4-T4)', "val": 1001.69, "s": 4},
    {"f": 'IF(OR(N4="",N4=0,U4=""),"",U4/N4)', "val": 2.00, "s": 6},
    {"f": 'IF(U4="","",IF(U4>0,"Win",IF(U4<0,"Loss","BE")))', "val": "Win", "s": 5},
    {"val": 5, "s": 5},
    {"val": "N", "s": 5},
    {"val": "None", "s": 5},
    {"val": 2, "s": 5},
    {"val": 3, "s": 5},
    {"val": 2, "s": 5},
    {"f": 'IF(OR(X4="",Y4=""),"",IF(AND(X4>=5,Y4="N"),"Y","N"))', "val": "Y", "s": 5},
    {"val": "Good patience waiting for bar close confirmation. Exited at 2.2R target.", "s": 0},
    {"val": "https://tradingview.com/x/example3", "s": 0}
])

for r in range(5, 51):
    s_norm = 0 if r % 2 == 1 else 20
    s_date = 2 if r % 2 == 1 else 21
    s_curr = 4 if r % 2 == 1 else 22
    s_cntr = 5 if r % 2 == 1 else 23
    trade_rows.append([
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_date},
        {"f": f'IF(B{r}="","",TEXT(B{r},"ddd"))', "val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_norm},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": 6},
        {"val": "", "s": 3},
        {"f": f'IF(OR(O{r}="",P{r}="",R{r}=""),"",ABS(O{r}-P{r})*R{r})', "val": "", "s": s_curr},
        {"val": "", "s": s_curr},
        {"val": "", "s": s_curr},
        {"val": "", "s": s_curr},
        {"val": "", "s": s_norm},
        {"f": f'IF(OR(O{r}="",Q{r}="",R{r}=""),"",IF(F{r}="Long",(Q{r}-O{r})*R{r},(O{r}-Q{r})*R{r}))', "val": "", "s": s_curr},
        {"f": f'IF(OR(O{r}="",Q{r}="",R{r}=""),"",ROUND((MIN(IF(F{r}="Long",O{r}*R{r},Q{r}*R{r})*0.0003,20)+MIN(IF(F{r}="Long",Q{r}*R{r},O{r}*R{r})*0.0003,20))*1.18+IF(F{r}="Long",Q{r}*R{r},O{r}*R{r})*0.00025+IF(F{r}="Long",O{r}*R{r},Q{r}*R{r})*0.00003+(O{r}+Q{r})*R{r}*0.000035164,2))', "val": "", "s": s_curr},
        {"f": f'IF(S{r}="","",S{r}-T{r})', "val": "", "s": s_curr},
        {"f": f'IF(OR(N{r}="",N{r}=0,U{r}=""),"",U{r}/N{r})', "val": "", "s": 6},
        {"f": f'IF(U{r}="","",IF(U{r}>0,"Win",IF(U{r}<0,"Loss","BE")))', "val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"f": f'IF(OR(X{r}="",Y{r}=""),"",IF(AND(X{r}>=5,Y{r}="N"),"Y","N"))', "val": "", "s": s_cntr},
        {"val": "", "s": s_norm},
        {"val": "", "s": s_norm}
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
                             col_widths=trade_widths,
                             header_style_map=trade_header_map)

# ==========================================
# 3. DAILY_SCORECARD TAB
# ==========================================
daily_headers = [
    "Date","Trades_Taken","Max_Trades_Allowed","Losses","Max_Losses_Allowed",
    "Daily_Net_PnL","Daily_R","Checklist_Trades_5of5","Rule_Violations",
    "Adherence_Score_0to5","Adherence_Pct","Hit_Daily_Loss_Limit","Stopped_After_2_Losses","Notes"
]

daily_rows = []
daily_rows.append([
    {"val": "2026-10-20", "s": 2},
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A2)', "val": 2, "s": 5},
    {"val": 2, "s": 5},
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A2,Trade_Log!$W:$W,"Loss")', "val": 1, "s": 5},
    {"val": 2, "s": 5},
    {"f": 'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,$A2)', "val": 356.36, "s": 4},
    {"f": 'SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,$A2)', "val": 0.71, "s": 6},
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A2,Trade_Log!$X:$X,5)', "val": 2, "s": 5},
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A2,Trade_Log!$Y:$Y,"Y")', "val": 0, "s": 5},
    {"val": 5, "s": 5},
    {"f": 'IF(J2="","",J2/5)', "val": 1.0, "s": 3},
    {"val": "N", "s": 5},
    {"val": "N", "s": 5},
    {"val": "[EXAMPLE] 09:15-10:30 window followed. 1 win, 1 loss. Respected 30m cooldown.", "s": 0}
])

daily_rows.append([
    {"val": "2026-10-21", "s": 2},
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A3)', "val": 1, "s": 5},
    {"val": 2, "s": 5},
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A3,Trade_Log!$W:$W,"Loss")', "val": 0, "s": 5},
    {"val": 2, "s": 5},
    {"f": 'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,$A3)', "val": 1001.69, "s": 4},
    {"f": 'SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,$A3)', "val": 2.00, "s": 6},
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A3,Trade_Log!$X:$X,5)', "val": 1, "s": 5},
    {"f": 'COUNTIFS(Trade_Log!$B:$B,$A3,Trade_Log!$Y:$Y,"Y")', "val": 0, "s": 5},
    {"val": 5, "s": 5},
    {"f": 'IF(J3="","",J3/5)', "val": 1.0, "s": 3},
    {"val": "N", "s": 5},
    {"val": "N", "s": 5},
    {"val": "[EXAMPLE] Single A+ trade taken within 09:15-10:30 window. Platform closed.", "s": 0}
])

for r in range(4, 36):
    s_date = 2 if r % 2 == 1 else 21
    s_cntr = 5 if r % 2 == 1 else 23
    s_curr = 4 if r % 2 == 1 else 22
    s_norm = 0 if r % 2 == 1 else 20
    daily_rows.append([
        {"val": "", "s": s_date},
        {"f": f'COUNTIFS(Trade_Log!$B:$B,$A{r})', "val": "", "s": s_cntr},
        {"val": 2, "s": s_cntr},
        {"f": f'COUNTIFS(Trade_Log!$B:$B,$A{r},Trade_Log!$W:$W,"Loss")', "val": "", "s": s_cntr},
        {"val": 2, "s": s_cntr},
        {"f": f'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,$A{r})', "val": "", "s": s_curr},
        {"f": f'SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,$A{r})', "val": "", "s": 6},
        {"f": f'COUNTIFS(Trade_Log!$B:$B,$A{r},Trade_Log!$X:$X,5)', "val": "", "s": s_cntr},
        {"f": f'COUNTIFS(Trade_Log!$B:$B,$A{r},Trade_Log!$Y:$Y,"Y")', "val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"f": f'IF(J{r}="","",J{r}/5)', "val": "", "s": 3},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_norm}
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

# ==========================================
# 4. WEEKLY_REVIEW TAB
# ==========================================
weekly_headers = [
    "Week_Start","Week_End","Trades","Wins","Losses","Win_Rate","Net_PnL","Avg_R",
    "Expectancy_R","Checklist_Adherence_Pct","Violations","Revenge_Trades",
    "Best_Time_Window","Worst_Time_Window","Top_Mistake","Rule_To_Tighten"
]

weekly_rows = []
weekly_rows.append([
    {"val": "2026-10-19", "s": 2},
    {"val": "2026-10-23", "s": 2},
    {"f": 'COUNTIFS(Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2)', "val": 3, "s": 5},
    {"f": 'COUNTIFS(Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2,Trade_Log!$W:$W,"Win")', "val": 2, "s": 5},
    {"f": 'COUNTIFS(Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2,Trade_Log!$W:$W,"Loss")', "val": 1, "s": 5},
    {"f": 'IF(C2=0,"",D2/C2)', "val": 0.667, "s": 3},
    {"f": 'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2)', "val": 1358.05, "s": 4},
    {"f": 'IFERROR(AVERAGEIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2),"")', "val": 0.90, "s": 6},
    {"f": 'IF(C2=0,"",SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2)/C2)', "val": 0.90, "s": 6},
    {"f": 'IF(C2=0,"",COUNTIFS(Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2,Trade_Log!$X:$X,5)/C2)', "val": 1.0, "s": 3},
    {"f": 'COUNTIFS(Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2,Trade_Log!$Y:$Y,"Y")', "val": 0, "s": 5},
    {"f": 'COUNTIFS(Trade_Log!$B:$B,">="&$A2,Trade_Log!$B:$B,"<="&$B2,Trade_Log!$Z:$Z,"Revenge")', "val": 0, "s": 5},
    {"val": "09:15-10:00", "s": 5},
    {"val": "None", "s": 5},
    {"val": "[EXAMPLE] None (100% adherence to 09:15-10:30 window)", "s": 0},
    {"val": "Maintain RR >= 2.2 and 30-min cooldown after any loss", "s": 0}
])

for r in range(3, 10):
    weekly_rows.append([
        {"val": "", "s": 2},
        {"val": "", "s": 2},
        {"f": f'COUNTIFS(Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r})', "val": "", "s": 5},
        {"f": f'COUNTIFS(Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r},Trade_Log!$W:$W,"Win")', "val": "", "s": 5},
        {"f": f'COUNTIFS(Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r},Trade_Log!$W:$W,"Loss")', "val": "", "s": 5},
        {"f": f'IF(C{r}=0,"",D{r}/C{r})', "val": "", "s": 3},
        {"f": f'SUMIFS(Trade_Log!$U:$U,Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r})', "val": "", "s": 4},
        {"f": f'IFERROR(AVERAGEIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r}),"")', "val": "", "s": 6},
        {"f": f'IF(C{r}=0,"",SUMIFS(Trade_Log!$V:$V,Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r})/C{r})', "val": "", "s": 6},
        {"f": f'IF(C{r}=0,"",COUNTIFS(Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r},Trade_Log!$X:$X,5)/C{r})', "val": "", "s": 3},
        {"f": f'COUNTIFS(Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r},Trade_Log!$Y:$Y,"Y")', "val": "", "s": 5},
        {"f": f'COUNTIFS(Trade_Log!$B:$B,">="&$A{r},Trade_Log!$B:$B,"<="&$B{r},Trade_Log!$Z:$Z,"Revenge")', "val": "", "s": 5},
        {"val": "", "s": 5},
        {"val": "", "s": 5},
        {"val": "", "s": 0},
        {"val": "", "s": 0}
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

# ==========================================
# 5. JOURNAL TAB
# ==========================================
journal_headers = [
    "Date","Trade_ID","Symbol","Setup","What_I_Saw","Why_I_Entered",
    "Emotion_Before","Emotion_During","Emotion_After","Rule_Violation",
    "What_I_Did_Well","What_Ill_Do_Differently","Screenshot_Link"
]

journal_rows = []
journal_rows.append([
    {"val": "2026-10-20", "s": 2},
    {"val": "T-001 [EXAMPLE]", "s": 5},
    {"val": "RELIANCE", "s": 5},
    {"val": "1m Pullback to 9EMA", "s": 0},
    {"val": "15m bullish trend. 1m scanner alert at 09:23 inside 09:15-10:30 window. Flag pullback to 9EMA with low volume.", "s": 0},
    {"val": "Bullish pinbar rejection at 9EMA. Limit order placed at 2500, stop 2495 (5 pts risk), target 2511 (2.2R).", "s": 0},
    {"val": 2, "s": 5},
    {"val": 3, "s": 5},
    {"val": 2, "s": 5},
    {"val": "N", "s": 5},
    {"val": "Waited for limit order fill. Respected 2.2R target. Did not market chase.", "s": 0},
    {"val": "Trail stop to breakeven after 1.5R reached.", "s": 0},
    {"val": "https://tradingview.com/x/example1", "s": 0}
])

journal_rows.append([
    {"val": "2026-10-20", "s": 2},
    {"val": "T-002 [EXAMPLE]", "s": 5},
    {"val": "TCS", "s": 5},
    {"val": "1m Breakdown Re-test", "s": 0},
    {"val": "15m downward structure. 1m scanner alerted breakdown at 10:02 inside window. Retest of 3500 level.", "s": 0},
    {"val": "Bearish engulfing on 1m. Stop at 3510 (10 pts), target 3478 (2.2R).", "s": 0},
    {"val": 3, "s": 5},
    {"val": 4, "s": 5},
    {"val": 3, "s": 5},
    {"val": "N", "s": 5},
    {"val": "Accepted loss immediately at stop without widening. Walked away for 30m cooldown.", "s": 0},
    {"val": "Verify sectoral index (IT) alignment before shorting stock.", "s": 0},
    {"val": "https://tradingview.com/x/example2", "s": 0}
])

for r in range(4, 30):
    s_date = 2 if r % 2 == 1 else 21
    s_cntr = 5 if r % 2 == 1 else 23
    s_norm = 0 if r % 2 == 1 else 20
    journal_rows.append([
        {"val": "", "s": s_date},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_norm},
        {"val": "", "s": s_norm},
        {"val": "", "s": s_norm},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_cntr},
        {"val": "", "s": s_norm},
        {"val": "", "s": s_norm},
        {"val": "", "s": s_norm}
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

# ==========================================
# OPENXML DRAWING & CHARTS (Pie & Column Charts)
# ==========================================
chart1_pie_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<c:chartSpace xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <c:chart>
    <c:title>
      <c:tx><c:rich><a:bodyPr/><a:lstStyle/><a:p><a:pPr><a:defRPr b="1" sz="1100"><a:solidFill><a:srgbClr val="0F172A"/></a:solidFill></a:defRPr></a:pPr><a:r><a:t>Win / Loss Distribution</a:t></a:r></a:p></c:rich></c:tx>
      <c:overlay val="0"/>
    </c:title>
    <c:plotArea>
      <c:layout/>
      <c:pieChart>
        <c:varyColors val="1"/>
        <c:ser>
          <c:idx val="0"/>
          <c:order val="0"/>
          <c:tx><c:v>Outcomes</c:v></c:tx>
          <c:cat>
            <c:strLit>
              <c:ptCount val="2"/>
              <c:pt idx="0"><c:v>Wins (67%)</c:v></c:pt>
              <c:pt idx="1"><c:v>Losses (33%)</c:v></c:pt>
            </c:strLit>
          </c:cat>
          <c:val>
            <c:numLit>
              <c:ptCount val="2"/>
              <c:pt idx="0"><c:v>2</c:v></c:pt>
              <c:pt idx="1"><c:v>1</c:v></c:pt>
            </c:numLit>
          </c:val>
        </c:ser>
      </c:pieChart>
    </c:plotArea>
    <c:legend>
      <c:legendPos val="b"/>
      <c:overlay val="0"/>
    </c:legend>
  </c:chart>
</c:chartSpace>"""

drawing_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<xdr:wsDr xmlns:xdr="http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <xdr:twoCellAnchor>
    <xdr:from><xdr:col>8</xdr:col><xdr:colOff>50000</xdr:colOff><xdr:row>12</xdr:row><xdr:rowOff>50000</xdr:rowOff></xdr:from>
    <xdr:to><xdr:col>12</xdr:col><xdr:colOff>50000</xdr:colOff><xdr:row>19</xdr:row><xdr:rowOff>150000</xdr:rowOff></xdr:to>
    <xdr:graphicFrame macro="">
      <xdr:nvGraphicFramePr>
        <xdr:cNvPr id="2" name="PieChart1"/>
        <xdr:cNvGraphicFramePr/>
      </xdr:nvGraphicFramePr>
      <xdr:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/></xdr:xfrm>
      <a:graphic>
        <a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/chart">
          <c:chart xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart" r:id="rId1"/>
        </a:graphicData>
      </a:graphic>
    </xdr:graphicFrame>
    <xdr:clientData/>
  </xdr:twoCellAnchor>
</xdr:wsDr>"""

drawing_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/chart" Target="../charts/chart1.xml"/>
</Relationships>"""

sheet1_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/drawing" Target="../drawings/drawing1.xml"/>
</Relationships>"""

# Packaging into .xlsx
content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet3.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet4.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet5.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet6.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
  <Override PartName="/xl/sharedStrings.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"/>
  <Override PartName="/xl/drawings/drawing1.xml" ContentType="application/vnd.openxmlformats-officedocument.drawing+xml"/>
  <Override PartName="/xl/charts/chart1.xml" ContentType="application/vnd.openxmlformats-officedocument.drawingml.chart+xml"/>
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
  <Relationship Id="rId5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet5.xml"/>
  <Relationship Id="rId6" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet6.xml"/>
  <Relationship Id="rId7" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId8" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings" Target="sharedStrings.xml"/>
</Relationships>"""

workbook_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="Dashboard" sheetId="1" r:id="rId1"/>
    <sheet name="Quick_Log" sheetId="2" r:id="rId2"/>
    <sheet name="Trade_Log" sheetId="3" r:id="rId3"/>
    <sheet name="Daily_Scorecard" sheetId="4" r:id="rId4"/>
    <sheet name="Weekly_Review" sheetId="5" r:id="rId5"/>
    <sheet name="Journal" sheetId="6" r:id="rId6"/>
  </sheets>
</workbook>"""

out_path = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D3_Tracking_Spreadsheet.xlsx"
sst_xml = sst.to_xml()

with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml', content_types)
    z.writestr('_rels/.rels', root_rels)
    z.writestr('xl/_rels/workbook.xml.rels', wb_rels)
    z.writestr('xl/workbook.xml', workbook_xml)
    z.writestr('xl/styles.xml', styles_xml)
    z.writestr('xl/sharedStrings.xml', sst_xml)
    z.writestr('xl/worksheets/_rels/sheet1.xml.rels', sheet1_rels)
    z.writestr('xl/worksheets/sheet1.xml', sheet0_xml) # Dashboard
    z.writestr('xl/worksheets/sheet2.xml', sheet_quick_xml) # Quick_Log (Fast Entry)
    z.writestr('xl/worksheets/sheet3.xml', sheet1_xml) # Trade_Log (Master)
    z.writestr('xl/worksheets/sheet4.xml', sheet2_xml) # Daily_Scorecard
    z.writestr('xl/worksheets/sheet5.xml', sheet3_xml) # Weekly_Review
    z.writestr('xl/worksheets/sheet6.xml', sheet4_xml) # Journal
    z.writestr('xl/drawings/drawing1.xml', drawing_xml)
    z.writestr('xl/drawings/_rels/drawing1.xml.rels', drawing_rels)
    z.writestr('xl/charts/chart1.xml', chart1_pie_xml)

print(f"Spreadsheet V2 with Charts and Quick_Log generated successfully at: {out_path}")
