# 3. Feedback control: PID, sampling, saturation, and holding torque

**Languages:** [en](03-feedback-control.md) · [fr](../../fr/notes/03-feedback-control.md) · [de](../../de/notes/03-feedback-control.md) · [it](../../it/notes/03-feedback-control.md) · [es](../../es/notes/03-feedback-control.md) · [pt](../../pt/notes/03-feedback-control.md) · [zh](../../zh/notes/03-feedback-control.md) · [ja](../../ja/notes/03-feedback-control.md) · [nb](../../nb/notes/03-feedback-control.md) · [ru](../../ru/notes/03-feedback-control.md) · [ko](../../ko/notes/03-feedback-control.md) · [fi](../../fi/notes/03-feedback-control.md) · [pl](../../pl/notes/03-feedback-control.md)

**Units used here (defined before the examples):** `rpm` — revolution per minute; `A` — ampere; `s` — second; `rpm/s` — revolution per minute / second — angular acceleration; `A/rpm` — ampere / (revolution per minute) — gain per unit speed; `A/(rpm·s)` — ampere / (revolution per minute · second) — time-integral gain; `A·s/rpm` — ampere · second / (revolution per minute) — time-derivative gain; `N·m` — newton · metre — torque; `kg` — kilogram; `m` — metre; `N` — newton. [Full unit reference](../UNITS.md).

[README](../README.md) · [Math foundations](00-calculus-foundations.md) · [First-order dynamics](02-first-order-dynamics.md) · [Trigonometry](../TRIGONOMETRY.md)

> **Educational model:** Do not connect these simplified algorithms to real motors or machinery.

## Contents

- [1. Closed-loop speed control](#section-1)
- [2. P: proportional response](#section-2)
- [3. I: accumulated error and current setpoint](#section-3)
- [4. D: changing error and sensor noise](#section-4)
- [5. Sample periods, saturation, and anti-windup](#section-5)
- [6. Holding a robot joint against gravity](#section-6)
- [7. Checks and limitations](#section-7)

<a id="section-1"></a>
## 1. Closed-loop speed control

A closed-loop controller (feedback controller) compares a desired setpoint with a sensor measurement. For a motor speed setpoint of 1000 rpm and measured speed of 950 rpm, the speed error is +50 rpm. A PI/PID controller converts that error into a command. In our example, the command is a **target torque-producing current** in amperes, not an instruction to add that many amperes to the previous measured current.

$$
\varepsilon(t)=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}},
\qquad I_{\mathrm{set}}=u_P+u_I+u_D.
$$

The drive may contain a separate current-control loop, which varies voltage or PWM to track the current setpoint. Other architectures can output voltage, torque, PWM, etc. Do not assume all real drives expose a current setpoint.

<a id="section-2"></a>
## 2. P: proportional response

The P term reacts to error **now**. In the simple model with no feedforward or command offset, a constant load requires nonzero motor torque and hence nonzero current. If the speed error were exactly zero, the P term would also be zero. Thus P-only control can settle with a steady-state speed error.

$$
u_P=K_p\varepsilon,\quad [K_p]=\mathrm{A/rpm}.
$$

<a id="section-3"></a>
## 3. I: accumulated error and current setpoint

The I term integrates the error over time. It keeps a single accumulated state, not a list of all old errors. While positive error persists, the integral grows; when error is zero, it holds the previous value; when error becomes negative, it decreases. Thus it can keep a nonzero torque command even after the speed reaches the setpoint.

$$
z(t)=\int_0^t\varepsilon(s)\ \mathrm{d}s,\quad u_I=K_i z(t),\quad [K_i]=\mathrm{A/(rpm\cdot s)}.
$$

```python
integral = 0.0  # saved between controller iterations
for speed in [950, 950, 950, 1000, 1020, 1020]:
    error = 1000 - speed       # rpm
    integral += error * 1.0   # rpm*s; dt = 1 s
    p_command = 0.02 * error # amperes
    i_command = 0.002 * integral # amperes
    current_setpoint = p_command + i_command
    print(round(integral), round(i_command, 2), round(current_setpoint, 2))
```

For an illustrative controller with dt = 1 s, Kp = 0.02 A/rpm and Ki = 0.002 A/(rpm·s), a constant error +50 rpm for three samples gives integrals 50, 100, 150 rpm·s and I terms 0.10, 0.20, 0.30 A. With zero error the I term remains 0.30 A; one second at −20 rpm changes it to 0.26 A, then 0.22 A. The −0.04 A is the **change per step**, not the absolute new current setpoint.

The program prints only the accumulated integral, the I term and the total current setpoint. This table also shows the P term, so the calculation can be checked step by step. Each sample is 1 s after the preceding sample; the accumulator begins at zero.

| k | Measured speed (rpm) | ε (rpm) | z (rpm·s) | u_P (A) | u_I (A) | I_set (A) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 950 | +50 | 50 | +1.00 | +0.10 | +1.10 |
| 2 | 950 | +50 | 100 | +1.00 | +0.20 | +1.20 |
| 3 | 950 | +50 | 150 | +1.00 | +0.30 | +1.30 |
| 4 | 1000 | 0 | 150 | 0.00 | +0.30 | +0.30 |
| 5 | 1020 | −20 | 130 | −0.40 | +0.26 | −0.14 |
| 6 | 1020 | −20 | 110 | −0.40 | +0.22 | −0.18 |

At 1020 rpm the error is −20 rpm: the P term is −0.40 A, but the I term is still +0.26 A, giving a **signed total setpoint of −0.14 A**. At the next sample the total is −0.18 A. The change of the I term (−0.04 A per sample) is not the total command. These values describe an idealized calculation, not settings for a real drive.

<a id="section-4"></a>
## 4. D: changing error and sensor noise

The D term reacts to the **rate of change of error**. With a constant speed setpoint, acceleration of the measured speed makes error shrink, giving a negative derivative contribution that can reduce overshoot. D is not the motor speed itself. A sensor jump of 8 rpm in 0.01 s creates an apparent change rate of 800 rpm/s even if true speed is nearly constant.

$$
u_D=K_d\frac{\mathrm{d}\varepsilon}{\mathrm{d}t},\quad [K_d]=\mathrm{A\cdot s/rpm},\qquad
\frac{\Delta\omega}{\Delta t}=\frac{8\ \mathrm{rpm}}{0.01\ \mathrm{s}}=800\ \mathrm{rpm/s}.
$$

The error derivative has units rpm/s. Because the D contribution is a current command in A, the gain must cancel rpm/s: the units of `K_d` are A·s/rpm, so their product is A.

Derivative filtering can suppress high-frequency noise, but filtering too strongly delays the useful response. A common implementation differentiates the measurement rather than the setpoint to avoid a derivative kick on setpoint changes; gains and sign conventions must match the architecture.

<a id="section-5"></a>
## 5. Sample periods, saturation, and anti-windup

A digital controller updates at finite intervals. With error 20 rpm constant for one second, 100 samples at dt = 0.01 s and 10 samples at dt = 0.1 s both integrate to 20 rpm·s. Forgetting multiplication by dt makes the faster controller accumulate ten times as much. Practical tuning still depends on sampling, delay, noise, and drive dynamics.

$$
z_{k+1}=z_k+\varepsilon_k\ \Delta t.
$$

When an actuator is limited, the requested current may exceed the allowed current. If the integral continues increasing during this saturation (integral windup), the system can overshoot badly when the load reduces. Anti-windup may stop integration when the saturated command would be pushed further outward, or correct the internal state using the difference between requested and applied commands. Limit the **total** request and treat the P contribution correctly.

<a id="section-6"></a>
## 6. Holding a robot joint against gravity

The motor torque constant Kt is the torque produced per unit of **torque-producing current**: Kt in N·m/A, current in A, torque in N·m. For example, Kt = 0.1 N·m/A and current = 2 A give 0.2 N·m, with the manufacturer’s current convention respected.

$$
M_{\mathrm{motor}}=K_t I,\qquad [K_t]=\mathrm{N\cdot m/A}.
$$

A lever carrying mass m a distance L from a horizontal-axis joint has gravity torque magnitude mgL|cos θ| when θ is measured from horizontal. At rest, motor torque must oppose the load torque so that their signed sum is zero. A joint holding a load can therefore need nonzero current even at zero position error. A mechanical brake or genuine self-locking mechanism may hold the load without current; a strain-wave (harmonic) gearbox is **not inherently self-locking**.

$$
J\alpha=M_{\mathrm{motor}}+M_{\mathrm{load}},\quad
\alpha=0\ \Longrightarrow\ M_{\mathrm{motor}}=-M_{\mathrm{load}},
$$
$$
|M_g|=mgL|\cos\theta|.
$$

Outrunner BLDC motors rotate their outside shell, while inrunner BLDC motors rotate an internal rotor. “Rotor” always means the rotating part and “stator” the stationary part; their radial arrangement does not change those definitions.

<a id="section-7"></a>
## 7. Checks and limitations

In all examples, currents are idealized and do not represent real hardware instructions. A real drive needs correct current definitions, limits, encoder calibration, thermal constraints, filtering, anti-windup, interlocks, and safe testing. PID gains that work in one model are not universal.

[Math foundation](00-calculus-foundations.md) · [Trigonometry table](../TRIGONOMETRY.md) · [First-order dynamics](02-first-order-dynamics.md)
