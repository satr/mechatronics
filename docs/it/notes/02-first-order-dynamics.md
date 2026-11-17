# 2. Dinamica del primo ordine e rotazione


**Leggi questa pagina in:** [en](../../en/notes/02-first-order-dynamics.md) · [fr](../../fr/notes/02-first-order-dynamics.md) · [de](../../de/notes/02-first-order-dynamics.md) · [it](02-first-order-dynamics.md) · [es](../../es/notes/02-first-order-dynamics.md) · [pt](../../pt/notes/02-first-order-dynamics.md) · [zh](../../zh/notes/02-first-order-dynamics.md) · [ja](../../ja/notes/02-first-order-dynamics.md) · [nb](../../nb/notes/02-first-order-dynamics.md) · [ru](../../ru/notes/02-first-order-dynamics.md) · [ko](../../ko/notes/02-first-order-dynamics.md) · [fi](../../fi/notes/02-first-order-dynamics.md) · [pl](../../pl/notes/02-first-order-dynamics.md)

**Unità usate qui (spiegate prima degli esempi):** `s` — secondo; `mm/s` — millimetro / secondo — velocità lineare; `kg` — chilogrammo; `m` — metro; `rad/s` — radiante / secondo — velocità angolare; `N` — newton; `N·m` — newton · metro — momento torcente; `J` — joule; `rpm` — giro al minuto; `kg·m²` — chilogrammo · metro² — momento d'inerzia; `N·m·s/rad` — newton · metro · secondo / radiante — guadagno per unità di velocità; `%` — percento (un centesimo); `rad` — radiante. [Glossario delle unità](../UNITS.md).

**Fondamenti:** [0. Fondamenti di derivate, differenziali e integrali](00-calculus-foundations.md) · [Tabella degli integrali](../INTEGRAL_TABLE.md)

[README](../README.md) · [Formulario rapido](../CHEATSHEET.md) · [Esercizi Python](../exercises/README.md) · [Moto, derivate e integrali](01-motion-calculus.md)

> **Avvertenza:** Questi materiali didattici, elaborati anche con l'IA, possono contenere errori, traduzioni imprecise e ipotesi non valide. L'uso è a proprio rischio. Verificare i calcoli in modo indipendente; non utilizzare gli esempi per controllare macchine reali.

> **Ipotesi del modello del motore:** Si assume un controllo proporzionale ideale della coppia, senza carico, attrito, ritardi, limiti di tensione, saturazione o dinamiche di ordine superiore. Non è una descrizione universale dei motori.

## In breve

La costante di tempo $\tau$ misura la rapidità con cui un sistema del primo ordine si avvicina al nuovo equilibrio. Il passo $dt$ regola soltanto la discretizzazione numerica. Nel modello ideale $\tau=\frac{J}{K}$: una risposta identica non implica uguali coppia e consumo di energia.

**Termini inglesi:**

- sistema del primo ordine (first-order system)
- costante di tempo (time constant)
- passo temporale (time step)
- momento d’inerzia (moment of inertia)
- coppia (torque)
- guadagno del controllore (controller gain)
- accelerazione angolare (angular acceleration)
- identificazione di sistema (system identification)
- energia cinetica rotazionale (rotational kinetic energy)

## In questa pagina

- [1. Risposta del primo ordine](#section-1)
- [2. Coppia e inerzia](#section-2)
- [3. Passo numerico e costante di tempo](#section-3)
- [4. Stimare la costante di tempo dalle misure](#section-4)
- [5. Energia di rotazione](#section-5)
- [6. Da provare](#section-6)
- [7. Approfondimenti (facoltativi)](#section-7)
  - [Da dove provengono 63.2 %, 86.5 % e 95.0 %?](#time-constant-derivation)
  - [Come si ottengono i risultati di Eulero](#euler-values-derivation)

[Unità SI e punto decimale](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Risposta del primo ordine

Per unità, dimostrazioni e limiti numerici, consultare gli [Approfondimenti](#section-7).

Con velocità obiettivo costante $u$, velocità effettiva $v$ e $\tau>0$, il modello completa circa il $63.2\ \%$ della variazione dopo $\tau$, l'$86.5\ \%$ dopo $2\tau$ e il $95.0\ \%$ dopo $3\tau$. Non significa raggiungere esattamente il valore obiettivo dopo un solo $\tau$.

**Notazione:** $\varepsilon(t)=u-v(t)$ è l’errore di velocità (speed error; epsilon greco). La funzione esponenziale naturale (exponential function) è $\exp(z)=\mathrm{e}^{z}$, dove $\mathrm{e}\approx2.71828$ è il numero di Eulero (Euler’s number), **non** l’errore. [Derivazione e calcolo del 63.2 %](#time-constant-derivation).

$$
\frac{dv}{dt}=\frac{u-v}{\tau}.
$$

$$
v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right).
$$

| Tempo | Frazione della variazione |
| --- | ---: |
| $\tau$ | 63.2 % |
| $2\tau$ | 86.5 % |
| $3\tau$ | 95.0 % |

[Perché proprio queste percentuali? Vedi il calcolo.](#time-constant-derivation)

![Risposta normalizzata del primo ordine: ogni costante di tempo elimina circa il 63.2 % dell’errore residuo.](../../../assets/figures/first_order_response.svg)

<a id="section-2"></a>

## 2. Coppia e inerzia

Il controllore calcola un comando elettrico; la coppia meccanica $M$ è generata fisicamente dal motore. Nel modello $J$ è il momento d'inerzia, $\omega$ la velocità angolare, e $K$ il coefficiente che lega la coppia all'errore di velocità. Raddoppiare $J$ con $K$ fisso raddoppia $\tau$. Raddoppiare sia $J$ sia $K$ conserva $\tau$ ma raddoppia la coppia richiesta a parità di errore. Attrito, carichi, ritardi e limiti di corrente non sono inclusi.

$$
J\frac{d\omega}{dt}=M,\qquad M=K(u-\omega).
$$

$$
\frac{d\omega}{dt}=\frac{K}{J}(u-\omega),\qquad \tau=\frac{J}{K}.
$$

**Unità:** $J$: $\mathrm{kg}\cdot\mathrm{m}^2$; $\omega,u$: $\mathrm{rad/s}$; $M$: $\mathrm{N}\cdot\mathrm{m}$; $K$: $\mathrm{N}\cdot\mathrm{m}\cdot\mathrm{s}/\mathrm{rad}$; $\tau$: s.

Ciclo di retroazione simbolico nel modello ideale. Il controllore invia il comando; il motore produce la coppia fisica.

![Ciclo di retroazione simbolico nel modello ideale. Il controllore invia il comando; il motore produce la coppia fisica](../../../assets/figures/control_loop.svg)

<a id="section-3"></a>

## 3. Passo numerico e costante di tempo

Eulero aggiorna il valore a intervalli di durata $dt$. Ridurre $dt$ non accelera il motore nel modello: migliora l'approssimazione. Con $u=10\ \mathrm{mm/s}$, $\tau=1\ \mathrm{s}$ e durata di un secondo, Eulero dà $6.513$ con $dt=0.1$ oppure $6.340\ \mathrm{mm/s}$ con $dt=0.01$; il valore esatto è $6.321\ \mathrm{mm/s}$.

$$
v_{n+1}=v_n+\frac{u-v_n}{\tau}\ dt.
$$

| Metodo | $v(1\ \mathrm{s})$ (mm/s) |
| --- | ---: |
| Euler $dt=0.1\ \mathrm{s}$ | 6.513 |
| Euler $dt=0.01\ \mathrm{s}$ | 6.340 |
| Esatto | 6.321 |

[Calcolo dei valori numerici.](#euler-values-derivation)

<a id="section-4"></a>

## 4. Stimare la costante di tempo dalle misure

Per un comando da 0 a 1000 rpm (giri al minuto), si osserva quando la velocità misurata raggiunge circa 632 rpm. Se accade dopo 2 secondi, il modello del primo ordine suggerisce $\tau\approx2\ \mathrm{s}$. Se la velocità iniziale non è zero, si usa il 63.2 % della **variazione totale**. Rumore, ritardo e sovraelongazione rendono più incerta questa identificazione di sistema (system identification).

**Che cosa restituisce il codice:** la funzione [`estimate_tau`](../../../exercises/02_first_order_response.py) richiede misure con timestamp **strettamente crescenti**, contati dall'inizio del gradino. Restituisce il tempo del **primo campione osservato** che raggiunge la soglia del 63.2 % della variazione, tollerando metà della risoluzione di misura nota. Se la soglia appare per la prima volta a 2 s e il campione precedente era a 1 s, l'attraversamento reale può essere avvenuto **tra i campioni**. Quindi 2 s è una stima limitata dal campionamento, non un valore esatto. Campioni non validi o timestamp ripetuti e fuori ordine vengono rifiutati anche dopo la soglia; senza attraversamento si ottiene `None`.

**La risoluzione del sensore conta:** il parametro `resolution` di `estimate_tau` deve essere **inferiore al modulo della variazione complessiva di velocità**. Se la velocità passa da 0 a 10 rpm, ma il display cambia solo a passi di 10 rpm, il passaggio della soglia del 63.2 % non può essere stimato in modo affidabile. La funzione rifiuta i dati anziché segnalare un attraversamento artificiale al primo campione. Anche con una risoluzione sufficiente, la stima è limitata dal campionamento.

<a id="section-5"></a>

## 5. Energia di rotazione

La coppia risultante soddisfa $M=J\alpha$. Con $J=2\ \mathrm{kg}\cdot\mathrm{m}^2$ e $\omega=10\ \mathrm{rad/s}$, l'energia rotazionale vale $100\ \mathrm{J}$; raddoppiare $J$ porta a $200\ \mathrm{J}$. Raddoppiare $\omega$ quadruplica l'energia. L'energia meccanica non coincide con il consumo elettrico totale.

$$
M=J\alpha,\qquad \alpha=\frac{d\omega}{dt}.
$$

$$
E=\frac{1}{2}J\omega^2.
$$

<a id="section-6"></a>

## 6. Da provare

Per un gradino ideale da 0 a 1000 rpm, raggiungere circa 632 rpm dopo due secondi suggerisce $\tau\approx2\ \mathrm{s}$. Rumore e campionamento possono richiedere tecniche di identificazione più accurate. Confrontare la soluzione di Eulero con quella esatta.

[02_first_order_response.py](../../../exercises/02_first_order_response.py) · [03_rotation_energy.py](../../../exercises/03_rotation_energy.py) · [plot_models.py](../../../exercises/plot_models.py)


<a id="section-7"></a>

## 7. Approfondimenti (facoltativi)


### Stabilità di Eulero

A ogni passo **l’errore rispetto al comando** è moltiplicato per $1-\frac{dt}{\tau}$. Per convergere serve $0<dt<2\tau$; per $\tau<dt<2\tau$ il valore numerico oscilla intorno al comando, senza implicare oscillazioni fisiche del motore.

### Limiti del modello

Una relazione più generale è $J\ \frac{d\omega}{dt}=M_{\text{motore}}-M_{\text{carico}}-M_{\text{attrito}}$. La formula $\tau=\frac{J}{K}$ richiede l’ipotesi $M_{\text{risultante}}=K(u-\omega)$. Attrito, carico, ritardo e limiti di corrente possono modificare la risposta.

### Energia e potenza

Per $J$ costante, $\Delta E=\frac{1}{2} J(\omega_2^2-\omega_1^2)$ e la potenza meccanica istantanea (mechanical power) è $P=M\omega$. Ciò non equivale al consumo elettrico totale.


<a id="time-constant-derivation"></a>

### Da dove provengono 63.2 %, 86.5 % e 95.0 %?

Le percentuali e l’esponenziale derivano **dalla stessa equazione**. Definiamo l’errore di velocità come $\varepsilon(t)=u-v(t)$ (non il numero di Eulero). Con $u$ costante, $\frac{d\varepsilon}{dt}=-\frac{dv}{dt}$:

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

La separazione delle variabili divide per $\varepsilon$, quindi questo passaggio presuppone un errore iniziale diverso da zero. Se $u=v_0$, l'errore rimane nullo e l'equazione differenziale originale fornisce direttamente la soluzione costante $v(t)=u$.

$$
f(t)=\frac{v(t)-v_0}{u-v_0}=1-\exp\!\left(-\frac{t}{\tau}\right),\qquad (u\ne v_0).
$$

| $t$ | $f(t)$ |
| ---: | ---: |
| $\tau$ | $1-\exp(-1)=0.63212056\ldots\approx63.2\ \%$ |
| $2\tau$ | $1-\exp(-2)=0.86466472\ldots\approx86.5\ \%$ |
| $3\tau$ | $1-\exp(-3)=0.95021293\ldots\approx95.0\ \%$ |

Per un gradino da 0 a 1000 rpm, si ottengono circa 632, 865 e 950 rpm dopo una, due e tre costanti di tempo. Nel modello ideale, la velocità si avvicina asintoticamente al valore richiesto.

<a id="euler-values-derivation"></a>

### Come si ottengono i risultati di Eulero

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
