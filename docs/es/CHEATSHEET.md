# Formulario de consulta rápida

**Leer esta página en:** [en](../en/CHEATSHEET.md) · [fr](../fr/CHEATSHEET.md) · [de](../de/CHEATSHEET.md) · [it](../it/CHEATSHEET.md) · [es](CHEATSHEET.md) · [pt](../pt/CHEATSHEET.md) · [zh](../zh/CHEATSHEET.md) · [ja](../ja/CHEATSHEET.md) · [nb](../nb/CHEATSHEET.md) · [ru](../ru/CHEATSHEET.md) · [ko](../ko/CHEATSHEET.md) · [fi](../fi/CHEATSHEET.md) · [pl](../pl/CHEATSHEET.md)

**Unidades empleadas aquí (definidas antes de los ejemplos):** `s` — segundo; `m` — metro; `m/s` — metro / segundo — velocidad lineal; `rad/s` — radián / segundo — velocidad angular; `kg·m²` — kilogramo · metro² — momento de inercia; `N·m` — newton · metro — par de torsión; `N·m·s/rad` — newton · metro · segundo / radián — ganancia por velocidad; `J` — julio (joule); `mm` — milímetro = 0.001 m; `mm/s` — milímetro / segundo — velocidad lineal; `%` — por ciento (una centésima parte). [Glosario de unidades](UNITS.md).

[Contenido](README.md) · [Movimiento, derivadas e integrales](notes/01-motion-calculus.md) · [Dinámica de primer orden y rotación](notes/02-first-order-dynamics.md) · [Ejercicios de Python](exercises/README.md)

> **Advertencia:** Este material didáctico elaborado con ayuda de IA puede contener errores, traducciones inexactas o supuestos incorrectos. Su uso es bajo responsabilidad propia. Verifica los cálculos de manera independiente y no emplees los ejemplos para controlar maquinaria real.

| Repaso rápido | Formulario de consulta rápida |
| --- | --- |
| Desplazamiento | $\Delta x=x_2-x_1$ |
| Distancia recorrida | $s=\int_{t_1}^{t_2}\lvert v(t)\rvert\ \mathrm{d}t\ge 0$ |
| Velocidad vectorial media | $\overline{v}=\frac{\Delta x}{\Delta t}$ |
| Rapidez media | $\frac{s}{\Delta t}$ |
| Velocidad instantánea | $v(t)=\frac{dx}{dt}$ |
| Método de Euler | $x_{n+1}=x_n+v_n\ dt$ |
| Dinámica de primer orden | $\frac{dv}{dt}=\frac{u-v}{\tau}$ |
| Error de velocidad | $\varepsilon(t)=u-v(t)$ |
| Constante de tiempo | $t=\tau$: $1-\exp(-1)\approx63.2\ \%$ |
| Par neto | $M=J\alpha$ |
| Inercia y ganancia | $\tau=\frac{J}{K}$ (Solo para el modelo idealizado de par) |
| Energía cinética de rotación | $E=\frac{1}{2}J\omega^2$ |

**Notación:** $\varepsilon$ es el error de velocidad (speed error); $\mathrm{e}\approx2.71828$ es el número de Euler (Euler’s number); $\exp(z)=\mathrm{e}^{z}$.

**Unidades (SI):**

| Símbolo | Magnitud | Unidad SI |
| --- | --- | --- |
| `t, dt, τ` | Tiempo | s (second) |
| `x` | Posición | m (meter) |
| `v` | Velocidad | m/s (meter per second) |
| `ω` | Velocidad angular | rad/s (radian per second) |
| `J` | Momento de inercia | kg·m² (kilogram square meter) |
| `M` | Par | N·m (newton meter) |
| `K` | Ganancia de par | N·m·s/rad |
| `E` | Energía | J (joule) |

El punto `·` indica multiplicación. La consigna $u$ es velocidad lineal o angular según el modelo.

## Advertencias

No confundas rapidez con velocidad vectorial, distancia con desplazamiento, ni $dt$ con $\tau$. La identidad $\tau=\frac{J}{K}$ solo corresponde al modelo indicado. Energía mecánica no significa consumo eléctrico.

**Términos ingleses:**

- distancia recorrida (distance traveled)
- desplazamiento (displacement)
- rapidez (speed)
- velocidad vectorial (velocity)
- derivada (derivative)
- integral (integral)
- integración numérica (numerical integration)
- método de Euler explícito (explicit Euler method)

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

Para ampliar: [derivadas](notes/01-motion-calculus.md#section-6) y [límites del modelo](notes/02-first-order-dynamics.md#section-7).


[¿Por qué exactamente esos porcentajes? Consulta el cálculo.](notes/02-first-order-dynamics.md#time-constant-derivation)

[Cálculo de 3, 3.8 y 3.98.](notes/01-motion-calculus.md#motion-values-derivation)


## Símbolos y notación

**Σ / ∑ (sumatorio / summation)** suma varios términos: $\sum_{n=1}^{3}n=1+2+3=6$. [Otros símbolos](SYMBOLS.md).


## Tabla de integrales

[0. Fundamentos de derivadas, diferenciales e integrales](notes/00-calculus-foundations.md) · [Tabla de integrales](INTEGRAL_TABLE.md)


## Control realimentado: PID y par de sujeción

| $\varepsilon=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}}$ | $u_P=K_p\varepsilon$, $u_I=K_i\int\varepsilon\ \mathrm{d}t$ |
| --- | --- |
| $M_{\mathrm{motor}}=K_t I$ | $\lvert M_g\rvert=mgL\lvert\cos\theta\rvert$ |

[Control realimentado: PID y par de sujeción](notes/03-feedback-control.md) · [Tabla trigonométrica y ejemplos mecánicos](TRIGONOMETRY.md)

<a id="joint-velocity"></a>
## Rotación, velocidad y jacobiano

Las velocidades angulares se dan en rad/s y las lineales en mm/s para longitudes en mm.

$$
v_x=-L\sin Q\cdot\dot Q,\qquad v_y=L\cos Q\cdot\dot Q
$$

$$
\det J=L_1L_2\sin Q_2
$$

[Rotación, velocidad y jacobiano](notes/05-velocity-jacobian.md)
