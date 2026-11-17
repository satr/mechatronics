# Trigonometrie: Winkel, Sinus, Kosinus, Tangens und Arkustangens

**Sprachen:** [en](../en/TRIGONOMETRY.md) · [fr](../fr/TRIGONOMETRY.md) · [de](TRIGONOMETRY.md) · [it](../it/TRIGONOMETRY.md) · [es](../es/TRIGONOMETRY.md) · [pt](../pt/TRIGONOMETRY.md) · [zh](../zh/TRIGONOMETRY.md) · [ja](../ja/TRIGONOMETRY.md) · [nb](../nb/TRIGONOMETRY.md) · [ru](../ru/TRIGONOMETRY.md) · [ko](../ko/TRIGONOMETRY.md) · [fi](../fi/TRIGONOMETRY.md) · [pl](../pl/TRIGONOMETRY.md)

**Hier verwendete Einheiten (vor den Beispielen erklärt):** `°` — Grad; `rad` — Radiant; `kg` — Kilogramm; `m` — Meter; `m/s²` — Meter / Sekunde² — Beschleunigung; `N·m` — Newton · Meter — Drehmoment; `mm` — Millimeter = 0.001 m; `N` — Newton. [Einheitenverzeichnis](UNITS.md).

[README](README.md) · [Calculus](notes/00-calculus-foundations.md) · [Integral table](INTEGRAL_TABLE.md)

<a id="unit-circle-values"></a>
## Einheitskreis: Sinus und Kosinus

Ein Punkt des Einheitskreises bei Winkel θ hat die Koordinaten **(cos θ, sin θ)**. Winkel werden von +X gegen den Uhrzeigersinn gemessen. Kosinus (cosine) ist horizontal, Sinus (sine) vertikal. Nur ein Diagramm zeigt alle 16 exakten Paare; eine einzige Tabelle ergänzt Dezimalwerte, Tangens und Arkustangens-Hauptwerte.

![Ein Einheitskreis mit 16 Winkeln und exakten Koordinatenpaaren (cos θ, sin θ).](../../assets/figures/unit_circle_reference.svg)

*Ein Einheitskreis mit 16 Winkeln und exakten Koordinatenpaaren (cos θ, sin θ).*

**Exakte Brüche und Dezimalnäherungen:**

| θ | cos θ (exakt) | cos θ (dezimal) | sin θ (exakt) | sin θ (dezimal) | tan θ (exakt) | tan θ (dezimal) | arctan(tan θ), Hauptwert |
| --- | --- | ---: | --- | ---: | --- | ---: | --- |
| 0° | $1$ | 1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 30° | $\frac{\sqrt3}{2}$ | 0.8660 | $\frac12$ | 0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 45° | $\frac{\sqrt2}{2}$ | 0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 60° | $\frac12$ | 0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 90° | $0$ | 0.0000 | $1$ | 1.0000 | **undefiniert** | — | — |
| 120° | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 135° | $-\frac{\sqrt2}{2}$ | -0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 150° | $-\frac{\sqrt3}{2}$ | -0.8660 | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |
| 180° | $-1$ | -1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 210° | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 225° | $-\frac{\sqrt2}{2}$ | -0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 240° | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 270° | $0$ | 0.0000 | $-1$ | -1.0000 | **undefiniert** | — | — |
| 300° | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 315° | $\frac{\sqrt2}{2}$ | 0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 330° | $\frac{\sqrt3}{2}$ | 0.8660 | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |

Tangens ist bei 90° und 270° **nicht definiert**, da cos θ = 0; arctan(tan θ) ist dort ebenfalls nicht definiert. Die letzte Spalte zeigt den **Hauptwert** zwischen −90° und 90°, nicht immer den Ausgangswinkel: arctan(tan 135°) = −45° und arctan(tan 225°) = 45°. Dezimalwerte sind auf vier Stellen gerundet. Bei 360° gelten wieder die Werte von 0°.

<a id="trigonometric-identities"></a>
### Nützliche trigonometrische Identitäten

Eine Verschiebung um 90° vertauscht Sinus und Kosinus, manchmal mit Vorzeichenwechsel. Klammern sind entscheidend: cos(θ − 90°) berechnet den Kosinus der Winkeldifferenz, nicht cos θ minus 90.

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

**Negative Winkel und Periodizität:**

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

Vorzeichen je Quadrant (cos, sin, tan): I (+,+,+), II (−,+,−), III (−,−,+), IV (+,−,−). Negative Winkel verlaufen im Uhrzeigersinn.

Bei inversen Funktionen Quadrant und Hauptwertebereich prüfen.

<a id="inverse-cosine-reference"></a>
### Arkuskosinus und Winkelabschätzung

Zwischen 0° und 180° sinkt der Kosinus von 1 auf −1. arccos(0.19) liegt knapp unter 80°: cos 80°≈0.1736 und arccos(0.19)≈79.05°. Wegen cos(+θ)=cos(−θ) können zwei vorzeichenverschiedene Gelenklösungen möglich sein. Der Hauptwert von arccos liegt zwischen 0° und 180°.

![cos θ versus θ, with arccos(0.19) marked](../../assets/figures/arccos_reference_curve.svg)



## Bild: Gegenkathete, Ankathete und Hypotenuse

![Drei rechtwinklige Dreiecke: Sinus = Gegenkathete a durch Hypotenuse c, Kosinus = Ankathete b durch c, Tangens = a durch b.](../../assets/figures/trig_ratios.svg)

In der Zeichnung ist **a** die Gegenkathete, **b** die Ankathete und **c** die Hypotenuse zum markierten Winkel θ. Für einen spitzen Winkel gelten $\sin\theta=a/c$, $\cos\theta=b/c$ und $\tan\theta=a/b$ (nur bei $b\ne0$). **Seitenlängen sind nichtnegativ**; die Zeichnung allein erklärt keine Vorzeichen bei negativen Winkeln oder in anderen Quadranten. Bei einem gerichteten Winkel ab der positiven x-Achse gilt $\sin(+60^\circ)=+\sqrt3/2$, aber $\sin(-60^\circ)=-\sqrt3/2$.

## Mechanik: Gewichtsmoment am Hebel

Für eine Masse m im Abstand L vom Drehpunkt und einen Winkel θ über der Horizontalen ist der **Betrag** des Gewichtsmoments mgL|cos θ|. Das Vorzeichen richtet sich nach der Drehrichtungskonvention.

$$
|M_g|=mgL|\cos\theta|.
$$

Bei m = 0.5 kg, L = 0.2 m, g = 9.81 m/s² und θ = 60° beträgt der Betrag 0.4905 N·m, bei 0° 0.981 N·m und bei 90° null (idealisierte Punktlast).

## Umkehraufgabe: Winkel aus Steigung

Eine Achse steigt 0.05 m über 0.1 m Horizontalweg. Das Verhältnis beträgt 0.5 und der Winkel ist θ = arctan(0.5) ≈ 26.565°. Das Argument ist kein Gradwert.

$$
\tan\theta=\frac{0.05\ \mathrm{m}}{0.1\ \mathrm{m}}=0.5,\qquad \theta=\arctan(0.5)\approx26.565^\circ.
$$

Umrechnung: θ_rad = θ_deg·π/180. In numerischen Bibliotheken werden meist Radiant erwartet.

$$
\theta_{\mathrm{rad}}=\theta_{\mathrm{deg}}\frac{\pi}{180}.
$$

### Richtung eines Vektors: Warum `atan2` nötig ist

Für einen Vektor vom Ursprung nach $(x,y)$ sieht der einfache Arkustangens nur das Verhältnis $y/x$. Die Vektoren $(1, -1)$ und $(-1, 1)$ haben dasselbe Verhältnis, zeigen aber in **verschiedene Quadranten**. Bei $x=-1\ \mathrm{mm}$ und $y=+1\ \mathrm{mm}$ führt das Verhältnis allein zur falschen Weltrichtung:

$$
\arctan\left(\frac{y}{x}\right)=\arctan(-1)=-45^\circ,\qquad
\operatorname{atan2}(+1, -1)=+135^\circ.
$$

`atan2(y, x)` berücksichtigt die Vorzeichen **beider Komponenten** und liefert die Richtung eines von null verschiedenen 2D-Vektors. Beide Argumente benötigen dieselbe Längeneinheit. Bei $x=0$ ist $y/x$ undefiniert, während `atan2` für $y\ne0$ noch eine Achsenrichtung liefert. Für $(0, 0)$ ist keine Richtung definiert; $+180^\circ$ und $-180^\circ$ bezeichnen dieselbe Richtung. Das ist beim Bestimmen von [Koordinatensystemwinkeln](notes/04-coordinate-frames.md) wichtig.

## Kosinussatz: Geometrie von zwei Gliedern

![Two-link robot triangle OAB, exact link lengths and the law of cosines](../../assets/figures/two_link_cosine_law.svg)

Basis O, Gelenk A und Werkzeug B bilden ein Dreieck: OA = L1, AB = L2 und OB = r, der direkte Abstand von Basis zu Werkzeug. Das Bild zeigt L1 = 100 mm, L2 = 50 mm, r = 120 mm. Der Innenwinkel φ unterscheidet sich vom relativen Gelenkwinkel θ2: φ = 180° − |θ2|. Das Bild zeigt negatives θ2, die gespiegelte Lage positives θ2.

Der Kosinussatz lautet $r^2=L_1^2+L_2^2-2L_1L_2\cos\varphi$. Wegen $\cos(180^\circ-|\theta_2|)=-\cos\theta_2$ folgt $r^2=L_1^2+L_2^2+2L_1L_2\cos\theta_2$, also $\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}$. Hier ist $(14400-10000-2500)/10000=0.19$ und $|\theta_2|\approx79.05^\circ$. Für eine konkrete Position (X,Y) muss danach θ1 bestimmt werden.


[Differentialrechnung](notes/00-calculus-foundations.md) · [Regelungstechnik](notes/03-feedback-control.md)
