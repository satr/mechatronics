# Jednostki miary i zapis wymiarów

**Języki:** [en](../en/UNITS.md) · [fr](../fr/UNITS.md) · [de](../de/UNITS.md) · [it](../it/UNITS.md) · [es](../es/UNITS.md) · [pt](../pt/UNITS.md) · [zh](../zh/UNITS.md) · [ja](../ja/UNITS.md) · [nb](../nb/UNITS.md) · [ru](../ru/UNITS.md) · [ko](../ko/UNITS.md) · [fi](../fi/UNITS.md) · [pl](UNITS.md)

[Spis treści](README.md) · [Symbole matematyczne](SYMBOLS.md)

Symbole jednostek są międzynarodowe i **nie są tłumaczone**. Symbole wielkości fizycznych zapisujemy kursywą, a symbole jednostek pismem prostym. Między liczbą a jednostką pozostawiamy odstęp (np. `10 mm`); wyjątkiem jest znak stopnia kąta płaskiego (`30°`). Przed znakiem procenta także stosujemy odstęp (`63.2 %`). W całym kursie separatorem dziesiętnym jest kropka.

| Symbol | English unit name | Znaczenie po polsku | Status względem SI |
| --- | --- | --- | --- |
| `m` | metre | metr | jednostka podstawowa SI |
| `mm` | millimetre | milimetr = 0.001 m | podwielokrotność dziesiętna SI |
| `s` | second | sekunda | jednostka podstawowa SI |
| `ms` | millisecond | milisekunda = 0.001 s | podwielokrotność dziesiętna SI |
| `kg` | kilogram | kilogram | jednostka podstawowa SI |
| `A` | ampere | amper | jednostka podstawowa SI |
| `N` | newton | niuton — siła | jednostka pochodna SI |
| `J` | joule | dżul — energia i praca | jednostka pochodna SI |
| `W` | watt | wat — moc | jednostka pochodna SI |
| `rad` | radian | radian — kąt płaski | jednostka pochodna SI (wymiar 1) |
| `°` | degree of plane angle | stopień kąta płaskiego | jednostka spoza SI |
| `rpm` | revolution per minute | obrót na minutę | jednostka spoza SI |
| `%` | percent | procent — jedna setna | stosunek bezwymiarowy, nie jednostka SI |
| `m/s` | metre per second | metr na sekundę — prędkość liniowa | jednostka pochodna SI |
| `mm/s` | millimetre per second | milimetr na sekundę — prędkość liniowa | jednostka oparta na SI |
| `m/s²` | metre per second squared | metr na sekundę do kwadratu — przyspieszenie | jednostka pochodna SI |
| `mm/s²` | millimetre per second squared | milimetr na sekundę do kwadratu — przyspieszenie | jednostka oparta na SI |
| `rad/s` | radian per second | radian na sekundę — prędkość kątowa | jednostka pochodna SI |
| `rad/s²` | radian per second squared | radian na sekundę do kwadratu — przyspieszenie kątowe | jednostka pochodna SI |
| `mm/rad` | millimetre per radian | milimetr na radian — współczynnik jakobianu (długość na kąt) | jednostka oparta na SI |
| `kg·m²` | kilogram metre squared | kilogram razy metr kwadratowy — moment bezwładności | jednostka pochodna SI |
| `N·m` | newton metre (torque) | niutonometr — moment siły | jednostka pochodna SI |
| `N·m·s/rad` | newton metre second per radian | niutonometr razy sekunda na radian — współczynnik momentu względem prędkości kątowej | jednostka pochodna SI |
| `N/m` | newton per metre | niuton na metr — sztywność sprężyny | jednostka pochodna SI |
| `rpm/s` | revolutions per minute per second | obrót na minutę na sekundę — przyspieszenie kątowe | zawiera rpm spoza SI |
| `A/rpm` | ampere per rpm | amper na jednostkę rpm — wzmocnienie proporcjonalne | zawiera rpm spoza SI |
| `A/(rpm·s)` | ampere per rpm-second | amper na iloczyn rpm i sekundy — wzmocnienie całkujące | zawiera rpm spoza SI |
| `A·s/rpm` | ampere-second per rpm | amper razy sekunda na rpm — wzmocnienie różniczkujące | zawiera rpm spoza SI |
| `mm³/s` | cubic millimetre per second | milimetr sześcienny na sekundę — strumień objętości | jednostka oparta na SI |
| `Hz` | hertz | herc — częstotliwość | jednostka pochodna SI |
| `min` | minute | minuta — czas | jednostka spoza SI dopuszczona do stosowania z SI |

## Przeliczenia i znaczenie fizyczne

- `1 mm = 0.001 m`; `1 ms = 0.001 s`; `1 min = 60 s`.
- `1° = π/180 rad`; `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m`. Dżul i niutonometr mają zgodne wymiary, ale moment obrotowy oznaczamy `N·m`, natomiast energię — `J`.
- `N·m·s/rad` opisuje współczynnik momentu względem prędkości kątowej. Jednostki `A/rpm`, `A/(rpm·s)` i `A·s/rpm` dotyczą odpowiednio członów P, I i D w syntetycznym przykładzie regulatora z wyjściem prądowym.
- `%` to jedna setna, nie jednostka podstawowa ani pochodna SI. Pisz `63.2 %` z odstępem, a nie `63.2%`.

[Międzynarodowy układ SI — broszura BIPM, wydanie 9 (aktualizacja z czerwca 2026)](https://www.bipm.org/en/si-brochure-9) · [Wzory matematyczne w GitHub Markdown](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
