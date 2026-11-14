# Hardware — Optolink-IR-Kopf

## Bauteile

| Teil | Wert / Typ |
|---|---|
| Controller | ESP8266 D1 Mini (oder ESP32, siehe unten) |
| IR-Sender | IR-LED 5 mm, 940 nm, klar |
| IR-Empfänger | Fototransistor 5 mm, schwarz |
| Vorwiderstand | 220 Ω |
| Pull-Up | 10 kΩ |
| Gehäuse | 3D-Druck, V-Keil passend zur Optolink-Kerbe |

## Verdrahtung

| Signal | Verbindung |
|---|---|
| IR-LED Anode (langes Bein) | 3V3 |
| IR-LED Kathode (kurzes Bein) | 220 Ω → TX (GPIO1) |
| Fototransistor Kollektor (lang) | RX (GPIO3) **und** 10 kΩ → 3V3 |
| Fototransistor Emitter (kurz) | GND |

Die LED ist **low-aktiv**: UART-Idle ist HIGH, der Startbit zieht die Leitung auf LOW und
die LED leuchtet. Der Fototransistor der Heizung invertiert das Signal wieder.

> Häufig falsch verdrahtet: „Anode an TX, Kathode über den Widerstand an GND". Das
> leuchtet im Idle und invertiert damit die gesamte Übertragung.

## Pinout D1 Mini (Bestückungsseite oben, Antenne oben, USB unten)

| links (von oben) | rechts (von oben) |
|---|---|
| TX | 3V3 |
| RX | D8 |
| D1 | D7 |
| D2 | D6 |
| D3 | D5 |
| D4 | D0 |
| G | A0 |
| 5V | RST |

## Fallstricke

1. **Flash über USB:** Vorher die Litzen von GPIO1/GPIO3 abziehen. Der Fototransistor
   zieht RX bei Lichteinfall auf GND und blockiert die Flash-Daten — es erscheint
   `Failed to connect to ESP8266: No serial data received`.
2. **Logger:** `logger: baud_rate: 0` ist Pflicht, sonst belegt der Logger UART0 und
   die 4800-8E2-Konfiguration greift nicht.
3. **Kabel:** Reine Ladekabel ohne Datenadern führen dazu, dass gar kein COM-Port
   erscheint.
4. **Ausrichtung:** Die LED muss auf den Empfänger der Heizung zeigen, der
   Fototransistor auf deren Sender. Bei Timeouts das Gehäuse um 180° drehen.
