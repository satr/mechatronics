# Trygonometria: kąty, sinus, cosinus, tangens i arcus tangens

**Języki:** [en](../en/TRIGONOMETRY.md) · [fr](../fr/TRIGONOMETRY.md) · [de](../de/TRIGONOMETRY.md) · [it](../it/TRIGONOMETRY.md) · [es](../es/TRIGONOMETRY.md) · [pt](../pt/TRIGONOMETRY.md) · [zh](../zh/TRIGONOMETRY.md) · [ja](../ja/TRIGONOMETRY.md) · [nb](../nb/TRIGONOMETRY.md) · [ru](../ru/TRIGONOMETRY.md) · [ko](../ko/TRIGONOMETRY.md) · [fi](../fi/TRIGONOMETRY.md) · [pl](TRIGONOMETRY.md)

**Jednostki tej części (wyjaśnione przed przykładami):** `°` — stopień kąta płaskiego; `rad` — radian; `kg` — kilogram; `m` — metr; `m/s²` — metr na sekundę do kwadratu (przyspieszenie); `N·m` — niutonometr (moment siły); `mm` — milimetr; `N` — niuton (siła). [Pełny słownik jednostek](UNITS.md).

[Spis treści](README.md) · [Analiza matematyczna](notes/00-calculus-foundations.md) · [Tablica całek](INTEGRAL_TABLE.md)

<a id="unit-circle-values"></a>
## Okrąg jednostkowy: sinus i cosinus

Na okręgu jednostkowym punkt odpowiadający kątowi θ ma współrzędne **(cos θ, sin θ)**. Kąt mierzymy od dodatniej osi X przeciwnie do ruchu wskazówek zegara. Składowa pozioma odpowiada cosinusowi, a pionowa sinusowi. Rysunek przedstawia dokładne pary ze znakami dla 16 kątów, a jedna zbiorcza tabela uzupełnia je o przybliżenia, tangens oraz główną wartość arcus tangensa.

![Okrąg jednostkowy i 16 kątów ze znakami współrzędnych (cos θ, sin θ).](../../assets/figures/unit_circle_reference.svg)

*Jeden okrąg jednostkowy z 16 parami współrzędnych (cos θ, sin θ).*

**Dokładne wartości i przybliżenia dziesiętne:**

| θ | cos θ (dokładnie) | cos θ (dziesiętnie) | sin θ (dokładnie) | sin θ (dziesiętnie) | tan θ (dokładnie) | tan θ (dziesiętnie) | arctan(tan θ) — wartość główna |
| --- | --- | ---: | --- | ---: | --- | ---: | --- |
| 0° | $1$ | 1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 30° | $\frac{\sqrt3}{2}$ | 0.8660 | $\frac12$ | 0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 45° | $\frac{\sqrt2}{2}$ | 0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 60° | $\frac12$ | 0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 90° | $0$ | 0.0000 | $1$ | 1.0000 | **nieokreślony** | — | — |
| 120° | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 135° | $-\frac{\sqrt2}{2}$ | -0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 150° | $-\frac{\sqrt3}{2}$ | -0.8660 | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |
| 180° | $-1$ | -1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 210° | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 225° | $-\frac{\sqrt2}{2}$ | -0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 240° | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 270° | $0$ | 0.0000 | $-1$ | -1.0000 | **nieokreślony** | — | — |
| 300° | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 315° | $\frac{\sqrt2}{2}$ | 0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 330° | $\frac{\sqrt3}{2}$ | 0.8660 | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |

Tangens jest **nieokreślony** dla 90° i 270°, ponieważ cos θ = 0; także arctan(tan θ) nie ma tam wartości. Ostatnia kolumna zawiera **wartość główną** z przedziału (−90°, 90°), niekoniecznie pierwotny kąt: na przykład arctan(tan 135°) = −45°, natomiast arctan(tan 225°) = 45°. Wyniki dziesiętne zaokrąglono do czterech miejsc. Dla θ = 360° sinus i cosinus przyjmują te same wartości co dla 0°.

<a id="trigonometric-identities"></a>
### Przydatne tożsamości trygonometryczne

Przesunięcie o 90° zamienia sinus z cosinusem, czasami zmieniając znak. Nawiasy są istotne: cos(θ − 90°) oznacza obliczenie cosinusa *po odjęciu kąta*, a nie odjęcie 90 od wartości cos θ.

$$
\cos(90^\circ-\theta)=\sin(\theta),\qquad
\sin(90^\circ-\theta)=\cos(\theta)
$$

$$
\cos(\theta-90^\circ)=\sin(\theta),\qquad
\sin(\theta+90^\circ)=\cos(\theta)
$$

$$
\cos(\theta+90^\circ)=-\sin(\theta),\qquad
\sin(\theta-90^\circ)=-\cos(\theta)
$$

**Kąty ujemne i okresowość:**

$$
\sin(-\theta)=-\sin(\theta),\qquad
\cos(-\theta)=\cos(\theta)
$$

$$
\tan(-\theta)=-\tan(\theta),\qquad
\tan(\theta)=\frac{\sin(\theta)}{\cos(\theta)}
$$

$$
\sin(\theta+360^\circ)=\sin(\theta),\qquad
\cos(\theta+360^\circ)=\cos(\theta)
$$

$$
\tan(\theta+180^\circ)=\tan(\theta),\qquad
\sin^2(\theta)+\cos^2(\theta)=1
$$

Znaki funkcji w ćwiartkach (w kolejności cos, sin, tan): I (+,+,+), II (−,+,−), III (−,−,+), IV (+,−,−). Kąt ujemny mierzymy zgodnie z ruchem wskazówek zegara.

Przy szacowaniu kątów odwrotnych zwracaj uwagę na znaki na okręgu oraz przedział monotoniczności danej funkcji.

<a id="inverse-cosine-reference"></a>
### Arcus cosinus i szacowanie kąta

W przedziale 0°–180° cos θ maleje od 1 do −1. Dlatego arccos(0.19) jest nieco mniejszy od 80°: cos 80°≈0.1736, a arccos(0.19)≈79.05°. Cosinus jest funkcją parzystą, więc cos(+79.05°)=cos(−79.05°). Możliwe są dwie konfiguracje łokcia o przeciwnych znakach, chociaż główna wartość arccos należy do [0°,180°]. Wykres przedstawia malejący cosinus.

![Wykres cos θ z zaznaczonym arccos(0.19).](../../assets/figures/arccos_reference_curve.svg)



## Trójkąt prostokątny: przyprostokątne i przeciwprostokątna

![Trzy trójkąty prostokątne: sinus to stosunek przeciwległej przyprostokątnej a do przeciwprostokątnej c, cosinus — sąsiedniej b do c, tangens — a do b.](../../assets/figures/trig_ratios.svg)

Na schemacie **a** jest przyprostokątną naprzeciw kąta θ, **b** — przyprostokątną przyległą, a **c** — przeciwprostokątną. Dla kąta ostrego w trójkącie prostokątnym $\sin\theta=a/c$, $\cos\theta=b/c$, $\tan\theta=a/b$ (gdy $b\ne0$). **Długości boków są nieujemne.** Ten rysunek nie pokazuje znaków sinusa i cosinusa dla kątów ujemnych lub innych ćwiartek: $\sin(+60^\circ)=+\sqrt3/2$, a $\sin(-60^\circ)=-\sqrt3/2$.

## Przykład mechaniczny: moment siły ciężkości na dźwigni

Dla masy $m$ w odległości $L$ od osi obrotu i dźwigni ustawionej pod kątem θ do poziomu **wartość bezwzględna** momentu grawitacyjnego wynosi $mgL|\cos\theta|$. Znak rzeczywistego momentu wynika z przyjętego zwrotu obrotu.

$$
|M_g|=mgL|\cos\theta|.
$$

Dla $m=0.5\ \mathrm{kg}$, $L=0.2\ \mathrm{m}$ i $g=9.81\ \mathrm{m/s^2}$ moment przy θ = 60° wynosi $0.4905\ \mathrm{N\cdot m}$. Przy 0° jest równy $0.981\ \mathrm{N\cdot m}$, a przy 90° jest zerowy — w tym wyidealizowanym modelu obciążenia punktowego.

## Przykład odwrotny: wyznaczanie kąta z geometrii

Jeżeli oś narzędzia wznosi się o 0.05 m na odcinku poziomym 0.1 m, stosunek wynosi 0.5. Zatem θ = arctan(0.5) ≈ 26.565°. Argumentem jest **bezwymiarowy stosunek długości**, nie »0.5 stopnia«.

$$
\tan\theta=\frac{0.05\ \mathrm{m}}{0.1\ \mathrm{m}}=0.5,\qquad \theta=\arctan(0.5)\approx26.565^\circ.
$$

Przeliczenie stopni na radiany: θ_rad = θ_deg·π/180. Biblioteki matematyczne zazwyczaj oczekują radianów.

$$
\theta_{\mathrm{rad}}=\theta_{\mathrm{deg}}\frac{\pi}{180}.
$$

### Kierunek wektora: dlaczego potrzebujemy `atan2`

Dla wektora od początku układu do $(x,y)$ zwykły arcus tangens widzi tylko iloraz $y/x$. Wektory $(1, -1)$ i $(-1, 1)$ mają taki sam iloraz, lecz są skierowane do **różnych ćwiartek**. Przy $x=-1\ \mathrm{mm}$ oraz $y=+1\ \mathrm{mm}$ sam iloraz daje błędny kierunek w układzie świata:

$$
\arctan\left(\frac{y}{x}\right)=\arctan(-1)=-45^\circ,\qquad
\operatorname{atan2}(+1, -1)=+135^\circ.
$$

Do wyznaczania kierunku niezerowego wektora 2D używaj `atan2(y, x)`, ponieważ uwzględnia znaki **obu składowych**. Argumenty muszą mieć tę samą jednostkę długości. Gdy $x=0$, iloraz $y/x$ jest nieokreślony, ale `atan2` zwraca kierunek osi, jeżeli $y\ne0$. Dla $(0, 0)$ kierunek nie istnieje. Kąty +180° i −180° oznaczają ten sam kierunek. Rozróżnienie jest ważne przy [zmianie układów współrzędnych](notes/04-coordinate-frames.md).

## Prawo cosinusów: geometria ramienia z dwoma członami

![Trójkąt robota dwuprzegubowego OAB i prawo cosinusów.](../../assets/figures/two_link_cosine_law.svg)

Baza O, łokieć A i narzędzie B tworzą trójkąt: OA = L1, AB = L2, OB = r (bezpośrednia odległość bazy od narzędzia). Na rysunku L1 = 100 mm, L2 = 50 mm, r = 120 mm. Kąt wewnętrzny φ różni się od względnego kąta przegubu θ2: φ = 180° − |θ2|. Rysunek przedstawia ujemne θ2, a lustrzana konfiguracja dodatnie θ2.

Prawo cosinusów ma postać $r^2=L_1^2+L_2^2-2L_1L_2\cos\varphi$. Ponieważ $\cos(180^\circ-|\theta_2|)=-\cos\theta_2$, równoważnie $r^2=L_1^2+L_2^2+2L_1L_2\cos\theta_2$. Stąd $\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}$. W przykładzie $(14400-10000-2500)/10000=0.19$, czyli $|\theta_2|\approx79.05^\circ$. Aby osiągnąć zadane (X,Y), trzeba jeszcze wyznaczyć pierwszy kąt przegubu θ1.


[Podstawy analizy](notes/00-calculus-foundations.md) · [Sterowanie ze sprzężeniem zwrotnym](notes/03-feedback-control.md)
