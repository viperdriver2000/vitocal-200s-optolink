# P300-Frame-Format und Checksumme

## Request (Read)

```
41 05 00 01 <addr_hi> <addr_lo> <len> <crc>
```

Beispiel: `0x01C1`, 2 Byte → `41 05 00 01 01 C1 02 CA`

## Antwort

Erfolg:

```
06 41 <len> 01 <addr_hi> <addr_lo> <len> <data...> <crc>
```

Fehler:

```
06 41 06 03 <addr_hi> <addr_lo> 01 <code> <crc>
```

| Code | Bedeutung (empirisch) |
|---|---|
| 3 | Datenpunkt existiert nicht |
| 4 | Datenpunkt existiert, ist aber nicht lesbar / anderer Zugriff |

## Checksumme

Aus echten Frames rekonstruiert und gegen drei Frames verifiziert:

```python
def crc(body: list[int]) -> int:
    """body = alle Bytes nach dem fuehrenden 0x06"""
    return (sum(body) + 0xBF) & 0xFF
```

## UART

4800 Baud, 8 Datenbits, **even** Parity, **2** Stopbits (8E2).
Abweichende Einstellungen beantwortet der Regler nicht.
