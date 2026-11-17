# 0. Calculus foundations: practical derivatives, limits, and integrals

**Languages:** [en](00-calculus-foundations.md) · [fr](../../fr/notes/00-calculus-foundations.md) · [de](../../de/notes/00-calculus-foundations.md) · [it](../../it/notes/00-calculus-foundations.md) · [es](../../es/notes/00-calculus-foundations.md) · [pt](../../pt/notes/00-calculus-foundations.md) · [zh](../../zh/notes/00-calculus-foundations.md) · [ja](../../ja/notes/00-calculus-foundations.md) · [nb](../../nb/notes/00-calculus-foundations.md) · [ru](../../ru/notes/00-calculus-foundations.md) · [ko](../../ko/notes/00-calculus-foundations.md) · [fi](../../fi/notes/00-calculus-foundations.md) · [pl](../../pl/notes/00-calculus-foundations.md)

The **natural exponential** is $\exp(x)=\mathrm{e}^{x}$, where **Euler's number** is $\mathrm{e}\approx2.71828$. It describes continuous growth or decay; $\exp(0)=1$ and $\exp(-1)\approx0.3679$. The natural logarithm $\ln$ is its inverse: $\ln(\exp(x))=x$. See the [symbol guide](../SYMBOLS.md).

**Units used here (defined before the examples):** `s` — second; `mm` — millimetre = 0.001 m; `mm/s` — millimetre / second — linear speed; `mm/s²` — millimetre / second² — acceleration; `kg·m²` — kilogram · metre² — moment of inertia; `rad/s` — radian / second — angular speed; `rad/s²` — radian / second² — angular acceleration; `N·m` — newton · metre — torque; `W` — watt; `rpm` — revolution per minute; `N/m` — newton / metre — stiffness; `mm³/s` — millimetre³ / second — volumetric flow; `%` — percent (one part in a hundred); `m` — metre; `kg` — kilogram; `N` — newton; `J` — joule; `rad` — radian. [Full unit reference](../UNITS.md).

[README](../README.md) · [Integral table](../INTEGRAL_TABLE.md) · [Trigonometry table](../TRIGONOMETRY.md) · [Motion](01-motion-calculus.md) · [Dynamics](02-first-order-dynamics.md) · [Symbols](../SYMBOLS.md)

> **Educational approximation:** Verify models and units independently; never connect demo code to real equipment.

A derivative tells us how fast a quantity changes **now**; a second derivative tells us how its change rate changes. An integral accumulates small changes. A limit defines an instantaneous rate. A logarithm often lets us solve an exponential response for elapsed time.

The same tools appear in a machine axis, servo drive, robot joint, spring, and sensor. Start with an engineering question, identify the changing quantity and units, then choose a rule.

## Contents

- [1. From a measured change to a mathematical model](#section-1)
- [2. Limits and first derivatives](#section-2)
- [3. First and second derivatives: an axis in motion](#section-3)
- [4. Chain rule: rotating energy](#section-4)
- [5. Exponential functions and logarithms: settling time](#section-5)
- [6. Integrals: displacement and mechanical work](#section-6)
- [7. Further example: expanding sphere](#section-7)
- [8. Units, checks, and next steps](#section-8)

<a id="section-1"></a>
## 1. From a measured change to a mathematical model

| Physical question | Mathematical tool |
| --- | --- |
| How fast does the axis move **now**? | First derivative $dx/dt$ |
| How fast does speed change? | Second derivative $d^2x/dt^2$ |
| When will a response reach 90 %? | Logarithm $\ln$ |
| How far did it move in 2 s? | Definite integral $\int v\ \mathrm{d}t$ |
| What is the work of a variable force? | Integral $\int F\ \mathrm{d}x$ |

<a id="section-2"></a>
## 2. Limits and first derivatives

A finite difference between two measurements is an **average rate** over an interval. A derivative is the limit of that rate when the interval shrinks toward zero.

$$
v(t)=\frac{dx}{dt}=\lim_{h\to0}\frac{x(t+h)-x(t)}{h}.
$$

For a position $x(t)=a t^2$ with $a=2\ \mathrm{mm/s^2}$, expand the numerator before taking the limit:

$$
\frac{x(t+h)-x(t)}h=\frac{a[(t+h)^2-t^2]}h=a(2t+h)\longrightarrow 2at.
$$

The $h$ cancels **before** setting $h$ to zero. At $t=1\ \mathrm{s}$ the instantaneous velocity is $4\ \mathrm{mm/s}$. The limit does not mean evaluating an undefined $0/0$.

**Frequently used differentiation rules** (coefficients $c$ and $n$ are constant; trigonometric arguments in radians):

| Rule | Formula |
| --- | --- |
| Constant | $\frac{d}{dt}c=0$ |
| Power | $\frac{d}{dt}t^n=n t^{n-1}$ |
| Coefficient and sum | $(cf+g)'=cf'+g'$ |
| Product | $(fg)'=f' g+fg'$ |
| Quotient, $g\ne0$ | $\left(\frac{f}{g}\right)'=\frac{f' g-fg'}{g^2}$ |
| Chain | $\frac{d}{dt}f(g(t))=f'(g(t))g'(t)$ |
| Exponential | $\frac{d}{dt}\exp(t)=\exp(t)$ |
| Natural logarithm, $t>0$ | $\frac{d}{dt}\ln t=\frac1t$ |
| Sine / cosine | $\frac{d}{dt}\sin t=\cos t$, $\frac{d}{dt}\cos t=-\sin t$ |

![Slope of position and area under velocity](../../../assets/figures/calculus_slope_area.svg)

<a id="section-3"></a>
## 3. First and second derivatives: an axis in motion

A carriage starts at position 2 mm, has initial velocity 3 mm/s, and experiences constant acceleration 4 mm/s². Its position is:

$$
x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2.
$$

First derivative (velocity): differentiate each term. The constant 2 mm disappears, the $t$ term becomes 3 mm/s, and the $t^2$ term becomes linear in $t$.

$$
v(t)=\frac{dx}{dt}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t.
$$

Second derivative (acceleration): differentiate the velocity once more. At 2 s the position is 16 mm, velocity is 11 mm/s, and acceleration remains 4 mm/s².

$$
a(t)=\frac{d^2x}{dt^2}=\frac{dv}{dt}=4\ \mathrm{mm/s^2}.
$$

A second derivative has physical units of distance divided by time squared. It is **not** the square of the first derivative.

<a id="section-4"></a>
## 4. Chain rule: rotating energy

A rotating flywheel stores kinetic energy. If angular speed $\omega$ depends on time, the energy $E$ changes through that speed: this is the **chain rule**.

$$
E(\omega)=\frac12J\omega^2,\quad \omega=\omega(t),
$$
$$
\frac{dE}{dt}=\frac{dE}{d\omega}\frac{d\omega}{dt}=J\omega\alpha=M\omega=P.
$$

For $J=0.01\ \mathrm{kg\cdot m^2}$, $\omega=10\ \mathrm{rad/s}$, and $\alpha=2\ \mathrm{rad/s^2}$, the motor torque is $J\alpha=0.02\ \mathrm{N\cdot m}$ and instantaneous mechanical power is $0.2\ \mathrm{W}$. This is a practical use of the chain rule: $P=M\omega$.

<a id="section-5"></a>
## 5. Exponential functions and logarithms: settling time

For a simple first-order drive model, the speed can approach its final value exponentially. The parameter $\tau$ (time constant) is measured in seconds.

$$
\omega(t)=\omega_\infty\bigl(1-\exp(-t/\tau)\bigr),\quad t\ge0,\ \tau>0.
$$

This expression assumes **zero initial angular speed**, $\omega(0)=0$, and a constant target $\omega_\infty$. For a nonzero initial speed $\omega_0$, the general first-order response is

$$
\omega(t)=\omega_\infty+(\omega_0-\omega_\infty)\exp(-t/\tau).
$$

**Nonzero initial speed, worked out:** Let $\omega_0=200\ \mathrm{rpm}$, $\omega_\infty=1000\ \mathrm{rpm}$, and $\tau=0.5\ \mathrm{s}$. After one time constant ($t=0.5\ \mathrm{s}$):

$$
\omega(\tau)=1000+(200-1000)\exp(-1)\approx705.7\ \mathrm{rpm}.
$$

The response has completed **63.2 % of the 800 rpm change**, not 63.2 % of the final 1000 rpm. Substituting $t=0$ returns 200 rpm; as time grows, the result approaches 1000 rpm. The example is a mathematical response, not a motor command.

The exponential describes the remaining fraction of an initial error. To find **when** a specified fraction remains, use the natural logarithm $\ln$, the inverse of $\exp$. Here the logarithm argument $0.1$ is dimensionless.

$$
\exp(-t/\tau)=0.1
\quad\Longrightarrow\quad
-\frac{t}{\tau}=\ln(0.1)
\quad\Longrightarrow\quad
t=-\tau\ln(0.1)=\tau\ln(10)\approx2.303\tau.
$$

To reach 90 % of the final change, only 10 % of the initial error remains. With $\tau=0.5\ \mathrm{s}$, the ideal model gives about 1.151 s. Real drives may have additional limits and delays.

The derivative of $\ln z$ is $1/z$ for $z>0$; for $z=z(t)$, multiply by $dz/dt$ using the chain rule. Never take a logarithm of a dimensional quantity without forming a dimensionless ratio.

$$
\ln(1)=0,\quad \ln(\mathrm{e})=1,\quad \ln(\mathrm{e}^{z})=z,\quad \frac{d}{dz}\ln z=\frac1z\ (z>0).
$$

<a id="section-6"></a>
## 6. Integrals: displacement and mechanical work

An **indefinite integral** finds all antiderivatives and includes an unknown constant $C$. A **definite integral** finds the net accumulated change on a specified interval.

$$
\int 4t\ \mathrm{d}t=2t^2+C,\qquad \int t^n\ \mathrm{d}t=\frac{t^{n+1}}{n+1}+C\ (n\ne-1).
$$

**Motion example.** A carriage begins at $x_0=2\ \mathrm{mm}$ and its velocity increases linearly as $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$. Find the displacement over 0–2 s:

$$
\Delta x=\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
$$
$$
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}=6\ \mathrm{mm}+8\ \mathrm{mm}=14\ \mathrm{mm}.
$$

The displacement is 14 mm; add the initial position to obtain $x(2)=16\ \mathrm{mm}$. A negative velocity would contribute negative signed displacement, not negative distance traveled.

**Spring work example.** Stretch an ideal linear spring from $x=0$ to $x=0.01\ \mathrm{m}$, with stiffness $k=200\ \mathrm{N/m}$. Force increases with extension, so multiply each tiny movement by its own force and integrate:

$$
F(x)=kx,\qquad W=\int_0^{0.01\ \mathrm{m}}kx\ \mathrm{d}x
=\left[\frac{kx^2}{2}\right]_0^{0.01\ \mathrm{m}}
=\frac{200\ \mathrm{N/m}}2(0.01\ \mathrm{m})^2=0.01\ \mathrm{J}.
$$

The work is 0.01 J. Using only the final force $F=2\ \mathrm{N}$ over the entire movement would give the incorrect value 0.02 J; force was not constant.

<a id="section-7"></a>
## 7. Further example: expanding sphere

**Optional chain-rule example.** The volume of a sphere depends on its radius, and the radius may depend on time. This is mathematically the same dependency pattern as flywheel energy depending on angular speed.

$$
V(r)=\frac43\pi r^3,\qquad \frac{dV}{dt}=\frac{dV}{dr}\frac{dr}{dt}=4\pi r^2\frac{dr}{dt}.
$$

At $r=10\ \mathrm{mm}$ and $dr/dt=1\ \mathrm{mm/s}$, the instantaneous volume growth is $400\pi\approx1256.64\ \mathrm{mm^3/s}$. For $r(t)=10\ \mathrm{mm}+(1\ \mathrm{mm/s^2})t^2$, at 2 s we get $r=14\ \mathrm{mm}$, $dr/dt=4\ \mathrm{mm/s}$, and $3136\pi\approx9852.03\ \mathrm{mm^3/s}$.

<a id="section-8"></a>
## 8. Units, checks, and next steps

**Checks:** a position derivative has units m/s and a second derivative m/s²; an integral of N over m gives N·m = J; $C$ is necessary for indefinite integrals; a derivative is local, whereas an integral over an interval is accumulated; $dt$ is a calculus differential, but `dt` in Euler code is a finite sample period.

**Try independently:** (1) For $x(t)=5\ \mathrm{mm}+(2\ \mathrm{mm/s})t+(1\ \mathrm{mm/s^2})t^2$, calculate velocity and acceleration at 3 s. (2) With $\tau=1\ \mathrm{s}$, how long for an ideal first-order response to complete 90 % of its change? (3) Integrate constant $v=4\ \mathrm{mm/s}$ over 2 s. **Answers:** 8 mm/s and 2 mm/s²; approximately 2.303 s; 8 mm.

**Worked solutions:**

1. $v(t)=\frac{dx}{dt}=2\ \mathrm{mm/s}+2(1\ \mathrm{mm/s^2})t$; $v(3\ \mathrm{s})=2+2\cdot3=8\ \mathrm{mm/s}$. $a(t)=\frac{dv}{dt}=2\ \mathrm{mm/s^2}$.
2. $f(t)=1-\exp(-t/\tau)=0.9$; $\exp(-t/\tau)=0.1$; $t=-\tau\ln(0.1)=\tau\ln(10)$. $\tau=1\ \mathrm{s}$; $t\approx2.303\ \mathrm{s}$.
3. $\Delta x=\int_0^{2\ \mathrm{s}}(4\ \mathrm{mm/s})\ \mathrm{d}t=(4\ \mathrm{mm/s})(2\ \mathrm{s})=8\ \mathrm{mm}$.


[Integral reference](../INTEGRAL_TABLE.md) · [Trigonometry](../TRIGONOMETRY.md) · [Next: motion](01-motion-calculus.md) · [Python exercises](../exercises/README.md)
