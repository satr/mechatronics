# Table des dérivées

**Langues:** [en](../en/DERIVATIVE_TABLE.md) · [fr](DERIVATIVE_TABLE.md) · [de](../de/DERIVATIVE_TABLE.md) · [it](../it/DERIVATIVE_TABLE.md) · [es](../es/DERIVATIVE_TABLE.md) · [pt](../pt/DERIVATIVE_TABLE.md) · [zh](../zh/DERIVATIVE_TABLE.md) · [ja](../ja/DERIVATIVE_TABLE.md) · [nb](../nb/DERIVATIVE_TABLE.md) · [ru](../ru/DERIVATIVE_TABLE.md) · [ko](../ko/DERIVATIVE_TABLE.md) · [fi](../fi/DERIVATIVE_TABLE.md) · [pl](../pl/DERIVATIVE_TABLE.md)

**Unités utilisées ici (définies avant les exemples):** `s` — seconde; `mm` — millimètre = 0.001 m; `mm/s` — millimètre / seconde — vitesse linéaire; `mm/s²` — millimètre / seconde² — accélération. [Glossaire des unités](UNITS.md).

[Sommaire du cours](README.md) · [Table des intégrales](INTEGRAL_TABLE.md) · [Bases du calcul](notes/00-calculus-foundations.md)

Si $u$ et $v$ dépendent de $x$ et si $a$ est constant, les primes indiquent une dérivation par rapport à $x$. Les angles sont en radians. Une dérivée est définie là où la limite correspondante existe. Pour une fonction composée, appliquer la règle de la chaîne (chain rule). Ici $u'=\frac{\mathrm{d}u}{\mathrm{d}x}$ et $v'=\frac{\mathrm{d}v}{\mathrm{d}x}$.

## Règles

| Fonction | Dérivée | Conditions |
| --- | --- | --- |
| $c$ | $0$ | $c$ constant |
| $x$ | $1$ | — |
| $x^n$ | $nx^{n-1}$ | réel $n$ ; là où la fonction est définie et dérivable |
| $u+v$ | $u'+v'$ | — |
| $au$ | $au'$ | $a$ constant |
| $uv$ | $u'v+uv'$ | règle du produit |
| $\frac{u}{v}$ | $\frac{u'v-uv'}{v^2}$ | $v\ne0$ |
| $f(u)$ | $f'(u)u'$ | règle de la chaîne |
| $\frac{1}{u}$ | $-\frac{u'}{u^2}$ | $u\ne0$ |
| $\sqrt{u}$ | $\frac{u'}{2\sqrt{u}}$ | $u>0$ |
| $\exp(u)$ | $\exp(u)u'$ | — |
| $a^u$ | $a^u\ln(a)u'$ | $a>0$ |
| $\ln(u)$ | $\frac{u'}{u}$ | $u>0$ |
| $\ln\lvert u\rvert$ | $\frac{u'}{u}$ | $u\ne0$ |
| $\sin(u)$ | $\cos(u)u'$ | — |
| $\cos(u)$ | $-\sin(u)u'$ | — |
| $\tan(u)$ | $\frac{u'}{\cos^2(u)}$ | $\cos(u)\ne0$ |
| $\arcsin(u)$ | $\frac{u'}{\sqrt{1-u^2}}$ | $-1<u<1$ |
| $\arccos(u)$ | $-\frac{u'}{\sqrt{1-u^2}}$ | $-1<u<1$ |
| $\arctan(u)$ | $\frac{u'}{1+u^2}$ | — |
| $\mathrm{arsinh}(u)$ | $\frac{u'}{\sqrt{1+u^2}}$ | — |

## Exemples

**Règle de la chaîne (chain rule) :** Pour $y=(3x^2+1)^4$, posons $u=3x^2+1$. Alors $u'=6x$ et

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=4u^3u'=24x(3x^2+1)^3.
$$

**Vitesse et accélération :** Pour la position $x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2$, la dérivée temporelle donne la vitesse, puis sa dérivée donne l'accélération :

$$
v(t)=\frac{\mathrm{d}x}{\mathrm{d}t}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t,
$$

$$
a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=4\ \mathrm{mm/s^2}.
$$

À $t=2\ \mathrm{s}$, la vitesse vaut $11\ \mathrm{mm/s}$. Il s'agit d'un exemple mathématique, pas d'une consigne de commande d'une machine.

**Fonction réciproque (inverse function) :** Si $y=f^{-1}(x)$, si $f$ est dérivable en $y$ et si $f'(y)\ne0$, alors $(f^{-1})'(x)=1/f'(y)$ sur une branche localement inversible.
