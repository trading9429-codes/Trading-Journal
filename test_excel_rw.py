import zipfile
import xml.etree.ElementTree as ET

xlsx_path = "/home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/D3_Tracking_Spreadsheet.xlsx"

with zipfile.ZipFile(xlsx_path, 'r') as z:
    print("Files in xlsx:")
    for name in z.namelist():
        if "sheet" in name or "shared" in name:
            print(" -", name)
            
    sst_xml = z.read("xl/sharedStrings.xml").decode()
    sst_tree = ET.fromstring(sst_xml)
    shared_strings = [elem.text or "" for elem in sst_tree.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t")]
    print(f"Loaded {len(shared_strings)} shared strings.")
    print("Sample strings:", shared_strings[:10])
