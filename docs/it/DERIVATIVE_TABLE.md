# Tabella delle derivate

**Lingue:** [en](../en/DERIVATIVE_TABLE.md) · [fr](../fr/DERIVATIVE_TABLE.md) · [de](../de/DERIVATIVE_TABLE.md) · [it](DERIVATIVE_TABLE.md) · [es](../es/DERIVATIVE_TABLE.md) · [pt](../pt/DERIVATIVE_TABLE.md) · [zh](../zh/DERIVATIVE_TABLE.md) · [ja](../ja/DERIVATIVE_TABLE.md) · [nb](../nb/DERIVATIVE_TABLE.md) · [ru](../ru/DERIVATIVE_TABLE.md) · [ko](../ko/DERIVATIVE_TABLE.md) · [fi](../fi/DERIVATIVE_TABLE.md) · [pl](../pl/DERIVATIVE_TABLE.md)

**Unità usate qui (spiegate prima degli esempi):** `s` — secondo; `mm` — millimetro = 0.001 m; `mm/s` — millimetro / secondo — velocità lineare; `mm/s²` — millimetro / secondo² — accelerazione. [Glossario delle unità](UNITS.md).

[Indice del corso](README.md) · [Tabella degli integrali](INTEGRAL_TABLE.md) · [Fondamenti di calcolo](notes/00-calculus-foundations.md)

Se $u$ e $v$ dipendono da $x$ e $a$ è costante, gli apici indicano la derivazione rispetto a $x$. Gli angoli sono in radianti. La derivata è definita solo dove esiste il limite corrispondente. Per le funzioni composte si usa la regola della catena (chain rule). Qui $u'=\frac{\mathrm{d}u}{\mathrm{d}x}$ e $v'=\frac{\mathrm{d}v}{\mathrm{d}x}$.

## Regole

| Funzione | Derivata | Condizioni |
| --- | --- | --- |
| $c$ | $0$ | $c$ costante |
| $x$ | $1$ | — |
| $x^n$ | $nx^{n-1}$ | $n$ reale; dove la funzione è definita e derivabile |
| $u+v$ | $u'+v'$ | — |
| $au$ | $au'$ | $a$ costante |
| $uv$ | $u'v+uv'$ | regola del prodotto |
| $\frac{u}{v}$ | $\frac{u'v-uv'}{v^2}$ | $v\ne0$ |
| $f(u)$ | $f'(u)u'$ | regola della catena |
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

## Esempi

**Regola della catena (chain rule):** Per $y=(3x^2+1)^4$, poniamo $u=3x^2+1$. Allora $u'=6x$ e

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=4u^3u'=24x(3x^2+1)^3.
$$

**Velocità e accelerazione:** Per la posizione $x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2$, la derivata temporale dà la velocità, e la sua derivata dà l'accelerazione:

$$
v(t)=\frac{\mathrm{d}x}{\mathrm{d}t}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t,
$$

$$
a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=4\ \mathrm{mm/s^2}.
$$

A $t=2\ \mathrm{s}$ la velocità è $11\ \mathrm{mm/s}$. È un esempio matematico, non un'istruzione per controllare una macchina.

**Funzione inversa (inverse function):** Se $y=f^{-1}(x)$, $f$ è derivabile in $y$ e $f'(y)\ne0$, allora $(f^{-1})'(x)=1/f'(y)$ su un ramo localmente invertibile.
