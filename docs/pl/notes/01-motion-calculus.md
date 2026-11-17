# 1. Ruch, pochodne i całki

**Języki:** [en](../../en/notes/01-motion-calculus.md) · [fr](../../fr/notes/01-motion-calculus.md) · [de](../../de/notes/01-motion-calculus.md) · [it](../../it/notes/01-motion-calculus.md) · [es](../../es/notes/01-motion-calculus.md) · [pt](../../pt/notes/01-motion-calculus.md) · [zh](../../zh/notes/01-motion-calculus.md) · [ja](../../ja/notes/01-motion-calculus.md) · [nb](../../nb/notes/01-motion-calculus.md) · [ru](../../ru/notes/01-motion-calculus.md) · [ko](../../ko/notes/01-motion-calculus.md) · [fi](../../fi/notes/01-motion-calculus.md) · [pl](01-motion-calculus.md)

**Jednostki tej lekcji (wyjaśnione przed przykładami):** `s` — sekunda; `mm` — milimetr; `mm/s` — milimetr na sekundę (prędkość liniowa); `mm/s²` — milimetr na sekundę do kwadratu (przyspieszenie); `%` — procent (jedna setna). [Pełny słownik jednostek](../UNITS.md).

**Przypomnienie matematyki:** [0. Podstawy analizy: pochodne, różniczki i całki](00-calculus-foundations.md) · [Tablica całek](../INTEGRAL_TABLE.md)


[Spis treści](../README.md) · [Ściąga ze wzorami](../CHEATSHEET.md) · [Ćwiczenia](../exercises/README.md) · [Następna lekcja](02-first-order-dynamics.md)

> **Uwaga o dokładności:** to uproszczony model jednowymiarowy. Przed jego adaptacją sprawdzaj jednostki, zwroty osi i błędy numeryczne.

## Krótkie przypomnienie

- **Droga** to całkowita długość toru; **przemieszczenie** to różnica między położeniem końcowym i początkowym.
- **Szybkość (speed)** jest nieujemna; **prędkość ze znakiem (velocity)** uwzględnia kierunek i na wybranej osi może być ujemna.
- Pochodna położenia po czasie daje prędkość chwilową. Całkowanie prędkości ze znakiem daje przemieszczenie.
- **Jawna metoda Eulera (explicit Euler)** przybliża zmianę wielkości, uznając jej pochodną za stałą na krótkim kroku.

## Na tej stronie

- [1. Droga, przemieszczenie, szybkość i prędkość](#section-1)
- [2. Pochodna: prędkość chwilowa](#section-2)
- [3. Całka: przemieszczenie i droga](#section-3)
- [4. Całkowanie numeryczne](#section-4)
- [5. Ćwiczenia](#section-5)
- [6. Dodatkowe wyjaśnienia (opcjonalnie)](#section-6)
  - [Dlaczego pochodna 2t² to 4t](#power-rule-derivation)
  - [Skąd pochodzą wyniki tabeli przemieszczenia](#motion-values-derivation)

[Jednostki SI i separator dziesiętny](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Droga, przemieszczenie, szybkość i prędkość

Wyprowadzenia, jednostki i ograniczenia numeryczne opisano w [dodatkowych wyjaśnieniach](#section-6).

Rozważmy wirtualną oś poruszającą się przez 2 sekundy z prędkością $+3\ \mathrm{mm/s}$, a przez kolejne 2 sekundy z $-3\ \mathrm{mm/s}$. Jej przemieszczenie wynosi $+6-6=0\ \mathrm{mm}$, ale przebyta droga to $6+6=12\ \mathrm{mm}$. Szybkość w obu etapach wynosi $3\ \mathrm{mm/s}$; znak prędkości określa zwrot.

Dla przedziału czasu $[t_1,t_2]$:

$$
\text{average velocity}=\frac{x(t_2)-x(t_1)}{t_2-t_1},\qquad
\text{average speed}=\frac{\text{total distance traveled}}{t_2-t_1}.
$$

W dwóch i trzech wymiarach prędkość jest wektorem. Obiekt krążący po okręgu ze stałą szybkością stale zmienia wektor prędkości, ponieważ zmienia kierunek. Po pełnym okrążeniu średnia prędkość wektorowa jest zerowa, jeżeli obiekt wrócił do punktu wyjścia.

Na **całym czterosekundowym odcinku** średnia prędkość ze znakiem i średnia szybkość są **różne**: oś wraca do położenia początkowego, ale przebywa 12 mm.

$$
\overline{v}_x=\frac{0\ \mathrm{mm}}{4\ \mathrm{s}}=0\ \mathrm{mm/s}
$$

$$
\overline{\lvert v\rvert}=\frac{12\ \mathrm{mm}}{4\ \mathrm{s}}=3\ \mathrm{mm/s}
$$

**Średnia szybkość nie musi być wartością bezwzględną średniej prędkości.** Podobnie po pełnym okrążeniu średni wektor prędkości jest zerowy, choć droga i szybkość średnia są dodatnie.

<a id="section-2"></a>

## 2. Pochodna: prędkość chwilowa

Dla różniczkowalnej funkcji położenia $x(t)$:

$$
v(t)=\frac{dx}{dt}.
$$

Jeśli $x(t)=2t^2\ \mathrm{mm}$, a czas $t$ jest liczony w sekundach, wtedy $v(t)=4t\ \mathrm{mm/s}$. **Skąd 4?** Z reguły potęgowej $d(t^2)/dt=2t$, więc pochodna $2t^2$ wynosi $2\cdot2t=4t$. [Pełne wyprowadzenie z jednostkami](#power-rule-derivation). W chwili $t=1\ \mathrm{s}$ prędkość wynosi $4\ \mathrm{mm/s}$.

Przybliżenie pochodnej różnicą w przód (forward finite difference) ma postać:

$$
v(t)\approx\frac{x(t+\Delta t)-x(t)}{\Delta t}.
$$

Przy $t=1\ \mathrm{s}$ kroki $\Delta t=1; 0.1; 0.01\ \mathrm{s}$ dają odpowiednio $6; 4.2; 4.02\ \mathrm{mm/s}$. Malejący krok zbliża wynik do pochodnej, ale w końcu dokładność ogranicza zaokrąglanie liczb zmiennoprzecinkowych.

**Dlaczego zbyt mały krok zawodzi:** dla $t=1\ \mathrm{s}$ rzeczywista pochodna $x(t)=2t^2$ wynosi $4\ \mathrm{mm/s}$. Przy `dt = 1e-17` zwykłe obliczenia zmiennoprzecinkowe Pythona zaokrąglają `t + dt` do tej samej liczby `t`. Oba położenia są wtedy identyczne, co dałoby fałszywą prędkość zero. W innych skalach wartości mogą zaniknąć numerycznie (underflow). Funkcja [`forward_derivative`](../../../exercises/01_motion_and_integral.py) odrzuca takie przypadki przez `ValueError` zamiast zwracać błędne zero. Oblicza nadal rzeczywistą różnicę skończoną; wybieraj rozróżnialny krok, a nie najmniejszy możliwy.

<a id="section-3"></a>

## 3. Całka: przemieszczenie i droga

Dla jednowymiarowej prędkości ze znakiem $v(t)$:

$$
x(t_2)-x(t_1)=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t,\qquad
s=\int_{t_1}^{t_2}|v(t)|\ \mathrm{d}t.
$$

Pierwsza całka może być ujemna lub zerowa, druga nigdy nie jest ujemna. Geometria całki odpowiada polu ze znakiem pod wykresem prędkości od czasu. **To niezależny przykład od sekcji 2:** wcześniejsze $x(t)=2t^2$ ma pochodną $v(t)=4t$, natomiast tutaj do całkowania celowo używamy $v(t)=2t$. Odpowiada mu położenie $x(t)=t^2+C$ (z właściwymi jednostkami). Gdy $v(t)=2t\ \mathrm{mm/s}$ dla $0\le t\le2\ \mathrm{s}$, przemieszczenie wynosi $4\ \mathrm{mm}$.

<a id="section-4"></a>

## 4. Całkowanie numeryczne

Dokładne przemieszczenie i przybliżenie metodą Eulera z lewym punktem przedziału (dane syntetyczne).

![Przemieszczenie dokładne i przybliżone metodą Eulera z lewego końca kroku.](../../../assets/figures/euler_vs_exact.svg)

Jawna metoda Eulera bierze pochodną **na początku** przedziału:

$$
x_{n+1}=x_n+v(t_n)\ \Delta t.
$$

Dla $v(t)=2t\ \mathrm{mm/s}$ od $t=0$ do $2\ \mathrm{s}$:

| Krok czasu $\Delta t$ | Przemieszczenie Eulera |
| ---: | ---: |
| $0.5\ \mathrm{s}$ | $3.000\ \mathrm{mm}$ |
| $0.1\ \mathrm{s}$ | $3.800\ \mathrm{mm}$ |
| $0.01\ \mathrm{s}$ | $3.980\ \mathrm{mm}$ |
| Dokładna całka | $4.000\ \mathrm{mm}$ |

Metoda Eulera zaniża wynik w tym przykładzie, ponieważ prędkość rośnie podczas każdego kroku. Reguła trapezów, wykorzystująca średnią wartości na obu końcach, daje dokładną całkę dla prędkości liniowej w czasie, ale nie dla dowolnej funkcji nieliniowej.


[Obliczenia prowadzące do wartości 3, 3.8 i 3.98](#motion-values-derivation).

<a id="section-5"></a>

## 5. Ćwiczenia

Uruchom [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py). Zmniejszaj $\Delta t$ i obserwuj zmianę wyniku. Następnie wyjaśnij, dlaczego droga powrotna może dać zerowe przemieszczenie, chociaż przebyta droga jest dodatnia.

Przykłady korzystają z danych syntetycznych i nie sterują rzeczywistym sprzętem.

<a id="section-6"></a>

## 6. Dodatkowe wyjaśnienia (opcjonalnie)

### Jednostki i znaczenie współczynników

Jeżeli czas $t$ jest liczony w sekundach, zapis $x(t)=2t^2$ milimetrów jest skrótem. Współczynnik ma wtedy wartość i jednostkę $2\ \mathrm{mm/s^2}$. Funkcja $v(t)=4t$ jest wyrażana w $\mathrm{mm/s}$. Zawsze sprawdzaj jednostki przed podstawieniem liczb do wzoru.

### Różnice skończone i błędy numeryczne

Różnica skończona przybliża pochodną na niezerowym kroku, a nie jej dokładną wartość chwilową. Mniejszy krok redukuje błąd obcięcia dla gładkich funkcji, ale bardzo mały krok nasila błędy odejmowania lub szum pomiaru. Metoda Eulera używa wartości na początku kroku; przy rosnącej liniowo prędkości zaniża całkę.

### Więcej niż jeden wymiar

Dla wektora położenia $\mathbf r(t)$ prędkość to $\mathbf v(t)=d\mathbf r/dt$. Szybkość to długość wektora $\|\mathbf v\|$, a droga $s=\int\|\mathbf v(t)\|dt$.


<a id="power-rule-derivation"></a>

### Dlaczego pochodna $2t^2$ to $4t$



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

### Skąd pochodzą wyniki tabeli przemieszczenia

$$
a=2\ \mathrm{mm/s^2},\qquad v(t)=at,\qquad 0\le t\le2\ \mathrm{s}.
$$

$$
\Delta x=\int_{0}^{2\ \mathrm{s}}at\ \mathrm{d}t
=\left[\frac{at^2}{2}\right]_{0}^{2\ \mathrm{s}}
=4\ \mathrm{mm}.
$$



Symbol $\sum$ (wielka grecka litera **sigma**, sumowanie) oznacza dodawanie kolejnych składników. W $\sum_{n=0}^{N-1}(2nh)h$ indeks $n$ przyjmuje $0; 1; \ldots; N-1$, co daje $N$ składników. Można to porównać do pętli Pythona `for`. Na przykład $\sum_{n=1}^{3}n=1+2+3=6$. [← Wyjaśnienie symboli](../SYMBOLS.md#summation).

$$
h=\frac{dt}{1\ \mathrm{s}},\qquad N=\frac{2}{h}.
$$

$$
x_{\mathrm{Euler}}(2\ \mathrm{s})
=\left[\sum_{n=0}^{N-1}(2nh)h\right]\ \mathrm{mm}
=\left[h^2N(N-1)\right]\ \mathrm{mm}
=(4-2h)\ \mathrm{mm}.
$$

`h` jest liczbową wartością kroku `dt` w sekundach (np. `dt = 0.5 s` oznacza `h = 0.5`), a `N` — liczbą kroków. Wynik to **długość w milimetrach**, a nie liczba bezwymiarowa.



Dla kroków `dt = 0.5`, `0.1` i `0.01` s otrzymujemy `3`, `3.8` i `3.98` mm. Zakładamy, że bezwymiarowa liczba kroków $N=(2\ \mathrm{s})/dt$ jest całkowita.
