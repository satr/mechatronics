# 1. Motion, derivatives, and integrals

**Read this page in:** [en](01-motion-calculus.md) · [fr](../../fr/notes/01-motion-calculus.md) · [de](../../de/notes/01-motion-calculus.md) · [it](../../it/notes/01-motion-calculus.md) · [es](../../es/notes/01-motion-calculus.md) · [pt](../../pt/notes/01-motion-calculus.md) · [zh](../../zh/notes/01-motion-calculus.md) · [ja](../../ja/notes/01-motion-calculus.md) · [nb](../../nb/notes/01-motion-calculus.md) · [ru](../../ru/notes/01-motion-calculus.md) · [ko](../../ko/notes/01-motion-calculus.md) · [fi](../../fi/notes/01-motion-calculus.md) · [pl](../../pl/notes/01-motion-calculus.md)

**Units used here (defined before the examples):** `s` — second; `mm` — millimetre = 0.001 m; `mm/s` — millimetre / second — linear speed; `mm/s²` — millimetre / second² — acceleration; `%` — percent (one part in a hundred). [Full unit reference](../UNITS.md).

**Calculus refresher:** [0. Calculus foundations: derivatives, differentials, and integrals](00-calculus-foundations.md) · [Integral reference table](../INTEGRAL_TABLE.md)


[Contents](../README.md) · [Cheat sheet](../CHEATSHEET.md) · [Exercises](../exercises/README.md) · [Next chapter](02-first-order-dynamics.md)

> **Accuracy notice:** The following is a simplified, one-dimensional model. Validate units, coordinate conventions, and numerical accuracy before adapting it.

## Quick review

- **Distance traveled** is the total length of a path; **displacement** is final position minus initial position.
- **Speed** is nonnegative; **velocity** includes direction and may be negative along a chosen axis.
- Differentiating position with respect to time produces instantaneous velocity. Integrating signed velocity produces displacement.
- **Explicit Euler integration** approximates a changing quantity by holding its derivative constant during a short time step.

## On this page

- [1. Distance, displacement, speed, and velocity](#section-1)
- [2. Derivative: instantaneous velocity](#section-2)
- [3. Integral: displacement and traveled distance](#section-3)
- [4. Numerical integration](#section-4)
- [5. Try it](#section-5)
- [6. Further details (optional)](#section-6)
  - [Why the derivative of 2t² is 4t](#power-rule-derivation)
  - [Where the displacement table values come from](#motion-values-derivation)

[SI notation and decimal points](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Distance, displacement, speed, and velocity

For derivations, units, and numerical limitations, see [Further details](#section-6).

Take a virtual axis that moves at $+3\ \mathrm{mm/s}$ for two seconds, then $-3\ \mathrm{mm/s}$ for another two seconds. Its displacement is $+6-6=0\ \mathrm{mm}$ but it travels $6+6=12\ \mathrm{mm}$. During either segment, speed is $3\ \mathrm{mm/s}$; the signed velocity changes direction.

For a time interval $[t_1,t_2]$:

$$
\text{average velocity}=\frac{x(t_2)-x(t_1)}{t_2-t_1},\qquad
\text{average speed}=\frac{\text{total distance traveled}}{t_2-t_1}.
$$

In two or three dimensions, velocity is a vector. An object moving around a circle at a constant speed changes its velocity because its direction changes. Its average velocity over one full revolution is zero if it returns to its starting point.

Over the **entire four-second interval**, mean signed velocity and mean speed produce **different results**. The axis returns to its starting position but covers 12 mm of distance:

$$
\overline{v}_x=\frac{0\ \mathrm{mm}}{4\ \mathrm{s}}=0\ \mathrm{mm/s}
$$

$$
\overline{\lvert v\rvert}=\frac{12\ \mathrm{mm}}{4\ \mathrm{s}}=3\ \mathrm{mm/s}
$$

Average speed is therefore **not necessarily the magnitude of average velocity**. After a full revolution on a circle, the mean velocity vector is likewise zero, although the traveled distance and average speed are positive.

<a id="section-2"></a>

## 2. Derivative: instantaneous velocity

For a differentiable position function $x(t)$:

$$
v(t)=\frac{dx}{dt}.
$$

For $x(t)=2t^2\ \mathrm{mm}$, with $t$ measured in seconds, $v(t)=4t\ \mathrm{mm/s}$. **Why 4?** The power rule gives $d(t^2)/dt=2t$, so differentiating $2t^2$ gives $2\cdot2t=4t$. [See the full calculation and units](#power-rule-derivation). At $t=1\ \mathrm{s}$ the instantaneous velocity is $4\ \mathrm{mm/s}$.

A forward finite-difference approximation is

$$
v(t)\approx\frac{x(t+\Delta t)-x(t)}{\Delta t}.
$$

With $t=1\ \mathrm{s}$, steps $\Delta t=1; 0.1; 0.01\ \mathrm{s}$ yield $6; 4.2; 4.02\ \mathrm{mm/s}$ respectively. Smaller steps approach the derivative here; floating-point roundoff eventually limits accuracy.

**Why an excessively small step can fail:** at $t=1\ \mathrm{s}$, the true derivative of $x(t)=2t^2$ is $4\ \mathrm{mm/s}$. With $dt=1e-17\ \mathrm{s}$, ordinary Python floating-point arithmetic rounds `t + dt` back to `t`. The two computed positions are identical and their difference would wrongly suggest zero velocity. At other tiny scales, both position values can underflow to zero even when the derivative is nonzero. The synthetic [`forward_derivative`](../../../exercises/01_motion_and_integral.py) example now raises `ValueError` in these cases instead of reporting a false zero. It still computes an actual finite difference; choose a resolvable step rather than shrinking it without limit.

<a id="section-3"></a>

## 3. Integral: displacement and traveled distance

For signed one-dimensional velocity $v(t)$:

$$
x(t_2)-x(t_1)=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t,\qquad
s=\int_{t_1}^{t_2}|v(t)|\ \mathrm{d}t.
$$

The first integral can be negative or zero; the second cannot be negative. The integral corresponds geometrically to signed area under a velocity-time curve. **This is a separate example from Section 2:** the earlier position $x(t)=2t^2$ has derivative $v(t)=4t$, whereas the following integration example deliberately uses $v(t)=2t$. Its corresponding position is $x(t)=t^2+C$ (with consistent units). If $v(t)=2t\ \mathrm{mm/s}$ for $0\le t\le2\ \mathrm{s}$, displacement is $4\ \mathrm{mm}$.

<a id="section-4"></a>

## 4. Numerical integration

Exact displacement versus the left-endpoint Euler approximation (synthetic data).

![Exact displacement versus the left-endpoint Euler approximation (synthetic data)](../../../assets/figures/euler_vs_exact.svg)

Explicit Euler uses the derivative at the **start** of each interval:

$$
x_{n+1}=x_n+v(t_n)\ \Delta t.
$$

For $v(t)=2t\ \mathrm{mm/s}$ from $t=0$ to $2\ \mathrm{s}$:

| Time step $\Delta t$ | Euler displacement |
| ---: | ---: |
| $0.5\ \mathrm{s}$ | $3.000\ \mathrm{mm}$ |
| $0.1\ \mathrm{s}$ | $3.800\ \mathrm{mm}$ |
| $0.01\ \mathrm{s}$ | $3.980\ \mathrm{mm}$ |
| Exact integral | $4.000\ \mathrm{mm}$ |

Euler underestimates this example because velocity increases during each interval. The trapezoidal rule, using the mean of both endpoint values, gives the exact integral for a linear velocity function but not necessarily for a nonlinear one.


[See how the values 3, 3.8 and 3.98 are calculated.](#motion-values-derivation)

<a id="section-5"></a>

## 5. Try it

Run [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py). Explore the effect of decreasing $\Delta t$. Then explain why a full return journey can have zero displacement but positive traveled distance.

The examples are synthetic and do not control actual equipment.

<a id="section-6"></a>

## 6. Further details (optional)

### Units and what the coefficients mean

If time $t$ is measured in seconds, writing $x(t)=2t^2$ millimeters is shorthand: the coefficient has units $2\ \mathrm{mm/s^2}$. Then $v(t)=4t$ has units of $\mathrm{mm/s}$. Always check units before putting numerical values into a formula.

### Finite differences and numerical error

A finite difference is an estimate of a derivative over a nonzero step, not the exact instantaneous value. A smaller step reduces truncation error for smooth functions, but a very small step can increase floating-point cancellation or measurement noise. Euler integration uses the beginning-of-step value; for an increasing linear velocity it underestimates the integral.

### More than one dimension

For a position vector $\mathbf r(t)$, velocity is $\mathbf v(t)=d\mathbf r/dt$. Speed is its magnitude $\|\mathbf v\|$, and path length is $s=\int\|\mathbf v(t)\|dt$.


<a id="power-rule-derivation"></a>

### Why the derivative of $2t^2$ is $4t$



$$
x(t)=at^2,\qquad
\frac{dx}{dt}=\lim_{h\to0}\frac{a(t+h)^2-at^2}{h}
=\lim_{h\to0}a(2t+h)=2at.
$$

$$
 a=2\ \mathrm{mm/s^2},\qquad
 v(t)=2at=(4\ \mathrm{mm/s^2})t.
$$

<a id="motion-values-derivation"></a>

### Where the displacement table values come from

$$
a=2\ \mathrm{mm/s^2},\qquad v(t)=at,\qquad 0\le t\le2\ \mathrm{s}.
$$

$$
\Delta x=\int_{0}^{2\ \mathrm{s}}at\ \mathrm{d}t
=\left[\frac{at^2}{2}\right]_{0}^{2\ \mathrm{s}}
=4\ \mathrm{mm}.
$$



The symbol $\sum$ (capital Greek **sigma**, **summation**) means *add up the terms*. In $\sum_{n=0}^{N-1}(2nh)h$, the index $n$ takes the values $0; 1; \ldots; N-1$: there are $N$ contributions. Think of a Python `for` loop adding one contribution at a time. For example, $\sum_{n=1}^{3}n=1+2+3=6$. [← Symbols explained](../SYMBOLS.md#summation).

$$
h=\frac{dt}{1\ \mathrm{s}},\qquad N=\frac{2}{h}.
$$

$$
x_{\mathrm{Euler}}(2\ \mathrm{s})
=\left[\sum_{n=0}^{N-1}(2nh)h\right]\ \mathrm{mm}
=\left[h^2N(N-1)\right]\ \mathrm{mm}
=(4-2h)\ \mathrm{mm}.
$$

Here `h` is the numerical value of the step `dt` measured in seconds (for example, `dt = 0.5 s` means `h = 0.5`), and `N` is the number of steps. The result above is a **distance in millimetres**, not a dimensionless number.



For $dt=0.5$, $0.1$, and $0.01$ seconds, this gives $3$, $3.8$, and $3.98$ millimeters. The calculation assumes the dimensionless step count $N=(2\ \mathrm{s})/dt$ is an integer.
