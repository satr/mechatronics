# Integraltafel

**Diese Seite auf:** [en](../en/INTEGRAL_TABLE.md) · [fr](../fr/INTEGRAL_TABLE.md) · [de](INTEGRAL_TABLE.md) · [it](../it/INTEGRAL_TABLE.md) · [es](../es/INTEGRAL_TABLE.md) · [pt](../pt/INTEGRAL_TABLE.md) · [zh](../zh/INTEGRAL_TABLE.md) · [ja](../ja/INTEGRAL_TABLE.md) · [nb](../nb/INTEGRAL_TABLE.md) · [ru](../ru/INTEGRAL_TABLE.md) · [ko](../ko/INTEGRAL_TABLE.md) · [fi](../fi/INTEGRAL_TABLE.md) · [pl](../pl/INTEGRAL_TABLE.md)

**Hier verwendete Einheiten (vor den Beispielen erklärt):** `s` — Sekunde; `mm` — Millimeter = 0.001 m; `mm/s` — Millimeter / Sekunde — lineare Geschwindigkeit; `mm/s²` — Millimeter / Sekunde² — Beschleunigung; `N` — Newton; `m` — Meter; `N/m` — Newton / Meter — Steifigkeit; `J` — Joule. [Einheitenverzeichnis](UNITS.md).

[README](README.md) · [0. Grundlagen von Ableitungen, Differentialen und Integralen](notes/00-calculus-foundations.md) · [Symbole](SYMBOLS.md)

Bei unbestimmten Integralen steht stets +C als Integrationskonstante. a ist konstant; die Formeln gelten auf Intervallen, in denen der Integrand definiert ist. Winkel werden in Radiant angegeben.

Zuerst Polynome üben; trigonometrische Integrale und Wurzelterme können später folgen.

## Inhalt

- [Potenzen und Logarithmus](#section-1)
- [Exponentialfunktionen](#section-2)
- [Trigonometrische Funktionen](#section-3)
- [Rationale Ausdrücke und inverse Trigonometrie](#section-4)
- [Weitere Formeln: Wurzeln und Kehrwerte](#section-5)
- [Formel wählen und Ergebnis prüfen](#section-6)

<a id="section-1"></a>
## 1. Potenzen und Logarithmus

| Formel | Voraussetzungen / Erläuterung |
| --- | --- |
| $\int 1\ \mathrm{d}x=x+C$ | alle reellen $x$ |
| $\int x^n\ \mathrm{d}x=\frac{x^{n+1}}{n+1}+C$ | $n\ne-1$; reellen Definitionsbereich der Potenz beachten |
| $\int\frac{1}{x}\ \mathrm{d}x=\ln\lvert x\rvert+C$ | $x\ne0$ |

<a id="section-2"></a>
## 2. Exponentialfunktionen

| Formel | Voraussetzungen / Erläuterung |
| --- | --- |
| $\int \mathrm{e}^{x}\ \mathrm{d}x=\mathrm{e}^{x}+C$ | alle reellen $x$ |
| $\int a^x\ \mathrm{d}x=\frac{a^x}{\ln a}+C$ | $a>0$, $a\ne1$ |

<a id="section-3"></a>
## 3. Trigonometrische Funktionen

| Formel | Voraussetzungen / Erläuterung |
| --- | --- |
| $\int\sin x\ \mathrm{d}x=-\cos x+C$ | $x$ im Bogenmaß |
| $\int\cos x\ \mathrm{d}x=\sin x+C$ | $x$ im Bogenmaß |
| $\int\frac{1}{\cos^2 x}\ \mathrm{d}x=\tan x+C$ | $\cos x\ne0$ |
| $\int\frac{1}{\sin^2 x}\ \mathrm{d}x=-\cot x+C$ | $\sin x\ne0$ |

<a id="section-4"></a>
## 4. Rationale Ausdrücke und inverse Trigonometrie

| Formel | Voraussetzungen / Erläuterung |
| --- | --- |
| $\int\frac{1}{1+x^2}\ \mathrm{d}x=\arctan x+C$ | alle reellen $x$ |
| $\int\frac{1}{\sqrt{1-x^2}}\ \mathrm{d}x=\arcsin x+C$ | $\lvert x\rvert<1$ |
| $\int\frac{1}{a^2+x^2}\ \mathrm{d}x=\frac{1}{a}\arctan\frac{x}{a}+C$ | $a>0$ |
| $\int\frac{1}{a^2-x^2}\ \mathrm{d}x=\frac{1}{2a}\ln\left\lvert\frac{a+x}{a-x}\right\rvert+C$ | $a>0$, $x\ne\pm a$ |
| $\int\frac{1}{\sqrt{a^2-x^2}}\ \mathrm{d}x=\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |

<a id="section-5"></a>
## 5. Weitere Formeln: Wurzeln und Kehrwerte

| Formel | Voraussetzungen / Erläuterung |
| --- | --- |
| $\int\frac{1}{\sqrt{x^2+a^2}}\ \mathrm{d}x=\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{a^2-x^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{a^2-x^2}+\frac{a^2}{2}\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |
| $\int\sqrt{x^2+a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2+a^2}+\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{x^2-a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2-a^2}-\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2-a^2}\right\rvert+C$ | $a>0$, $\lvert x\rvert>a$ |
| $\int\frac{1}{\sin x}\ \mathrm{d}x=\ln\left\lvert\tan\frac{x}{2}\right\rvert+C$ | $\sin x\ne0$; Intervalle ohne Polstellen |
| $\int\frac{1}{\cos x}\ \mathrm{d}x=\ln\left\lvert\tan\left(\frac{x}{2}+\frac{\pi}{4}\right)\right\rvert+C$ | $\cos x\ne0$; Intervalle ohne Polstellen |

## Formel prüfen

Zur Prüfung die rechte Seite ableiten. Bei Potenzen wird die Potenzregel umgekehrt angewandt.

Logarithmen benötigen dimensionslose Argumente; x wird hier ohne andere Angabe als dimensionslos behandelt. Vorzeichen und Definitionsbereiche sind zu beachten.

<a id="section-6"></a>
## 6. Formel wählen und Ergebnis prüfen

Bestimmen Sie zuerst die Integrationsvariable hinter dem Differential (dx, dt oder dθ). Ein Koeffizient ist nur dann konstant, wenn er von dieser Variablen unabhängig ist. Bei unbestimmten Integralen C addieren, bei bestimmten F(b) − F(a) berechnen. Durch Ableiten prüfen.

### Beispiel A — Wegänderung aus Geschwindigkeit

Für v(t) = 3 mm/s + (4 mm/s²)t von 0 bis 2 s jeden Term integrieren:

$$
\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}
=14\ \mathrm{mm}.
$$

Ergebnis 14 mm, nicht 14 mm/s: Das Zeitintegral der Geschwindigkeit ist eine Wegänderung.

### Beispiel B — Arbeit einer veränderlichen Kraft

Eine Feder F(x) = kx mit k = 200 N/m wird von 0 bis 0.01 m gedehnt:

$$
\int_0^{0.01\ \mathrm{m}}(200\ \mathrm{N/m})x\ \mathrm{d}x
=\left[(100\ \mathrm{N/m})x^2\right]_0^{0.01\ \mathrm{m}}=0.01\ \mathrm{J}.
$$

Es ergeben sich 0.01 J. Die Endkraft mit dem Gesamtweg zu multiplizieren wäre falsch.

### Beispiel C — Logarithmus einer einfachen Funktion

Eine Stammfunktion von 1/x ist ln|x|. Für dimensionsloses x von 1 bis 2:

$$
\int_1^2\frac1x\ \mathrm{d}x=[\ln x]_1^2=\ln2-\ln1=\ln2\approx0.693.
$$

Das Ergebnis ist ln 2 ≈ 0.693. x ist ein Verhältnis, keine Länge.
