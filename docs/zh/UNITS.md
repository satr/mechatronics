# 单位与量纲符号

**语言:** [en](../en/UNITS.md) · [fr](../fr/UNITS.md) · [de](../de/UNITS.md) · [it](../it/UNITS.md) · [es](../es/UNITS.md) · [pt](../pt/UNITS.md) · [zh](UNITS.md) · [ja](../ja/UNITS.md) · [nb](../nb/UNITS.md) · [ru](../ru/UNITS.md) · [ko](../ko/UNITS.md) · [fi](../fi/UNITS.md) · [pl](../pl/UNITS.md)

[课程目录](README.md) · [数学符号](SYMBOLS.md)

单位符号采用国际通用写法，不翻译。物理量变量用斜体，单位符号用正体。数值与单位之间留空格，平面角度符号 ° 除外；百分号 % 前也留空格。

| 符号 | English unit name | 中文含义 | SI 状态 |
| --- | --- | --- | --- |
| `m` | metre | 米 | SI base |
| `mm` | millimetre | 毫米 = 0.001 m | SI decimal submultiple |
| `s` | second | 秒 | SI base |
| `ms` | millisecond | 毫秒 = 0.001 s | SI decimal submultiple |
| `kg` | kilogram | 千克 | SI base |
| `A` | ampere | 安培 | SI base |
| `N` | newton | 牛顿 | SI derived |
| `J` | joule | 焦耳 | SI derived |
| `W` | watt | 瓦特 | SI derived |
| `rad` | radian | 弧度 | SI derived (unit one) |
| `°` | degree of plane angle | 度 | non-SI angle unit |
| `rpm` | revolution per minute | 每分钟转数 | non-SI |
| `%` | percent | 百分比（百分之一） | ratio; not an SI unit |
| `m/s` | metre per second | 米 / 秒 — 线速度 | SI derived |
| `mm/s` | millimetre per second | 毫米 / 秒 — 线速度 | SI decimal units |
| `m/s²` | metre per second squared | 米 / 秒² — 加速度 | SI derived |
| `mm/s²` | millimetre per second squared | 毫米 / 秒² — 加速度 | SI decimal units |
| `rad/s` | radian per second | 弧度 / 秒 — 角速度 | SI derived |
| `rad/s²` | radian per second squared | 弧度 / 秒² — 角加速度 | SI derived |
| `mm/rad` | millimetre per radian | 毫米 / 弧度 — 雅可比矩阵系数（长度与角度之比） | SI decimal units |
| `kg·m²` | kilogram metre squared | 千克 · 米² — 转动惯量 | SI derived |
| `N·m` | newton metre (torque) | 牛顿 · 米 — 转矩 | SI derived |
| `N·m·s/rad` | newton metre second per radian | 牛顿 · 米 · 秒 / 弧度 — 速度增益 | SI derived |
| `N/m` | newton per metre | 牛顿 / 米 — 刚度 | SI derived |
| `rpm/s` | revolutions per minute per second | 每分钟转数 / 秒 — 角加速度 | contains non-SI rpm |
| `A/rpm` | ampere per rpm | 安培 / (每分钟转数) — 速度增益 | contains non-SI rpm |
| `A/(rpm·s)` | ampere per rpm-second | 安培 / (每分钟转数 · 秒) — 积分增益 | contains non-SI rpm |
| `A·s/rpm` | ampere-second per rpm | 安培 · 秒 / (每分钟转数) — 微分增益 | contains non-SI rpm |
| `mm³/s` | cubic millimetre per second | 毫米³ / 秒 — 体积流量 | SI decimal units |
| `Hz` | hertz | 赫兹 — 频率 | SI derived |
| `min` | minute | 分钟 — 时间 | non-SI time unit |

## 换算和物理意义

- `1 mm = 0.001 m`; `1 ms = 0.001 s`; `1 min = 60 s`.
- `1° = π/180 rad`; `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m` — 焦耳与牛顿米在量纲上等价；转矩使用 `N·m`，能量使用 `J`。
- `N·m·s/rad` 表示转矩相对角速度的系数。`A/rpm`、`A/(rpm·s)` 和 `A·s/rpm` 分别是示例电流输出 PID 中的比例、积分、微分增益单位。
- `%` 表示百分之一，不是 SI 单位。按规范写成 `63.2 %`，而非 `63.2%`。

[BIPM SI Brochure, edition 9, revision June 2026](https://www.bipm.org/en/si-brochure-9) · [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
