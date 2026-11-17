# Единицы измерения и размерности

**Языки:** [en](../en/UNITS.md) · [fr](../fr/UNITS.md) · [de](../de/UNITS.md) · [it](../it/UNITS.md) · [es](../es/UNITS.md) · [pt](../pt/UNITS.md) · [zh](../zh/UNITS.md) · [ja](../ja/UNITS.md) · [nb](../nb/UNITS.md) · [ru](UNITS.md) · [ko](../ko/UNITS.md) · [fi](../fi/UNITS.md) · [pl](../pl/UNITS.md)

[Содержание курса](README.md) · [Математические обозначения](SYMBOLS.md)

Обозначения единиц международные и не переводятся. Символы физических величин пишутся курсивом, обозначения единиц — прямым шрифтом. Между числом и единицей нужен пробел; исключение — градус плоского угла °. Перед знаком процента % пробел тоже нужен.

| Символ | English unit name | Значение по-русски | Статус SI |
| --- | --- | --- | --- |
| `m` | metre | метр | SI base |
| `mm` | millimetre | миллиметр = 0.001 m | SI decimal submultiple |
| `s` | second | секунда | SI base |
| `ms` | millisecond | миллисекунда = 0.001 s | SI decimal submultiple |
| `kg` | kilogram | килограмм | SI base |
| `A` | ampere | ампер | SI base |
| `N` | newton | ньютон | SI derived |
| `J` | joule | джоуль | SI derived |
| `W` | watt | ватт | SI derived |
| `rad` | radian | радиан | SI derived (unit one) |
| `°` | degree of plane angle | градус | non-SI angle unit |
| `rpm` | revolution per minute | оборот в минуту | non-SI |
| `%` | percent | процент (одна сотая) | ratio; not an SI unit |
| `m/s` | metre per second | метр / секунда — линейная скорость | SI derived |
| `mm/s` | millimetre per second | миллиметр / секунда — линейная скорость | SI decimal units |
| `m/s²` | metre per second squared | метр / секунда² — ускорение | SI derived |
| `mm/s²` | millimetre per second squared | миллиметр / секунда² — ускорение | SI decimal units |
| `rad/s` | radian per second | радиан / секунда — угловая скорость | SI derived |
| `rad/s²` | radian per second squared | радиан / секунда² — угловое ускорение | SI derived |
| `mm/rad` | millimetre per radian | миллиметр / радиан — коэффициент Якобиана (длина на единицу угла) | SI decimal units |
| `kg·m²` | kilogram metre squared | килограмм · метр² — момент инерции | SI derived |
| `N·m` | newton metre (torque) | ньютон · метр — крутящий момент | SI derived |
| `N·m·s/rad` | newton metre second per radian | ньютон · метр · секунда / радиан — коэффициент усиления по скорости | SI derived |
| `N/m` | newton per metre | ньютон / метр — жёсткость | SI derived |
| `rpm/s` | revolutions per minute per second | оборот в минуту / секунда — угловое ускорение | contains non-SI rpm |
| `A/rpm` | ampere per rpm | ампер / (оборот в минуту) — коэффициент усиления по скорости | contains non-SI rpm |
| `A/(rpm·s)` | ampere per rpm-second | ампер / (оборот в минуту · секунда) — интегральный коэффициент | contains non-SI rpm |
| `A·s/rpm` | ampere-second per rpm | ампер · секунда / (оборот в минуту) — дифференциальный коэффициент | contains non-SI rpm |
| `mm³/s` | cubic millimetre per second | миллиметр³ / секунда — объёмный расход | SI decimal units |
| `Hz` | hertz | герц — частота | SI derived |
| `min` | minute | минута — время | non-SI time unit |

## Пересчёт и физический смысл

- `1 mm = 0.001 m`; `1 ms = 0.001 s`; `1 min = 60 s`.
- `1° = π/180 rad`; `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m` — Джоуль и ньютон-метр имеют одинаковую размерность: для крутящего момента используем `N·m`, для энергии — `J`.
- `N·m·s/rad` — коэффициент крутящего момента по угловой скорости. `A/rpm`, `A/(rpm·s)` и `A·s/rpm` — единицы пропорционального, интегрального и дифференциального коэффициентов в учебной модели регулятора с выходом по току.
- `%` обозначает сотую долю и не является единицей SI. Пишем `63.2 %` с пробелом, а не `63.2%`.

[BIPM SI Brochure, edition 9, revision June 2026](https://www.bipm.org/en/si-brochure-9) · [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
