# Ableitungstabelle

**Sprachen:** [en](../en/DERIVATIVE_TABLE.md) · [fr](../fr/DERIVATIVE_TABLE.md) · [de](DERIVATIVE_TABLE.md) · [it](../it/DERIVATIVE_TABLE.md) · [es](../es/DERIVATIVE_TABLE.md) · [pt](../pt/DERIVATIVE_TABLE.md) · [zh](../zh/DERIVATIVE_TABLE.md) · [ja](../ja/DERIVATIVE_TABLE.md) · [nb](../nb/DERIVATIVE_TABLE.md) · [ru](../ru/DERIVATIVE_TABLE.md) · [ko](../ko/DERIVATIVE_TABLE.md) · [fi](../fi/DERIVATIVE_TABLE.md) · [pl](../pl/DERIVATIVE_TABLE.md)

**Hier verwendete Einheiten (vor den Beispielen erklärt):** `s` — Sekunde; `mm` — Millimeter = 0.001 m; `mm/s` — Millimeter / Sekunde — lineare Geschwindigkeit; `mm/s²` — Millimeter / Sekunde² — Beschleunigung. [Einheitenverzeichnis](UNITS.md).

[Kursübersicht](README.md) · [Integraltabelle](INTEGRAL_TABLE.md) · [Grundlagen der Analysis](notes/00-calculus-foundations.md)

Wenn $u$ und $v$ von $x$ abhängen und $a$ konstant ist, bezeichnen Striche die Ableitung nach $x$. Winkel werden im Bogenmaß angegeben. Die Ableitung ist nur dort definiert, wo der entsprechende Grenzwert existiert. Für zusammengesetzte Funktionen gilt die Kettenregel (chain rule). Hier sind $u'=\frac{\mathrm{d}u}{\mathrm{d}x}$ und $v'=\frac{\mathrm{d}v}{\mathrm{d}x}$.

## Regeln

| Funktion | Ableitung | Bedingungen |
| --- | --- | --- |
| $c$ | $0$ | $c$ konstant |
| $x$ | $1$ | — |
| $x^n$ | $nx^{n-1}$ | reelles $n$; wo die Funktion definiert und differenzierbar ist |
| $u+v$ | $u'+v'$ | — |
| $au$ | $au'$ | $a$ konstant |
| $uv$ | $u'v+uv'$ | Produktregel |
| $\frac{u}{v}$ | $\frac{u'v-uv'}{v^2}$ | $v\ne0$ |
| $f(u)$ | $f'(u)u'$ | Kettenregel |
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

## Beispiele

**Kettenregel (chain rule):** Für $y=(3x^2+1)^4$ setzen wir $u=3x^2+1$. Dann gilt $u'=6x$ und

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=4u^3u'=24x(3x^2+1)^3.
$$

**Geschwindigkeit und Beschleunigung:** Für den Ort $x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2$ liefert die zeitliche Ableitung die Geschwindigkeit und deren Ableitung die Beschleunigung:

$$
v(t)=\frac{\mathrm{d}x}{\mathrm{d}t}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t,
$$

$$
a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=4\ \mathrm{mm/s^2}.
$$

Bei $t=2\ \mathrm{s}$ beträgt die Geschwindigkeit $11\ \mathrm{mm/s}$. Dies ist ein mathematisches Beispiel und keine Anweisung zur Maschinensteuerung.

**Umkehrfunktion (inverse function):** Wenn $y=f^{-1}(x)$ ist, $f$ an der Stelle $y$ differenzierbar ist und $f'(y)\ne0$ gilt, folgt $(f^{-1})'(x)=1/f'(y)$ auf einem lokal umkehrbaren Zweig.
