# Trigonométrie : angles, sinus, cosinus, tangente et arctangente

**Langues:** [en](../en/TRIGONOMETRY.md) · [fr](TRIGONOMETRY.md) · [de](../de/TRIGONOMETRY.md) · [it](../it/TRIGONOMETRY.md) · [es](../es/TRIGONOMETRY.md) · [pt](../pt/TRIGONOMETRY.md) · [zh](../zh/TRIGONOMETRY.md) · [ja](../ja/TRIGONOMETRY.md) · [nb](../nb/TRIGONOMETRY.md) · [ru](../ru/TRIGONOMETRY.md) · [ko](../ko/TRIGONOMETRY.md) · [fi](../fi/TRIGONOMETRY.md) · [pl](../pl/TRIGONOMETRY.md)

**Unités utilisées ici (définies avant les exemples):** `°` — degré; `rad` — radian; `kg` — kilogramme; `m` — mètre; `m/s²` — mètre / seconde² — accélération; `N·m` — newton · mètre — moment de force; `mm` — millimètre = 0.001 m; `N` — newton. [Glossaire des unités](UNITS.md).

[README](README.md) · [Calculus](notes/00-calculus-foundations.md) · [Integral table](INTEGRAL_TABLE.md)

<a id="unit-circle-values"></a>
## Cercle unité : sinus et cosinus

Un point du cercle unité d’angle θ possède les coordonnées **(cos θ, sin θ)**. Les angles partent de +X dans le sens antihoraire. Le cosinus (cosine) est horizontal et le sinus (sine) vertical. Un seul dessin indique les 16 paires exactes, et un tableau unique donne les valeurs décimales, la tangente et l'arctangente principale.

![Un cercle unité présentant 16 angles et leurs couples exacts (cos θ, sin θ).](../../assets/figures/unit_circle_reference.svg)

*Un cercle unité présentant 16 angles et leurs couples exacts (cos θ, sin θ).*

**Fractions exactes et approximations décimales:**

| θ | cos θ (exact) | cos θ (décimal) | sin θ (exact) | sin θ (décimal) | tan θ (exact) | tan θ (décimal) | arctan(tan θ), principale |
| --- | --- | ---: | --- | ---: | --- | ---: | --- |
| 0° | $1$ | 1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 30° | $\frac{\sqrt3}{2}$ | 0.8660 | $\frac12$ | 0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 45° | $\frac{\sqrt2}{2}$ | 0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 60° | $\frac12$ | 0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 90° | $0$ | 0.0000 | $1$ | 1.0000 | **indéfini** | — | — |
| 120° | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 135° | $-\frac{\sqrt2}{2}$ | -0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 150° | $-\frac{\sqrt3}{2}$ | -0.8660 | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |
| 180° | $-1$ | -1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 210° | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 225° | $-\frac{\sqrt2}{2}$ | -0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 240° | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 270° | $0$ | 0.0000 | $-1$ | -1.0000 | **indéfini** | — | — |
| 300° | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 315° | $\frac{\sqrt2}{2}$ | 0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 330° | $\frac{\sqrt3}{2}$ | 0.8660 | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |

La tangente est **indéfinie** à 90° et 270°, car cos θ = 0; arctan(tan θ) l’est aussi. La dernière colonne donne la **valeur principale** entre −90° et 90°, parfois différente de l’angle de départ : arctan(tan 135°) = −45° et arctan(tan 225°) = 45°. Les nombres sont arrondis à quatre décimales. Les valeurs à 360° répètent celles de 0°.

<a id="trigonometric-identities"></a>
### Identités trigonométriques utiles

Un décalage de 90° échange sinus et cosinus, parfois en inversant le signe. Les parenthèses sont essentielles : cos(θ − 90°) prend le cosinus de la différence, et ne soustrait pas 90 au cosinus.

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

**Angles négatifs et périodicité:**

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

Signes par quadrant (cos, sin, tan) : I (+,+,+), II (−,+,−), III (−,−,+), IV (+,−,−). Un angle négatif tourne dans le sens horaire.

Pour résoudre un angle, vérifier son quadrant et l’intervalle principal de la fonction inverse.

<a id="inverse-cosine-reference"></a>
### Arccosinus et estimation d'un angle

Entre 0° et 180°, le cosinus décroît de 1 à −1. Ainsi arccos(0.19) est légèrement inférieur à 80° : cos 80°≈0.1736 et arccos(0.19)≈79.05°. Comme cos(+θ)=cos(−θ), deux configurations articulaires signées sont possibles. La valeur principale d'arccos est entre 0° et 180°.

![cos θ versus θ, with arccos(0.19) marked](../../assets/figures/arccos_reference_curve.svg)



## Schéma : côté opposé, adjacent et hypoténuse

![Trois triangles rectangles : sinus = côté opposé a sur hypoténuse c, cosinus = adjacent b sur c, tangente = a sur b.](../../assets/figures/trig_ratios.svg)

Dans le schéma, **a** est le côté opposé à l’angle θ, **b** le côté adjacent et **c** l’hypoténuse. Pour un angle aigu, $\sin\theta=a/c$, $\cos\theta=b/c$ et $\tan\theta=a/b$ (si $b\ne0$). Les **longueurs sont non négatives** : ce schéma ne montre pas à lui seul le signe des fonctions pour les angles négatifs ou d’autres quadrants. Pour un angle orienté depuis l’axe x positif, $\sin(+60^\circ)=+\sqrt3/2$ mais $\sin(-60^\circ)=-\sqrt3/2$.

## Mécanique : couple gravitationnel sur un bras

Pour une masse m à la distance L de l’axe, avec un bras incliné de θ au-dessus de l’horizontale, le **module** du couple vaut mgL|cos θ|. Le signe dépend du sens positif choisi.

$$
|M_g|=mgL|\cos\theta|.
$$

Avec m = 0.5 kg, L = 0.2 m, g = 9.81 m/s² et θ = 60°, le couple est de 0.4905 N·m en valeur absolue ; à 0° 0.981 N·m, à 90° zéro, dans ce modèle idéal.

## Exemple inverse : calculer un angle

Un outil monte de 0.05 m pour une course horizontale de 0.1 m. Le rapport est 0.5 ; θ = arctan(0.5) ≈ 26.565°. L’argument est un rapport, pas « 0.5 degré ».

$$
\tan\theta=\frac{0.05\ \mathrm{m}}{0.1\ \mathrm{m}}=0.5,\qquad \theta=\arctan(0.5)\approx26.565^\circ.
$$

Conversion : θ_rad = θ_deg·π/180. Les bibliothèques trigonométriques attendent généralement les radians.

$$
\theta_{\mathrm{rad}}=\theta_{\mathrm{deg}}\frac{\pi}{180}.
$$

### Direction d'un vecteur : pourquoi utiliser `atan2`

Pour un vecteur allant de l'origine à $(x,y)$, l'arctangente ordinaire ne voit que le rapport $y/x$. Les vecteurs $(1, -1)$ et $(-1, 1)$ ont le même rapport mais pointent dans des **quadrants différents**. Pour $x=-1\ \mathrm{mm}$ et $y=+1\ \mathrm{mm}$, ce rapport donne une mauvaise direction dans le repère monde :

$$
\arctan\left(\frac{y}{x}\right)=\arctan(-1)=-45^\circ,\qquad
\operatorname{atan2}(+1, -1)=+135^\circ.
$$

`atan2(y, x)` tient compte des signes des **deux composantes** et détermine la direction d'un vecteur non nul. Les arguments doivent avoir la même unité de longueur. Si $x=0$, le quotient $y/x$ n'existe pas, mais `atan2` indique encore l'axe quand $y\ne0$. Au point $(0, 0)$, aucune direction n'est définie ; $+180^\circ$ et $-180^\circ$ désignent la même direction. Ce choix importe pour les [angles des repères](notes/04-coordinate-frames.md).

## Loi des cosinus : géométrie à deux segments

![Two-link robot triangle OAB, exact link lengths and the law of cosines](../../assets/figures/two_link_cosine_law.svg)

La base O, le coude A et l'outil B forment un triangle : OA = L1, AB = L2 et OB = r, distance directe entre la base et l'outil. Le schéma utilise L1 = 100 mm, L2 = 50 mm, r = 120 mm. L'angle intérieur φ est différent de l'angle articulaire relatif θ2 : φ = 180° − |θ2|. Le schéma montre θ2 négatif ; sa réflexion montre θ2 positif.

La loi des cosinus est $r^2=L_1^2+L_2^2-2L_1L_2\cos\varphi$. Comme $\cos(180^\circ-|\theta_2|)=-\cos\theta_2$, on obtient $r^2=L_1^2+L_2^2+2L_1L_2\cos\theta_2$, soit $\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}$. Ici, $(14400-10000-2500)/10000=0.19$ et $|\theta_2|\approx79.05^\circ$. Il faut encore trouver θ1 pour atteindre un point (X,Y) précis.


[Calcul différentiel](notes/00-calculus-foundations.md) · [Commande avec rétroaction](notes/03-feedback-control.md)
