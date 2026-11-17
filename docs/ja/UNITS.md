# 単位と次元の表記

**言語:** [en](../en/UNITS.md) · [fr](../fr/UNITS.md) · [de](../de/UNITS.md) · [it](../it/UNITS.md) · [es](../es/UNITS.md) · [pt](../pt/UNITS.md) · [zh](../zh/UNITS.md) · [ja](UNITS.md) · [nb](../nb/UNITS.md) · [ru](../ru/UNITS.md) · [ko](../ko/UNITS.md) · [fi](../fi/UNITS.md) · [pl](../pl/UNITS.md)

[コース目次](README.md) · [数学記号](SYMBOLS.md)

単位記号は国際共通であり翻訳しません。物理量を表す変数は斜体、単位記号は立体で書きます。数値と単位の間には空白を置きますが角度の ° は例外です。% の前にも空白を置きます。

| 記号 | English unit name | 日本語での意味 | SI の区分 |
| --- | --- | --- | --- |
| `m` | metre | メートル | SI base |
| `mm` | millimetre | ミリメートル = 0.001 m | SI decimal submultiple |
| `s` | second | 秒 | SI base |
| `ms` | millisecond | ミリ秒 = 0.001 s | SI decimal submultiple |
| `kg` | kilogram | キログラム | SI base |
| `A` | ampere | アンペア | SI base |
| `N` | newton | ニュートン | SI derived |
| `J` | joule | ジュール | SI derived |
| `W` | watt | ワット | SI derived |
| `rad` | radian | ラジアン | SI derived (unit one) |
| `°` | degree of plane angle | 度 | non-SI angle unit |
| `rpm` | revolution per minute | 毎分回転数 | non-SI |
| `%` | percent | パーセント（百分の一） | ratio; not an SI unit |
| `m/s` | metre per second | メートル / 秒 — 線速度 | SI derived |
| `mm/s` | millimetre per second | ミリメートル / 秒 — 線速度 | SI decimal units |
| `m/s²` | metre per second squared | メートル / 秒² — 加速度 | SI derived |
| `mm/s²` | millimetre per second squared | ミリメートル / 秒² — 加速度 | SI decimal units |
| `rad/s` | radian per second | ラジアン / 秒 — 角速度 | SI derived |
| `rad/s²` | radian per second squared | ラジアン / 秒² — 角加速度 | SI derived |
| `mm/rad` | millimetre per radian | ミリメートル / ラジアン — ヤコビ行列の係数（角度当たりの長さ） | SI decimal units |
| `kg·m²` | kilogram metre squared | キログラム · メートル² — 慣性モーメント | SI derived |
| `N·m` | newton metre (torque) | ニュートン · メートル — トルク | SI derived |
| `N·m·s/rad` | newton metre second per radian | ニュートン · メートル · 秒 / ラジアン — 速度に対するゲイン | SI derived |
| `N/m` | newton per metre | ニュートン / メートル — 剛性 | SI derived |
| `rpm/s` | revolutions per minute per second | 毎分回転数 / 秒 — 角加速度 | contains non-SI rpm |
| `A/rpm` | ampere per rpm | アンペア / (毎分回転数) — 速度に対するゲイン | contains non-SI rpm |
| `A/(rpm·s)` | ampere per rpm-second | アンペア / (毎分回転数 · 秒) — 積分ゲイン | contains non-SI rpm |
| `A·s/rpm` | ampere-second per rpm | アンペア · 秒 / (毎分回転数) — 微分ゲイン | contains non-SI rpm |
| `mm³/s` | cubic millimetre per second | ミリメートル³ / 秒 — 体積流量 | SI decimal units |
| `Hz` | hertz | ヘルツ — 周波数 | SI derived |
| `min` | minute | 分 — 時間 | non-SI time unit |

## 換算と物理的意味

- `1 mm = 0.001 m`; `1 ms = 0.001 s`; `1 min = 60 s`.
- `1° = π/180 rad`; `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m` — ジュールとニュートンメートルは次元が同じです。トルクには `N·m`、エネルギーには `J` を使います。
- `N·m·s/rad` は角速度に対するトルクの係数です。`A/rpm`、`A/(rpm·s)`、`A·s/rpm` は教材の電流出力 PID における P、I、D ゲインの単位です。
- `%` は百分の一を表し、SI 単位ではありません。`63.2%` ではなく空白を入れて `63.2 %` と記します。

[BIPM SI Brochure, edition 9, revision June 2026](https://www.bipm.org/en/si-brochure-9) · [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
