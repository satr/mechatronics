# Enheter og dimensjonsnotasjon

**Språk:** [en](../en/UNITS.md) · [fr](../fr/UNITS.md) · [de](../de/UNITS.md) · [it](../it/UNITS.md) · [es](../es/UNITS.md) · [pt](../pt/UNITS.md) · [zh](../zh/UNITS.md) · [ja](../ja/UNITS.md) · [nb](UNITS.md) · [ru](../ru/UNITS.md) · [ko](../ko/UNITS.md) · [fi](../fi/UNITS.md) · [pl](../pl/UNITS.md)

[Kursoversikt](README.md) · [Matematiske symboler](SYMBOLS.md)

Enhetssymbolene er internasjonale og oversettes ikke. Størrelsessymboler skrives i kursiv, enhetssymboler med opprett skrift. Det skal være mellomrom mellom tall og enhet, bortsett fra vinkelgrader; prosenttegnet krever også mellomrom.

| Symbol | English unit name | Betydning på norsk | SI-status |
| --- | --- | --- | --- |
| `m` | metre | meter | SI base |
| `mm` | millimetre | millimeter = 0.001 m | SI decimal submultiple |
| `s` | second | sekund | SI base |
| `ms` | millisecond | millisekund = 0.001 s | SI decimal submultiple |
| `kg` | kilogram | kilogram | SI base |
| `A` | ampere | ampere | SI base |
| `N` | newton | newton | SI derived |
| `J` | joule | joule | SI derived |
| `W` | watt | watt | SI derived |
| `rad` | radian | radian | SI derived (unit one) |
| `°` | degree of plane angle | grad | non-SI angle unit |
| `rpm` | revolution per minute | omdreining per minutt | non-SI |
| `%` | percent | prosent (en hundredel) | ratio; not an SI unit |
| `m/s` | metre per second | meter / sekund — lineær hastighet | SI derived |
| `mm/s` | millimetre per second | millimeter / sekund — lineær hastighet | SI decimal units |
| `m/s²` | metre per second squared | meter / sekund² — akselerasjon | SI derived |
| `mm/s²` | millimetre per second squared | millimeter / sekund² — akselerasjon | SI decimal units |
| `rad/s` | radian per second | radian / sekund — vinkelhastighet | SI derived |
| `rad/s²` | radian per second squared | radian / sekund² — vinkelakselerasjon | SI derived |
| `mm/rad` | millimetre per radian | millimeter / radian — Jacobi-koeffisient (lengde per vinkel) | SI decimal units |
| `kg·m²` | kilogram metre squared | kilogram · meter² — treghetsmoment | SI derived |
| `N·m` | newton metre (torque) | newton · meter — dreiemoment | SI derived |
| `N·m·s/rad` | newton metre second per radian | newton · meter · sekund / radian — forsterkning per hastighet | SI derived |
| `N/m` | newton per metre | newton / meter — stivhet | SI derived |
| `rpm/s` | revolutions per minute per second | omdreining per minutt / sekund — vinkelakselerasjon | contains non-SI rpm |
| `A/rpm` | ampere per rpm | ampere / (omdreining per minutt) — forsterkning per hastighet | contains non-SI rpm |
| `A/(rpm·s)` | ampere per rpm-second | ampere / (omdreining per minutt · sekund) — integralforsterkning | contains non-SI rpm |
| `A·s/rpm` | ampere-second per rpm | ampere · sekund / (omdreining per minutt) — derivatforsterkning | contains non-SI rpm |
| `mm³/s` | cubic millimetre per second | millimeter³ / sekund — volumstrøm | SI decimal units |
| `Hz` | hertz | hertz — frekvens | SI derived |
| `min` | minute | minutt — varighet | non-SI time unit |

## Omregninger og fysisk betydning

- `1 mm = 0.001 m`; `1 ms = 0.001 s`; `1 min = 60 s`.
- `1° = π/180 rad`; `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m` — Joule og newtonmeter har samme dimensjon: bruk `N·m` for dreiemoment og `J` for energi.
- `N·m·s/rad` er en momentforsterkning per vinkelhastighet. `A/rpm`, `A/(rpm·s)` og `A·s/rpm` er enhetene til P-, I- og D-leddet i den syntetiske strømregulatoren.
- `%` betyr hundredeler og er ikke en SI-enhet. Skriv `63.2 %` med mellomrom, ikke `63.2%`.

[BIPM SI Brochure, edition 9, revision June 2026](https://www.bipm.org/en/si-brochure-9) · [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
