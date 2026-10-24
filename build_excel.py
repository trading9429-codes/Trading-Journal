import zipfile
import html
import os

def escape_xml(s):
    if s is None:
        return ""
    return html.escape(str(s))

def col_letter(col_idx):
    """1-based col_idx to Excel column letter (1 -> A, 27 -> AA)"""
    result = ""
    while col_idx > 0:
        col_idx, remainder = divmod(col_idx - 1, 26)
        result = chr(65 + remainder) + result
    return result

def make_cell(ref, val=None, formula=None, style_id=None, cell_type=None):
    s_attr = f' s="{style_id}"' if style_id is not None else ""
    if formula is not None:
        f_xml = f'<f>{escape_xml(formula)}</f>'
        v_xml = f'<v>{escape_xml(val)}</v>' if val is not None else '<v></v>'
        return f'<c r="{ref}"{s_attr}>{f_xml}{v_xml}</c>'
    elif val is None or val == "":
        return f'<c r="{ref}"{s_attr}/>'
    elif cell_type == "s" or isinstance(val, str):
        # inline string
        return f'<c r="{ref}"{s_attr} t="inlineStr"><is><t>{escape_xml(val)}</t></is></c>'
    elif isinstance(val, (int, float)):
        return f'<c r="{ref}"{s_attr}><v>{val}</v></c>'
    else:
        return f'<c r="{ref}"{s_attr} t="inlineStr"><is><t>{escape_xml(str(val))}</t></is></c>'

# Let's define the styles XML
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
    <!-- 0: Standard normal -->
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1"/>
    <!-- 1: Header (Navy bold white) -->
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
    <!-- 4: Currency / Two decimal (0.00) -->
    <xf numFmtId="166" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="right" vertical="center"/>
    </xf>
    <!-- 5: Center aligned normal -->
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
    <!-- 6: Number 2 decimal (0.00) -->
    <xf numFmtId="167" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="right" vertical="center"/>
    </xf>
    <!-- 7: Bold Normal -->
    <xf numFmtId="0" fontId="2" fillId="0" borderId="1" xfId="0" applyFont="1" applyBorder="1"/>
    <!-- 8: Subheader / Section header -->
    <xf numFmtId="0" fontId="2" fillId="6" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1"/>
    <!-- 9: Center aligned bold -->
    <xf numFmtId="0" fontId="2" fillId="0" borderId="1" xfId="0" applyFont="1" applyBorder="1" applyAlignment="1">
      <alignment horizontal="center" vertical="center"/>
    </xf>
  </cellXfs>
  <dxfs count="4">
    <!-- dxf 0: Red fill, dark red text -->
    <dxf>
      <font><color rgb="FF9C0006"/><b/></font>
      <fill><patternFill><bgColor rgb="FFFFC7CE"/></patternFill></fill>
    </dxf>
    <!-- dxf 1: Green fill, dark green text -->
    <dxf>
      <font><color rgb="FF006100"/><b/></font>
      <fill><patternFill><bgColor rgb="FFC6EFCE"/></patternFill></fill>
    </dxf>
    <!-- dxf 2: Orange fill, dark orange text -->
    <dxf>
      <font><color rgb="FF9C6500"/><b/></font>
      <fill><patternFill><bgColor rgb="FFFFEB9C"/></patternFill></fill>
    </dxf>
    <!-- dxf 3: Light gray fill -->
    <dxf>
      <fill><patternFill><bgColor rgb="FFF2F2F2"/></patternFill></fill>
    </dxf>
  </dxfs>
</styleSheet>"""

def build_sheet_xml(headers, rows, max_rows=100, data_validations_xml="", conditional_formatting_xml="", col_widths=None):
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
    
    # Row 1: Headers
    header_cells = []
    for c_idx, h in enumerate(headers, 1):
        ref = f"{col_letter(c_idx)}1"
        header_cells.append(make_cell(ref, val=h, style_id=1, cell_type="s"))
    xml_parts.append(f'<row r="1" ht="28" customHeight="1">{"".join(header_cells)}</row>')
    
    # Data Rows
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

print("Helper defined successfully")
