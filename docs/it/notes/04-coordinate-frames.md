# 4. Sistemi di riferimento del robot e cinematica piana

**Languages:** [en](../../en/notes/04-coordinate-frames.md) · [fr](../../fr/notes/04-coordinate-frames.md) · [de](../../de/notes/04-coordinate-frames.md) · [it](04-coordinate-frames.md) · [es](../../es/notes/04-coordinate-frames.md) · [pt](../../pt/notes/04-coordinate-frames.md) · [zh](../../zh/notes/04-coordinate-frames.md) · [ja](../../ja/notes/04-coordinate-frames.md) · [nb](../../nb/notes/04-coordinate-frames.md) · [ru](../../ru/notes/04-coordinate-frames.md) · [ko](../../ko/notes/04-coordinate-frames.md) · [fi](../../fi/notes/04-coordinate-frames.md) · [pl](../../pl/notes/04-coordinate-frames.md)

**Unità usate qui (spiegate prima degli esempi):** `mm` — millimetro = 0.001 m; `°` — grado. [Glossario delle unità](../UNITS.md).

[README](../README.md) · [Trigonometria](../TRIGONOMETRY.md) · [Simboli matematici](../SYMBOLS.md) · [Controllo in retroazione](03-feedback-control.md)

> **Modello didattico:** Non utilizzare queste formule semplificate per comandare robot o macchine reali.

## Indice
1. [Perché usare i sistemi di riferimento](#section-1)
2. [Rotazione e traslazione](#section-2)
3. [Concatenare i sistemi](#section-3)
4. [Cinematica diretta di due segmenti](#section-4)
5. [Due configurazioni e spazio raggiungibile](#section-5)
6. [Esercizi con soluzioni complete](#section-6)
7. [Limiti e matrici](#section-7)

<a id="section-1"></a>
## 1. Perché usare i sistemi di riferimento

Un **sistema di riferimento (coordinate frame)** ha un'origine e assi orientati. Il **sistema globale (world frame)** W è fissato alla base; il **sistema dell'utensile (tool frame)** T si muove con l'utensile. Lo stesso punto fisico ha coordinate diverse nei due sistemi. Posizione significa punto, orientamento significa direzione degli assi. Un cambio di coordinate non implica movimento.

Usare la stessa unità per tutte le lunghezze (mm). Gli angoli positivi in 2D si misurano in senso antiorario da +X globale. Gli indici w e l indicano globale e locale. Il modello assume segmenti rigidi.

<a id="section-2"></a>
## 2. Rotazione e traslazione

![Assi globali e locali dopo +90°; punti P e Q.](../../../assets/figures/world_local_frames.svg)

*Assi globali e locali dopo +90°; punti P e Q.*

L'origine T è in (100 mm, 50 mm) nel sistema globale, ruotata di +90°. L'asse locale +x punta verso +Y globale, +y locale verso −X globale. Di conseguenza P=(0 mm, 10 mm) locale diventa (90 mm, 50 mm) globale e Q=(20 mm, 0 mm) diventa (100 mm, 70 mm).

Per il punto locale $(x_l,y_l)$, l'origine globale $(t_x,t_y)$ e l'angolo $\theta$, **prima ruotare e poi traslare**:

$$
x_w=t_x+x_l\cos\theta-y_l\sin\theta
$$

$$
y_w=t_y+x_l\sin\theta+y_l\cos\theta
$$

Il segno di $\sin\theta$ e $\cos\theta$ dipende dall'angolo orientato. Per $\theta=0^\circ$ basta aggiungere l'origine. Non sono comandi a un motore.

<a id="section-3"></a>
## 3. Concatenare i sistemi

I riferimenti possono formare la catena **W → T → S** (mondo → utensile → sensore). Se S ha origine (20 mm, 0 mm) in T e assi paralleli a T, la sua origine globale è (100 mm, 70 mm). Un punto (0 mm, 10 mm) in S è (90 mm, 70 mm) nel mondo. Si procede dal riferimento figlio a quello genitore.

Con vettori colonna, $T_{WS}=T_{WT}T_{TS}$; $T_{AB}$ trasforma le coordinate **da B ad A**. L'ordine delle matrici non è intercambiabile.

**Calcolo matriciale completo (vettori colonna):** il sistema T è ruotato di +90° rispetto a W e ha origine globale (100 mm, 50 mm). Il sensore S non ha ulteriore rotazione e ha origine locale (20 mm, 0 mm) in T, dove si trova Q nella figura precedente. Le parti di rotazione sono adimensionali; le traslazioni sono in mm:

$$
T_{WT}=
\begin{bmatrix}
0 & -1 & 100\\
1 & 0 & 50\\
0 & 0 & 1
\end{bmatrix}
$$

$$
T_{TS}=
\begin{bmatrix}
1 & 0 & 20\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
$$

$$
T_{WS}=T_{WT}T_{TS}=
\begin{bmatrix}
0 & -1 & 100\\
1 & 0 & 70\\
0 & 0 & 1
\end{bmatrix}
$$

$$
T_{WS}\begin{bmatrix}0\\10\\1\end{bmatrix}
=\begin{bmatrix}90\\70\\1\end{bmatrix}
$$

Il prodotto ruota prima lo spostamento locale (20 mm, 0 mm) del sensore in (0 mm, 20 mm) nel mondo, poi lo somma a (100 mm, 50 mm). Il punto (0 mm, 10 mm) di S diventa quindi (90 mm, 70 mm) in W. Sommare 20 mm direttamente alla X globale sarebbe errato, perché lo spostamento è definito **in T**. L'ultima coordinata omogenea 1 è adimensionale. È un calcolo di coordinate; [tf2 in ROS 2](06-ros2-foundations.md#section-7) pubblica e interroga trasformazioni con timestamp, senza risolvere la cinematica inversa.

<a id="section-4"></a>
## 4. Cinematica diretta di due segmenti

![Angoli 30° e relativo 60° dei due segmenti.](../../../assets/figures/two_link_fk.svg)

*Angoli 30° e relativo 60° dei due segmenti.*

Un braccio piano ha segmenti $L_1,L_2$. $\theta_1$ è l'angolo di L1 rispetto a +X globale; $\theta_2$ è **relativo al primo segmento**. La direzione assoluta del secondo è quindi $\theta_1+\theta_2$. Le coordinate dell'utensile sono la somma dei vettori:

$$
X=L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2)
$$

$$
Y=L_1\sin\theta_1+L_2\sin(\theta_1+\theta_2)
$$

Con L1=100 mm, L2=50 mm, $\theta_1=30^\circ$, $\theta_2=60^\circ$, il gomito si trova in (86.60 mm, 50 mm). Il secondo segmento punta verso l'alto e l'utensile si trova in (86.60 mm, 100 mm).

<a id="section-5"></a>
## 5. Due configurazioni e spazio raggiungibile

![Due configurazioni diverse per la stessa posizione.](../../../assets/figures/two_link_elbow_solutions.svg)

*Due configurazioni diverse per la stessa posizione.*

La **cinematica inversa (inverse kinematics)** calcola gli angoli per una posizione richiesta. Due segmenti da 100 mm raggiungono (100 mm, 100 mm) con $(\theta_1,\theta_2)=(0^\circ,+90^\circ)$ oppure $(+90^\circ,-90^\circ)$. L'angolo θ2 resta relativo.

![Corona circolare raggiungibile con raggio 50–150 mm.](../../../assets/figures/two_link_workspace.svg)

*Corona circolare raggiungibile con raggio 50–150 mm.*

Senza limiti o collisioni, $|L_1-L_2|\le r\le L_1+L_2$. Con 100 mm e 50 mm, la zona ideale è una **corona circolare** di raggio da 50 mm a 150 mm. Gli ostacoli reali riducono questo spazio.

<a id="section-6"></a>
## 6. Esercizi con soluzioni complete

Tutti e **sei gli esercizi includono soluzione e spiegazione**, senza lasciare domande personali inevase.

<a id="worked-1"></a>
### 6.1. Punto locale P ruotato

**Problema.** T in (100 mm, 50 mm), ruotato +90°; trovare P=(0 mm, 10 mm) nel mondo.

**Soluzione.** L'asse +y locale punta verso −X globale: diminuire X di 10 mm.

$$
x_w=100+0\cdot0-10\cdot1=90\ \mathrm{mm}
$$

$$
y_w=50+0\cdot1+10\cdot0=50\ \mathrm{mm}
$$

**Risposta:** (90 mm, 50 mm).

<a id="worked-2"></a>
### 6.2. Punto locale Q sull'asse x

**Problema.** Stesso T, trovare Q=(20 mm, 0 mm) nel mondo.

**Soluzione.** L'asse +x locale punta verso +Y globale: aumentare Y di 20 mm.

$$
x_w=100+20\cdot0-0\cdot1=100\ \mathrm{mm}
$$

$$
y_w=50+20\cdot1+0\cdot0=70\ \mathrm{mm}
$$

**Risposta:** (100 mm, 70 mm).

<a id="worked-3"></a>
### 6.3. Cinematica diretta a due segmenti

**Problema.** L1=100 mm, L2=50 mm, θ1=30°, θ2 relativo=60°. Trovare l'utensile.

**Soluzione.** L'angolo assoluto del secondo segmento è 30°+60°=90°.

$$
X=100\cos30^\circ+50\cos90^\circ=50\sqrt3\approx86.60\ \mathrm{mm}
$$

$$
Y=100\sin30^\circ+50\sin90^\circ=100\ \mathrm{mm}
$$

**Risposta:** (86.60 mm, 100 mm).

<a id="worked-4"></a>
### 6.4. Due soluzioni della cinematica inversa

**Problema.** Due segmenti da 100 mm devono raggiungere (100 mm, 100 mm). Due coppie di angoli?

**Soluzione.** La prima configurazione va a destra e poi su; la seconda su e poi a destra.

$$
(\theta_1,\theta_2)=(0^\circ,+90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

$$
(\theta_1,\theta_2)=(+90^\circ,-90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

<a id="worked-5"></a>
### 6.5. Verifica della raggiungibilità

**Problema.** L1=100 mm, L2=50 mm. Verificare (0 mm, 120 mm) e (0 mm, 0 mm).

**Soluzione.** Confrontare la distanza con la differenza e la somma delle lunghezze.

$$
r_{\min}=|100-50|=50\ \mathrm{mm},\qquad r_{\max}=100+50=150\ \mathrm{mm}
$$

$$
r_{(0, 120)}=\sqrt{0^2+120^2}=120\ \mathrm{mm}
$$

(0 mm, 120 mm) è **raggiungibile** perché 50 ≤ 120 ≤ 150. L'origine (0 mm, 0 mm) è **irraggiungibile** perché la distanza vale zero.

<a id="worked-6"></a>
### 6.6. Coseno dell'angolo relativo del gomito

**Problema.** L1=100 mm, L2=50 mm, r=120 mm: calcolare cos θ2.

**Soluzione.** Il coseno dà la flessione in valore assoluto; le due configurazioni speculari hanno θ2 di segno opposto.

$$
\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}
=\frac{14400-10000-2500}{10000}=\frac{1900}{10000}=0.19
$$

$$
\theta_2\approx\pm79.05^\circ
$$

L'angolo interno del triangolo è $\varphi=180^\circ-|\theta_2|$. Dal solo raggio non si ricava $\theta_1$. Si veda lo schema in [Trigonometria](../TRIGONOMETRY.md).

<a id="section-7"></a>
## 7. Limiti e matrici

Il modello è piano e rigido. In realtà esistono limiti dei giunti, collisioni, gioco, deformazioni, errore dello zero dell'encoder e calibrazione dei sensori. Un encoder misura un angolo, non direttamente la posizione globale. Gli esempi non sono istruzioni per macchine reali.

**Matrice omogenea facoltativa:** una matrice 3×3 combina rotazione e traslazione per il punto colonna $[x_l,y_l,1]^T$. Il vettore di spostamento ha l'ultima coordinata pari a 0.

$$
T_{WL}=
\begin{bmatrix}
\cos\theta & -\sin\theta & t_x \\
\sin\theta & \cos\theta & t_y \\
0 & 0 & 1
\end{bmatrix},
\qquad
\begin{bmatrix}x_w\\y_w\\1\end{bmatrix}
=T_{WL}\begin{bmatrix}x_l\\y_l\\1\end{bmatrix}
$$

[Trigonometria](../TRIGONOMETRY.md) · [Simboli matematici](../SYMBOLS.md) · [Controllo in retroazione](03-feedback-control.md)

[Prossimo: rotazione, velocità e singolarità](05-velocity-jacobian.md)
