# 导数公式表

**语言:** [en](../en/DERIVATIVE_TABLE.md) · [fr](../fr/DERIVATIVE_TABLE.md) · [de](../de/DERIVATIVE_TABLE.md) · [it](../it/DERIVATIVE_TABLE.md) · [es](../es/DERIVATIVE_TABLE.md) · [pt](../pt/DERIVATIVE_TABLE.md) · [zh](DERIVATIVE_TABLE.md) · [ja](../ja/DERIVATIVE_TABLE.md) · [nb](../nb/DERIVATIVE_TABLE.md) · [ru](../ru/DERIVATIVE_TABLE.md) · [ko](../ko/DERIVATIVE_TABLE.md) · [fi](../fi/DERIVATIVE_TABLE.md) · [pl](../pl/DERIVATIVE_TABLE.md)

**本页使用的单位（示例前先解释）:** `s` — 秒; `mm` — 毫米 = 0.001 m; `mm/s` — 毫米 / 秒 — 线速度; `mm/s²` — 毫米 / 秒² — 加速度. [完整单位表](UNITS.md).

[课程目录](README.md) · [积分公式表](INTEGRAL_TABLE.md) · [微积分基础](notes/00-calculus-foundations.md)

若 $u$ 和 $v$ 是 $x$ 的函数、$a$ 是常数，撇号表示对 $x$ 求导。角度以弧度计。只有在相应极限存在的地方，导数才有定义。复合函数使用链式法则（chain rule）。这里 $u'=\frac{\mathrm{d}u}{\mathrm{d}x}$，$v'=\frac{\mathrm{d}v}{\mathrm{d}x}$。

## 求导法则

| 函数 | 导数 | 条件 |
| --- | --- | --- |
| $c$ | $0$ | $c$ 常数 |
| $x$ | $1$ | — |
| $x^n$ | $nx^{n-1}$ | 实数 $n$；函数有定义且可导的范围内 |
| $u+v$ | $u'+v'$ | — |
| $au$ | $au'$ | $a$ 常数 |
| $uv$ | $u'v+uv'$ | 乘积求导法则 |
| $\frac{u}{v}$ | $\frac{u'v-uv'}{v^2}$ | $v\ne0$ |
| $f(u)$ | $f'(u)u'$ | 链式法则 |
| $\frac{1}{u}$ | $-\frac{u'}{u^2}$ | $u\ne0$ |
| $\sqrt{u}$ | $\frac{u'}{2\sqrt{u}}$ | $u>0$ |
| $\exp(u)$ | $\exp(u)u'$ | — |
| $a^u$ | $a^u\ln(a)u'$ | $a>0$ |
| $\ln(u)$ | $\frac{u'}{u}$ | $u>0$ |
| $\ln\lvert u\rvert$ | $\frac{u'}{u}$ | $u\ne0$ |
| $\sin(u)$ | $\cos(u)u'$ | — |
| $\cos(u)$ | $-\sin(u)u'$ | — |
| $\tan(u)$ | $\frac{u'}{\cos^2(u)}$ | $\cos(u)\ne0$ |
| $\arcsin(u)$ | $\frac{u'}{\sqrt{1-u^2}}$ | $-1<u<1$ |
| $\arccos(u)$ | $-\frac{u'}{\sqrt{1-u^2}}$ | $-1<u<1$ |
| $\arctan(u)$ | $\frac{u'}{1+u^2}$ | — |
| $\mathrm{arsinh}(u)$ | $\frac{u'}{\sqrt{1+u^2}}$ | — |

## 例题

**链式法则（chain rule）：** 对 $y=(3x^2+1)^4$，令 $u=3x^2+1$，则 $u'=6x$，因此

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=4u^3u'=24x(3x^2+1)^3.
$$

**速度与加速度：** 对于位置 $x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2$，对时间求导得到速度，再求导得到加速度：

$$
v(t)=\frac{\mathrm{d}x}{\mathrm{d}t}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t,
$$

$$
a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=4\ \mathrm{mm/s^2}.
$$

在 $t=2\ \mathrm{s}$ 时，速度为 $11\ \mathrm{mm/s}$。这只是数学示例，不是机器控制指令。

**反函数（inverse function）：** 若 $y=f^{-1}(x)$，$f$ 在 $y$ 处可导且 $f'(y)\ne0$，则在局部可逆的分支上，$(f^{-1})'(x)=1/f'(y)$。
