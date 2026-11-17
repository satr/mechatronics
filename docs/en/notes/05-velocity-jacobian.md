# 5. Rotation, linear velocity, and singularities

**Languages:** [en](05-velocity-jacobian.md) · [fr](../../fr/notes/05-velocity-jacobian.md) · [de](../../de/notes/05-velocity-jacobian.md) · [it](../../it/notes/05-velocity-jacobian.md) · [es](../../es/notes/05-velocity-jacobian.md) · [pt](../../pt/notes/05-velocity-jacobian.md) · [zh](../../zh/notes/05-velocity-jacobian.md) · [ja](../../ja/notes/05-velocity-jacobian.md) · [nb](../../nb/notes/05-velocity-jacobian.md) · [ru](../../ru/notes/05-velocity-jacobian.md) · [ko](../../ko/notes/05-velocity-jacobian.md) · [fi](../../fi/notes/05-velocity-jacobian.md) · [pl](../../pl/notes/05-velocity-jacobian.md)

**Units used here (defined before the examples):** `mm` — millimetre = 0.001 m; `mm/s` — millimetre / second — linear speed; `rad` — radian; `rad/s` — radian / second — angular speed; `mm/rad` — millimetre / radian — Jacobian coefficient (length per angle); `°` — degree. [Full unit reference](../UNITS.md).

[README](../README.md) · [Trigonometry](../TRIGONOMETRY.md#unit-circle-values) · [Coordinate frames](04-coordinate-frames.md) · [Calculus foundations](00-calculus-foundations.md)

> Ideal synthetic model only. Do not use for controlling real equipment.

A rotating arm end follows a circular arc. Its instantaneous velocity is tangent to that arc, not along the arm. This lesson builds from geometry to time derivatives and only then to the optional Jacobian matrix. Joint angles use radians in derivatives; examples also show degrees to aid visualization.

## Contents

1. [From a rotating arm to tangential speed](#section-1)
2. [Where the derivatives come from](#section-2)
3. [Worked speed and sign examples](#section-3)
4. [Two rotating links: relative and absolute angles](#section-4)
5. [Folded and straight singular configurations](#section-5)
6. [Three different displacements near folding](#section-6)
7. [Optional Jacobian and fully solved checks](#section-7)

<a id="section-1"></a>
## 1. From a rotating arm to tangential speed

For a rigid link of length $L$ rotating about a fixed pivot $O$, let $\Delta Q$ denote the change of angle **in radians** over a time interval $\Delta t>0$. During a rotation increment without reversal, the tip follows a circular arc. Its **arc length** is exactly $\Delta s=L|\Delta Q|$. The **signed distance along the oriented arc** is $L\Delta Q$: the sign tells us the direction of rotation. Neither quantity should be confused with the straight-line displacement (chord) between the two tip positions.

$$
\Delta s=L\lvert\Delta Q\rvert,\qquad
\Delta s_{\mathrm{signed}}=L\Delta Q
$$

Divide the arc length by the elapsed time to obtain the **average speed** for this interval:

$$
\overline{v}=\frac{\Delta s}{\Delta t}
=L\left\lvert\frac{\Delta Q}{\Delta t}\right\rvert
$$

For **instantaneous speed**, take the limit as $\Delta t\to0$. Since $\omega=\dot Q=\mathrm{d}Q/\mathrm{d}t$ is angular velocity in rad/s, the speed magnitude is $v=L|\omega|$. Its velocity **direction** is tangent to the circle and perpendicular to the link. For counterclockwise rotation ($\omega>0$), at $Q=45^\circ$ the tip moves up and left: the horizontal component is negative and the vertical component positive.

$$
v=L\lvert\dot Q\rvert
$$

![Rigid link and tip velocity tangent: Q=45°, counterclockwise rotation, component signs shown.](../../../assets/figures/link_tangent_velocity.svg)

*Rigid link and tip velocity tangent: Q=45°, counterclockwise rotation, component signs shown.*

<a id="section-2"></a>
## 2. Where the derivatives come from

The tip coordinates are functions of the angle; the angle is itself a function of time. These are TWO different dependencies. The chain rule multiplies the change of a coordinate per radian by the radians turned per second. Differentiate sine and cosine with angles measured in radians:

$$
x(t)=L\cdot\cos\bigl(Q(t)\bigr),\qquad y(t)=L\cdot\sin\bigl(Q(t)\bigr)
$$

$$
v_x=\frac{\mathrm{d}x}{\mathrm{d}t}
=\frac{\mathrm{d}x}{\mathrm{d}Q}\cdot\frac{\mathrm{d}Q}{\mathrm{d}t}
=-L\cdot\sin(Q)\cdot\dot{Q}
$$

$$
v_y=\frac{\mathrm{d}y}{\mathrm{d}t}
=\frac{\mathrm{d}y}{\mathrm{d}Q}\cdot\frac{\mathrm{d}Q}{\mathrm{d}t}
=L\cdot\cos(Q)\cdot\dot{Q}
$$

Angular velocity is $\dot Q=\mathrm{d}Q/\mathrm{d}t$ in rad/s, not the angle itself. When L is in mm, vx and vy are in mm/s; trigonometric derivatives use radians.


$$
\omega=\dot{Q},\qquad \omega_1=\dot{Q}_1,\qquad \omega_2=\dot{Q}_2
$$

<a id="section-3"></a>
## 3. Worked speed and sign examples

At Q=45°, L=150 mm and ω=+0.1 rad/s, the tip moves left and up at equal component speeds. Reversing rotation to −0.1 rad/s reverses both signs but not the speed magnitude. At Q=0° the horizontal speed is zero and the vertical velocity is +15 mm/s. The dot is a time derivative, not multiplication by the angle.

$$
Q=45^\circ:\quad v_x=-150\frac{\sqrt2}{2}\cdot0.1\approx-10.61\ \mathrm{mm/s}
$$

$$
v_y=+150\frac{\sqrt2}{2}\cdot0.1\approx+10.61\ \mathrm{mm/s}
$$

$$
\sqrt{v_x^2+v_y^2}=L\lvert\dot Q\rvert=15\ \mathrm{mm/s}
$$

<a id="section-4"></a>
## 4. Two rotating links: relative and absolute angles

A planar two-link arm has world angle Q1 for link 1 and a RELATIVE joint angle Q2 for link 2. Thus the world orientation of link 2 is Q1+Q2, whose angular speed is ω₁+ω₂. Differentiating the forward-kinematics coordinates produces both joints' contributions:

$$
X=L_1\cdot\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)
$$

$$
Y=L_1\cdot\sin(Q_1)+L_2\cdot\sin(Q_1+Q_2)
$$

$$
v_x=-L_1\cdot\sin(Q_1)\cdot\dot{Q}_1
-L_2\cdot\sin(Q_1+Q_2)\cdot(\dot{Q}_1+\dot{Q}_2)
$$

$$
v_y=L_1\cdot\cos(Q_1)\cdot\dot{Q}_1
+L_2\cdot\cos(Q_1+Q_2)\cdot(\dot{Q}_1+\dot{Q}_2)
$$

<a id="section-5"></a>
## 5. Folded and straight singular configurations

For ideal unrestricted links of L1=100 mm and L2=50 mm, r ranges from 50 mm (completely folded Q2=±180°) to 150 mm (completely extended Q2=0°). In both collinear configurations, the instantaneous joint-generated velocities are transverse to the link line: arbitrary radial velocity cannot be produced at that exact pose using finite joint speeds. Joint limits and physical collisions can reduce the real workspace. Position reachability alone does not guarantee tool orientation or clearance.

$$
r^2=L_1^2+L_2^2+2L_1L_2\cos(Q_2)
$$

$$
\lvert L_1-L_2\rvert\le r\le L_1+L_2
$$

$$
\frac{\mathrm{d}r}{\mathrm{d}Q_2}
=-\frac{L_1L_2\sin(Q_2)}{r}
$$

The derivative formula assumes $r>0$. For equal-length links folded exactly onto the base ($L_1=L_2$, $Q_2=180^\circ$), $r=0$ and the expression divides by zero; radial distance is not differentiable there as a function of the signed elbow-angle offset. This does not affect the unequal-link examples below.

<a id="section-6"></a>
## 6. Three different displacements near folding

Fix link 1 horizontally and consider link 2 initially pointing backward. Let δ≥0 be its small departure from the folded position in radians. The longitudinal displacement along the FIXED axis of link 1 is not the same as the change of base-to-tip radius. The exact formulas are:

$$
\Delta x_{\mathrm{axis}}=L_2\bigl(1-\cos(\delta)\bigr)
\approx\frac{L_2\delta^2}{2}
$$

$$
\Delta y_{\mathrm{perp}}=L_2\cdot\sin(\delta)\approx L_2\delta
$$

$$
\Delta r=\sqrt{(L_1-L_2)^2+2L_1L_2\bigl(1-\cos(\delta)\bigr)}-(L_1-L_2)
$$

$$
L_1>L_2>0:\qquad
\Delta r\approx\frac{L_1L_2}{2(L_1-L_2)}\delta^2
$$

The square and the factor 1/2 arise from 1−cosδ=2sin²(δ/2) and sin(δ/2)≈δ/2. For these unequal links, radial change has a different coefficient: Δr≈50δ² mm, whereas fixed-axis longitudinal change is ≈25δ² mm. Halving δ quarters either quadratic change but halves the transverse displacement. These approximations apply only at small δ.

$$
1-\cos(\delta)=2\sin^2\left(\frac{\delta}{2}\right)
\approx2\left(\frac{\delta}{2}\right)^2=\frac{\delta^2}{2}
$$

![Three displacements as the folded arm opens; angles plotted in degrees, approximations calculated in radians.](../../../assets/figures/folded_displacement_curves.svg)

*Three displacements as the folded arm opens; angles plotted in degrees, approximations calculated in radians.*

To demand a fixed, nonzero outward radial speed vr near the folded boundary, the elbow's angular speed must grow as δ tends to zero. At δ=0 the first-order radial speed is zero with any finite joint rates. The ideal inverse-velocity demand diverges; a real robot can unfold at a finite angular speed, starting with zero radial speed and increasing it gradually.

$$
\left.\frac{\mathrm{d}r}{\mathrm{d}\delta}\right|_{L_1=100,L_2=50}
=\frac{5000\sin(\delta)}{r}
\approx100\delta\ \mathrm{mm/rad}
$$

$$
v_r\approx(100\delta)\dot\delta\ \mathrm{mm/s},
\qquad
\dot\delta\approx\frac{1\ \mathrm{mm/s}}{100\ \mathrm{mm/rad}\cdot\delta}
$$

![Angular elbow speed required to sustain 1 mm/s radial speed, showing the singular boundary.](../../../assets/figures/folded_radial_speed.svg)

*Angular elbow speed required to sustain 1 mm/s radial speed, showing the singular boundary.*

<a id="section-7"></a>
## 7. Optional Jacobian and fully solved checks

A Jacobian matrix collects the derivatives of tool coordinates with respect to joint angles. It maps instantaneous joint speeds into tool velocity, not joint positions into absolute coordinates. In this ideal planar model the determinant vanishes exactly when sin Q2=0: straight and folded configurations. Near those positions the inverse velocity mapping becomes ill-conditioned. Use this mathematical model only for learning; actual systems also have joint limits, tool offsets, backlash, compliance and collisions.

$$
v_x=J_{11}\cdot\omega_1+J_{12}\cdot\omega_2
$$

$$
v_y=J_{21}\cdot\omega_1+J_{22}\cdot\omega_2
$$

| Coefficient | Geometry of the velocity mapping |
| --- | --- |
| $J_{11}$ | $-L_1\sin(Q_1)-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{12}$ | $-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{21}$ | $L_1\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)$ |
| $J_{22}$ | $L_2\cdot\cos(Q_1+Q_2)$ |



**Deriving the determinant.** Each Jacobian entry is a partial derivative of the tool coordinate X or Y with respect to a joint angle Q1 or Q2 in radians. With lengths in mm, its units are mm/rad; multiplying by rad/s gives mm/s.

$$
J_{11}=\frac{\partial X}{\partial Q_1},\qquad
J_{12}=\frac{\partial X}{\partial Q_2}
$$

$$
J_{21}=\frac{\partial Y}{\partial Q_1},\qquad
J_{22}=\frac{\partial Y}{\partial Q_2}
$$

$$
\det J=J_{11}J_{22}-J_{12}J_{21}
$$

$$
\det J=L_1L_2\bigl[\sin(Q_1+Q_2)\cos(Q_1)
-\sin(Q_1)\cos(Q_1+Q_2)\bigr]
$$

$$
\det J=L_1L_2\sin\bigl((Q_1+Q_2)-Q_1\bigr)
$$

Expanding the two determinant products cancels the terms with L2 squared. The sine-difference identity then eliminates Q1.

$$
\det J=L_1L_2\sin(Q_2)
$$

![The two joint-rate contributions add as vectors to give the tool velocity.](../../../assets/figures/two_link_jacobian_velocity.svg)

*The two joint-rate contributions add as vectors to give the tool velocity.*

### Complete worked checks

1. One rigid 150 mm link points right (Q=0°). For ω=+0.1 rad/s: vx=0, vy=150·0.1=+15 mm/s. The velocity points up.
2. At Q=45° with ω=−0.1 rad/s (clockwise): vx=−150·sin45°·(−0.1)=+10.61 mm/s, vy=150·cos45°·(−0.1)=−10.61 mm/s. The tip moves down and right; speed magnitude remains 15 mm/s.
3. For L1=100 mm, L2=50 mm, Q1=30°, Q2=60°, ω₁=0.1 rad/s and ω₂=0.2 rad/s, the second-link absolute angular speed is 0.3 rad/s. Therefore vx=−100·sin30°·0.1−50·sin90°·0.3=−20 mm/s; vy=100·cos30°·0.1+50·cos90°·0.3≈+8.66 mm/s.
4. At δ=0.02 rad from the folded position, fixed-axis longitudinal change is ≈25·0.02²=0.010 mm; transverse displacement is ≈50·0.02=1.000 mm; base-to-tip radial increase is ≈50·0.02²=0.020 mm. Do not confuse the two quadratic coefficients.

[Trigonometry](../TRIGONOMETRY.md) · [Coordinate frames](04-coordinate-frames.md) · [Calculus foundations](00-calculus-foundations.md)
