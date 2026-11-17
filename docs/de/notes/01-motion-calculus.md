# 1. Bewegung, Ableitungen und Integrale


**Diese Seite lesen auf:** [en](../../en/notes/01-motion-calculus.md) · [fr](../../fr/notes/01-motion-calculus.md) · [de](01-motion-calculus.md) · [it](../../it/notes/01-motion-calculus.md) · [es](../../es/notes/01-motion-calculus.md) · [pt](../../pt/notes/01-motion-calculus.md) · [zh](../../zh/notes/01-motion-calculus.md) · [ja](../../ja/notes/01-motion-calculus.md) · [nb](../../nb/notes/01-motion-calculus.md) · [ru](../../ru/notes/01-motion-calculus.md) · [ko](../../ko/notes/01-motion-calculus.md) · [fi](../../fi/notes/01-motion-calculus.md) · [pl](../../pl/notes/01-motion-calculus.md)

**Hier verwendete Einheiten (vor den Beispielen erklärt):** `s` — Sekunde; `mm` — Millimeter = 0.001 m; `mm/s` — Millimeter / Sekunde — lineare Geschwindigkeit; `mm/s²` — Millimeter / Sekunde² — Beschleunigung; `%` — Prozent (ein Hundertstel). [Einheitenverzeichnis](../UNITS.md).

**Grundlagen:** [0. Grundlagen von Ableitungen, Differentialen und Integralen](00-calculus-foundations.md) · [Integraltafel](../INTEGRAL_TABLE.md)

[README](../README.md) · [Formelsammlung](../CHEATSHEET.md) · [Python-Übungen](../exercises/README.md) · [Dynamik erster Ordnung und Rotation](02-first-order-dynamics.md)

> **Warnung:** Dieses KI-unterstützte Lernmaterial kann Fehler, falsche Übersetzungen und unzutreffende Annahmen enthalten. Nutzung auf eigenes Risiko. Ergebnisse unabhängig prüfen; Beispiele niemals zur Steuerung realer Maschinen verwenden.

## Kurzüberblick

Die zurückgelegte Strecke ist die gesamte Weglänge; die Verschiebung ist Endposition minus Anfangsposition. Der Geschwindigkeitsbetrag (speed) ist nichtnegativ, der Geschwindigkeitsvektor (velocity) enthält die Richtung. Die Ableitung der Position liefert die momentane Geschwindigkeit; das Integral der vorzeichenbehafteten Geschwindigkeit die Verschiebung.

**Englische Fachbegriffe:**

- zurückgelegte Strecke (distance traveled)
- Verschiebung (displacement)
- Geschwindigkeitsbetrag (speed)
- Geschwindigkeit als Vektor (velocity)
- Ableitung (derivative)
- Integral (integral)
- numerische Integration (numerical integration)
- explizites Euler-Verfahren (explicit Euler method)

## Auf dieser Seite

- [1. Bewegungsbeispiel](#section-1)
- [2. Ableitung und momentane Geschwindigkeit](#section-2)
- [3. Integral und Verschiebung](#section-3)
- [4. Numerische Integration](#section-4)
- [5. Ausprobieren](#section-5)
- [6. Vertiefung (optional)](#section-6)
  - [Warum die Ableitung von 2t² gleich 4t ist](#power-rule-derivation)
  - [Herleitung der Verschiebungswerte in der Tabelle](#motion-values-derivation)

[SI-Einheiten und Dezimalpunkt](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Bewegungsbeispiel

Einheiten, Herleitungen und numerische Grenzen stehen unter [Vertiefung](#section-6).

Eine virtuelle Achse bewegt sich zwei Sekunden mit $+3\ \mathrm{mm/s}$ und anschließend zwei Sekunden mit $-3\ \mathrm{mm/s}$. Die Verschiebung beträgt $+6-6=0\ \mathrm{mm}$, die Strecke jedoch $12\ \mathrm{mm}$. Bei Kreisbewegung ändert sich trotz konstantem Geschwindigkeitsbetrag fortlaufend die Richtung des Geschwindigkeitsvektors.

$$
\overline{v}=\frac{x(t_2)-x(t_1)}{t_2-t_1}.
$$

$$
\text{durchschnittliche Schnelligkeit}=\frac{\text{gesamte zurückgelegte Strecke}}{t_2-t_1}.
$$

Über die **gesamten vier Sekunden** ergeben mittlere vorzeichenbehaftete Geschwindigkeit und mittlere Schnelligkeit **verschiedene Werte**. Die Achse kehrt zum Ausgangspunkt zurück und legt dennoch 12 mm zurück:

$$
\overline{v}_x=\frac{0\ \mathrm{mm}}{4\ \mathrm{s}}=0\ \mathrm{mm/s}
$$

$$
\overline{\lvert v\rvert}=\frac{12\ \mathrm{mm}}{4\ \mathrm{s}}=3\ \mathrm{mm/s}
$$

Die mittlere Schnelligkeit ist also **nicht immer der Betrag der mittleren Geschwindigkeit**. Bei einer vollen Kreisrunde ist der mittlere Geschwindigkeitsvektor ebenfalls null, obwohl Strecke und mittlere Schnelligkeit positiv sind.

<a id="section-2"></a>

## 2. Ableitung und momentane Geschwindigkeit

Für $x(t)=2t^2\ \mathrm{mm}$ mit Zeit $t$ in Sekunden ist $v(t)=4t\ \mathrm{mm/s}$. **Warum 4?** Nach der Potenzregel gilt $d(t^2)/dt=2t$. Bei $2t^2$ ergibt das $2\cdot2t=4t$. [Herleitung und Einheiten](#power-rule-derivation). Bei $t=1\ \mathrm{s}$ gilt $v=4\ \mathrm{mm/s}$. Der Vorwärts-Differenzenquotient liefert für $dt=1$, $0.1$ und $0.01\ \mathrm{s}$ die Näherungen $6$, $4.2$ und $4.02\ \mathrm{mm/s}$.

$$
v(t)=\frac{dx}{dt},\qquad v(t)\approx\frac{x(t+dt)-x(t)}{dt}.
$$

**Warum ein zu kleiner Schritt falsche Werte liefern kann:** Bei $t=1\ \mathrm{s}$ beträgt die exakte Ableitung von $x(t)=2t^2$ genau $4\ \mathrm{mm/s}$. Mit $dt=1e-17\ \mathrm{s}$ rundet Python `float` die Rechnung `t + dt` wieder auf `t`. Beide berechneten Positionen sind gleich; ihre Differenz würde fälschlich eine Geschwindigkeit von null liefern. Bei noch kleineren Größenordnungen können auch beide Positionswerte auf null unterlaufen, obwohl die Ableitung ungleich null ist. Das Beispiel [`forward_derivative`](../../../exercises/01_motion_and_integral.py) meldet nun `ValueError` statt dieses falschen Nullwerts. Die finite Differenz bleibt erhalten; wähle einen numerisch auflösbaren Zeitschritt statt ihn unbegrenzt zu verkleinern.

<a id="section-3"></a>

## 3. Integral und Verschiebung

Das Integral der vorzeichenbehafteten Geschwindigkeit kann null oder negativ sein; das Integral ihres Betrags ergibt eine nichtnegative Strecke. Für $v(t)=2t\ \mathrm{mm/s}$ von $0$ bis $2\ \mathrm{s}$ beträgt die exakte Verschiebung $4\ \mathrm{mm}$.

$$
\Delta x=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t,\qquad
s=\int_{t_1}^{t_2}|v(t)|\ \mathrm{d}t.
$$

Geometrisch entspricht das vorzeichenbehaftete Integral der orientierten Fläche unter der Geschwindigkeit-Zeit-Kurve. **Dies ist ein anderes Beispiel als in Abschnitt 2.** Dort wurde die Position $x(t)=2t^2$ verwendet; ihre Ableitung ist $v(t)=4t$. Für die Integration wird hier bewusst eine andere Geschwindigkeit gewählt: $v(t)=2t$. Die dazugehörige Position lautet $x(t)=t^2+C$ (bei konsistenten Einheiten). Die beiden Bewegungsgesetze dürfen nicht miteinander verwechselt werden.

<a id="section-4"></a>

## 4. Numerische Integration

Exakte Verschiebung und Euler-Näherung mit dem linken Intervallrand (synthetische Werte).

![Exakte Verschiebung und Euler-Näherung mit dem linken Intervallrand (synthetische Werte)](../../../assets/figures/euler_vs_exact.svg)

Das explizite Euler-Verfahren verwendet die Geschwindigkeit **am Anfang** jedes Schritts, nicht den tatsächlichen Mittelwert. Bei der hier ansteigenden Geschwindigkeit unterschätzt es den Weg: Für $dt=0.5$, $0.1$ und $0.01\ \mathrm{s}$ erhält man $3$, $3.8$ und $3.98\ \mathrm{mm}$ (exakt $4\ \mathrm{mm}$). Die Trapezregel ist hier wegen der linearen Zeitabhängigkeit exakt.

$$
x_{n+1}=x_n+v(t_n)\ dt.
$$

| `dt` (s) | Euler (mm) |
| ---: | ---: |
| 0.5 | 3.000 |
| 0.1 | 3.800 |
| 0.01 | 3.980 |
| Exakt | 4.000 |


[Berechnung von 3, 3.8 und 3.98.](#motion-values-derivation)

<a id="section-5"></a>

## 5. Ausprobieren

Das Bewegungsprogramm starten und $dt$ verkleinern. Warum kann die Verschiebung nach einer Hin- und Rückbewegung null sein, obwohl eine positive Strecke zurückgelegt wurde?

[01_motion_and_integral.py](../../../exercises/01_motion_and_integral.py)

<a id="section-6"></a>

## 6. Vertiefung (optional)

### Einheiten und Koeffizienten

Ist $t$ in Sekunden angegeben, ist $x(t)=2t^2$ mm eine Kurzschreibweise: Der Vorfaktor hat die Einheit $2\ \mathrm{mm/s^2}$. Die Ableitung $v(t)=4t$ hat dann die Einheit mm/s. Einheiten stets prüfen.

### Grenzen der Näherung

Ein Differenzenquotient (finite difference) schätzt die Ableitung über ein endliches Intervall. Ein kleinerer Schritt verringert häufig den Diskretisierungsfehler, kann aber Rundungsfehler oder Messrauschen verstärken. Euler verwendet jeweils den Wert am Schrittanfang.

### Mehrdimensionale Bewegung

Für den Ortsvektor $\mathbf r(t)$ gilt $\mathbf v=d\mathbf r/dt$; der Geschwindigkeitsbetrag ist $\|\mathbf v\|$, die Weglänge $s=\int\|\mathbf v(t)\|dt$.


<a id="power-rule-derivation"></a>

### Warum die Ableitung von $2t^2$ gleich $4t$ ist



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

### Herleitung der Verschiebungswerte in der Tabelle

$$
a=2\ \mathrm{mm/s^2},\qquad v(t)=at,\qquad 0\le t\le2\ \mathrm{s}.
$$

$$
\Delta x=\int_{0}^{2\ \mathrm{s}}at\ \mathrm{d}t
=\left[\frac{at^2}{2}\right]_{0}^{2\ \mathrm{s}}
=4\ \mathrm{mm}.
$$



Das Zeichen $\sum$ (großes griechisches Sigma, **Summenzeichen** / summation) bedeutet: Terme addieren. In $\sum_{n=0}^{N-1}(2nh)h$ durchläuft der Index $n$ die Werte $0; 1; \ldots; N-1$: insgesamt $N$ Terme. Das entspricht einer Python-`for`-Schleife, die die Beiträge aufsummiert. Beispielsweise gilt $\sum_{n=1}^{3}n=1+2+3=6$. [← Symbolerklärungen](../SYMBOLS.md#summation).

$$
h=\frac{dt}{1\ \mathrm{s}},\qquad N=\frac{2}{h}.
$$

$$
x_{\mathrm{Euler}}(2\ \mathrm{s})
=\left[\sum_{n=0}^{N-1}(2nh)h\right]\ \mathrm{mm}
=\left[h^2N(N-1)\right]\ \mathrm{mm}
=(4-2h)\ \mathrm{mm}.
$$

Hier ist `h` der Zahlenwert des Zeitschritts `dt` in Sekunden (`dt = 0.5 s` ergibt `h = 0.5`); `N` ist die Zahl der Schritte. Das Ergebnis ist eine **Strecke in Millimetern**.



Für $dt=0.5$, $0.1$ und $0.01$ Sekunden ergibt das $3$, $3.8$ und $3.98$ Millimeter. Dabei ist $2/dt$ eine ganze Zahl.
