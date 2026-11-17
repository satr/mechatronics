# Formulario rapido

**Leggi questa pagina in:** [en](../en/CHEATSHEET.md) · [fr](../fr/CHEATSHEET.md) · [de](../de/CHEATSHEET.md) · [it](CHEATSHEET.md) · [es](../es/CHEATSHEET.md) · [pt](../pt/CHEATSHEET.md) · [zh](../zh/CHEATSHEET.md) · [ja](../ja/CHEATSHEET.md) · [nb](../nb/CHEATSHEET.md) · [ru](../ru/CHEATSHEET.md) · [ko](../ko/CHEATSHEET.md) · [fi](../fi/CHEATSHEET.md) · [pl](../pl/CHEATSHEET.md)

**Unità usate qui (spiegate prima degli esempi):** `s` — secondo; `m` — metro; `m/s` — metro / secondo — velocità lineare; `rad/s` — radiante / secondo — velocità angolare; `kg·m²` — chilogrammo · metro² — momento d'inerzia; `N·m` — newton · metro — momento torcente; `N·m·s/rad` — newton · metro · secondo / radiante — guadagno per unità di velocità; `J` — joule; `mm` — millimetro = 0.001 m; `mm/s` — millimetro / secondo — velocità lineare; `%` — percento (un centesimo). [Glossario delle unità](UNITS.md).

[Indice](README.md) · [Moto, derivate e integrali](notes/01-motion-calculus.md) · [Dinamica del primo ordine e rotazione](notes/02-first-order-dynamics.md) · [Esercizi Python](exercises/README.md)

> **Avvertenza:** Questi materiali didattici, elaborati anche con l'IA, possono contenere errori, traduzioni imprecise e ipotesi non valide. L'uso è a proprio rischio. Verificare i calcoli in modo indipendente; non utilizzare gli esempi per controllare macchine reali.

| In breve | Formulario rapido |
| --- | --- |
| Spostamento | $\Delta x=x_2-x_1$ |
| Spazio percorso | $s=\int_{t_1}^{t_2}\lvert v(t)\rvert\ \mathrm{d}t\ge 0$ |
| Velocità vettoriale media | $\overline{v}=\frac{\Delta x}{\Delta t}$ |
| Rapidità media | $\frac{s}{\Delta t}$ |
| Velocità istantanea | $v(t)=\frac{dx}{dt}$ |
| Metodo di Eulero | $x_{n+1}=x_n+v_n\ dt$ |
| Dinamica del primo ordine | $\frac{dv}{dt}=\frac{u-v}{\tau}$ |
| Errore di velocità | $\varepsilon(t)=u-v(t)$ |
| Costante di tempo | $t=\tau$: $1-\exp(-1)\approx63.2\ \%$ |
| Coppia risultante | $M=J\alpha$ |
| Momento d’inerzia e guadagno | $\tau=\frac{J}{K}$ (Solo nel modello ideale di coppia) |
| Energia cinetica di rotazione | $E=\frac{1}{2}J\omega^2$ |

**Notazione:** $\varepsilon$ è l’errore di velocità (speed error); $\mathrm{e}\approx2.71828$ è il numero di Eulero (Euler’s number); $\exp(z)=\mathrm{e}^{z}$.

**Unità (SI):**

| Simbolo | Grandezza | Unità SI |
| --- | --- | --- |
| `t, dt, τ` | Tempo | s (second) |
| `x` | Posizione | m (meter) |
| `v` | Velocità | m/s (meter per second) |
| `ω` | Velocità angolare | rad/s (radian per second) |
| `J` | Momento d’inerzia | kg·m² (kilogram square meter) |
| `M` | Coppia | N·m (newton meter) |
| `K` | Guadagno di coppia | N·m·s/rad |
| `E` | Energia | J (joule) |

Il punto `·` indica la moltiplicazione. La consigna $u$ è una velocità lineare o angolare secondo il modello.

## Avvertenze

Non confondere rapidità e velocità vettoriale, spazio percorso e spostamento, oppure $dt$ e $\tau$. La relazione $\tau=\frac{J}{K}$ vale solo nell'ipotesi di coppia proporzionale; l'energia meccanica non è l'energia elettrica assorbita.

**Termini inglesi:**

- distanza percorsa (distance traveled)
- spostamento (displacement)
- rapidità (speed)
- velocità vettoriale (velocity)
- derivata (derivative)
- integrale (integral)
- integrazione numerica (numerical integration)
- metodo di Eulero esplicito (explicit Euler method)

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

Per approfondire: [derivate](notes/01-motion-calculus.md#section-6) e [limiti del modello](notes/02-first-order-dynamics.md#section-7).


[Perché proprio queste percentuali? Vedi il calcolo.](notes/02-first-order-dynamics.md#time-constant-derivation)

[Calcolo di 3; 3.8 e 3.98.](notes/01-motion-calculus.md#motion-values-derivation)


## Simboli e notazione

**Σ / ∑ (sommatoria / summation)** somma più termini: $\sum_{n=1}^{3}n=1+2+3=6$. [Altri simboli](SYMBOLS.md).


## Tabella degli integrali

[0. Fondamenti di derivate, differenziali e integrali](notes/00-calculus-foundations.md) · [Tabella degli integrali](INTEGRAL_TABLE.md)


## Retroazione: PID e coppia di sostegno

| $\varepsilon=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}}$ | $u_P=K_p\varepsilon$, $u_I=K_i\int\varepsilon\ \mathrm{d}t$ |
| --- | --- |
| $M_{\mathrm{motor}}=K_t I$ | $\lvert M_g\rvert=mgL\lvert\cos\theta\rvert$ |

[Retroazione: PID e coppia di sostegno](notes/03-feedback-control.md) · [Tabella trigonometrica ed esempi meccanici](TRIGONOMETRY.md)

<a id="joint-velocity"></a>
## Rotazione, velocità e jacobiano

Velocità angolari in rad/s; velocità lineari in mm/s per lunghezze in mm.

$$
v_x=-L\sin Q\cdot\dot Q,\qquad v_y=L\cos Q\cdot\dot Q
$$

$$
\det J=L_1L_2\sin Q_2
$$

[Rotazione, velocità e jacobiano](notes/05-velocity-jacobian.md)
