# Reisepackliste (PWA)

Dateien: `index.html` (App), `data.json` (Packliste), `manifest.webmanifest`, `sw.js`, `icons/`, `excel_to_json.py`.

## Liste aktualisieren
1. Excel anpassen (gleiche Struktur: Überschriften in Zeile 3, orange = nur Tanja).
2. `pip install openpyxl` (einmalig), dann `python3 excel_to_json.py MeineListe.xlsx`
3. Neue `data.json` ins Repo hochladen. Häkchen bleiben erhalten, solange der Name eines Eintrags gleich bleibt.

## Lokal testen
`python3 -m http.server 8000` im Ordner, dann http://localhost:8000 öffnen.

## Veröffentlichen (Cloudflare Pages, kostenlos, privates Repo möglich)
1. Auf github.com: New repository → Private → alle Dateien hochladen (Add file → Upload files, Ordner `icons` mitnehmen).
2. dash.cloudflare.com → Workers & Pages → Create → Pages → Connect to Git → Repo wählen.
3. Build command leer lassen, Output directory `/` → Deploy. Du erhältst eine Adresse wie `packliste.pages.dev`.
4. iPhone: Adresse in **Safari** öffnen → Teilen-Symbol → «Zum Home-Bildschirm».

Hinweis: Die Webseite ist unter der Adresse für alle erreichbar, die sie kennen (auch bei privatem Repo). Cloudflare Access kann das bei Bedarf absichern.
Die Häkchen werden pro Gerät gespeichert, nicht zwischen den iPhones synchronisiert.
