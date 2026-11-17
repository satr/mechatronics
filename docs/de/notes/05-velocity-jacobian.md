# 5. Rotation, lineare Geschwindigkeit und Singularitäten

**Languages:** [en](../../en/notes/05-velocity-jacobian.md) · [fr](../../fr/notes/05-velocity-jacobian.md) · [de](05-velocity-jacobian.md) · [it](../../it/notes/05-velocity-jacobian.md) · [es](../../es/notes/05-velocity-jacobian.md) · [pt](../../pt/notes/05-velocity-jacobian.md) · [zh](../../zh/notes/05-velocity-jacobian.md) · [ja](../../ja/notes/05-velocity-jacobian.md) · [nb](../../nb/notes/05-velocity-jacobian.md) · [ru](../../ru/notes/05-velocity-jacobian.md) · [ko](../../ko/notes/05-velocity-jacobian.md) · [fi](../../fi/notes/05-velocity-jacobian.md) · [pl](../../pl/notes/05-velocity-jacobian.md)

**Hier verwendete Einheiten (vor den Beispielen erklärt):** `mm` — Millimeter = 0.001 m; `mm/s` — Millimeter / Sekunde — lineare Geschwindigkeit; `rad` — Radiant; `rad/s` — Radiant / Sekunde — Winkelgeschwindigkeit; `mm/rad` — Millimeter / Radiant — Jacobi-Koeffizient (Länge pro Winkel); `°` — Grad. [Einheitenverzeichnis](../UNITS.md).

[README](../README.md) · [Trigonometry](../TRIGONOMETRY.md#unit-circle-values) · [Coordinate frames](04-coordinate-frames.md) · [Calculus foundations](00-calculus-foundations.md)

> Nur ideales Lernmodell; nicht für echte Maschinensteuerung verwenden.

Die Spitze eines rotierenden Glieds folgt einem Kreisbogen. Ihre momentane Geschwindigkeit ist tangential und steht senkrecht auf dem Glied. Erst Geometrie, dann zeitliche Ableitung und schließlich optional die Jacobi-Matrix (Jacobian matrix).

## Inhalt

1. [Drehung und Tangentialgeschwindigkeit](#section-1)
2. [Herleitung der Ableitungen](#section-2)
3. [Beispiele mit Geschwindigkeit und Vorzeichen](#section-3)
4. [Zwei Glieder: relative und absolute Winkel](#section-4)
5. [Singularitäten bei gestrecktem und gefaltetem Arm](#section-5)
6. [Drei Verschiebungen nahe der Faltung](#section-6)
7. [Optional: Jacobi-Matrix und gelöste Aufgaben](#section-7)

<a id="section-1"></a>
## 1. Drehung und Tangentialgeschwindigkeit

Ein starres Glied der Länge $L$ dreht sich um den festen Punkt $O$. Dabei sei $\Delta Q$ die Winkeländerung **im Bogenmaß** während $\Delta t>0$. Wenn die Drehrichtung in diesem Zeitabschnitt nicht wechselt, beschreibt die Spitze einen Kreisbogen. Dessen **Bogenlänge** ist exakt $\Delta s=L|\Delta Q|$. Die **vorzeichenbehaftete Bogenstrecke** $L\Delta Q$ gibt zusätzlich die Drehrichtung an. Sie ist nicht mit der geradlinigen Verschiebung (Sehne) zwischen Anfangs- und Endpunkt zu verwechseln.

$$
\Delta s=L\lvert\Delta Q\rvert,\qquad
\Delta s_{\mathrm{signed}}=L\Delta Q
$$

Die zurückgelegte Bogenlänge geteilt durch die Zeit ergibt die **mittlere Bahngeschwindigkeit**:

$$
\overline{v}=\frac{\Delta s}{\Delta t}
=L\left\lvert\frac{\Delta Q}{\Delta t}\right\rvert
$$

Für die **Momentangeschwindigkeit** nehmen wir den Grenzwert $\Delta t\to0$. Die Winkelgeschwindigkeit ist $\omega=\dot Q=\mathrm{d}Q/\mathrm{d}t$ in rad/s; daher beträgt der Betrag der Spitzengeschwindigkeit $v=L|\omega|$. Der Geschwindigkeitsvektor liegt **tangential zum Kreis**, also senkrecht zum Glied. Bei $Q=45^\circ$ und gegen den Uhrzeigersinn ($\omega>0$) bewegt sich die Spitze nach links oben: die horizontale Komponente ist negativ, die vertikale positiv.

$$
v=L\lvert\dot Q\rvert
$$

![Tangentialgeschwindigkeit und Vorzeichen bei Q=45°.](../../../assets/figures/link_tangent_velocity.svg)

*Tangentialgeschwindigkeit und Vorzeichen bei Q=45°.*

<a id="section-2"></a>
## 2. Herleitung der Ableitungen

Die Koordinaten hängen von Q ab, während Q von der Zeit abhängt. Die Kettenregel (chain rule) multipliziert Ortsänderung je Radiant mit Radiant je Sekunde.

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

Die Winkelgeschwindigkeit $\dot Q=\mathrm{d}Q/\mathrm{d}t$ hat die Einheit rad/s und ist nicht der Winkel selbst. Bei L in mm sind vx und vy in mm/s. Trigonometrische Ableitungen erfordern Bogenmaß.


$$
\omega=\dot{Q},\qquad \omega_1=\dot{Q}_1,\qquad \omega_2=\dot{Q}_2
$$

<a id="section-3"></a>
## 3. Beispiele mit Geschwindigkeit und Vorzeichen

Bei L=150 mm, Q=45° und ω=+0.1 rad/s sind beide Komponenten betragsgleich: links und oben. Ein Vorzeichenwechsel von ω kehrt beide Komponenten um. Bei Q=0° gilt vy=15 mm/s, vx=0.

$$
Q=45^\circ:\quad v_x=-150\frac{\sqrt2}{2}\cdot0.1\approx-10.61\ \mathrm{mm/s}
$$

$$
v_y=+150\frac{\sqrt2}{2}\cdot0.1\approx+10.61\ \mathrm{mm/s}
$$

$$
\sqrt{v_x^2+v_y^2}=L\lvert\dot Q\rvert=15\ \mathrm{mm/s}
$$

Der Punkt über $Q$ kennzeichnet die **Zeitableitung** $\dot Q$, nicht eine Multiplikation mit dem Winkel. Ein Wechsel von $\omega$ zu $-\omega$ kehrt die Vorzeichen beider Geschwindigkeitskomponenten um, aber nicht den Betrag $L|\omega|$.

<a id="section-4"></a>
## 4. Zwei Glieder: relative und absolute Winkel

Q1 ist der absolute Winkel zur +X-Achse, Q2 der relative Ellenbogenwinkel. Die absolute Orientierung des zweiten Glieds ist Q1+Q2, seine Winkelgeschwindigkeit ω₁+ω₂.

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

Beide Gelenke tragen zur Spitzengeschwindigkeit bei: Das erste Glied hat den Faktor $\dot Q_1$, das zweite den Faktor $\dot Q_1+\dot Q_2$. Nur $\dot Q_2$ für das zweite Glied einzusetzen wäre falsch, weil sein Winkel relativ zum ersten Glied definiert ist.

<a id="section-5"></a>
## 5. Singularitäten bei gestrecktem und gefaltetem Arm

Für L1=100 mm und L2=50 mm reicht der ideale Abstand von 50 bis 150 mm. Vollständig gefaltete (Q2=180°) und gestreckte (Q2=0°) Positionen sind singulär: die momentane radiale Geschwindigkeit ist dort für endliche Gelenkgeschwindigkeiten null.

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

Die Ableitung gilt nur für $r>0$. Bei gleich langen Gliedern ($L_1=L_2$) fällt die Spitze in vollständig gefalteter Stellung ($Q_2=180^\circ$) auf den Ursprung: $r=0$, und die Formel würde durch null teilen. An diesem Punkt ist der Radius als Funktion der **vorzeichenbehafteten** Abweichung des Ellenbogenwinkels nicht differenzierbar. Für die hier verwendeten ungleichen Längen $L_1=100$ mm und $L_2=50$ mm tritt dieser Sonderfall nicht auf.

Gelenkanschläge und Kollisionen können den realen Arbeitsraum weiter verkleinern. Ein erreichbarer Punkt allein garantiert weder die gewünschte Werkzeugorientierung noch ausreichenden Abstand zu Hindernissen.

<a id="section-6"></a>
## 6. Drei Verschiebungen nahe der Faltung

Bei fixiertem erstem Glied beschreibt δ die kleine Abweichung in Radiant von der gefalteten Lage. Die Verschiebung entlang der festen Gliedachse unterscheidet sich von der radialen Abstandsänderung.

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

Aus 1−cosδ=2sin²(δ/2) und sin(δ/2)≈δ/2 folgen Quadrat und Faktor 1/2. Hier ist der radiale Zuwachs ≈50δ² mm, der axiale ≈25δ² mm.

Die Näherungen gelten nur für kleine $\delta$ in Radiant. Wenn $\delta$ halbiert wird, werden beide quadratischen Änderungen (axial und radial) etwa **geviertelt**, die transversale Verschiebung aber nur **halbiert**. Bei fest vorgegebener radialer Geschwindigkeit würde die ideale inverse Abbildung für $\delta\to0$ unbegrenzte Gelenkgeschwindigkeit verlangen; ein realer Arm kann dagegen mit endlicher Winkelgeschwindigkeit beginnen und erst allmählich radiale Geschwindigkeit aufbauen.

$$
1-\cos(\delta)=2\sin^2\left(\frac{\delta}{2}\right)
\approx2\left(\frac{\delta}{2}\right)^2=\frac{\delta^2}{2}
$$

![Axiale, transversale und radiale Verschiebung nahe der Faltung.](../../../assets/figures/folded_displacement_curves.svg)

*Axiale, transversale und radiale Verschiebung nahe der Faltung.*

Für konstante positive radiale Geschwindigkeit nahe der Faltung muss die Gelenkwinkelgeschwindigkeit bei δ→0 stark zunehmen. Im exakt gefalteten Zustand entsteht aus endlichen Gelenkgeschwindigkeiten keine sofortige radiale Geschwindigkeit.

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

![Benötigte Gelenkwinkelgeschwindigkeit nahe einer Singularität.](../../../assets/figures/folded_radial_speed.svg)

*Benötigte Gelenkwinkelgeschwindigkeit nahe einer Singularität.*

<a id="section-7"></a>
## 7. Optional: Jacobi-Matrix und gelöste Aufgaben

Die Jacobi-Matrix (Jacobian matrix) bildet Gelenkgeschwindigkeiten auf die Werkzeuggeschwindigkeit ab. Ihre Determinante L1L2 sin Q2 verschwindet bei kollinearen Gliedern. Reale Anschläge und Kollisionen fehlen im Modell.

$$
v_x=J_{11}\cdot\omega_1+J_{12}\cdot\omega_2
$$

$$
v_y=J_{21}\cdot\omega_1+J_{22}\cdot\omega_2
$$

| Koeffizient | Geometrie der Geschwindigkeitsabbildung |
| --- | --- |
| $J_{11}$ | $-L_1\sin(Q_1)-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{12}$ | $-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{21}$ | $L_1\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)$ |
| $J_{22}$ | $L_2\cdot\cos(Q_1+Q_2)$ |



**Herleitung der Determinante.** Jeder Eintrag ist eine partielle Ableitung der Werkzeugkoordinate X oder Y nach dem Gelenkwinkel Q1 oder Q2 im Bogenmaß. Bei Längen in mm lautet die Einheit mm/rad; multipliziert mit rad/s ergibt sich mm/s.

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

Beim Ausmultiplizieren der beiden Produkte fallen die Terme mit L2 zum Quadrat weg. Die Sinus-Differenzformel beseitigt anschließend Q1.

$$
\det J=L_1L_2\sin(Q_2)
$$

![Die beiden Gelenkbeiträge addieren sich als Vektoren zur Werkzeuggeschwindigkeit.](../../../assets/figures/two_link_jacobian_velocity.svg)

*Die beiden Gelenkbeiträge addieren sich als Vektoren zur Werkzeuggeschwindigkeit.*

### Vollständig gelöste Aufgaben

1. Das einzelne Glied mit $L=150$ mm zeigt bei $Q=0^\circ$ nach rechts. Für $\omega=+0.1$ rad/s sind $\sin0^\circ=0$ und $\cos0^\circ=1$, also $v_x=-150\cdot0\cdot0.1=0$ und $v_y=150\cdot1\cdot0.1=+15$ mm/s: die Spitze bewegt sich nach oben.
2. Bei $Q=45^\circ$ und $\omega=-0.1$ rad/s kehrt die Drehrichtung um: $v_x=-150\sin45^\circ\cdot(-0.1)\approx+10.61$ mm/s, $v_y=150\cos45^\circ\cdot(-0.1)\approx-10.61$ mm/s. Die Spitze bewegt sich nach rechts unten; der Betrag bleibt $L|\omega|=15$ mm/s.
3. Bei $L_1=100$ mm, $L_2=50$ mm, $Q_1=30^\circ$, $Q_2=60^\circ$, $\omega_1=0.1$ rad/s und $\omega_2=0.2$ rad/s hat Glied 2 den absoluten Winkel $Q_1+Q_2=90^\circ$ und die Winkelgeschwindigkeit $\omega_1+\omega_2=0.3$ rad/s. Daher $v_x=-100\sin30^\circ\cdot0.1-50\sin90^\circ\cdot0.3=-5-15=-20$ mm/s und $v_y=100\cos30^\circ\cdot0.1+50\cos90^\circ\cdot0.3\approx+8.66$ mm/s.
4. Nahe der Faltung ist $\delta=0.02$ rad. Die axiale Änderung an der **festen** Gliedachse beträgt näherungsweise $25\delta^2=25\cdot0.02^2=0.010$ mm, die transversale $50\delta=1.000$ mm und die Radiuszunahme $50\delta^2=0.020$ mm. Die zwei quadratischen Änderungen haben unterschiedliche Koeffizienten und dürfen nicht verwechselt werden.

[Trigonometry](../TRIGONOMETRY.md) · [Coordinate frames](04-coordinate-frames.md) · [Calculus foundations](00-calculus-foundations.md)
