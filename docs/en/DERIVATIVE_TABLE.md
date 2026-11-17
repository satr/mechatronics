# Derivative reference table

**Languages:** [en](DERIVATIVE_TABLE.md) · [fr](../fr/DERIVATIVE_TABLE.md) · [de](../de/DERIVATIVE_TABLE.md) · [it](../it/DERIVATIVE_TABLE.md) · [es](../es/DERIVATIVE_TABLE.md) · [pt](../pt/DERIVATIVE_TABLE.md) · [zh](../zh/DERIVATIVE_TABLE.md) · [ja](../ja/DERIVATIVE_TABLE.md) · [nb](../nb/DERIVATIVE_TABLE.md) · [ru](../ru/DERIVATIVE_TABLE.md) · [ko](../ko/DERIVATIVE_TABLE.md) · [fi](../fi/DERIVATIVE_TABLE.md) · [pl](../pl/DERIVATIVE_TABLE.md)

**Units used here (defined before the examples):** `s` — second; `mm` — millimetre = 0.001 m; `mm/s` — millimetre / second — linear speed; `mm/s²` — millimetre / second² — acceleration. [Full unit reference](UNITS.md).

[Course index](README.md) · [Integral table](INTEGRAL_TABLE.md) · [Calculus foundations](notes/00-calculus-foundations.md)

If u and v depend on x, a is constant, and primes mean differentiation with respect to x. Angles are in radians. The derivative is defined where the relevant limit exists. For composite functions use the chain rule. Here $u'=\frac{\mathrm{d}u}{\mathrm{d}x}$ and $v'=\frac{\mathrm{d}v}{\mathrm{d}x}$.

## Rules

| Function | Derivative | Conditions |
| --- | --- | --- |
| $c$ | $0$ | $c$ constant |
| $x$ | $1$ | — |
| $x^n$ | $nx^{n-1}$ | real $n$; where defined and differentiable |
| $u+v$ | $u'+v'$ | — |
| $au$ | $au'$ | $a$ constant |
| $uv$ | $u'v+uv'$ | product rule |
| $\frac{u}{v}$ | $\frac{u'v-uv'}{v^2}$ | $v\ne0$ |
| $f(u)$ | $f'(u)u'$ | chain rule |
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

## Examples

**Chain rule:** For $y=(3x^2+1)^4$, set $u=3x^2+1$. Then $u'=6x$ and

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=4u^3u'=24x(3x^2+1)^3.
$$

**Velocity and acceleration:** With $x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2$,

$$
v(t)=\frac{\mathrm{d}x}{\mathrm{d}t}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t,
$$

$$
a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=4\ \mathrm{mm/s^2}.
$$

At $t=2\ \mathrm{s}$, $v=11\ \mathrm{mm/s}$. This is a mathematical example, not a machine-control instruction.

**Inverse functions:** If $y=f^{-1}(x)$, $f$ is differentiable at $y$, and $f'(y)\ne0$, then $(f^{-1})'(x)=1/f'(y)$. This requires a locally invertible branch.
