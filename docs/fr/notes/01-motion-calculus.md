# 1. Mouvement, dérivées et intégrales


**Lire cette page en:** [en](../../en/notes/01-motion-calculus.md) · [fr](01-motion-calculus.md) · [de](../../de/notes/01-motion-calculus.md) · [it](../../it/notes/01-motion-calculus.md) · [es](../../es/notes/01-motion-calculus.md) · [pt](../../pt/notes/01-motion-calculus.md) · [zh](../../zh/notes/01-motion-calculus.md) · [ja](../../ja/notes/01-motion-calculus.md) · [nb](../../nb/notes/01-motion-calculus.md) · [ru](../../ru/notes/01-motion-calculus.md) · [ko](../../ko/notes/01-motion-calculus.md) · [fi](../../fi/notes/01-motion-calculus.md) · [pl](../../pl/notes/01-motion-calculus.md)

**Unités utilisées ici (définies avant les exemples):** `s` — seconde; `mm` — millimètre = 0.001 m; `mm/s` — millimètre / seconde — vitesse linéaire; `mm/s²` — millimètre / seconde² — accélération; `%` — pour cent (un centième). [Glossaire des unités](../UNITS.md).

**Bases:** [0. Bases du calcul différentiel et intégral](00-calculus-foundations.md) · [Table des intégrales](../INTEGRAL_TABLE.md)

[README](../README.md) · [Aide-mémoire des formules](../CHEATSHEET.md) · [Exercices Python](../exercises/README.md) · [Dynamique du premier ordre et rotation](02-first-order-dynamics.md)

> **Avertissement :** Ces ressources pédagogiques assistées par IA peuvent contenir des erreurs, des traductions inexactes et des hypothèses incorrectes. Utilisation à vos risques et périls. Vérifiez les calculs indépendamment et n'utilisez aucun exemple pour piloter des machines réelles.

## Points essentiels

La distance parcourue est la longueur totale du trajet, tandis que le déplacement est la différence entre les positions finale et initiale. La vitesse scalaire (speed) est positive ou nulle ; la vitesse vectorielle (velocity) possède un sens. Dériver la position donne la vitesse instantanée ; intégrer la vitesse signée donne le déplacement.

**Termes anglais :**

- distance parcourue (distance traveled)
- déplacement (displacement)
- vitesse scalaire (speed)
- vitesse vectorielle (velocity)
- dérivée (derivative)
- intégrale (integral)
- intégration numérique (numerical integration)
- méthode d’Euler explicite (explicit Euler method)

## Dans cette page

- [1. Exemple de trajet](#section-1)
- [2. Dérivée et vitesse instantanée](#section-2)
- [3. Intégrale et déplacement](#section-3)
- [4. Intégration numérique](#section-4)
- [5. Essayer](#section-5)
- [6. Pour aller plus loin (facultatif)](#section-6)
  - [Pourquoi la dérivée de 2t² est 4t](#power-rule-derivation)
  - [Calcul des déplacements du tableau](#motion-values-derivation)

[Unités SI et point décimal](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Exemple de trajet

Pour les unités, les démonstrations et les limites numériques, voir [Pour aller plus loin](#section-6).

Un axe virtuel se déplace à $+3\ \mathrm{mm/s}$ pendant deux secondes puis à $-3\ \mathrm{mm/s}$ pendant deux secondes. Son déplacement vaut $+6-6=0\ \mathrm{mm}$, mais la distance parcourue vaut $12\ \mathrm{mm}$. Sur un cercle, la direction de la vitesse vectorielle change même lorsque la vitesse scalaire reste constante.

$$
\overline{v}=\frac{x(t_2)-x(t_1)}{t_2-t_1}.
$$

$$
\text{vitesse moyenne scalaire}=\frac{\text{distance totale parcourue}}{t_2-t_1}.
$$

Sur **les quatre secondes**, la vitesse moyenne signée et la vitesse scalaire moyenne donnent **des résultats différents**. L'axe revient au point de départ tout en parcourant 12 mm:

$$
\overline{v}_x=\frac{0\ \mathrm{mm}}{4\ \mathrm{s}}=0\ \mathrm{mm/s}
$$

$$
\overline{\lvert v\rvert}=\frac{12\ \mathrm{mm}}{4\ \mathrm{s}}=3\ \mathrm{mm/s}
$$

La vitesse scalaire moyenne n'est donc **pas nécessairement la norme de la vitesse vectorielle moyenne**. Sur un tour de cercle, le vecteur vitesse moyenne est également nul, mais la distance parcourue et la vitesse scalaire moyenne sont positives.

<a id="section-2"></a>

## 2. Dérivée et vitesse instantanée

Pour $x(t)=2t^2\ \mathrm{mm}$, avec $t$ en secondes, on obtient $v(t)=4t\ \mathrm{mm/s}$. **Pourquoi 4 ?** La règle de dérivation donne $d(t^2)/dt=2t$ ; donc $2t^2$ devient $2\cdot2t=4t$. [Calcul complet et unités](#power-rule-derivation). À $t=1\ \mathrm{s}$, la vitesse instantanée est $4\ \mathrm{mm/s}$. La différence finie avant donne $6$, $4.2$ et $4.02\ \mathrm{mm/s}$ avec des pas de $1$, $0.1$ et $0.01\ \mathrm{s}$ : elle se rapproche de la dérivée.

$$
v(t)=\frac{dx}{dt},\qquad v(t)\approx\frac{x(t+dt)-x(t)}{dt}.
$$

**Pourquoi un pas trop petit peut tromper :** à $t=1\ \mathrm{s}$, la dérivée exacte de $x(t)=2t^2$ vaut $4\ \mathrm{mm/s}$. Avec $dt=1e-17\ \mathrm{s}$, l'arithmétique `float` de Python arrondit `t + dt` à `t` : les deux positions calculées deviennent identiques et leur différence indiquerait faussement une vitesse nulle. À des échelles encore plus petites, les deux positions peuvent aussi s'arrondir à zéro alors que la dérivée ne l'est pas. L'exemple [`forward_derivative`](../../../exercises/01_motion_and_integral.py) renvoie maintenant `ValueError` dans ces cas au lieu d'un faux zéro. Il conserve le calcul par différence finie : choisir un pas représentable plutôt que le diminuer sans limite.

<a id="section-3"></a>

## 3. Intégrale et déplacement

L'intégrale de la vitesse signée peut être négative ou nulle ; celle de sa valeur absolue donne une distance non négative. Pour $v(t)=2t\ \mathrm{mm/s}$ de $0$ à $2\ \mathrm{s}$, le déplacement exact est $4\ \mathrm{mm}$.

$$
\Delta x=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t,\qquad
s=\int_{t_1}^{t_2}|v(t)|\ \mathrm{d}t.
$$

Géométriquement, la première intégrale représente l’aire algébrique sous la courbe vitesse–temps. **C’est un exemple distinct de celui de la section 2.** Là, la position $x(t)=2t^2$ a pour dérivée $v(t)=4t$. Pour montrer l’intégration, on choisit ici volontairement une autre vitesse : $v(t)=2t$. La position correspondante est $x(t)=t^2+C$ (avec des unités cohérentes). Il ne faut donc pas confondre les deux lois du mouvement.

<a id="section-4"></a>

## 4. Intégration numérique

Déplacement exact et approximation d’Euler au début du pas (données synthétiques).

![Déplacement exact et approximation d’Euler au début du pas (données synthétiques)](../../../assets/figures/euler_vs_exact.svg)

La méthode d'Euler explicite utilise la vitesse **au début** de chaque pas, pas la moyenne réelle sur l'intervalle. Dans cet exemple de vitesse croissante, elle sous-estime le déplacement : avec $dt=0.5$, $0.1$ et $0.01\ \mathrm{s}$, les résultats sont respectivement $3$, $3.8$ et $3.98\ \mathrm{mm}$ (valeur exacte : $4\ \mathrm{mm}$). La règle des trapèzes est exacte ici car la vitesse dépend linéairement du temps.

$$
x_{n+1}=x_n+v(t_n)\ dt.
$$

| `dt` (s) | Euler (mm) |
| ---: | ---: |
| 0.5 | 3.000 |
| 0.1 | 3.800 |
| 0.01 | 3.980 |
| Exact | 4.000 |


[Calcul des valeurs 3 ; 3.8 et 3.98.](#motion-values-derivation)

<a id="section-5"></a>

## 5. Essayer

Exécutez le programme de mouvement et réduisez progressivement $dt$. Pourquoi un aller-retour complet donne-t-il un déplacement nul mais une distance positive ?

[01_motion_and_integral.py](../../../exercises/01_motion_and_integral.py)

<a id="section-6"></a>

## 6. Pour aller plus loin (facultatif)

### Unités et coefficients

Lorsque $t$ est exprimé en secondes, $x(t)=2t^2$ mm est une écriture abrégée : le coefficient vaut $2\ \mathrm{mm/s^2}$. La dérivée $v(t)=4t$ s’exprime alors en mm/s. Vérifiez toujours les unités.

### Limites de l’approximation

Une différence finie (finite difference) estime la dérivée sur un intervalle non nul. Réduire le pas diminue souvent l’erreur de troncature, mais un pas minuscule peut accroître les erreurs d’arrondi ou le bruit. La méthode d’Euler utilise la valeur au début du pas.

### Mouvement dans plusieurs dimensions

Pour une position vectorielle $\mathbf r(t)$, la vitesse vectorielle est $\mathbf v=d\mathbf r/dt$ ; la vitesse scalaire est $\|\mathbf v\|$ et la longueur du trajet $s=\int\|\mathbf v(t)\|dt$.


<a id="power-rule-derivation"></a>

### Pourquoi la dérivée de $2t^2$ est $4t$



$$
x(t)=at^2,\qquad
\frac{dx}{dt}=\lim_{h\to0}\frac{a(t+h)^2-at^2}{h}
=\lim_{h\to0}a(2t+h)=2at.
$$

$$
 a=2\ \mathrm{mm/s^2},\qquad
 v(t)=2at=(4\ \mathrm{mm/s^2})t.
$$

<a id="motion-values-derivation"></a>

### Calcul des déplacements du tableau

$$
a=2\ \mathrm{mm/s^2},\qquad v(t)=at,\qquad 0\le t\le2\ \mathrm{s}.
$$

$$
\Delta x=\int_{0}^{2\ \mathrm{s}}at\ \mathrm{d}t
=\left[\frac{at^2}{2}\right]_{0}^{2\ \mathrm{s}}
=4\ \mathrm{mm}.
$$



Le symbole $\sum$ (sigma majuscule grec, **sommation** / summation) signifie « additionner les termes ». Dans $\sum_{n=0}^{N-1}(2nh)h$, l’indice $n$ prend les valeurs $0; 1; \ldots; N-1$ : il y a $N$ termes. C’est comme une boucle Python `for` qui ajoute chaque contribution. Par exemple, $\sum_{n=1}^{3}n=1+2+3=6$. [← Symboles expliqués](../SYMBOLS.md#summation).

$$
h=\frac{dt}{1\ \mathrm{s}},\qquad N=\frac{2}{h}.
$$

$$
x_{\mathrm{Euler}}(2\ \mathrm{s})
=\left[\sum_{n=0}^{N-1}(2nh)h\right]\ \mathrm{mm}
=\left[h^2N(N-1)\right]\ \mathrm{mm}
=(4-2h)\ \mathrm{mm}.
$$

Ici `h` est la valeur numérique du pas `dt` exprimé en secondes (`dt = 0.5 s` donne `h = 0.5`) ; `N` est le nombre de pas. Le résultat est une **distance en millimètres**.



Pour $dt=0.5$, $0.1$ et $0.01$ seconde, on obtient $3$, $3.8$ et $3.98$ millimètres. On suppose que $2/dt$ est entier.
