#!/usr/bin/env python3
"""Wandelt die Excel-Packliste in data.json um.

Aufruf:  python3 excel_to_json.py Reisepackliste.xlsx
Voraussetzung:  pip install openpyxl

Regeln (passend zu eurer Excel):
- Zeile 3 enthält die Kategorie-Überschriften (Kleider, Schuhe, ...).
- Darunter stehen die Gegenstände in derselben Spalte (Leerzeilen werden ignoriert).
- Leerzeilen trennen Bereiche (Feld "g"); die App zeigt dort einen Abstand.
- Zellen MIT Füllfarbe (orange) = nur Tanja. Zellen ohne Füllfarbe = alle.
- Kategorien in KERN sind immer dabei, die anderen sind zuschaltbare Module.
"""
import json, re, sys
from openpyxl import load_workbook

HEADER_ROW = 3
# Überschrift in Excel -> (id, Typ, Modul-Schalter)
KATEGORIEN = {
    "Kleider": ("kleider", "core"), "Schuhe": ("schuhe", "core"),
    "Necessaire": ("necessaire", "core"), "Dokumente": ("dokumente", "core"),
    "Elektronik": ("elektronik", "core"), "Verschiedenes": ("verschiedenes", "core"),
    "Kinder": ("kinder", "kinder"), "Outdoor / Wandern": ("outdoor", "outdoor"),
    "Ferienwohnungen": ("ferienwohnung", "ferienwohnung"), "Camping": ("camping", "camping"),
}

def slug(s):
    s = s.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

def hat_fuellung(cell):
    f = cell.fill
    return bool(f and f.fill_type == "solid" and f.fgColor is not None
                and f.fgColor.rgb not in ("00000000", "FFFFFFFF"))

def main(pfad):
    ws = load_workbook(pfad).worksheets[0]
    kategorien = []
    for cell in ws[HEADER_ROW]:
        name = (str(cell.value).strip() if cell.value else "")
        if name not in KATEGORIEN:
            continue
        cid, modul = KATEGORIEN[name]
        items, gesehen = [], {}
        block, vorher_leer = 0, False   # Leerzeilen trennen Bereiche (Block 0, 1, 2, ...)
        for r in range(HEADER_ROW + 1, ws.max_row + 1):
            c = ws.cell(row=r, column=cell.column)
            if c.value is None or not str(c.value).strip():
                vorher_leer = bool(items)   # führende Leerzeilen zählen nicht
                continue
            if vorher_leer:
                block += 1
                vorher_leer = False
            text = str(c.value).strip()
            basis = f"{cid}-{slug(text)}"          # stabile ID: bleibt gleich, solange der Name gleich bleibt
            gesehen[basis] = gesehen.get(basis, 0) + 1
            iid = basis if gesehen[basis] == 1 else f"{basis}-{gesehen[basis]}"
            items.append({"id": iid, "name": text, "tanja": hat_fuellung(c), "g": block})
        kategorien.append({"id": cid, "name": name, "module": None if modul == "core" else modul, "items": items})
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump({"categories": kategorien}, f, ensure_ascii=False, indent=1)
    print(f"{len(kategorien)} Kategorien, {sum(len(k['items']) for k in kategorien)} Einträge -> data.json")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "Reisepackliste.xlsx")
