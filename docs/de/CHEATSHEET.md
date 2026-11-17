# Formelsammlung

**Diese Seite lesen auf:** [en](../en/CHEATSHEET.md) · [fr](../fr/CHEATSHEET.md) · [de](CHEATSHEET.md) · [it](../it/CHEATSHEET.md) · [es](../es/CHEATSHEET.md) · [pt](../pt/CHEATSHEET.md) · [zh](../zh/CHEATSHEET.md) · [ja](../ja/CHEATSHEET.md) · [nb](../nb/CHEATSHEET.md) · [ru](../ru/CHEATSHEET.md) · [ko](../ko/CHEATSHEET.md) · [fi](../fi/CHEATSHEET.md) · [pl](../pl/CHEATSHEET.md)

**Hier verwendete Einheiten (vor den Beispielen erklärt):** `s` — Sekunde; `m` — Meter; `m/s` — Meter / Sekunde — lineare Geschwindigkeit; `rad/s` — Radiant / Sekunde — Winkelgeschwindigkeit; `kg·m²` — Kilogramm · Meter² — Trägheitsmoment; `N·m` — Newton · Meter — Drehmoment; `N·m·s/rad` — Newton · Meter · Sekunde / Radiant — Verstärkung pro Geschwindigkeit; `J` — Joule; `mm` — Millimeter = 0.001 m; `mm/s` — Millimeter / Sekunde — lineare Geschwindigkeit; `%` — Prozent (ein Hundertstel). [Einheitenverzeichnis](UNITS.md).

[Inhalt](README.md) · [Bewegung, Ableitungen und Integrale](notes/01-motion-calculus.md) · [Dynamik erster Ordnung und Rotation](notes/02-first-order-dynamics.md) · [Python-Übungen](exercises/README.md)

> **Warnung:** Dieses KI-unterstützte Lernmaterial kann Fehler, falsche Übersetzungen und unzutreffende Annahmen enthalten. Nutzung auf eigenes Risiko. Ergebnisse unabhängig prüfen; Beispiele niemals zur Steuerung realer Maschinen verwenden.

| Kurzüberblick | Formelsammlung |
| --- | --- |
| Verschiebung | $\Delta x=x_2-x_1$ |
| Zurückgelegte Strecke | $s=\int_{t_1}^{t_2}\lvert v(t)\rvert\ \mathrm{d}t\ge 0$ |
| Mittlere vektorielle Geschwindigkeit | $\overline{v}=\frac{\Delta x}{\Delta t}$ |
| Mittlerer Geschwindigkeitsbetrag | $\frac{s}{\Delta t}$ |
| Momentane Geschwindigkeit | $v(t)=\frac{dx}{dt}$ |
| Explizites Euler-Verfahren | $x_{n+1}=x_n+v_n\ dt$ |
| System erster Ordnung | $\frac{dv}{dt}=\frac{u-v}{\tau}$ |
| Geschwindigkeitsfehler | $\varepsilon(t)=u-v(t)$ |
| Zeitkonstante | $t=\tau$: $1-\exp(-1)\approx63.2\ \%$ |
| Resultierendes Drehmoment | $M=J\alpha$ |
| Trägheitsmoment und Verstärkung | $\tau=\frac{J}{K}$ (Nur im idealisierten Drehmomentmodell) |
| Rotationsenergie | $E=\frac{1}{2}J\omega^2$ |

**Notation:** $\varepsilon$ ist der Geschwindigkeitsfehler (speed error); $\mathrm{e}\approx2.71828$ ist die Eulersche Zahl (Euler’s number); $\exp(z)=\mathrm{e}^{z}$.

**Einheiten (SI):**

| Symbol | Größe | SI-Einheit |
| --- | --- | --- |
| `t, dt, τ` | Zeit | s (second) |
| `x` | Position | m (meter) |
| `v` | Geschwindigkeit | m/s (meter per second) |
| `ω` | Winkelgeschwindigkeit | rad/s (radian per second) |
| `J` | Trägheitsmoment | kg·m² (kilogram square meter) |
| `M` | Drehmoment | N·m (newton meter) |
| `K` | Drehmomentverstärkung | N·m·s/rad |
| `E` | Energie | J (joule) |

Der Mittelpunkt `·` bedeutet Multiplikation. Der Sollwert $u$ ist je nach Modell eine lineare oder Winkelgeschwindigkeit.

## Hinweise

Geschwindigkeitsbetrag und vorzeichenbehaftete Geschwindigkeit, Strecke und Verschiebung sowie $dt$ und $\tau$ nicht verwechseln. $\tau=\frac{J}{K}$ gilt nur unter den genannten Annahmen; mechanische Energie ist nicht der elektrische Gesamtverbrauch.

**Englische Fachbegriffe:**

- zurückgelegte Strecke (distance traveled)
- Verschiebung (displacement)
- Geschwindigkeitsbetrag (speed)
- Geschwindigkeit als Vektor (velocity)
- Ableitung (derivative)
- Integral (integral)
- numerische Integration (numerical integration)
- explizites Euler-Verfahren (explicit Euler method)

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

Mehr dazu in den [Details zu Ableitungen](notes/01-motion-calculus.md#section-6) und den [Modellgrenzen](notes/02-first-order-dynamics.md#section-7).


[Warum genau diese Prozentwerte? Zur Rechnung.](notes/02-first-order-dynamics.md#time-constant-derivation)

[Berechnung von 3, 3.8 und 3.98.](notes/01-motion-calculus.md#motion-values-derivation)


## Symbole und Schreibweise

**Σ / ∑ (Summenzeichen / summation)** addiert mehrere Terme: $\sum_{n=1}^{3}n=1+2+3=6$. [Weitere Symbole](SYMBOLS.md).


## Integraltafel

[0. Grundlagen von Ableitungen, Differentialen und Integralen](notes/00-calculus-foundations.md) · [Integraltafel](INTEGRAL_TABLE.md)

## Regelung: PID und Haltemoment

| $\varepsilon=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}}$ | $u_P=K_p\varepsilon$, $u_I=K_i\int\varepsilon\ \mathrm{d}t$ |
| --- | --- |
| $M_{\mathrm{motor}}=K_t I$ | $\lvert M_g\rvert=mgL\lvert\cos\theta\rvert$ |

[Regelung: PID und Haltemoment](notes/03-feedback-control.md) · [Trigonometrische Tabelle und mechanische Beispiele](TRIGONOMETRY.md)

<a id="joint-velocity"></a>
## Rotation, Geschwindigkeit und Jacobi-Matrix

Gelenkwinkelgeschwindigkeiten haben rad/s, lineare Geschwindigkeiten mm/s bei Längen in mm.

$$
v_x=-L\sin Q\cdot\dot Q,\qquad v_y=L\cos Q\cdot\dot Q
$$

$$
\det J=L_1L_2\sin Q_2
$$

[Rotation, Geschwindigkeit und Jacobi-Matrix](notes/05-velocity-jacobian.md)
