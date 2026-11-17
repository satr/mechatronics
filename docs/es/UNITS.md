# Unidades y notación dimensional

**Idiomas:** [en](../en/UNITS.md) · [fr](../fr/UNITS.md) · [de](../de/UNITS.md) · [it](../it/UNITS.md) · [es](UNITS.md) · [pt](../pt/UNITS.md) · [zh](../zh/UNITS.md) · [ja](../ja/UNITS.md) · [nb](../nb/UNITS.md) · [ru](../ru/UNITS.md) · [ko](../ko/UNITS.md) · [fi](../fi/UNITS.md) · [pl](../pl/UNITS.md)

[Índice del curso](README.md) · [Símbolos matemáticos](SYMBOLS.md)

Los símbolos de las unidades son internacionales y no se traducen. Las magnitudes se escriben en cursiva y las unidades en letra recta. Se deja un espacio entre el número y la unidad, salvo en los grados angulares; el porcentaje también lleva espacio.

| Símbolo | English unit name | Significado en español | Estado SI |
| --- | --- | --- | --- |
| `m` | metre | metro | SI base |
| `mm` | millimetre | milímetro = 0.001 m | SI decimal submultiple |
| `s` | second | segundo | SI base |
| `ms` | millisecond | milisegundo = 0.001 s | SI decimal submultiple |
| `kg` | kilogram | kilogramo | SI base |
| `A` | ampere | amperio | SI base |
| `N` | newton | newton | SI derived |
| `J` | joule | julio (joule) | SI derived |
| `W` | watt | vatio | SI derived |
| `rad` | radian | radián | SI derived (unit one) |
| `°` | degree of plane angle | grado | non-SI angle unit |
| `rpm` | revolution per minute | revolución por minuto | non-SI |
| `%` | percent | por ciento (una centésima parte) | ratio; not an SI unit |
| `m/s` | metre per second | metro / segundo — velocidad lineal | SI derived |
| `mm/s` | millimetre per second | milímetro / segundo — velocidad lineal | SI decimal units |
| `m/s²` | metre per second squared | metro / segundo² — aceleración | SI derived |
| `mm/s²` | millimetre per second squared | milímetro / segundo² — aceleración | SI decimal units |
| `rad/s` | radian per second | radián / segundo — velocidad angular | SI derived |
| `rad/s²` | radian per second squared | radián / segundo² — aceleración angular | SI derived |
| `mm/rad` | millimetre per radian | milímetro / radián — coeficiente del jacobiano (longitud por ángulo) | SI decimal units |
| `kg·m²` | kilogram metre squared | kilogramo · metro² — momento de inercia | SI derived |
| `N·m` | newton metre (torque) | newton · metro — par de torsión | SI derived |
| `N·m·s/rad` | newton metre second per radian | newton · metro · segundo / radián — ganancia por velocidad | SI derived |
| `N/m` | newton per metre | newton / metro — rigidez | SI derived |
| `rpm/s` | revolutions per minute per second | revolución por minuto / segundo — aceleración angular | contains non-SI rpm |
| `A/rpm` | ampere per rpm | amperio / (revolución por minuto) — ganancia por velocidad | contains non-SI rpm |
| `A/(rpm·s)` | ampere per rpm-second | amperio / (revolución por minuto · segundo) — ganancia integral | contains non-SI rpm |
| `A·s/rpm` | ampere-second per rpm | amperio · segundo / (revolución por minuto) — ganancia derivativa | contains non-SI rpm |
| `mm³/s` | cubic millimetre per second | milímetro³ / segundo — caudal volumétrico | SI decimal units |
| `Hz` | hertz | hercio — frecuencia | SI derived |
| `min` | minute | minuto — duración | non-SI time unit |

## Conversiones y significado físico

- `1 mm = 0.001 m`; `1 ms = 0.001 s`; `1 min = 60 s`.
- `1° = π/180 rad`; `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m` — Julio y newton metro equivalen dimensionalmente: usar `N·m` para el par y `J` para la energía.
- `N·m·s/rad` es una ganancia de par por velocidad angular. `A/rpm`, `A/(rpm·s)` y `A·s/rpm` son las unidades de las ganancias P, I y D del ejemplo de corriente sintético.
- `%` indica partes por cien y no es una unidad SI. Escribir `63.2 %` con espacio, no `63.2%`.

[BIPM SI Brochure, edition 9, revision June 2026](https://www.bipm.org/en/si-brochure-9) · [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
