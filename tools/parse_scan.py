#!/usr/bin/env python3
"""Wertet Optolink-Adress-Scans aus.

Liest ein ESPHome-Log (UTF-8 oder UTF-16, wie PowerShell Tee-Object schreibt)
und gibt alle Adressen aus, die mit einem Erfolgs-Frame geantwortet haben.

Frame-Formate (P300):
  OK:    06 41 <len> 01 <addr_hi> <addr_lo> <len> <data...> <crc>
  Fehler: 06 41 06 03 <addr_hi> <addr_lo> 01 <code> <crc>

Aufruf:
  python3 parse_scan.py scan.log [--min 0x0000] [--max 0xFFFF] [--raw]

Beispiel:
  python3 parse_scan.py ~/tmp/scan-mid.log --min 0x0880 --max 0x0897
"""

import argparse
import re
import sys

FRAME_RE = re.compile(r'<<<\s*([0-9A-F:]+)')


def read_log(path):
    data = open(path, 'rb').read()
    for enc in ('utf-16', 'utf-8'):
        try:
            text = data.decode(enc)
        except UnicodeDecodeError:
            continue
        if '<<<' in text:
            return text
    return data.decode('utf-8', errors='ignore')


def parse(text):
    ok, errors = {}, {}
    for match in FRAME_RE.finditer(text):
        try:
            b = [int(x, 16) for x in match.group(1).split(':') if x]
        except ValueError:
            continue
        if len(b) < 8:
            continue
        status = b[3]
        addr = (b[5] << 8) | b[6]
        length = b[7]
        if status == 0x01:
            ok[addr] = b[8:8 + length]
        else:
            errors[status] = errors.get(status, 0) + 1
    return ok, errors


def sval(data):
    """signed int16, little endian"""
    if len(data) == 2:
        v = data[0] | (data[1] << 8)
        return v - 65536 if v > 32767 else v
    return int.from_bytes(bytes(data), 'little')


def main():
    ap = argparse.ArgumentParser(description='Optolink-Scan-Log auswerten')
    ap.add_argument('log')
    ap.add_argument('--min', default='0x0000')
    ap.add_argument('--max', default='0xFFFF')
    ap.add_argument('--raw', action='store_true', help='Rohbytes mit ausgeben')
    args = ap.parse_args()

    lo, hi = int(args.min, 16), int(args.max, 16)
    ok, errors = parse(read_log(args.log))

    hits = {a: d for a, d in ok.items() if lo <= a <= hi}
    print(f'Antworten gesamt: {len(ok)}  |  Fehlercodes: {errors or "-"}')
    print(f'Bereich 0x{lo:04X}-0x{hi:04X}: {len(hits)} Treffer\n')

    for addr in sorted(hits):
        data = hits[addr]
        raw = ' '.join(f'{x:02X}' for x in data) if args.raw else ''
        print(f'0x{addr:04X}  len={len(data)}  int={sval(data):>8d}  '
              f'div10={sval(data) / 10:>8.1f}  {raw}'.rstrip())


if __name__ == '__main__':
    sys.exit(main())
