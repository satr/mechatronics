# Unidades e notação dimensional

**Idiomas:** [en](../en/UNITS.md) · [fr](../fr/UNITS.md) · [de](../de/UNITS.md) · [it](../it/UNITS.md) · [es](../es/UNITS.md) · [pt](UNITS.md) · [zh](../zh/UNITS.md) · [ja](../ja/UNITS.md) · [nb](../nb/UNITS.md) · [ru](../ru/UNITS.md) · [ko](../ko/UNITS.md) · [fi](../fi/UNITS.md) · [pl](../pl/UNITS.md)

[Índice do curso](README.md) · [Símbolos matemáticos](SYMBOLS.md)

Os símbolos das unidades são internacionais e não são traduzidos. As grandezas usam itálico; as unidades usam caracteres direitos. Há um espaço entre número e unidade, exceto nos graus angulares; o símbolo de percentagem também requer espaço.

| Símbolo | English unit name | Significado em português | Estado SI |
| --- | --- | --- | --- |
| `m` | metre | metro | SI base |
| `mm` | millimetre | milímetro = 0.001 m | SI decimal submultiple |
| `s` | second | segundo | SI base |
| `ms` | millisecond | milissegundo = 0.001 s | SI decimal submultiple |
| `kg` | kilogram | quilograma | SI base |
| `A` | ampere | ampere | SI base |
| `N` | newton | newton | SI derived |
| `J` | joule | joule | SI derived |
| `W` | watt | watt | SI derived |
| `rad` | radian | radiano | SI derived (unit one) |
| `°` | degree of plane angle | grau | non-SI angle unit |
| `rpm` | revolution per minute | rotação por minuto | non-SI |
| `%` | percent | percentagem (uma centésima parte) | ratio; not an SI unit |
| `m/s` | metre per second | metro / segundo — velocidade linear | SI derived |
| `mm/s` | millimetre per second | milímetro / segundo — velocidade linear | SI decimal units |
| `m/s²` | metre per second squared | metro / segundo² — aceleração | SI derived |
| `mm/s²` | millimetre per second squared | milímetro / segundo² — aceleração | SI decimal units |
| `rad/s` | radian per second | radiano / segundo — velocidade angular | SI derived |
| `rad/s²` | radian per second squared | radiano / segundo² — aceleração angular | SI derived |
| `mm/rad` | millimetre per radian | milímetro / radiano — coeficiente jacobiano (comprimento por ângulo) | SI decimal units |
| `kg·m²` | kilogram metre squared | quilograma · metro² — momento de inércia | SI derived |
| `N·m` | newton metre (torque) | newton · metro — binário (torque) | SI derived |
| `N·m·s/rad` | newton metre second per radian | newton · metro · segundo / radiano — ganho por velocidade | SI derived |
| `N/m` | newton per metre | newton / metro — rigidez | SI derived |
| `rpm/s` | revolutions per minute per second | rotação por minuto / segundo — aceleração angular | contains non-SI rpm |
| `A/rpm` | ampere per rpm | ampere / (rotação por minuto) — ganho por velocidade | contains non-SI rpm |
| `A/(rpm·s)` | ampere per rpm-second | ampere / (rotação por minuto · segundo) — ganho integral | contains non-SI rpm |
| `A·s/rpm` | ampere-second per rpm | ampere · segundo / (rotação por minuto) — ganho derivativo | contains non-SI rpm |
| `mm³/s` | cubic millimetre per second | milímetro³ / segundo — caudal volumétrico | SI decimal units |
| `Hz` | hertz | hertz — frequência | SI derived |
| `min` | minute | minuto — duração | non-SI time unit |

## Conversões e significado físico

- `1 mm = 0.001 m`; `1 ms = 0.001 s`; `1 min = 60 s`.
- `1° = π/180 rad`; `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m` — Joule e newton-metro são equivalentes dimensionalmente: usar `N·m` para o binário e `J` para a energia.
- `N·m·s/rad` é um ganho de binário por velocidade angular. `A/rpm`, `A/(rpm·s)` e `A·s/rpm` são as unidades dos ganhos P, I e D do exemplo didático com saída de corrente.
- `%` representa partes por cem e não é uma unidade SI. Escrever `63.2 %` com espaço, não `63.2%`.

[BIPM SI Brochure, edition 9, revision June 2026](https://www.bipm.org/en/si-brochure-9) · [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
