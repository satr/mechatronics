# 0. 微积分基础：机械实例中的导数、极限和积分

**语言:** [en](../../en/notes/00-calculus-foundations.md) · [fr](../../fr/notes/00-calculus-foundations.md) · [de](../../de/notes/00-calculus-foundations.md) · [it](../../it/notes/00-calculus-foundations.md) · [es](../../es/notes/00-calculus-foundations.md) · [pt](../../pt/notes/00-calculus-foundations.md) · [zh](00-calculus-foundations.md) · [ja](../../ja/notes/00-calculus-foundations.md) · [nb](../../nb/notes/00-calculus-foundations.md) · [ru](../../ru/notes/00-calculus-foundations.md) · [ko](../../ko/notes/00-calculus-foundations.md) · [fi](../../fi/notes/00-calculus-foundations.md) · [pl](../../pl/notes/00-calculus-foundations.md)

**本页使用的单位（示例前先解释）:** `s` — 秒; `mm` — 毫米 = 0.001 m; `mm/s` — 毫米 / 秒 — 线速度; `mm/s²` — 毫米 / 秒² — 加速度; `kg·m²` — 千克 · 米² — 转动惯量; `rad/s` — 弧度 / 秒 — 角速度; `rad/s²` — 弧度 / 秒² — 角加速度; `N·m` — 牛顿 · 米 — 转矩; `W` — 瓦特; `rpm` — 每分钟转数; `N/m` — 牛顿 / 米 — 刚度; `mm³/s` — 毫米³ / 秒 — 体积流量; `%` — 百分比（百分之一）; `m` — 米; `kg` — 千克; `N` — 牛顿; `J` — 焦耳; `rad` — 弧度. [完整单位表](../UNITS.md).

[README](../README.md) · [Integral table](../INTEGRAL_TABLE.md) · [Trigonometry table](../TRIGONOMETRY.md) · [Motion](01-motion-calculus.md) · [Dynamics](02-first-order-dynamics.md) · [Symbols](../SYMBOLS.md)

> **教学近似:** 请独立核实模型与单位；不要用演示代码控制真实设备.

**自然指数函数**为 $\exp(x)=\mathrm{e}^{x}$，其中**欧拉数** $\mathrm{e}\approx2.71828$。它描述连续增长或衰减：$\exp(0)=1$，$\exp(-1)\approx0.3679$。自然对数 $\ln$ 是其反函数：$\ln(\exp(x))=x$。参见[符号表](../SYMBOLS.md)。

**导数（derivative）**描述某个量在此刻变化得多快；**二阶导数（second derivative）**描述这个变化速度如何变化。**积分（integral）**累计微小变化。**极限（limit）**给出瞬时变化率的严格定义；**对数（logarithm）**可以从指数响应中求出所需时间。

这些工具用于机床运动轴、伺服驱动器、机器人关节、弹簧和传感器。先确定物理问题，再选择规则并检查单位。

## 目录

- [1. 从测量变化到数学模型](#section-1)
- [2. 极限与一阶导数](#section-2)
- [3. 一阶与二阶导数：运动轴](#section-3)
- [4. 链式法则：转动能量](#section-4)
- [5. 指数与对数：响应时间](#section-5)
- [6. 积分：位移与机械功](#section-6)
- [7. 扩展例题：膨胀的球体](#section-7)
- [8. 单位、检查与练习](#section-8)

<a id="section-1"></a>
## 1. 从测量变化到数学模型

| 物理问题 | 数学工具 |
| --- | --- |
| 轴在**此刻**移动多快？ | 一阶导数 $dx/dt$ |
| 速度变化得多快？ | 二阶导数 $d^2x/dt^2$ |
| 何时达到 90 %？ | 对数 $\ln$ |
| 2 s 内移动多少？ | 定积分 $\int v\ \mathrm{d}t$ |
| 变力做了多少功？ | 积分 $\int F\ \mathrm{d}x$ |

<a id="section-2"></a>
## 2. 极限与一阶导数

两次测量的**有限差分（finite difference）**给出时间间隔内的平均变化率。当间隔趋于零时，它的极限就是导数。

$$
v(t)=\frac{dx}{dt}=\lim_{h\to0}\frac{x(t+h)-x(t)}{h}.
$$

设位置 $x(t)=a t^2$，其中 $a=2\ \mathrm{mm/s^2}$。先展开分子，再求极限：

$$
\frac{x(t+h)-x(t)}h=\frac{a[(t+h)^2-t^2]}h=a(2t+h)\longrightarrow 2at.
$$

要在令 $h$ 趋近于零**之前**约去因子 $h$。在 $t=1\ \mathrm{s}$ 时，瞬时速度为 $4\ \mathrm{mm/s}$。不能直接把未定义的 $0/0$ 当作数值。

**常用求导法则（differentiation rules）**：$c$ 和 $n$ 为常数；三角函数自变量使用弧度。

| 规则 | 公式 |
| --- | --- |
| 常数 | $\frac{d}{dt}c=0$ |
| 幂函数 | $\frac{d}{dt}t^n=n t^{n-1}$ |
| 系数与和 | $(cf+g)'=cf'+g'$ |
| 乘积 | $(fg)'=f' g+fg'$ |
| 商，$g\ne0$ | $\left(\frac{f}{g}\right)'=\frac{f' g-fg'}{g^2}$ |
| 复合函数 | $\frac{d}{dt}f(g(t))=f'(g(t))g'(t)$ |
| 指数函数 | $\frac{d}{dt}\exp(t)=\exp(t)$ |
| 自然对数，$t>0$ | $\frac{d}{dt}\ln t=\frac1t$ |
| 正弦 / 余弦 | $\frac{d}{dt}\sin t=\cos t$, $\frac{d}{dt}\cos t=-\sin t$ |

![位置曲线切线斜率与速度曲线下的面积](../../../assets/figures/calculus_slope_area.svg)

<a id="section-3"></a>
## 3. 一阶与二阶导数：运动轴

一辆滑台的初始位置为 2 mm，初速度为 3 mm/s，恒定加速度为 4 mm/s²。其位置函数：

$$
x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2.
$$

**一阶导数**是速度。常数项求导为零，一次项给出 3 mm/s，二次项变为关于时间的一次项。

$$
v(t)=\frac{dx}{dt}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t.
$$

**二阶导数**是加速度。对速度再次求导。2 s 时位置为 16 mm、速度为 11 mm/s、加速度为 4 mm/s²。

$$
a(t)=\frac{d^2x}{dt^2}=\frac{dv}{dt}=4\ \mathrm{mm/s^2}.
$$

二阶导数的单位是长度/时间²，**不是**一阶导数的平方。

<a id="section-4"></a>
## 4. 链式法则：转动能量

旋转飞轮储存动能。如果角速度 $\omega$ 随时间变化，能量 $E$ 通过角速度变化；这就是**链式法则（chain rule）**。

$$
E(\omega)=\frac12J\omega^2,\quad \omega=\omega(t),
$$
$$
\frac{dE}{dt}=\frac{dE}{d\omega}\frac{d\omega}{dt}=J\omega\alpha=M\omega=P.
$$

取 $J=0.01\ \mathrm{kg\cdot m^2}$、$\omega=10\ \mathrm{rad/s}$、$\alpha=2\ \mathrm{rad/s^2}$，转矩 $J\alpha=0.02\ \mathrm{N\cdot m}$，瞬时机械功率为 $0.2\ \mathrm{W}$，即 $P=M\omega$。

<a id="section-5"></a>
## 5. 指数与对数：响应时间

在简单的一阶系统模型中，速度按指数规律趋近最终值。$\tau$ 为**时间常数（time constant）**，单位秒。

$$
\omega(t)=\omega_\infty\bigl(1-\exp(-t/\tau)\bigr),\quad t\ge0,\ \tau>0.
$$

这个公式假设**初始角速度为零**，即 $\omega(0)=0$，且最终目标 $\omega_\infty$ 保持不变。如果初始角速度为 $\omega_0\ne0$，同一个一阶模型的通式是：

$$
\omega(t)=\omega_\infty+(\omega_0-\omega_\infty)\exp(-t/\tau).
$$

**初始速度非零的计算示例：** 取 $\omega_0=200\ \mathrm{rpm}$、$\omega_\infty=1000\ \mathrm{rpm}$、$\tau=0.5\ \mathrm{s}$。经过一个时间常数（$t=0.5\ \mathrm{s}$）时：

$$
\omega(\tau)=1000+(200-1000)\exp(-1)\approx705.7\ \mathrm{rpm}.
$$

这里完成的是 **800 rpm 变化量的 63.2 %**，并非最终速度 1000 rpm 的 63.2 %。在 $t=0$ 时公式给出 200 rpm；随着时间增加，结果趋向 1000 rpm。此计算仅用于数学说明，不是电机指令。

指数函数表示初始误差还剩多少。要计算**何时**剩下某一比例，使用**自然对数（natural logarithm）** $\ln$，它与 $\exp$ 互为反函数。$0.1$ 是无量纲的。

$$
\exp(-t/\tau)=0.1
\quad\Longrightarrow\quad
-\frac{t}{\tau}=\ln(0.1)
\quad\Longrightarrow\quad
t=-\tau\ln(0.1)=\tau\ln(10)\approx2.303\tau.
$$

达到最终变化的 90 % 时，初始误差剩下 10 %。若 $\tau=0.5\ \mathrm{s}$，理想模型给出约 1.151 s。真实驱动器还可能有限幅和延迟。

当 $z>0$ 时，$\ln z$ 的导数为 $1/z$；如果 $z=z(t)$，还要按链式法则乘 $dz/dt$。有单位的物理量必须先构造成无量纲比值再取对数。

$$
\ln(1)=0,\quad \ln(\mathrm{e})=1,\quad \ln(\mathrm{e}^{z})=z,\quad \frac{d}{dz}\ln z=\frac1z\ (z>0).
$$

<a id="section-6"></a>
## 6. 积分：位移与机械功

**不定积分（indefinite integral）**给出一族原函数（antiderivatives），带积分常数 $C$。**定积分（definite integral）**计算某个区间上的累计变化。

$$
\int 4t\ \mathrm{d}t=2t^2+C,\qquad \int t^n\ \mathrm{d}t=\frac{t^{n+1}}{n+1}+C\ (n\ne-1).
$$

**位移例题。** 滑台初始位置 $x_0=2\ \mathrm{mm}$，速度为 $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$。求 0–2 s 的位移：

$$
\Delta x=\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
$$
$$
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}=6\ \mathrm{mm}+8\ \mathrm{mm}=14\ \mathrm{mm}.
$$

位移为 14 mm；加上初始位置得 $x(2)=16\ \mathrm{mm}$。负速度产生负的有符号位移，但路程不能为负。

**弹簧做功例题。** 将刚度 $k=200\ \mathrm{N/m}$ 的理想线性弹簧从 $x=0$ 拉伸到 $x=0.01\ \mathrm{m}$。力随伸长量增大，应累计每一小段的功：

$$
F(x)=kx,\qquad W=\int_0^{0.01\ \mathrm{m}}kx\ \mathrm{d}x
=\left[\frac{kx^2}{2}\right]_0^{0.01\ \mathrm{m}}
=\frac{200\ \mathrm{N/m}}2(0.01\ \mathrm{m})^2=0.01\ \mathrm{J}.
$$

做功为 0.01 J。若把最终力 $F=2\ \mathrm{N}$ 直接乘整个距离，会错误得到 0.02 J；这里力不是常数。

<a id="section-7"></a>
## 7. 扩展例题：膨胀的球体

**可选链式法则例题。** 球体体积取决于半径，半径又可能随时间变化；这与飞轮能量通过角速度随时间变化具有相同的依赖结构。

$$
V(r)=\frac43\pi r^3,\qquad \frac{dV}{dt}=\frac{dV}{dr}\frac{dr}{dt}=4\pi r^2\frac{dr}{dt}.
$$

当 $r=10\ \mathrm{mm}$、$dr/dt=1\ \mathrm{mm/s}$ 时，体积变化率为 $400\pi\approx1256.64\ \mathrm{mm^3/s}$。若 $r(t)=10\ \mathrm{mm}+(1\ \mathrm{mm/s^2})t^2$，2 s 时 $r=14\ \mathrm{mm}$，$dr/dt=4\ \mathrm{mm/s}$，结果为 $3136\pi\approx9852.03\ \mathrm{mm^3/s}$。

<a id="section-8"></a>
## 8. 单位、检查与练习

**检查：** 位置的一阶导数单位为 m/s，二阶导数为 m/s²；力对位移的积分单位为 N·m = J；不定积分不能漏掉 $C$；导数描述局部变化，积分描述累计变化；数学微分 $\mathrm{d}t$ 与数值程序中的有限步长 `dt` 不同。

**练习：** (1) 对 $x(t)=5\ \mathrm{mm}+(2\ \mathrm{mm/s})t+(1\ \mathrm{mm/s^2})t^2$，求 3 s 时的速度与加速度。(2) 当 $\tau=1\ \mathrm{s}$ 时，一阶响应达到 90 % 需要多久？(3) 4 mm/s 匀速运动 2 s 的位移？**答案：** 8 mm/s 和 2 mm/s²；约 2.303 s；8 mm。

**完整解题步骤：**

1. $v(t)=\frac{dx}{dt}=2\ \mathrm{mm/s}+2(1\ \mathrm{mm/s^2})t$; $v(3\ \mathrm{s})=2+2\cdot3=8\ \mathrm{mm/s}$. $a(t)=\frac{dv}{dt}=2\ \mathrm{mm/s^2}$.
2. $f(t)=1-\exp(-t/\tau)=0.9$; $\exp(-t/\tau)=0.1$; $t=-\tau\ln(0.1)=\tau\ln(10)$. $\tau=1\ \mathrm{s}$; $t\approx2.303\ \mathrm{s}$.
3. $\Delta x=\int_0^{2\ \mathrm{s}}(4\ \mathrm{mm/s})\ \mathrm{d}t=(4\ \mathrm{mm/s})(2\ \mathrm{s})=8\ \mathrm{mm}$.


[Integral reference](../INTEGRAL_TABLE.md) · [Trigonometry](../TRIGONOMETRY.md) · [Next: motion](01-motion-calculus.md) · [Python exercises](../exercises/README.md)
