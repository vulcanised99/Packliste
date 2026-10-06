# Reisepackliste (PWA)

Reine HTML/CSS/JavaScript-App ohne Build-Schritt für das iPhone (Safari, «Zum Home-Bildschirm»), läuft offline.

Dateien (alle im Hauptverzeichnis, ohne Unterordner): `index.html` (App), `data.json` (Packliste), `manifest.webmanifest`, `sw.js` (Service Worker), `excel_to_json.py`, `app-icon-180.png`, `app-icon-192.png`, `app-icon-512.png`.

## Liste aktualisieren
1. Excel anpassen (gleiche Struktur: Kategorien in Zeile 3, Gegenstände darunter, Leerzeile = Abstand in der App, orange gefüllte Zelle = nur Tanja).
2. Einmalig `pip install openpyxl`, dann `python3 excel_to_json.py MeineListe.xlsx`.
   Das Skript warnt, wenn eine Spalte in Zeile 3 nicht erkannt wird oder eine erwartete Kategorie fehlt.
3. Neue `data.json` auf GitHub hochladen (Add file > Upload files). Häkchen bleiben erhalten, solange der Name eines Eintrags und seine Kategorie gleich bleiben.
4. In `sw.js` die `VERSION` erhöhen, wenn sich Dateien geändert haben, und `sw.js` ebenfalls hochladen.

Neue Kategorie hinzufügen: Überschrift in Excel-Zeile 3 eintragen und im Dictionary `KATEGORIEN` in `excel_to_json.py` ergänzen. Soll sie per Schalter zuschaltbar sein, muss der Schalter zusätzlich in `index.html` (`SWITCHES`, `DEFAULTS`) ergänzt werden.

## Bedienung
Tippen auf einen Eintrag wechselt den Zustand: 1x ✓ eingepackt, 2x ✕ für diese Reise unnötig, 3x wieder offen. Beide Zustände zählen als erledigt. «Alle Häkchen zurücksetzen» löscht die Häkchen, eigene Einträge bleiben erhalten.

## Veröffentlichen (GitHub Pages)
Das Repo ist öffentlich und über GitHub Pages gehostet. Auf dem iPhone die Adresse in **Safari** öffnen, Teilen-Symbol, «Zum Home-Bildschirm».

Hinweis: Die Seite ist für alle erreichbar, die die Adresse kennen. Die Häkchen werden pro Gerät im localStorage gespeichert und nicht zwischen Geräten synchronisiert.

## Updates
Die App zeigt zuerst die gespeicherte Version und holt die neue im Hintergrund. Eine Änderung ist deshalb oft erst nach dem zweiten Öffnen (bzw. nach dem vollständigen Schliessen der App) sichtbar.

## Lokal testen
`python3 -m http.server 8000` im Projektordner, dann http://localhost:8000 öffnen.
