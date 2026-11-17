# Trigonometry: angles, sine, cosine, tangent and arctangent

**Languages:** [en](TRIGONOMETRY.md) · [fr](../fr/TRIGONOMETRY.md) · [de](../de/TRIGONOMETRY.md) · [it](../it/TRIGONOMETRY.md) · [es](../es/TRIGONOMETRY.md) · [pt](../pt/TRIGONOMETRY.md) · [zh](../zh/TRIGONOMETRY.md) · [ja](../ja/TRIGONOMETRY.md) · [nb](../nb/TRIGONOMETRY.md) · [ru](../ru/TRIGONOMETRY.md) · [ko](../ko/TRIGONOMETRY.md) · [fi](../fi/TRIGONOMETRY.md) · [pl](../pl/TRIGONOMETRY.md)

**Units used here (defined before the examples):** `°` — degree; `rad` — radian; `kg` — kilogram; `m` — metre; `m/s²` — metre / second² — acceleration; `N·m` — newton · metre — torque; `mm` — millimetre = 0.001 m; `N` — newton. [Full unit reference](UNITS.md).

[README](README.md) · [Calculus](notes/00-calculus-foundations.md) · [Integral table](INTEGRAL_TABLE.md)

<a id="unit-circle-values"></a>
## Unit circle: sine and cosine

On the unit circle a point at angle θ has coordinates **(cos θ, sin θ)**. Angles start at +X and increase counterclockwise; horizontal components are cosine and vertical components are sine. The diagram shows exact signed pairs for all 16 angles, and the single table adds decimal approximations, tangent and principal arctangent values.

![Single unit circle with all 16 common angles and signed coordinate pairs (cos θ, sin θ).](../../assets/figures/unit_circle_reference.svg)

*Single unit circle with all 16 common angles and signed coordinate pairs (cos θ, sin θ).*

**Exact fractions and decimal approximations:**

| θ | cos θ (exact) | cos θ (decimal) | sin θ (exact) | sin θ (decimal) | tan θ (exact) | tan θ (decimal) | arctan(tan θ), principal |
| --- | --- | ---: | --- | ---: | --- | ---: | --- |
| 0° | $1$ | 1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 30° | $\frac{\sqrt3}{2}$ | 0.8660 | $\frac12$ | 0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 45° | $\frac{\sqrt2}{2}$ | 0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 60° | $\frac12$ | 0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 90° | $0$ | 0.0000 | $1$ | 1.0000 | **undefined** | — | — |
| 120° | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 135° | $-\frac{\sqrt2}{2}$ | -0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 150° | $-\frac{\sqrt3}{2}$ | -0.8660 | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |
| 180° | $-1$ | -1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 210° | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 225° | $-\frac{\sqrt2}{2}$ | -0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 240° | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 270° | $0$ | 0.0000 | $-1$ | -1.0000 | **undefined** | — | — |
| 300° | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 315° | $\frac{\sqrt2}{2}$ | 0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 330° | $\frac{\sqrt3}{2}$ | 0.8660 | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |

Tangent is **undefined** at 90° and 270° because cos θ = 0. Its inverse arctangent is therefore also undefined there. The last column is the **principal value** in the interval (−90°, 90°), not necessarily the original angle: for example, arctan(tan 135°) = −45° and arctan(tan 225°) = 45°. Decimal approximations are rounded to four places. At θ = 360° sine and cosine repeat their 0° values.

<a id="trigonometric-identities"></a>
### Useful angle identities

A 90° shift exchanges sine and cosine, sometimes changing the sign. Parentheses are essential: cos(θ − 90°) means take the cosine *after subtracting the angle*, not cos θ minus 90.

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

**Negative angles and periodicity:**

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

Signs by quadrant: I (+,+,+); II (−,+,−); III (−,−,+); IV (+,−,−), ordered as (cos, sin, tan). A negative angle is measured clockwise.

To estimate inverse angles, use the unit-circle signs and the monotonic part of the appropriate function.

<a id="inverse-cosine-reference"></a>
### Inverse cosine and angle estimates

On 0°–180°, cos θ decreases from 1 to −1. Thus arccos(0.19) is just below 80°: cos 80°≈0.1736 and arccos(0.19)≈79.05°. Cosine is even, so cos(+79.05°)=cos(−79.05°); two signed elbow configurations may be possible, although the principal arccos output is in 0°–180°. The diagram below plots the decreasing cosine.

![cos θ versus θ, with arccos(0.19) marked](../../assets/figures/arccos_reference_curve.svg)



## Visual guide: opposite, adjacent and hypotenuse

![Three right-triangle diagrams: sine compares opposite a to hypotenuse c; cosine compares adjacent b to c; tangent compares a to b.](../../assets/figures/trig_ratios.svg)

In the diagram, **a** is the opposite side (opposite the marked angle θ), **b** is the adjacent side, and **c** is the hypotenuse. For an acute angle θ in a right triangle, $\sin\theta=a/c$, $\cos\theta=b/c$, $\tan\theta=a/b$ (only for $b\ne0$). **Side lengths are nonnegative**; the diagram alone does not show the signs of sine and cosine for negative angles or other quadrants. With a directed angle measured from the positive x-axis, $\sin(+60^\circ)=+\sqrt3/2$ while $\sin(-60^\circ)=-\sqrt3/2$.

## Mechanical example: gravity acting on a lever

For a mass m at distance L from a pivot, with the lever at angle θ above the horizontal, the **magnitude** of gravity torque is mgL|cos θ|. The sign of the actual torque follows the rotation convention.

$$
|M_g|=mgL|\cos\theta|.
$$

With m = 0.5 kg, L = 0.2 m, g = 9.81 m/s², at θ = 60° the torque magnitude is 0.4905 N·m. It is 0.981 N·m at 0° and zero at 90° for this ideal point-load model.

## Inverse example: finding an angle from geometry

If a tool axis climbs 0.05 m over a horizontal run of 0.1 m, its slope ratio is 0.5. Therefore θ = arctan(0.5) ≈ 26.565°. Input is a ratio, not “0.5 degrees”.

$$
\tan\theta=\frac{0.05\ \mathrm{m}}{0.1\ \mathrm{m}}=0.5,\qquad \theta=\arctan(0.5)\approx26.565^\circ.
$$

Angle to radians: θ_rad = θ_deg·π/180. Numerical trig libraries usually expect radians.

$$
\theta_{\mathrm{rad}}=\theta_{\mathrm{deg}}\frac{\pi}{180}.
$$

### Inverse direction of a vector: why `atan2` matters

For a vector from the origin to $(x,y)$, the ordinary inverse tangent sees only the ratio $y/x$. The vectors $(1, -1)$ and $(-1, 1)$ have the same ratio, but point in **different quadrants**. For $x=-1\ \mathrm{mm}$ and $y=+1\ \mathrm{mm}$, using the ratio alone gives the wrong world direction:

$$
\arctan\left(\frac{y}{x}\right)=\arctan(-1)=-45^\circ,\qquad
\operatorname{atan2}(+1, -1)=+135^\circ.
$$

Use `atan2(y, x)` for the direction of a nonzero 2D vector, since it uses the signs of **both components**. Its arguments must use the same length unit. For $x=0$, the ratio $y/x$ is undefined while `atan2` still gives an axis direction when $y\ne0$. At $(0, 0)$ no direction is defined; angle branches such as $+180^\circ$ and $-180^\circ$ describe the same direction. This distinction matters when converting a measured displacement into a [coordinate-frame angle](notes/04-coordinate-frames.md).

## Law of cosines: two-link geometry

![Two-link robot triangle OAB, exact link lengths and the law of cosines](../../assets/figures/two_link_cosine_law.svg)

Base O, elbow A, and tool B form a triangle: OA = L1, AB = L2, and OB = r (the direct base-to-tool distance). The diagram uses L1 = 100 mm, L2 = 50 mm, r = 120 mm. The internal triangle angle φ differs from the relative elbow joint angle θ2: φ = 180° − |θ2|. The drawing shows negative θ2; its mirror image has positive θ2.

The cosine rule (law of cosines) is $r^2=L_1^2+L_2^2-2L_1L_2\cos\varphi$. Since $\cos(180^\circ-|\theta_2|)=-\cos\theta_2$, this is equivalent to $r^2=L_1^2+L_2^2+2L_1L_2\cos\theta_2$. Therefore, $\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}$. In this example, $(14400-10000-2500)/10000=0.19$, and $|\theta_2|\approx79.05^\circ$. The first joint angle θ1 still needs to be found to reach a specified (X,Y).


[Calculus](notes/00-calculus-foundations.md) · [Feedback control](notes/03-feedback-control.md)
