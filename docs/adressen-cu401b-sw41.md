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
