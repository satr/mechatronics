# Unités et notation dimensionnelle

**Langues:** [en](../en/UNITS.md) · [fr](UNITS.md) · [de](../de/UNITS.md) · [it](../it/UNITS.md) · [es](../es/UNITS.md) · [pt](../pt/UNITS.md) · [zh](../zh/UNITS.md) · [ja](../ja/UNITS.md) · [nb](../nb/UNITS.md) · [ru](../ru/UNITS.md) · [ko](../ko/UNITS.md) · [fi](../fi/UNITS.md) · [pl](../pl/UNITS.md)

[Sommaire du cours](README.md) · [Symboles mathématiques](SYMBOLS.md)

Les symboles des unités sont internationaux et ne se traduisent pas. Les grandeurs s'écrivent en italique et les unités en caractères droits. Une espace sépare valeur et unité, sauf pour le degré d'angle ; le symbole de pourcentage prend aussi une espace.

| Symbole | English unit name | Signification en français | Statut SI |
| --- | --- | --- | --- |
| `m` | metre | mètre | SI base |
| `mm` | millimetre | millimètre = 0.001 m | SI decimal submultiple |
| `s` | second | seconde | SI base |
| `ms` | millisecond | milliseconde = 0.001 s | SI decimal submultiple |
| `kg` | kilogram | kilogramme | SI base |
| `A` | ampere | ampère | SI base |
| `N` | newton | newton | SI derived |
| `J` | joule | joule | SI derived |
| `W` | watt | watt | SI derived |
| `rad` | radian | radian | SI derived (unit one) |
| `°` | degree of plane angle | degré | non-SI angle unit |
| `rpm` | revolution per minute | tour par minute | non-SI |
| `%` | percent | pour cent (un centième) | ratio; not an SI unit |
| `m/s` | metre per second | mètre / seconde — vitesse linéaire | SI derived |
| `mm/s` | millimetre per second | millimètre / seconde — vitesse linéaire | SI decimal units |
| `m/s²` | metre per second squared | mètre / seconde² — accélération | SI derived |
| `mm/s²` | millimetre per second squared | millimètre / seconde² — accélération | SI decimal units |
| `rad/s` | radian per second | radian / seconde — vitesse angulaire | SI derived |
| `rad/s²` | radian per second squared | radian / seconde² — accélération angulaire | SI derived |
| `mm/rad` | millimetre per radian | millimètre / radian — coefficient du jacobien (longueur par angle) | SI decimal units |
| `kg·m²` | kilogram metre squared | kilogramme · mètre² — moment d'inertie | SI derived |
| `N·m` | newton metre (torque) | newton · mètre — moment de force | SI derived |
| `N·m·s/rad` | newton metre second per radian | newton · mètre · seconde / radian — gain par unité de vitesse | SI derived |
| `N/m` | newton per metre | newton / mètre — raideur | SI derived |
| `rpm/s` | revolutions per minute per second | tour par minute / seconde — accélération angulaire | contains non-SI rpm |
| `A/rpm` | ampere per rpm | ampère / (tour par minute) — gain par unité de vitesse | contains non-SI rpm |
| `A/(rpm·s)` | ampere per rpm-second | ampère / (tour par minute · seconde) — gain intégral | contains non-SI rpm |
| `A·s/rpm` | ampere-second per rpm | ampère · seconde / (tour par minute) — gain dérivé | contains non-SI rpm |
| `mm³/s` | cubic millimetre per second | millimètre³ / seconde — débit volumique | SI decimal units |
| `Hz` | hertz | hertz — fréquence | SI derived |
| `min` | minute | minute — durée | non-SI time unit |

## Conversions et sens physique

- `1 mm = 0.001 m`; `1 ms = 0.001 s`; `1 min = 60 s`.
- `1° = π/180 rad`; `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m` — L'égalité entre joule et newton-mètre est dimensionnelle : employer `N·m` pour le moment de force et `J` pour l'énergie.
- `N·m·s/rad` est un coefficient de moment de force par vitesse angulaire. Les termes `A/rpm`, `A/(rpm·s)` et `A·s/rpm` sont les unités des gains P, I et D du modèle de courant fictif.
- `%` désigne une fraction de cent, pas une unité SI. Écrire `63.2 %` avec une espace, et non `63.2%`.

[BIPM SI Brochure, edition 9, revision June 2026](https://www.bipm.org/en/si-brochure-9) · [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
