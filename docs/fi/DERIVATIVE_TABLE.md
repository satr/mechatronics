# Derivaattojen taulukko

**Kielet:** [en](../en/DERIVATIVE_TABLE.md) · [fr](../fr/DERIVATIVE_TABLE.md) · [de](../de/DERIVATIVE_TABLE.md) · [it](../it/DERIVATIVE_TABLE.md) · [es](../es/DERIVATIVE_TABLE.md) · [pt](../pt/DERIVATIVE_TABLE.md) · [zh](../zh/DERIVATIVE_TABLE.md) · [ja](../ja/DERIVATIVE_TABLE.md) · [nb](../nb/DERIVATIVE_TABLE.md) · [ru](../ru/DERIVATIVE_TABLE.md) · [ko](../ko/DERIVATIVE_TABLE.md) · [fi](DERIVATIVE_TABLE.md) · [pl](../pl/DERIVATIVE_TABLE.md)

**Tämän sivun yksiköt (selitetty ennen esimerkkejä):** `s` — sekunti; `mm` — millimetri = 0.001 m; `mm/s` — millimetri / sekunti — lineaarinen nopeus; `mm/s²` — millimetri / sekunti² — kiihtyvyys. [Yksikköluettelo](UNITS.md).

[Sisällysluettelo](README.md) · [Integraalien kaavataulukko](INTEGRAL_TABLE.md) · [Differentiaali- ja integraalilaskennan perusteet](notes/00-calculus-foundations.md)

u ja v riippuvat muuttujasta x; a on vakio. Kulmat ovat radiaaneina. Derivaatta on määritelty siellä, missä vastaava raja-arvo on olemassa. Yhdistetyille funktioille käytetään ketjusääntöä. Tässä $u'=\frac{\mathrm{d}u}{\mathrm{d}x}$ ja $v'=\frac{\mathrm{d}v}{\mathrm{d}x}$.

## Derivointisäännöt

| Funktio | Derivaatta | Ehdot |
| --- | --- | --- |
| $c$ | $0$ | $c$ vakio |
| $x$ | $1$ | — |
| $x^n$ | $nx^{n-1}$ | reaalinen $n$; missä funktio on määritelty ja derivoituva |
| $u+v$ | $u'+v'$ | — |
| $au$ | $au'$ | $a$ vakio |
| $uv$ | $u'v+uv'$ | tulon derivointisääntö |
| $\frac{u}{v}$ | $\frac{u'v-uv'}{v^2}$ | $v\ne0$ |
| $f(u)$ | $f'(u)u'$ | ketjusääntö |
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

## Esimerkit

**Ketjusääntö (chain rule):** Derivoidaan $y=(3x^2+1)^4$. Merkitään $u=3x^2+1$, jolloin $u'=6x$. Siten

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=4u^3u'=24x(3x^2+1)^3.
$$

**Nopeus ja kiihtyvyys (velocity and acceleration):** Oletetaan paikan riippuvan ajasta seuraavasti:

$$
x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2.
$$

Paikan aikaderivaatta on nopeus ja nopeuden aikaderivaatta kiihtyvyys:

$$
v(t)=\frac{\mathrm{d}x}{\mathrm{d}t}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t,
$$

$$
a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=4\ \mathrm{mm/s^2}.
$$

Kun $t=2\ \mathrm{s}$, nopeus on $11\ \mathrm{mm/s}$. Tämä on matemaattinen esimerkki, ei koneen ohjausohje.

**Käänteisfunktio (inverse function):** Jos $y=f^{-1}(x)$, $f$ on derivoituva kohdassa $y$ ja $f'(y)\ne0$, niin $(f^{-1})'(x)=1/f'(y)$ paikallisesti kääntyvällä haaralla.
