# 0. Podstawy analizy matematycznej: pochodne, granice i całki

**Języki:** [en](../../en/notes/00-calculus-foundations.md) · [fr](../../fr/notes/00-calculus-foundations.md) · [de](../../de/notes/00-calculus-foundations.md) · [it](../../it/notes/00-calculus-foundations.md) · [es](../../es/notes/00-calculus-foundations.md) · [pt](../../pt/notes/00-calculus-foundations.md) · [zh](../../zh/notes/00-calculus-foundations.md) · [ja](../../ja/notes/00-calculus-foundations.md) · [nb](../../nb/notes/00-calculus-foundations.md) · [ru](../../ru/notes/00-calculus-foundations.md) · [ko](../../ko/notes/00-calculus-foundations.md) · [fi](../../fi/notes/00-calculus-foundations.md) · [pl](00-calculus-foundations.md)

**Jednostki w tej części (objaśnione przed przykładami):** `s` — sekunda; `mm` — milimetr = 0.001 m; `mm/s` — milimetr na sekundę — prędkość liniowa; `mm/s²` — milimetr na sekundę do kwadratu — przyspieszenie; `kg·m²` — kilogram razy metr kwadratowy — moment bezwładności; `rad/s` — radian na sekundę — prędkość kątowa; `rad/s²` — radian na sekundę do kwadratu — przyspieszenie kątowe; `N·m` — niutonometr — moment siły; `W` — wat — moc; `rpm` — obrót na minutę; `N/m` — niuton na metr — sztywność sprężyny; `mm³/s` — milimetr sześcienny na sekundę — strumień objętości; `%` — procent — jedna setna; `m` — metr; `kg` — kilogram; `N` — niuton — siła; `J` — dżul — energia i praca; `rad` — radian — kąt płaski. [Słownik jednostek](../UNITS.md).

[Spis treści](../README.md) · [Tablica całek](../INTEGRAL_TABLE.md) · [Trygonometria](../TRIGONOMETRY.md) · [Ruch](01-motion-calculus.md) · [Dynamika](02-first-order-dynamics.md) · [Symbole](../SYMBOLS.md)

> **Model edukacyjny:** samodzielnie weryfikuj założenia i jednostki; nie podłączaj przykładowego kodu do prawdziwego sprzętu.

**Naturalna funkcja wykładnicza** to $\exp(x)=\mathrm{e}^{x}$, gdzie **liczba Eulera** wynosi $\mathrm{e}\approx2.71828$. Opisuje ciągły wzrost lub zanik; $\exp(0)=1$ i $\exp(-1)\approx0.3679$. Logarytm naturalny $\ln$ jest funkcją odwrotną: $\ln(\exp(x))=x$. Zobacz [spis symboli](../SYMBOLS.md).

**Pochodna (derivative)** określa, jak szybko zmienia się dana wielkość **w danej chwili**. Druga pochodna mówi, jak zmienia się ta szybkość zmian. Całka (integral) sumuje małe przyrosty. Granica (limit) definiuje zmianę chwilową. Logarytm pozwala wyznaczyć czas potrzebny do osiągnięcia zadanego fragmentu odpowiedzi wykładniczej.

Tych samych narzędzi używamy w osi maszyny, serwonapędzie, przegubie robota, sprężynie i czujniku. Najpierw sformułuj pytanie fizyczne, ustal wielkość, która się zmienia, oraz jej jednostkę, a dopiero potem wybierz regułę obliczeń.

## Spis treści

- [1. Od pomiaru zmiany do modelu matematycznego](#section-1)
- [2. Granice i pierwsza pochodna](#section-2)
- [3. Pierwsza i druga pochodna: ruch osi](#section-3)
- [4. Reguła łańcuchowa: energia obrotowa](#section-4)
- [5. Funkcje wykładnicze i logarytmy: czas odpowiedzi](#section-5)
- [6. Całki: przemieszczenie i praca mechaniczna](#section-6)
- [7. Dodatkowy przykład: rosnąca kula](#section-7)
- [8. Jednostki, kontrola wyników i kolejne kroki](#section-8)

<a id="section-1"></a>
## 1. Od pomiaru zmiany do modelu matematycznego

| Pytanie fizyczne | Narzędzie matematyczne |
| --- | --- |
| Jak szybko oś porusza się **teraz**? | Pierwsza pochodna $dx/dt$ |
| Jak szybko zmienia się prędkość? | Druga pochodna $d^2x/dt^2$ |
| Kiedy odpowiedź osiągnie 90 %? | Logarytm $\ln$ |
| O ile przesunie się oś w 2 s? | Całka oznaczona $\int v\ \mathrm{d}t$ |
| Jaka jest praca zmiennej siły? | Całka $\int F\ \mathrm{d}x$ |

<a id="section-2"></a>
## 2. Granice i pierwsza pochodna

Iloraz przyrostów pomiędzy dwoma pomiarami opisuje **średnią szybkość zmiany** na danym przedziale. Pochodna jest granicą tego ilorazu, gdy szerokość przedziału dąży do zera.

$$
v(t)=\frac{dx}{dt}=\lim_{h\to0}\frac{x(t+h)-x(t)}{h}.
$$

Dla położenia $x(t)=at^2$ i $a=2\ \mathrm{mm/s^2}$ najpierw rozwiń licznik, zanim przejdziesz do granicy:

$$
\frac{x(t+h)-x(t)}h=\frac{a[(t+h)^2-t^2]}h=a(2t+h)\longrightarrow 2at.
$$

Czynnik $h$ skraca się **zanim** przyjmiemy, że dąży do zera. W chwili $t=1\ \mathrm{s}$ prędkość chwilowa wynosi $4\ \mathrm{mm/s}$. Granica nie oznacza podstawiania niedozwolonego $0/0$.

**Najczęstsze reguły różniczkowania** (współczynniki $c$ i $n$ są stałe, a argumenty trygonometryczne podane w radianach):

| Reguła | Wzór |
| --- | --- |
| Stała | $\frac{d}{dt}c=0$ |
| Potęga | $\frac{d}{dt}t^n=n t^{n-1}$ |
| Stały współczynnik i suma | $(cf+g)'=cf'+g'$ |
| Iloczyn | $(fg)'=f' g+fg'$ |
| Iloraz, $g\ne0$ | $\left(\frac{f}{g}\right)'=\frac{f' g-fg'}{g^2}$ |
| Reguła łańcuchowa | $\frac{d}{dt}f(g(t))=f'(g(t))g'(t)$ |
| Funkcja wykładnicza | $\frac{d}{dt}\exp(t)=\exp(t)$ |
| Logarytm naturalny, $t>0$ | $\frac{d}{dt}\ln t=\frac1t$ |
| Sinus i cosinus | $\frac{d}{dt}\sin t=\cos t$, $\frac{d}{dt}\cos t=-\sin t$ |

![Nachylenie wykresu położenia i pole pod wykresem prędkości.](../../../assets/figures/calculus_slope_area.svg)

<a id="section-3"></a>
## 3. Pierwsza i druga pochodna: ruch osi

Wózek rozpoczyna ruch w położeniu 2 mm z prędkością początkową 3 mm/s i stałym przyspieszeniem 4 mm/s². Jego położenie opisuje wzór:

$$
x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2.
$$

Pierwsza pochodna to **prędkość**. Różniczkujemy każdy składnik: stałe 2 mm znika, składnik liniowy w $t$ daje 3 mm/s, a składnik z $t^2$ daje wyrażenie liniowe w $t$.

$$
v(t)=\frac{dx}{dt}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t.
$$

Druga pochodna to **przyspieszenie**: różniczkujemy prędkość ponownie. Po 2 s położenie wynosi 16 mm, prędkość 11 mm/s, a przyspieszenie wciąż 4 mm/s².

$$
a(t)=\frac{d^2x}{dt^2}=\frac{dv}{dt}=4\ \mathrm{mm/s^2}.
$$

Druga pochodna ma jednostki długości dzielonej przez czas do kwadratu. **Nie jest** kwadratem pierwszej pochodnej.

<a id="section-4"></a>
## 4. Reguła łańcuchowa: energia ruchu obrotowego

Obracające się koło zamachowe magazynuje energię kinetyczną. Gdy prędkość kątowa $\omega$ zależy od czasu, energia $E$ zmienia się za jej pośrednictwem. To zastosowanie **reguły łańcuchowej (chain rule)**.

$$
E(\omega)=\frac12J\omega^2,\quad \omega=\omega(t),
$$
$$
\frac{dE}{dt}=\frac{dE}{d\omega}\frac{d\omega}{dt}=J\omega\alpha=M\omega=P.
$$

Dla $J=0.01\ \mathrm{kg\cdot m^2}$, $\omega=10\ \mathrm{rad/s}$ oraz $\alpha=2\ \mathrm{rad/s^2}$ moment silnika to $J\alpha=0.02\ \mathrm{N\cdot m}$, a chwilowa moc mechaniczna wynosi $0.2\ \mathrm{W}$. Widzimy tutaj praktyczne zastosowanie reguły łańcuchowej: $P=M\omega$.

<a id="section-5"></a>
## 5. Funkcje wykładnicze i logarytmy: czas odpowiedzi

W prostym modelu napędu pierwszego rzędu prędkość może zbliżać się do wartości końcowej wykładniczo. Parametr $\tau$ to **stała czasowa (time constant)** mierzona w sekundach.

$$
\omega(t)=\omega_\infty\bigl(1-\exp(-t/\tau)\bigr),\quad t\ge0,\ \tau>0.
$$

To wyrażenie zakłada **zerową początkową prędkość kątową** $\omega(0)=0$ oraz stałą wartość docelową $\omega_\infty$. Gdy prędkość początkowa $\omega_0$ jest niezerowa, ogólna odpowiedź pierwszego rzędu ma postać:

$$
\omega(t)=\omega_\infty+(\omega_0-\omega_\infty)\exp(-t/\tau).
$$

**Przykład z niezerową prędkością początkową:** $\omega_0=200\ \mathrm{rpm}$, $\omega_\infty=1000\ \mathrm{rpm}$ i $\tau=0.5\ \mathrm{s}$. Po jednej stałej czasowej ($t=0.5\ \mathrm{s}$):

$$
\omega(\tau)=1000+(200-1000)\exp(-1)\approx705.7\ \mathrm{rpm}.
$$

Odpowiedź zrealizowała **63.2 % zmiany wynoszącej 800 rpm**, a nie 63.2 % docelowych 1000 rpm. Podstawienie $t=0$ daje 200 rpm; dla rosnącego czasu wynik zbliża się do 1000 rpm. To obliczenie matematyczne, nie polecenie dla silnika.

Funkcja wykładnicza opisuje pozostałą część początkowego błędu. Aby ustalić, **kiedy** pozostanie zadana część, stosujemy logarytm naturalny $\ln$, funkcję odwrotną do $\exp$. Argument $0.1$ jest tutaj bezwymiarowy.

$$
\exp(-t/\tau)=0.1
\quad\Longrightarrow\quad
-\frac{t}{\tau}=\ln(0.1)
\quad\Longrightarrow\quad
t=-\tau\ln(0.1)=\tau\ln(10)\approx2.303\tau.
$$

Aby uzyskać 90 % końcowej zmiany, powinno pozostać 10 % początkowego błędu. Przy $\tau=0.5\ \mathrm{s}$ model idealny daje około 1.151 s. Rzeczywisty napęd może mieć inne ograniczenia i opóźnienia.

Pochodna $\ln z$ to $1/z$ dla $z>0$; gdy $z=z(t)$, mnożymy dodatkowo przez $dz/dt$ na mocy reguły łańcuchowej. Nigdy nie obliczaj logarytmu wielkości wymiarowej, jeżeli wcześniej nie utworzysz stosunku bezwymiarowego.

$$
\ln(1)=0,\quad \ln(\mathrm{e})=1,\quad \ln(\mathrm{e}^{z})=z,\quad \frac{d}{dz}\ln z=\frac1z\ (z>0).
$$

<a id="section-6"></a>
## 6. Całki: przemieszczenie i praca mechaniczna

**Całka nieoznaczona** wyznacza rodzinę wszystkich funkcji pierwotnych i zawiera nieznaną stałą $C$. **Całka oznaczona** wyznacza sumaryczną zmianę na określonym przedziale.

$$
\int 4t\ \mathrm{d}t=2t^2+C,\qquad \int t^n\ \mathrm{d}t=\frac{t^{n+1}}{n+1}+C\ (n\ne-1).
$$

**Przykład ruchu.** Wózek zaczyna od $x_0=2\ \mathrm{mm}$, a prędkość rośnie liniowo: $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$. Wyznacz przemieszczenie w czasie od 0 do 2 s:

$$
\Delta x=\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
$$
$$
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}=6\ \mathrm{mm}+8\ \mathrm{mm}=14\ \mathrm{mm}.
$$

Przemieszczenie wynosi 14 mm. Po dodaniu położenia początkowego otrzymujemy $x(2)=16\ \mathrm{mm}$. Prędkość ujemna daje ujemny wkład do przemieszczenia ze znakiem, ale nie ujemną drogę.

**Praca sprężyny.** Rozciągamy idealną liniową sprężynę od $x=0$ do $x=0.01\ \mathrm{m}$ przy sztywności $k=200\ \mathrm{N/m}$. Siła rośnie wraz z wydłużeniem, więc sumujemy iloczyny siły i małego przyrostu drogi:

$$
F(x)=kx,\qquad W=\int_0^{0.01\ \mathrm{m}}kx\ \mathrm{d}x
=\left[\frac{kx^2}{2}\right]_0^{0.01\ \mathrm{m}}
=\frac{200\ \mathrm{N/m}}2(0.01\ \mathrm{m})^2=0.01\ \mathrm{J}.
$$

Praca wynosi 0.01 J. Gdyby użyć tylko siły końcowej $F=2\ \mathrm{N}$ dla całej drogi, otrzymalibyśmy błędne 0.02 J, bo siła nie była stała.

<a id="section-7"></a>
## 7. Dodatkowy przykład: powiększająca się kula

**Opcjonalny przykład reguły łańcuchowej.** Objętość kuli zależy od promienia, a promień może zmieniać się w czasie. Matematycznie jest to ta sama zależność złożona co energia koła zamachowego zależna od prędkości kątowej.

$$
V(r)=\frac43\pi r^3,\qquad \frac{dV}{dt}=\frac{dV}{dr}\frac{dr}{dt}=4\pi r^2\frac{dr}{dt}.
$$

Przy $r=10\ \mathrm{mm}$ i $dr/dt=1\ \mathrm{mm/s}$ chwilowe tempo przyrostu objętości wynosi $400\pi\approx1256.64\ \mathrm{mm^3/s}$. Jeśli $r(t)=10\ \mathrm{mm}+(1\ \mathrm{mm/s^2})t^2$, to przy 2 s promień wynosi 14 mm, pochodna $dr/dt=4\ \mathrm{mm/s}$, a tempo zmiany objętości to $3136\pi\approx9852.03\ \mathrm{mm^3/s}$.

<a id="section-8"></a>
## 8. Jednostki, sprawdzenie wyników i kolejne kroki

**Sprawdzenie:** pochodna położenia ma jednostkę m/s, druga pochodna m/s²; całka z siły po drodze daje N·m = J; całka nieoznaczona wymaga stałej $C$; pochodna opisuje zmianę lokalną, całka — akumulację na przedziale. Symbol $\mathrm{d}t$ jest różniczką, ale `dt` w kodzie Eulera jest skończonym krokiem czasu.

**Zadania z odpowiedziami:** (1) Dla $x(t)=5\ \mathrm{mm}+(2\ \mathrm{mm/s})t+(1\ \mathrm{mm/s^2})t^2$ policz prędkość i przyspieszenie po 3 s. (2) Ile trwa osiągnięcie 90 % zmiany przez idealny układ pierwszego rzędu z $\tau=1\ \mathrm{s}$? (3) Wyznacz przemieszczenie przy stałej prędkości 4 mm/s przez 2 s. **Odpowiedzi:** 8 mm/s i 2 mm/s²; około 2.303 s; 8 mm.

**Rozwiązania krok po kroku:**

1. $v(t)=\frac{dx}{dt}=2\ \mathrm{mm/s}+2(1\ \mathrm{mm/s^2})t$; $v(3\ \mathrm{s})=2+2\cdot3=8\ \mathrm{mm/s}$. $a(t)=\frac{dv}{dt}=2\ \mathrm{mm/s^2}$.
2. $f(t)=1-\exp(-t/\tau)=0.9$; $\exp(-t/\tau)=0.1$; $t=-\tau\ln(0.1)=\tau\ln(10)$. $\tau=1\ \mathrm{s}$; $t\approx2.303\ \mathrm{s}$.
3. $\Delta x=\int_0^{2\ \mathrm{s}}(4\ \mathrm{mm/s})\ \mathrm{d}t=(4\ \mathrm{mm/s})(2\ \mathrm{s})=8\ \mathrm{mm}$.


[Tablica całek](../INTEGRAL_TABLE.md) · [Trygonometria](../TRIGONOMETRY.md) · [Dalej: ruch](01-motion-calculus.md) · [Ćwiczenia w Pythonie](../exercises/README.md)
