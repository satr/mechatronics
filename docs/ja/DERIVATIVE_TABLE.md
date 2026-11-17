# 導関数一覧

**言語:** [en](../en/DERIVATIVE_TABLE.md) · [fr](../fr/DERIVATIVE_TABLE.md) · [de](../de/DERIVATIVE_TABLE.md) · [it](../it/DERIVATIVE_TABLE.md) · [es](../es/DERIVATIVE_TABLE.md) · [pt](../pt/DERIVATIVE_TABLE.md) · [zh](../zh/DERIVATIVE_TABLE.md) · [ja](DERIVATIVE_TABLE.md) · [nb](../nb/DERIVATIVE_TABLE.md) · [ru](../ru/DERIVATIVE_TABLE.md) · [ko](../ko/DERIVATIVE_TABLE.md) · [fi](../fi/DERIVATIVE_TABLE.md) · [pl](../pl/DERIVATIVE_TABLE.md)

**このページの単位（例の前に説明）:** `s` — 秒; `mm` — ミリメートル = 0.001 m; `mm/s` — ミリメートル / 秒 — 線速度; `mm/s²` — ミリメートル / 秒² — 加速度. [単位一覧](UNITS.md).

[コース目次](README.md) · [積分公式表](INTEGRAL_TABLE.md) · [微積分の基礎](notes/00-calculus-foundations.md)

$u$ と $v$ は $x$ の関数、$a$ は定数とし、プライム記号は $x$ に関する微分を表します。角度はラジアンで測ります。導関数は対応する極限が存在する点でのみ定義されます。合成関数には連鎖律（chain rule）を使います。ここで $u'=\frac{\mathrm{d}u}{\mathrm{d}x}$、$v'=\frac{\mathrm{d}v}{\mathrm{d}x}$ です。

## 微分法則

| 関数 | 導関数 | 条件 |
| --- | --- | --- |
| $c$ | $0$ | $c$ 定数 |
| $x$ | $1$ | — |
| $x^n$ | $nx^{n-1}$ | 実数 $n$；関数が定義され微分可能な範囲 |
| $u+v$ | $u'+v'$ | — |
| $au$ | $au'$ | $a$ 定数 |
| $uv$ | $u'v+uv'$ | 積の微分法則 |
| $\frac{u}{v}$ | $\frac{u'v-uv'}{v^2}$ | $v\ne0$ |
| $f(u)$ | $f'(u)u'$ | 連鎖律 |
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

## 例題

**連鎖律（chain rule）：** $y=(3x^2+1)^4$ に対し、$u=3x^2+1$ とおきます。すると $u'=6x$ なので

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=4u^3u'=24x(3x^2+1)^3.
$$

**速度と加速度：** 位置 $x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2$ を時間で微分すると速度、さらに微分すると加速度になります：

$$
v(t)=\frac{\mathrm{d}x}{\mathrm{d}t}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t,
$$

$$
a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=4\ \mathrm{mm/s^2}.
$$

$t=2\ \mathrm{s}$ のとき速度は $11\ \mathrm{mm/s}$ です。これは数学上の例であり、機械の制御指示ではありません。

**逆関数（inverse function）：** $y=f^{-1}(x)$、$f$ が $y$ で微分可能、かつ $f'(y)\ne0$ なら、局所的に逆関数が存在する枝で $(f^{-1})'(x)=1/f'(y)$ です。
