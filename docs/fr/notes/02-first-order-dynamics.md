# 2. Dynamique du premier ordre et rotation


**Lire cette page en:** [en](../../en/notes/02-first-order-dynamics.md) · [fr](02-first-order-dynamics.md) · [de](../../de/notes/02-first-order-dynamics.md) · [it](../../it/notes/02-first-order-dynamics.md) · [es](../../es/notes/02-first-order-dynamics.md) · [pt](../../pt/notes/02-first-order-dynamics.md) · [zh](../../zh/notes/02-first-order-dynamics.md) · [ja](../../ja/notes/02-first-order-dynamics.md) · [nb](../../nb/notes/02-first-order-dynamics.md) · [ru](../../ru/notes/02-first-order-dynamics.md) · [ko](../../ko/notes/02-first-order-dynamics.md) · [fi](../../fi/notes/02-first-order-dynamics.md) · [pl](../../pl/notes/02-first-order-dynamics.md)

**Unités utilisées ici (définies avant les exemples):** `s` — seconde; `mm/s` — millimètre / seconde — vitesse linéaire; `kg` — kilogramme; `m` — mètre; `rad/s` — radian / seconde — vitesse angulaire; `N` — newton; `N·m` — newton · mètre — moment de force; `J` — joule; `rpm` — tour par minute; `kg·m²` — kilogramme · mètre² — moment d'inertie; `N·m·s/rad` — newton · mètre · seconde / radian — gain par unité de vitesse; `%` — pour cent (un centième); `rad` — radian. [Glossaire des unités](../UNITS.md).

**Bases:** [0. Bases du calcul différentiel et intégral](00-calculus-foundations.md) · [Table des intégrales](../INTEGRAL_TABLE.md)

[README](../README.md) · [Aide-mémoire des formules](../CHEATSHEET.md) · [Exercices Python](../exercises/README.md) · [Mouvement, dérivées et intégrales](01-motion-calculus.md)

> **Avertissement :** Ces ressources pédagogiques assistées par IA peuvent contenir des erreurs, des traductions inexactes et des hypothèses incorrectes. Utilisation à vos risques et périls. Vérifiez les calculs indépendamment et n'utilisez aucun exemple pour piloter des machines réelles.

> **Hypothèses du modèle moteur :** Le modèle suppose une commande proportionnelle idéale du couple, sans charge, frottement, retard, limite de tension, saturation ni dynamique d'ordre supérieur. Il ne décrit pas universellement le comportement des moteurs.

## Points essentiels

La constante de temps $\tau$ décrit la rapidité d'approche d'un état d'équilibre dans un modèle du premier ordre. Le pas de simulation $dt$ règle la résolution numérique et non les propriétés physiques. Pour notre modèle idéal, $\tau=\frac{J}{K}$ ; une constante identique n'implique pas une énergie identique.

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

## Dans cette page

- [1. Réponse du premier ordre](#section-1)
- [2. Couple et inertie](#section-2)
- [3. Pas numérique et constante de temps](#section-3)
- [4. Estimer la constante de temps à partir de mesures](#section-4)
- [5. Énergie de rotation](#section-5)
- [6. Essayer](#section-6)
- [7. Pour aller plus loin (facultatif)](#section-7)
  - [D’où viennent 63.2 %, 86.5 % et 95.0 % ?](#time-constant-derivation)
  - [Calcul des résultats de la méthode d’Euler](#euler-values-derivation)

[Unités SI et point décimal](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Réponse du premier ordre

Pour les unités, les démonstrations et les limites numériques, voir [Pour aller plus loin](#section-7).

Pour une consigne constante $u$, une vitesse actuelle $v$ et $\tau>0$, la solution donnée ci-dessous atteint environ $63.2\ \%$ du changement après un temps $\tau$, $86.5\ \%$ après $2\tau$ et $95.0\ \%$ après $3\tau$. Cela **ne signifie pas** que la consigne est atteinte exactement à $t=\tau$.

**Notation :** $\varepsilon(t)=u-v(t)$ est l’erreur de vitesse (speed error, epsilon grec). La fonction exponentielle naturelle (exponential function) est $\exp(z)=\mathrm{e}^{z}$, où $\mathrm{e}\approx2.71828$ est le nombre d’Euler (Euler’s number), **pas** l’erreur. [Voir la dérivation et le calcul de 63.2 %](#time-constant-derivation).

$$
\frac{dv}{dt}=\frac{u-v}{\tau}.
$$

$$
v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right).
$$

| Temps | Part du changement |
| --- | ---: |
| $\tau$ | 63.2 % |
| $2\tau$ | 86.5 % |
| $3\tau$ | 95.0 % |

[D’où viennent exactement ces pourcentages ? Voir le calcul.](#time-constant-derivation)

![Réponse normalisée du premier ordre : chaque constante de temps élimine environ 63.2 % de l’erreur restante.](../../../assets/figures/first_order_response.svg)

<a id="section-2"></a>

## 2. Couple et inertie

Le contrôleur calcule une commande électrique ; le moteur produit physiquement le couple $M$. Dans le modèle simplifié, $J$ est le moment d'inertie, $\omega$ la vitesse angulaire et $K$ le coefficient reliant le couple à l'erreur de vitesse. Doubler $J$ à $K$ constant double $\tau$. Doubler simultanément $J$ et $K$ conserve $\tau$ tout en doublant le couple requis pour la même erreur. Frottements, charges, retards et limites de courant sont exclus.

$$
J\frac{d\omega}{dt}=M,\qquad M=K(u-\omega).
$$

$$
\frac{d\omega}{dt}=\frac{K}{J}(u-\omega),\qquad \tau=\frac{J}{K}.
$$

**Unités:** $J$: $\mathrm{kg}\cdot\mathrm{m}^2$; $\omega,u$: $\mathrm{rad/s}$; $M$: $\mathrm{N}\cdot\mathrm{m}$; $K$: $\mathrm{N}\cdot\mathrm{m}\cdot\mathrm{s}/\mathrm{rad}$; $\tau$: s.

Boucle de retour symbolique du modèle idéal. Le régulateur envoie une commande ; le moteur produit le couple physique.

![Boucle de retour symbolique du modèle idéal. Le régulateur envoie une commande ; le moteur produit le couple physique](../../../assets/figures/control_loop.svg)

<a id="section-3"></a>

## 3. Pas numérique et constante de temps

L'algorithme d'Euler calcule les changements par pas $dt$. Réduire $dt$ n'accélère pas le moteur du modèle : cela modifie seulement l'approximation. Pour $u=10\ \mathrm{mm/s}$, $\tau=1\ \mathrm{s}$ et une durée d'une seconde, Euler donne $6.513$ (pas $0.1$) ou $6.340\ \mathrm{mm/s}$ (pas $0.01$), contre $6.321\ \mathrm{mm/s}$ exactement.

$$
v_{n+1}=v_n+\frac{u-v_n}{\tau}\ dt.
$$

| Méthode | $v(1\ \mathrm{s})$ (mm/s) |
| --- | ---: |
| Euler $dt=0.1\ \mathrm{s}$ | 6.513 |
| Euler $dt=0.01\ \mathrm{s}$ | 6.340 |
| Exact | 6.321 |

[Calcul détaillé de ces valeurs numériques.](#euler-values-derivation)

<a id="section-4"></a>

## 4. Estimer la constante de temps à partir de mesures

Pour un changement de consigne de 0 à 1000 rpm (tours par minute), cherchez quand la vitesse mesurée atteint environ 632 rpm. Si cela se produit après 2 secondes, le modèle du premier ordre suggère $\tau\approx2\ \mathrm{s}$. Si la vitesse initiale n’est pas nulle, prenez 63.2 % de la **variation totale**, et non de la seule consigne. Le bruit, les délais et les dépassements compliquent cette estimation : c’est une forme élémentaire d’identification de système (system identification).

**Résultat exact du programme :** la fonction [`estimate_tau`](../../../exercises/02_first_order_response.py) demande des mesures avec des horodatages **strictement croissants** depuis le début de l'échelon. Elle renvoie l'instant du **premier échantillon observé** qui atteint le seuil de 63.2 % du changement, avec une tolérance de la moitié de la résolution de mesure connue. Si l'on observe le seuil à 2 s et que la mesure précédente date de 1 s, le vrai franchissement peut s'être produit **entre les mesures** : 2 s est une estimation limitée par l'échantillonnage, pas un ajustement exact. Les horodatages répétés, désordonnés ou les valeurs invalides sont rejetés même après ce franchissement ; sans franchissement, la fonction renvoie `None`.

**La résolution du capteur compte :** le paramètre `resolution` de `estimate_tau` doit être **inférieur à l'amplitude du changement total de vitesse**. Si la vitesse passe de 0 à 10 rpm mais que l'affichage avance par pas de 10 rpm, on ne peut pas estimer de façon fiable le passage du seuil de 63.2 %. La fonction rejette cette entrée au lieu d'annoncer un franchissement artificiel dès le premier échantillon. Même avec une résolution suffisante, l'estimation reste limitée par la fréquence d'échantillonnage.

<a id="section-5"></a>

## 5. Énergie de rotation

Le couple net est lié à l'accélération angulaire par $M=J\alpha$. Avec $J=2\ \mathrm{kg}\cdot\mathrm{m}^2$ et $\omega=10\ \mathrm{rad/s}$, l'énergie cinétique vaut $100\ \mathrm{J}$ ; doubler $J$ donne $200\ \mathrm{J}$. Doubler $\omega$ quadruple l'énergie. Il s'agit d'énergie mécanique, pas de la consommation électrique totale.

$$
M=J\alpha,\qquad \alpha=\frac{d\omega}{dt}.
$$

$$
E=\frac{1}{2}J\omega^2.
$$

<a id="section-6"></a>

## 6. Essayer

Dans une réponse indicielle idéale de 0 à 1000 rpm, atteindre environ 632 rpm après deux secondes suggère $\tau\approx2\ \mathrm{s}$. Les données réelles bruitées ou échantillonnées peuvent nécessiter un ajustement plus robuste. Comparez les solutions d'Euler et exacte dans les exercices.

[02_first_order_response.py](../../../exercises/02_first_order_response.py) · [03_rotation_energy.py](../../../exercises/03_rotation_energy.py) · [plot_models.py](../../../exercises/plot_models.py)


<a id="section-7"></a>

## 7. Pour aller plus loin (facultatif)


### Stabilité de la méthode d’Euler

À chaque pas, **l’écart à la consigne** calculé est multiplié par $1-\frac{dt}{\tau}$. Pour cette équation, la convergence exige $0<dt<2\tau$. Entre $\tau$ et $2\tau$, la valeur numérique oscille autour de la consigne : ce n’est pas le mouvement réel du moteur.

### Limites du modèle physique

Un bilan plus général est $J\ \frac{d\omega}{dt}=M_{\text{moteur}}-M_{\text{charge}}-M_{\text{frottement}}$. La relation $\tau=\frac{J}{K}$ suppose spécialement $M_{\text{résultant}}=K(u-\omega)$. Charges, frottements, délais et limites de courant peuvent la rendre inadaptée.

### Énergie et puissance

Pour $J$ constant, $\Delta E=\frac{1}{2} J(\omega_2^2-\omega_1^2)$ et la puissance mécanique instantanée (mechanical power) vaut $P=M\omega$. Cela ne donne pas directement la consommation électrique.


<a id="time-constant-derivation"></a>

### D’où viennent 63.2 %, 86.5 % et 95.0 % ?

Les pourcentages et l’exponentielle proviennent de **la même équation**. On définit l’erreur de vitesse par $\varepsilon(t)=u-v(t)$ (et non par le nombre d’Euler). Pour une consigne $u$ constante, $\frac{d\varepsilon}{dt}=-\frac{dv}{dt}$ :

$$
\varepsilon(t)=u-v(t),\qquad \frac{d\varepsilon}{dt}=-\frac{\varepsilon}{\tau}.
$$

$$
\frac{d\varepsilon}{\varepsilon}=-\frac{dt}{\tau}
\quad\Longrightarrow\quad
\ln\left\lvert\frac{\varepsilon(t)}{\varepsilon(0)}\right\rvert=-\frac{t}{\tau}
\quad\Longrightarrow\quad
\varepsilon(t)=\varepsilon(0)\exp\!\left(-\frac{t}{\tau}\right).
$$

La séparation des variables divise par $\varepsilon$ : cette étape suppose donc une erreur initiale non nulle. Si $u=v_0$, l'erreur reste nulle et l'équation différentielle initiale donne directement la solution constante $v(t)=u$.

$$
f(t)=\frac{v(t)-v_0}{u-v_0}=1-\exp\!\left(-\frac{t}{\tau}\right),\qquad (u\ne v_0).
$$

| $t$ | $f(t)$ |
| ---: | ---: |
| $\tau$ | $1-\exp(-1)=0.63212056\ldots\approx63.2\ \%$ |
| $2\tau$ | $1-\exp(-2)=0.86466472\ldots\approx86.5\ \%$ |
| $3\tau$ | $1-\exp(-3)=0.95021293\ldots\approx95.0\ \%$ |

Pour un échelon de 0 à 1000 rpm, cela donne environ 632, 865 et 950 rpm après une, deux et trois constantes de temps. Dans ce modèle idéal, on s’approche asymptotiquement de la consigne.

<a id="euler-values-derivation"></a>

### Calcul des résultats de la méthode d’Euler

$$
v_N=u+(v_0-u)\left(1-\frac{dt}{\tau}\right)^N,\qquad N=\frac{t}{dt}.
$$

$$
\begin{aligned}
u&=10,\quad v_0=0,\quad t=\tau=1;\\
v_{dt=0.1}&=10(1-0.9^{10})\approx6.5132;\\
v_{dt=0.01}&=10(1-0.99^{100})\approx6.3397;\\
v_{\mathrm{exact}}&=10(1-\exp(-1))\approx6.3212.
\end{aligned}
$$
