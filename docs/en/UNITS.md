# Units and dimensional notation

**Languages:** [en](UNITS.md) · [fr](../fr/UNITS.md) · [de](../de/UNITS.md) · [it](../it/UNITS.md) · [es](../es/UNITS.md) · [pt](../pt/UNITS.md) · [zh](../zh/UNITS.md) · [ja](../ja/UNITS.md) · [nb](../nb/UNITS.md) · [ru](../ru/UNITS.md) · [ko](../ko/UNITS.md) · [fi](../fi/UNITS.md) · [pl](../pl/UNITS.md)

[Course index](README.md) · [Mathematical symbols](SYMBOLS.md)

The symbols below are international and must not be translated. Quantity symbols are italic variables; unit symbols are upright. The unit name, physical meaning, and its status are explained here. A value and its unit are separated by a space (except plane-angle degrees); the percent sign also takes a space.

| Symbol | English unit name | Meaning in this language | SI status |
| --- | --- | --- | --- |
| `m` | metre | metre | SI base |
| `mm` | millimetre | millimetre = 0.001 m | SI decimal submultiple |
| `s` | second | second | SI base |
| `ms` | millisecond | millisecond = 0.001 s | SI decimal submultiple |
| `kg` | kilogram | kilogram | SI base |
| `A` | ampere | ampere | SI base |
| `N` | newton | newton | SI derived |
| `J` | joule | joule | SI derived |
| `W` | watt | watt | SI derived |
| `rad` | radian | radian | SI derived (unit one) |
| `°` | degree of plane angle | degree | non-SI angle unit |
| `rpm` | revolution per minute | revolution per minute | non-SI |
| `%` | percent | percent (one part in a hundred) | ratio; not an SI unit |
| `m/s` | metre per second | metre / second — linear speed | SI derived |
| `mm/s` | millimetre per second | millimetre / second — linear speed | SI decimal units |
| `m/s²` | metre per second squared | metre / second² — acceleration | SI derived |
| `mm/s²` | millimetre per second squared | millimetre / second² — acceleration | SI decimal units |
| `rad/s` | radian per second | radian / second — angular speed | SI derived |
| `rad/s²` | radian per second squared | radian / second² — angular acceleration | SI derived |
| `mm/rad` | millimetre per radian | millimetre / radian — Jacobian coefficient (length per angle) | SI decimal units |
| `kg·m²` | kilogram metre squared | kilogram · metre² — moment of inertia | SI derived |
| `N·m` | newton metre (torque) | newton · metre — torque | SI derived |
| `N·m·s/rad` | newton metre second per radian | newton · metre · second / radian — gain per unit speed | SI derived |
| `N/m` | newton per metre | newton / metre — stiffness | SI derived |
| `rpm/s` | revolutions per minute per second | revolution per minute / second — angular acceleration | contains non-SI rpm |
| `A/rpm` | ampere per rpm | ampere / (revolution per minute) — gain per unit speed | contains non-SI rpm |
| `A/(rpm·s)` | ampere per rpm-second | ampere / (revolution per minute · second) — time-integral gain | contains non-SI rpm |
| `A·s/rpm` | ampere-second per rpm | ampere · second / (revolution per minute) — time-derivative gain | contains non-SI rpm |
| `mm³/s` | cubic millimetre per second | millimetre³ / second — volumetric flow | SI decimal units |
| `Hz` | hertz | hertz — frequency | SI derived |
| `min` | minute | minute — duration | non-SI time unit |

## Conversions and physical meaning

- `1 mm = 0.001 m`; `1 ms = 0.001 s`; `1 min = 60 s`.
- `1° = π/180 rad`; `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m` — The equality of the joule and newton metre is dimensional: use `N·m` for torque and `J` for energy.
- `N·m·s/rad` is a torque gain per angular speed. The terms `A/rpm`, `A/(rpm·s)` and `A·s/rpm` are the P, I and D gain units in the synthetic current-output example.
- `%` means parts per hundred, not an SI unit. Write `63.2 %` with a space, not `63.2%`.

[BIPM SI Brochure, edition 9, revision June 2026](https://www.bipm.org/en/si-brochure-9) · [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
