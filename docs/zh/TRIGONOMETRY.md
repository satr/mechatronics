# 三角函数：角度、正弦、余弦、正切与反正切

**语言:** [en](../en/TRIGONOMETRY.md) · [fr](../fr/TRIGONOMETRY.md) · [de](../de/TRIGONOMETRY.md) · [it](../it/TRIGONOMETRY.md) · [es](../es/TRIGONOMETRY.md) · [pt](../pt/TRIGONOMETRY.md) · [zh](TRIGONOMETRY.md) · [ja](../ja/TRIGONOMETRY.md) · [nb](../nb/TRIGONOMETRY.md) · [ru](../ru/TRIGONOMETRY.md) · [ko](../ko/TRIGONOMETRY.md) · [fi](../fi/TRIGONOMETRY.md) · [pl](../pl/TRIGONOMETRY.md)

**本页使用的单位（示例前先解释）:** `°` — 度; `rad` — 弧度; `kg` — 千克; `m` — 米; `m/s²` — 米 / 秒² — 加速度; `N·m` — 牛顿 · 米 — 转矩; `mm` — 毫米 = 0.001 m; `N` — 牛顿. [完整单位表](UNITS.md).

[README](README.md) · [Calculus](notes/00-calculus-foundations.md) · [Integral table](INTEGRAL_TABLE.md)

<a id="unit-circle-values"></a>
## 单位圆：正弦与余弦

单位圆上角度为 θ 的点的坐标是 **(cos θ, sin θ)**。角度从 +X 轴逆时针测量。余弦（cosine）是水平坐标，正弦（sine）是竖直坐标。一幅图列出全部 16 个常用角度的精确坐标对；唯一的表格还给出小数近似、正切和反正切的主值。

![单一单位圆，标出 16 个角度及精确坐标对 (cos θ, sin θ)。](../../assets/figures/unit_circle_reference.svg)

*单一单位圆，标出 16 个角度及精确坐标对 (cos θ, sin θ)。*

**精确分数和小数近似:**

| θ | cos θ (精确值) | cos θ (小数) | sin θ (精确值) | sin θ (小数) | tan θ (精确值) | tan θ (小数) | arctan(tan θ) 主值 |
| --- | --- | ---: | --- | ---: | --- | ---: | --- |
| 0° | $1$ | 1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 30° | $\frac{\sqrt3}{2}$ | 0.8660 | $\frac12$ | 0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 45° | $\frac{\sqrt2}{2}$ | 0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 60° | $\frac12$ | 0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 90° | $0$ | 0.0000 | $1$ | 1.0000 | **无定义** | — | — |
| 120° | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 135° | $-\frac{\sqrt2}{2}$ | -0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 150° | $-\frac{\sqrt3}{2}$ | -0.8660 | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |
| 180° | $-1$ | -1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 210° | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 225° | $-\frac{\sqrt2}{2}$ | -0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 240° | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 270° | $0$ | 0.0000 | $-1$ | -1.0000 | **无定义** | — | — |
| 300° | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 315° | $\frac{\sqrt2}{2}$ | 0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 330° | $\frac{\sqrt3}{2}$ | 0.8660 | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |

90° 与 270° 处 cos θ = 0，正切 **无定义**，因此 arctan(tan θ) 也无定义。最后一列为 (−90°, 90°) 内的**主值**，不一定等于原角度，例如 arctan(tan 135°) = −45°，arctan(tan 225°) = 45°。小数四舍五入保留四位。360° 的值与 0° 相同。

<a id="trigonometric-identities"></a>
### 常用三角恒等式

角度偏移 90° 可使正弦与余弦互换，有时需要变号。括号十分关键：cos(θ − 90°) 是角度差的余弦，并非 cos θ 减去 90。

$$
\cos(90^\circ-\theta)=\sin(\theta),\qquad
\sin(90^\circ-\theta)=\cos(\theta)
$$

$$
\cos(\theta-90^\circ)=\sin(\theta),\qquad
\sin(\theta+90^\circ)=\cos(\theta)
$$

$$
\cos(\theta+90^\circ)=-\sin(\theta),\qquad
\sin(\theta-90^\circ)=-\cos(\theta)
$$

**负角与周期性:**

$$
\sin(-\theta)=-\sin(\theta),\qquad
\cos(-\theta)=\cos(\theta)
$$

$$
\tan(-\theta)=-\tan(\theta),\qquad
\tan(\theta)=\frac{\sin(\theta)}{\cos(\theta)}
$$

$$
\sin(\theta+360^\circ)=\sin(\theta),\qquad
\cos(\theta+360^\circ)=\cos(\theta)
$$

$$
\tan(\theta+180^\circ)=\tan(\theta),\qquad
\sin^2(\theta)+\cos^2(\theta)=1
$$

各象限符号（按 cos、sin、tan 顺序）：I (+,+,+)，II (−,+,−)，III (−,−,+)，IV (+,−,−)。负角按顺时针测量。

求反三角函数时应同时检查象限和主值区间。

<a id="inverse-cosine-reference"></a>
### 反余弦与角度估计

在 0° 到 180° 之间，余弦从 1 单调下降到 −1。因此 arccos(0.19) 略小于 80°：cos 80°≈0.1736，而 arccos(0.19)≈79.05°。由于 cos(+θ)=cos(−θ)，可能出现符号相反的两组关节角解。arccos 主值位于 0° 到 180°。

![cos θ versus θ, with arccos(0.19) marked](../../assets/figures/arccos_reference_curve.svg)



## 图解：对边、邻边与斜边

![三个直角三角形：正弦为对边 a 与斜边 c 之比，余弦为邻边 b 与 c 之比，正切为 a 与 b 之比。](../../assets/figures/trig_ratios.svg)

图中，**a** 是角 θ 的对边（opposite），**b** 是邻边（adjacent），**c** 是斜边（hypotenuse）。对锐角 θ，有 $\sin\theta=a/c$、$\cos\theta=b/c$ 和 $\tan\theta=a/b$（要求 $b\ne0$）。**边长非负**；直角三角形示意图本身无法显示负角或其他象限中的函数符号。若从 x 轴正方向测量有向角，则 $\sin(+60^\circ)=+\sqrt3/2$，而 $\sin(-60^\circ)=-\sqrt3/2$。

## 机械例子：杠杆上的重力矩

质量 m 的载荷距转轴 L，杠杆与水平面夹角 θ，则重力矩的**大小**为 mgL|cos θ|。正负号取决于所规定的转动方向。

$$
|M_g|=mgL|\cos\theta|.
$$

若 m = 0.5 kg、L = 0.2 m、g = 9.81 m/s²、θ = 60°，力矩大小为 0.4905 N·m；在 0° 为 0.981 N·m，在 90° 为零（理想点载荷）。

## 反向例子：由斜率求角度

一个轴在水平移动 0.1 m 时上升 0.05 m，斜率比为 0.5，因此 θ = arctan(0.5) ≈ 26.565°。输入是长度比，不是“0.5 度”。

$$
\tan\theta=\frac{0.05\ \mathrm{m}}{0.1\ \mathrm{m}}=0.5,\qquad \theta=\arctan(0.5)\approx26.565^\circ.
$$

角度换算：θ_rad = θ_deg·π/180。数值数学库通常需要弧度。

$$
\theta_{\mathrm{rad}}=\theta_{\mathrm{deg}}\frac{\pi}{180}.
$$

### 二维向量的方向：为何需要 `atan2`

对于从原点指向 $(x,y)$ 的向量，普通反正切只能看到比值 $y/x$。向量 $(1, -1)$ 和 $(-1, 1)$ 具有相同的比值，却指向**不同象限**。例如 $x=-1\ \mathrm{mm}$、$y=+1\ \mathrm{mm}$ 时，仅使用比值会得到错误的世界坐标方向：

$$
\arctan\left(\frac{y}{x}\right)=\arctan(-1)=-45^\circ,\qquad
\operatorname{atan2}(+1, -1)=+135^\circ.
$$

`atan2(y, x)` 同时考虑**两个分量的符号**，可求出非零二维向量的方向。两个参数必须使用相同的长度单位。$x=0$ 时无法计算 $y/x$，但若 $y\ne0$，`atan2` 仍可给出坐标轴方向。在 $(0, 0)$ 处方向没有定义；$+180^\circ$ 和 $-180^\circ$ 表示相同方向。这对计算[坐标系中的角度](notes/04-coordinate-frames.md)尤为重要。

## 余弦定理：双连杆几何

![Two-link robot triangle OAB, exact link lengths and the law of cosines](../../assets/figures/two_link_cosine_law.svg)

基座 O、肘关节 A、工具 B 构成三角形：OA = L1，AB = L2，OB = r（基座到工具的直线距离）。示例为 L1 = 100 mm、L2 = 50 mm、r = 120 mm。三角形内角 φ 不等于第二关节的相对转角 θ2：φ = 180° − |θ2|。图中 θ2 为负，镜像姿态的 θ2 为正。

余弦定理 (law of cosines) 为 $r^2=L_1^2+L_2^2-2L_1L_2\cos\varphi$。由于 $\cos(180^\circ-|\theta_2|)=-\cos\theta_2$，等价于 $r^2=L_1^2+L_2^2+2L_1L_2\cos\theta_2$，因此 $\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}$。本例 $(14400-10000-2500)/10000=0.19$，$|\theta_2|\approx79.05^\circ$。要达到指定 (X,Y)，还要计算 θ1。


[微积分](notes/00-calculus-foundations.md) · [反馈控制](notes/03-feedback-control.md)
