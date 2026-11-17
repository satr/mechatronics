# Aide-mémoire des formules

**Lire cette page en:** [en](../en/CHEATSHEET.md) · [fr](CHEATSHEET.md) · [de](../de/CHEATSHEET.md) · [it](../it/CHEATSHEET.md) · [es](../es/CHEATSHEET.md) · [pt](../pt/CHEATSHEET.md) · [zh](../zh/CHEATSHEET.md) · [ja](../ja/CHEATSHEET.md) · [nb](../nb/CHEATSHEET.md) · [ru](../ru/CHEATSHEET.md) · [ko](../ko/CHEATSHEET.md) · [fi](../fi/CHEATSHEET.md) · [pl](../pl/CHEATSHEET.md)

**Unités utilisées ici (définies avant les exemples):** `s` — seconde; `m` — mètre; `m/s` — mètre / seconde — vitesse linéaire; `rad/s` — radian / seconde — vitesse angulaire; `kg·m²` — kilogramme · mètre² — moment d'inertie; `N·m` — newton · mètre — moment de force; `N·m·s/rad` — newton · mètre · seconde / radian — gain par unité de vitesse; `J` — joule; `mm` — millimètre = 0.001 m; `mm/s` — millimètre / seconde — vitesse linéaire; `%` — pour cent (un centième). [Glossaire des unités](UNITS.md).

[Sommaire](README.md) · [Mouvement, dérivées et intégrales](notes/01-motion-calculus.md) · [Dynamique du premier ordre et rotation](notes/02-first-order-dynamics.md) · [Exercices Python](exercises/README.md)

> **Avertissement :** Ces ressources pédagogiques assistées par IA peuvent contenir des erreurs, des traductions inexactes et des hypothèses incorrectes. Utilisation à vos risques et périls. Vérifiez les calculs indépendamment et n'utilisez aucun exemple pour piloter des machines réelles.

| Points essentiels | Aide-mémoire des formules |
| --- | --- |
| Déplacement | $\Delta x=x_2-x_1$ |
| Distance parcourue | $s=\int_{t_1}^{t_2}\lvert v(t)\rvert\ \mathrm{d}t\ge 0$ |
| Vitesse moyenne vectorielle | $\overline{v}=\frac{\Delta x}{\Delta t}$ |
| Vitesse scalaire moyenne | $\frac{s}{\Delta t}$ |
| Vitesse instantanée | $v(t)=\frac{dx}{dt}$ |
| Méthode d’Euler | $x_{n+1}=x_n+v_n\ dt$ |
| Dynamique du premier ordre | $\frac{dv}{dt}=\frac{u-v}{\tau}$ |
| Erreur de vitesse | $\varepsilon(t)=u-v(t)$ |
| Constante de temps | $t=\tau$: $1-\exp(-1)\approx63.2\ \%$ |
| Couple net | $M=J\alpha$ |
| Inertie et gain | $\tau=\frac{J}{K}$ (Modèle de couple idéalisé uniquement) |
| Énergie cinétique de rotation | $E=\frac{1}{2}J\omega^2$ |

**Notation :** $\varepsilon$ est l’erreur de vitesse (speed error) ; $\mathrm{e}\approx2.71828$ est le nombre d’Euler (Euler’s number) ; $\exp(z)=\mathrm{e}^{z}$.

**Unités (SI):**

| Symbole | Grandeur | Unité SI |
| --- | --- | --- |
| `t, dt, τ` | Temps | s (second) |
| `x` | Position | m (meter) |
| `v` | Vitesse | m/s (meter per second) |
| `ω` | Vitesse angulaire | rad/s (radian per second) |
| `J` | Moment d’inertie | kg·m² (kilogram square meter) |
| `M` | Couple | N·m (newton meter) |
| `K` | Gain couple/erreur | N·m·s/rad |
| `E` | Énergie | J (joule) |

Le point médian `·` indique une multiplication. La consigne $u$ désigne une vitesse linéaire ou angulaire selon le modèle.

## Précautions

Ne pas confondre vitesse scalaire et vitesse vectorielle, distance et déplacement, $dt$ et $\tau$. La formule $\tau=\frac{J}{K}$ n'est valable que pour le modèle de couple explicité ; l'énergie mécanique n'est pas la consommation électrique.

**Termes anglais :**

- distance parcourue (distance traveled)
- déplacement (displacement)
- vitesse scalaire (speed)
- vitesse vectorielle (velocity)
- dérivée (derivative)
- intégrale (integral)
- intégration numérique (numerical integration)
- méthode d’Euler explicite (explicit Euler method)

**Termes anglais :**

- système du premier ordre (first-order system)
- constante de temps (time constant)
- pas temporel (time step)
- moment d’inertie (moment of inertia)
- couple (torque)
- gain du régulateur (controller gain)
- accélération angulaire (angular acceleration)
- identification du système (system identification)
- énergie cinétique de rotation (rotational kinetic energy)

Pour approfondir, voir les [détails sur les dérivées](notes/01-motion-calculus.md#section-6) et les [limites du modèle](notes/02-first-order-dynamics.md#section-7).


[D’où viennent exactement ces pourcentages ? Voir le calcul.](notes/02-first-order-dynamics.md#time-constant-derivation)

[Calcul des valeurs 3 ; 3.8 et 3.98.](notes/01-motion-calculus.md#motion-values-derivation)


## Symboles et notation

**Σ / ∑ (sommation / summation)** indique la somme de plusieurs termes : $\sum_{n=1}^{3}n=1+2+3=6$. [Autres symboles](SYMBOLS.md).


## Table des intégrales

[0. Bases du calcul différentiel et intégral](notes/00-calculus-foundations.md) · [Table des intégrales](INTEGRAL_TABLE.md)

## Commande en boucle fermée : PID et couple de maintien

| $\varepsilon=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}}$ | $u_P=K_p\varepsilon$, $u_I=K_i\int\varepsilon\ \mathrm{d}t$ |
| --- | --- |
| $M_{\mathrm{motor}}=K_t I$ | $\lvert M_g\rvert=mgL\lvert\cos\theta\rvert$ |

[Commande en boucle fermée : PID et couple de maintien](notes/03-feedback-control.md) · [Table trigonométrique et exemples mécaniques](TRIGONOMETRY.md)

<a id="joint-velocity"></a>
## Rotation, vitesse et jacobien

Les vitesses angulaires sont en rad/s et les vitesses linéaires en mm/s lorsque les longueurs sont en mm.

$$
v_x=-L\sin Q\cdot\dot Q,\qquad v_y=L\cos Q\cdot\dot Q
$$

$$
\det J=L_1L_2\sin Q_2
$$

[Rotation, vitesse et jacobien](notes/05-velocity-jacobian.md)
