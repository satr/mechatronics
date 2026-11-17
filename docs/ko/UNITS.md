# 측정 단위와 차원 표기

**언어:** [en](../en/UNITS.md) · [fr](../fr/UNITS.md) · [de](../de/UNITS.md) · [it](../it/UNITS.md) · [es](../es/UNITS.md) · [pt](../pt/UNITS.md) · [zh](../zh/UNITS.md) · [ja](../ja/UNITS.md) · [nb](../nb/UNITS.md) · [ru](../ru/UNITS.md) · [ko](UNITS.md) · [fi](../fi/UNITS.md) · [pl](../pl/UNITS.md)

[목차](README.md) · [수학 기호](SYMBOLS.md)

단위 기호는 국제적으로 동일하며 번역하지 않습니다. 물리량 변수는 이탤릭체, 단위 기호는 바른 글꼴로 씁니다. 숫자와 단위 사이에는 공백을 두며 각도의 °는 예외입니다. 퍼센트 기호 % 앞에도 공백을 둡니다.

| 기호 | English unit name | 한국어 의미 | SI 구분 |
| --- | --- | --- | --- |
| `m` | metre | 미터 | SI base |
| `mm` | millimetre | 밀리미터 = 0.001 m | SI decimal submultiple |
| `s` | second | 초 | SI base |
| `ms` | millisecond | 밀리초 = 0.001 s | SI decimal submultiple |
| `kg` | kilogram | 킬로그램 | SI base |
| `A` | ampere | 암페어 | SI base |
| `N` | newton | 뉴턴 | SI derived |
| `J` | joule | 줄 | SI derived |
| `W` | watt | 와트 | SI derived |
| `rad` | radian | 라디안 | SI derived (unit one) |
| `°` | degree of plane angle | 도 | non-SI angle unit |
| `rpm` | revolution per minute | 분당 회전수 | non-SI |
| `%` | percent | 퍼센트(100분의 1) | ratio; not an SI unit |
| `m/s` | metre per second | 미터 / 초 — 선속도 | SI derived |
| `mm/s` | millimetre per second | 밀리미터 / 초 — 선속도 | SI decimal units |
| `m/s²` | metre per second squared | 미터 / 초² — 가속도 | SI derived |
| `mm/s²` | millimetre per second squared | 밀리미터 / 초² — 가속도 | SI decimal units |
| `rad/s` | radian per second | 라디안 / 초 — 각속도 | SI derived |
| `rad/s²` | radian per second squared | 라디안 / 초² — 각가속도 | SI derived |
| `mm/rad` | millimetre per radian | 밀리미터 / 라디안 — 야코비 행렬 계수(각도당 길이) | SI decimal units |
| `kg·m²` | kilogram metre squared | 킬로그램 · 미터² — 관성 모멘트 | SI derived |
| `N·m` | newton metre (torque) | 뉴턴 · 미터 — 토크 | SI derived |
| `N·m·s/rad` | newton metre second per radian | 뉴턴 · 미터 · 초 / 라디안 — 속도에 대한 이득 | SI derived |
| `N/m` | newton per metre | 뉴턴 / 미터 — 강성 | SI derived |
| `rpm/s` | revolutions per minute per second | 분당 회전수 / 초 — 각가속도 | contains non-SI rpm |
| `A/rpm` | ampere per rpm | 암페어 / (분당 회전수) — 속도에 대한 이득 | contains non-SI rpm |
| `A/(rpm·s)` | ampere per rpm-second | 암페어 / (분당 회전수 · 초) — 적분 이득 | contains non-SI rpm |
| `A·s/rpm` | ampere-second per rpm | 암페어 · 초 / (분당 회전수) — 미분 이득 | contains non-SI rpm |
| `mm³/s` | cubic millimetre per second | 밀리미터³ / 초 — 체적 유량 | SI decimal units |
| `Hz` | hertz | 헤르츠 — 주파수 | SI derived |
| `min` | minute | 분 — 시간 | non-SI time unit |

## 단위 변환과 물리적 의미

- `1 mm = 0.001 m`; `1 ms = 0.001 s`; `1 min = 60 s`.
- `1° = π/180 rad`; `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m` — 줄과 뉴턴미터는 차원이 같지만, 토크는 `N·m`, 에너지는 `J`로 표시합니다.
- `N·m·s/rad` 는 각속도에 대한 토크 계수입니다. `A/rpm`, `A/(rpm·s)`, `A·s/rpm`는 교육용 전류 출력 PID 모델에서 P, I, D 이득의 단위입니다.
- `%` 는 100분의 1을 뜻하며 SI 단위가 아닙니다. `63.2%`가 아니라 공백을 둔 `63.2 %`로 표기합니다.

[BIPM SI Brochure, edition 9, revision June 2026](https://www.bipm.org/en/si-brochure-9) · [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
