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

## Entity-ID-Präfix

Home Assistant stellt dem Gerätenamen das Area-Kürzel voran. Im Referenzaufbau heißt
das Präfix `hwr_eg_` (Heizungsraum, Erdgeschoss):

```
sensor.hwr_eg_vitocal_optolink_kesseltemperatur
```

Bei anderer Area-Zuordnung weicht das Präfix ab — die tatsächlichen IDs stehen unter
**Einstellungen → Geräte & Dienste → ESPHome → Vitocal Optolink**.

## Stoerungs-Helper

Die Bits sind maskiert (`bit_mask: 1` = Bit 0). `esphome_vitoconnect` kann keine
Bitmasken, deshalb liefern die ESPHome-Sensoren den Rohwert und Home Assistant
wertet ihn aus. Zwei Template-Helper sind angelegt:

| Helper | Quelle | Ausdruck |
|---|---|---|
| `binary_sensor.vitocal_sammelstoerung` | `sensor.hwr_eg_vitocal_optolink_status_sammelstoerung_roh` | `{{ (states(...) \| int(0)) % 2 == 1 }}` |
| `binary_sensor.vitocal_stoerung_folge_wp` | `sensor.hwr_eg_vitocal_optolink_status_folgewp_roh` | dito |

Modulo statt Bitwise-AND, weil Jinja in HA-Templates `&` nicht akzeptiert.
Beide sind im Normalbetrieb `off` (Rohwert 2, Bit 0 = 0).
