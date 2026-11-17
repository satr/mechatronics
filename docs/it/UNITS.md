# Unità e notazione dimensionale

**Lingue:** [en](../en/UNITS.md) · [fr](../fr/UNITS.md) · [de](../de/UNITS.md) · [it](UNITS.md) · [es](../es/UNITS.md) · [pt](../pt/UNITS.md) · [zh](../zh/UNITS.md) · [ja](../ja/UNITS.md) · [nb](../nb/UNITS.md) · [ru](../ru/UNITS.md) · [ko](../ko/UNITS.md) · [fi](../fi/UNITS.md) · [pl](../pl/UNITS.md)

[Indice del corso](README.md) · [Simboli matematici](SYMBOLS.md)

I simboli delle unità sono internazionali e non si traducono. I simboli delle grandezze sono in corsivo, quelli delle unità in carattere diritto. Tra numero e unità si lascia uno spazio, tranne che per i gradi angolari; anche la percentuale richiede uno spazio.

| Simbolo | English unit name | Significato in italiano | Stato SI |
| --- | --- | --- | --- |
| `m` | metre | metro | SI base |
| `mm` | millimetre | millimetro = 0.001 m | SI decimal submultiple |
| `s` | second | secondo | SI base |
| `ms` | millisecond | millisecondo = 0.001 s | SI decimal submultiple |
| `kg` | kilogram | chilogrammo | SI base |
| `A` | ampere | ampere | SI base |
| `N` | newton | newton | SI derived |
| `J` | joule | joule | SI derived |
| `W` | watt | watt | SI derived |
| `rad` | radian | radiante | SI derived (unit one) |
| `°` | degree of plane angle | grado | non-SI angle unit |
| `rpm` | revolution per minute | giro al minuto | non-SI |
| `%` | percent | percento (un centesimo) | ratio; not an SI unit |
| `m/s` | metre per second | metro / secondo — velocità lineare | SI derived |
| `mm/s` | millimetre per second | millimetro / secondo — velocità lineare | SI decimal units |
| `m/s²` | metre per second squared | metro / secondo² — accelerazione | SI derived |
| `mm/s²` | millimetre per second squared | millimetro / secondo² — accelerazione | SI decimal units |
| `rad/s` | radian per second | radiante / secondo — velocità angolare | SI derived |
| `rad/s²` | radian per second squared | radiante / secondo² — accelerazione angolare | SI derived |
| `mm/rad` | millimetre per radian | millimetro / radiante — coefficiente jacobiano (lunghezza per angolo) | SI decimal units |
| `kg·m²` | kilogram metre squared | chilogrammo · metro² — momento d'inerzia | SI derived |
| `N·m` | newton metre (torque) | newton · metro — momento torcente | SI derived |
| `N·m·s/rad` | newton metre second per radian | newton · metro · secondo / radiante — guadagno per unità di velocità | SI derived |
| `N/m` | newton per metre | newton / metro — rigidezza | SI derived |
| `rpm/s` | revolutions per minute per second | giro al minuto / secondo — accelerazione angolare | contains non-SI rpm |
| `A/rpm` | ampere per rpm | ampere / (giro al minuto) — guadagno per unità di velocità | contains non-SI rpm |
| `A/(rpm·s)` | ampere per rpm-second | ampere / (giro al minuto · secondo) — guadagno integrale | contains non-SI rpm |
| `A·s/rpm` | ampere-second per rpm | ampere · secondo / (giro al minuto) — guadagno derivativo | contains non-SI rpm |
| `mm³/s` | cubic millimetre per second | millimetro³ / secondo — portata volumetrica | SI decimal units |
| `Hz` | hertz | hertz — frequenza | SI derived |
| `min` | minute | minuto — durata | non-SI time unit |

## Conversioni e significato fisico

- `1 mm = 0.001 m`; `1 ms = 0.001 s`; `1 min = 60 s`.
- `1° = π/180 rad`; `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m` — Joule e newton metro sono dimensionalmente equivalenti: usare `N·m` per il momento torcente e `J` per l'energia.
- `N·m·s/rad` è un guadagno di coppia rispetto alla velocità angolare. `A/rpm`, `A/(rpm·s)` e `A·s/rpm` sono le unità dei guadagni P, I e D dell'esempio didattico con uscita di corrente.
- `%` indica parti per cento e non è un'unità SI. Scrivere `63.2 %` con uno spazio, non `63.2%`.

[BIPM SI Brochure, edition 9, revision June 2026](https://www.bipm.org/en/si-brochure-9) · [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
