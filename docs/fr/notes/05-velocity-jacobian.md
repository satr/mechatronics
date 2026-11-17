# 5. Rotation, vitesse linéaire et singularités

**Languages:** [en](../../en/notes/05-velocity-jacobian.md) · [fr](05-velocity-jacobian.md) · [de](../../de/notes/05-velocity-jacobian.md) · [it](../../it/notes/05-velocity-jacobian.md) · [es](../../es/notes/05-velocity-jacobian.md) · [pt](../../pt/notes/05-velocity-jacobian.md) · [zh](../../zh/notes/05-velocity-jacobian.md) · [ja](../../ja/notes/05-velocity-jacobian.md) · [nb](../../nb/notes/05-velocity-jacobian.md) · [ru](../../ru/notes/05-velocity-jacobian.md) · [ko](../../ko/notes/05-velocity-jacobian.md) · [fi](../../fi/notes/05-velocity-jacobian.md) · [pl](../../pl/notes/05-velocity-jacobian.md)

**Unités utilisées ici (définies avant les exemples):** `mm` — millimètre = 0.001 m; `mm/s` — millimètre / seconde — vitesse linéaire; `rad` — radian; `rad/s` — radian / seconde — vitesse angulaire; `mm/rad` — millimètre / radian — coefficient du jacobien (longueur par angle); `°` — degré. [Glossaire des unités](../UNITS.md).

[README](../README.md) · [Trigonometry](../TRIGONOMETRY.md#unit-circle-values) · [Coordinate frames](04-coordinate-frames.md) · [Calculus foundations](00-calculus-foundations.md)

> Modèle idéal pour l'étude seulement; ne pas commander de matériel réel.

L'extrémité d'un bras tournant décrit un arc de cercle. Sa vitesse instantanée est tangentielle, perpendiculaire au bras. La géométrie précède ici la dérivation temporelle et la matrice jacobienne (Jacobian matrix) facultative.

## Sommaire

1. [De la rotation à la vitesse tangentielle](#section-1)
2. [Origine des dérivées](#section-2)
3. [Exemples de vitesse et de signe](#section-3)
4. [Deux bras : angles relatifs et absolus](#section-4)
5. [Configurations singulières pliée et étendue](#section-5)
6. [Trois déplacements près du pliage](#section-6)
7. [Complément : matrice jacobienne et exercices résolus](#section-7)

<a id="section-1"></a>
## 1. De la rotation à la vitesse tangentielle

Considérons un bras rigide de longueur $L$ tournant autour du pivot fixe $O$. Soit $\Delta Q$ la variation d'angle **en radians** pendant $\Delta t>0$. Si le sens de rotation ne change pas pendant cet intervalle, l'extrémité parcourt un arc de cercle. Sa **longueur d'arc** vaut exactement $\Delta s=L|\Delta Q|$. La **distance orientée le long de l'arc** est $L\Delta Q$ : son signe indique le sens de rotation. Il ne faut pas la confondre avec le déplacement rectiligne (la corde) entre les deux positions.

$$
\Delta s=L\lvert\Delta Q\rvert,\qquad
\Delta s_{\mathrm{signed}}=L\Delta Q
$$

La longueur d'arc divisée par le temps écoulé donne la **vitesse scalaire moyenne** sur cet intervalle :

$$
\overline{v}=\frac{\Delta s}{\Delta t}
=L\left\lvert\frac{\Delta Q}{\Delta t}\right\rvert
$$

Pour obtenir la **vitesse instantanée**, on prend la limite lorsque $\Delta t\to0$. La vitesse angulaire est $\omega=\dot Q=\mathrm{d}Q/\mathrm{d}t$, en rad/s; la norme de la vitesse linéaire vaut donc $v=L|\omega|$. Le vecteur vitesse est **tangent au cercle**, perpendiculaire au bras. Si $Q=45^\circ$ et que la rotation est antihoraire ($\omega>0$), l'extrémité part vers la gauche et vers le haut : composante horizontale négative et composante verticale positive.

$$
v=L\lvert\dot Q\rvert
$$

![Vitesse tangentielle et composantes signées à Q=45°.](../../../assets/figures/link_tangent_velocity.svg)

*Vitesse tangentielle et composantes signées à Q=45°.*

<a id="section-2"></a>
## 2. Origine des dérivées

Les coordonnées dépendent de Q, qui dépend lui-même du temps. La règle de chaîne (chain rule) multiplie la variation de position par radian par la variation d'angle par seconde.

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

La vitesse angulaire $\dot Q=\mathrm{d}Q/\mathrm{d}t$ s'exprime en rad/s, ce n'est pas l'angle lui-même. Si L est en mm, vx et vy sont en mm/s. Les dérivées trigonométriques exigent des radians.


$$
\omega=\dot{Q},\qquad \omega_1=\dot{Q}_1,\qquad \omega_2=\dot{Q}_2
$$

<a id="section-3"></a>
## 3. Exemples de vitesse et de signe

Avec L=150 mm, Q=45° et ω=+0.1 rad/s, les deux composantes ont même module et sont dirigées vers la gauche et le haut. Inverser ω inverse les signes. À Q=0°, vy=15 mm/s et vx=0.

$$
Q=45^\circ:\quad v_x=-150\frac{\sqrt2}{2}\cdot0.1\approx-10.61\ \mathrm{mm/s}
$$

$$
v_y=+150\frac{\sqrt2}{2}\cdot0.1\approx+10.61\ \mathrm{mm/s}
$$

$$
\sqrt{v_x^2+v_y^2}=L\lvert\dot Q\rvert=15\ \mathrm{mm/s}
$$

Le point sur $Q$ désigne sa **dérivée temporelle** $\dot Q$, et non une multiplication par l'angle. Passer de $\omega$ à $-\omega$ inverse les signes des deux composantes sans modifier la norme $L|\omega|$.

<a id="section-4"></a>
## 4. Deux bras : angles relatifs et absolus

Q1 est mesuré depuis +X et Q2 est l'angle relatif du coude. L'orientation absolue du deuxième bras est Q1+Q2; sa vitesse angulaire est ω₁+ω₂.

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

Les deux articulations contribuent à la vitesse de l'extrémité : le premier bras contient le facteur $\dot Q_1$, le second le facteur $\dot Q_1+\dot Q_2$. Utiliser seulement $\dot Q_2$ pour le second bras serait incorrect, car son angle est défini relativement au premier.

<a id="section-5"></a>
## 5. Configurations singulières pliée et étendue

Pour L1=100 mm et L2=50 mm, la portée idéale est de 50 à 150 mm. Les positions alignées, pliée (Q2=180°) et étendue (Q2=0°), sont singulières : la vitesse radiale instantanée y est nulle pour des vitesses articulaires finies.

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

Cette formule de dérivation suppose $r>0$. Si les deux bras ont la même longueur ($L_1=L_2$), leur repli complet sur la base ($Q_2=180^\circ$) donne $r=0$ : la formule ferait intervenir une division par zéro. À cette position, la distance radiale n'est pas dérivable par rapport à l'écart **signé** de l'angle du coude. Ce cas particulier ne concerne pas les longueurs inégales $L_1=100$ mm et $L_2=50$ mm utilisées ici.

Les limites articulaires et les collisions peuvent encore réduire l'espace de travail réel. Atteindre une position ne garantit ni l'orientation de l'outil ni un dégagement suffisant devant les obstacles.

<a id="section-6"></a>
## 6. Trois déplacements près du pliage

Avec le premier bras fixe, δ est le petit écart (en radians) depuis la position pliée. Distinguer le déplacement le long de l'axe fixe du premier bras, le déplacement transverse et le changement de rayon.

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

L'identité 1−cosδ=2sin²(δ/2) et sin(δ/2)≈δ/2 donnent le carré et le facteur 1/2. Ici le changement radial ≈50δ² mm, mais la projection longitudinale ≈25δ² mm.

Ces approximations ne valent que pour de petits $\delta$ exprimés en radians. Si $\delta$ est divisé par deux, les deux variations quadratiques (axiale et radiale) sont environ **divisées par quatre**, alors que le déplacement transversal n'est que **divisé par deux**. Imposer une vitesse radiale non nulle constante quand $\delta\to0$ exigerait une vitesse articulaire sans borne dans le modèle inverse idéal; un bras réel peut toutefois commencer à se déplier à vitesse angulaire finie, avec une vitesse radiale initialement nulle puis croissante.

$$
1-\cos(\delta)=2\sin^2\left(\frac{\delta}{2}\right)
\approx2\left(\frac{\delta}{2}\right)^2=\frac{\delta^2}{2}
$$

![Déplacements axial, transversal et radial près du pliage.](../../../assets/figures/folded_displacement_curves.svg)

*Déplacements axial, transversal et radial près du pliage.*

Pour maintenir une vitesse radiale non nulle près du pliage, la vitesse angulaire requise augmente fortement lorsque δ→0. Exactement au pliage, aucune vitesse articulaire finie ne peut produire instantanément une vitesse radiale non nulle.

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

![Vitesse requise du coude près d'une singularité.](../../../assets/figures/folded_radial_speed.svg)

*Vitesse requise du coude près d'une singularité.*

<a id="section-7"></a>
## 7. Complément : matrice jacobienne et exercices résolus

La matrice jacobienne (Jacobian matrix) relie les vitesses articulaires à la vitesse cartésienne. Son déterminant est L1L2 sin Q2 et s'annule lorsque les bras sont colinéaires. Ce modèle ignore butées et collisions.

$$
v_x=J_{11}\cdot\omega_1+J_{12}\cdot\omega_2
$$

$$
v_y=J_{21}\cdot\omega_1+J_{22}\cdot\omega_2
$$

| Coefficient | Géométrie de la transformation des vitesses |
| --- | --- |
| $J_{11}$ | $-L_1\sin(Q_1)-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{12}$ | $-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{21}$ | $L_1\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)$ |
| $J_{22}$ | $L_2\cdot\cos(Q_1+Q_2)$ |



**Dérivation du déterminant.** Chaque coefficient est une dérivée partielle de X ou Y, coordonnées de l'outil, par rapport à Q1 ou Q2 en radians. Pour des longueurs en mm, son unité est mm/rad ; le produit par rad/s donne des mm/s.

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

Le développement des deux produits du déterminant annule les termes contenant L2 au carré. L'identité de la différence des sinus élimine alors Q1.

$$
\det J=L_1L_2\sin(Q_2)
$$

![Les deux contributions des articulations s'additionnent comme des vecteurs pour donner la vitesse de l'outil.](../../../assets/figures/two_link_jacobian_velocity.svg)

*Les deux contributions des articulations s'additionnent comme des vecteurs pour donner la vitesse de l'outil.*

### Exemples entièrement résolus

1. Un bras de $L=150$ mm pointe vers la droite pour $Q=0^\circ$. Avec $\omega=+0.1$ rad/s, $\sin0^\circ=0$ et $\cos0^\circ=1$ : $v_x=-150\cdot0\cdot0.1=0$ et $v_y=150\cdot1\cdot0.1=+15$ mm/s. L'extrémité monte.
2. Pour $Q=45^\circ$ et $\omega=-0.1$ rad/s, on inverse la rotation : $v_x=-150\sin45^\circ\cdot(-0.1)\approx+10.61$ mm/s et $v_y=150\cos45^\circ\cdot(-0.1)\approx-10.61$ mm/s. L'extrémité va vers la droite et le bas, sans changer de rapidité $L|\omega|=15$ mm/s.
3. Pour $L_1=100$ mm, $L_2=50$ mm, $Q_1=30^\circ$, $Q_2=60^\circ$, $\omega_1=0.1$ rad/s et $\omega_2=0.2$ rad/s, le deuxième bras a pour orientation absolue $Q_1+Q_2=90^\circ$ et pour vitesse angulaire $\omega_1+\omega_2=0.3$ rad/s. D'où $v_x=-100\sin30^\circ\cdot0.1-50\sin90^\circ\cdot0.3=-5-15=-20$ mm/s et $v_y=100\cos30^\circ\cdot0.1+50\cos90^\circ\cdot0.3\approx+8.66$ mm/s.
4. Près du repli, avec $\delta=0.02$ rad, la variation axiale selon l'axe **fixe** est environ $25\delta^2=25\cdot0.02^2=0.010$ mm. Le déplacement transversal vaut environ $50\delta=1.000$ mm, tandis que l'augmentation radiale vaut $50\delta^2=0.020$ mm. Les coefficients des deux termes quadratiques sont différents.

[Trigonometry](../TRIGONOMETRY.md) · [Coordinate frames](04-coordinate-frames.md) · [Calculus foundations](00-calculus-foundations.md)
