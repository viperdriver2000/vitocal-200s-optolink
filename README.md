# Vitocal 200-S — lokales Auslesen über Optolink

Lokaler, cloudfreier Zugriff auf eine **Viessmann Vitocal 200-S** (Regler
`CU401B_S`, Geräte-ID `0x204D`, Typ WO1C) über die optische Optolink-Schnittstelle.
Selbstgebauter IR-Kopf am ESP8266, eingebunden in Home Assistant via ESPHome.

Entstanden aus einem realen Aufbau im November 2026. Der Wert dieses Repos liegt
weniger in der Schaltung — die ist bekannt — als in der **Adresstabelle für
Firmware-Stand 0x41**, die in keinem öffentlichen Katalog enthalten ist.

## Was es kann

- Temperaturen lesen: Außentemperatur, Warmwasser, Vorlauf primär/sekundär,
  Rücklauf, Heißgas
- Zähler lesen: Betriebsstunden und Einschaltungen des Verdichters
- Status-Bits lesen: Sammelstörung, EVU-Sperre, Motorschutz, Pumpen, E-Heizung

## Was es nicht kann

- **Keine Bedienung.** `esphome_vitoconnect` ist ein reines Lesemodul — keine
  Sollwerte, keine Betriebsart, kein Warmwasser-Push.

## Aufbau

```
bench.yaml              LED- und Empfängertest ohne Heizung
vitocal-live.yaml       die nutzbare Konfiguration (ESP8266, nur lesen)
vitocal-vitohome.yaml   Alternative fuer ESP32 mit Schreibmoeglichkeit
scan.yaml               Adress-Scanner (Bereich per globals einstellbar)
scan-overnight.yaml     Voller Bereichsscan, loggt nur Treffer
tools/parse_scan.py     wertet Scan-Logs aus
docs/hardware.md        Schaltplan, Pinout, Fallstricke
docs/crc.md             P300-Frame-Format und Checksumme
docs/adressen-*.md      gescannte Adressbereiche mit Belegung
```

## Schnellstart

```bash
cp secrets.yaml.example secrets.yaml   # WLAN eintragen
esphome run bench.yaml                 # erst LED-Test, dann an die Heizung
esphome run vitocal-live.yaml
```

Benötigt das Component [`dannerph/esphome_vitoconnect`](https://github.com/dannerph/esphome_vitoconnect)
(MIT), wird per `external_components` automatisch geladen. Für den ersten Flash
werden Git und der CH340-Treiber benötigt.

## Wichtig beim Flashen

Vor dem Flash über USB die Litzen von GPIO1/GPIO3 abziehen — der Fototransistor
blockiert sonst die Flash-Daten. Danach nur noch OTA.

## Adressen

Die Messwerte liegen bei **`0x0880`–`0x0897`** und fehlen in den Vitosoft-Exporten.
Details, inklusive der Sentinel-Werte für „nicht verfügbar", in
[`docs/adressen-cu401b-sw41.md`](docs/adressen-cu401b-sw41.md).

Scan-Log auswerten:

```bash
python3 tools/parse_scan.py scan.log --min 0x0880 --max 0x0897 --raw
```

## vitoconnect oder vitohome?

| | **vitoconnect** (dannerph) | **vitohome** (SoulSolistice) |
|---|---|---|
| Lizenz | MIT | GPL-3.0 |
| Board | ESP8266 **und** ESP32 | **nur ESP32** |
| Protokolle | P300, KW, GWG | P300, KW, GWG |
| `sensor` / `binary_sensor` | ✓ | ✓ |
| `text_sensor` (inkl. Fehlerhistorie) | ✗ | ✓ |
| `number` / `select` / `switch` | ✗ | ✓ |
| `climate` / `water_heater` | ✗ | ✓ |
| Schreibzugriff | nein | ja (EEPROM-Verschleiß) |
| Zeitsync zum Regler | ✗ | ✓ |
| Katalog-Generator | ✗ | ✓ |

Faustregel: **vitoconnect** für schlankes Lesen auf ESP8266, **vitohome** wenn
Bedienung gebraucht wird — dann ESP32 und seltene Schreibzugriffe.

## Quellen und Danksagung

- [`dannerph/esphome_vitoconnect`](https://github.com/dannerph/esphome_vitoconnect) — ESPHome-Component (MIT)
- [`SoulSolistice/esphome_vitohome`](https://github.com/SoulSolistice/esphome_vitohome) — Kataloge und Referenz (GPL-3.0, nur verlinkt)
- [`openv/openv`](https://github.com/openv/openv) — Wiki mit Adresslisten und Protokolldoku
- Viessmann, Vitocal, Optolink sind Marken der Viessmann Group. Dieses Projekt steht
  in keiner Verbindung zu Viessmann.

## Lizenz

MIT — siehe [LICENSE](LICENSE). Keine Inhalte aus GPL-Projekten eingebettet.
