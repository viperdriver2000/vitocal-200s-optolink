# Adressen — Vitocal 200-S, CU401B_S, SW 0x41
Empirisch durch Adress-Scans ermittelt (November 2026).
Gerät: `0x204D` = CU401B_S (Vitotronic 200, Typ WO1C), HW 0x01, SW 0x41.
Scan-Methode: `scan.yaml`, P300-Read mit Länge 2, Bereichsweise.

## Messwerte — 0x0880 bis 0x0897
Diese Adressen stehen in **keinem** der öffentlichen Kataloge (Vitosoft-Export
für 0x204D enthält sie nicht). Skalierung: signed int16 / 10.

| Adresse | Roh | Wert | Bedeutung (verifiziert durch Verlauf) |
|---|---|---|---|
| 0x0880 | `53 00` | 8.3 | Außentemperatur (fällt nachts) |
| 0x0881 | `DC FD` | -54.8 | nicht verfügbar |
| 0x0882 | `C6 01` | 45.4 | Warmwasser (stabil) |
| 0x0883 | `DC FD` | -54.8 | nicht verfügbar |
| 0x0884 | `06 F5` | -281.0 | nicht verfügbar |
| 0x0885 | `DC FD` | -54.8 |  |
| 0x0886 | `DC FD` | -54.8 |  |
| 0x0887 | `DC FD` | -54.8 |  |
| 0x0888 | `DC FD` | -54.8 |  |
| 0x0889 | `DC FD` | -54.8 |  |
| 0x088A | `DB FD` | -54.9 |  |
| 0x088B | `DC FD` | -54.8 |  |
| 0x088C | `DC FD` | -54.8 |  |
| 0x088D | `67 19` | 650.3 | unbekannt, konstant 650.3 |
| 0x088E | `AE 0B` | 299.0 | Druck Kältemittel (Hypothese, konstant 29.9) |
| 0x088F | `35 01` | 30.9 | Vorlauf primär (steigt im Heizbetrieb) |
| 0x0890 | `38 01` | 31.2 | Vorlauf sekundär (steigt) |
| 0x0891 | `37 01` | 31.1 | Rücklauf (steigt) |
| 0x0892 | `AE 0B` | 299.0 | unbekannt, konstant 299.0 |
| 0x0893 | `4F 01` | 33.5 | Heißgas (schwankt mit Verdichter) |
| 0x0894 | `35 01` | 30.9 | Rücklauf 2 (steigt) |
| 0x0895 | `AE 0B` | 299.0 | unbekannt, konstant 299.0 |
| 0x0896 | `66 19` | 650.2 | unbekannt, konstant 650.2 |
| 0x0897 | `18 F5` | -279.2 | nicht verfügbar |

**Sentinel für „nicht verfügbar":** `DC FD` = −548 (−54,8 °C), `18 F5` = −2792 (−279,2 °C).
Ein Sensor, der dauerhaft einen dieser Werte liefert, ist nicht angeschlossen.

## Status-Bits (binary) — 0x03C0 bis 0x04BE
Länge 1 Byte, Wert `02` = aktiv, `00` = inaktiv. Auszug der belegten Adressen:

| Adresse | Roh | Bedeutung |
|---|---|---|
| 0x03C1 | `00 02` | Strömungswächter |
| 0x03C3 | `00 02` | EVU-Sperre |
| 0x03C7 | `00 02` | Sicherheitshochdruck Verdichter |
| 0x03C9 | `00 02` | Regelhochdruck Verdichter |
| 0x03CB | `00 02` | Niederdruck Verdichter |
| 0x03CD | `02 02` | Motorschutz Verdichter |
| 0x03D8 | `02 02` | Störung Folge-WP |
| 0x0488 | `00 00` | E-Heizung Stufe 1 |
| 0x0489 | `00 02` | E-Heizung Stufe 2 |
| 0x048D | `01 02` | Heizkreispumpe HK1 |
| 0x0491 | `02 02` | Sammelstörung |
| 0x0496 | `02 02` | Speicherladepumpe |

## Zähler
| Adresse | Länge | Bedeutung | Beispiel |
|---|---|---|---|
| 0x0580 | 4 | Betriebsstunden Verdichter (Sekunden) | 30.193.089 s = 8387 h |
| 0x0501 | 4 | Einschaltungen Verdichter | 0 |

## Nicht belegt
| Bereich | Ergebnis |
|---|---|
| 0x0000–0x00FF | 59 Antworten, nur System- und ID-Adressen (0xF7–0xFE) |
| 0x0100–0x01FF | fast ausschließlich Fehler 3; Katalogadressen 0x01C1/0x01CB/0x01CD existieren hier **nicht** |
| 0x0200–0x07FF | 299 Antworten: Korrekturwerte, Gradienten, Status-Bits, Ausstattungsmerkmale — keine Messwerte |
| 0x7000–0x70FF | 1 Antwort (0x7000), sonst Fehler 3 |

---

## Voller Scan 0x0900–0xFFFF

Durchgeführt November 2026, 63.232 Adressen, 600 ms Abstand, Laufzeit ~10,5 h.
Gefiltert auf Erfolgs-Frames; zwei Durchläufe zum Abgleich.

**Ergebnis:** 2143 belegte Adressen, davon **28 mit wechselnden Werten** zwischen den
Durchläufen. Wechselnde Werte sind der verlässlichste Beleg für echte Messwerte —
Konfigurationsregister bleiben konstant.

### Belegte Blöcke

| Block | Adressen |
|---|---|
| 0x0900–0x09FF | 192 |
| 0x1300–0x13FF | 89 |
| 0x1600–0x16FF | 33 |
| 0x1800–0x18FF | 33 |
| 0x1A00–0x1AFF | 133 |
| 0x2000 / 0x3000 / 0x4000 | je 27 |
| 0x5000–0x5400 | 368 |
| 0x5A00–0x5B00 | 118 |
| 0x7000–0x7E00 | ~500 |
| 0xA000–0xA4FF | 43 |
| 0xB000–0xB4FF | 131 |
| 0xFD00–0xFDFF | 255 (Systembereich) |

### Messwerte mit Namen (aus dem Katalog bestätigt)

| Adresse | Name | Skalierung | Beispiel |
|---|---|---|---|
| 0xA309 | Kesseltemperatur | ÷100 | 36,50 °C |
| 0xA393 | Anlagenvorlauf-Kessel-Isttemperatur | ÷100 | 33,60 °C |
| 0xA307 | effektive Kessellsolltemperatur | ÷100 | 32,50 °C |
| 0xA391 | Aktiver Anlagen-/Solltemperaturwert | ÷100 | 32,50 °C |
| 0x16B2 | Mittlere sek. Vorlauftemperatur | ÷10 | 31,1 °C |
| 0x16B3 | Mittlere sek. Rücklauftemperatur RL1 | ÷10 | 30,8 °C |
| 0x16B0 | Mittlere primäre Eingangstemperatur | ÷10 | 3,3 °C |
| 0x16B1 | Mittlere primäre Ausgangstemperatur | ÷10 | 2,8 °C |
| 0x16C0 | Max. sek. Vorlauftemperatur Heizen | ÷10 | 37,7 °C |
| 0x16C2 | Max. sek. Rücklauftemperatur Heizen RL1 | ÷10 | 34,2 °C |
| 0x1800 | Vorlauftemp. Soll HK1 | ÷10 | 32,2 °C |
| 0x1804 | Anlagenvorlauf Solltemperatur | ÷10 | 32,2 °C |
| 0x1690 | COP Verdichter 1 | ÷10 | 5,6 |
| 0x1684 | JAZ incl. PV | ÷10 | (Wert 0 = nv) |
| 0xB420 | Drehzahl Primärquelle | % | 0–25 |
| 0x1624 | Belastungsklasse 3 Verdichter | h | 3038–3039 |
| 0x130A | Zustandsautomat WP1 | — | 768 / 0 |
| 0x1372 | Timer OPT Laufzeit WP1 | s | 5 |
| 0x1374 | Timer Sperrzeit WP1 | s | 186 |
| 0x1375 | Timer Abtauung WP1 | s | 1193 |

### Dynamisch, aber nicht im Katalog

| Adresse | Werte | Hypothese |
|---|---|---|
| 0xA14F | 240 → 140 | unbekannt |
| 0xA152 | 8224 → 8354 | unbekannt |
| 0xA3C3 | 4570 → 4520 | 45,7 → 45,2 °C (Warmwasser?) |
| 0xBF80 | 213 → 240 | Zähler |
| 0xBF81 | 544 → 575 | Zähler |
| 0xBF83 | 637 → 718 | Zähler |
| 0xBF84 | 2139 → 2275 | Zähler |
