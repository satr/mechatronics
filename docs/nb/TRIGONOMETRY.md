# Trigonometri: vinkler, sinus, cosinus, tangens og arctangens

**Språk:** [en](../en/TRIGONOMETRY.md) · [fr](../fr/TRIGONOMETRY.md) · [de](../de/TRIGONOMETRY.md) · [it](../it/TRIGONOMETRY.md) · [es](../es/TRIGONOMETRY.md) · [pt](../pt/TRIGONOMETRY.md) · [zh](../zh/TRIGONOMETRY.md) · [ja](../ja/TRIGONOMETRY.md) · [nb](TRIGONOMETRY.md) · [ru](../ru/TRIGONOMETRY.md) · [ko](../ko/TRIGONOMETRY.md) · [fi](../fi/TRIGONOMETRY.md) · [pl](../pl/TRIGONOMETRY.md)

**Enheter på denne siden (forklart før eksemplene):** `°` — grad; `rad` — radian; `kg` — kilogram; `m` — meter; `m/s²` — meter / sekund² — akselerasjon; `N·m` — newton · meter — dreiemoment; `mm` — millimeter = 0.001 m; `N` — newton. [Enhetsoversikt](UNITS.md).

[README](README.md) · [Calculus](notes/00-calculus-foundations.md) · [Integral table](INTEGRAL_TABLE.md)

<a id="unit-circle-values"></a>
## Enhetssirkelen: sinus og cosinus

Et punkt ved vinkel θ på enhetssirkelen har koordinatene **(cos θ, sin θ)**. Vinkler måles mot klokken fra +X. Cosinus (cosine) er horisontal, sinus (sine) vertikal. Ett diagram viser eksakte koordinatpar for alle 16 vanlige vinkler; én tabell legger til desimaler, tangens og hovedverdien av arctan.

![Én enhetssirkel med 16 vinkler og eksakte koordinatpar (cos θ, sin θ).](../../assets/figures/unit_circle_reference.svg)

*Én enhetssirkel med 16 vinkler og eksakte koordinatpar (cos θ, sin θ).*

**Eksakte brøker og desimaltilnærminger:**

| θ | cos θ (eksakt) | cos θ (desimal) | sin θ (eksakt) | sin θ (desimal) | tan θ (eksakt) | tan θ (desimal) | arctan(tan θ), hovedverdi |
| --- | --- | ---: | --- | ---: | --- | ---: | --- |
| 0° | $1$ | 1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 30° | $\frac{\sqrt3}{2}$ | 0.8660 | $\frac12$ | 0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 45° | $\frac{\sqrt2}{2}$ | 0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 60° | $\frac12$ | 0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 90° | $0$ | 0.0000 | $1$ | 1.0000 | **udefinert** | — | — |
| 120° | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 135° | $-\frac{\sqrt2}{2}$ | -0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 150° | $-\frac{\sqrt3}{2}$ | -0.8660 | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |
| 180° | $-1$ | -1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 210° | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 225° | $-\frac{\sqrt2}{2}$ | -0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 240° | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 270° | $0$ | 0.0000 | $-1$ | -1.0000 | **udefinert** | — | — |
| 300° | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 315° | $\frac{\sqrt2}{2}$ | 0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 330° | $\frac{\sqrt3}{2}$ | 0.8660 | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |

Tangens er **udefinert** ved 90° og 270° fordi cos θ = 0. Dermed er arctan(tan θ) også udefinert. Siste kolonne viser **hovedverdien** mellom −90° og 90°, som ikke alltid er den opprinnelige vinkelen: arctan(tan 135°) = −45° og arctan(tan 225°) = 45°. Desimaler er avrundet til fire plasser. Ved 360° gjentas verdiene fra 0°.

<a id="trigonometric-identities"></a>
### Nyttige trigonometriske identiteter

Et skift på 90° bytter sinus og cosinus, noen ganger med fortegnsskifte. Parentesene er avgjørende: cos(θ − 90°) betyr cosinus av vinkelforskjellen, ikke cos θ minus 90.

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

**Negative vinkler og periodisitet:**

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

Fortegn per kvadrant (cos, sin, tan): I (+,+,+), II (−,+,−), III (−,−,+), IV (+,−,−). Negative vinkler måles med klokken.

Ved invers trigonometrisk beregning må man kontrollere kvadrant og hovedverdiområde.

<a id="inverse-cosine-reference"></a>
### Invers cosinus og vinkelanslag

Fra 0° til 180° avtar cosinus fra 1 til −1. Dermed er arccos(0.19) litt mindre enn 80°: cos 80°≈0.1736 og arccos(0.19)≈79.05°. Siden cos(+θ)=cos(−θ), kan to leddvinkelløsninger med ulikt fortegn finnes. Hovedverdien av arccos ligger mellom 0° og 180°.

![cos θ versus θ, with arccos(0.19) marked](../../assets/figures/arccos_reference_curve.svg)



## Figur: motstående katet, hosliggende katet og hypotenus

![Tre rettvinklede trekanter: sinus = motstående a delt på hypotenus c, cosinus = hosliggende b delt på c, tangens = a delt på b.](../../assets/figures/trig_ratios.svg)

I figuren er **a** motstående katet (opposite) til vinkelen θ, **b** hosliggende katet (adjacent) og **c** hypotenusen (hypotenuse). For en spiss vinkel er $\sin\theta=a/c$, $\cos\theta=b/c$ og $\tan\theta=a/b$ (når $b\ne0$). **Sidelengder er ikke-negative**; figuren alene viser ikke fortegnene ved negative vinkler eller i andre kvadranter. For en orientert vinkel fra positiv x-akse er $\sin(+60^\circ)=+\sqrt3/2$, mens $\sin(-60^\circ)=-\sqrt3/2$.

## Mekanikk: gravitasjonsmoment på en arm

For en masse m i avstand L fra omdreiningspunktet og armen i vinkel θ over horisontalen er **størrelsen** på gravitasjonsmomentet mgL|cos θ|. Fortegnet avhenger av valgt positiv rotasjonsretning.

$$
|M_g|=mgL|\cos\theta|.
$$

Med m = 0.5 kg, L = 0.2 m, g = 9.81 m/s² og θ = 60° er størrelsen 0.4905 N·m. Ved 0° er den 0.981 N·m og ved 90° null (ideell punktlast).

## Omvendt eksempel: vinkel fra stigning

En akse stiger 0.05 m på 0.1 m horisontal forflytning. Forholdet er 0.5, så θ = arctan(0.5) ≈ 26.565°. Argumentet er et forhold, ikke grader.

$$
\tan\theta=\frac{0.05\ \mathrm{m}}{0.1\ \mathrm{m}}=0.5,\qquad \theta=\arctan(0.5)\approx26.565^\circ.
$$

Omregning: θ_rad = θ_deg·π/180. Numeriske biblioteker bruker vanligvis radianer.

$$
\theta_{\mathrm{rad}}=\theta_{\mathrm{deg}}\frac{\pi}{180}.
$$

### Vektorretning: hvorfor `atan2` er nødvendig

For en vektor fra origo til $(x,y)$ bruker vanlig arctan bare forholdet $y/x$. Vektorene $(1, -1)$ og $(-1, 1)$ har samme forhold, men peker i **ulike kvadranter**. Med $x=-1\ \mathrm{mm}$ og $y=+1\ \mathrm{mm}$ gir forholdet alene feil retning i verdensrammen:

$$
\arctan\left(\frac{y}{x}\right)=\arctan(-1)=-45^\circ,\qquad
\operatorname{atan2}(+1, -1)=+135^\circ.
$$

`atan2(y, x)` tar hensyn til fortegnet til **begge komponentene** og gir retningen til en ikke-null 2D-vektor. Argumentene må bruke samme lengdeenhet. Ved $x=0$ er $y/x$ udefinert, men `atan2` gir fortsatt akseretningen når $y\ne0$. For $(0, 0)$ finnes ingen definert retning; $+180^\circ$ og $-180^\circ$ er samme retning. Dette er viktig for [vinkler i koordinatsystemer](notes/04-coordinate-frames.md).

## Cosinussetningen: geometrien til to lenker

![Two-link robot triangle OAB, exact link lengths and the law of cosines](../../assets/figures/two_link_cosine_law.svg)

Basen O, leddet A og verktøyet B danner en trekant: OA = L1, AB = L2 og OB = r (rett avstand fra base til verktøy). Figuren bruker L1 = 100 mm, L2 = 50 mm, r = 120 mm. Den indre vinkelen φ er ulik den relative leddvinkelen θ2: φ = 180° − |θ2|. Figuren viser negativ θ2, speilbildet positiv θ2.

Cosinussetningen (law of cosines) gir $r^2=L_1^2+L_2^2-2L_1L_2\cos\varphi$. Fordi $\cos(180^\circ-|\theta_2|)=-\cos\theta_2$, får vi $r^2=L_1^2+L_2^2+2L_1L_2\cos\theta_2$, altså $\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}$. Her er $(14400-10000-2500)/10000=0.19$ og $|\theta_2|\approx79.05^\circ$. For et bestemt punkt (X,Y) trengs også θ1.


[Differensialregning](notes/00-calculus-foundations.md) · [Tilbakekoblingsregulering](notes/03-feedback-control.md)
