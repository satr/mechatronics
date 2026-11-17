# Mittayksiköt ja dimensioiden merkintä

**Kielet:** [en](../en/UNITS.md) · [fr](../fr/UNITS.md) · [de](../de/UNITS.md) · [it](../it/UNITS.md) · [es](../es/UNITS.md) · [pt](../pt/UNITS.md) · [zh](../zh/UNITS.md) · [ja](../ja/UNITS.md) · [nb](../nb/UNITS.md) · [ru](../ru/UNITS.md) · [ko](../ko/UNITS.md) · [fi](UNITS.md) · [pl](../pl/UNITS.md)

[Sisällysluettelo](README.md) · [Matemaattiset symbolit](SYMBOLS.md)

Yksiköiden tunnukset ovat kansainvälisiä eikä niitä käännetä. Suuresymbolit kirjoitetaan kursiivilla ja yksikkötunnukset pystyllä kirjasimella. Luvun ja yksikön väliin tulee välilyönti; tasokulman aste ° on poikkeus. Myös prosenttimerkin % edelle tulee välilyönti.

| Tunnus | English unit name | Merkitys suomeksi | SI-luokitus |
| --- | --- | --- | --- |
| `m` | metre | metri | SI base |
| `mm` | millimetre | millimetri = 0.001 m | SI decimal submultiple |
| `s` | second | sekunti | SI base |
| `ms` | millisecond | millisekunti = 0.001 s | SI decimal submultiple |
| `kg` | kilogram | kilogramma | SI base |
| `A` | ampere | ampeeri | SI base |
| `N` | newton | newton | SI derived |
| `J` | joule | joule | SI derived |
| `W` | watt | watti | SI derived |
| `rad` | radian | radiaani | SI derived (unit one) |
| `°` | degree of plane angle | aste | non-SI angle unit |
| `rpm` | revolution per minute | kierros minuutissa | non-SI |
| `%` | percent | prosentti (sadasosa) | ratio; not an SI unit |
| `m/s` | metre per second | metri / sekunti — lineaarinen nopeus | SI derived |
| `mm/s` | millimetre per second | millimetri / sekunti — lineaarinen nopeus | SI decimal units |
| `m/s²` | metre per second squared | metri / sekunti² — kiihtyvyys | SI derived |
| `mm/s²` | millimetre per second squared | millimetri / sekunti² — kiihtyvyys | SI decimal units |
| `rad/s` | radian per second | radiaani / sekunti — kulmanopeus | SI derived |
| `rad/s²` | radian per second squared | radiaani / sekunti² — kulmakiihtyvyys | SI derived |
| `mm/rad` | millimetre per radian | millimetri / radiaani — Jacobimatriisin kerroin (pituus kulmaa kohti) | SI decimal units |
| `kg·m²` | kilogram metre squared | kilogramma · metri² — hitausmomentti | SI derived |
| `N·m` | newton metre (torque) | newton · metri — vääntömomentti | SI derived |
| `N·m·s/rad` | newton metre second per radian | newton · metri · sekunti / radiaani — nopeuteen suhteutettu vahvistus | SI derived |
| `N/m` | newton per metre | newton / metri — jäykkyys | SI derived |
| `rpm/s` | revolutions per minute per second | kierros minuutissa / sekunti — kulmakiihtyvyys | contains non-SI rpm |
| `A/rpm` | ampere per rpm | ampeeri / (kierros minuutissa) — nopeuteen suhteutettu vahvistus | contains non-SI rpm |
| `A/(rpm·s)` | ampere per rpm-second | ampeeri / (kierros minuutissa · sekunti) — integraalivahvistus | contains non-SI rpm |
| `A·s/rpm` | ampere-second per rpm | ampeeri · sekunti / (kierros minuutissa) — derivointivahvistus | contains non-SI rpm |
| `mm³/s` | cubic millimetre per second | millimetri³ / sekunti — tilavuusvirta | SI decimal units |
| `Hz` | hertz | hertsi — taajuus | SI derived |
| `min` | minute | minuutti — aika | non-SI time unit |

## Muunnokset ja fysikaalinen merkitys

- `1 mm = 0.001 m`; `1 ms = 0.001 s`; `1 min = 60 s`.
- `1° = π/180 rad`; `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m` — Joulen ja newtonmetrin dimensio on sama: vääntömomentin yksikkönä käytetään `N·m` ja energian yksikkönä `J`.
- `N·m·s/rad` on vääntömomentin kerroin kulmanopeutta kohden. `A/rpm`, `A/(rpm·s)` ja `A·s/rpm` ovat esimerkin virtalähtöisen PID-säätimen P-, I- ja D-vahvistusten yksiköt.
- `%` tarkoittaa sadasosaa eikä ole SI-yksikkö. Kirjoita `63.2 %` välilyönnillä, ei `63.2%`.

[BIPM SI Brochure, edition 9, revision June 2026](https://www.bipm.org/en/si-brochure-9) · [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
