# Table des intégrales

**Lire dans cette langue:** [en](../en/INTEGRAL_TABLE.md) · [fr](INTEGRAL_TABLE.md) · [de](../de/INTEGRAL_TABLE.md) · [it](../it/INTEGRAL_TABLE.md) · [es](../es/INTEGRAL_TABLE.md) · [pt](../pt/INTEGRAL_TABLE.md) · [zh](../zh/INTEGRAL_TABLE.md) · [ja](../ja/INTEGRAL_TABLE.md) · [nb](../nb/INTEGRAL_TABLE.md) · [ru](../ru/INTEGRAL_TABLE.md) · [ko](../ko/INTEGRAL_TABLE.md) · [fi](../fi/INTEGRAL_TABLE.md) · [pl](../pl/INTEGRAL_TABLE.md)

**Unités utilisées ici (définies avant les exemples):** `s` — seconde; `mm` — millimètre = 0.001 m; `mm/s` — millimètre / seconde — vitesse linéaire; `mm/s²` — millimètre / seconde² — accélération; `N` — newton; `m` — mètre; `N/m` — newton / mètre — raideur; `J` — joule. [Glossaire des unités](UNITS.md).

[README](README.md) · [0. Bases du calcul différentiel et intégral](notes/00-calculus-foundations.md) · [Symboles](SYMBOLS.md)

Chaque intégrale indéfinie comporte +C, la constante d’intégration. a est constant ; on travaille sur un intervalle où l’intégrande est défini. Les angles sont en radians.

Commencez par les polynômes ; les formules trigonométriques et avec racines sont facultatives au début.

## Sommaire

- [Puissances et logarithmes](#section-1)
- [Fonctions exponentielles](#section-2)
- [Fonctions trigonométriques](#section-3)
- [Fractions rationnelles et fonctions trigonométriques inverses](#section-4)
- [Référence avancée : racines et réciproques](#section-5)
- [Choisir une formule et vérifier le résultat](#section-6)

<a id="section-1"></a>
## 1. Puissances et logarithmes

| Formule | Conditions / explication |
| --- | --- |
| $\int 1\ \mathrm{d}x=x+C$ | tout $x$ réel |
| $\int x^n\ \mathrm{d}x=\frac{x^{n+1}}{n+1}+C$ | $n\ne-1$; respecter le domaine réel des puissances |
| $\int\frac{1}{x}\ \mathrm{d}x=\ln\lvert x\rvert+C$ | $x\ne0$ |

<a id="section-2"></a>
## 2. Fonctions exponentielles

| Formule | Conditions / explication |
| --- | --- |
| $\int \mathrm{e}^{x}\ \mathrm{d}x=\mathrm{e}^{x}+C$ | tout $x$ réel |
| $\int a^x\ \mathrm{d}x=\frac{a^x}{\ln a}+C$ | $a>0$, $a\ne1$ |

<a id="section-3"></a>
## 3. Fonctions trigonométriques

| Formule | Conditions / explication |
| --- | --- |
| $\int\sin x\ \mathrm{d}x=-\cos x+C$ | $x$ en radians |
| $\int\cos x\ \mathrm{d}x=\sin x+C$ | $x$ en radians |
| $\int\frac{1}{\cos^2 x}\ \mathrm{d}x=\tan x+C$ | $\cos x\ne0$ |
| $\int\frac{1}{\sin^2 x}\ \mathrm{d}x=-\cot x+C$ | $\sin x\ne0$ |

<a id="section-4"></a>
## 4. Fractions rationnelles et fonctions trigonométriques inverses

| Formule | Conditions / explication |
| --- | --- |
| $\int\frac{1}{1+x^2}\ \mathrm{d}x=\arctan x+C$ | tout $x$ réel |
| $\int\frac{1}{\sqrt{1-x^2}}\ \mathrm{d}x=\arcsin x+C$ | $\lvert x\rvert<1$ |
| $\int\frac{1}{a^2+x^2}\ \mathrm{d}x=\frac{1}{a}\arctan\frac{x}{a}+C$ | $a>0$ |
| $\int\frac{1}{a^2-x^2}\ \mathrm{d}x=\frac{1}{2a}\ln\left\lvert\frac{a+x}{a-x}\right\rvert+C$ | $a>0$, $x\ne\pm a$ |
| $\int\frac{1}{\sqrt{a^2-x^2}}\ \mathrm{d}x=\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |

<a id="section-5"></a>
## 5. Référence avancée : racines et réciproques

| Formule | Conditions / explication |
| --- | --- |
| $\int\frac{1}{\sqrt{x^2+a^2}}\ \mathrm{d}x=\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{a^2-x^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{a^2-x^2}+\frac{a^2}{2}\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |
| $\int\sqrt{x^2+a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2+a^2}+\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{x^2-a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2-a^2}-\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2-a^2}\right\rvert+C$ | $a>0$, $\lvert x\rvert>a$ |
| $\int\frac{1}{\sin x}\ \mathrm{d}x=\ln\left\lvert\tan\frac{x}{2}\right\rvert+C$ | $\sin x\ne0$; intervalles sans singularités |
| $\int\frac{1}{\cos x}\ \mathrm{d}x=\ln\left\lvert\tan\left(\frac{x}{2}+\frac{\pi}{4}\right)\right\rvert+C$ | $\cos x\ne0$; intervalles sans singularités |

## Vérifier une formule

Dérivez le membre de droite pour vérifier une formule. Pour les puissances, inversez la règle de dérivation.

L’argument d’un logarithme doit être sans dimension ; ici x est sans dimension sauf échelle précisée. Respectez les domaines de définition et le signe choisi.

<a id="section-6"></a>
## 6. Choisir une formule et vérifier le résultat

Identifiez la variable après le différentiel (dx, dt ou dθ). Un coefficient n’est constant que s’il ne dépend pas de cette variable. Pour une primitive, ajoutez C ; pour une intégrale définie, calculez F(b) − F(a). Vérifiez en dérivant.

### Exemple A — déplacement par intégration de la vitesse

Pour v(t) = 3 mm/s + (4 mm/s²)t entre 0 et 2 s, on intègre chaque terme :

$$
\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}
=14\ \mathrm{mm}.
$$

Le résultat vaut 14 mm, pas 14 mm/s : vitesse intégrée sur le temps donne déplacement.

### Exemple B — travail d’une force variable

Un ressort F(x) = kx avec k = 200 N/m, étiré de 0 à 0.01 m :

$$
\int_0^{0.01\ \mathrm{m}}(200\ \mathrm{N/m})x\ \mathrm{d}x
=\left[(100\ \mathrm{N/m})x^2\right]_0^{0.01\ \mathrm{m}}=0.01\ \mathrm{J}.
$$

Le travail vaut 0.01 J. Il faut intégrer la force, non multiplier sa valeur finale par toute la course.

### Exemple C — logarithme d’un taux simple

Une primitive de 1/x est ln|x|. Pour x sans dimension de 1 à 2 :

$$
\int_1^2\frac1x\ \mathrm{d}x=[\ln x]_1^2=\ln2-\ln1=\ln2\approx0.693.
$$

Le résultat est ln 2 ≈ 0.693. x est un rapport sans dimension, pas une longueur.
