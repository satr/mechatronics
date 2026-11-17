# 2. Dinámica de primer orden y rotación


**Leer esta página en:** [en](../../en/notes/02-first-order-dynamics.md) · [fr](../../fr/notes/02-first-order-dynamics.md) · [de](../../de/notes/02-first-order-dynamics.md) · [it](../../it/notes/02-first-order-dynamics.md) · [es](02-first-order-dynamics.md) · [pt](../../pt/notes/02-first-order-dynamics.md) · [zh](../../zh/notes/02-first-order-dynamics.md) · [ja](../../ja/notes/02-first-order-dynamics.md) · [nb](../../nb/notes/02-first-order-dynamics.md) · [ru](../../ru/notes/02-first-order-dynamics.md) · [ko](../../ko/notes/02-first-order-dynamics.md) · [fi](../../fi/notes/02-first-order-dynamics.md) · [pl](../../pl/notes/02-first-order-dynamics.md)

**Unidades empleadas aquí (definidas antes de los ejemplos):** `s` — segundo; `mm/s` — milímetro / segundo — velocidad lineal; `kg` — kilogramo; `m` — metro; `rad/s` — radián / segundo — velocidad angular; `N` — newton; `N·m` — newton · metro — par de torsión; `J` — julio (joule); `rpm` — revolución por minuto; `kg·m²` — kilogramo · metro² — momento de inercia; `N·m·s/rad` — newton · metro · segundo / radián — ganancia por velocidad; `%` — por ciento (una centésima parte); `rad` — radián. [Glosario de unidades](../UNITS.md).

**Fundamentos:** [0. Fundamentos de derivadas, diferenciales e integrales](00-calculus-foundations.md) · [Tabla de integrales](../INTEGRAL_TABLE.md)

[README](../README.md) · [Formulario de consulta rápida](../CHEATSHEET.md) · [Ejercicios de Python](../exercises/README.md) · [Movimiento, derivadas e integrales](01-motion-calculus.md)

> **Advertencia:** Este material didáctico elaborado con ayuda de IA puede contener errores, traducciones inexactas o supuestos incorrectos. Su uso es bajo responsabilidad propia. Verifica los cálculos de manera independiente y no emplees los ejemplos para controlar maquinaria real.

> **Supuestos del modelo de motor:** Se supone un control proporcional ideal del par, sin carga, fricción, retardos, límites de tensión, saturación ni dinámicas de orden superior. No es una descripción universal de los motores.

## Repaso rápido

La constante de tiempo $\tau$ caracteriza la rapidez con la que un sistema de primer orden se acerca a su nuevo equilibrio. El paso de simulación $dt$ controla la precisión numérica, no la física. En el modelo ideal $\tau=\frac{J}{K}$; igual respuesta no implica igual par ni igual energía.

**Términos ingleses:**

- sistema de primer orden (first-order system)
- constante de tiempo (time constant)
- paso temporal (time step)
- momento de inercia (moment of inertia)
- par (torque)
- ganancia del controlador (controller gain)
- aceleración angular (angular acceleration)
- identificación del sistema (system identification)
- energía cinética rotacional (rotational kinetic energy)

## En esta página

- [1. Respuesta de primer orden](#section-1)
- [2. Par e inercia](#section-2)
- [3. Paso numérico y constante de tiempo](#section-3)
- [4. Estimar la constante de tiempo con mediciones](#section-4)
- [5. Energía de rotación](#section-5)
- [6. Pruébalo](#section-6)
- [7. Detalles adicionales (opcional)](#section-7)
  - [De dónde salen 63.2 %, 86.5 % y 95.0 %](#time-constant-derivation)
  - [De dónde salen los resultados de Euler](#euler-values-derivation)

[Unidades SI y punto decimal](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Respuesta de primer orden

Para las unidades, demostraciones y límites numéricos, consulta los [Detalles adicionales](#section-7).

Con velocidad objetivo constante $u$, velocidad real $v$ y $\tau>0$, el modelo completa aproximadamente el $63.2\ \%$ del cambio después de $\tau$, el $86.5\ \%$ después de $2\tau$ y el $95.0\ \%$ después de $3\tau$. No significa alcanzar exactamente el objetivo en un tiempo $\tau$.

**Notación:** $\varepsilon(t)=u-v(t)$ es el error de velocidad (speed error; épsilon griega). La función exponencial natural (exponential function) es $\exp(z)=\mathrm{e}^{z}$, donde $\mathrm{e}\approx2.71828$ es el número de Euler (Euler’s number), **no** el error. [Derivación y cálculo del 63.2 %](#time-constant-derivation).

$$
\frac{dv}{dt}=\frac{u-v}{\tau}.
$$

$$
v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right).
$$

| Tiempo | Fracción del cambio |
| --- | ---: |
| $\tau$ | 63.2 % |
| $2\tau$ | 86.5 % |
| $3\tau$ | 95.0 % |

[¿Por qué exactamente esos porcentajes? Consulta el cálculo.](#time-constant-derivation)

![Respuesta normalizada de primer orden: cada constante de tiempo elimina cerca del 63.2 % del error restante.](../../../assets/figures/first_order_response.svg)

<a id="section-2"></a>

## 2. Par e inercia

El controlador calcula una orden eléctrica; el motor produce físicamente el par $M$. En el modelo $J$ es el momento de inercia, $\omega$ la velocidad angular y $K$ el coeficiente de par proporcional al error de velocidad. Duplicar $J$ con $K$ fijo duplica $\tau$. Duplicar ambos conserva $\tau$ y duplica el par para el mismo error. El modelo omite fricción, carga, retardos y límites de corriente.

$$
J\frac{d\omega}{dt}=M,\qquad M=K(u-\omega).
$$

$$
\frac{d\omega}{dt}=\frac{K}{J}(u-\omega),\qquad \tau=\frac{J}{K}.
$$

**Unidades:** $J$: $\mathrm{kg}\cdot\mathrm{m}^2$; $\omega,u$: $\mathrm{rad/s}$; $M$: $\mathrm{N}\cdot\mathrm{m}$; $K$: $\mathrm{N}\cdot\mathrm{m}\cdot\mathrm{s}/\mathrm{rad}$; $\tau$: s.

Lazo de realimentación simbólico del modelo ideal. El controlador envía la orden; el motor produce físicamente el par.

![Lazo de realimentación simbólico del modelo ideal. El controlador envía la orden; el motor produce físicamente el par](../../../assets/figures/control_loop.svg)

<a id="section-3"></a>

## 3. Paso numérico y constante de tiempo

Euler actualiza el estado mediante intervalos $dt$. Reducir $dt$ no acelera el motor modelado, solo cambia la aproximación. Con $u=10\ \mathrm{mm/s}$, $\tau=1\ \mathrm{s}$ y un segundo de duración, Euler da $6.513$ para $dt=0.1$ o $6.340\ \mathrm{mm/s}$ para $dt=0.01$; el valor exacto es $6.321\ \mathrm{mm/s}$.

$$
v_{n+1}=v_n+\frac{u-v_n}{\tau}\ dt.
$$

| Método | $v(1\ \mathrm{s})$ (mm/s) |
| --- | ---: |
| Euler $dt=0.1\ \mathrm{s}$ | 6.513 |
| Euler $dt=0.01\ \mathrm{s}$ | 6.340 |
| Exacto | 6.321 |

[Cálculo paso a paso de estos valores.](#euler-values-derivation)

<a id="section-4"></a>

## 4. Estimar la constante de tiempo con mediciones

Si la consigna pasa de 0 a 1000 rpm, busca cuándo la velocidad medida alcanza aproximadamente 632 rpm. Si ocurre a los 2 segundos, el modelo de primer orden sugiere $\tau\approx2\ \mathrm{s}$. Con velocidad inicial distinta de cero, se usa el 63.2 % del **cambio total**, no el 63.2 % de la consigna. El ruido, los retardos y el sobreimpulso complican esta identificación del sistema (system identification).

**Qué devuelve realmente el código:** la función [`estimate_tau`](../../../exercises/02_first_order_response.py) necesita mediciones con tiempos **estrictamente crecientes**, contados desde el cambio de consigna. Devuelve el instante de la **primera muestra observada** que alcanza el umbral del 63.2 % de la variación, permitiendo la mitad de la resolución conocida del sensor por redondeo. Si el umbral se detecta por primera vez a los 2 s y la muestra anterior fue a 1 s, el cruce real pudo ocurrir **entre las muestras**. Por eso 2 s es una estimación limitada por el muestreo, no un ajuste exacto. Los tiempos repetidos o desordenados y las mediciones inválidas se rechazan incluso después del cruce; si nunca se alcanza, el resultado es `None`.

**La resolución del sensor importa:** el parámetro `resolution` de `estimate_tau` debe ser **menor que la magnitud del cambio total de velocidad**. Si la velocidad pasa de 0 a 10 rpm pero la pantalla solo cambia en incrementos de 10 rpm, no se puede estimar de forma fiable el cruce del umbral del 63.2 %. La función rechaza estos datos en lugar de informar un cruce artificial en la primera muestra. Incluso con resolución suficiente, la estimación está limitada por el muestreo.

<a id="section-5"></a>

## 5. Energía de rotación

El par neto satisface $M=J\alpha$. Para $J=2\ \mathrm{kg}\cdot\mathrm{m}^2$ y $\omega=10\ \mathrm{rad/s}$, la energía de rotación es $100\ \mathrm{J}$; duplicar $J$ da $200\ \mathrm{J}$. Duplicar $\omega$ cuadruplica la energía. La energía mecánica no equivale al consumo eléctrico total.

$$
M=J\alpha,\qquad \alpha=\frac{d\omega}{dt}.
$$

$$
E=\frac{1}{2}J\omega^2.
$$

<a id="section-6"></a>

## 6. Pruébalo

En un escalón ideal de 0 a 1000 rpm, alcanzar unas 632 rpm después de dos segundos indica $\tau\approx2\ \mathrm{s}$. El ruido y el muestreo pueden requerir una identificación más precisa. Compara Euler con la solución exacta en el programa.

[02_first_order_response.py](../../../exercises/02_first_order_response.py) · [03_rotation_energy.py](../../../exercises/03_rotation_energy.py) · [plot_models.py](../../../exercises/plot_models.py)


<a id="section-7"></a>

## 7. Detalles adicionales (opcional)


### Estabilidad de Euler

En cada paso **el error respecto de la consigna** se multiplica por $1-\frac{dt}{\tau}$. La convergencia requiere $0<dt<2\tau$; para $\tau<dt<2\tau$ el resultado numérico oscila alrededor de la consigna. No se trata de una oscilación física del motor.

### Límites del modelo

En general, $J\ \frac{d\omega}{dt}=M_{\text{motor}}-M_{\text{carga}}-M_{\text{fricción}}$. La expresión $\tau=\frac{J}{K}$ exige la hipótesis específica $M_{\text{neto}}=K(u-\omega)$. Carga, fricción, retardo y límites de corriente pueden invalidarla.

### Energía y potencia

Con $J$ constante, $\Delta E=\frac{1}{2} J(\omega_2^2-\omega_1^2)$ y la potencia mecánica instantánea (mechanical power) es $P=M\omega$. Esto no determina el consumo eléctrico.


<a id="time-constant-derivation"></a>

### De dónde salen 63.2 %, 86.5 % y 95.0 %

Los porcentajes y la exponencial proceden de **la misma ecuación**. Definimos el error de velocidad como $\varepsilon(t)=u-v(t)$ (no es el número de Euler). Si $u$ es constante, $\frac{d\varepsilon}{dt}=-\frac{dv}{dt}$:

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

La separación de variables divide entre $\varepsilon$, por lo que este paso supone un error inicial distinto de cero. Si $u=v_0$, el error permanece en cero y la ecuación diferencial original da directamente la solución constante $v(t)=u$.

$$
f(t)=\frac{v(t)-v_0}{u-v_0}=1-\exp\!\left(-\frac{t}{\tau}\right),\qquad (u\ne v_0).
$$

| $t$ | $f(t)$ |
| ---: | ---: |
| $\tau$ | $1-\exp(-1)=0.63212056\ldots\approx63.2\ \%$ |
| $2\tau$ | $1-\exp(-2)=0.86466472\ldots\approx86.5\ \%$ |
| $3\tau$ | $1-\exp(-3)=0.95021293\ldots\approx95.0\ \%$ |

Para un escalón de 0 a 1000 rpm, se obtienen aproximadamente 632, 865 y 950 rpm después de una, dos y tres constantes de tiempo. El modelo ideal se aproxima asintóticamente al objetivo.

<a id="euler-values-derivation"></a>

### De dónde salen los resultados de Euler

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
