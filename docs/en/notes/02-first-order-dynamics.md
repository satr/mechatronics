# 2. First-order dynamics, torque, and rotational energy

**Read this page in:** [en](02-first-order-dynamics.md) · [fr](../../fr/notes/02-first-order-dynamics.md) · [de](../../de/notes/02-first-order-dynamics.md) · [it](../../it/notes/02-first-order-dynamics.md) · [es](../../es/notes/02-first-order-dynamics.md) · [pt](../../pt/notes/02-first-order-dynamics.md) · [zh](../../zh/notes/02-first-order-dynamics.md) · [ja](../../ja/notes/02-first-order-dynamics.md) · [nb](../../nb/notes/02-first-order-dynamics.md) · [ru](../../ru/notes/02-first-order-dynamics.md) · [ko](../../ko/notes/02-first-order-dynamics.md) · [fi](../../fi/notes/02-first-order-dynamics.md) · [pl](../../pl/notes/02-first-order-dynamics.md)

**Units used here (defined before the examples):** `s` — second; `mm/s` — millimetre / second — linear speed; `kg` — kilogram; `m` — metre; `rad/s` — radian / second — angular speed; `N` — newton; `N·m` — newton · metre — torque; `J` — joule; `rpm` — revolution per minute; `kg·m²` — kilogram · metre² — moment of inertia; `N·m·s/rad` — newton · metre · second / radian — gain per unit speed; `%` — percent (one part in a hundred); `rad` — radian. [Full unit reference](../UNITS.md).

**Calculus refresher:** [0. Calculus foundations: derivatives, differentials, and integrals](00-calculus-foundations.md) · [Integral reference table](../INTEGRAL_TABLE.md)


[Contents](../README.md) · [Cheat sheet](../CHEATSHEET.md) · [Exercises](../exercises/README.md) · [Previous chapter](01-motion-calculus.md)

> **Accuracy notice:** The motor model below assumes ideal proportional torque control with no load, friction, delays, voltage limits, saturation, or higher-order dynamics. It is not a universal description of motors.

## Quick review

- A **time constant** $\tau$ characterizes how quickly a first-order system approaches its new equilibrium.
- The simulation time step $dt$ changes the numerical approximation; it does **not** change the physical model's $\tau$.
- In one idealized rotating system, $\tau=\frac{J}{K}$, with rotor moment of inertia $J$ and a proportional torque coefficient $K$.
- Equal $J/K$ can produce the same speed response, while requiring different torques and mechanical energies.

## On this page

- [1. First-order speed response](#section-1)
- [2. What determines the time constant?](#section-2)
- [3. Numerical time step versus time constant](#section-3)
- [4. Estimating a time constant from data](#section-4)
- [5. Torque and rotational energy](#section-5)
- [6. Try it](#section-6)
- [7. Further details (optional)](#section-7)
  - [Where 63.2 %, 86.5 %, and 95.0 % come from](#time-constant-derivation)
  - [Where the Euler values come from](#euler-values-derivation)

[SI notation and decimal points](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. First-order speed response

For derivations, units, and numerical limitations, see [Further details](#section-7).

Let $u$ be a constant target velocity, $v$ the actual velocity, and $\tau>0$ the time constant. Consider:

**Notation:** $\varepsilon(t)=u-v(t)$ is the speed error (the Greek letter epsilon). The natural exponential function is $\exp(z)=\mathrm{e}^{z}$, where $\mathrm{e}\approx2.71828$ is **Euler’s number**, not the error. We deliberately use different symbols to avoid confusion. [See the derivation and the 63.2 % calculation](#time-constant-derivation).

$$
\frac{dv}{dt}=\frac{u-v}{\tau}.
$$

With constant $u$ and initial velocity $v_0$, the exact solution is

$$
v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right).
$$

After one time constant, the system has completed $1-\exp(-1)\approx63.2\ \%$ of the initial-to-final change; after two, $86.5\ \%$; after three, $95.0\ \%$. Thus $\tau=2\ \mathrm{s}$ means approximately 63.2 % of the *change* occurs in two seconds. It does **not** mean the target is reached exactly at two seconds.

[Why exactly these percentages? See the calculation.](#time-constant-derivation)

![A normalized first-order step response: each time constant removes approximately 63.2 % of the *remaining* error.](../../../assets/figures/first_order_response.svg)

<a id="section-2"></a>

## 2. What determines the time constant?

For a highly simplified rotating system, Newton's second law for rotation is

$$
J\frac{d\omega}{dt}=M,
$$

where $J$ is moment of inertia ($\mathrm{kg}\cdot\mathrm{m}^2$), $\omega$ is angular velocity ($\mathrm{rad/s}$), and $M$ is **net physical torque** ($\mathrm{N}\cdot\mathrm{m}$). A controller computes an electrical drive command; the motor physically produces torque. It is imprecise to say the controller itself creates torque.

Assume the motor and drive can provide torque proportional to speed error:

$$
M=K(u-\omega).
$$

In this rotational example, $u$ denotes a **target angular velocity** in rad/s, not the linear target velocity in mm/s used in Section 1. Both $u$ and $\omega$ must use the same angular-velocity units; otherwise $u-\omega$ and the torque law are dimensionally invalid.

Here $K$ is a torque-versus-speed-error coefficient, with units $\mathrm{N}\cdot\mathrm{m}\cdot\mathrm{s}/\mathrm{rad}$. Under these assumptions:

$$
\frac{d\omega}{dt}=\frac{K}{J}(u-\omega),\qquad
\tau=\frac{J}{K}.
$$

Doubling $J$ with fixed $K$ doubles $\tau$ and reduces acceleration at the same speed error. Doubling both $J$ and $K$ preserves $\tau$, but the required torque at the same error doubles. $J$ is **not** a friction force; it is a measure of resistance to changes in angular velocity. A real model may require load torque, friction, electrical dynamics, nonlinear current limits, and more state variables.

Symbolic feedback loop for the idealized model. The controller commands the drive; the motor, not the software, supplies physical torque.

![Symbolic feedback loop for the idealized model. The controller commands the drive; the motor, not the software, supplies physical torque](../../../assets/figures/control_loop.svg)

<a id="section-3"></a>

## 3. Numerical time step versus time constant

Explicit Euler applied to the first-order equation gives

$$
v_{n+1}=v_n+\frac{u-v_n}{\tau}\ dt.
$$

If $u=10\ \mathrm{mm/s}$, $v_0=0$, $\tau=1\ \mathrm{s}$, evaluate after one second:

| Method | $v(1\ \mathrm{s})$ |
| --- | ---: |
| Euler, $dt=0.1\ \mathrm{s}$ | $6.513\ \mathrm{mm/s}$ |
| Euler, $dt=0.01\ \mathrm{s}$ | $6.340\ \mathrm{mm/s}$ |
| Exact | $6.321\ \mathrm{mm/s}$ |

Changing $dt$ changes how often the calculation updates. It does not make the model's motor speed up. Stability and error also depend on the relationship between $dt$, $\tau$, and the chosen numerical method.

[See how these numerical values are calculated.](#euler-values-derivation)

<a id="section-4"></a>

## 4. Estimating a time constant from data

In a clean first-order step response from $0$ to $1000\ \mathrm{rpm}$, reaching about $632\ \mathrm{rpm}$ at $t=2\ \mathrm{s}$ suggests $\tau\approx2\ \mathrm{s}$. Use 63.2 % of the **change from initial value to final steady-state value**, not necessarily 63.2 % of the command's absolute value. Real measurements may have noise, sampling error, delay, and overshoot.

**What the example code actually returns:** [`estimate_tau`](../../../exercises/02_first_order_response.py) takes samples ordered by their timestamps (strictly increasing, starting from the step's time origin). It returns the timestamp of the **first observed sample** at or beyond the 63.2 % change threshold, allowing half the known measurement resolution for rounding. If readings are taken at 1 s and 2 s and the threshold is first detected at 2 s, the actual crossing could have occurred **between samples**, so 2 s is a sampling-limited estimate, not an exact fit. Out-of-order, repeated-time or invalid samples are rejected, including those after the crossing; no crossing returns `None`.

**Sensor resolution matters:** The `resolution` passed to `estimate_tau` must be **smaller than the magnitude of the total speed change**. If a step is from 0 to 10 rpm but the display changes only in 10 rpm increments, the 63.2 % crossing cannot be estimated reliably from that display; the function rejects the input instead of reporting an artificial crossing at the first sample. A sufficiently fine resolution still yields only a sampling-limited estimate.

<a id="section-5"></a>

## 5. Torque and rotational energy

Angular acceleration $\alpha=\frac{d\omega}{dt}$ satisfies

$$
M=J\alpha.
$$

Rotational kinetic energy is

$$
E=\frac{1}{2}J\omega^2.
$$

At $\omega=10\ \mathrm{rad/s}$, $J=2\ \mathrm{kg}\cdot\mathrm{m}^2$ gives $100\ \mathrm{J}$; doubling $J$ gives $200\ \mathrm{J}$. At fixed $J$, doubling $\omega$ quadruples $E$. This is **mechanical kinetic energy**, not electrical energy drawn from a power supply: losses and efficiency matter.

<a id="section-6"></a>

## 6. Try it

Run [`02_first_order_response.py`](../../../exercises/02_first_order_response.py) and [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py). Optional plots are generated by [`plot_models.py`](../../../exercises/plot_models.py). These programs use synthetic numbers and no hardware interfaces.


<a id="section-7"></a>

## 7. Further details (optional)


### When the Euler calculation becomes unstable

For the simple first-order equation, each Euler step multiplies the **remaining speed error** by $1-\frac{dt}{\tau}$. Convergence requires $0<dt<2\tau$. When $dt$ is between $\tau$ and $2\tau$, the estimate oscillates around the target. This is a property of the **numerical method**, not the physical motor. Use a smaller step to improve accuracy.

### Limits of the torque model

More generally, $J\ \frac{d\omega}{dt}=M_{\text{motor}}-M_{\text{load}}-M_{\text{friction}}$. The formula $\tau=\frac{J}{K}$ requires the special idealization $M_{\text{net}}=K(u-\omega)$. Real drive saturation, sensor delays, friction, and additional electrical states can change the response.

### Energy and power

For constant $J$, the change in rotational kinetic energy is $\Delta E=\frac{1}{2} J(\omega_2^2-\omega_1^2)$, and instantaneous **mechanical** power is $P=M\omega$. Neither alone determines actual electrical input energy; losses and efficiencies matter.


<a id="time-constant-derivation"></a>

### Where 63.2 %, 86.5 %, and 95.0 % come from

The percentages and the exponential come from the **same equation**. Define the speed error as $\varepsilon(t)=u-v(t)$ (not Euler’s number). When $u$ is constant, $\frac{d\varepsilon}{dt}=-\frac{dv}{dt}$, so the original first-order equation becomes:

$$
\varepsilon(t)=u-v(t),\qquad \frac{d\varepsilon}{dt}=-\frac{\varepsilon}{\tau}.
$$

$$
\frac{d\varepsilon}{\varepsilon}=-\frac{dt}{\tau}
\quad\Longrightarrow\quad
\ln\left\lvert\frac{\varepsilon(t)}{\varepsilon(0)}\right\rvert=-\frac{t}{\tau}
\quad\Longrightarrow\quad
\varepsilon(t)=\varepsilon(0)\exp\!\left(-\frac{t}{\tau}\right).
$$

The separation step divides by $\varepsilon$, so it assumes a nonzero initial error. If $u=v_0$, the error is zero for all time and the constant solution $v(t)=u$ follows directly from the original differential equation.

$$
f(t)=\frac{v(t)-v_0}{u-v_0}=1-\exp\!\left(-\frac{t}{\tau}\right),\qquad (u\ne v_0).
$$

| $t$ | $f(t)$ |
| ---: | ---: |
| $\tau$ | $1-\exp(-1)=0.63212056\ldots\approx63.2\ \%$ |
| $2\tau$ | $1-\exp(-2)=0.86466472\ldots\approx86.5\ \%$ |
| $3\tau$ | $1-\exp(-3)=0.95021293\ldots\approx95.0\ \%$ |

For a step from 0 to 1000 rpm, these fractions give approximately 632, 865, and 950 rpm after one, two, and three time constants. This ideal model approaches the target asymptotically.

<a id="euler-values-derivation"></a>

### Where the Euler values come from

$$
v_N=u+(v_0-u)\left(1-\frac{dt}{\tau}\right)^N,\qquad N=\frac{t}{dt}.
$$

$$
\begin{aligned}
u&=10,\quad v_0=0,\quad t=\tau=1;\\
v_{dt=0.1}&=10(1-0.9^{10})\approx6.5132;\\
v_{dt=0.01}&=10(1-0.99^{100})\approx6.3397;\\
v_{\mathrm{exact}}&=10(1-\exp(-1))\approx6.3212.
\end{aligned}
$$
