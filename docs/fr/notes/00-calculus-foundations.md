# 0. Calcul différentiel et intégral : exemples pratiques en mécanique

**Langues:** [en](../../en/notes/00-calculus-foundations.md) · [fr](00-calculus-foundations.md) · [de](../../de/notes/00-calculus-foundations.md) · [it](../../it/notes/00-calculus-foundations.md) · [es](../../es/notes/00-calculus-foundations.md) · [pt](../../pt/notes/00-calculus-foundations.md) · [zh](../../zh/notes/00-calculus-foundations.md) · [ja](../../ja/notes/00-calculus-foundations.md) · [nb](../../nb/notes/00-calculus-foundations.md) · [ru](../../ru/notes/00-calculus-foundations.md) · [ko](../../ko/notes/00-calculus-foundations.md) · [fi](../../fi/notes/00-calculus-foundations.md) · [pl](../../pl/notes/00-calculus-foundations.md)

L'**exponentielle naturelle** est $\exp(x)=\mathrm{e}^{x}$, où le **nombre d'Euler** vaut $\mathrm{e}\approx2.71828$. Elle décrit une croissance ou une décroissance continue ; $\exp(0)=1$ et $\exp(-1)\approx0.3679$. Le logarithme naturel $\ln$ est sa fonction réciproque : $\ln(\exp(x))=x$. Voir le [guide des symboles](../SYMBOLS.md).

**Unités utilisées ici (définies avant les exemples):** `s` — seconde; `mm` — millimètre = 0.001 m; `mm/s` — millimètre / seconde — vitesse linéaire; `mm/s²` — millimètre / seconde² — accélération; `kg·m²` — kilogramme · mètre² — moment d'inertie; `rad/s` — radian / seconde — vitesse angulaire; `rad/s²` — radian / seconde² — accélération angulaire; `N·m` — newton · mètre — moment de force; `W` — watt; `rpm` — tour par minute; `N/m` — newton / mètre — raideur; `mm³/s` — millimètre³ / seconde — débit volumique; `%` — pour cent (un centième); `m` — mètre; `kg` — kilogramme; `N` — newton; `J` — joule; `rad` — radian. [Glossaire des unités](../UNITS.md).

[README](../README.md) · [Integral table](../INTEGRAL_TABLE.md) · [Trigonometry table](../TRIGONOMETRY.md) · [Motion](01-motion-calculus.md) · [Dynamics](02-first-order-dynamics.md) · [Symbols](../SYMBOLS.md)

> **Approximation pédagogique:** Vérifiez modèles et unités ; n’utilisez pas ce code sur une vraie machine.

La **dérivée (derivative)** indique la vitesse de variation instantanée ; la **dérivée seconde (second derivative)** indique comment évolue cette vitesse. L’**intégrale (integral)** accumule les variations. Une **limite (limit)** définit le taux instantané ; un **logarithme (logarithm)** permet de retrouver le temps dans une réponse exponentielle.

On retrouve ces outils dans un axe de machine, un servomoteur, une articulation de robot, un ressort et un capteur. Partons de la question physique, puis choisissons la règle et les unités.

## Sommaire

- [1. Du changement mesuré au modèle mathématique](#section-1)
- [2. Limites et dérivées premières](#section-2)
- [3. Dérivées première et seconde : mouvement d’un axe](#section-3)
- [4. Règle de la chaîne : énergie de rotation](#section-4)
- [5. Exponentielle et logarithme : temps de réponse](#section-5)
- [6. Intégrales : déplacement et travail mécanique](#section-6)
- [7. Exemple complémentaire : sphère en expansion](#section-7)
- [8. Unités, vérifications et exercices](#section-8)

<a id="section-1"></a>
## 1. Du changement mesuré au modèle mathématique

| Question physique | Outil mathématique |
| --- | --- |
| À quelle vitesse se déplace l’axe **maintenant** ? | Dérivée première $dx/dt$ |
| Comment varie la vitesse ? | Dérivée seconde $d^2x/dt^2$ |
| Quand la réponse atteint-elle 90 % ? | Logarithme $\ln$ |
| Quel déplacement en 2 s ? | Intégrale définie $\int v\ \mathrm{d}t$ |
| Quel travail d’une force variable ? | Intégrale $\int F\ \mathrm{d}x$ |

<a id="section-2"></a>
## 2. Limites et dérivées premières

Une **différence finie (finite difference)** entre deux mesures donne un taux moyen sur un intervalle. La dérivée est la limite de ce taux lorsque l’intervalle tend vers zéro.

$$
v(t)=\frac{dx}{dt}=\lim_{h\to0}\frac{x(t+h)-x(t)}{h}.
$$

Pour la position $x(t)=a t^2$, avec $a=2\ \mathrm{mm/s^2}$, développons le numérateur avant de prendre la limite :

$$
\frac{x(t+h)-x(t)}h=\frac{a[(t+h)^2-t^2]}h=a(2t+h)\longrightarrow 2at.
$$

Le facteur $h$ se simplifie **avant** de faire tendre $h$ vers zéro. À $t=1\ \mathrm{s}$, la vitesse instantanée vaut $4\ \mathrm{mm/s}$. On ne remplace jamais directement une forme indéterminée $0/0$.

**Règles usuelles de dérivation (differentiation rules)** : $c$ et $n$ sont constants ; les angles des fonctions trigonométriques sont en radians.

| Règle | Formule |
| --- | --- |
| Constante | $\frac{d}{dt}c=0$ |
| Puissance | $\frac{d}{dt}t^n=n t^{n-1}$ |
| Coefficient et somme | $(cf+g)'=cf'+g'$ |
| Produit | $(fg)'=f' g+fg'$ |
| Quotient, $g\ne0$ | $\left(\frac{f}{g}\right)'=\frac{f' g-fg'}{g^2}$ |
| Fonction composée | $\frac{d}{dt}f(g(t))=f'(g(t))g'(t)$ |
| Exponentielle | $\frac{d}{dt}\exp(t)=\exp(t)$ |
| Logarithme népérien, $t>0$ | $\frac{d}{dt}\ln t=\frac1t$ |
| Sinus / cosinus | $\frac{d}{dt}\sin t=\cos t$, $\frac{d}{dt}\cos t=-\sin t$ |

![Pente de la position et aire sous la vitesse](../../../assets/figures/calculus_slope_area.svg)

<a id="section-3"></a>
## 3. Dérivées première et seconde : mouvement d’un axe

Un chariot commence à 2 mm avec une vitesse initiale de 3 mm/s et une accélération constante de 4 mm/s². Sa position est :

$$
x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2.
$$

**Première dérivée** : la vitesse. Le terme constant disparaît, le terme en $t$ devient 3 mm/s et le terme en $t^2$ devient linéaire en $t$.

$$
v(t)=\frac{dx}{dt}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t.
$$

**Seconde dérivée** : l’accélération. On dérive encore la vitesse. À 2 s : position 16 mm, vitesse 11 mm/s, accélération 4 mm/s².

$$
a(t)=\frac{d^2x}{dt^2}=\frac{dv}{dt}=4\ \mathrm{mm/s^2}.
$$

La seconde dérivée a les unités longueur/temps² ; ce n’est **pas** le carré de la première dérivée.

<a id="section-4"></a>
## 4. Règle de la chaîne : énergie de rotation

Un volant tournant stocke de l’énergie cinétique. Si $\omega$ dépend du temps, l’énergie $E$ varie à travers $\omega$ : c’est la **règle de la chaîne (chain rule)**.

$$
E(\omega)=\frac12J\omega^2,\quad \omega=\omega(t),
$$
$$
\frac{dE}{dt}=\frac{dE}{d\omega}\frac{d\omega}{dt}=J\omega\alpha=M\omega=P.
$$

Pour $J=0.01\ \mathrm{kg\cdot m^2}$, $\omega=10\ \mathrm{rad/s}$ et $\alpha=2\ \mathrm{rad/s^2}$, le couple $J\alpha$ vaut $0.02\ \mathrm{N\cdot m}$ et la puissance mécanique instantanée vaut $0.2\ \mathrm{W}$. On retrouve $P=M\omega$.

<a id="section-5"></a>
## 5. Exponentielle et logarithme : temps de réponse

Dans un modèle simple du premier ordre, la vitesse atteint progressivement sa valeur finale selon une exponentielle. $\tau$ est la **constante de temps (time constant)**, en secondes.

$$
\omega(t)=\omega_\infty\bigl(1-\exp(-t/\tau)\bigr),\quad t\ge0,\ \tau>0.
$$

Cette forme suppose une **vitesse angulaire initiale nulle**, $\omega(0)=0$, et une consigne finale constante $\omega_\infty$. Si la vitesse initiale vaut $\omega_0\ne0$, la réponse générale du même modèle du premier ordre est :

$$
\omega(t)=\omega_\infty+(\omega_0-\omega_\infty)\exp(-t/\tau).
$$

**Exemple avec une vitesse initiale non nulle :** prenons $\omega_0=200\ \mathrm{rpm}$, $\omega_\infty=1000\ \mathrm{rpm}$ et $\tau=0.5\ \mathrm{s}$. Après une constante de temps ($t=0.5\ \mathrm{s}$) :

$$
\omega(\tau)=1000+(200-1000)\exp(-1)\approx705.7\ \mathrm{rpm}.
$$

La réponse a effectué **63.2 % des 800 rpm de variation**, et non 63.2 % de la valeur finale de 1000 rpm. À $t=0$, la formule donne 200 rpm ; à long terme elle tend vers 1000 rpm. Il s'agit d'un calcul théorique et non d'une commande moteur.

L’exponentielle représente la fraction d’erreur restante. Pour trouver **quand** une fraction donnée reste, on emploie le **logarithme népérien (natural logarithm)** $\ln$, inverse de $\exp$. L’argument $0.1$ est sans dimension.

$$
\exp(-t/\tau)=0.1
\quad\Longrightarrow\quad
-\frac{t}{\tau}=\ln(0.1)
\quad\Longrightarrow\quad
t=-\tau\ln(0.1)=\tau\ln(10)\approx2.303\tau.
$$

À 90 % du changement final, il reste 10 % de l’erreur initiale. Pour $\tau=0.5\ \mathrm{s}$, le modèle idéal donne environ 1.151 s. Un système réel peut avoir des limites et des retards.

La dérivée de $\ln z$ vaut $1/z$ pour $z>0$ ; avec $z=z(t)$, multiplier également par $dz/dt$. Le logarithme d’une grandeur physique nécessite un rapport sans dimension.

$$
\ln(1)=0,\quad \ln(\mathrm{e})=1,\quad \ln(\mathrm{e}^{z})=z,\quad \frac{d}{dz}\ln z=\frac1z\ (z>0).
$$

<a id="section-6"></a>
## 6. Intégrales : déplacement et travail mécanique

L’**intégrale indéfinie (indefinite integral)** donne des primitives (antiderivatives) avec une constante $C$. L’**intégrale définie (definite integral)** donne la variation accumulée sur un intervalle.

$$
\int 4t\ \mathrm{d}t=2t^2+C,\qquad \int t^n\ \mathrm{d}t=\frac{t^{n+1}}{n+1}+C\ (n\ne-1).
$$

**Déplacement.** Le chariot part de $x_0=2\ \mathrm{mm}$ et sa vitesse est $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$. Calculons le déplacement entre 0 et 2 s :

$$
\Delta x=\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
$$
$$
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}=6\ \mathrm{mm}+8\ \mathrm{mm}=14\ \mathrm{mm}.
$$

Le déplacement est de 14 mm ; avec la position initiale, $x(2)=16\ \mathrm{mm}$. Une vitesse négative contribue négativement au déplacement signé, pas à la distance parcourue.

**Travail du ressort.** Étirons un ressort linéaire idéal de $x=0$ à $x=0.01\ \mathrm{m}$ avec $k=200\ \mathrm{N/m}$. La force augmente avec l’allongement ; on intègre le travail élémentaire :

$$
F(x)=kx,\qquad W=\int_0^{0.01\ \mathrm{m}}kx\ \mathrm{d}x
=\left[\frac{kx^2}{2}\right]_0^{0.01\ \mathrm{m}}
=\frac{200\ \mathrm{N/m}}2(0.01\ \mathrm{m})^2=0.01\ \mathrm{J}.
$$

Le travail vaut 0.01 J. Multiplier la force finale $F=2\ \mathrm{N}$ par toute la course donnerait 0.02 J, valeur incorrecte puisque la force n’est pas constante.

<a id="section-7"></a>
## 7. Exemple complémentaire : sphère en expansion

**Exemple facultatif de règle de la chaîne.** Le volume d’une sphère dépend du rayon, qui peut dépendre du temps : même structure que l’énergie du volant dépendant de la vitesse angulaire.

$$
V(r)=\frac43\pi r^3,\qquad \frac{dV}{dt}=\frac{dV}{dr}\frac{dr}{dt}=4\pi r^2\frac{dr}{dt}.
$$

À $r=10\ \mathrm{mm}$ et $dr/dt=1\ \mathrm{mm/s}$, le taux volumique vaut $400\pi\approx1256.64\ \mathrm{mm^3/s}$. Pour $r(t)=10\ \mathrm{mm}+(1\ \mathrm{mm/s^2})t^2$, à 2 s on obtient $r=14\ \mathrm{mm}$, $dr/dt=4\ \mathrm{mm/s}$, puis $3136\pi\approx9852.03\ \mathrm{mm^3/s}$.

<a id="section-8"></a>
## 8. Unités, vérifications et exercices

**Vérifications :** dérivée de position en m/s, seconde dérivée en m/s² ; intégrale de force sur une distance en N·m = J ; constante $C$ pour une primitive ; dérivée locale, intégrale accumulée ; différentielle $\mathrm{d}t$ distincte du pas fini `dt` dans un programme.

**À essayer :** (1) Avec $x(t)=5\ \mathrm{mm}+(2\ \mathrm{mm/s})t+(1\ \mathrm{mm/s^2})t^2$, trouver vitesse et accélération à 3 s. (2) Avec $\tau=1\ \mathrm{s}$, combien de temps pour atteindre 90 % ? (3) Déplacement à 4 mm/s durant 2 s. **Réponses :** 8 mm/s et 2 mm/s² ; environ 2.303 s ; 8 mm.

**Solutions détaillées :**

1. $v(t)=\frac{dx}{dt}=2\ \mathrm{mm/s}+2(1\ \mathrm{mm/s^2})t$; $v(3\ \mathrm{s})=2+2\cdot3=8\ \mathrm{mm/s}$. $a(t)=\frac{dv}{dt}=2\ \mathrm{mm/s^2}$.
2. $f(t)=1-\exp(-t/\tau)=0.9$; $\exp(-t/\tau)=0.1$; $t=-\tau\ln(0.1)=\tau\ln(10)$. $\tau=1\ \mathrm{s}$; $t\approx2.303\ \mathrm{s}$.
3. $\Delta x=\int_0^{2\ \mathrm{s}}(4\ \mathrm{mm/s})\ \mathrm{d}t=(4\ \mathrm{mm/s})(2\ \mathrm{s})=8\ \mathrm{mm}$.


[Integral reference](../INTEGRAL_TABLE.md) · [Trigonometry](../TRIGONOMETRY.md) · [Next: motion](01-motion-calculus.md) · [Python exercises](../exercises/README.md)
