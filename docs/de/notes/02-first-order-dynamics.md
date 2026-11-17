# 2. Dynamik erster Ordnung und Rotation


**Diese Seite lesen auf:** [en](../../en/notes/02-first-order-dynamics.md) · [fr](../../fr/notes/02-first-order-dynamics.md) · [de](02-first-order-dynamics.md) · [it](../../it/notes/02-first-order-dynamics.md) · [es](../../es/notes/02-first-order-dynamics.md) · [pt](../../pt/notes/02-first-order-dynamics.md) · [zh](../../zh/notes/02-first-order-dynamics.md) · [ja](../../ja/notes/02-first-order-dynamics.md) · [nb](../../nb/notes/02-first-order-dynamics.md) · [ru](../../ru/notes/02-first-order-dynamics.md) · [ko](../../ko/notes/02-first-order-dynamics.md) · [fi](../../fi/notes/02-first-order-dynamics.md) · [pl](../../pl/notes/02-first-order-dynamics.md)

**Hier verwendete Einheiten (vor den Beispielen erklärt):** `s` — Sekunde; `mm/s` — Millimeter / Sekunde — lineare Geschwindigkeit; `kg` — Kilogramm; `m` — Meter; `rad/s` — Radiant / Sekunde — Winkelgeschwindigkeit; `N` — Newton; `N·m` — Newton · Meter — Drehmoment; `J` — Joule; `rpm` — Umdrehung pro Minute; `kg·m²` — Kilogramm · Meter² — Trägheitsmoment; `N·m·s/rad` — Newton · Meter · Sekunde / Radiant — Verstärkung pro Geschwindigkeit; `%` — Prozent (ein Hundertstel); `rad` — Radiant. [Einheitenverzeichnis](../UNITS.md).

**Grundlagen:** [0. Grundlagen von Ableitungen, Differentialen und Integralen](00-calculus-foundations.md) · [Integraltafel](../INTEGRAL_TABLE.md)

[README](../README.md) · [Formelsammlung](../CHEATSHEET.md) · [Python-Übungen](../exercises/README.md) · [Bewegung, Ableitungen und Integrale](01-motion-calculus.md)

> **Warnung:** Dieses KI-unterstützte Lernmaterial kann Fehler, falsche Übersetzungen und unzutreffende Annahmen enthalten. Nutzung auf eigenes Risiko. Ergebnisse unabhängig prüfen; Beispiele niemals zur Steuerung realer Maschinen verwenden.

> **Annahmen des Motormodells:** Es wird eine ideale proportionale Drehmomentregelung ohne Last, Reibung, Verzögerungen, Spannungsgrenzen, Sättigung und Dynamik höherer Ordnung angenommen. Dies ist keine allgemeingültige Beschreibung von Motoren.

## Kurzüberblick

Die Zeitkonstante $\tau$ bestimmt, wie schnell ein System erster Ordnung einem neuen Gleichgewicht zustrebt. Der Simulationsschritt $dt$ bestimmt die numerische Auflösung, nicht die Eigenschaften des physikalischen Systems. Im idealisierten Modell gilt $\tau=\frac{J}{K}$; gleiche Zeitkonstante bedeutet nicht gleichen Energiebedarf.

**Englische Fachbegriffe:**

- System erster Ordnung (first-order system)
- Zeitkonstante (time constant)
- Zeitschritt (time step)
- Trägheitsmoment (moment of inertia)
- Drehmoment (torque)
- Reglerverstärkung (controller gain)
- Winkelbeschleunigung (angular acceleration)
- Systemidentifikation (system identification)
- Rotationsenergie (rotational kinetic energy)

## Auf dieser Seite

- [1. Antwort erster Ordnung](#section-1)
- [2. Drehmoment und Trägheit](#section-2)
- [3. Zeitschritt und Zeitkonstante](#section-3)
- [4. Zeitkonstante aus Messwerten abschätzen](#section-4)
- [5. Rotationsenergie](#section-5)
- [6. Ausprobieren](#section-6)
- [7. Vertiefung (optional)](#section-7)
  - [Woher kommen 63.2 %, 86.5 % und 95.0 %?](#time-constant-derivation)
  - [Herleitung der Euler-Zahlen](#euler-values-derivation)

[SI-Einheiten und Dezimalpunkt](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Antwort erster Ordnung

Einheiten, Herleitungen und numerische Grenzen stehen unter [Vertiefung](#section-7).

Für eine konstante Sollgeschwindigkeit $u$, die Istgeschwindigkeit $v$ und $\tau>0$ durchläuft das System nach $\tau$ ungefähr $63.2\ \%$, nach $2\tau$ etwa $86.5\ \%$ und nach $3\tau$ etwa $95.0\ \%$ der Gesamtänderung. Die Sollgeschwindigkeit wird **nicht** genau nach einer Zeitkonstante erreicht.

**Notation:** $\varepsilon(t)=u-v(t)$ ist der Geschwindigkeitsfehler (speed error; griechisches Epsilon). Die natürliche Exponentialfunktion (exponential function) ist $\exp(z)=\mathrm{e}^{z}$, wobei $\mathrm{e}\approx2.71828$ die Eulersche Zahl (Euler’s number) und **nicht** der Fehler ist. [Herleitung und Berechnung der 63.2 %](#time-constant-derivation).

$$
\frac{dv}{dt}=\frac{u-v}{\tau}.
$$

$$
v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right).
$$

| Zeit | Anteil der Änderung |
| --- | ---: |
| $\tau$ | 63.2 % |
| $2\tau$ | 86.5 % |
| $3\tau$ | 95.0 % |

[Warum genau diese Prozentwerte? Zur Rechnung.](#time-constant-derivation)

![Normierte Sprungantwort erster Ordnung: Nach jeder Zeitkonstante sinkt der verbleibende Fehler um etwa 63.2 %.](../../../assets/figures/first_order_response.svg)

<a id="section-2"></a>

## 2. Drehmoment und Trägheit

Der Regler berechnet einen elektrischen Stellwert; der Motor erzeugt das physikalische Drehmoment $M$. Im Modell ist $J$ das Trägheitsmoment, $\omega$ die Winkelgeschwindigkeit und $K$ der Proportionalitätsfaktor zwischen Drehmoment und Drehzahlfehler. Verdoppeltes $J$ bei konstantem $K$ verdoppelt $\tau$. Werden $J$ und $K$ beide verdoppelt, bleibt $\tau$ gleich; bei gleichem Fehler ist das erforderliche Drehmoment doppelt so groß. Reibung, Lasten, Verzögerungen und Stromgrenzen fehlen im Modell.

$$
J\frac{d\omega}{dt}=M,\qquad M=K(u-\omega).
$$

$$
\frac{d\omega}{dt}=\frac{K}{J}(u-\omega),\qquad \tau=\frac{J}{K}.
$$

**Einheiten:** $J$: $\mathrm{kg}\cdot\mathrm{m}^2$; $\omega,u$: $\mathrm{rad/s}$; $M$: $\mathrm{N}\cdot\mathrm{m}$; $K$: $\mathrm{N}\cdot\mathrm{m}\cdot\mathrm{s}/\mathrm{rad}$; $\tau$: s.

Symbolischer Rückkopplungskreis im idealisierten Modell. Der Regler gibt einen Befehl; das Motordrehmoment entsteht physikalisch im Motor.

![Symbolischer Rückkopplungskreis im idealisierten Modell. Der Regler gibt einen Befehl; das Motordrehmoment entsteht physikalisch im Motor](../../../assets/figures/control_loop.svg)

<a id="section-3"></a>

## 3. Zeitschritt und Zeitkonstante

Das Euler-Verfahren aktualisiert mit Schrittweite $dt$. Ein kleineres $dt$ lässt den modellierten Motor nicht schneller reagieren, sondern verändert die Rechengenauigkeit. Für $u=10\ \mathrm{mm/s}$, $\tau=1\ \mathrm{s}$ und eine Sekunde ergibt Euler $6.513$ bei $dt=0.1$ beziehungsweise $6.340\ \mathrm{mm/s}$ bei $dt=0.01$; exakt sind $6.321\ \mathrm{mm/s}$.

$$
v_{n+1}=v_n+\frac{u-v_n}{\tau}\ dt.
$$

| Verfahren | $v(1\ \mathrm{s})$ (mm/s) |
| --- | ---: |
| Euler $dt=0.1\ \mathrm{s}$ | 6.513 |
| Euler $dt=0.01\ \mathrm{s}$ | 6.340 |
| Exakt | 6.321 |

[Rechnung zu diesen Zahlenwerten.](#euler-values-derivation)

<a id="section-4"></a>

## 4. Zeitkonstante aus Messwerten abschätzen

Bei einem Sollwertsprung von 0 auf 1000 rpm (Umdrehungen pro Minute) sucht man den Zeitpunkt, zu dem die gemessene Drehzahl etwa 632 rpm erreicht. Nach 2 Sekunden ergibt sich im einfachen Modell $\tau\approx2\ \mathrm{s}$. Bei einem anderen Anfangswert zählen 63.2 % der **gesamten Änderung**. Rauschen, Verzögerung und Überschwingen erschweren diese einfache Systemidentifikation (system identification).

**Was das Programm zurückgibt:** Die Funktion [`estimate_tau`](../../../exercises/02_first_order_response.py) erwartet Messwerte mit **streng aufsteigenden Zeitstempeln**, gezählt ab dem Sollwertsprung. Sie gibt den Zeitpunkt der **ersten beobachteten Probe** am oder über dem 63.2 %-Änderungsschwellenwert zurück; eine bekannte Messauflösung wird mit einer halben Auflösungseinheit berücksichtigt. Wird die Schwelle erstmals bei 2 s erkannt, die vorige Probe aber bei 1 s aufgenommen, kann das tatsächliche Überschreiten **zwischen den Proben** stattgefunden haben. 2 s ist daher eine durch Abtastung begrenzte Schätzung, keine exakte Anpassung. Ungültige, wiederholte oder unsortierte Zeitstempel werden auch nach dem Überschreiten abgewiesen; ohne Überschreitung folgt `None`.

**Die Messauflösung ist entscheidend:** Der Parameter `resolution` in `estimate_tau` muss **kleiner als der Betrag der gesamten Geschwindigkeitsänderung** sein. Wenn die Drehzahl von 0 auf 10 rpm steigt, die Anzeige aber nur in 10-rpm-Schritten wechselt, lässt sich der Zeitpunkt der 63.2 %-Schwelle daraus nicht zuverlässig bestimmen. Die Funktion weist solche Daten zurück, statt einen künstlichen Schwellenübertritt bei der ersten Probe zu melden. Auch bei feinerer Auflösung bleibt die Schätzung durch die Abtastrate begrenzt.

<a id="section-5"></a>

## 5. Rotationsenergie

Das resultierende Drehmoment erfüllt $M=J\alpha$. Bei $J=2\ \mathrm{kg}\cdot\mathrm{m}^2$ und $\omega=10\ \mathrm{rad/s}$ beträgt die Rotationsenergie $100\ \mathrm{J}$; doppeltes $J$ ergibt $200\ \mathrm{J}$. Eine Verdopplung von $\omega$ vervierfacht die Energie. Mechanische Energie ist nicht gleich elektrischer Aufnahmeenergie.

$$
M=J\alpha,\qquad \alpha=\frac{d\omega}{dt}.
$$

$$
E=\frac{1}{2}J\omega^2.
$$

<a id="section-6"></a>

## 6. Ausprobieren

Bei einem idealen Geschwindigkeitssprung von 0 auf 1000 rpm deutet das Erreichen von etwa 632 rpm nach zwei Sekunden auf $\tau\approx2\ \mathrm{s}$ hin. Messrauschen und Abtastung können eine genauere Systemidentifikation erfordern. Euler-Verfahren und exakte Lösung im Programm vergleichen.

[02_first_order_response.py](../../../exercises/02_first_order_response.py) · [03_rotation_energy.py](../../../exercises/03_rotation_energy.py) · [plot_models.py](../../../exercises/plot_models.py)


<a id="section-7"></a>

## 7. Vertiefung (optional)


### Stabilität des Euler-Verfahrens

Pro Schritt wird die **verbleibende Sollwertabweichung** mit $1-\frac{dt}{\tau}$ multipliziert. Für dieses Modell ist $0<dt<2\tau$ zur Konvergenz nötig; bei $\tau<dt<2\tau$ schwingt der Zahlenwert um den Sollwert. Das ist kein physikalisches Motorschwingen.

### Modellgrenzen

Allgemeiner lautet die Drehmomentbilanz $J\ \frac{d\omega}{dt}=M_{\text{Motor}}-M_{\text{Last}}-M_{\text{Reibung}}$. $\tau=\frac{J}{K}$ gilt nur für die besondere Annahme $M_{\text{gesamt}}=K(u-\omega)$. Last, Reibung, Verzögerung und Stromgrenzen können dieses Modell ändern.

### Energie und Leistung

Bei konstantem $J$: $\Delta E=\frac{1}{2} J(\omega_2^2-\omega_1^2)$ und die momentane mechanische Leistung (mechanical power) $P=M\omega$. Damit ist der elektrische Verbrauch noch nicht bestimmt.


<a id="time-constant-derivation"></a>

### Woher kommen 63.2 %, 86.5 % und 95.0 %?

Die Prozentwerte und die Exponentialfunktion entstehen aus **derselben Gleichung**. Der Geschwindigkeitsfehler ist $\varepsilon(t)=u-v(t)$ (nicht die Eulersche Zahl). Bei konstantem Sollwert $u$ gilt $\frac{d\varepsilon}{dt}=-\frac{dv}{dt}$:

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

Beim Trennen der Variablen wird durch $\varepsilon$ dividiert. Daher setzt dieser Schritt einen von null verschiedenen Anfangsfehler voraus. Falls $u=v_0$, bleibt der Fehler stets null; direkt aus der ursprünglichen Differentialgleichung folgt die konstante Lösung $v(t)=u$.

$$
f(t)=\frac{v(t)-v_0}{u-v_0}=1-\exp\!\left(-\frac{t}{\tau}\right),\qquad (u\ne v_0).
$$

| $t$ | $f(t)$ |
| ---: | ---: |
| $\tau$ | $1-\exp(-1)=0.63212056\ldots\approx63.2\ \%$ |
| $2\tau$ | $1-\exp(-2)=0.86466472\ldots\approx86.5\ \%$ |
| $3\tau$ | $1-\exp(-3)=0.95021293\ldots\approx95.0\ \%$ |

Bei einem Sprung von 0 auf 1000 rpm ergibt das nach einer, zwei und drei Zeitkonstanten rund 632, 865 und 950 rpm. Im idealen Modell nähert sich die Drehzahl asymptotisch dem Sollwert.

<a id="euler-values-derivation"></a>

### Herleitung der Euler-Zahlen

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
