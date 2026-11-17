# 1. Movimiento, derivadas e integrales


**Leer esta página en:** [en](../../en/notes/01-motion-calculus.md) · [fr](../../fr/notes/01-motion-calculus.md) · [de](../../de/notes/01-motion-calculus.md) · [it](../../it/notes/01-motion-calculus.md) · [es](01-motion-calculus.md) · [pt](../../pt/notes/01-motion-calculus.md) · [zh](../../zh/notes/01-motion-calculus.md) · [ja](../../ja/notes/01-motion-calculus.md) · [nb](../../nb/notes/01-motion-calculus.md) · [ru](../../ru/notes/01-motion-calculus.md) · [ko](../../ko/notes/01-motion-calculus.md) · [fi](../../fi/notes/01-motion-calculus.md) · [pl](../../pl/notes/01-motion-calculus.md)

**Unidades empleadas aquí (definidas antes de los ejemplos):** `s` — segundo; `mm` — milímetro = 0.001 m; `mm/s` — milímetro / segundo — velocidad lineal; `mm/s²` — milímetro / segundo² — aceleración; `%` — por ciento (una centésima parte). [Glosario de unidades](../UNITS.md).

**Fundamentos:** [0. Fundamentos de derivadas, diferenciales e integrales](00-calculus-foundations.md) · [Tabla de integrales](../INTEGRAL_TABLE.md)

[README](../README.md) · [Formulario de consulta rápida](../CHEATSHEET.md) · [Ejercicios de Python](../exercises/README.md) · [Dinámica de primer orden y rotación](02-first-order-dynamics.md)

> **Advertencia:** Este material didáctico elaborado con ayuda de IA puede contener errores, traducciones inexactas o supuestos incorrectos. Su uso es bajo responsabilidad propia. Verifica los cálculos de manera independiente y no emplees los ejemplos para controlar maquinaria real.

## Repaso rápido

La distancia recorrida es la longitud total del trayecto; el desplazamiento es la posición final menos la inicial. La rapidez (speed) no es negativa; la velocidad vectorial (velocity) incluye dirección. Derivar la posición respecto al tiempo proporciona la velocidad instantánea e integrar la velocidad con signo proporciona el desplazamiento.

**Términos ingleses:**

- distancia recorrida (distance traveled)
- desplazamiento (displacement)
- rapidez (speed)
- velocidad vectorial (velocity)
- derivada (derivative)
- integral (integral)
- integración numérica (numerical integration)
- método de Euler explícito (explicit Euler method)

## En esta página

- [1. Ejemplo de movimiento](#section-1)
- [2. Derivada y velocidad instantánea](#section-2)
- [3. Integral y desplazamiento](#section-3)
- [4. Integración numérica](#section-4)
- [5. Pruébalo](#section-5)
- [6. Detalles adicionales (opcional)](#section-6)
  - [Por qué la derivada de 2t² es 4t](#power-rule-derivation)
  - [De dónde salen los desplazamientos de la tabla](#motion-values-derivation)

[Unidades SI y punto decimal](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Ejemplo de movimiento

Para las unidades, demostraciones y límites numéricos, consulta los [Detalles adicionales](#section-6).

Un eje virtual avanza a $+3\ \mathrm{mm/s}$ durante dos segundos y retrocede a $-3\ \mathrm{mm/s}$ otros dos. El desplazamiento es $+6-6=0\ \mathrm{mm}$, pero la distancia recorrida es $12\ \mathrm{mm}$. En un movimiento circular, el vector velocidad cambia de dirección aunque la rapidez sea constante.

$$
\overline{v}=\frac{x(t_2)-x(t_1)}{t_2-t_1}.
$$

$$
\text{rapidez media}=\frac{\text{distancia total recorrida}}{t_2-t_1}.
$$

Durante **los cuatro segundos completos**, la velocidad media con signo y la rapidez media dan **resultados distintos**. El eje regresa al punto inicial tras recorrer 12 mm:

$$
\overline{v}_x=\frac{0\ \mathrm{mm}}{4\ \mathrm{s}}=0\ \mathrm{mm/s}
$$

$$
\overline{\lvert v\rvert}=\frac{12\ \mathrm{mm}}{4\ \mathrm{s}}=3\ \mathrm{mm/s}
$$

Por tanto, la rapidez media **no equivale necesariamente al módulo de la velocidad media**. En una vuelta completa a una circunferencia, la velocidad media vectorial es cero, pero la distancia recorrida y la rapidez media son positivas.

<a id="section-2"></a>

## 2. Derivada y velocidad instantánea

Con $x(t)=2t^2\ \mathrm{mm}$ y $t$ en segundos, $v(t)=4t\ \mathrm{mm/s}$. **¿De dónde sale el 4?** La regla de la potencia dice $d(t^2)/dt=2t$; por eso $2t^2$ produce $2\cdot2t=4t$. [Demostración y unidades](#power-rule-derivation). En $t=1\ \mathrm{s}$, la velocidad instantánea es $4\ \mathrm{mm/s}$. La diferencia finita hacia delante da $6$, $4.2$ y $4.02\ \mathrm{mm/s}$ con $dt=1$, $0.1$ y $0.01\ \mathrm{s}$.

$$
v(t)=\frac{dx}{dt},\qquad v(t)\approx\frac{x(t+dt)-x(t)}{dt}.
$$

**Por qué un paso demasiado pequeño puede fallar:** en $t=1\ \mathrm{s}$, la derivada exacta de $x(t)=2t^2$ es $4\ \mathrm{mm/s}$. Si $dt=1e-17\ \mathrm{s}$, el tipo `float` de Python redondea `t + dt` al mismo `t`: las dos posiciones calculadas coinciden y su diferencia sugeriría erróneamente velocidad cero. En escalas más pequeñas, ambas posiciones también pueden redondearse a cero aunque la derivada no sea cero. El ejemplo [`forward_derivative`](../../../exercises/01_motion_and_integral.py) ahora lanza `ValueError` en estos casos en vez de un cero falso. Sigue calculando una diferencia finita; hay que elegir un paso representable y no reducirlo indefinidamente.

<a id="section-3"></a>

## 3. Integral y desplazamiento

La integral de la velocidad con signo puede ser negativa o nula; la integral de su valor absoluto da una distancia no negativa. Para $v(t)=2t\ \mathrm{mm/s}$ entre $0$ y $2\ \mathrm{s}$, el desplazamiento exacto es $4\ \mathrm{mm}$.

$$
\Delta x=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t,\qquad
s=\int_{t_1}^{t_2}|v(t)|\ \mathrm{d}t.
$$

Geométricamente, la primera integral es el área con signo bajo la curva velocidad–tiempo. **Este es un ejemplo distinto del de la sección 2.** Allí la posición $x(t)=2t^2$ tiene como derivada $v(t)=4t$. Para explicar la integración aquí se elige deliberadamente otra velocidad: $v(t)=2t$. Su posición correspondiente es $x(t)=t^2+C$ (con unidades coherentes). No se deben confundir ambas leyes de movimiento.

<a id="section-4"></a>

## 4. Integración numérica

Desplazamiento exacto y aproximación de Euler por el extremo izquierdo (datos sintéticos).

![Desplazamiento exacto y aproximación de Euler por el extremo izquierdo (datos sintéticos)](../../../assets/figures/euler_vs_exact.svg)

El método de Euler explícito utiliza la velocidad **al inicio** de cada intervalo, no la media exacta. Para esta velocidad creciente, subestima el desplazamiento: con $dt=0.5$, $0.1$ y $0.01\ \mathrm{s}$ se obtienen $3$, $3.8$ y $3.98\ \mathrm{mm}$ (exacto: $4\ \mathrm{mm}$). La regla trapezoidal es exacta en este ejemplo lineal.

$$
x_{n+1}=x_n+v(t_n)\ dt.
$$

| `dt` (s) | Euler (mm) |
| ---: | ---: |
| 0.5 | 3.000 |
| 0.1 | 3.800 |
| 0.01 | 3.980 |
| Exacto | 4.000 |


[Cálculo de 3, 3.8 y 3.98.](#motion-values-derivation)

<a id="section-5"></a>

## 5. Pruébalo

Ejecuta el programa de movimiento y reduce $dt$. ¿Por qué un trayecto de ida y vuelta puede tener desplazamiento cero y distancia recorrida positiva?

[01_motion_and_integral.py](../../../exercises/01_motion_and_integral.py)

<a id="section-6"></a>

## 6. Detalles adicionales (opcional)

### Unidades y coeficientes

Si $t$ se expresa en segundos, escribir $x(t)=2t^2$ mm es una abreviatura: el coeficiente tiene unidades $2\ \mathrm{mm/s^2}$. La derivada $v(t)=4t$ tiene unidades de mm/s. Conviene comprobar todas las dimensiones.

### Límites de la aproximación

Una diferencia finita (finite difference) estima la derivada sobre un intervalo no nulo. Reducir el paso suele disminuir el error de discretización, pero un paso demasiado pequeño puede amplificar el redondeo o el ruido. Euler utiliza el valor al comienzo del paso.

### Movimiento en varias dimensiones

Para el vector de posición $\mathbf r(t)$, $\mathbf v=d\mathbf r/dt$; la rapidez es $\|\mathbf v\|$ y la distancia total $s=\int\|\mathbf v(t)\|dt$.


<a id="power-rule-derivation"></a>

### Por qué la derivada de $2t^2$ es $4t$



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

### De dónde salen los desplazamientos de la tabla

$$
a=2\ \mathrm{mm/s^2},\qquad v(t)=at,\qquad 0\le t\le2\ \mathrm{s}.
$$

$$
\Delta x=\int_{0}^{2\ \mathrm{s}}at\ \mathrm{d}t
=\left[\frac{at^2}{2}\right]_{0}^{2\ \mathrm{s}}
=4\ \mathrm{mm}.
$$



El símbolo $\sum$ (sigma mayúscula griega, **sumatorio** / summation) indica que se suman varios términos. En $\sum_{n=0}^{N-1}(2nh)h$, el índice $n$ recorre $0; 1; \ldots; N-1$: hay $N$ sumandos. Es equivalente a un bucle `for` de Python que acumula valores. Por ejemplo, $\sum_{n=1}^{3}n=1+2+3=6$. [← Símbolos explicados](../SYMBOLS.md#summation).

$$
h=\frac{dt}{1\ \mathrm{s}},\qquad N=\frac{2}{h}.
$$

$$
x_{\mathrm{Euler}}(2\ \mathrm{s})
=\left[\sum_{n=0}^{N-1}(2nh)h\right]\ \mathrm{mm}
=\left[h^2N(N-1)\right]\ \mathrm{mm}
=(4-2h)\ \mathrm{mm}.
$$

Aquí `h` es el valor numérico del paso `dt` en segundos (`dt = 0.5 s` corresponde a `h = 0.5`); `N` es el número de pasos. El resultado es una **distancia en milímetros**.



Con $dt=0.5$, $0.1$ y $0.01$ segundos se obtienen $3$, $3.8$ y $3.98$ milímetros. Se supone que $2/dt$ es entero.
