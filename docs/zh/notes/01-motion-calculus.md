# 1. 运动、导数与积分


**切换此页语言:** [en](../../en/notes/01-motion-calculus.md) · [fr](../../fr/notes/01-motion-calculus.md) · [de](../../de/notes/01-motion-calculus.md) · [it](../../it/notes/01-motion-calculus.md) · [es](../../es/notes/01-motion-calculus.md) · [pt](../../pt/notes/01-motion-calculus.md) · [zh](01-motion-calculus.md) · [ja](../../ja/notes/01-motion-calculus.md) · [nb](../../nb/notes/01-motion-calculus.md) · [ru](../../ru/notes/01-motion-calculus.md) · [ko](../../ko/notes/01-motion-calculus.md) · [fi](../../fi/notes/01-motion-calculus.md) · [pl](../../pl/notes/01-motion-calculus.md)

**本页使用的单位（示例前先解释）:** `s` — 秒; `mm` — 毫米 = 0.001 m; `mm/s` — 毫米 / 秒 — 线速度; `mm/s²` — 毫米 / 秒² — 加速度; `%` — 百分比（百分之一）. [完整单位表](../UNITS.md).

**基础:** [0. 微积分基础：导数、微分与积分](00-calculus-foundations.md) · [积分公式表](../INTEGRAL_TABLE.md)

[README](../README.md) · [公式速查表](../CHEATSHEET.md) · [Python 练习](../exercises/README.md) · [一阶动力学与旋转运动](02-first-order-dynamics.md)

> **警告：** 本仓库是人工智能辅助编写的教学资料，可能存在事实错误、公式错误、翻译不准确或不成立的假设。使用者自行承担风险，必须独立验证计算结果。**切勿使用示例程序控制真实机器、电机或机器人。**

## 要点回顾

路程是运动轨迹的总长度，位移是末位置减去初位置。速率（speed）非负；速度（velocity）包含方向，可以在所选坐标轴上取负值。位置对时间求导得到瞬时速度；对带符号速度积分得到位移。

**英文术语：**

- 路程 (distance traveled)
- 位移 (displacement)
- 速率 (speed)
- 速度矢量 (velocity)
- 导数 (derivative)
- 积分 (integral)
- 数值积分 (numerical integration)
- 显式欧拉法 (explicit Euler method)

**单位说明（units）：** 这里时间以秒（s，second）计，位置以毫米（mm，millimeter）计，速度以毫米每秒（mm/s，millimeter per second）计；其他常用单位见[公式速查表](../CHEATSHEET.md)。

## 本页目录

- [1. 运动示例](#section-1)
- [2. 导数与瞬时速度](#section-2)
- [3. 积分与位移](#section-3)
- [4. 数值积分](#section-4)
- [5. 动手试试](#section-5)
- [6. 进一步说明（选读）](#section-6)
  - [为什么 2t² 的导数是 4t](#power-rule-derivation)
  - [位移表格数值的来源](#motion-values-derivation)

[SI 单位与小数点说明](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. 运动示例

有关单位、推导和数值方法的限制，请参阅[进一步说明](#section-6)。

假设虚拟直线轴以 $+3\ \mathrm{mm/s}$ 运动两秒，再以 $-3\ \mathrm{mm/s}$ 运动两秒。位移为 $+6-6=0\ \mathrm{mm}$，路程却为 $12\ \mathrm{mm}$。圆周运动中，即使速率恒定，速度矢量的方向也不断变化。

$$
\overline{v}=\frac{x(t_2)-x(t_1)}{t_2-t_1}.
$$

$$
\text{平均速率}=\frac{\text{总路程}}{t_2-t_1}.
$$

在**完整的四秒内**，沿轴的平均速度和平均速率得到**不同结果**。虽然轴回到起点，仍走过 12 mm 的路程：

$$
\overline{v}_x=\frac{0\ \mathrm{mm}}{4\ \mathrm{s}}=0\ \mathrm{mm/s}
$$

$$
\overline{\lvert v\rvert}=\frac{12\ \mathrm{mm}}{4\ \mathrm{s}}=3\ \mathrm{mm/s}
$$

所以平均速率**不一定等于平均速度矢量的大小**。沿圆周完整转一圈也是如此：由于回到起点，平均速度矢量为零，但路程和平均速率都为正。

<a id="section-2"></a>

## 2. 导数与瞬时速度

设 $x(t)=2t^2\ \mathrm{mm}$，其中 $t$ 的单位为秒，则 $v(t)=4t\ \mathrm{mm/s}$. **为什么出现 4？** 幂函数求导法则（power rule）给出 $d(t^2)/dt=2t$，因此对 $2t^2$ 求导为 $2\cdot2t=4t$。[查看完整计算与单位](#power-rule-derivation)。。当 $t=1\ \mathrm{s}$ 时，瞬时速度为 $4\ \mathrm{mm/s}$。取 $dt=1$、$0.1$、$0.01\ \mathrm{s}$，前向差分估计分别为 $6$、$4.2$、$4.02\ \mathrm{mm/s}$。

$$
v(t)=\frac{dx}{dt},\qquad v(t)\approx\frac{x(t+dt)-x(t)}{dt}.
$$

**为什么时间步长太小反而会得到错误结果：** 在 $t=1\ \mathrm{s}$，$x(t)=2t^2$ 的精确导数为 $4\ \mathrm{mm/s}$。但若取 $dt=1e-17\ \mathrm{s}$，Python 的 `float` 会把 `t + dt` 舍入回 `t`。两次计算的位置变成相同，差商便错误地给出零速度。在更小的数值尺度上，即使导数不为零，两次位置计算也可能都下溢到零。练习函数 [`forward_derivative`](../../../exercises/01_motion_and_integral.py) 现在会在这些情况下抛出 `ValueError`，而不是返回错误的零值。函数仍然使用有限差分；应选取浮点数能够分辨的步长，而不是无限缩小步长。

<a id="section-3"></a>

## 3. 积分与位移

带符号速度的积分可能为负或零，速度绝对值的积分则是非负的路程。对于 $0$ 到 $2\ \mathrm{s}$ 内的 $v(t)=2t\ \mathrm{mm/s}$，精确位移为 $4\ \mathrm{mm}$。

$$
\Delta x=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t,\qquad
s=\int_{t_1}^{t_2}|v(t)|\ \mathrm{d}t.
$$

从几何上看，带符号速度的积分对应速度–时间图像下的带符号面积。**这里使用的是与第 2 节不同的运动模型。** 第 2 节的位置为 $x(t)=2t^2$，其导数是 $v(t)=4t$；而本节为了演示积分，特意选用另一速度函数 $v(t)=2t$。它对应的位置为 $x(t)=t^2+C$（各量的单位需保持一致）。不能把 $2t$ 当作 $2t^2$ 的导数；这是两种不同的运动规律。

<a id="section-4"></a>

## 4. 数值积分

精确位移与左端点欧拉近似的比较（合成数据）。

![精确位移与左端点欧拉近似的比较（合成数据）。](../../../assets/figures/euler_vs_exact.svg)

显式欧拉法使用每一步**起点**的速度，而不是该区间内的真实平均速度。在速度不断增大的例子中，它低估位移：$dt=0.5$、$0.1$、$0.01\ \mathrm{s}$ 时分别得到 $3$、$3.8$、$3.98\ \mathrm{mm}$，精确值为 $4\ \mathrm{mm}$。由于本例速度随时间线性变化，梯形法在这里给出精确结果。

$$
x_{n+1}=x_n+v(t_n)\ dt.
$$

| `dt` (s) | Euler (mm) |
| ---: | ---: |
| 0.5 | 3.000 |
| 0.1 | 3.800 |
| 0.01 | 3.980 |
| 精确解 | 4.000 |


[查看 3、3.8 和 3.98 的计算。](#motion-values-derivation)

<a id="section-5"></a>

## 5. 动手试试

运行运动模拟程序，逐渐减小 $dt$。思考：为什么往返运动的位移可以为零，而路程仍为正？

[01_motion_and_integral.py](../../../exercises/01_motion_and_integral.py)

<a id="section-6"></a>

## 6. 进一步说明（选读）

### 单位与系数

若 $t$ 以秒为单位，$x(t)=2t^2$ mm 是简写：系数实际具有 $2\ \mathrm{mm/s^2}$ 的单位，因此 $v(t)=4t$ 的单位为 mm/s。使用公式前应检查单位。

### 近似计算的局限

有限差分 (finite difference) 用非零时间间隔估计导数。较小步长通常减小截断误差，但过小的步长可能放大浮点舍入误差或测量噪声。欧拉法采用步长起点的数值。

### 多维运动

若位置向量为 $\mathbf r(t)$，速度向量为 $\mathbf v=d\mathbf r/dt$，速率为 $\|\mathbf v\|$，总路程为 $s=\int\|\mathbf v(t)\|dt$。


<a id="power-rule-derivation"></a>

### 为什么 $2t^2$ 的导数是 $4t$



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

### 位移表格数值的来源

$$
a=2\ \mathrm{mm/s^2},\qquad v(t)=at,\qquad 0\le t\le2\ \mathrm{s}.
$$

$$
\Delta x=\int_{0}^{2\ \mathrm{s}}at\ \mathrm{d}t
=\left[\frac{at^2}{2}\right]_{0}^{2\ \mathrm{s}}
=4\ \mathrm{mm}.
$$



符号 $\sum$（希腊大写字母 sigma，**求和符号** / summation）表示把若干项加起来。在 $\sum_{n=0}^{N-1}(2nh)h$ 中，指标 $n$ 依次取 $0; 1; \ldots; N-1$，一共有 $N$ 项。可以把它想成 Python 的 `for` 循环累加。例如，$\sum_{n=1}^{3}n=1+2+3=6$。 [← 数学符号说明](../SYMBOLS.md#summation).

$$
h=\frac{dt}{1\ \mathrm{s}},\qquad N=\frac{2}{h}.
$$

$$
x_{\mathrm{Euler}}(2\ \mathrm{s})
=\left[\sum_{n=0}^{N-1}(2nh)h\right]\ \mathrm{mm}
=\left[h^2N(N-1)\right]\ \mathrm{mm}
=(4-2h)\ \mathrm{mm}.
$$

这里 `h` 是以秒为单位的时间步长 `dt` 的数值（`dt = 0.5 s` 时 `h = 0.5`）；`N` 是步数。计算结果是**以毫米（mm，millimetre）表示的位移**，不是无量纲数。



这里 $t$ 的单位是秒（s，second），$v$ 为毫米每秒（mm/s，millimeter per second）。当 $dt$ 依次为 $0.5$、$0.1$、$0.01$ 秒时，位移为 $3$、$3.8$、$3.98$ 毫米（mm，millimeter）。本式要求 $2/dt$ 为整数。
