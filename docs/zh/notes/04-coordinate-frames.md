# 4. 机器人坐标系与平面运动学

**Languages:** [en](../../en/notes/04-coordinate-frames.md) · [fr](../../fr/notes/04-coordinate-frames.md) · [de](../../de/notes/04-coordinate-frames.md) · [it](../../it/notes/04-coordinate-frames.md) · [es](../../es/notes/04-coordinate-frames.md) · [pt](../../pt/notes/04-coordinate-frames.md) · [zh](04-coordinate-frames.md) · [ja](../../ja/notes/04-coordinate-frames.md) · [nb](../../nb/notes/04-coordinate-frames.md) · [ru](../../ru/notes/04-coordinate-frames.md) · [ko](../../ko/notes/04-coordinate-frames.md) · [fi](../../fi/notes/04-coordinate-frames.md) · [pl](../../pl/notes/04-coordinate-frames.md)

**本页使用的单位（示例前先解释）:** `mm` — 毫米 = 0.001 m; `°` — 度. [完整单位表](../UNITS.md).

[README](../README.md) · [三角函数](../TRIGONOMETRY.md) · [数学符号](../SYMBOLS.md) · [反馈控制](03-feedback-control.md)

> **教学模型:** 这些简化几何公式不能用于控制真实机器人或机器。

## 目录
1. [坐标系为什么重要](#section-1)
2. [点的旋转和平移](#section-2)
3. [多坐标系的组合](#section-3)
4. [双连杆正向运动学](#section-4)
5. [两种肘部姿态与可达空间](#section-5)
6. [带完整解答的练习](#section-6)
7. [模型限制与矩阵表达](#section-7)

<a id="section-1"></a>
## 1. 坐标系为什么重要

**坐标系 (coordinate frame)** 包含原点和有方向的坐标轴。固定的**世界坐标系 (world frame)** W 可以绑定在机器人基座，**工具坐标系 (tool frame)** T 随工具移动。同一物理点在不同坐标系中的数值坐标不同。位置表示点所在的位置，姿态表示坐标轴的方向。转换坐标本身不代表机器人实际运动。

所有长度使用同一单位（这里为 mm）。二维正角从世界 +X 轴逆时针测量。下标 w 表示世界，l 表示局部。模型假设连杆为刚体。

<a id="section-2"></a>
## 2. 点的旋转和平移

![世界坐标轴与旋转 +90° 的工具局部轴、点 P 和 Q。](../../../assets/figures/world_local_frames.svg)

*世界坐标轴与旋转 +90° 的工具局部轴、点 P 和 Q。*

图中工具 T 的世界原点为 (100 mm, 50 mm)，局部坐标轴旋转了 +90°。局部 +x 指向世界 +Y，局部 +y 指向世界 −X。因此局部 P=(0 mm, 10 mm) 转换为世界 (90 mm, 50 mm)，Q=(20 mm, 0 mm) 转换为 (100 mm, 70 mm)。

若局部点为 $(x_l,y_l)$、局部原点的世界坐标为 $(t_x,t_y)$、旋转角为 $\theta$，应**先旋转再平移**：

$$
x_w=t_x+x_l\cos\theta-y_l\sin\theta
$$

$$
y_w=t_y+x_l\sin\theta+y_l\cos\theta
$$

$\sin\theta$ 和 $\cos\theta$ 的符号取决于有向角。$\theta=0^\circ$ 时，只需加上原点的平移量。这些是坐标换算公式，不是电机指令。

<a id="section-3"></a>
## 3. 多坐标系的组合

坐标系可组合为 **W → T → S**（世界 → 工具 → 传感器）。保留上述 T，若 S 的原点在 T 中为 (20 mm, 0 mm)，且两者轴平行，则 S 的世界原点为 (100 mm, 70 mm)。S 中的点 (0 mm, 10 mm) 位于世界 (90 mm, 70 mm)。先转换到父坐标系，再向上组合。

对于列向量有 $T_{WS}=T_{WT}T_{TS}$；$T_{AB}$ 表示坐标**由 B 转到 A**。矩阵乘法顺序不可随意交换。

**完整矩阵计算（列向量）：** 工具坐标系 T 相对世界 W 旋转 +90°，其世界原点为 (100 mm, 50 mm)。传感器坐标系 S 相对 T 不再旋转，原点在 T 中为 (20 mm, 0 mm)，对应上一幅图中的 Q 点。旋转矩阵元素无量纲，平移分量的单位为 mm：

$$
T_{WT}=
\begin{bmatrix}
0 & -1 & 100\\
1 & 0 & 50\\
0 & 0 & 1
\end{bmatrix}
$$

$$
T_{TS}=
\begin{bmatrix}
1 & 0 & 20\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
$$

$$
T_{WS}=T_{WT}T_{TS}=
\begin{bmatrix}
0 & -1 & 100\\
1 & 0 & 70\\
0 & 0 & 1
\end{bmatrix}
$$

$$
T_{WS}\begin{bmatrix}0\\10\\1\end{bmatrix}
=\begin{bmatrix}90\\70\\1\end{bmatrix}
$$

矩阵相乘时，先把传感器在 T 中的偏移 (20 mm, 0 mm) 旋转为世界偏移 (0 mm, 20 mm)，再加到 (100 mm, 50 mm)。因此，S 中的点 (0 mm, 10 mm) 在 W 中为 (90 mm, 70 mm)。如果直接把 20 mm 加到世界 X 坐标上，就混淆了**在 T 中表示的偏移**与世界坐标。齐次坐标末尾的 1 无量纲。这是坐标数学；[ROS 2 的 tf2](06-ros2-foundations.md#section-7) 负责发布和查询带时间戳的变换，不负责求解逆运动学。

<a id="section-4"></a>
## 4. 双连杆正向运动学

![双连杆正向运动学：第一关节 30°、第二相对角 60°。](../../../assets/figures/two_link_fk.svg)

*双连杆正向运动学：第一关节 30°、第二相对角 60°。*

平面双连杆的长度为 $L_1,L_2$。第一关节角 $\theta_1$ 相对世界 +X 测量；第二关节角 $\theta_2$ **相对第一连杆**测量。因此第二连杆的绝对方向为 $\theta_1+\theta_2$。工具的位置是两个连杆向量之和：

$$
X=L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2)
$$

$$
Y=L_1\sin\theta_1+L_2\sin(\theta_1+\theta_2)
$$

若 L1=100 mm、L2=50 mm、$\theta_1=30^\circ$、$\theta_2=60^\circ$，肘关节位于 (86.60 mm, 50 mm)。第二连杆的世界角为 90°，竖直向上，工具位于 (86.60 mm, 100 mm)。

<a id="section-5"></a>
## 5. 两种肘部姿态与可达空间

![两种关节姿态到达同一个终点。](../../../assets/figures/two_link_elbow_solutions.svg)

*两种关节姿态到达同一个终点。*

**逆运动学 (inverse kinematics)** 从目标位置反求关节角。两根 100 mm 的连杆用 $(\theta_1,\theta_2)=(0^\circ,+90^\circ)$ 或 $(+90^\circ,-90^\circ)$ 都能到达 (100 mm, 100 mm)。第二关节角是相对角，而非世界中的绝对方向。

![理想可达圆环的半径从 50 mm 到 150 mm。](../../../assets/figures/two_link_workspace.svg)

*理想可达圆环的半径从 50 mm 到 150 mm。*

在关节可以自由旋转且没有碰撞的情况下，径向距离满足 $|L_1-L_2|\le r\le L_1+L_2$。对于 100 mm 与 50 mm 连杆，理想**可达空间 (reachable workspace)** 为内半径 50 mm、外半径 150 mm 的圆环。真实限位和障碍可能减小范围。

<a id="section-6"></a>
## 6. 带完整解答的练习

以下**六道练习都包含答案及推导过程**，不是针对某位读者的未解问题。

<a id="worked-1"></a>
### 6.1. 旋转坐标系中的局部点 P

**题目.** 工具 T 在世界 (100 mm, 50 mm)，旋转 +90°。求局部 P=(0 mm, 10 mm) 的世界坐标。

**解答.** 局部 +y 对应世界 −X，因此 X 减少 10 mm。

$$
x_w=100+0\cdot0-10\cdot1=90\ \mathrm{mm}
$$

$$
y_w=50+0\cdot1+10\cdot0=50\ \mathrm{mm}
$$

**答案:** (90 mm, 50 mm).

<a id="worked-2"></a>
### 6.2. 沿工具局部 x 轴的点 Q

**题目.** 仍使用相同 T，求 Q=(20 mm, 0 mm) 的世界坐标。

**解答.** 局部 +x 对应世界 +Y，因此只有 Y 增加 20 mm。

$$
x_w=100+20\cdot0-0\cdot1=100\ \mathrm{mm}
$$

$$
y_w=50+20\cdot1+0\cdot0=70\ \mathrm{mm}
$$

**答案:** (100 mm, 70 mm).

<a id="worked-3"></a>
### 6.3. 双连杆正向运动学

**题目.** L1=100 mm、L2=50 mm、θ1=30°、相对 θ2=60°，求工具位置。

**解答.** 第二连杆在世界中的绝对角为 30°+60°=90°。

$$
X=100\cos30^\circ+50\cos90^\circ=50\sqrt3\approx86.60\ \mathrm{mm}
$$

$$
Y=100\sin30^\circ+50\sin90^\circ=100\ \mathrm{mm}
$$

**答案:** (86.60 mm, 100 mm).

<a id="worked-4"></a>
### 6.4. 同一目标的两种逆运动学解

**题目.** 两根 100 mm 连杆到达 (100 mm, 100 mm)，给出两组关节角。

**解答.** 第一种先向右再向上；第二种先向上再向右。

$$
(\theta_1,\theta_2)=(0^\circ,+90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

$$
(\theta_1,\theta_2)=(+90^\circ,-90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

<a id="worked-5"></a>
### 6.5. 不求关节角的可达性检查

**题目.** L1=100 mm、L2=50 mm：检查 (0 mm, 120 mm) 和 (0 mm, 0 mm)。

**解答.** 径向距离必须在两连杆长度之差与之和之间。

$$
r_{\min}=|100-50|=50\ \mathrm{mm},\qquad r_{\max}=100+50=150\ \mathrm{mm}
$$

$$
r_{(0, 120)}=\sqrt{0^2+120^2}=120\ \mathrm{mm}
$$

(0 mm, 120 mm) **可以到达**，因为 50 ≤ 120 ≤ 150。原点 (0 mm, 0 mm) **不可到达**，因为距离为零。

<a id="worked-6"></a>
### 6.6. 肘关节相对角的余弦

**题目.** L1=100 mm、L2=50 mm、r=120 mm：求 cos θ2。

**解答.** 余弦只决定弯曲幅度；镜像肘部姿态的相对角符号相反。

$$
\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}
=\frac{14400-10000-2500}{10000}=\frac{1900}{10000}=0.19
$$

$$
\theta_2\approx\pm79.05^\circ
$$

三角形内角为 $\varphi=180^\circ-|\theta_2|$。单凭径向距离不能求出 $\theta_1$。参见示意图所在的 [三角函数](../TRIGONOMETRY.md).

<a id="section-7"></a>
## 7. 模型限制与矩阵表达

这里假设刚性二维连杆、理想编码器且没有碰撞。实际还存在关节限位、间隙、变形、编码器零位误差、相机标定和三维旋转。编码器测量关节角，而不是工具的世界坐标。传感器观测需经过坐标转换。示例不可用于控制真实设备。

**可选的齐次矩阵 3×3** 将旋转和平移作用于点的列向量 $[x_l,y_l,1]^T$。纯位移向量的最后一项为 0，因此不受平移影响。

$$
T_{WL}=
\begin{bmatrix}
\cos\theta & -\sin\theta & t_x \\
\sin\theta & \cos\theta & t_y \\
0 & 0 & 1
\end{bmatrix},
\qquad
\begin{bmatrix}x_w\\y_w\\1\end{bmatrix}
=T_{WL}\begin{bmatrix}x_l\\y_l\\1\end{bmatrix}
$$

[三角函数](../TRIGONOMETRY.md) · [数学符号](../SYMBOLS.md) · [反馈控制](03-feedback-control.md)

[下一章：旋转、速度与奇异位形](05-velocity-jacobian.md)
