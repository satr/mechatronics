# 0. Fondamenti di analisi: derivate, limiti e integrali nella meccanica

**Lingue:** [en](../../en/notes/00-calculus-foundations.md) · [fr](../../fr/notes/00-calculus-foundations.md) · [de](../../de/notes/00-calculus-foundations.md) · [it](00-calculus-foundations.md) · [es](../../es/notes/00-calculus-foundations.md) · [pt](../../pt/notes/00-calculus-foundations.md) · [zh](../../zh/notes/00-calculus-foundations.md) · [ja](../../ja/notes/00-calculus-foundations.md) · [nb](../../nb/notes/00-calculus-foundations.md) · [ru](../../ru/notes/00-calculus-foundations.md) · [ko](../../ko/notes/00-calculus-foundations.md) · [fi](../../fi/notes/00-calculus-foundations.md) · [pl](../../pl/notes/00-calculus-foundations.md)

L'**esponenziale naturale** è $\exp(x)=\mathrm{e}^{x}$, dove il **numero di Eulero** è $\mathrm{e}\approx2.71828$. Descrive crescita o decadimento continui; $\exp(0)=1$ e $\exp(-1)\approx0.3679$. Il logaritmo naturale $\ln$ è la sua funzione inversa: $\ln(\exp(x))=x$. Vedi la [guida ai simboli](../SYMBOLS.md).

**Unità usate qui (spiegate prima degli esempi):** `s` — secondo; `mm` — millimetro = 0.001 m; `mm/s` — millimetro / secondo — velocità lineare; `mm/s²` — millimetro / secondo² — accelerazione; `kg·m²` — chilogrammo · metro² — momento d'inerzia; `rad/s` — radiante / secondo — velocità angolare; `rad/s²` — radiante / secondo² — accelerazione angolare; `N·m` — newton · metro — momento torcente; `W` — watt; `rpm` — giro al minuto; `N/m` — newton / metro — rigidezza; `mm³/s` — millimetro³ / secondo — portata volumetrica; `%` — percento (un centesimo); `m` — metro; `kg` — chilogrammo; `N` — newton; `J` — joule; `rad` — radiante. [Glossario delle unità](../UNITS.md).

[README](../README.md) · [Integral table](../INTEGRAL_TABLE.md) · [Trigonometry table](../TRIGONOMETRY.md) · [Motion](01-motion-calculus.md) · [Dynamics](02-first-order-dynamics.md) · [Symbols](../SYMBOLS.md)

> **Modello didattico:** Verificare modelli e unità; non collegare il codice a macchine reali.

La **derivata (derivative)** indica la variazione istantanea; la **derivata seconda (second derivative)** descrive come cambia tale velocità di variazione. L’**integrale (integral)** accumula variazioni. Il **limite (limit)** definisce un tasso istantaneo; il **logaritmo (logarithm)** consente di ricavare il tempo da una risposta esponenziale.

Questi strumenti servono per assi di macchine, servomotori, giunti robotici, molle e sensori. Partiamo dal problema fisico, poi scegliamo regola e unità.

## Indice

- [1. Dalla variazione misurata al modello](#section-1)
- [2. Limiti e derivate prime](#section-2)
- [3. Derivata prima e seconda: un asse in movimento](#section-3)
- [4. Regola della catena: energia di rotazione](#section-4)
- [5. Esponenziali e logaritmi: tempo di risposta](#section-5)
- [6. Integrali: spostamento e lavoro meccanico](#section-6)
- [7. Esempio aggiuntivo: sfera in espansione](#section-7)
- [8. Unità, verifiche ed esercizi](#section-8)

<a id="section-1"></a>
## 1. Dalla variazione misurata al modello

| Domanda fisica | Strumento matematico |
| --- | --- |
| Quanto velocemente si muove l’asse **ora**? | Derivata prima $dx/dt$ |
| Come cambia la velocità? | Derivata seconda $d^2x/dt^2$ |
| Quando si raggiunge il 90 %? | Logaritmo $\ln$ |
| Quanto si sposta in 2 s? | Integrale definito $\int v\ \mathrm{d}t$ |
| Quale lavoro di una forza variabile? | Integrale $\int F\ \mathrm{d}x$ |

<a id="section-2"></a>
## 2. Limiti e derivate prime

La **differenza finita (finite difference)** tra due letture dà una variazione media nell’intervallo. La derivata è il limite di quel rapporto quando l’intervallo tende a zero.

$$
v(t)=\frac{dx}{dt}=\lim_{h\to0}\frac{x(t+h)-x(t)}{h}.
$$

Per $x(t)=a t^2$ con $a=2\ \mathrm{mm/s^2}$, sviluppiamo il numeratore prima del limite:

$$
\frac{x(t+h)-x(t)}h=\frac{a[(t+h)^2-t^2]}h=a(2t+h)\longrightarrow 2at.
$$

Il fattore $h$ si cancella **prima** di porre il limite a zero. A $t=1\ \mathrm{s}$ la velocità istantanea è $4\ \mathrm{mm/s}$. Non valutiamo direttamente la forma indeterminata $0/0$.

**Regole di derivazione (differentiation rules)**: $c$ e $n$ costanti; argomenti trigonometrici in radianti.

| Regola | Formula |
| --- | --- |
| Costante | $\frac{d}{dt}c=0$ |
| Potenza | $\frac{d}{dt}t^n=n t^{n-1}$ |
| Coefficiente e somma | $(cf+g)'=cf'+g'$ |
| Prodotto | $(fg)'=f' g+fg'$ |
| Quoziente, $g\ne0$ | $\left(\frac{f}{g}\right)'=\frac{f' g-fg'}{g^2}$ |
| Composizione | $\frac{d}{dt}f(g(t))=f'(g(t))g'(t)$ |
| Esponenziale | $\frac{d}{dt}\exp(t)=\exp(t)$ |
| Logaritmo naturale, $t>0$ | $\frac{d}{dt}\ln t=\frac1t$ |
| Seno / coseno | $\frac{d}{dt}\sin t=\cos t$, $\frac{d}{dt}\cos t=-\sin t$ |

![Pendenza della posizione e area sotto la velocità](../../../assets/figures/calculus_slope_area.svg)

<a id="section-3"></a>
## 3. Derivata prima e seconda: un asse in movimento

Un carrello parte da 2 mm con velocità iniziale 3 mm/s e accelerazione costante 4 mm/s². La posizione è:

$$
x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2.
$$

**Derivata prima**: velocità. La costante sparisce; il termine lineare dà 3 mm/s; quello quadratico diventa lineare nel tempo.

$$
v(t)=\frac{dx}{dt}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t.
$$

**Derivata seconda**: accelerazione. Deriviamo ancora la velocità. A 2 s: posizione 16 mm, velocità 11 mm/s, accelerazione 4 mm/s².

$$
a(t)=\frac{d^2x}{dt^2}=\frac{dv}{dt}=4\ \mathrm{mm/s^2}.
$$

La derivata seconda ha unità lunghezza/tempo², non è **il quadrato** della derivata prima.

<a id="section-4"></a>
## 4. Regola della catena: energia di rotazione

Un volano in rotazione immagazzina energia cinetica. Quando $\omega$ dipende dal tempo, anche $E$ varia tramite $\omega$: è la **regola della catena (chain rule)**.

$$
E(\omega)=\frac12J\omega^2,\quad \omega=\omega(t),
$$
$$
\frac{dE}{dt}=\frac{dE}{d\omega}\frac{d\omega}{dt}=J\omega\alpha=M\omega=P.
$$

Con $J=0.01\ \mathrm{kg\cdot m^2}$, $\omega=10\ \mathrm{rad/s}$, $\alpha=2\ \mathrm{rad/s^2}$, la coppia $J\alpha=0.02\ \mathrm{N\cdot m}$ e la potenza meccanica è $0.2\ \mathrm{W}$. Ecco $P=M\omega$.

<a id="section-5"></a>
## 5. Esponenziali e logaritmi: tempo di risposta

In un modello semplice del primo ordine la velocità si avvicina al valore finale secondo una legge esponenziale. $\tau$ è la **costante di tempo (time constant)** in secondi.

$$
\omega(t)=\omega_\infty\bigl(1-\exp(-t/\tau)\bigr),\quad t\ge0,\ \tau>0.
$$

Questa forma presuppone una **velocità angolare iniziale nulla**, $\omega(0)=0$, e un valore finale costante $\omega_\infty$. Se la velocità iniziale è $\omega_0\ne0$, la risposta generale dello stesso sistema del primo ordine è:

$$
\omega(t)=\omega_\infty+(\omega_0-\omega_\infty)\exp(-t/\tau).
$$

**Esempio con velocità iniziale non nulla:** siano $\omega_0=200\ \mathrm{rpm}$, $\omega_\infty=1000\ \mathrm{rpm}$ e $\tau=0.5\ \mathrm{s}$. Dopo una costante di tempo ($t=0.5\ \mathrm{s}$):

$$
\omega(\tau)=1000+(200-1000)\exp(-1)\approx705.7\ \mathrm{rpm}.
$$

La risposta ha completato il **63.2 % della variazione di 800 rpm**, non il 63.2 % del valore finale di 1000 rpm. Per $t=0$ il risultato è 200 rpm; con il passare del tempo tende a 1000 rpm. È un esempio matematico, non un comando motore.

L’esponenziale indica la frazione di errore residua. Per scoprire **quando** rimane una certa frazione, usiamo il **logaritmo naturale (natural logarithm)** $\ln$, inverso di $\exp$. L’argomento $0.1$ è adimensionale.

$$
\exp(-t/\tau)=0.1
\quad\Longrightarrow\quad
-\frac{t}{\tau}=\ln(0.1)
\quad\Longrightarrow\quad
t=-\tau\ln(0.1)=\tau\ln(10)\approx2.303\tau.
$$

Il 90 % di variazione lascia il 10 % dell’errore iniziale. Con $\tau=0.5\ \mathrm{s}$ il modello ideale indica circa 1.151 s. Il sistema reale può avere limiti e ritardi.

La derivata di $\ln z$ è $1/z$ per $z>0$; se $z=z(t)$ si moltiplica per $dz/dt$. Il logaritmo richiede un argomento adimensionale.

$$
\ln(1)=0,\quad \ln(\mathrm{e})=1,\quad \ln(\mathrm{e}^{z})=z,\quad \frac{d}{dz}\ln z=\frac1z\ (z>0).
$$

<a id="section-6"></a>
## 6. Integrali: spostamento e lavoro meccanico

L’**integrale indefinito (indefinite integral)** fornisce primitive (antiderivatives) con una costante $C$. L’**integrale definito (definite integral)** accumula la variazione su un intervallo.

$$
\int 4t\ \mathrm{d}t=2t^2+C,\qquad \int t^n\ \mathrm{d}t=\frac{t^{n+1}}{n+1}+C\ (n\ne-1).
$$

**Spostamento.** Da $x_0=2\ \mathrm{mm}$ la velocità è $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$. Spostamento tra 0 e 2 s:

$$
\Delta x=\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
$$
$$
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}=6\ \mathrm{mm}+8\ \mathrm{mm}=14\ \mathrm{mm}.
$$

Lo spostamento è 14 mm; con la posizione iniziale $x(2)=16\ \mathrm{mm}$. La velocità negativa riduce lo spostamento con segno, non la distanza percorsa.

**Lavoro della molla.** Una molla ideale lineare con $k=200\ \mathrm{N/m}$ si allunga da 0 a 0.01 m. La forza aumenta durante il moto; integriamo i contributi di lavoro:

$$
F(x)=kx,\qquad W=\int_0^{0.01\ \mathrm{m}}kx\ \mathrm{d}x
=\left[\frac{kx^2}{2}\right]_0^{0.01\ \mathrm{m}}
=\frac{200\ \mathrm{N/m}}2(0.01\ \mathrm{m})^2=0.01\ \mathrm{J}.
$$

Il lavoro è 0.01 J. Usare la forza finale $F=2\ \mathrm{N}$ per tutto il percorso darebbe erroneamente 0.02 J, perché la forza non è costante.

<a id="section-7"></a>
## 7. Esempio aggiuntivo: sfera in espansione

**Esempio facoltativo della regola della catena.** Il volume della sfera dipende dal raggio, a sua volta dipendente dal tempo: la stessa struttura di energia e velocità angolare del volano.

$$
V(r)=\frac43\pi r^3,\qquad \frac{dV}{dt}=\frac{dV}{dr}\frac{dr}{dt}=4\pi r^2\frac{dr}{dt}.
$$

Con $r=10\ \mathrm{mm}$ e $dr/dt=1\ \mathrm{mm/s}$, $400\pi\approx1256.64\ \mathrm{mm^3/s}$. Per $r(t)=10\ \mathrm{mm}+(1\ \mathrm{mm/s^2})t^2$, a 2 s: $r=14\ \mathrm{mm}$, $dr/dt=4\ \mathrm{mm/s}$, e $3136\pi\approx9852.03\ \mathrm{mm^3/s}$.

<a id="section-8"></a>
## 8. Unità, verifiche ed esercizi

**Controlli:** prima derivata di posizione in m/s, seconda in m/s²; integrale forza-distanza in N·m = J; costante $C$ nell’integrale indefinito; derivata locale contro integrale accumulato; differenziale $\mathrm{d}t$ diverso dal passo finito `dt` del programma.

**Esercizi:** (1) Con $x(t)=5\ \mathrm{mm}+(2\ \mathrm{mm/s})t+(1\ \mathrm{mm/s^2})t^2$, velocità e accelerazione a 3 s. (2) Con $\tau=1\ \mathrm{s}$, quando si raggiunge il 90 %? (3) Spostamento a 4 mm/s per 2 s. **Risposte:** 8 mm/s e 2 mm/s²; circa 2.303 s; 8 mm.

**Soluzioni svolte:**

1. $v(t)=\frac{dx}{dt}=2\ \mathrm{mm/s}+2(1\ \mathrm{mm/s^2})t$; $v(3\ \mathrm{s})=2+2\cdot3=8\ \mathrm{mm/s}$. $a(t)=\frac{dv}{dt}=2\ \mathrm{mm/s^2}$.
2. $f(t)=1-\exp(-t/\tau)=0.9$; $\exp(-t/\tau)=0.1$; $t=-\tau\ln(0.1)=\tau\ln(10)$. $\tau=1\ \mathrm{s}$; $t\approx2.303\ \mathrm{s}$.
3. $\Delta x=\int_0^{2\ \mathrm{s}}(4\ \mathrm{mm/s})\ \mathrm{d}t=(4\ \mathrm{mm/s})(2\ \mathrm{s})=8\ \mathrm{mm}$.


[Integral reference](../INTEGRAL_TABLE.md) · [Trigonometry](../TRIGONOMETRY.md) · [Next: motion](01-motion-calculus.md) · [Python exercises](../exercises/README.md)
