# 积分公式表

**阅读语言:** [en](../en/INTEGRAL_TABLE.md) · [fr](../fr/INTEGRAL_TABLE.md) · [de](../de/INTEGRAL_TABLE.md) · [it](../it/INTEGRAL_TABLE.md) · [es](../es/INTEGRAL_TABLE.md) · [pt](../pt/INTEGRAL_TABLE.md) · [zh](INTEGRAL_TABLE.md) · [ja](../ja/INTEGRAL_TABLE.md) · [nb](../nb/INTEGRAL_TABLE.md) · [ru](../ru/INTEGRAL_TABLE.md) · [ko](../ko/INTEGRAL_TABLE.md) · [fi](../fi/INTEGRAL_TABLE.md) · [pl](../pl/INTEGRAL_TABLE.md)

**本页使用的单位（示例前先解释）:** `s` — 秒; `mm` — 毫米 = 0.001 m; `mm/s` — 毫米 / 秒 — 线速度; `mm/s²` — 毫米 / 秒² — 加速度; `N` — 牛顿; `m` — 米; `N/m` — 牛顿 / 米 — 刚度; `J` — 焦耳. [完整单位表](UNITS.md).

[README](README.md) · [0. 微积分基础：导数、微分与积分](notes/00-calculus-foundations.md) · [符号](SYMBOLS.md)

每个不定积分（indefinite integral）都包含积分常数 +C。参数 a 为常数；公式只在被积函数有定义的区间使用。三角函数角度使用弧度（rad，radian）。

建议先掌握多项式积分，再学习三角函数及根式积分。

## 目录

- [幂函数与对数](#section-1)
- [指数函数](#section-2)
- [三角函数](#section-3)
- [有理式与反三角函数](#section-4)
- [扩展参考：根式及倒数三角函数](#section-5)
- [如何选择公式并验证答案](#section-6)

<a id="section-1"></a>
## 1. 幂函数与对数

| 积分公式 | 条件与含义 |
| --- | --- |
| $\int 1\ \mathrm{d}x=x+C$ | 所有实数 $x$ |
| $\int x^n\ \mathrm{d}x=\frac{x^{n+1}}{n+1}+C$ | $n\ne-1$; 注意实数幂函数的定义域 |
| $\int\frac{1}{x}\ \mathrm{d}x=\ln\lvert x\rvert+C$ | $x\ne0$ |

<a id="section-2"></a>
## 2. 指数函数

| 积分公式 | 条件与含义 |
| --- | --- |
| $\int \mathrm{e}^{x}\ \mathrm{d}x=\mathrm{e}^{x}+C$ | 所有实数 $x$ |
| $\int a^x\ \mathrm{d}x=\frac{a^x}{\ln a}+C$ | $a>0$, $a\ne1$ |

<a id="section-3"></a>
## 3. 三角函数

| 积分公式 | 条件与含义 |
| --- | --- |
| $\int\sin x\ \mathrm{d}x=-\cos x+C$ | $x$ 以弧度为单位 |
| $\int\cos x\ \mathrm{d}x=\sin x+C$ | $x$ 以弧度为单位 |
| $\int\frac{1}{\cos^2 x}\ \mathrm{d}x=\tan x+C$ | $\cos x\ne0$ |
| $\int\frac{1}{\sin^2 x}\ \mathrm{d}x=-\cot x+C$ | $\sin x\ne0$ |

<a id="section-4"></a>
## 4. 有理式与反三角函数

| 积分公式 | 条件与含义 |
| --- | --- |
| $\int\frac{1}{1+x^2}\ \mathrm{d}x=\arctan x+C$ | 所有实数 $x$ |
| $\int\frac{1}{\sqrt{1-x^2}}\ \mathrm{d}x=\arcsin x+C$ | $\lvert x\rvert<1$ |
| $\int\frac{1}{a^2+x^2}\ \mathrm{d}x=\frac{1}{a}\arctan\frac{x}{a}+C$ | $a>0$ |
| $\int\frac{1}{a^2-x^2}\ \mathrm{d}x=\frac{1}{2a}\ln\left\lvert\frac{a+x}{a-x}\right\rvert+C$ | $a>0$, $x\ne\pm a$ |
| $\int\frac{1}{\sqrt{a^2-x^2}}\ \mathrm{d}x=\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |

<a id="section-5"></a>
## 5. 扩展参考：根式及倒数三角函数

| 积分公式 | 条件与含义 |
| --- | --- |
| $\int\frac{1}{\sqrt{x^2+a^2}}\ \mathrm{d}x=\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{a^2-x^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{a^2-x^2}+\frac{a^2}{2}\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |
| $\int\sqrt{x^2+a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2+a^2}+\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{x^2-a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2-a^2}-\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2-a^2}\right\rvert+C$ | $a>0$, $\lvert x\rvert>a$ |
| $\int\frac{1}{\sin x}\ \mathrm{d}x=\ln\left\lvert\tan\frac{x}{2}\right\rvert+C$ | $\sin x\ne0$; 不跨越奇点的区间 |
| $\int\frac{1}{\cos x}\ \mathrm{d}x=\ln\left\lvert\tan\left(\frac{x}{2}+\frac{\pi}{4}\right)\right\rvert+C$ | $\cos x\ne0$; 不跨越奇点的区间 |

## 验证公式

对等式右侧求导即可验证积分公式。对于幂函数，积分正好是求导法则的逆操作。

对数的自变量必须是无量纲的；除非提供参考尺度，此处 x 视为无量纲。带 ± 的公式必须按具体被积式和定义域选择，不能随意组合。

<a id="section-6"></a>
## 6. 如何选择公式并验证答案

首先确定微分符号后的积分变量（dx、dt 或 dθ）。只有与该变量无关的系数才可作为常数。不定积分加 C；定积分先求原函数 F，再算 F(b) − F(a)。对结果求导可验证。

### 例题 A — 由速度计算位移

在 0–2 s 内，若 v(t) = 3 mm/s + (4 mm/s²)t，逐项积分：

$$
\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}
=14\ \mathrm{mm}.
$$

结果为 14 mm，而非 14 mm/s：速度对时间积分就是位移。

### 例题 B — 变力所做的功

弹簧 F(x) = kx、k = 200 N/m，从 0 拉伸到 0.01 m：

$$
\int_0^{0.01\ \mathrm{m}}(200\ \mathrm{N/m})x\ \mathrm{d}x
=\left[(100\ \mathrm{N/m})x^2\right]_0^{0.01\ \mathrm{m}}=0.01\ \mathrm{J}.
$$

结果为 0.01 J。不能用最终力乘全部位移，因为力随伸长量改变。

### 例题 C — 简单函数产生对数

1/x 的一个原函数是 ln|x|。令无量纲 x 从 1 到 2：

$$
\int_1^2\frac1x\ \mathrm{d}x=[\ln x]_1^2=\ln2-\ln1=\ln2\approx0.693.
$$

结果为 ln 2 ≈ 0.693。x 是无量纲比值，并非有单位的长度。
