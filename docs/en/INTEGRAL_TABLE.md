# Integral reference table

**Read this page in:** [en](INTEGRAL_TABLE.md) · [fr](../fr/INTEGRAL_TABLE.md) · [de](../de/INTEGRAL_TABLE.md) · [it](../it/INTEGRAL_TABLE.md) · [es](../es/INTEGRAL_TABLE.md) · [pt](../pt/INTEGRAL_TABLE.md) · [zh](../zh/INTEGRAL_TABLE.md) · [ja](../ja/INTEGRAL_TABLE.md) · [nb](../nb/INTEGRAL_TABLE.md) · [ru](../ru/INTEGRAL_TABLE.md) · [ko](../ko/INTEGRAL_TABLE.md) · [fi](../fi/INTEGRAL_TABLE.md) · [pl](../pl/INTEGRAL_TABLE.md)

**Units used here (defined before the examples):** `s` — second; `mm` — millimetre = 0.001 m; `mm/s` — millimetre / second — linear speed; `mm/s²` — millimetre / second² — acceleration; `N` — newton; `m` — metre; `N/m` — newton / metre — stiffness; `J` — joule. [Full unit reference](UNITS.md).

[README](README.md) · [0. Calculus foundations: derivatives, differentials, and integrals](notes/00-calculus-foundations.md) · [Symbols](SYMBOLS.md) · [Trigonometry](TRIGONOMETRY.md)

All indefinite integrals include +C, a constant of integration. Parameters a are constant, and functions are considered on intervals where the integrands are defined. Trigonometric arguments are in radians.

Start with polynomial integrals before using the optional trigonometric and radical formulas.

## Contents

- [Basic power and logarithm](#section-1)
- [Exponential functions](#section-2)
- [Trigonometric functions](#section-3)
- [Rational and inverse trigonometric forms](#section-4)
- [Further reference: radicals and reciprocals](#section-5)
- [How to choose and verify a formula](#section-6)

<a id="section-1"></a>
## 1. Basic power and logarithm

| Formula | Conditions / meaning |
| --- | --- |
| $\int 1\ \mathrm{d}x=x+C$ | all real $x$ |
| $\int x^n\ \mathrm{d}x=\frac{x^{n+1}}{n+1}+C$ | $n\ne-1$; real powers need their real domain |
| $\int\frac{1}{x}\ \mathrm{d}x=\ln\lvert x\rvert+C$ | $x\ne0$ |

<a id="section-2"></a>
## 2. Exponential functions

| Formula | Conditions / meaning |
| --- | --- |
| $\int \mathrm{e}^{x}\ \mathrm{d}x=\mathrm{e}^{x}+C$ | all real $x$ |
| $\int a^x\ \mathrm{d}x=\frac{a^x}{\ln a}+C$ | $a>0$, $a\ne1$ |

<a id="section-3"></a>
## 3. Trigonometric functions

| Formula | Conditions / meaning |
| --- | --- |
| $\int\sin x\ \mathrm{d}x=-\cos x+C$ | $x$ in radians |
| $\int\cos x\ \mathrm{d}x=\sin x+C$ | $x$ in radians |
| $\int\frac{1}{\cos^2 x}\ \mathrm{d}x=\tan x+C$ | $\cos x\ne0$ |
| $\int\frac{1}{\sin^2 x}\ \mathrm{d}x=-\cot x+C$ | $\sin x\ne0$ |

<a id="section-4"></a>
## 4. Rational and inverse trigonometric forms

| Formula | Conditions / meaning |
| --- | --- |
| $\int\frac{1}{1+x^2}\ \mathrm{d}x=\arctan x+C$ | all real $x$ |
| $\int\frac{1}{\sqrt{1-x^2}}\ \mathrm{d}x=\arcsin x+C$ | $\lvert x\rvert<1$ |
| $\int\frac{1}{a^2+x^2}\ \mathrm{d}x=\frac{1}{a}\arctan\frac{x}{a}+C$ | $a>0$ |
| $\int\frac{1}{a^2-x^2}\ \mathrm{d}x=\frac{1}{2a}\ln\left\lvert\frac{a+x}{a-x}\right\rvert+C$ | $a>0$, $x\ne\pm a$ |
| $\int\frac{1}{\sqrt{a^2-x^2}}\ \mathrm{d}x=\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |

<a id="section-5"></a>
## 5. Further reference: radicals and reciprocals

| Formula | Conditions / meaning |
| --- | --- |
| $\int\frac{1}{\sqrt{x^2+a^2}}\ \mathrm{d}x=\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{a^2-x^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{a^2-x^2}+\frac{a^2}{2}\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |
| $\int\sqrt{x^2+a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2+a^2}+\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{x^2-a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2-a^2}-\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2-a^2}\right\rvert+C$ | $a>0$, $\lvert x\rvert>a$ |
| $\int\frac{1}{\sin x}\ \mathrm{d}x=\ln\left\lvert\tan\frac{x}{2}\right\rvert+C$ | $\sin x\ne0$; intervals not crossing poles |
| $\int\frac{1}{\cos x}\ \mathrm{d}x=\ln\left\lvert\tan\left(\frac{x}{2}+\frac{\pi}{4}\right)\right\rvert+C$ | $\cos x\ne0$; intervals not crossing poles |

## How to check

Differentiate the right-hand side to check any entry. For the elementary power rule, do the reverse operation and verify the exponent and coefficient.

A logarithm of a dimensional quantity requires a dimensionless argument; formulas here use dimensionless x unless a reference scale is supplied. Choose each formula only on the stated real domain.

<a id="section-6"></a>
## 6. How to choose and verify a formula

First identify the variable after the differential (dx, dt, or dθ). Keep coefficients constant only when they truly are constant. For an indefinite integral add C; for a definite integral find an antiderivative F and calculate F(b) − F(a). Check by differentiating your answer.

### Worked example A — displacement from measured velocity

For a simple axis model v(t) = 3 mm/s + (4 mm/s²)t over 0–2 s, integrate each term:

$$
\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}
=14\ \mathrm{mm}.
$$

The result is 14 mm, not 14 mm/s. The integral accumulated velocity over time.

### Worked example B — work of a linearly increasing force

For a spring F(x) = kx, k = 200 N/m, extended from 0 to 0.01 m:

$$
\int_0^{0.01\ \mathrm{m}}(200\ \mathrm{N/m})x\ \mathrm{d}x
=\left[(100\ \mathrm{N/m})x^2\right]_0^{0.01\ \mathrm{m}}=0.01\ \mathrm{J}.
$$

The result is 0.01 J. Integrating force over displacement gives mechanical work; multiplying just the final force by the entire distance would overestimate it.

### Worked example C — logarithm from a simple rate law

The primitive of 1/x is ln|x|. For a dimensionless ratio x from 1 to 2:

$$
\int_1^2\frac1x\ \mathrm{d}x=[\ln x]_1^2=\ln2-\ln1=\ln2\approx0.693.
$$

The result is ln 2 ≈ 0.693. This is not the log of a length in meters; x is dimensionless.
