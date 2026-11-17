# 1. Moto, derivate e integrali


**Leggi questa pagina in:** [en](../../en/notes/01-motion-calculus.md) · [fr](../../fr/notes/01-motion-calculus.md) · [de](../../de/notes/01-motion-calculus.md) · [it](01-motion-calculus.md) · [es](../../es/notes/01-motion-calculus.md) · [pt](../../pt/notes/01-motion-calculus.md) · [zh](../../zh/notes/01-motion-calculus.md) · [ja](../../ja/notes/01-motion-calculus.md) · [nb](../../nb/notes/01-motion-calculus.md) · [ru](../../ru/notes/01-motion-calculus.md) · [ko](../../ko/notes/01-motion-calculus.md) · [fi](../../fi/notes/01-motion-calculus.md) · [pl](../../pl/notes/01-motion-calculus.md)

**Unità usate qui (spiegate prima degli esempi):** `s` — secondo; `mm` — millimetro = 0.001 m; `mm/s` — millimetro / secondo — velocità lineare; `mm/s²` — millimetro / secondo² — accelerazione; `%` — percento (un centesimo). [Glossario delle unità](../UNITS.md).

**Fondamenti:** [0. Fondamenti di derivate, differenziali e integrali](00-calculus-foundations.md) · [Tabella degli integrali](../INTEGRAL_TABLE.md)

[README](../README.md) · [Formulario rapido](../CHEATSHEET.md) · [Esercizi Python](../exercises/README.md) · [Dinamica del primo ordine e rotazione](02-first-order-dynamics.md)

> **Avvertenza:** Questi materiali didattici, elaborati anche con l'IA, possono contenere errori, traduzioni imprecise e ipotesi non valide. L'uso è a proprio rischio. Verificare i calcoli in modo indipendente; non utilizzare gli esempi per controllare macchine reali.

## In breve

Lo spazio percorso è la lunghezza totale del tragitto; lo spostamento è posizione finale meno posizione iniziale. La rapidità o modulo della velocità (speed) non è negativa, mentre la velocità vettoriale (velocity) comprende la direzione. La derivata della posizione restituisce la velocità istantanea e l'integrale della velocità con segno restituisce lo spostamento.

**Termini inglesi:**

- distanza percorsa (distance traveled)
- spostamento (displacement)
- rapidità (speed)
- velocità vettoriale (velocity)
- derivata (derivative)
- integrale (integral)
- integrazione numerica (numerical integration)
- metodo di Eulero esplicito (explicit Euler method)

## In questa pagina

- [1. Esempio di movimento](#section-1)
- [2. Derivata e velocità istantanea](#section-2)
- [3. Integrale e spostamento](#section-3)
- [4. Integrazione numerica](#section-4)
- [5. Da provare](#section-5)
- [6. Approfondimenti (facoltativi)](#section-6)
  - [Perché la derivata di 2t² è 4t](#power-rule-derivation)
  - [Calcolo degli spostamenti nella tabella](#motion-values-derivation)

[Unità SI e punto decimale](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Esempio di movimento

Per unità, dimostrazioni e limiti numerici, consultare gli [Approfondimenti](#section-6).

Un asse virtuale si muove a $+3\ \mathrm{mm/s}$ per due secondi e a $-3\ \mathrm{mm/s}$ per altri due. Lo spostamento è $+6-6=0\ \mathrm{mm}$, ma lo spazio percorso è $12\ \mathrm{mm}$. Nel moto circolare la direzione del vettore velocità cambia anche quando il suo modulo è costante.

$$
\overline{v}=\frac{x(t_2)-x(t_1)}{t_2-t_1}.
$$

$$
\text{velocità scalare media}=\frac{\text{distanza totale percorsa}}{t_2-t_1}.
$$

Durante **tutti i quattro secondi**, la velocità vettoriale media con segno e la velocità scalare media hanno **valori diversi**. L'asse torna all'inizio dopo aver percorso 12 mm:

$$
\overline{v}_x=\frac{0\ \mathrm{mm}}{4\ \mathrm{s}}=0\ \mathrm{mm/s}
$$

$$
\overline{\lvert v\rvert}=\frac{12\ \mathrm{mm}}{4\ \mathrm{s}}=3\ \mathrm{mm/s}
$$

Quindi la velocità scalare media **non coincide necessariamente con il modulo della velocità vettoriale media**. Dopo un giro completo il vettore velocità media è nullo, ma distanza percorsa e velocità scalare media sono positive.

<a id="section-2"></a>

## 2. Derivata e velocità istantanea

Con $x(t)=2t^2\ \mathrm{mm}$ e $t$ in secondi, $v(t)=4t\ \mathrm{mm/s}$. **Perché 4?** La regola di derivazione dà $d(t^2)/dt=2t$; quindi $2t^2$ diventa $2\cdot2t=4t$. [Calcolo completo e unità](#power-rule-derivation). A $t=1\ \mathrm{s}$ la velocità istantanea è $4\ \mathrm{mm/s}$. Una differenza finita in avanti fornisce $6$, $4.2$ e $4.02\ \mathrm{mm/s}$ usando $dt=1$, $0.1$ e $0.01\ \mathrm{s}$.

$$
v(t)=\frac{dx}{dt},\qquad v(t)\approx\frac{x(t+dt)-x(t)}{dt}.
$$

**Perché un passo troppo piccolo può ingannare:** a $t=1\ \mathrm{s}$, la derivata esatta di $x(t)=2t^2$ è $4\ \mathrm{mm/s}$. Con $dt=1e-17\ \mathrm{s}$, Python `float` arrotonda `t + dt` a `t`: le due posizioni calcolate sono uguali e la differenza suggerirebbe erroneamente velocità zero. A scale ancora più piccole, entrambe le posizioni possono sottorappresentarsi a zero pur avendo derivata non nulla. L'esempio [`forward_derivative`](../../../exercises/01_motion_and_integral.py) ora solleva `ValueError` invece di restituire questo falso zero. Continua a calcolare la differenza finita: scegliere un passo risolvibile numericamente, anziché ridurlo all'infinito.

<a id="section-3"></a>

## 3. Integrale e spostamento

L'integrale della velocità con segno può essere nullo o negativo, mentre l'integrale del suo modulo è una distanza non negativa. Per $v(t)=2t\ \mathrm{mm/s}$ da $0$ a $2\ \mathrm{s}$, lo spostamento esatto è $4\ \mathrm{mm}$.

$$
\Delta x=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t,\qquad
s=\int_{t_1}^{t_2}|v(t)|\ \mathrm{d}t.
$$

Geometricamente, il primo integrale rappresenta l’area con segno sotto il grafico velocità–tempo. **Questo è un esempio diverso da quello della sezione 2.** Lì la posizione $x(t)=2t^2$ ha derivata $v(t)=4t$. Per mostrare l’integrazione si sceglie qui volutamente un’altra velocità: $v(t)=2t$. La posizione corrispondente è $x(t)=t^2+C$ (con unità coerenti). Le due leggi del moto non vanno confuse.

<a id="section-4"></a>

## 4. Integrazione numerica

Spostamento esatto e approssimazione di Eulero al principio del passo (dati sintetici).

![Spostamento esatto e approssimazione di Eulero al principio del passo (dati sintetici)](../../../assets/figures/euler_vs_exact.svg)

Il metodo di Eulero esplicito usa la velocità **all'inizio** di ciascun intervallo, non la media esatta. Per questa velocità crescente sottostima lo spostamento: con $dt=0.5$, $0.1$ e $0.01\ \mathrm{s}$ otteniamo $3$, $3.8$ e $3.98\ \mathrm{mm}$ (valore esatto $4\ \mathrm{mm}$). La regola dei trapezi è esatta in questo esempio lineare.

$$
x_{n+1}=x_n+v(t_n)\ dt.
$$

| `dt` (s) | Euler (mm) |
| ---: | ---: |
| 0.5 | 3.000 |
| 0.1 | 3.800 |
| 0.01 | 3.980 |
| Esatto | 4.000 |


[Calcolo di 3; 3.8 e 3.98.](#motion-values-derivation)

<a id="section-5"></a>

## 5. Da provare

Eseguire il programma sul moto e diminuire $dt$. Perché un percorso di andata e ritorno può avere spostamento nullo ma spazio percorso positivo?

[01_motion_and_integral.py](../../../exercises/01_motion_and_integral.py)

<a id="section-6"></a>

## 6. Approfondimenti (facoltativi)

### Unità e coefficienti

Se $t$ è in secondi, $x(t)=2t^2$ mm è una notazione abbreviata: il coefficiente è $2\ \mathrm{mm/s^2}$. La derivata $v(t)=4t$ ha quindi unità mm/s. Controllare sempre la coerenza dimensionale.

### Limiti dell’approssimazione

Una differenza finita (finite difference) stima la derivata su un intervallo non nullo. Ridurre il passo spesso diminuisce l’errore di discretizzazione, ma un passo troppo piccolo può amplificare errori di arrotondamento e rumore. Eulero usa il valore iniziale del passo.

### Moto multidimensionale

Per il vettore posizione $\mathbf r(t)$, $\mathbf v=d\mathbf r/dt$; la rapidità è $\|\mathbf v\|$ e la lunghezza del percorso è $s=\int\|\mathbf v(t)\|dt$.


<a id="power-rule-derivation"></a>

### Perché la derivata di $2t^2$ è $4t$



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

### Calcolo degli spostamenti nella tabella

$$
a=2\ \mathrm{mm/s^2},\qquad v(t)=at,\qquad 0\le t\le2\ \mathrm{s}.
$$

$$
\Delta x=\int_{0}^{2\ \mathrm{s}}at\ \mathrm{d}t
=\left[\frac{at^2}{2}\right]_{0}^{2\ \mathrm{s}}
=4\ \mathrm{mm}.
$$



Il simbolo $\sum$ (sigma maiuscola greca, **sommatoria** / summation) indica la somma di più termini. In $\sum_{n=0}^{N-1}(2nh)h$, l’indice $n$ assume i valori $0; 1; \ldots; N-1$: in totale $N$ termini. È come un ciclo Python `for` che accumula ogni contributo. Per esempio, $\sum_{n=1}^{3}n=1+2+3=6$. [← Spiegazione dei simboli](../SYMBOLS.md#summation).

$$
h=\frac{dt}{1\ \mathrm{s}},\qquad N=\frac{2}{h}.
$$

$$
x_{\mathrm{Euler}}(2\ \mathrm{s})
=\left[\sum_{n=0}^{N-1}(2nh)h\right]\ \mathrm{mm}
=\left[h^2N(N-1)\right]\ \mathrm{mm}
=(4-2h)\ \mathrm{mm}.
$$

Qui `h` è il valore numerico del passo `dt` in secondi (`dt = 0.5 s` dà `h = 0.5`); `N` è il numero di passi. Il risultato è una **distanza in millimetri**.



Con $dt=0.5$, $0.1$ e $0.01$ secondi si ottengono $3$, $3.8$ e $3.98$ millimetri. Si suppone che $2/dt$ sia intero.
