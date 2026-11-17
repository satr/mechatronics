# 0. Grundlagen der Analysis: Ableitungen, Grenzwerte und Integrale aus der Mechanik

**Sprachen:** [en](../../en/notes/00-calculus-foundations.md) · [fr](../../fr/notes/00-calculus-foundations.md) · [de](00-calculus-foundations.md) · [it](../../it/notes/00-calculus-foundations.md) · [es](../../es/notes/00-calculus-foundations.md) · [pt](../../pt/notes/00-calculus-foundations.md) · [zh](../../zh/notes/00-calculus-foundations.md) · [ja](../../ja/notes/00-calculus-foundations.md) · [nb](../../nb/notes/00-calculus-foundations.md) · [ru](../../ru/notes/00-calculus-foundations.md) · [ko](../../ko/notes/00-calculus-foundations.md) · [fi](../../fi/notes/00-calculus-foundations.md) · [pl](../../pl/notes/00-calculus-foundations.md)

Die **natürliche Exponentialfunktion** ist $\exp(x)=\mathrm{e}^{x}$, wobei die **Eulersche Zahl** $\mathrm{e}\approx2.71828$ ist. Sie beschreibt stetiges Wachstum oder Abklingen; $\exp(0)=1$ und $\exp(-1)\approx0.3679$. Der natürliche Logarithmus $\ln$ ist ihre Umkehrfunktion: $\ln(\exp(x))=x$. Siehe [Symbolübersicht](../SYMBOLS.md).

**Hier verwendete Einheiten (vor den Beispielen erklärt):** `s` — Sekunde; `mm` — Millimeter = 0.001 m; `mm/s` — Millimeter / Sekunde — lineare Geschwindigkeit; `mm/s²` — Millimeter / Sekunde² — Beschleunigung; `kg·m²` — Kilogramm · Meter² — Trägheitsmoment; `rad/s` — Radiant / Sekunde — Winkelgeschwindigkeit; `rad/s²` — Radiant / Sekunde² — Winkelbeschleunigung; `N·m` — Newton · Meter — Drehmoment; `W` — Watt; `rpm` — Umdrehung pro Minute; `N/m` — Newton / Meter — Steifigkeit; `mm³/s` — Millimeter³ / Sekunde — Volumenstrom; `%` — Prozent (ein Hundertstel); `m` — Meter; `kg` — Kilogramm; `N` — Newton; `J` — Joule; `rad` — Radiant. [Einheitenverzeichnis](../UNITS.md).

[README](../README.md) · [Integral table](../INTEGRAL_TABLE.md) · [Trigonometry table](../TRIGONOMETRY.md) · [Motion](01-motion-calculus.md) · [Dynamics](02-first-order-dynamics.md) · [Symbols](../SYMBOLS.md)

> **Lernmodell:** Modelle und Einheiten prüfen; Demo-Code nicht an echte Anlagen anschließen.

Die **Ableitung (derivative)** beschreibt die momentane Änderungsrate, die **zweite Ableitung (second derivative)** die Änderung dieser Rate. Das **Integral (integral)** summiert Änderungen. Ein **Grenzwert (limit)** definiert die momentane Rate; ein **Logarithmus (logarithm)** hilft, aus einer exponentiellen Antwort die Zeit zu bestimmen.

Diese Werkzeuge begegnen uns an einer Maschinenachse, einem Servoantrieb, einem Robotergelenk, einer Feder oder einem Sensor. Zuerst steht die physikalische Frage, danach folgen Rechenregel und Einheit.

## Inhalt

- [1. Von Messwertänderungen zum mathematischen Modell](#section-1)
- [2. Grenzwerte und erste Ableitungen](#section-2)
- [3. Erste und zweite Ableitung: eine bewegte Achse](#section-3)
- [4. Kettenregel: Rotationsenergie](#section-4)
- [5. Exponentialfunktion und Logarithmus: Einschwingzeit](#section-5)
- [6. Integrale: Wegänderung und mechanische Arbeit](#section-6)
- [7. Weiteres Beispiel: wachsender Kugelradius](#section-7)
- [8. Einheiten, Kontrollen und Übungen](#section-8)

<a id="section-1"></a>
## 1. Von Messwertänderungen zum mathematischen Modell

| Physikalische Frage | Mathematisches Werkzeug |
| --- | --- |
| Wie schnell bewegt sich die Achse **jetzt**? | Erste Ableitung $dx/dt$ |
| Wie ändert sich ihre Geschwindigkeit? | Zweite Ableitung $d^2x/dt^2$ |
| Wann erreicht die Antwort 90 %? | Logarithmus $\ln$ |
| Wie groß ist die Wegänderung in 2 s? | Bestimmtes Integral $\int v\ \mathrm{d}t$ |
| Wie viel Arbeit verrichtet eine variable Kraft? | Integral $\int F\ \mathrm{d}x$ |

<a id="section-2"></a>
## 2. Grenzwerte und erste Ableitungen

Der **Differenzenquotient (finite difference)** zweier Messungen ist eine mittlere Änderungsrate über ein Intervall. Die Ableitung ist sein Grenzwert für immer kleinere Intervalle.

$$
v(t)=\frac{dx}{dt}=\lim_{h\to0}\frac{x(t+h)-x(t)}{h}.
$$

Für die Position $x(t)=a t^2$ mit $a=2\ \mathrm{mm/s^2}$ entwickeln wir zuerst den Zähler:

$$
\frac{x(t+h)-x(t)}h=\frac{a[(t+h)^2-t^2]}h=a(2t+h)\longrightarrow 2at.
$$

Der Faktor $h$ wird **vor** dem Grenzübergang gekürzt. Bei $t=1\ \mathrm{s}$ beträgt die momentane Geschwindigkeit $4\ \mathrm{mm/s}$. Ein undefinierter Ausdruck $0/0$ wird nicht direkt eingesetzt.

**Wichtige Ableitungsregeln (differentiation rules)**: $c$ und $n$ sind konstant; trigonometrische Argumente sind im Bogenmaß.

| Regel | Formel |
| --- | --- |
| Konstante | $\frac{d}{dt}c=0$ |
| Potenz | $\frac{d}{dt}t^n=n t^{n-1}$ |
| Koeffizient und Summe | $(cf+g)'=cf'+g'$ |
| Produkt | $(fg)'=f' g+fg'$ |
| Quotient, $g\ne0$ | $\left(\frac{f}{g}\right)'=\frac{f' g-fg'}{g^2}$ |
| Verkettung | $\frac{d}{dt}f(g(t))=f'(g(t))g'(t)$ |
| Exponential | $\frac{d}{dt}\exp(t)=\exp(t)$ |
| Natürlicher Logarithmus, $t>0$ | $\frac{d}{dt}\ln t=\frac1t$ |
| Sinus / Kosinus | $\frac{d}{dt}\sin t=\cos t$, $\frac{d}{dt}\cos t=-\sin t$ |

![Tangentensteigung und Fläche unter der Geschwindigkeitskurve](../../../assets/figures/calculus_slope_area.svg)

<a id="section-3"></a>
## 3. Erste und zweite Ableitung: eine bewegte Achse

Ein Schlitten startet bei 2 mm mit 3 mm/s Anfangsgeschwindigkeit und 4 mm/s² konstanter Beschleunigung. Die Position lautet:

$$
x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2.
$$

**Erste Ableitung**: Geschwindigkeit. Die Konstante entfällt, der lineare Term liefert 3 mm/s, und der quadratische Term wird linear in $t$.

$$
v(t)=\frac{dx}{dt}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t.
$$

**Zweite Ableitung**: Beschleunigung. Wir leiten die Geschwindigkeit erneut ab. Bei 2 s: Position 16 mm, Geschwindigkeit 11 mm/s, Beschleunigung 4 mm/s².

$$
a(t)=\frac{d^2x}{dt^2}=\frac{dv}{dt}=4\ \mathrm{mm/s^2}.
$$

Die zweite Ableitung hat die Einheit Länge/Zeit². Sie ist **nicht** das Quadrat der ersten Ableitung.

<a id="section-4"></a>
## 4. Kettenregel: Rotationsenergie

Ein rotierendes Schwungrad speichert kinetische Energie. Hängt $\omega$ von der Zeit ab, ändert sich die Energie $E$ über $\omega$: die **Kettenregel (chain rule)**.

$$
E(\omega)=\frac12J\omega^2,\quad \omega=\omega(t),
$$
$$
\frac{dE}{dt}=\frac{dE}{d\omega}\frac{d\omega}{dt}=J\omega\alpha=M\omega=P.
$$

Bei $J=0.01\ \mathrm{kg\cdot m^2}$, $\omega=10\ \mathrm{rad/s}$, $\alpha=2\ \mathrm{rad/s^2}$ beträgt das Drehmoment $J\alpha=0.02\ \mathrm{N\cdot m}$ und die mechanische Leistung $0.2\ \mathrm{W}$. Daraus folgt $P=M\omega$.

<a id="section-5"></a>
## 5. Exponentialfunktion und Logarithmus: Einschwingzeit

In einem einfachen System erster Ordnung nähert sich die Drehzahl dem Endwert exponentiell. $\tau$ ist die **Zeitkonstante (time constant)** in Sekunden.

$$
\omega(t)=\omega_\infty\bigl(1-\exp(-t/\tau)\bigr),\quad t\ge0,\ \tau>0.
$$

Diese Form setzt **Anfangswinkelgeschwindigkeit null**, $\omega(0)=0$, und einen konstanten Endwert $\omega_\infty$ voraus. Ist die Anfangsgeschwindigkeit $\omega_0\ne0$, gilt für dasselbe System erster Ordnung die allgemeine Antwort:

$$
\omega(t)=\omega_\infty+(\omega_0-\omega_\infty)\exp(-t/\tau).
$$

**Beispiel mit Anfangsgeschwindigkeit ungleich null:** Sei $\omega_0=200\ \mathrm{rpm}$, $\omega_\infty=1000\ \mathrm{rpm}$ und $\tau=0.5\ \mathrm{s}$. Nach einer Zeitkonstante ($t=0.5\ \mathrm{s}$) gilt:

$$
\omega(\tau)=1000+(200-1000)\exp(-1)\approx705.7\ \mathrm{rpm}.
$$

Die Antwort hat **63.2 % der Änderung um 800 rpm** erreicht, nicht 63.2 % des Endwerts von 1000 rpm. Bei $t=0$ ergibt sich 200 rpm; langfristig nähert sich der Wert 1000 rpm. Dies ist ein mathematisches Beispiel und kein Motorbefehl.

Die Exponentialfunktion beschreibt den verbleibenden Fehleranteil. Mit dem **natürlichen Logarithmus (natural logarithm)** $\ln$, der Umkehrfunktion von $\exp$, bestimmen wir die dazugehörige **Zeit**. Das Argument $0.1$ ist dimensionslos.

$$
\exp(-t/\tau)=0.1
\quad\Longrightarrow\quad
-\frac{t}{\tau}=\ln(0.1)
\quad\Longrightarrow\quad
t=-\tau\ln(0.1)=\tau\ln(10)\approx2.303\tau.
$$

Bei 90 % der Endwertänderung bleiben 10 % des ursprünglichen Fehlers. Für $\tau=0.5\ \mathrm{s}$ ergibt das ideale Modell etwa 1.151 s. Reale Antriebe können Grenzen und Verzögerungen haben.

Die Ableitung von $\ln z$ ist $1/z$ für $z>0$; bei $z=z(t)$ zusätzlich mit $dz/dt$ multiplizieren. Logarithmusargumente physikalischer Größen müssen dimensionslos sein.

$$
\ln(1)=0,\quad \ln(\mathrm{e})=1,\quad \ln(\mathrm{e}^{z})=z,\quad \frac{d}{dz}\ln z=\frac1z\ (z>0).
$$

<a id="section-6"></a>
## 6. Integrale: Wegänderung und mechanische Arbeit

Ein **unbestimmtes Integral (indefinite integral)** liefert Stammfunktionen (antiderivatives) mit der Konstante $C$. Ein **bestimmtes Integral (definite integral)** summiert die Änderung auf einem Intervall.

$$
\int 4t\ \mathrm{d}t=2t^2+C,\qquad \int t^n\ \mathrm{d}t=\frac{t^{n+1}}{n+1}+C\ (n\ne-1).
$$

**Wegänderung.** Anfangsposition $x_0=2\ \mathrm{mm}$, Geschwindigkeit $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$. Wegänderung von 0 bis 2 s:

$$
\Delta x=\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
$$
$$
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}=6\ \mathrm{mm}+8\ \mathrm{mm}=14\ \mathrm{mm}.
$$

Die Wegänderung beträgt 14 mm; mit dem Anfangswert folgt $x(2)=16\ \mathrm{mm}$. Negative Geschwindigkeit ergibt negative vorzeichenbehaftete Wegänderung, nicht negative Weglänge.

**Federarbeit.** Eine ideale lineare Feder mit $k=200\ \mathrm{N/m}$ wird von $x=0$ bis $x=0.01\ \mathrm{m}$ gedehnt. Die Kraft wächst mit der Dehnung; deshalb integrieren wir die Teil-Arbeiten:

$$
F(x)=kx,\qquad W=\int_0^{0.01\ \mathrm{m}}kx\ \mathrm{d}x
=\left[\frac{kx^2}{2}\right]_0^{0.01\ \mathrm{m}}
=\frac{200\ \mathrm{N/m}}2(0.01\ \mathrm{m})^2=0.01\ \mathrm{J}.
$$

Die Arbeit ist 0.01 J. Die Endkraft $F=2\ \mathrm{N}$ mit dem Gesamtweg zu multiplizieren ergäbe fälschlich 0.02 J: Die Kraft ist nicht konstant.

<a id="section-7"></a>
## 7. Weiteres Beispiel: wachsender Kugelradius

**Optionales Kettenregelbeispiel.** Das Kugelvolumen hängt vom Radius und dieser eventuell von der Zeit ab. Dieselbe Struktur gilt für Schwungradenergie und Winkelgeschwindigkeit.

$$
V(r)=\frac43\pi r^3,\qquad \frac{dV}{dt}=\frac{dV}{dr}\frac{dr}{dt}=4\pi r^2\frac{dr}{dt}.
$$

Bei $r=10\ \mathrm{mm}$ und $dr/dt=1\ \mathrm{mm/s}$ ergibt sich $400\pi\approx1256.64\ \mathrm{mm^3/s}$. Bei $r(t)=10\ \mathrm{mm}+(1\ \mathrm{mm/s^2})t^2$ folgt nach 2 s: $r=14\ \mathrm{mm}$, $dr/dt=4\ \mathrm{mm/s}$ und $3136\pi\approx9852.03\ \mathrm{mm^3/s}$.

<a id="section-8"></a>
## 8. Einheiten, Kontrollen und Übungen

**Kontrolle:** Positionsableitung in m/s und zweite Ableitung in m/s²; Kraft-Weg-Integral in N·m = J; Integrationskonstante $C$ nicht vergessen; Ableitung momentan, Integral aufsummiert; das Differential $\mathrm{d}t$ ist nicht der diskrete Schritt `dt` eines Programms.

**Übungen:** (1) Für $x(t)=5\ \mathrm{mm}+(2\ \mathrm{mm/s})t+(1\ \mathrm{mm/s^2})t^2$ Geschwindigkeit und Beschleunigung bei 3 s. (2) Bei $\tau=1\ \mathrm{s}$ Zeit für 90 % Endwertänderung? (3) Weg bei 4 mm/s in 2 s? **Antworten:** 8 mm/s und 2 mm/s²; ca. 2.303 s; 8 mm.

**Ausführliche Lösungen:**

1. $v(t)=\frac{dx}{dt}=2\ \mathrm{mm/s}+2(1\ \mathrm{mm/s^2})t$; $v(3\ \mathrm{s})=2+2\cdot3=8\ \mathrm{mm/s}$. $a(t)=\frac{dv}{dt}=2\ \mathrm{mm/s^2}$.
2. $f(t)=1-\exp(-t/\tau)=0.9$; $\exp(-t/\tau)=0.1$; $t=-\tau\ln(0.1)=\tau\ln(10)$. $\tau=1\ \mathrm{s}$; $t\approx2.303\ \mathrm{s}$.
3. $\Delta x=\int_0^{2\ \mathrm{s}}(4\ \mathrm{mm/s})\ \mathrm{d}t=(4\ \mathrm{mm/s})(2\ \mathrm{s})=8\ \mathrm{mm}$.


[Integral reference](../INTEGRAL_TABLE.md) · [Trigonometry](../TRIGONOMETRY.md) · [Next: motion](01-motion-calculus.md) · [Python exercises](../exercises/README.md)
