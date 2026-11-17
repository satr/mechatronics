# Tablica całek

**Języki:** [en](../en/INTEGRAL_TABLE.md) · [fr](../fr/INTEGRAL_TABLE.md) · [de](../de/INTEGRAL_TABLE.md) · [it](../it/INTEGRAL_TABLE.md) · [es](../es/INTEGRAL_TABLE.md) · [pt](../pt/INTEGRAL_TABLE.md) · [zh](../zh/INTEGRAL_TABLE.md) · [ja](../ja/INTEGRAL_TABLE.md) · [nb](../nb/INTEGRAL_TABLE.md) · [ru](../ru/INTEGRAL_TABLE.md) · [ko](../ko/INTEGRAL_TABLE.md) · [fi](../fi/INTEGRAL_TABLE.md) · [pl](INTEGRAL_TABLE.md)

**Jednostki w tej części (wyjaśnione przed przykładami):** `s` — sekunda; `mm` — milimetr = 0.001 m; `mm/s` — milimetr na sekundę — prędkość liniowa; `mm/s²` — milimetr na sekundę do kwadratu — przyspieszenie; `N` — niuton — siła; `m` — metr; `N/m` — niuton na metr — sztywność sprężyny; `J` — dżul — energia i praca. [Słownik jednostek](UNITS.md).

[Spis treści](README.md) · [0. Podstawy analizy: pochodne i całki](notes/00-calculus-foundations.md) · [Symbole](SYMBOLS.md) · [Trygonometria](TRIGONOMETRY.md)

W każdej całce nieoznaczonej występuje $+C$, czyli stała całkowania. Parametr $a$ jest stały, a wzory stosujemy na przedziałach, gdzie funkcje podcałkowe są określone. Argumenty trygonometryczne podajemy w radianach.

Zacznij od całek funkcji potęgowych. Wzory trygonometryczne, odwrotne i z pierwiastkami są materiałem dodatkowym.

## Spis treści

- [Potęgi i logarytmy](#section-1)
- [Funkcje wykładnicze](#section-2)
- [Funkcje trygonometryczne](#section-3)
- [Funkcje wymierne i odwrotne trygonometryczne](#section-4)
- [Dodatkowe wzory: pierwiastki i odwrotności](#section-5)
- [Jak dobrać i sprawdzić wzór](#section-6)

<a id="section-1"></a>
## 1. Potęgi i logarytmy

| Wzór | Warunki / znaczenie |
| --- | --- |
| $\int 1\ \mathrm{d}x=x+C$ | dowolne rzeczywiste $x$ |
| $\int x^n\ \mathrm{d}x=\frac{x^{n+1}}{n+1}+C$ | $n\ne-1$; potęgi rzeczywiste tylko w swojej dziedzinie |
| $\int\frac{1}{x}\ \mathrm{d}x=\ln\lvert x\rvert+C$ | $x\ne0$ |

<a id="section-2"></a>
## 2. Funkcje wykładnicze

| Wzór | Warunki / znaczenie |
| --- | --- |
| $\int \mathrm{e}^{x}\ \mathrm{d}x=\mathrm{e}^{x}+C$ | dowolne rzeczywiste $x$ |
| $\int a^x\ \mathrm{d}x=\frac{a^x}{\ln a}+C$ | $a>0$, $a\ne1$ |

<a id="section-3"></a>
## 3. Funkcje trygonometryczne

| Wzór | Warunki / znaczenie |
| --- | --- |
| $\int\sin x\ \mathrm{d}x=-\cos x+C$ | $x$ wyrażony w radianach |
| $\int\cos x\ \mathrm{d}x=\sin x+C$ | $x$ wyrażony w radianach |
| $\int\frac{1}{\cos^2 x}\ \mathrm{d}x=\tan x+C$ | $\cos x\ne0$ |
| $\int\frac{1}{\sin^2 x}\ \mathrm{d}x=-\cot x+C$ | $\sin x\ne0$ |

<a id="section-4"></a>
## 4. Funkcje wymierne i odwrotne trygonometryczne

| Wzór | Warunki / znaczenie |
| --- | --- |
| $\int\frac{1}{1+x^2}\ \mathrm{d}x=\arctan x+C$ | dowolne rzeczywiste $x$ |
| $\int\frac{1}{\sqrt{1-x^2}}\ \mathrm{d}x=\arcsin x+C$ | $\lvert x\rvert<1$ |
| $\int\frac{1}{a^2+x^2}\ \mathrm{d}x=\frac{1}{a}\arctan\frac{x}{a}+C$ | $a>0$ |
| $\int\frac{1}{a^2-x^2}\ \mathrm{d}x=\frac{1}{2a}\ln\left\lvert\frac{a+x}{a-x}\right\rvert+C$ | $a>0$, $x\ne\pm a$ |
| $\int\frac{1}{\sqrt{a^2-x^2}}\ \mathrm{d}x=\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |

<a id="section-5"></a>
## 5. Dodatkowe wzory: pierwiastki i odwrotności

| Wzór | Warunki / znaczenie |
| --- | --- |
| $\int\frac{1}{\sqrt{x^2+a^2}}\ \mathrm{d}x=\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{a^2-x^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{a^2-x^2}+\frac{a^2}{2}\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |
| $\int\sqrt{x^2+a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2+a^2}+\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{x^2-a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2-a^2}-\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2-a^2}\right\rvert+C$ | $a>0$, $\lvert x\rvert>a$ |
| $\int\frac{1}{\sin x}\ \mathrm{d}x=\ln\left\lvert\tan\frac{x}{2}\right\rvert+C$ | $\sin x\ne0$; na przedziałach nieprzecinających biegunów |
| $\int\frac{1}{\cos x}\ \mathrm{d}x=\ln\left\lvert\tan\left(\frac{x}{2}+\frac{\pi}{4}\right)\right\rvert+C$ | $\cos x\ne0$; na przedziałach nieprzecinających biegunów |

## Sposób sprawdzania wzorów

Różniczkuj prawą stronę każdego wzoru i porównaj z funkcją podcałkową. Dla prostej potęgi wykonaj działanie odwrotne oraz sprawdź wykładnik i współczynnik.

Logarytm wielkości mającej jednostkę wymaga wcześniej podzielenia jej przez wielkość odniesienia o tej samej jednostce. Wzory z logarytmem zakładają bezwymiarowe $x$ lub podanie skali odniesienia. Przestrzegaj dziedziny rzeczywistej.

<a id="section-6"></a>
## 6. Jak dobrać i sprawdzić wzór

Najpierw ustal zmienną całkowania po różniczce (np. $\mathrm{d}x$, $\mathrm{d}t$ lub $\mathrm{d}\theta$). Traktuj współczynnik jako stały tylko wtedy, gdy rzeczywiście nie zależy od tej zmiennej. Przy całce nieoznaczonej dodaj $C$. Przy oznaczonej znajdź funkcję pierwotną $F$ i policz $F(b)-F(a)$. Na końcu sprawdź wynik przez różniczkowanie.

### Rozwiązany przykład A — przemieszczenie z pomierzonej prędkości

Dla prostego modelu osi z $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$ w przedziale $0$–$2\ \mathrm{s}$ całkujemy każdy składnik:

$$
\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}
=14\ \mathrm{mm}.
$$

Wynik to $14\ \mathrm{mm}$, a nie $14\ \mathrm{mm/s}$. Całka z prędkości po czasie daje przemieszczenie.

### Rozwiązany przykład B — praca siły rosnącej liniowo

Dla sprężyny $F(x)=kx$, gdzie $k=200\ \mathrm{N/m}$, rozciąganej od $0$ do $0.01\ \mathrm{m}$:

$$
\int_0^{0.01\ \mathrm{m}}(200\ \mathrm{N/m})x\ \mathrm{d}x
=\left[(100\ \mathrm{N/m})x^2\right]_0^{0.01\ \mathrm{m}}=0.01\ \mathrm{J}.
$$

Otrzymujemy $0.01\ \mathrm{J}$. Całka z siły po drodze to praca mechaniczna; pomnożenie samej siły końcowej przez całą odległość dałoby zbyt duży wynik.

### Rozwiązany przykład C — logarytm z prostego prawa szybkości zmian

Funkcją pierwotną dla $1/x$ jest $\ln|x|$. Niech bezwymiarowy stosunek $x$ zmienia się od $1$ do $2$:

$$
\int_1^2\frac1x\ \mathrm{d}x=[\ln x]_1^2=\ln2-\ln1=\ln2\approx0.693.
$$

Wynik wynosi $\ln2\approx0.693$. Nie jest to logarytm długości w metrach: zmienna $x$ jest bezwymiarowa.
