# Home Assistant

`vitocal-dashboard.yaml` ist eine fertige Lovelace-View für die Sensoren aus
`vitocal-live.yaml`.

## Einbauen

1. Dashboard öffnen → Stift-Symbol → **Raw Configuration Editor**
2. Inhalt unter `views:` einfügen (die Datei enthält eine View, kein komplettes Dashboard)
3. Speichern

Die Entity-IDs entstehen aus dem ESPHome-Gerätenamen (`Vitocal Optolink`) plus dem
Sensornamen. Weichen sie ab, in **Einstellungen → Geräte & Dienste → ESPHome** die
tatsächlichen IDs prüfen.

## Noch nicht enthalten

- **Störungs-Binärsensor** (`0x0491` Sammelstörung) — die Bedeutung der Werte `02`/`00`
  ist noch nicht verifiziert. Erst einbauen, wenn klar ist, welcher Wert „Störung aktiv"
  bedeutet.
- **Druck-Warnung** — der Heizkreis-Druck ist mechanisch (Manometer), kein Datenpunkt.
