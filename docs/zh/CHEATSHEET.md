# 公式速查表

**切换此页语言:** [en](../en/CHEATSHEET.md) · [fr](../fr/CHEATSHEET.md) · [de](../de/CHEATSHEET.md) · [it](../it/CHEATSHEET.md) · [es](../es/CHEATSHEET.md) · [pt](../pt/CHEATSHEET.md) · [zh](CHEATSHEET.md) · [ja](../ja/CHEATSHEET.md) · [nb](../nb/CHEATSHEET.md) · [ru](../ru/CHEATSHEET.md) · [ko](../ko/CHEATSHEET.md) · [fi](../fi/CHEATSHEET.md) · [pl](../pl/CHEATSHEET.md)

**本页使用的单位（示例前先解释）:** `s` — 秒; `m` — 米; `m/s` — 米 / 秒 — 线速度; `rad/s` — 弧度 / 秒 — 角速度; `kg·m²` — 千克 · 米² — 转动惯量; `N·m` — 牛顿 · 米 — 转矩; `N·m·s/rad` — 牛顿 · 米 · 秒 / 弧度 — 速度增益; `J` — 焦耳; `mm` — 毫米 = 0.001 m; `mm/s` — 毫米 / 秒 — 线速度; `%` — 百分比（百分之一）. [完整单位表](UNITS.md).

[目录](README.md) · [运动、导数与积分](notes/01-motion-calculus.md) · [一阶动力学与旋转运动](notes/02-first-order-dynamics.md) · [Python 练习](exercises/README.md)

> **警告：** 本仓库是人工智能辅助编写的教学资料，可能存在事实错误、公式错误、翻译不准确或不成立的假设。使用者自行承担风险，必须独立验证计算结果。**切勿使用示例程序控制真实机器、电机或机器人。**

| 要点回顾 | 公式速查表 |
| --- | --- |
| 位移 | $\Delta x=x_2-x_1$ |
| 路程 | $s=\int_{t_1}^{t_2}\lvert v(t)\rvert\ \mathrm{d}t\ge 0$ |
| 平均速度（矢量） | $\overline{v}=\frac{\Delta x}{\Delta t}$ |
| 平均速率 | $\frac{s}{\Delta t}$ |
| 瞬时速度 | $v(t)=\frac{dx}{dt}$ |
| 显式欧拉法 | $x_{n+1}=x_n+v_n\ dt$ |
| 一阶动态系统 | $\frac{dv}{dt}=\frac{u-v}{\tau}$ |
| 速度误差（speed error） | $\varepsilon(t)=u-v(t)$ |
| 时间常数 | $t=\tau$: $1-\exp(-1)\approx63.2\ \%$ |
| 净扭矩 | $M=J\alpha$ |
| 转动惯量与比例系数 | $\tau=\frac{J}{K}$ (仅适用于理想扭矩模型) |
| 旋转动能 | $E=\frac{1}{2}J\omega^2$ |

**符号说明：** $\varepsilon$ 是速度误差（speed error）；$\mathrm{e}\approx2.71828$ 是欧拉数（Euler’s number）；$\exp(z)=\mathrm{e}^{z}$。

**单位 (SI):**

| 符号 | 含义 | 单位（SI） |
| --- | --- | --- |
| `t, dt, τ` | 时间 (time) | 秒（s，second） |
| `x` | 位置 (position) | 米（m，meter） |
| `v` | 速率 (speed) | 米/秒（m/s，meter per second） |
| `ω` | 角速度 (angular velocity) | 弧度/秒（rad/s，radian per second） |
| `J` | 转动惯量 (moment of inertia) | 千克·平方米（kg·m²，kilogram square meter） |
| `M` | 扭矩 (torque) | 牛顿·米（N·m，newton meter） |
| `K` | 扭矩增益 (torque gain) | 牛顿·米·秒/弧度（N·m·s/rad） |
| `E` | 能量 (energy) | 焦耳（J，joule） |

中点 `·` 表示单位相乘，不是逗号分隔。目标值 $u$ 在直线运动模型中为线速度，在旋转模型中为角速度。

## 注意事项

不要混淆速率与有方向的速度、路程与位移、$dt$ 与 $\tau$。$\tau=\frac{J}{K}$ 仅适用于本文明确说明的扭矩模型；机械动能不等于电能消耗。

**英文术语：**

- 路程 (distance traveled)
- 位移 (displacement)
- 速率 (speed)
- 速度矢量 (velocity)
- 导数 (derivative)
- 积分 (integral)
- 数值积分 (numerical integration)
- 显式欧拉法 (explicit Euler method)

**英文术语：**

- 一阶系统 (first-order system)
- 时间常数 (time constant)
- 时间步长 (time step)
- 转动惯量 (moment of inertia)
- 扭矩 (torque)
- 控制器增益 (controller gain)
- 角加速度 (angular acceleration)
- 系统辨识 (system identification)
- 旋转动能 (rotational kinetic energy)

进一步学习：[导数与积分](notes/01-motion-calculus.md#section-6)、[模型假设与数值稳定性](notes/02-first-order-dynamics.md#section-7)。


[为什么恰好是这些百分比？查看推导。](notes/02-first-order-dynamics.md#time-constant-derivation)

[查看 3、3.8 和 3.98 的计算。](notes/01-motion-calculus.md#motion-values-derivation)


## 数学符号与记法

**Σ / ∑（求和 / summation）** 表示把若干项相加，例如 $\sum_{n=1}^{3}n=1+2+3=6$。[更多符号](SYMBOLS.md)。


## 积分公式表

[0. 微积分基础：导数、微分与积分](notes/00-calculus-foundations.md) · [积分公式表](INTEGRAL_TABLE.md)


## 反馈控制：PID 与保持转矩

| $\varepsilon=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}}$ | $u_P=K_p\varepsilon$, $u_I=K_i\int\varepsilon\ \mathrm{d}t$ |
| --- | --- |
| $M_{\mathrm{motor}}=K_t I$ | $\lvert M_g\rvert=mgL\lvert\cos\theta\rvert$ |

[反馈控制：PID 与保持转矩](notes/03-feedback-control.md) · [三角函数表及机械例题](TRIGONOMETRY.md)

<a id="joint-velocity"></a>
## 旋转、速度与雅可比矩阵

角速度单位为 rad/s，长度使用 mm 时线速度单位为 mm/s。

$$
v_x=-L\sin Q\cdot\dot Q,\qquad v_y=L\cos Q\cdot\dot Q
$$

$$
\det J=L_1L_2\sin Q_2
$$

[旋转、速度与雅可比矩阵](notes/05-velocity-jacobian.md)
