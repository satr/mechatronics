# 数学符号与记法

**切换此页语言:** [en](../en/SYMBOLS.md) · [fr](../fr/SYMBOLS.md) · [de](../de/SYMBOLS.md) · [it](../it/SYMBOLS.md) · [es](../es/SYMBOLS.md) · [pt](../pt/SYMBOLS.md) · [zh](SYMBOLS.md) · [ja](../ja/SYMBOLS.md) · [nb](../nb/SYMBOLS.md) · [ru](../ru/SYMBOLS.md) · [ko](../ko/SYMBOLS.md) · [fi](../fi/SYMBOLS.md) · [pl](../pl/SYMBOLS.md)

**本页使用的单位（示例前先解释）:** `s` — 秒; `mm` — 毫米 = 0.001 m; `mm/s` — 毫米 / 秒 — 线速度; `kg·m²` — 千克 · 米² — 转动惯量; `N·m` — 牛顿 · 米 — 转矩; `N·m·s/rad` — 牛顿 · 米 · 秒 / 弧度 — 速度增益; `rpm` — 每分钟转数; `rad/s` — 弧度 / 秒 — 角速度; `%` — 百分比（百分之一）. [完整单位表](UNITS.md).

[← README](README.md) · [公式速查](CHEATSHEET.md) · [运动](notes/01-motion-calculus.md) · [动力学](notes/02-first-order-dynamics.md)

## 目录

- [求和：大写 sigma](#summation)
- [容易混淆的符号](#different-symbols)
- [Markdown 数学公式标记](#math-delimiters)
- [小数点、SI 单位及公式间距](#si-notation)

<a id="summation"></a>

## Σ / ∑ — 求和 (summation)

符号 $\sum$（希腊大写字母 sigma，**求和符号** / summation）表示把若干项加起来。在 $\sum_{n=0}^{N-1}(2nh)h$ 中，指标 $n$ 依次取 $0; 1; \ldots; N-1$，一共有 $N$ 项。可以把它想成 Python 的 `for` 循环累加。例如，$\sum_{n=1}^{3}n=1+2+3=6$。

<a id="different-symbols"></a>

## 外形相似的符号含义不同

小写 $\varepsilon(t)$（epsilon）表示速度误差 (speed error)；常数 $\mathrm{e}\approx2.71828$ 是欧拉数 (Euler’s number)。$\tau$（tau）表示时间常数 (time constant)，$\omega$（omega）表示角速度 (angular velocity)，$\alpha$（alpha）表示角加速度 (angular acceleration)，$\Delta$（delta）表示变化量 (change)。小写 $\sigma$（sigma）是另一个符号，在不同内容中可能表示标准差或应力，必须分别定义。

<a id="math-delimiters"></a>

## 为什么会出现美元符号 `$`？

在 Markdown **源文件**中，`$...$` 是行内公式的标记，`$$...$$` 是独立公式块的标记。这些美元符号不是公式的一部分，在 GitHub 的正常渲染页面中不应该显示。如果显示出来，请检查是否打开了源码视图、链接标题中是否含有数学标记，以及 Markdown 是否正确。

[GitHub — Markdown / MathJax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

<a id="si-notation"></a>

## 小数点、SI 单位及公式间距

全部语言版本都用小数点 `.`：`0.5`、`3.8`、`63.2 %`。逗号可以分隔列表项，但不能代替数值和单位之间的空格，也不能放在被积函数与微分 `dt` 之间。数值与单位之间留一个空格：`1 s`（秒，second）、`4 mm`（毫米，millimetre）、`10 mm/s`（毫米每秒，millimetres per second）。单位相乘用中点 `·`：`kg·m²`、`N·m·s/rad`；除号 `/` 两侧没有空格（`mm/s`）。公式中用 `\mathrm{kg}\cdot\mathrm{m}^2`，微分符号写作 `\mathrm{d}t`。采用小数点符合 [BIPM 国际单位制手册](https://www.bipm.org/en/publications/si-brochure)。程序中的 `dt` 是有限时间步长（time step）；积分中的 `\mathrm{d}t` 表示微分（differential）。


### rpm and rad/s

`rpm` 表示 **每分钟转数**（revolutions per minute），这是常见的**非 SI** 单位。SI 角速度单位是 `rad/s`（弧度每秒，radians per second）。换算为 `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`，所以 `1000 rpm ≈ 104.72 rad/s`。