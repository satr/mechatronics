# 5. Ruch obrotowy, prędkość liniowa i osobliwości

**Języki:** [en](../../en/notes/05-velocity-jacobian.md) · [fr](../../fr/notes/05-velocity-jacobian.md) · [de](../../de/notes/05-velocity-jacobian.md) · [it](../../it/notes/05-velocity-jacobian.md) · [es](../../es/notes/05-velocity-jacobian.md) · [pt](../../pt/notes/05-velocity-jacobian.md) · [zh](../../zh/notes/05-velocity-jacobian.md) · [ja](../../ja/notes/05-velocity-jacobian.md) · [nb](../../nb/notes/05-velocity-jacobian.md) · [ru](../../ru/notes/05-velocity-jacobian.md) · [ko](../../ko/notes/05-velocity-jacobian.md) · [fi](../../fi/notes/05-velocity-jacobian.md) · [pl](05-velocity-jacobian.md)

**Jednostki tej lekcji (wyjaśnione przed przykładami):** `mm` — milimetr; `mm/s` — milimetr na sekundę (prędkość liniowa); `rad` — radian; `rad/s` — radian na sekundę (prędkość kątowa); `mm/rad` — milimetr na radian (współczynnik jakobianu); `°` — stopień kąta płaskiego. [Pełny słownik jednostek](../UNITS.md).

[Spis treści](../README.md) · [Trygonometria](../TRIGONOMETRY.md#unit-circle-values) · [Układy współrzędnych](04-coordinate-frames.md) · [Podstawy analizy](00-calculus-foundations.md)

> Wyłącznie idealny model syntetyczny. Nie używaj go do sterowania rzeczywistym sprzętem.

Końcówka ramienia obracającego się wokół przegubu porusza się po łuku. Jej prędkość chwilowa jest **styczna** do łuku, nie skierowana wzdłuż ramienia. Przejdziemy od geometrii przez pochodne po czasie do opcjonalnej macierzy jakobianu. W pochodnych kąty są wyrażone w radianach; stopnie pomagają wizualizować przykłady.

## Spis treści

1. [Od ramienia obrotowego do prędkości stycznej](#section-1)
2. [Skąd pochodzą pochodne](#section-2)
3. [Przykłady prędkości i znaków](#section-3)
4. [Dwa człony: kąty względne i bezwzględne](#section-4)
5. [Osobliwości przy złożeniu i wyprostowaniu](#section-5)
6. [Trzy różne przemieszczenia blisko złożenia](#section-6)
7. [Jakobian i rozwiązane przykłady kontrolne](#section-7)

<a id="section-1"></a>
## 1. Od ramienia obrotowego do prędkości stycznej

Dla sztywnego członu długości $L$ obracającego się wokół stałej osi $O$ niech $\Delta Q$ oznacza zmianę kąta **w radianach** w przedziale $\Delta t>0$. Podczas obrotu bez zmiany zwrotu końcówka pokonuje łuk. **Jego długość** wynosi dokładnie $\Delta s=L|\Delta Q|$. **Droga ze znakiem wzdłuż zorientowanego łuku** ma wartość $L\Delta Q$; znak określa zwrot. Żadnej z tych wielkości nie należy mylić z prostoliniowym przemieszczeniem (cięciwą) między dwoma położeniami końcówki.

$$
\Delta s=L\lvert\Delta Q\rvert,\qquad
\Delta s_{\mathrm{signed}}=L\Delta Q
$$

Dzieląc długość łuku przez czas, otrzymujemy **średnią szybkość** w tym przedziale:

$$
\overline{v}=\frac{\Delta s}{\Delta t}
=L\left\lvert\frac{\Delta Q}{\Delta t}\right\rvert
$$

Aby wyznaczyć **szybkość chwilową**, przechodzimy do granicy $\Delta t\to0$. Ponieważ $\omega=\dot Q=\mathrm{d}Q/\mathrm{d}t$ jest prędkością kątową w rad/s, moduł prędkości końcówki to $v=L|\omega|$. Kierunek prędkości jest styczny do okręgu i prostopadły do członu. Przy obrocie przeciwnym do ruchu wskazówek zegara ($\omega>0$) i $Q=45^\circ$ końcówka porusza się w górę i w lewo: składowa pozioma jest ujemna, pionowa dodatnia.

$$
v=L\lvert\dot Q\rvert
$$

![Sztywny człon i styczna prędkość końcówki: Q=45°, dodatni obrót i znaki składowych.](../../../assets/figures/link_tangent_velocity.svg)

*Człon obrócony o 45°, prędkość końcówki styczna do łuku.*

<a id="section-2"></a>
## 2. Skąd pochodzą pochodne

Współrzędne końcówki zależą od kąta, a kąt zależy od czasu. Są to **dwie różne zależności**. Reguła łańcuchowa mnoży zmianę współrzędnej na radian przez liczbę radianów obracanych na sekundę. Różniczkujemy sinus i cosinus z argumentami w radianach:

$$
x(t)=L\cdot\cos\bigl(Q(t)\bigr),\qquad y(t)=L\cdot\sin\bigl(Q(t)\bigr)
$$

$$
v_x=\frac{\mathrm{d}x}{\mathrm{d}t}
=\frac{\mathrm{d}x}{\mathrm{d}Q}\cdot\frac{\mathrm{d}Q}{\mathrm{d}t}
=-L\cdot\sin(Q)\cdot\dot{Q}
$$

$$
v_y=\frac{\mathrm{d}y}{\mathrm{d}t}
=\frac{\mathrm{d}y}{\mathrm{d}Q}\cdot\frac{\mathrm{d}Q}{\mathrm{d}t}
=L\cdot\cos(Q)\cdot\dot{Q}
$$

Prędkość kątowa wynosi $\dot Q=\mathrm{d}Q/\mathrm{d}t$ i jest mierzona w rad/s. Nie jest samym kątem. Gdy $L$ jest w mm, $v_x$ i $v_y$ mają jednostkę mm/s; pochodne trygonometryczne wymagają radianów.


$$
\omega=\dot{Q},\qquad \omega_1=\dot{Q}_1,\qquad \omega_2=\dot{Q}_2
$$

<a id="section-3"></a>
## 3. Przykłady prędkości i znaków

Przy Q=45°, L=150 mm i ω=+0.1 rad/s końcówka porusza się w lewo i w górę, z równymi modułami składowych. Zmiana zwrotu obrotu na −0.1 rad/s odwraca oba znaki, ale nie zmienia modułu szybkości. Przy Q=0° składowa pozioma jest zerowa, a pionowa +15 mm/s. Kropka nad $Q$ oznacza pochodną po czasie, nie mnożenie przez kąt.

$$
Q=45^\circ:\quad v_x=-150\frac{\sqrt2}{2}\cdot0.1\approx-10.61\ \mathrm{mm/s}
$$

$$
v_y=+150\frac{\sqrt2}{2}\cdot0.1\approx+10.61\ \mathrm{mm/s}
$$

$$
\sqrt{v_x^2+v_y^2}=L\lvert\dot Q\rvert=15\ \mathrm{mm/s}
$$

<a id="section-4"></a>
## 4. Dwa człony: kąty względne i bezwzględne

W płaskim ramieniu o dwóch członach $Q_1$ oznacza kąt pierwszego członu względem świata, a $Q_2$ jest **względnym** kątem drugiego przegubu. Dlatego orientacja drugiego członu w świecie wynosi $Q_1+Q_2$, a jego prędkość kątowa to $\omega_1+\omega_2$. Różniczkowanie równań kinematyki prostej daje udział obu przegubów:

$$
X=L_1\cdot\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)
$$

$$
Y=L_1\cdot\sin(Q_1)+L_2\cdot\sin(Q_1+Q_2)
$$

$$
v_x=-L_1\cdot\sin(Q_1)\cdot\dot{Q}_1
-L_2\cdot\sin(Q_1+Q_2)\cdot(\dot{Q}_1+\dot{Q}_2)
$$

$$
v_y=L_1\cdot\cos(Q_1)\cdot\dot{Q}_1
+L_2\cdot\cos(Q_1+Q_2)\cdot(\dot{Q}_1+\dot{Q}_2)
$$

<a id="section-5"></a>
## 5. Osobliwości przy złożeniu i wyprostowaniu

Przy idealnych przegubach bez ograniczeń oraz L1=100 mm i L2=50 mm promień $r$ zmienia się od 50 mm (pełne złożenie Q2=±180°) do 150 mm (wyprostowanie Q2=0°). W obu konfiguracjach współliniowych prędkości wynikające z obrotów przegubów są prostopadłe do linii członów; dowolnej prędkości promieniowej nie można wtedy uzyskać przy skończonych prędkościach przegubów. Ograniczenia przegubów i kolizje zmniejszają rzeczywistą przestrzeń roboczą. Sama osiągalność położenia nie gwarantuje orientacji narzędzia ani wolnej przestrzeni.

$$
r^2=L_1^2+L_2^2+2L_1L_2\cos(Q_2)
$$

$$
\lvert L_1-L_2\rvert\le r\le L_1+L_2
$$

$$
\frac{\mathrm{d}r}{\mathrm{d}Q_2}
=-\frac{L_1L_2\sin(Q_2)}{r}
$$

Wzór na pochodną zakłada $r>0$. Dla równych członów dokładnie złożonych do bazy ($L_1=L_2$, $Q_2=180^\circ$) mamy $r=0$ i we wzorze pojawia się dzielenie przez zero. Odległość promieniowa nie jest tam różniczkowalna jako funkcja zorientowanego odchylenia kąta łokcia. Nie dotyczy to poniższych przykładów dla członów o różnych długościach.

<a id="section-6"></a>
## 6. Trzy różne przemieszczenia blisko złożenia

Ustawmy pierwszy człon poziomo, a drugi początkowo wstecz, w pozycji złożonej. Niech δ≥0 oznacza małe odchylenie od złożenia w radianach. Przemieszczenie wzdłuż **nieruchomej osi** pierwszego członu nie jest tym samym co zmiana odległości końcówki od bazy. Dokładne wzory są następujące:

$$
\Delta x_{\mathrm{axis}}=L_2\bigl(1-\cos(\delta)\bigr)
\approx\frac{L_2\delta^2}{2}
$$

$$
\Delta y_{\mathrm{perp}}=L_2\cdot\sin(\delta)\approx L_2\delta
$$

$$
\Delta r=\sqrt{(L_1-L_2)^2+2L_1L_2\bigl(1-\cos(\delta)\bigr)}-(L_1-L_2)
$$

$$
L_1>L_2>0:\qquad
\Delta r\approx\frac{L_1L_2}{2(L_1-L_2)}\delta^2
$$

Kwadrat i współczynnik 1/2 wynikają z $1-\cos\delta=2\sin^2(\delta/2)$ oraz $\sin(\delta/2)\approx\delta/2$. Dla członów o różnych długościach zmiana promienia ma inny współczynnik: $\Delta r\approx50\delta^2$ mm, a zmiana wzdłuż osi nieruchomej to około $25\delta^2$ mm. Podzielenie δ przez dwa zmniejsza każdą wielkość kwadratową czterokrotnie, lecz przemieszczenie poprzeczne tylko dwukrotnie. Przybliżenia dotyczą małych δ.

$$
1-\cos(\delta)=2\sin^2\left(\frac{\delta}{2}\right)
\approx2\left(\frac{\delta}{2}\right)^2=\frac{\delta^2}{2}
$$

![Trzy przemieszczenia przy rozkładaniu ramienia; stopnie na osi, radiany w przybliżeniach.](../../../assets/figures/folded_displacement_curves.svg)

*Przemieszczenia przy rozkładaniu ramienia. Obliczenia małokątowe wykonujemy w radianach.*

Aby utrzymać stałą niezerową prędkość promieniową $v_r$ blisko granicy złożenia, prędkość kątowa łokcia musiałaby rosnąć bez ograniczeń przy δ dążącym do zera. Dla δ=0 radialna prędkość pierwszego rzędu jest zerowa przy dowolnych skończonych prędkościach przegubów. Matematyczne żądanie odwrotnej prędkości rozbiega się. Fizyczny robot może rozpoczynać rozkładanie ze skończoną prędkością kątową, początkowo przy zerowej prędkości radialnej, a następnie stopniowo ją zwiększać.

$$
\left.\frac{\mathrm{d}r}{\mathrm{d}\delta}\right|_{L_1=100,L_2=50}
=\frac{5000\sin(\delta)}{r}
\approx100\delta\ \mathrm{mm/rad}
$$

$$
v_r\approx(100\delta)\dot\delta\ \mathrm{mm/s},
\qquad
\dot\delta\approx\frac{1\ \mathrm{mm/s}}{100\ \mathrm{mm/rad}\cdot\delta}
$$

![Prędkość kątowa łokcia wymagana do utrzymania 1 mm/s prędkości promieniowej blisko osobliwości.](../../../assets/figures/folded_radial_speed.svg)

*Rosnące zapotrzebowanie na prędkość kątową blisko granicy osobliwości.*

<a id="section-7"></a>
## 7. Jakobian i rozwiązane sprawdzenia

**Macierz jakobianu (Jacobian)** zbiera pochodne współrzędnych narzędzia względem kątów przegubów. Zamienia chwilowe prędkości przegubów na prędkość narzędzia, a nie położenia przegubów na współrzędne bezwzględne. W idealnym modelu płaskim wyznacznik znika dokładnie, gdy sin Q2=0, to jest przy wyprostowaniu lub złożeniu. W pobliżu tych konfiguracji odwrotne odwzorowanie prędkości jest źle uwarunkowane. Model służy wyłącznie do nauki; w praktyce liczą się także ograniczenia, odsunięcia narzędzia, luzy, podatność i kolizje.

$$
v_x=J_{11}\cdot\omega_1+J_{12}\cdot\omega_2
$$

$$
v_y=J_{21}\cdot\omega_1+J_{22}\cdot\omega_2
$$

| Współczynnik | Geometria odwzorowania prędkości |
| --- | --- |
| $J_{11}$ | $-L_1\sin(Q_1)-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{12}$ | $-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{21}$ | $L_1\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)$ |
| $J_{22}$ | $L_2\cdot\cos(Q_1+Q_2)$ |



**Wyprowadzenie wyznacznika.** Każda pozycja macierzy jakobianu jest pochodną cząstkową współrzędnej X lub Y końcówki względem kąta przegubu Q1 lub Q2 w radianach. Długość w mm daje współczynnik w mm/rad; po pomnożeniu przez rad/s otrzymujemy mm/s.

$$
J_{11}=\frac{\partial X}{\partial Q_1},\qquad
J_{12}=\frac{\partial X}{\partial Q_2}
$$

$$
J_{21}=\frac{\partial Y}{\partial Q_1},\qquad
J_{22}=\frac{\partial Y}{\partial Q_2}
$$

$$
\det J=J_{11}J_{22}-J_{12}J_{21}
$$

$$
\det J=L_1L_2\bigl[\sin(Q_1+Q_2)\cos(Q_1)
-\sin(Q_1)\cos(Q_1+Q_2)\bigr]
$$

$$
\det J=L_1L_2\sin\bigl((Q_1+Q_2)-Q_1\bigr)
$$

Po rozwinięciu dwóch iloczynów w wyznaczniku wyrazy z kwadratem L2 się redukują. Następnie tożsamość różnicy sinusów eliminuje Q1.

$$
\det J=L_1L_2\sin(Q_2)
$$

![Dwa wektorowe wkłady prędkości przegubów sumują się do prędkości narzędzia.](../../../assets/figures/two_link_jacobian_velocity.svg)

*Dwa wektory prędkości przegubów sumowane do prędkości końcówki.*

### Pełne przykłady kontrolne

1. Sztywny człon 150 mm wskazuje w prawo (Q=0°). Przy ω=+0.1 rad/s otrzymujemy vx=0, vy=150·0.1=+15 mm/s. Końcówka porusza się w górę.
2. Dla Q=45° i ω=−0.1 rad/s (zgodnie ze wskazówkami zegara): vx=−150·sin45°·(−0.1)=+10.61 mm/s, vy=150·cos45°·(−0.1)=−10.61 mm/s. Końcówka przesuwa się w prawo i w dół; moduł prędkości to nadal 15 mm/s.
3. Przy L1=100 mm, L2=50 mm, Q1=30°, Q2=60°, ω₁=0.1 rad/s, ω₂=0.2 rad/s bezwzględna prędkość kątowa drugiego członu wynosi 0.3 rad/s. Wówczas $v_x=-100\cdot\sin30^\circ\cdot0.1-50\cdot\sin90^\circ\cdot0.3=-5-15=-20\ \mathrm{mm/s}$; $v_y=100\cdot\cos30^\circ\cdot0.1+50\cdot\cos90^\circ\cdot0.3\approx+8.66\ \mathrm{mm/s}$. Zapis pośredni $-5-15=-20$ pokazuje osobny wkład każdego przegubu.
4. Przy $\delta=0.02\ \mathrm{rad}$ od pozycji złożonej zmiana wzdłuż osi nieruchomej wynosi $\Delta x_{\mathrm{axis}}\approx25\delta^2=25\cdot0.02^2=0.010\ \mathrm{mm}$; przemieszczenie poprzeczne $\Delta y\approx50\delta=1.000\ \mathrm{mm}$; wzrost odległości promieniowej $\Delta r\approx50\cdot0.02^2=0.020\ \mathrm{mm}$. Nie wolno mylić współczynników obu wielkości kwadratowych.

[Trygonometria](../TRIGONOMETRY.md) · [Układy współrzędnych](04-coordinate-frames.md) · [Podstawy analizy](00-calculus-foundations.md)
