# Einheiten und Dimensionsschreibweise

**Sprachen:** [en](../en/UNITS.md) · [fr](../fr/UNITS.md) · [de](UNITS.md) · [it](../it/UNITS.md) · [es](../es/UNITS.md) · [pt](../pt/UNITS.md) · [zh](../zh/UNITS.md) · [ja](../ja/UNITS.md) · [nb](../nb/UNITS.md) · [ru](../ru/UNITS.md) · [ko](../ko/UNITS.md) · [fi](../fi/UNITS.md) · [pl](../pl/UNITS.md)

[Kursübersicht](README.md) · [Mathematische Symbole](SYMBOLS.md)

Einheitenzeichen sind international und werden nicht übersetzt. Größenzeichen stehen kursiv, Einheiten aufrecht. Zwischen Zahl und Einheit steht ein Leerzeichen; nur bei Winkelgrad entfällt es. Auch vor dem Prozentzeichen steht ein Leerzeichen.

| Zeichen | English unit name | Bedeutung auf Deutsch | SI-Status |
| --- | --- | --- | --- |
| `m` | metre | Meter | SI base |
| `mm` | millimetre | Millimeter = 0.001 m | SI decimal submultiple |
| `s` | second | Sekunde | SI base |
| `ms` | millisecond | Millisekunde = 0.001 s | SI decimal submultiple |
| `kg` | kilogram | Kilogramm | SI base |
| `A` | ampere | Ampere | SI base |
| `N` | newton | Newton | SI derived |
| `J` | joule | Joule | SI derived |
| `W` | watt | Watt | SI derived |
| `rad` | radian | Radiant | SI derived (unit one) |
| `°` | degree of plane angle | Grad | non-SI angle unit |
| `rpm` | revolution per minute | Umdrehung pro Minute | non-SI |
| `%` | percent | Prozent (ein Hundertstel) | ratio; not an SI unit |
| `m/s` | metre per second | Meter / Sekunde — lineare Geschwindigkeit | SI derived |
| `mm/s` | millimetre per second | Millimeter / Sekunde — lineare Geschwindigkeit | SI decimal units |
| `m/s²` | metre per second squared | Meter / Sekunde² — Beschleunigung | SI derived |
| `mm/s²` | millimetre per second squared | Millimeter / Sekunde² — Beschleunigung | SI decimal units |
| `rad/s` | radian per second | Radiant / Sekunde — Winkelgeschwindigkeit | SI derived |
| `rad/s²` | radian per second squared | Radiant / Sekunde² — Winkelbeschleunigung | SI derived |
| `mm/rad` | millimetre per radian | Millimeter / Radiant — Jacobi-Koeffizient (Länge pro Winkel) | SI decimal units |
| `kg·m²` | kilogram metre squared | Kilogramm · Meter² — Trägheitsmoment | SI derived |
| `N·m` | newton metre (torque) | Newton · Meter — Drehmoment | SI derived |
| `N·m·s/rad` | newton metre second per radian | Newton · Meter · Sekunde / Radiant — Verstärkung pro Geschwindigkeit | SI derived |
| `N/m` | newton per metre | Newton / Meter — Steifigkeit | SI derived |
| `rpm/s` | revolutions per minute per second | Umdrehung pro Minute / Sekunde — Winkelbeschleunigung | contains non-SI rpm |
| `A/rpm` | ampere per rpm | Ampere / (Umdrehung pro Minute) — Verstärkung pro Geschwindigkeit | contains non-SI rpm |
| `A/(rpm·s)` | ampere per rpm-second | Ampere / (Umdrehung pro Minute · Sekunde) — Integralverstärkung | contains non-SI rpm |
| `A·s/rpm` | ampere-second per rpm | Ampere · Sekunde / (Umdrehung pro Minute) — Differentialverstärkung | contains non-SI rpm |
| `mm³/s` | cubic millimetre per second | Millimeter³ / Sekunde — Volumenstrom | SI decimal units |
| `Hz` | hertz | Hertz — Frequenz | SI derived |
| `min` | minute | Minute — Zeitdauer | non-SI time unit |

## Umrechnungen und physikalische Bedeutung

- `1 mm = 0.001 m`; `1 ms = 0.001 s`; `1 min = 60 s`.
- `1° = π/180 rad`; `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m` — Joule und Newtonmeter haben dieselbe Dimension; für Drehmoment schreibt man `N·m`, für Energie `J`.
- `N·m·s/rad` ist die Drehmomentverstärkung pro Winkelgeschwindigkeit. `A/rpm`, `A/(rpm·s)` und `A·s/rpm` sind die Einheiten der P-, I- und D-Verstärkung im rein rechnerischen Strommodell.
- `%` bezeichnet einen Anteil von Hundert und ist keine SI-Einheit. Richtig ist `63.2 %` mit Leerzeichen, nicht `63.2%`.

[BIPM SI Brochure, edition 9, revision June 2026](https://www.bipm.org/en/si-brochure-9) · [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
