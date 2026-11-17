# 도함수 공식표

**언어:** [en](../en/DERIVATIVE_TABLE.md) · [fr](../fr/DERIVATIVE_TABLE.md) · [de](../de/DERIVATIVE_TABLE.md) · [it](../it/DERIVATIVE_TABLE.md) · [es](../es/DERIVATIVE_TABLE.md) · [pt](../pt/DERIVATIVE_TABLE.md) · [zh](../zh/DERIVATIVE_TABLE.md) · [ja](../ja/DERIVATIVE_TABLE.md) · [nb](../nb/DERIVATIVE_TABLE.md) · [ru](../ru/DERIVATIVE_TABLE.md) · [ko](DERIVATIVE_TABLE.md) · [fi](../fi/DERIVATIVE_TABLE.md) · [pl](../pl/DERIVATIVE_TABLE.md)

**이 페이지의 단위(예제 전에 설명):** `s` — 초; `mm` — 밀리미터 = 0.001 m; `mm/s` — 밀리미터 / 초 — 선속도; `mm/s²` — 밀리미터 / 초² — 가속도. [단위 전체 목록](UNITS.md).

[목차](README.md) · [적분 공식표](INTEGRAL_TABLE.md) · [미적분 기초](notes/00-calculus-foundations.md)

u와 v는 x의 함수이고 a는 상수입니다. 각도는 라디안 단위입니다. 도함수는 해당 극한이 존재하는 곳에서 정의됩니다. 합성함수에는 연쇄 법칙을 적용합니다. 여기서 $u'=\frac{\mathrm{d}u}{\mathrm{d}x}$ 이고 $v'=\frac{\mathrm{d}v}{\mathrm{d}x}$.

## 미분 법칙

| 함수 | 도함수 | 조건 |
| --- | --- | --- |
| $c$ | $0$ | $c$ 상수 |
| $x$ | $1$ | — |
| $x^n$ | $nx^{n-1}$ | 실수 $n$; 함수가 정의되고 미분 가능한 곳 |
| $u+v$ | $u'+v'$ | — |
| $au$ | $au'$ | $a$ 상수 |
| $uv$ | $u'v+uv'$ | 곱의 미분법 |
| $\frac{u}{v}$ | $\frac{u'v-uv'}{v^2}$ | $v\ne0$ |
| $f(u)$ | $f'(u)u'$ | 연쇄 법칙 |
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

## 예제

**연쇄 법칙 (chain rule):** $y=(3x^2+1)^4$의 도함수를 구합니다. $u=3x^2+1$로 두면 $u'=6x$입니다. 따라서

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=4u^3u'=24x(3x^2+1)^3.
$$

**속도와 가속도 (velocity and acceleration):** 위치 함수가 다음과 같다고 가정합니다.

$$
x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2.
$$

시간에 대해 한 번 미분하면 속도, 두 번 미분하면 가속도가 됩니다.

$$
v(t)=\frac{\mathrm{d}x}{\mathrm{d}t}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t,
$$

$$
a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=4\ \mathrm{mm/s^2}.
$$

$t=2\ \mathrm{s}$일 때 속도는 $11\ \mathrm{mm/s}$입니다. 이 예제는 실제 기계의 제어 지침이 아닙니다.

**역함수 (inverse function):** $y=f^{-1}(x)$이고 $f$가 $y$에서 미분 가능하며 $f'(y)\ne0$이면, 국소적으로 역함수가 존재하는 구간에서 $(f^{-1})'(x)=1/f'(y)$입니다.
