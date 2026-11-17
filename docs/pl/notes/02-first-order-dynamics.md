# 2. Dynamika pierwszego rzędu, moment siły i energia ruchu obrotowego

**Języki:** [en](../../en/notes/02-first-order-dynamics.md) · [fr](../../fr/notes/02-first-order-dynamics.md) · [de](../../de/notes/02-first-order-dynamics.md) · [it](../../it/notes/02-first-order-dynamics.md) · [es](../../es/notes/02-first-order-dynamics.md) · [pt](../../pt/notes/02-first-order-dynamics.md) · [zh](../../zh/notes/02-first-order-dynamics.md) · [ja](../../ja/notes/02-first-order-dynamics.md) · [nb](../../nb/notes/02-first-order-dynamics.md) · [ru](../../ru/notes/02-first-order-dynamics.md) · [ko](../../ko/notes/02-first-order-dynamics.md) · [fi](../../fi/notes/02-first-order-dynamics.md) · [pl](02-first-order-dynamics.md)

**Jednostki tej lekcji (przed przykładami):** `s` — sekunda; `mm/s` — milimetr na sekundę (prędkość liniowa); `kg` — kilogram; `m` — metr; `rad/s` — radian na sekundę (prędkość kątowa); `N` — niuton; `N·m` — niutonometr (moment siły); `J` — dżul (energia); `rpm` — obroty na minutę, jednostka spoza SI; `kg·m²` — moment bezwładności; `N·m·s/rad` — współczynnik momentu względem prędkości kątowej; `%` — procent; `rad` — radian. [Pełny słownik jednostek](../UNITS.md).

**Przypomnienie matematyki:** [0. Podstawy pochodnych i całek](00-calculus-foundations.md) · [Tablica całek](../INTEGRAL_TABLE.md)


[Spis treści](../README.md) · [Ściąga](../CHEATSHEET.md) · [Ćwiczenia](../exercises/README.md) · [Poprzednia lekcja](01-motion-calculus.md)

> **Ostrzeżenie o dokładności:** poniższy model silnika zakłada idealny moment proporcjonalny do błędu prędkości. Pomija obciążenia, tarcie, opóźnienia, ograniczenia napięcia, nasycenie i dynamikę wyższych rzędów. Nie jest uniwersalnym modelem silników.

## Krótkie przypomnienie

- **Stała czasowa (time constant)** $\tau$ mówi, jak szybko układ pierwszego rzędu zbliża się do nowej równowagi.
- Numeryczny krok czasu `dt` wpływa na wynik przybliżenia, lecz **nie zmienia** fizycznej stałej $\tau$ modelu.
- Dla jednego wyidealizowanego układu obrotowego $\tau=\frac{J}{K}$, gdzie $J$ jest momentem bezwładności wirnika, a $K$ współczynnikiem momentu względem błędu prędkości.
- Dwie pary $J,K$ o takim samym ilorazie $J/K$ mogą dać podobną odpowiedź prędkości, lecz wymagać różnych momentów i energii mechanicznych.

## Na tej stronie

- [1. Odpowiedź prędkości układu pierwszego rzędu](#section-1)
- [2. Od czego zależy stała czasowa?](#section-2)
- [3. Krok numeryczny a stała czasowa](#section-3)
- [4. Wyznaczanie stałej czasowej z pomiarów](#section-4)
- [5. Moment siły i energia ruchu obrotowego](#section-5)
- [6. Ćwiczenia](#section-6)
- [7. Dodatkowe wyjaśnienia (opcjonalne)](#section-7)
  - [Skąd pochodzą 63.2 %, 86.5 % i 95.0 %](#time-constant-derivation)
  - [Obliczenie wyników metody Eulera](#euler-values-derivation)

[Jednostki SI i separator dziesiętny](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Odpowiedź prędkości układu pierwszego rzędu

Wyprowadzenie, jednostki i ograniczenia numeryczne znajdziesz w [części dodatkowej](#section-7).

Niech $u$ oznacza stałą prędkość docelową, $v$ prędkość rzeczywistą, a $\tau>0$ stałą czasową. Rozważamy równanie:

**Oznaczenia:** $\varepsilon(t)=u-v(t)$ to błąd prędkości (grecka litera epsilon). Funkcja wykładnicza ma postać $\exp(z)=\mathrm{e}^{z}$, gdzie $\mathrm{e}\approx2.71828$ jest **liczbą Eulera**, a nie błędem. Celowo stosujemy inne symbole. [Wyprowadzenie i skąd 63.2 %](#time-constant-derivation).

$$
\frac{dv}{dt}=\frac{u-v}{\tau}.
$$

Przy stałym $u$ i prędkości początkowej $v_0$ rozwiązanie dokładne brzmi:

$$
v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right).
$$

Po jednej stałej czasowej układ wykonuje $1-\exp(-1)\approx63.2\ \%$ zmiany między wartością początkową i końcową; po dwóch $86.5\ \%$, po trzech $95.0\ \%$. Jeśli $\tau=2\ \mathrm{s}$, w ciągu 2 s układ realizuje około 63.2 % **zmiany**, a nie osiąga już dokładnie wartości docelowej.

[Dlaczego takie procenty? Pełne obliczenie](#time-constant-derivation).

![Znormalizowana odpowiedź skokowa układu pierwszego rzędu: każda stała czasowa usuwa około 63.2 % pozostałego błędu.](../../../assets/figures/first_order_response.svg)

<a id="section-2"></a>

## 2. Od czego zależy stała czasowa?

Dla silnie uproszczonego układu obrotowego druga zasada dynamiki Newtona ma postać:

$$
J\frac{d\omega}{dt}=M,
$$

Tutaj $J$ to moment bezwładności ($\mathrm{kg}\cdot\mathrm{m}^2$), $\omega$ to prędkość kątowa ($\mathrm{rad/s}$), a $M$ to **wypadkowy fizyczny moment siły** ($\mathrm{N}\cdot\mathrm{m}$). Regulator oblicza polecenie dla napędu, natomiast silnik wytwarza moment fizyczny. Nie należy mówić, że sam program wytwarza moment.

Zakładamy, że silnik i napęd mogą wytwarzać moment proporcjonalny do błędu prędkości:

$$
M=K(u-\omega).
$$

W tym przykładzie obrotowym $u$ jest **docelową prędkością kątową** w rad/s, a nie liniową prędkością w mm/s z sekcji 1. Jednostki $u$ i $\omega$ muszą być takie same, inaczej odejmowanie $u-\omega$ i prawo momentu są wymiarowo błędne.

Współczynnik $K$ opisuje stosunek momentu do błędu prędkości i ma jednostkę $\mathrm{N}\cdot\mathrm{m}\cdot\mathrm{s}/\mathrm{rad}$. Przy podanych założeniach:

$$
\frac{d\omega}{dt}=\frac{K}{J}(u-\omega),\qquad
\tau=\frac{J}{K}.
$$

Podwojenie $J$ przy niezmienionym $K$ podwaja $\tau$ i zmniejsza przyspieszenie przy tym samym błędzie prędkości. Podwojenie zarówno $J$, jak i $K$ zachowuje $\tau$, ale przy tym samym błędzie wymagany moment jest dwukrotnie większy. $J$ **nie jest** siłą tarcia, lecz opisuje opór wobec zmiany prędkości kątowej. Modele rzeczywiste wymagają nieraz obciążenia, tarcia, dynamiki elektrycznej, ograniczeń prądu i kolejnych zmiennych stanu.

Symboliczna pętla sprzężenia zwrotnego modelu idealnego. Regulator wysyła polecenie do napędu; silnik, a nie oprogramowanie, wytwarza moment.

![Schemat pętli sprzężenia zwrotnego. Regulator steruje napędem, a silnik generuje fizyczny moment.](../../../assets/figures/control_loop.svg)

<a id="section-3"></a>

## 3. Krok numeryczny a stała czasowa

Zastosowanie jawnej metody Eulera do równania pierwszego rzędu daje:

$$
v_{n+1}=v_n+\frac{u-v_n}{\tau}\ dt.
$$

Dla $u=10\ \mathrm{mm/s}$, $v_0=0$ i $\tau=1\ \mathrm{s}$ obliczmy prędkość po jednej sekundzie:

| Metoda | $v(1\ \mathrm{s})$ |
| --- | ---: |
| Euler, $dt=0.1\ \mathrm{s}$ | $6.513\ \mathrm{mm/s}$ |
| Euler, $dt=0.01\ \mathrm{s}$ | $6.340\ \mathrm{mm/s}$ |
| Rozwiązanie dokładne | $6.321\ \mathrm{mm/s}$ |

Zmiana `dt` zmienia częstotliwość obliczeń, a nie przyspiesza fizycznego silnika w modelu. Stabilność i dokładność zależą od stosunku `dt` do $\tau$ i użytej metody numerycznej.

[Jak otrzymano wartości w tabeli?](#euler-values-derivation).

<a id="section-4"></a>

## 4. Wyznaczanie stałej czasowej z danych

Jeśli po skoku od 0 do $1000\ \mathrm{rpm}$ prędkość osiąga około $632\ \mathrm{rpm}$ w chwili $t=2\ \mathrm{s}$, wskazuje to na $\tau\approx2\ \mathrm{s}$ w czystym modelu pierwszego rzędu. Używaj 63.2 % **zmiany od wartości początkowej do końcowej**, nie zawsze 63.2 % wartości polecenia. Pomiary rzeczywiste mogą zawierać szum, błąd próbkowania, opóźnienie i przeregulowanie.

**Co rzeczywiście zwraca funkcja przykładowa:** [`estimate_tau`](../../../exercises/02_first_order_response.py) przyjmuje próbki ułożone według czasu (ściśle rosnącego, od chwili skoku). Zwraca znacznik czasu **pierwszego pomiaru**, który osiąga lub przekracza próg 63.2 % zmiany, uwzględniając połowę rozdzielczości pomiaru przy zaokrągleniach. Jeśli próbki wykonano po 1 s i 2 s, a przekroczenie widać dopiero po 2 s, faktyczny moment przejścia mógł być **między pomiarami**. Wynik 2 s jest oszacowaniem ograniczonym próbkowaniem, a nie dokładnym dopasowaniem. Nieuporządkowane, powtórzone lub błędne próbki, również po przekroczeniu progu, są odrzucane; przy braku przekroczenia funkcja zwraca `None`.

**Rozdzielczość czujnika ma znaczenie:** parametr `resolution` funkcji `estimate_tau` musi być **mniejszy niż wartość całkowitej zmiany prędkości**. Jeśli skok jest od 0 do 10 rpm, lecz wyświetlacz zmienia wartość co 10 rpm, nie można wiarygodnie wyznaczyć przekroczenia 63.2 %. Funkcja odrzuca taki przypadek zamiast wskazywać pozorną chwilę przejścia przy pierwszym pomiarze. Nawet przy dobrej rozdzielczości wynik ogranicza częstość próbkowania.

<a id="section-5"></a>

## 5. Moment siły i energia obrotowa

Przyspieszenie kątowe $\alpha=\frac{d\omega}{dt}$ spełnia równanie:

$$
M=J\alpha.
$$

Energia kinetyczna ruchu obrotowego wynosi:

$$
E=\frac{1}{2}J\omega^2.
$$

Przy $\omega=10\ \mathrm{rad/s}$ i $J=2\ \mathrm{kg}\cdot\mathrm{m}^2$ otrzymujemy $100\ \mathrm{J}$; podwojenie $J$ daje $200\ \mathrm{J}$. Przy stałym $J$ podwojenie $\omega$ zwiększa energię czterokrotnie. Jest to **mechaniczna energia kinetyczna**, a nie energia elektryczna pobierana z zasilania: liczą się sprawność i straty.

<a id="section-6"></a>

## 6. Ćwiczenia

Uruchom [`02_first_order_response.py`](../../../exercises/02_first_order_response.py) i [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py). Opcjonalne wykresy wygeneruje [`plot_models.py`](../../../exercises/plot_models.py). Programy używają danych syntetycznych i nie komunikują się z żadnym sprzętem.


<a id="section-7"></a>

## 7. Dodatkowe wyjaśnienia (opcjonalne)


### Kiedy metoda Eulera staje się niestabilna

W prostym modelu pierwszego rzędu każdy krok Eulera mnoży **pozostały błąd prędkości** przez $1-\frac{dt}{\tau}$. Zbieżność wymaga $0<dt<2\tau$. Gdy $dt$ leży między $\tau$ a $2\tau$, przybliżenie oscyluje wokół celu. To własność **metody numerycznej**, nie rzeczywistego silnika. Mniejszy krok poprawia dokładność.

### Ograniczenia modelu momentu

Ogólniejszy model ma postać $J\ \frac{d\omega}{dt}=M_{\text{motor}}-M_{\text{load}}-M_{\text{friction}}$. Równość $\tau=\frac{J}{K}$ wymaga szczególnego założenia $M_{\text{net}}=K(u-\omega)$. Nasycenie napędu, opóźnienia pomiaru, tarcie i dodatkowe stany elektryczne mogą zmieniać odpowiedź.

### Energia i moc

Dla stałego $J$ zmiana energii kinetycznej to $\Delta E=\frac{1}{2}J(\omega_2^2-\omega_1^2)$, a chwilowa **moc mechaniczna** wynosi $P=M\omega$. Te wielkości nie określają samodzielnie energii elektrycznej pobranej ze źródła; trzeba uwzględnić straty i sprawność.


<a id="time-constant-derivation"></a>

### Skąd 63.2 %, 86.5 % i 95.0 %?

Procenty i postać wykładnicza wynikają z **tego samego równania**. Definiujemy błąd prędkości jako $\varepsilon(t)=u-v(t)$ (a nie liczbę Eulera). Przy stałym $u$ mamy $\frac{d\varepsilon}{dt}=-\frac{dv}{dt}$, więc równanie pierwszego rzędu przybiera postać:

$$
\varepsilon(t)=u-v(t),\qquad \frac{d\varepsilon}{dt}=-\frac{\varepsilon}{\tau}.
$$

$$
\frac{d\varepsilon}{\varepsilon}=-\frac{dt}{\tau}
\quad\Longrightarrow\quad
\ln\left\lvert\frac{\varepsilon(t)}{\varepsilon(0)}\right\rvert=-\frac{t}{\tau}
\quad\Longrightarrow\quad
\varepsilon(t)=\varepsilon(0)\exp\!\left(-\frac{t}{\tau}\right).
$$

Przy rozdzielaniu zmiennych dzielimy przez $\varepsilon$, co wymaga niezerowego początkowego błędu. Gdy $u=v_0$, błąd jest zawsze zerowy, a stałe rozwiązanie $v(t)=u$ wynika bezpośrednio z pierwotnego równania różniczkowego.

$$
f(t)=\frac{v(t)-v_0}{u-v_0}=1-\exp\!\left(-\frac{t}{\tau}\right),\qquad (u\ne v_0).
$$

| $t$ | $f(t)$ |
| ---: | ---: |
| $\tau$ | $1-\exp(-1)=0.63212056\ldots\approx63.2\ \%$ |
| $2\tau$ | $1-\exp(-2)=0.86466472\ldots\approx86.5\ \%$ |
| $3\tau$ | $1-\exp(-3)=0.95021293\ldots\approx95.0\ \%$ |

Dla skoku od 0 do 1000 rpm otrzymujemy około 632, 865 i 950 rpm po jednej, dwóch i trzech stałych czasowych. Ten model idealny zbliża się do wartości docelowej asymptotycznie.

<a id="euler-values-derivation"></a>

### Skąd wyniki metody Eulera

$$
v_N=u+(v_0-u)\left(1-\frac{dt}{\tau}\right)^N,\qquad N=\frac{t}{dt}.
$$

$$
\begin{aligned}
u&=10,\quad v_0=0,\quad t=\tau=1;\\
v_{dt=0.1}&=10(1-0.9^{10})\approx6.5132;\\
v_{dt=0.01}&=10(1-0.99^{100})\approx6.3397;\\
v_{\mathrm{exact}}&=10(1-\exp(-1))\approx6.3212.
\end{aligned}
$$
