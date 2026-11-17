# 5. Rotazione, velocità lineare e singolarità

**Languages:** [en](../../en/notes/05-velocity-jacobian.md) · [fr](../../fr/notes/05-velocity-jacobian.md) · [de](../../de/notes/05-velocity-jacobian.md) · [it](05-velocity-jacobian.md) · [es](../../es/notes/05-velocity-jacobian.md) · [pt](../../pt/notes/05-velocity-jacobian.md) · [zh](../../zh/notes/05-velocity-jacobian.md) · [ja](../../ja/notes/05-velocity-jacobian.md) · [nb](../../nb/notes/05-velocity-jacobian.md) · [ru](../../ru/notes/05-velocity-jacobian.md) · [ko](../../ko/notes/05-velocity-jacobian.md) · [fi](../../fi/notes/05-velocity-jacobian.md) · [pl](../../pl/notes/05-velocity-jacobian.md)

**Unità usate qui (spiegate prima degli esempi):** `mm` — millimetro = 0.001 m; `mm/s` — millimetro / secondo — velocità lineare; `rad` — radiante; `rad/s` — radiante / secondo — velocità angolare; `mm/rad` — millimetro / radiante — coefficiente jacobiano (lunghezza per angolo); `°` — grado. [Glossario delle unità](../UNITS.md).

[README](../README.md) · [Trigonometry](../TRIGONOMETRY.md#unit-circle-values) · [Coordinate frames](04-coordinate-frames.md) · [Calculus foundations](00-calculus-foundations.md)

> Solo modello didattico ideale; non usarlo per controllare macchinari.

L'estremità di un braccio rotante descrive un arco. La sua velocità istantanea è tangente alla traiettoria, perpendicolare al braccio. Prima la geometria, poi le derivate e infine la matrice jacobiana (Jacobian matrix) facoltativa.

## Indice

1. [Rotazione e velocità tangenziale](#section-1)
2. [Origine delle derivate](#section-2)
3. [Esempi di velocità e segni](#section-3)
4. [Due bracci: angoli relativi e assoluti](#section-4)
5. [Singolarità con bracci piegati ed estesi](#section-5)
6. [Tre spostamenti vicino alla piegatura](#section-6)
7. [Approfondimento: matrice jacobiana ed esercizi svolti](#section-7)

<a id="section-1"></a>
## 1. Rotazione e velocità tangenziale

Consideriamo un'asta rigida di lunghezza $L$ che ruota attorno al perno fisso $O$. Sia $\Delta Q$ la variazione angolare **in radianti** nell'intervallo $\Delta t>0$. Se il verso di rotazione non cambia, la punta percorre un arco di circonferenza. La **lunghezza dell'arco** è esattamente $\Delta s=L|\Delta Q|$. La **distanza orientata lungo l'arco** è $L\Delta Q$: il segno indica il verso di rotazione. Non va confusa con lo spostamento rettilineo (la corda) fra le due posizioni della punta.

$$
\Delta s=L\lvert\Delta Q\rvert,\qquad
\Delta s_{\mathrm{signed}}=L\Delta Q
$$

Dividendo la lunghezza dell'arco per il tempo trascorso otteniamo la **velocità scalare media**:

$$
\overline{v}=\frac{\Delta s}{\Delta t}
=L\left\lvert\frac{\Delta Q}{\Delta t}\right\rvert
$$

Per la **velocità istantanea** consideriamo il limite $\Delta t\to0$. La velocità angolare è $\omega=\dot Q=\mathrm{d}Q/\mathrm{d}t$, in rad/s: il modulo della velocità lineare è quindi $v=L|\omega|$. Il vettore velocità è **tangente alla circonferenza**, quindi perpendicolare all'asta. Con $Q=45^\circ$ e rotazione antioraria ($\omega>0$), la punta si muove in alto a sinistra: componente orizzontale negativa e verticale positiva.

$$
v=L\lvert\dot Q\rvert
$$

![Velocità tangenziale e componenti con segno a Q=45°.](../../../assets/figures/link_tangent_velocity.svg)

*Velocità tangenziale e componenti con segno a Q=45°.*

<a id="section-2"></a>
## 2. Origine delle derivate

Le coordinate dipendono da Q, che a sua volta dipende dal tempo. La regola della catena (chain rule) moltiplica lo spostamento per radiante per i radianti al secondo.

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

La velocità angolare $\dot Q=\mathrm{d}Q/\mathrm{d}t$ è in rad/s e non è l'angolo stesso. Con L in mm, vx e vy sono in mm/s. Le derivate trigonometriche richiedono radianti.


$$
\omega=\dot{Q},\qquad \omega_1=\dot{Q}_1,\qquad \omega_2=\dot{Q}_2
$$

<a id="section-3"></a>
## 3. Esempi di velocità e segni

Con L=150 mm, Q=45° e ω=+0.1 rad/s, le componenti hanno uguale modulo e puntano a sinistra e in alto. Cambiando il segno di ω si invertono entrambe. A Q=0°, vy=15 mm/s e vx=0.

$$
Q=45^\circ:\quad v_x=-150\frac{\sqrt2}{2}\cdot0.1\approx-10.61\ \mathrm{mm/s}
$$

$$
v_y=+150\frac{\sqrt2}{2}\cdot0.1\approx+10.61\ \mathrm{mm/s}
$$

$$
\sqrt{v_x^2+v_y^2}=L\lvert\dot Q\rvert=15\ \mathrm{mm/s}
$$

Il punto sopra $Q$ indica la sua **derivata rispetto al tempo** $\dot Q$, non una moltiplicazione per l'angolo. Cambiando $\omega$ in $-\omega$ si invertono i segni delle due componenti, ma non il modulo $L|\omega|$.

<a id="section-4"></a>
## 4. Due bracci: angoli relativi e assoluti

Q1 è l'angolo assoluto rispetto a +X, Q2 l'angolo relativo del gomito. L'orientamento assoluto del secondo braccio è Q1+Q2, con velocità angolare ω₁+ω₂.

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

Entrambe le articolazioni contribuiscono alla velocità della punta: il primo braccio compare con $\dot Q_1$, il secondo con $\dot Q_1+\dot Q_2$. Usare solo $\dot Q_2$ per il secondo braccio sarebbe errato perché il suo angolo è relativo al primo.

<a id="section-5"></a>
## 5. Singolarità con bracci piegati ed estesi

Con L1=100 mm e L2=50 mm, la distanza raggiungibile ideale è fra 50 e 150 mm. Bracci completamente piegati (Q2=180°) o distesi (Q2=0°) sono singolari: in quel preciso assetto la velocità radiale istantanea è nulla per velocità articolari finite.

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

Questa formula per la derivata vale solo se $r>0$. Se i due bracci hanno la stessa lunghezza ($L_1=L_2$), la piegatura completa sulla base ($Q_2=180^\circ$) dà $r=0$ e la formula comporta una divisione per zero. In quella posizione la distanza radiale non è derivabile rispetto alla deviazione **con segno** dell'angolo del gomito. Il caso non si presenta per le lunghezze disuguali $L_1=100$ mm e $L_2=50$ mm usate qui.

I limiti articolari e le collisioni possono restringere ulteriormente lo spazio di lavoro reale. Raggiungere una posizione non garantisce né l'orientamento richiesto dell'utensile né spazio libero dagli ostacoli.

<a id="section-6"></a>
## 6. Tre spostamenti vicino alla piegatura

Fissato il primo braccio, δ è la piccola deviazione in radianti dalla piegatura completa. Lo spostamento lungo l'asse fisso del primo braccio è diverso dalla variazione della distanza radiale.

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

L'identità 1−cosδ=2sin²(δ/2) e sin(δ/2)≈δ/2 spiegano quadrato e fattore 1/2. La variazione radiale è ≈50δ² mm, quella assiale ≈25δ² mm.

Le approssimazioni valgono solo per piccoli $\delta$ espressi in radianti. Se $\delta$ si dimezza, entrambe le variazioni quadratiche (assiale e radiale) diventano circa **un quarto**, mentre lo spostamento trasversale si **dimezza**. Richiedere una velocità radiale costante e non nulla per $\delta\to0$ porta a una velocità articolare illimitata nel modello inverso ideale; un braccio reale può invece iniziare ad aprirsi con velocità angolare finita, partendo da velocità radiale zero.

$$
1-\cos(\delta)=2\sin^2\left(\frac{\delta}{2}\right)
\approx2\left(\frac{\delta}{2}\right)^2=\frac{\delta^2}{2}
$$

![Spostamenti assiale, trasversale e radiale vicino alla piegatura.](../../../assets/figures/folded_displacement_curves.svg)

*Spostamenti assiale, trasversale e radiale vicino alla piegatura.*

Per mantenere una velocità radiale non nulla vicino alla piegatura, la velocità angolare richiesta cresce rapidamente quando δ→0. Nella posa esattamente piegata, velocità articolari finite non producono subito velocità radiale.

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

![Velocità del gomito richiesta vicino alla singolarità.](../../../assets/figures/folded_radial_speed.svg)

*Velocità del gomito richiesta vicino alla singolarità.*

<a id="section-7"></a>
## 7. Approfondimento: matrice jacobiana ed esercizi svolti

La matrice jacobiana (Jacobian matrix) converte le velocità articolari in velocità cartesiane. Il determinante L1L2 sin Q2 è zero quando i bracci sono collineari. Il modello non considera collisioni o limiti.

$$
v_x=J_{11}\cdot\omega_1+J_{12}\cdot\omega_2
$$

$$
v_y=J_{21}\cdot\omega_1+J_{22}\cdot\omega_2
$$

| Coefficiente | Geometria della trasformazione delle velocità |
| --- | --- |
| $J_{11}$ | $-L_1\sin(Q_1)-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{12}$ | $-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{21}$ | $L_1\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)$ |
| $J_{22}$ | $L_2\cdot\cos(Q_1+Q_2)$ |



**Derivazione del determinante.** Ogni coefficiente è una derivata parziale della coordinata X o Y dell'utensile rispetto all'angolo articolare Q1 o Q2 in radianti. Con lunghezze in mm, l'unità è mm/rad; moltiplicando per rad/s si ottengono mm/s.

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

Sviluppando i due prodotti del determinante, i termini con L2 al quadrato si annullano. L'identità della differenza dei seni elimina Q1.

$$
\det J=L_1L_2\sin(Q_2)
$$

![I due contributi articolari si sommano come vettori e producono la velocità dell'utensile.](../../../assets/figures/two_link_jacobian_velocity.svg)

*I due contributi articolari si sommano come vettori e producono la velocità dell'utensile.*

### Esempi completamente svolti

1. Un singolo braccio di $L=150$ mm punta a destra per $Q=0^\circ$. Con $\omega=+0.1$ rad/s, $\sin0^\circ=0$ e $\cos0^\circ=1$: $v_x=-150\cdot0\cdot0.1=0$ e $v_y=150\cdot1\cdot0.1=+15$ mm/s. La punta va verso l'alto.
2. Con $Q=45^\circ$ e $\omega=-0.1$ rad/s si inverte il moto: $v_x=-150\sin45^\circ\cdot(-0.1)\approx+10.61$ mm/s, $v_y=150\cos45^\circ\cdot(-0.1)\approx-10.61$ mm/s. La punta va in basso a destra, ma il modulo rimane $L|\omega|=15$ mm/s.
3. Per $L_1=100$ mm, $L_2=50$ mm, $Q_1=30^\circ$, $Q_2=60^\circ$, $\omega_1=0.1$ rad/s e $\omega_2=0.2$ rad/s, il secondo braccio ha orientamento assoluto $Q_1+Q_2=90^\circ$ e velocità angolare $\omega_1+\omega_2=0.3$ rad/s. Quindi $v_x=-100\sin30^\circ\cdot0.1-50\sin90^\circ\cdot0.3=-5-15=-20$ mm/s e $v_y=100\cos30^\circ\cdot0.1+50\cos90^\circ\cdot0.3\approx+8.66$ mm/s.
4. Vicino alla piegatura, con $\delta=0.02$ rad, la variazione assiale sull'asse **fisso** è circa $25\delta^2=25\cdot0.02^2=0.010$ mm; quella trasversale è $50\delta=1.000$ mm e l'aumento radiale $50\delta^2=0.020$ mm. Non confondere i coefficienti dei due termini quadratici.

[Trigonometry](../TRIGONOMETRY.md) · [Coordinate frames](04-coordinate-frames.md) · [Calculus foundations](00-calculus-foundations.md)
