# Trigonometría: ángulos, seno, coseno, tangente y arcotangente

**Idiomas:** [en](../en/TRIGONOMETRY.md) · [fr](../fr/TRIGONOMETRY.md) · [de](../de/TRIGONOMETRY.md) · [it](../it/TRIGONOMETRY.md) · [es](TRIGONOMETRY.md) · [pt](../pt/TRIGONOMETRY.md) · [zh](../zh/TRIGONOMETRY.md) · [ja](../ja/TRIGONOMETRY.md) · [nb](../nb/TRIGONOMETRY.md) · [ru](../ru/TRIGONOMETRY.md) · [ko](../ko/TRIGONOMETRY.md) · [fi](../fi/TRIGONOMETRY.md) · [pl](../pl/TRIGONOMETRY.md)

**Unidades empleadas aquí (definidas antes de los ejemplos):** `°` — grado; `rad` — radián; `kg` — kilogramo; `m` — metro; `m/s²` — metro / segundo² — aceleración; `N·m` — newton · metro — par de torsión; `mm` — milímetro = 0.001 m; `N` — newton. [Glosario de unidades](UNITS.md).

[README](README.md) · [Calculus](notes/00-calculus-foundations.md) · [Integral table](INTEGRAL_TABLE.md)

<a id="unit-circle-values"></a>
## Circunferencia unitaria: seno y coseno

Un punto de la circunferencia unitaria de ángulo θ tiene coordenadas **(cos θ, sin θ)**. Los ángulos se miden desde +X en sentido antihorario. Coseno (cosine) es horizontal y seno (sine) vertical. Un solo diagrama muestra los 16 pares exactos; una única tabla agrega aproximaciones, tangente y arcotangente principal.

![Una circunferencia unitaria con 16 ángulos y pares exactos (cos θ, sin θ).](../../assets/figures/unit_circle_reference.svg)

*Una circunferencia unitaria con 16 ángulos y pares exactos (cos θ, sin θ).*

**Fracciones exactas y aproximaciones decimales:**

| θ | cos θ (exacto) | cos θ (decimal) | sin θ (exacto) | sin θ (decimal) | tan θ (exacto) | tan θ (decimal) | arctan(tan θ), principal |
| --- | --- | ---: | --- | ---: | --- | ---: | --- |
| 0° | $1$ | 1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 30° | $\frac{\sqrt3}{2}$ | 0.8660 | $\frac12$ | 0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 45° | $\frac{\sqrt2}{2}$ | 0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 60° | $\frac12$ | 0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 90° | $0$ | 0.0000 | $1$ | 1.0000 | **indefinido** | — | — |
| 120° | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 135° | $-\frac{\sqrt2}{2}$ | -0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 150° | $-\frac{\sqrt3}{2}$ | -0.8660 | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |
| 180° | $-1$ | -1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 210° | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 225° | $-\frac{\sqrt2}{2}$ | -0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 240° | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 270° | $0$ | 0.0000 | $-1$ | -1.0000 | **indefinido** | — | — |
| 300° | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 315° | $\frac{\sqrt2}{2}$ | 0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 330° | $\frac{\sqrt3}{2}$ | 0.8660 | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |

La tangente es **indefinida** a 90° y 270° porque cos θ = 0; también lo es arctan(tan θ). La última columna muestra el **valor principal** entre −90° y 90°, que puede diferir del ángulo original: arctan(tan 135°) = −45° y arctan(tan 225°) = 45°. Los decimales se redondean a cuatro cifras. A 360° se repiten los valores de 0°.

<a id="trigonometric-identities"></a>
### Identidades trigonométricas útiles

Desplazar 90° intercambia seno y coseno, a veces invierte el signo. Los paréntesis son imprescindibles: cos(θ − 90°) indica el coseno de la diferencia, no cos θ menos 90.

$$
\cos(90^\circ-\theta)=\sin(\theta),\qquad
\sin(90^\circ-\theta)=\cos(\theta)
$$

$$
\cos(\theta-90^\circ)=\sin(\theta),\qquad
\sin(\theta+90^\circ)=\cos(\theta)
$$

$$
\cos(\theta+90^\circ)=-\sin(\theta),\qquad
\sin(\theta-90^\circ)=-\cos(\theta)
$$

**Ángulos negativos y periodicidad:**

$$
\sin(-\theta)=-\sin(\theta),\qquad
\cos(-\theta)=\cos(\theta)
$$

$$
\tan(-\theta)=-\tan(\theta),\qquad
\tan(\theta)=\frac{\sin(\theta)}{\cos(\theta)}
$$

$$
\sin(\theta+360^\circ)=\sin(\theta),\qquad
\cos(\theta+360^\circ)=\cos(\theta)
$$

$$
\tan(\theta+180^\circ)=\tan(\theta),\qquad
\sin^2(\theta)+\cos^2(\theta)=1
$$

Signos por cuadrante (cos, sin, tan): I (+,+,+), II (−,+,−), III (−,−,+), IV (+,−,−). Los ángulos negativos giran en sentido horario.

Al calcular ángulos inversos, comprueba el cuadrante y el intervalo principal.

<a id="inverse-cosine-reference"></a>
### Arcocoseno y estimación del ángulo

Entre 0° y 180° el coseno desciende de 1 a −1. Por tanto, arccos(0.19) es algo menor que 80°: cos 80°≈0.1736 y arccos(0.19)≈79.05°. Como cos(+θ)=cos(−θ), pueden existir dos configuraciones articulares con signos opuestos. El valor principal de arccos está entre 0° y 180°.

![cos θ versus θ, with arccos(0.19) marked](../../assets/figures/arccos_reference_curve.svg)



## Esquema: cateto opuesto, adyacente e hipotenusa

![Tres triángulos rectángulos: seno = cateto opuesto a entre hipotenusa c; coseno = adyacente b entre c; tangente = a entre b.](../../assets/figures/trig_ratios.svg)

En la figura, **a** es el cateto opuesto al ángulo θ, **b** el adyacente y **c** la hipotenusa. Para un ángulo agudo, $\sin\theta=a/c$, $\cos\theta=b/c$, $\tan\theta=a/b$ (si $b\ne0$). Las **longitudes de los lados no son negativas**; esta figura por sí sola no indica los signos de los ángulos negativos u otros cuadrantes. Para un ángulo orientado desde el eje x positivo, $\sin(+60^\circ)=+\sqrt3/2$, mientras que $\sin(-60^\circ)=-\sqrt3/2$.

## Mecánica: par gravitatorio sobre una palanca

Para una masa m a distancia L del eje y una palanca a θ sobre la horizontal, la **magnitud** del par es mgL|cos θ|. El signo depende del sentido positivo de rotación.

$$
|M_g|=mgL|\cos\theta|.
$$

Con m = 0.5 kg, L = 0.2 m, g = 9.81 m/s² y θ = 60°, el módulo es 0.4905 N·m; a 0° es 0.981 N·m y a 90° cero (carga puntual ideal).

## Ejemplo inverso: calcular un ángulo

Un eje sube 0.05 m en 0.1 m de avance horizontal: razón 0.5. Así, θ = arctan(0.5) ≈ 26.565°. El argumento no son grados.

$$
\tan\theta=\frac{0.05\ \mathrm{m}}{0.1\ \mathrm{m}}=0.5,\qquad \theta=\arctan(0.5)\approx26.565^\circ.
$$

Conversión: θ_rad = θ_deg·π/180. Las bibliotecas matemáticas normalmente esperan radianes.

$$
\theta_{\mathrm{rad}}=\theta_{\mathrm{deg}}\frac{\pi}{180}.
$$

### Dirección de un vector: por qué usar `atan2`

Para un vector desde el origen hasta $(x,y)$, la arcotangente ordinaria solo conoce el cociente $y/x$. Los vectores $(1, -1)$ y $(-1, 1)$ tienen el mismo cociente, pero señalan **cuadrantes distintos**. Si $x=-1\ \mathrm{mm}$ e $y=+1\ \mathrm{mm}$, usar solo ese cociente da una dirección global equivocada:

$$
\arctan\left(\frac{y}{x}\right)=\arctan(-1)=-45^\circ,\qquad
\operatorname{atan2}(+1, -1)=+135^\circ.
$$

`atan2(y, x)` utiliza el signo de **ambas componentes** y encuentra la dirección de un vector no nulo. Los argumentos deben usar la misma unidad de longitud. Cuando $x=0$, el cociente $y/x$ no está definido; `atan2` aún determina la dirección sobre el eje si $y\ne0$. Para $(0, 0)$ no existe dirección; $+180^\circ$ y $-180^\circ$ representan la misma. Es importante al calcular [ángulos de marcos de referencia](notes/04-coordinate-frames.md).

## Ley de cosenos: geometría de dos eslabones

![Two-link robot triangle OAB, exact link lengths and the law of cosines](../../assets/figures/two_link_cosine_law.svg)

La base O, la articulación A y la herramienta B forman un triángulo: OA = L1, AB = L2 y OB = r, distancia directa de la base a la herramienta. La figura usa L1 = 100 mm, L2 = 50 mm y r = 120 mm. El ángulo interior φ no es el ángulo relativo θ2: φ = 180° − |θ2|. La figura muestra θ2 negativo; su reflexión tiene θ2 positivo.

La ley de cosenos es $r^2=L_1^2+L_2^2-2L_1L_2\cos\varphi$. Como $\cos(180^\circ-|\theta_2|)=-\cos\theta_2$, también $r^2=L_1^2+L_2^2+2L_1L_2\cos\theta_2$, así que $\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}$. Aquí $(14400-10000-2500)/10000=0.19$ y $|\theta_2|\approx79.05^\circ$. Para llegar a un punto (X,Y) también se necesita θ1.


[Cálculo](notes/00-calculus-foundations.md) · [Control por realimentación](notes/03-feedback-control.md)
