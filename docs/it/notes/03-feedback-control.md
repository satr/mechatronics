# 3. Controllo in retroazione: PID, campionamento e coppia di sostegno

**Lingue:** [en](../../en/notes/03-feedback-control.md) · [fr](../../fr/notes/03-feedback-control.md) · [de](../../de/notes/03-feedback-control.md) · [it](03-feedback-control.md) · [es](../../es/notes/03-feedback-control.md) · [pt](../../pt/notes/03-feedback-control.md) · [zh](../../zh/notes/03-feedback-control.md) · [ja](../../ja/notes/03-feedback-control.md) · [nb](../../nb/notes/03-feedback-control.md) · [ru](../../ru/notes/03-feedback-control.md) · [ko](../../ko/notes/03-feedback-control.md) · [fi](../../fi/notes/03-feedback-control.md) · [pl](../../pl/notes/03-feedback-control.md)

**Unità usate qui (spiegate prima degli esempi):** `rpm` — giro al minuto; `A` — ampere; `s` — secondo; `rpm/s` — giro al minuto / secondo — accelerazione angolare; `A/rpm` — ampere / (giro al minuto) — guadagno per unità di velocità; `A/(rpm·s)` — ampere / (giro al minuto · secondo) — guadagno integrale; `A·s/rpm` — ampere · secondo / (giro al minuto) — guadagno derivativo; `N·m` — newton · metro — momento torcente; `kg` — chilogrammo; `m` — metro; `N` — newton. [Glossario delle unità](../UNITS.md).

[README](../README.md) · [Math foundations](00-calculus-foundations.md) · [First-order dynamics](02-first-order-dynamics.md) · [Trigonometry](../TRIGONOMETRY.md)

> **Modello didattico:** Non collegare questi algoritmi semplificati a motori o macchine reali.

## Indice

- [1. Anello chiuso di velocità](#section-1)
- [2. P: azione proporzionale](#section-2)
- [3. I: errore accumulato e corrente richiesta](#section-3)
- [4. D: variazione dell’errore e rumore del sensore](#section-4)
- [5. Campionamento, saturazione e anti-windup](#section-5)
- [6. Sostenere un giunto robotico contro la gravità](#section-6)
- [7. Verifiche e limiti](#section-7)

<a id="section-1"></a>
## 1. Anello chiuso di velocità

Un **regolatore in retroazione (feedback controller)** confronta setpoint e sensore. Con 1000 rpm richiesti e 950 rpm misurati, errore +50 rpm. Qui PID produce un **setpoint di corrente che genera coppia**, non una variazione da sommare alla corrente precedente.

$$
\varepsilon(t)=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}},
\qquad I_{\mathrm{set}}=u_P+u_I+u_D.
$$

Il drive può contenere un regolatore interno di corrente che modifica tensione o PWM. Altri drive accettano coppia, tensione o PWM: il tipo di comando dipende dal sistema.

<a id="section-2"></a>
## 2. P: azione proporzionale

**P (proportional)** reagisce all’errore **attuale**. Senza feedforward o offset, un carico costante richiede coppia e corrente non nulle. A errore zero P produce zero; può quindi restare un **errore a regime (steady-state error)**.

$$
u_P=K_p\varepsilon,\quad [K_p]=\mathrm{A/rpm}.
$$

<a id="section-3"></a>
## 3. I: errore accumulato e corrente richiesta

**I (integral)** accumula l’errore nel tempo in una sola variabile, non in un elenco storico. Errore positivo: cresce; nullo: resta; negativo: diminuisce. Può quindi conservare corrente anche quando la velocità è esatta.

$$
z(t)=\int_0^t\varepsilon(s)\ \mathrm{d}s,\quad u_I=K_i z(t),\quad [K_i]=\mathrm{A/(rpm\cdot s)}.
$$

```python
integral = 0.0  # saved between controller iterations
for speed in [950, 950, 950, 1000, 1020, 1020]:
    error = 1000 - speed       # rpm
    integral += error * 1.0   # rpm*s; dt = 1 s
    p_command = 0.02 * error # amperes
    i_command = 0.002 * integral # amperes
    current_setpoint = p_command + i_command
    print(round(integral), round(i_command, 2), round(current_setpoint, 2))
```

Con dt = 1 s, Kp = 0.02 A/rpm, Ki = 0.002 A/(rpm·s), tre errori +50 rpm danno integrali 50, 100, 150 rpm·s e contributi I 0.10, 0.20, 0.30 A. Errore zero mantiene 0.30 A; −20 rpm per 1 s dà 0.26 A, ancora 1 s 0.22 A. −0.04 A è la **variazione per passo**, non la nuova corrente totale.

Il programma stampa solo l'integrale accumulato, il contributo I e la corrente totale richiesta. La tabella aggiunge l'errore e il contributo P per mostrare ogni passaggio. I campioni sono distanziati di 1 s e l'integrale parte da zero.

| k | Velocità misurata (rpm) | ε (rpm) | z (rpm·s) | u_P (A) | u_I (A) | I_set (A) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 950 | +50 | 50 | +1.00 | +0.10 | +1.10 |
| 2 | 950 | +50 | 100 | +1.00 | +0.20 | +1.20 |
| 3 | 950 | +50 | 150 | +1.00 | +0.30 | +1.30 |
| 4 | 1000 | 0 | 150 | 0.00 | +0.30 | +0.30 |
| 5 | 1020 | −20 | 130 | −0.40 | +0.26 | −0.14 |
| 6 | 1020 | −20 | 110 | −0.40 | +0.22 | −0.18 |

A 1020 rpm l'errore è −20 rpm: P vale −0.40 A, mentre I è ancora +0.26 A. La somma è una **corrente richiesta con segno di −0.14 A**; al campione successivo è −0.18 A. La variazione del termine I (−0.04 A per passo) non rappresenta la corrente totale. Sono valori del modello didattico, non impostazioni per un azionamento reale.

<a id="section-4"></a>
## 4. D: variazione dell’errore e rumore del sensore

**D (derivative)** reagisce alla **derivata dell’errore**. A setpoint fisso, quando la velocità cresce l’errore diminuisce, dando un termine D negativo che può ridurre l’overshoot. D non è la velocità. Un salto del sensore di 8 rpm in 0.01 s simula 800 rpm/s.

$$
u_D=K_d\frac{\mathrm{d}\varepsilon}{\mathrm{d}t},\quad [K_d]=\mathrm{A\cdot s/rpm},\qquad
\frac{\Delta\omega}{\Delta t}=\frac{8\ \mathrm{rpm}}{0.01\ \mathrm{s}}=800\ \mathrm{rpm/s}.
$$

La derivata dell’errore ha unità rpm/s. Poiché il termine D rappresenta una corrente richiesta in A, il guadagno `K_d` deve compensare rpm/s: la sua unità è A·s/rpm e il prodotto risulta in A.

Il **filtro della derivata (derivative filtering)** attenua il rumore rapido ma introduce ritardo. Spesso si deriva la misura anziché il setpoint per evitare impulsi quando cambia il comando richiesto.

<a id="section-5"></a>
## 5. Campionamento, saturazione e anti-windup

Nel controllo digitale conta il **periodo di campionamento (sampling period)**. Con errore costante 20 rpm, 100 passi da 0.01 s e 10 da 0.1 s sommano entrambi 20 rpm·s in 1 s. Dimenticare dt dà dieci volte più accumulo nel controller veloce.

$$
z_{k+1}=z_k+\varepsilon_k\ \Delta t.
$$

Quando il drive limita la corrente, l’integrale può crescere senza effetto: **integral windup**, con possibile overshoot dopo il calo di carico. **Anti-windup** ferma l’integrazione che aumenta la saturazione oppure corregge lo stato con l’uscita effettiva. Il limite riguarda il comando **totale**, inclusa P.

<a id="section-6"></a>
## 6. Sostenere un giunto robotico contro la gravità

La **costante di coppia Kt (motor torque constant)** indica il momento per ampere che genera coppia, in N·m/A. Kt = 0.1 N·m/A e 2 A danno 0.2 N·m, con la definizione di corrente del produttore.

$$
M_{\mathrm{motor}}=K_t I,\qquad [K_t]=\mathrm{N\cdot m/A}.
$$

Una massa m a distanza L da un giunto orizzontale produce un momento gravitazionale di modulo mgL|cos θ|. In equilibrio, coppia del motore e del carico hanno segno opposto; può servire corrente anche con errore di posizione nullo. Un freno o una trasmissione realmente autobloccante possono trattenere senza corrente; **Harmonic Drive** non è intrinsecamente autobloccante.

$$
J\alpha=M_{\mathrm{motor}}+M_{\mathrm{load}},\quad
\alpha=0\ \Longrightarrow\ M_{\mathrm{motor}}=-M_{\mathrm{load}},
$$
$$
|M_g|=mgL|\cos\theta|.
$$

Nel BLDC **outrunner** gira l’involucro esterno, nell’**inrunner** gira il rotore interno. Rotore = parte che gira, statore = parte fissa.

<a id="section-7"></a>
## 7. Verifiche e limiti

Le correnti sono numeri illustrativi, non impostazioni per hardware reale. Servono protezioni, limiti, filtraggio, calibrazione e prove sicure.

[Math foundation](00-calculus-foundations.md) · [Trigonometry table](../TRIGONOMETRY.md) · [First-order dynamics](02-first-order-dynamics.md)
