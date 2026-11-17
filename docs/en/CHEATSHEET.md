# Cheat sheet — motion and first-order systems

**Read this page in:** [en](CHEATSHEET.md) · [fr](../fr/CHEATSHEET.md) · [de](../de/CHEATSHEET.md) · [it](../it/CHEATSHEET.md) · [es](../es/CHEATSHEET.md) · [pt](../pt/CHEATSHEET.md) · [zh](../zh/CHEATSHEET.md) · [ja](../ja/CHEATSHEET.md) · [nb](../nb/CHEATSHEET.md) · [ru](../ru/CHEATSHEET.md) · [ko](../ko/CHEATSHEET.md) · [fi](../fi/CHEATSHEET.md) · [pl](../pl/CHEATSHEET.md)

**Units used here (defined before the examples):** `s` — second; `m` — metre; `m/s` — metre / second — linear speed; `rad/s` — radian / second — angular speed; `kg·m²` — kilogram · metre² — moment of inertia; `N·m` — newton · metre — torque; `N·m·s/rad` — newton · metre · second / radian — gain per unit speed; `J` — joule; `mm` — millimetre = 0.001 m; `mm/s` — millimetre / second — linear speed; `%` — percent (one part in a hundred). [Full unit reference](UNITS.md).

[Contents](README.md) · [Motion](notes/01-motion-calculus.md) · [Dynamics](notes/02-first-order-dynamics.md) · [Exercises](exercises/README.md)

> **Not an engineering specification.** Verify units and idealizing assumptions before use.

| Concept | Definition or equation |
| --- | --- |
| Displacement | $\Delta x=x_2-x_1$ (signed) |
| Distance traveled | $s=\int_{t_1}^{t_2}\lvert v(t)\rvert\ \mathrm{d}t\ge 0$ |
| Average velocity | $\bar v=\frac{\Delta x}{\Delta t}$ (signed, 1D) |
| Average speed | $\frac{s}{\Delta t}$ (nonnegative) |
| Instantaneous velocity | $v(t)=\frac{dx}{dt}$ |
| Displacement from velocity | $\Delta x=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t$ |
| Explicit Euler integration | $x_{n+1}=x_n+v_n\ dt$ |
| First-order dynamics | $\frac{dv}{dt}=\frac{u-v}{\tau}$ |
| Speed error | $\varepsilon(t)=u-v(t)$ |
| Exact step response | $v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right)$, for constant $u$ |
| Time constant | At $t=\tau$, $63.2\ \%$ of the change is complete |
| Simplified torque model | $M=K(u-\omega)$ |
| Rotational acceleration | $M=J\alpha$, $\alpha=\frac{d\omega}{dt}$ |
| Model time constant | $\tau=\frac{J}{K}$, **only** under stated torque-model assumptions |
| Rotational kinetic energy | $E=\frac{1}{2}J\omega^2$ |

**Notation:** $\varepsilon$ is a speed error; $\mathrm{e}\approx2.71828$ is Euler’s number; $\exp(z)=\mathrm{e}^{z}$ is the natural exponential. The two symbols are unrelated.

**Units (SI):**

| Quantity | Name | Unit |
| --- | --- | --- |
| `t, dt, τ` | Time | s (second) |
| `x` | Position | m (meter) |
| `v` | Speed | m/s (meter per second) |
| `ω` | Angular velocity | rad/s (radian per second) |
| `J` | Moment of inertia | kg·m² (kilogram square meter) |
| `M` | Torque | N·m (newton meter) |
| `K` | Torque gain | N·m·s/rad |
| `E` | Energy | J (joule) |

A centered dot `·` means multiplication, not a list separator. $u$ is linear velocity in the linear model, or angular velocity in the rotational model.

**Most common traps:** speed is not signed velocity; distance is not displacement; $dt$ is not $\tau$; reaching one $\tau$ does not mean reaching the target; $\frac{J}{K}$ is not a general identity for all motors; mechanical energy is not electrical input consumption.

For more context, see the [optional details on derivatives and integration](notes/01-motion-calculus.md#section-6) and [optional details on model assumptions and Euler stability](notes/02-first-order-dynamics.md#section-7).


[Why exactly these percentages? See the calculation.](notes/02-first-order-dynamics.md#time-constant-derivation)

[See how the values 3, 3.8 and 3.98 are calculated.](notes/01-motion-calculus.md#motion-values-derivation)


## Symbols and notation

**Σ / ∑ (summation)** means add the terms. Example: $\sum_{n=1}^{3} n=1+2+3=6$. Upper and lower limits tell you which terms to include. [More symbols and notation](SYMBOLS.md).


## Integral reference table

[0. Calculus foundations: derivatives, differentials, and integrals](notes/00-calculus-foundations.md) · [Integral reference table](INTEGRAL_TABLE.md)

## Feedback control: PID and holding torque

| $\varepsilon=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}}$ | $u_P=K_p\varepsilon$, $u_I=K_i\int\varepsilon\ \mathrm{d}t$ |
| --- | --- |
| $M_{\mathrm{motor}}=K_t I$ | $\lvert M_g\rvert=mgL\lvert\cos\theta\rvert$ |

[Feedback control: PID and holding torque](notes/03-feedback-control.md) · [Trigonometry table with mechanical examples](TRIGONOMETRY.md)

<a id="joint-velocity"></a>
## Rotation, velocity and Jacobian

Joint angular speeds use rad/s. Linear speed is mm/s for lengths in mm.

$$
v_x=-L\sin Q\cdot\dot Q,\qquad v_y=L\cos Q\cdot\dot Q
$$

$$
\det J=L_1L_2\sin Q_2
$$

[Rotation, velocity and Jacobian](notes/05-velocity-jacobian.md)
