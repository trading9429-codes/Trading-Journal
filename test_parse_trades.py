import zipfile
import xml.etree.ElementTree as ET

xlsx_path = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D3_Tracking_Spreadsheet.xlsx"

def col_from_ref(ref):
    return "".join([c for c in ref if c.isalpha()])

def row_from_ref(ref):
    return int("".join([c for c in ref if c.isdigit()]))

with zipfile.ZipFile(xlsx_path, 'r') as z:
    sst_xml = z.read("xl/sharedStrings.xml").decode()
    sst_tree = ET.fromstring(sst_xml)
    sst = [elem.text or "" for elem in sst_tree.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t")]
    
    sheet3_xml = z.read("xl/worksheets/sheet3.xml").decode()
    tree = ET.fromstring(sheet3_xml)
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    
    rows = tree.findall(".//m:row", ns)
    print("Found rows in Trade_Log:", len(rows))
    
    for r in rows[:6]:
        row_num = r.attrib.get("r")
        cells = {}
        for c in r.findall("m:c", ns):
            ref = c.attrib.get("r")
            col = col_from_ref(ref)
            cell_type = c.attrib.get("t")
            v_elem = c.find("m:v", ns)
            v_val = v_elem.text if v_elem is not None else ""
            if cell_type == "s" and v_val.isdigit():
                val = sst[int(v_val)]
            else:
                val = v_val
            cells[col] = val
        if cells.get("A") and "Trade_ID" not in cells.get("A"):
            print(f"Row {row_num}: ID={cells.get('A')}, Date={cells.get('B')}, Symbol={cells.get('E')}, Dir={cells.get('F')}, NetPnL={cells.get('U')}, NetR={cells.get('V')}, Outcome={cells.get('W')}")
