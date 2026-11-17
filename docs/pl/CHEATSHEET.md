# Ściąga ze wzorami — ruch i układy pierwszego rzędu

**Języki:** [en](../en/CHEATSHEET.md) · [fr](../fr/CHEATSHEET.md) · [de](../de/CHEATSHEET.md) · [it](../it/CHEATSHEET.md) · [es](../es/CHEATSHEET.md) · [pt](../pt/CHEATSHEET.md) · [zh](../zh/CHEATSHEET.md) · [ja](../ja/CHEATSHEET.md) · [nb](../nb/CHEATSHEET.md) · [ru](../ru/CHEATSHEET.md) · [ko](../ko/CHEATSHEET.md) · [fi](../fi/CHEATSHEET.md) · [pl](CHEATSHEET.md)

**Jednostki w tej części (wyjaśnione przed przykładami):** `s` — sekunda; `m` — metr; `m/s` — metr na sekundę — prędkość liniowa; `rad/s` — radian na sekundę — prędkość kątowa; `kg·m²` — kilogram razy metr kwadratowy — moment bezwładności; `N·m` — niutonometr — moment siły; `N·m·s/rad` — niutonometr razy sekunda na radian — współczynnik momentu względem prędkości kątowej; `J` — dżul — energia i praca; `mm` — milimetr = 0.001 m; `mm/s` — milimetr na sekundę — prędkość liniowa; `%` — procent — jedna setna. [Słownik jednostek](UNITS.md).

[Spis treści](README.md) · [Ruch](notes/01-motion-calculus.md) · [Dynamika](notes/02-first-order-dynamics.md) · [Ćwiczenia](exercises/README.md)

> **To nie specyfikacja inżynierska.** Przed zastosowaniem sprawdź jednostki i założenia modelu.

| Pojęcie | Definicja lub równanie |
| --- | --- |
| Przemieszczenie | $\Delta x=x_2-x_1$ (ze znakiem) |
| Droga przebyta | $s=\int_{t_1}^{t_2}\lvert v(t)\rvert\ \mathrm{d}t\ge 0$ |
| Prędkość średnia wektorowa | $\bar v=\frac{\Delta x}{\Delta t}$ (ze znakiem w 1D) |
| Szybkość średnia | $\frac{s}{\Delta t}$ (nieujemna) |
| Prędkość chwilowa | $v(t)=\frac{dx}{dt}$ |
| Przemieszczenie z prędkości | $\Delta x=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t$ |
| Jawny schemat Eulera | $x_{n+1}=x_n+v_n\ dt$ |
| Dynamika pierwszego rzędu | $\frac{dv}{dt}=\frac{u-v}{\tau}$ |
| Błąd prędkości | $\varepsilon(t)=u-v(t)$ |
| Dokładna odpowiedź skokowa | $v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right)$, dla stałego $u$ |
| Stała czasowa | Przy $t=\tau$ zrealizowano $63.2\ \%$ zmiany |
| Uproszczony model momentu | $M=K(u-\omega)$ |
| Przyspieszenie kątowe | $M=J\alpha$, $\alpha=\frac{d\omega}{dt}$ |
| Stała czasowa w tym modelu | $\tau=\frac{J}{K}$, **wyłącznie** przy podanych założeniach |
| Energia kinetyczna ruchu obrotowego | $E=\frac{1}{2}J\omega^2$ |

**Oznaczenia:** $\varepsilon$ to błąd prędkości, $\mathrm{e}\approx2.71828$ to liczba Eulera, a $\exp(z)=\mathrm{e}^{z}$ oznacza funkcję wykładniczą. Nie należy mylić tych symboli.

**Jednostki SI:**

| Wielkość | Nazwa | Jednostka |
| --- | --- | --- |
| `t, dt, τ` | Czas | s (sekunda) |
| `x` | Położenie | m (metr) |
| `v` | Prędkość liniowa | m/s (metr na sekundę) |
| `ω` | Prędkość kątowa | rad/s (radian na sekundę) |
| `J` | Moment bezwładności | kg·m² (kilogram razy metr kwadratowy) |
| `M` | Moment siły | N·m (niutonometr) |
| `K` | Współczynnik momentu | N·m·s/rad |
| `E` | Energia | J (dżul) |

Środkowa kropka `·` oznacza mnożenie, nie znak dziesiętny. W modelu liniowym $u$ jest prędkością liniową, a w modelu obrotowym — prędkością kątową.

**Typowe pułapki:** szybkość nie jest prędkością ze znakiem; droga to nie przemieszczenie; $dt$ nie jest stałą $\tau$; po jednej stałej czasowej układ nie osiąga jeszcze wartości docelowej; $J/K$ nie jest uniwersalną zależnością dla dowolnego silnika; energia mechaniczna nie oznacza całkowitego zużycia energii elektrycznej.

Więcej znajdziesz w [dodatkowych wyprowadzeniach rachunku różniczkowego i całkowego](notes/01-motion-calculus.md#section-6) i [ograniczeniach modelu oraz stabilności Eulera](notes/02-first-order-dynamics.md#section-7).


[Skąd się biorą wartości procentowe? Pełne obliczenia](notes/02-first-order-dynamics.md#time-constant-derivation).

[Skąd wyniki 3, 3.8 i 3.98? Pełne obliczenia](notes/01-motion-calculus.md#motion-values-derivation).


## Symbole i notacja

**Σ / ∑ (sumowanie)** oznacza dodawanie kolejnych składników. Przykład: $\sum_{n=1}^{3} n=1+2+3=6$. Granice sumowania określają, które składniki należy dodać. [Dalsze wyjaśnienia symboli](SYMBOLS.md).


## Tablica całek

[0. Podstawy analizy: pochodne i całki](notes/00-calculus-foundations.md) · [Tablica całek](INTEGRAL_TABLE.md)

## Sterowanie ze sprzężeniem zwrotnym: PID i moment utrzymujący

| $\varepsilon=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}}$ | $u_P=K_p\varepsilon$, $u_I=K_i\int\varepsilon\ \mathrm{d}t$ |
| --- | --- |
| $M_{\mathrm{motor}}=K_t I$ | $\lvert M_g\rvert=mgL\lvert\cos\theta\rvert$ |

[Sterowanie PID i moment utrzymujący](notes/03-feedback-control.md) · [Trygonometria z przykładami mechanicznymi](TRIGONOMETRY.md)

<a id="joint-velocity"></a>
## Prędkość obrotowa i jakobian

Prędkości kątowe przegubów są wyrażone w rad/s. Przy długościach w mm prędkość liniowa jest w mm/s.

$$
v_x=-L\sin Q\cdot\dot Q,\qquad v_y=L\cos Q\cdot\dot Q
$$

$$
\det J=L_1L_2\sin Q_2
$$

[Ruch obrotowy, prędkość i jakobian](notes/05-velocity-jacobian.md)
