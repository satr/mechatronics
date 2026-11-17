# 4. Robot coordinate frames and planar kinematics

**Languages:** [en](04-coordinate-frames.md) · [fr](../../fr/notes/04-coordinate-frames.md) · [de](../../de/notes/04-coordinate-frames.md) · [it](../../it/notes/04-coordinate-frames.md) · [es](../../es/notes/04-coordinate-frames.md) · [pt](../../pt/notes/04-coordinate-frames.md) · [zh](../../zh/notes/04-coordinate-frames.md) · [ja](../../ja/notes/04-coordinate-frames.md) · [nb](../../nb/notes/04-coordinate-frames.md) · [ru](../../ru/notes/04-coordinate-frames.md) · [ko](../../ko/notes/04-coordinate-frames.md) · [fi](../../fi/notes/04-coordinate-frames.md) · [pl](../../pl/notes/04-coordinate-frames.md)

**Units used here (defined before the examples):** `mm` — millimetre = 0.001 m; `°` — degree. [Full unit reference](../UNITS.md).

[README](../README.md) · [Trigonometry](../TRIGONOMETRY.md) · [Mathematical symbols](../SYMBOLS.md) · [Feedback control](03-feedback-control.md)

> **Educational model:** Do not use this simplified geometry to control real machinery.

## Contents
1. [Why frames matter](#section-1)
2. [Rotating and translating a point](#section-2)
3. [Chaining reference frames](#section-3)
4. [Two-link forward kinematics](#section-4)
5. [Two elbow solutions and reachable workspace](#section-5)
6. [Worked examples with complete solutions](#section-6)
7. [Model limits and matrix notation](#section-7)

<a id="section-1"></a>
## 1. Why frames matter

A coordinate frame (coordinate frame) consists of an origin and directed axes. A **world frame** W can remain fixed to the robot base, while a **tool frame** T moves with the tool. Coordinates of the same point change with the chosen frame. **Position** specifies a point; **orientation** specifies axis directions. Converting coordinates does not in itself move a robot.

All lengths use the same unit (here mm). Positive angles are measured counterclockwise from world +X. Indices w and l mean world and local. The model is a rigid 2D approximation.

<a id="section-2"></a>
## 2. Rotating and translating a point

![World versus tool axes with +90° rotation; local points P and Q.](../../../assets/figures/world_local_frames.svg)

*World versus tool axes with +90° rotation; local points P and Q.*

The figure shows tool origin T at world (100 mm, 50 mm) with local axes rotated +90°. The local +x axis points along world +Y; local +y points along world −X. Thus P=(0 mm, 10 mm) in T is world (90 mm, 50 mm), while Q=(20 mm, 0 mm) in T is world (100 mm, 70 mm).

Let $(t_x,t_y)$ locate the local origin in world coordinates, $\theta$ describe its angle, and $(x_l,y_l)$ give point coordinates in that local frame. **Rotate first, then translate**:

$$
x_w=t_x+x_l\cos\theta-y_l\sin\theta
$$

$$
y_w=t_y+x_l\sin\theta+y_l\cos\theta
$$

The signs of $\sin\theta$ and $\cos\theta$ depend on the oriented angle. For $\theta=0^\circ$, these equations simply add the origin offset. They transform a point's coordinates, not motor commands.

<a id="section-3"></a>
## 3. Chaining reference frames

Frames form chains such as **W → T → S** (world → tool → sensor). Keep T as above. Let S have origin (20 mm, 0 mm) in T, with axes parallel to T. Its world origin is (100 mm, 70 mm). A point (0 mm, 10 mm) measured in S is at (90 mm, 70 mm) in W. Convert from child to parent frame in order.

For column vectors, $T_{WS}=T_{WT}T_{TS}$, where $T_{AB}$ transforms coordinates **from B into A**. Matrix multiplication is not generally commutative.

**Complete matrix calculation (column vectors):** The tool frame T has a +90° orientation and world translation (100 mm, 50 mm). The sensor frame S has no additional rotation and sits at local (20 mm, 0 mm) in T—the same location as Q in the preceding diagram. Thus the rotation entries are dimensionless and the translation entries are in mm:

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

The matrix product first rotates the sensor offset into world axes: local (20 mm, 0 mm) becomes world (0 mm, 20 mm), which is then added to (100 mm, 50 mm). The S point (0 mm, 10 mm) therefore becomes world (90 mm, 70 mm). Adding 20 mm directly to world X would give a wrong answer because the sensor offset is expressed **in T**, not W. The last coordinate 1 is a dimensionless homogeneous-coordinate convention, not a length. This is coordinate mathematics; [ROS 2 tf2](06-ros2-foundations.md#section-7) distributes and queries time-stamped transforms but does not itself solve inverse kinematics.

<a id="section-4"></a>
## 4. Two-link forward kinematics

![First joint 30°, second relative joint 60°; second link vertical.](../../../assets/figures/two_link_fk.svg)

*First joint 30°, second relative joint 60°; second link vertical.*

A planar arm has link lengths $L_1,L_2$. Joint angle $\theta_1$ is measured from world +X; $\theta_2$ is measured **relative to the first link**. Therefore the second link points at the absolute world angle $\theta_1+\theta_2$. The tip position is the vector sum:

$$
X=L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2)
$$

$$
Y=L_1\sin\theta_1+L_2\sin(\theta_1+\theta_2)
$$

For L1=100 mm, L2=50 mm, $\theta_1=30^\circ$, $\theta_2=60^\circ$, the elbow is at (86.60 mm, 50 mm). The second link points upward at absolute 90°, yielding tip (86.60 mm, 100 mm).

<a id="section-5"></a>
## 5. Two elbow solutions and reachable workspace

![Two different sets of joint angles reach the same target.](../../../assets/figures/two_link_elbow_solutions.svg)

*Two different sets of joint angles reach the same target.*

Inverse kinematics seeks angles for a target position. For two links of 100 mm each, both $(\theta_1,\theta_2)=(0^\circ,+90^\circ)$ and $(+90^\circ,-90^\circ)$ reach (100 mm, 100 mm). These are joint angles; $\theta_2$ is relative, not absolute.

![Ideal reachable annulus between 50 mm and 150 mm.](../../../assets/figures/two_link_workspace.svg)

*Ideal reachable annulus between 50 mm and 150 mm.*

For freely rotating 2D joints and no collisions, the radial distance $r$ must satisfy $|L_1-L_2|\le r\le L_1+L_2$. With lengths 100 mm and 50 mm, the ideal reachable workspace is an annulus between radii 50 mm and 150 mm. Joint limits and obstacles can further restrict real reachability.

<a id="section-6"></a>
## 6. Worked examples with complete solutions

These **six stand-alone examples all include the solution and explanation**. They are not personal questions addressed to any reader.

<a id="worked-1"></a>
### 6.1. Local point P in a rotated frame

**Problem.** T is at world (100 mm, 50 mm), rotated +90°. Find world coordinates of local P=(0 mm, 10 mm).

**Solution.** Local +y points world −X, so subtract 10 mm from X only.

$$
x_w=100+0\cdot0-10\cdot1=90\ \mathrm{mm}
$$

$$
y_w=50+0\cdot1+10\cdot0=50\ \mathrm{mm}
$$

**Answer:** (90 mm, 50 mm).

<a id="worked-2"></a>
### 6.2. Local point Q on tool x

**Problem.** Using the same tool frame, find world coordinates of Q=(20 mm, 0 mm).

**Solution.** Local +x points world +Y, so add 20 mm to Y only.

$$
x_w=100+20\cdot0-0\cdot1=100\ \mathrm{mm}
$$

$$
y_w=50+20\cdot1+0\cdot0=70\ \mathrm{mm}
$$

**Answer:** (100 mm, 70 mm).

<a id="worked-3"></a>
### 6.3. Two-link forward kinematics

**Problem.** L1=100 mm, L2=50 mm, θ1=30° and relative θ2=60°. Find the tip.

**Solution.** Second link world angle is 30°+60°=90°, not 60°.

$$
X=100\cos30^\circ+50\cos90^\circ=50\sqrt3\approx86.60\ \mathrm{mm}
$$

$$
Y=100\sin30^\circ+50\sin90^\circ=100\ \mathrm{mm}
$$

**Answer:** (86.60 mm, 100 mm).

<a id="worked-4"></a>
### 6.4. Two configurations for one target

**Problem.** Two 100 mm links reach (100 mm, 100 mm). Find two angle pairs.

**Solution.** One pose moves right then up; the other moves up then right.

$$
(\theta_1,\theta_2)=(0^\circ,+90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

$$
(\theta_1,\theta_2)=(+90^\circ,-90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

<a id="worked-5"></a>
### 6.5. Reachability without solving angles

**Problem.** L1=100 mm, L2=50 mm. Are (0 mm, 120 mm) and (0 mm, 0 mm) reachable?

**Solution.** Compare each distance to the difference and sum of the link lengths.

$$
r_{\min}=|100-50|=50\ \mathrm{mm},\qquad r_{\max}=100+50=150\ \mathrm{mm}
$$

$$
r_{(0, 120)}=\sqrt{0^2+120^2}=120\ \mathrm{mm}
$$

The point (0 mm, 120 mm) is **reachable** because 50 ≤ 120 ≤ 150. The origin (0 mm, 0 mm) is **not reachable** because its radius is zero.

<a id="worked-6"></a>
### 6.6. Cosine rule for the elbow angle

**Problem.** L1=100 mm, L2=50 mm and r=120 mm. Calculate cos θ2.

**Solution.** The cosine fixes the magnitude of the bend; two mirrored elbow poses give opposite relative-angle signs.

$$
\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}
=\frac{14400-10000-2500}{10000}=\frac{1900}{10000}=0.19
$$

$$
\theta_2\approx\pm79.05^\circ
$$

The interior triangle angle is $\varphi=180^\circ-|\theta_2|$. The radius alone does not determine $\theta_1$. See the diagram in [Trigonometry](../TRIGONOMETRY.md).

<a id="section-7"></a>
## 7. Model limits and matrix notation

This ideal rigid planar model excludes joint limits, collisions, backlash, flex, encoder zero offsets, camera calibration, and 3D motion. Joint encoders measure joint angles, not direct world coordinates. Always transform sensor observations through calibrated frames. None of these calculations is an instruction to move equipment.

Optional homogeneous-matrix form: with column vectors, the 3×3 transform maps the local point $[x_l,y_l,1]^T$ into the world frame. A free displacement vector has third coordinate 0 so translation does not apply.

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

[Trigonometry](../TRIGONOMETRY.md) · [Mathematical symbols](../SYMBOLS.md) · [Feedback control](03-feedback-control.md)

[Next: rotation, velocity and singularities](05-velocity-jacobian.md)
