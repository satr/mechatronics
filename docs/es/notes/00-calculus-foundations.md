# 0. Fundamentos de cálculo: derivadas, límites e integrales aplicados

**Idiomas:** [en](../../en/notes/00-calculus-foundations.md) · [fr](../../fr/notes/00-calculus-foundations.md) · [de](../../de/notes/00-calculus-foundations.md) · [it](../../it/notes/00-calculus-foundations.md) · [es](00-calculus-foundations.md) · [pt](../../pt/notes/00-calculus-foundations.md) · [zh](../../zh/notes/00-calculus-foundations.md) · [ja](../../ja/notes/00-calculus-foundations.md) · [nb](../../nb/notes/00-calculus-foundations.md) · [ru](../../ru/notes/00-calculus-foundations.md) · [ko](../../ko/notes/00-calculus-foundations.md) · [fi](../../fi/notes/00-calculus-foundations.md) · [pl](../../pl/notes/00-calculus-foundations.md)

La **exponencial natural** es $\exp(x)=\mathrm{e}^{x}$, donde el **número de Euler** es $\mathrm{e}\approx2.71828$. Describe crecimiento o decaimiento continuo; $\exp(0)=1$ y $\exp(-1)\approx0.3679$. El logaritmo natural $\ln$ es su inversa: $\ln(\exp(x))=x$. Véase la [guía de símbolos](../SYMBOLS.md).

**Unidades empleadas aquí (definidas antes de los ejemplos):** `s` — segundo; `mm` — milímetro = 0.001 m; `mm/s` — milímetro / segundo — velocidad lineal; `mm/s²` — milímetro / segundo² — aceleración; `kg·m²` — kilogramo · metro² — momento de inercia; `rad/s` — radián / segundo — velocidad angular; `rad/s²` — radián / segundo² — aceleración angular; `N·m` — newton · metro — par de torsión; `W` — vatio; `rpm` — revolución por minuto; `N/m` — newton / metro — rigidez; `mm³/s` — milímetro³ / segundo — caudal volumétrico; `%` — por ciento (una centésima parte); `m` — metro; `kg` — kilogramo; `N` — newton; `J` — julio (joule); `rad` — radián. [Glosario de unidades](../UNITS.md).

[README](../README.md) · [Integral table](../INTEGRAL_TABLE.md) · [Trigonometry table](../TRIGONOMETRY.md) · [Motion](01-motion-calculus.md) · [Dynamics](02-first-order-dynamics.md) · [Symbols](../SYMBOLS.md)

> **Modelo educativo:** Verifique modelos y unidades; no conecte este código a máquinas reales.

La **derivada (derivative)** indica la tasa de cambio instantánea; la **segunda derivada (second derivative)** describe cómo cambia dicha tasa. La **integral (integral)** acumula cambios. El **límite (limit)** define la tasa instantánea; el **logaritmo (logarithm)** permite despejar el tiempo de una respuesta exponencial.

Se usan estas herramientas en ejes de máquinas, servomotores, articulaciones robóticas, resortes y sensores. Primero identificamos el problema físico; después, la regla y sus unidades.

## Contenido

- [1. Del cambio medido al modelo matemático](#section-1)
- [2. Límites y primeras derivadas](#section-2)
- [3. Primera y segunda derivada: eje en movimiento](#section-3)
- [4. Regla de la cadena: energía de rotación](#section-4)
- [5. Exponenciales y logaritmos: tiempo de respuesta](#section-5)
- [6. Integrales: desplazamiento y trabajo mecánico](#section-6)
- [7. Ejemplo adicional: esfera que se expande](#section-7)
- [8. Unidades, comprobaciones y ejercicios](#section-8)

<a id="section-1"></a>
## 1. Del cambio medido al modelo matemático

| Pregunta física | Herramienta matemática |
| --- | --- |
| ¿A qué velocidad se mueve el eje **ahora**? | Primera derivada $dx/dt$ |
| ¿Cómo cambia la velocidad? | Segunda derivada $d^2x/dt^2$ |
| ¿Cuándo llega la respuesta al 90 %? | Logaritmo $\ln$ |
| ¿Cuánto se desplaza en 2 s? | Integral definida $\int v\ \mathrm{d}t$ |
| ¿Qué trabajo realiza una fuerza variable? | Integral $\int F\ \mathrm{d}x$ |

<a id="section-2"></a>
## 2. Límites y primeras derivadas

Una **diferencia finita (finite difference)** entre dos lecturas representa el cambio medio durante el intervalo. La derivada es el límite cuando dicho intervalo tiende a cero.

$$
v(t)=\frac{dx}{dt}=\lim_{h\to0}\frac{x(t+h)-x(t)}{h}.
$$

Para la posición $x(t)=a t^2$ con $a=2\ \mathrm{mm/s^2}$, desarrollamos el numerador antes de tomar el límite:

$$
\frac{x(t+h)-x(t)}h=\frac{a[(t+h)^2-t^2]}h=a(2t+h)\longrightarrow 2at.
$$

El factor $h$ se cancela **antes** del límite. En $t=1\ \mathrm{s}$ la velocidad instantánea es $4\ \mathrm{mm/s}$. No sustituimos directamente la forma indeterminada $0/0$.

**Reglas de derivación (differentiation rules)**: $c$ y $n$ son constantes; los ángulos trigonométricos se expresan en radianes.

| Regla | Fórmula |
| --- | --- |
| Constante | $\frac{d}{dt}c=0$ |
| Potencia | $\frac{d}{dt}t^n=n t^{n-1}$ |
| Coeficiente y suma | $(cf+g)'=cf'+g'$ |
| Producto | $(fg)'=f' g+fg'$ |
| Cociente, $g\ne0$ | $\left(\frac{f}{g}\right)'=\frac{f' g-fg'}{g^2}$ |
| Composición | $\frac{d}{dt}f(g(t))=f'(g(t))g'(t)$ |
| Exponencial | $\frac{d}{dt}\exp(t)=\exp(t)$ |
| Logaritmo natural, $t>0$ | $\frac{d}{dt}\ln t=\frac1t$ |
| Seno / coseno | $\frac{d}{dt}\sin t=\cos t$, $\frac{d}{dt}\cos t=-\sin t$ |

![Pendiente de posición y área bajo velocidad](../../../assets/figures/calculus_slope_area.svg)

<a id="section-3"></a>
## 3. Primera y segunda derivada: eje en movimiento

Un carro parte de 2 mm, con velocidad inicial 3 mm/s y aceleración constante 4 mm/s². Su posición es:

$$
x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2.
$$

**Primera derivada**: velocidad. La constante desaparece, el término en $t$ da 3 mm/s y el término cuadrático pasa a depender linealmente de $t$.

$$
v(t)=\frac{dx}{dt}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t.
$$

**Segunda derivada**: aceleración. Derivamos de nuevo. A los 2 s: posición 16 mm, velocidad 11 mm/s y aceleración 4 mm/s².

$$
a(t)=\frac{d^2x}{dt^2}=\frac{dv}{dt}=4\ \mathrm{mm/s^2}.
$$

La segunda derivada tiene unidades de longitud/tiempo²; **no** es el cuadrado de la primera.

<a id="section-4"></a>
## 4. Regla de la cadena: energía de rotación

Un volante giratorio almacena energía cinética. Si $\omega$ depende del tiempo, la energía $E$ cambia a través de ella: es la **regla de la cadena (chain rule)**.

$$
E(\omega)=\frac12J\omega^2,\quad \omega=\omega(t),
$$
$$
\frac{dE}{dt}=\frac{dE}{d\omega}\frac{d\omega}{dt}=J\omega\alpha=M\omega=P.
$$

Con $J=0.01\ \mathrm{kg\cdot m^2}$, $\omega=10\ \mathrm{rad/s}$ y $\alpha=2\ \mathrm{rad/s^2}$, el par $J\alpha$ es $0.02\ \mathrm{N\cdot m}$ y la potencia mecánica instantánea, $0.2\ \mathrm{W}$. Así obtenemos $P=M\omega$.

<a id="section-5"></a>
## 5. Exponenciales y logaritmos: tiempo de respuesta

En un modelo sencillo de primer orden la velocidad se aproxima exponencialmente a su valor final. $\tau$ es la **constante de tiempo (time constant)** en segundos.

$$
\omega(t)=\omega_\infty\bigl(1-\exp(-t/\tau)\bigr),\quad t\ge0,\ \tau>0.
$$

Esta fórmula supone una **velocidad angular inicial igual a cero**, $\omega(0)=0$, y un objetivo final constante $\omega_\infty$. Si la velocidad inicial es $\omega_0\ne0$, la respuesta general del mismo sistema de primer orden es:

$$
\omega(t)=\omega_\infty+(\omega_0-\omega_\infty)\exp(-t/\tau).
$$

**Ejemplo con velocidad inicial distinta de cero:** tomemos $\omega_0=200\ \mathrm{rpm}$, $\omega_\infty=1000\ \mathrm{rpm}$ y $\tau=0.5\ \mathrm{s}$. Después de una constante de tiempo ($t=0.5\ \mathrm{s}$):

$$
\omega(\tau)=1000+(200-1000)\exp(-1)\approx705.7\ \mathrm{rpm}.
$$

Se ha completado el **63.2 % del cambio de 800 rpm**, no el 63.2 % del valor final de 1000 rpm. La fórmula da 200 rpm en $t=0$ y se aproxima a 1000 rpm con el tiempo. Este cálculo no es un comando para un motor.

La exponencial describe la fracción de error que queda. Para calcular **cuándo** queda una fracción dada, usamos el **logaritmo natural (natural logarithm)** $\ln$, inverso de $\exp$. El argumento $0.1$ es adimensional.

$$
\exp(-t/\tau)=0.1
\quad\Longrightarrow\quad
-\frac{t}{\tau}=\ln(0.1)
\quad\Longrightarrow\quad
t=-\tau\ln(0.1)=\tau\ln(10)\approx2.303\tau.
$$

Al completar el 90 % del cambio, queda el 10 % del error inicial. Con $\tau=0.5\ \mathrm{s}$ el modelo ideal da aproximadamente 1.151 s. Los sistemas reales pueden presentar límites y retardos.

La derivada de $\ln z$ es $1/z$ para $z>0$; si $z=z(t)$ hay que multiplicar por $dz/dt$. El argumento de un logaritmo físico debe ser adimensional.

$$
\ln(1)=0,\quad \ln(\mathrm{e})=1,\quad \ln(\mathrm{e}^{z})=z,\quad \frac{d}{dz}\ln z=\frac1z\ (z>0).
$$

<a id="section-6"></a>
## 6. Integrales: desplazamiento y trabajo mecánico

La **integral indefinida (indefinite integral)** encuentra primitivas (antiderivatives) más una constante $C$. La **integral definida (definite integral)** calcula el cambio acumulado en un intervalo.

$$
\int 4t\ \mathrm{d}t=2t^2+C,\qquad \int t^n\ \mathrm{d}t=\frac{t^{n+1}}{n+1}+C\ (n\ne-1).
$$

**Desplazamiento.** Partimos de $x_0=2\ \mathrm{mm}$, con $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$. Desplazamiento entre 0 y 2 s:

$$
\Delta x=\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
$$
$$
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}=6\ \mathrm{mm}+8\ \mathrm{mm}=14\ \mathrm{mm}.
$$

Se recorren 14 mm de desplazamiento; al sumar el valor inicial, $x(2)=16\ \mathrm{mm}$. La velocidad negativa resta desplazamiento con signo, no distancia recorrida.

**Trabajo de un resorte.** Un resorte lineal ideal con $k=200\ \mathrm{N/m}$ se estira de 0 a 0.01 m. La fuerza crece con la extensión, por eso integramos cada pequeño trabajo:

$$
F(x)=kx,\qquad W=\int_0^{0.01\ \mathrm{m}}kx\ \mathrm{d}x
=\left[\frac{kx^2}{2}\right]_0^{0.01\ \mathrm{m}}
=\frac{200\ \mathrm{N/m}}2(0.01\ \mathrm{m})^2=0.01\ \mathrm{J}.
$$

El trabajo es 0.01 J. Multiplicar la fuerza final $F=2\ \mathrm{N}$ por todo el recorrido daría el valor incorrecto 0.02 J: la fuerza no era constante.

<a id="section-7"></a>
## 7. Ejemplo adicional: esfera que se expande

**Ejemplo opcional de la regla de la cadena.** El volumen de una esfera depende de su radio, que a su vez puede variar con el tiempo. Es la misma estructura que la energía del volante respecto de su velocidad angular.

$$
V(r)=\frac43\pi r^3,\qquad \frac{dV}{dt}=\frac{dV}{dr}\frac{dr}{dt}=4\pi r^2\frac{dr}{dt}.
$$

Con $r=10\ \mathrm{mm}$ y $dr/dt=1\ \mathrm{mm/s}$, obtenemos $400\pi\approx1256.64\ \mathrm{mm^3/s}$. Si $r(t)=10\ \mathrm{mm}+(1\ \mathrm{mm/s^2})t^2$, a los 2 s: $r=14\ \mathrm{mm}$, $dr/dt=4\ \mathrm{mm/s}$ y $3136\pi\approx9852.03\ \mathrm{mm^3/s}$.

<a id="section-8"></a>
## 8. Unidades, comprobaciones y ejercicios

**Comprobaciones:** derivada de posición en m/s, segunda derivada en m/s²; integral de fuerza por distancia en N·m = J; constante $C$ para integrales indefinidas; derivada local frente a integral acumulada; diferencial $\mathrm{d}t$ distinto del paso finito `dt` de un programa.

**Ejercicios:** (1) Para $x(t)=5\ \mathrm{mm}+(2\ \mathrm{mm/s})t+(1\ \mathrm{mm/s^2})t^2$, velocidad y aceleración en 3 s. (2) Con $\tau=1\ \mathrm{s}$, ¿cuándo se completa el 90 %? (3) Desplazamiento a 4 mm/s durante 2 s. **Respuestas:** 8 mm/s y 2 mm/s²; unos 2.303 s; 8 mm.

**Soluciones desarrolladas:**

1. $v(t)=\frac{dx}{dt}=2\ \mathrm{mm/s}+2(1\ \mathrm{mm/s^2})t$; $v(3\ \mathrm{s})=2+2\cdot3=8\ \mathrm{mm/s}$. $a(t)=\frac{dv}{dt}=2\ \mathrm{mm/s^2}$.
2. $f(t)=1-\exp(-t/\tau)=0.9$; $\exp(-t/\tau)=0.1$; $t=-\tau\ln(0.1)=\tau\ln(10)$. $\tau=1\ \mathrm{s}$; $t\approx2.303\ \mathrm{s}$.
3. $\Delta x=\int_0^{2\ \mathrm{s}}(4\ \mathrm{mm/s})\ \mathrm{d}t=(4\ \mathrm{mm/s})(2\ \mathrm{s})=8\ \mathrm{mm}$.


[Integral reference](../INTEGRAL_TABLE.md) · [Trigonometry](../TRIGONOMETRY.md) · [Next: motion](01-motion-calculus.md) · [Python exercises](../exercises/README.md)
