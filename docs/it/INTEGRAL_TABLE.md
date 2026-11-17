# Tabella degli integrali

**Leggi in:** [en](../en/INTEGRAL_TABLE.md) · [fr](../fr/INTEGRAL_TABLE.md) · [de](../de/INTEGRAL_TABLE.md) · [it](INTEGRAL_TABLE.md) · [es](../es/INTEGRAL_TABLE.md) · [pt](../pt/INTEGRAL_TABLE.md) · [zh](../zh/INTEGRAL_TABLE.md) · [ja](../ja/INTEGRAL_TABLE.md) · [nb](../nb/INTEGRAL_TABLE.md) · [ru](../ru/INTEGRAL_TABLE.md) · [ko](../ko/INTEGRAL_TABLE.md) · [fi](../fi/INTEGRAL_TABLE.md) · [pl](../pl/INTEGRAL_TABLE.md)

**Unità usate qui (spiegate prima degli esempi):** `s` — secondo; `mm` — millimetro = 0.001 m; `mm/s` — millimetro / secondo — velocità lineare; `mm/s²` — millimetro / secondo² — accelerazione; `N` — newton; `m` — metro; `N/m` — newton / metro — rigidezza; `J` — joule. [Glossario delle unità](UNITS.md).

[README](README.md) · [0. Fondamenti di derivate, differenziali e integrali](notes/00-calculus-foundations.md) · [Simboli](SYMBOLS.md)

Ogni integrale indefinito include +C, la costante di integrazione. Il parametro a è costante; si considera un intervallo dove l’integranda è definita. Gli angoli sono in radianti.

Inizia dai polinomi; gli integrali trigonometrici e con radicali sono facoltativi all’inizio.

## Indice

- [Potenze e logaritmi](#section-1)
- [Funzioni esponenziali](#section-2)
- [Funzioni trigonometriche](#section-3)
- [Forme razionali e funzioni trigonometriche inverse](#section-4)
- [Approfondimento: radicali e reciproci](#section-5)
- [Scegliere e verificare una formula](#section-6)

<a id="section-1"></a>
## 1. Potenze e logaritmi

| Formula | Condizioni / spiegazioni |
| --- | --- |
| $\int 1\ \mathrm{d}x=x+C$ | tutti gli $x$ reali |
| $\int x^n\ \mathrm{d}x=\frac{x^{n+1}}{n+1}+C$ | $n\ne-1$; rispettare il dominio reale della potenza |
| $\int\frac{1}{x}\ \mathrm{d}x=\ln\lvert x\rvert+C$ | $x\ne0$ |

<a id="section-2"></a>
## 2. Funzioni esponenziali

| Formula | Condizioni / spiegazioni |
| --- | --- |
| $\int \mathrm{e}^{x}\ \mathrm{d}x=\mathrm{e}^{x}+C$ | tutti gli $x$ reali |
| $\int a^x\ \mathrm{d}x=\frac{a^x}{\ln a}+C$ | $a>0$, $a\ne1$ |

<a id="section-3"></a>
## 3. Funzioni trigonometriche

| Formula | Condizioni / spiegazioni |
| --- | --- |
| $\int\sin x\ \mathrm{d}x=-\cos x+C$ | $x$ in radianti |
| $\int\cos x\ \mathrm{d}x=\sin x+C$ | $x$ in radianti |
| $\int\frac{1}{\cos^2 x}\ \mathrm{d}x=\tan x+C$ | $\cos x\ne0$ |
| $\int\frac{1}{\sin^2 x}\ \mathrm{d}x=-\cot x+C$ | $\sin x\ne0$ |

<a id="section-4"></a>
## 4. Forme razionali e funzioni trigonometriche inverse

| Formula | Condizioni / spiegazioni |
| --- | --- |
| $\int\frac{1}{1+x^2}\ \mathrm{d}x=\arctan x+C$ | tutti gli $x$ reali |
| $\int\frac{1}{\sqrt{1-x^2}}\ \mathrm{d}x=\arcsin x+C$ | $\lvert x\rvert<1$ |
| $\int\frac{1}{a^2+x^2}\ \mathrm{d}x=\frac{1}{a}\arctan\frac{x}{a}+C$ | $a>0$ |
| $\int\frac{1}{a^2-x^2}\ \mathrm{d}x=\frac{1}{2a}\ln\left\lvert\frac{a+x}{a-x}\right\rvert+C$ | $a>0$, $x\ne\pm a$ |
| $\int\frac{1}{\sqrt{a^2-x^2}}\ \mathrm{d}x=\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |

<a id="section-5"></a>
## 5. Approfondimento: radicali e reciproci

| Formula | Condizioni / spiegazioni |
| --- | --- |
| $\int\frac{1}{\sqrt{x^2+a^2}}\ \mathrm{d}x=\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{a^2-x^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{a^2-x^2}+\frac{a^2}{2}\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |
| $\int\sqrt{x^2+a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2+a^2}+\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{x^2-a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2-a^2}-\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2-a^2}\right\rvert+C$ | $a>0$, $\lvert x\rvert>a$ |
| $\int\frac{1}{\sin x}\ \mathrm{d}x=\ln\left\lvert\tan\frac{x}{2}\right\rvert+C$ | $\sin x\ne0$; intervalli senza singolarità |
| $\int\frac{1}{\cos x}\ \mathrm{d}x=\ln\left\lvert\tan\left(\frac{x}{2}+\frac{\pi}{4}\right)\right\rvert+C$ | $\cos x\ne0$; intervalli senza singolarità |

## Verificare una formula

Deriva il risultato per verificare ogni formula. Per le potenze, usa al contrario la regola di derivazione.

L’argomento del logaritmo deve essere adimensionale; qui x è adimensionale salvo una scala specificata. Rispetta segni e domini.

<a id="section-6"></a>
## 6. Scegliere e verificare una formula

Identificare la variabile dopo il differenziale (dx, dt o dθ). Un coefficiente è costante solo se non dipende da quella variabile. Negli integrali indefiniti aggiungere C, in quelli definiti calcolare F(b) − F(a). Verificare derivando.

### Esempio A — spostamento dalla velocità

Per v(t) = 3 mm/s + (4 mm/s²)t da 0 a 2 s, integriamo ogni termine:

$$
\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}
=14\ \mathrm{mm}.
$$

Risulta 14 mm, non 14 mm/s: la velocità integrata nel tempo è lo spostamento.

### Esempio B — lavoro di una forza variabile

Per una molla F(x) = kx con k = 200 N/m, estesa da 0 a 0.01 m:

$$
\int_0^{0.01\ \mathrm{m}}(200\ \mathrm{N/m})x\ \mathrm{d}x
=\left[(100\ \mathrm{N/m})x^2\right]_0^{0.01\ \mathrm{m}}=0.01\ \mathrm{J}.
$$

Il lavoro è 0.01 J. Non si deve moltiplicare la forza finale per tutto il percorso.

### Esempio C — logaritmo da una legge semplice

Una primitiva di 1/x è ln|x|. Per x adimensionale da 1 a 2:

$$
\int_1^2\frac1x\ \mathrm{d}x=[\ln x]_1^2=\ln2-\ln1=\ln2\approx0.693.
$$

Il risultato è ln 2 ≈ 0.693. x è un rapporto, non una lunghezza.
