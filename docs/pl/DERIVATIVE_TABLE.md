# Tablica pochodnych

**Języki:** [en](../en/DERIVATIVE_TABLE.md) · [fr](../fr/DERIVATIVE_TABLE.md) · [de](../de/DERIVATIVE_TABLE.md) · [it](../it/DERIVATIVE_TABLE.md) · [es](../es/DERIVATIVE_TABLE.md) · [pt](../pt/DERIVATIVE_TABLE.md) · [zh](../zh/DERIVATIVE_TABLE.md) · [ja](../ja/DERIVATIVE_TABLE.md) · [nb](../nb/DERIVATIVE_TABLE.md) · [ru](../ru/DERIVATIVE_TABLE.md) · [ko](../ko/DERIVATIVE_TABLE.md) · [fi](../fi/DERIVATIVE_TABLE.md) · [pl](DERIVATIVE_TABLE.md)

**Jednostki w tej części (wyjaśnione przed przykładami):** `s` — sekunda; `mm` — milimetr = 0.001 m; `mm/s` — milimetr na sekundę — prędkość liniowa; `mm/s²` — milimetr na sekundę do kwadratu — przyspieszenie. [Słownik jednostek](UNITS.md).

[Spis treści](README.md) · [Tablica całek](INTEGRAL_TABLE.md) · [Podstawy analizy](notes/00-calculus-foundations.md)

Jeśli $u$ i $v$ zależą od $x$, a $a$ jest stałą, apostrof oznacza pochodną względem $x$. Kąty w pochodnych funkcji trygonometrycznych mierzymy w radianach. Pochodna istnieje tam, gdzie istnieje odpowiednia granica. Dla funkcji złożonych stosujemy regułę łańcuchową (chain rule). Tutaj $u'=\frac{\mathrm{d}u}{\mathrm{d}x}$ i $v'=\frac{\mathrm{d}v}{\mathrm{d}x}$.

## Reguły

| Funkcja | Pochodna | Warunki |
| --- | --- | --- |
| $c$ | $0$ | $c$ — stała |
| $x$ | $1$ | — |
| $x^n$ | $nx^{n-1}$ | rzeczywiste $n$; tam, gdzie funkcja jest określona i różniczkowalna |
| $u+v$ | $u'+v'$ | — |
| $au$ | $au'$ | $a$ — stała |
| $uv$ | $u'v+uv'$ | reguła iloczynu |
| $\frac{u}{v}$ | $\frac{u'v-uv'}{v^2}$ | $v\ne0$ |
| $f(u)$ | $f'(u)u'$ | reguła łańcuchowa |
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

## Przykłady

**Reguła łańcuchowa (chain rule):** dla $y=(3x^2+1)^4$ podstawmy $u=3x^2+1$. Wtedy $u'=6x$ oraz

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=4u^3u'=24x(3x^2+1)^3.
$$

**Prędkość i przyspieszenie:** dla położenia $x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2$ pochodna po czasie daje prędkość, a kolejna pochodna — przyspieszenie:

$$
v(t)=\frac{\mathrm{d}x}{\mathrm{d}t}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t,
$$

$$
a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=4\ \mathrm{mm/s^2}.
$$

Dla $t=2\ \mathrm{s}$ prędkość wynosi $v=11\ \mathrm{mm/s}$. To przykład matematyczny, a nie instrukcja sterowania maszyną.

**Pochodna funkcji odwrotnej (inverse function):** jeśli $y=f^{-1}(x)$, funkcja $f$ jest różniczkowalna w $y$ i $f'(y)\ne0$, to na lokalnie odwracalnej gałęzi mamy $(f^{-1})'(x)=1/f'(y)$.
