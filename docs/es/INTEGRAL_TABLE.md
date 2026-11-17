# Tabla de integrales

**Leer en:** [en](../en/INTEGRAL_TABLE.md) · [fr](../fr/INTEGRAL_TABLE.md) · [de](../de/INTEGRAL_TABLE.md) · [it](../it/INTEGRAL_TABLE.md) · [es](INTEGRAL_TABLE.md) · [pt](../pt/INTEGRAL_TABLE.md) · [zh](../zh/INTEGRAL_TABLE.md) · [ja](../ja/INTEGRAL_TABLE.md) · [nb](../nb/INTEGRAL_TABLE.md) · [ru](../ru/INTEGRAL_TABLE.md) · [ko](../ko/INTEGRAL_TABLE.md) · [fi](../fi/INTEGRAL_TABLE.md) · [pl](../pl/INTEGRAL_TABLE.md)

**Unidades empleadas aquí (definidas antes de los ejemplos):** `s` — segundo; `mm` — milímetro = 0.001 m; `mm/s` — milímetro / segundo — velocidad lineal; `mm/s²` — milímetro / segundo² — aceleración; `N` — newton; `m` — metro; `N/m` — newton / metro — rigidez; `J` — julio (joule). [Glosario de unidades](UNITS.md).

[README](README.md) · [0. Fundamentos de derivadas, diferenciales e integrales](notes/00-calculus-foundations.md) · [Símbolos](SYMBOLS.md)

Todas las integrales indefinidas llevan +C, la constante de integración. a es constante y las fórmulas valen en intervalos donde el integrando está definido. Los ángulos se expresan en radianes.

Empieza con polinomios; las fórmulas trigonométricas y con raíces pueden dejarse para más adelante.

## Contenido

- [Potencias y logaritmos](#section-1)
- [Funciones exponenciales](#section-2)
- [Funciones trigonométricas](#section-3)
- [Expresiones racionales y trigonometría inversa](#section-4)
- [Referencia adicional: raíces y recíprocos](#section-5)
- [Elegir y comprobar una fórmula](#section-6)

<a id="section-1"></a>
## 1. Potencias y logaritmos

| Fórmula | Condiciones / significado |
| --- | --- |
| $\int 1\ \mathrm{d}x=x+C$ | todos los $x$ reales |
| $\int x^n\ \mathrm{d}x=\frac{x^{n+1}}{n+1}+C$ | $n\ne-1$; respetar el dominio real de las potencias |
| $\int\frac{1}{x}\ \mathrm{d}x=\ln\lvert x\rvert+C$ | $x\ne0$ |

<a id="section-2"></a>
## 2. Funciones exponenciales

| Fórmula | Condiciones / significado |
| --- | --- |
| $\int \mathrm{e}^{x}\ \mathrm{d}x=\mathrm{e}^{x}+C$ | todos los $x$ reales |
| $\int a^x\ \mathrm{d}x=\frac{a^x}{\ln a}+C$ | $a>0$, $a\ne1$ |

<a id="section-3"></a>
## 3. Funciones trigonométricas

| Fórmula | Condiciones / significado |
| --- | --- |
| $\int\sin x\ \mathrm{d}x=-\cos x+C$ | $x$ en radianes |
| $\int\cos x\ \mathrm{d}x=\sin x+C$ | $x$ en radianes |
| $\int\frac{1}{\cos^2 x}\ \mathrm{d}x=\tan x+C$ | $\cos x\ne0$ |
| $\int\frac{1}{\sin^2 x}\ \mathrm{d}x=-\cot x+C$ | $\sin x\ne0$ |

<a id="section-4"></a>
## 4. Expresiones racionales y trigonometría inversa

| Fórmula | Condiciones / significado |
| --- | --- |
| $\int\frac{1}{1+x^2}\ \mathrm{d}x=\arctan x+C$ | todos los $x$ reales |
| $\int\frac{1}{\sqrt{1-x^2}}\ \mathrm{d}x=\arcsin x+C$ | $\lvert x\rvert<1$ |
| $\int\frac{1}{a^2+x^2}\ \mathrm{d}x=\frac{1}{a}\arctan\frac{x}{a}+C$ | $a>0$ |
| $\int\frac{1}{a^2-x^2}\ \mathrm{d}x=\frac{1}{2a}\ln\left\lvert\frac{a+x}{a-x}\right\rvert+C$ | $a>0$, $x\ne\pm a$ |
| $\int\frac{1}{\sqrt{a^2-x^2}}\ \mathrm{d}x=\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |

<a id="section-5"></a>
## 5. Referencia adicional: raíces y recíprocos

| Fórmula | Condiciones / significado |
| --- | --- |
| $\int\frac{1}{\sqrt{x^2+a^2}}\ \mathrm{d}x=\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{a^2-x^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{a^2-x^2}+\frac{a^2}{2}\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |
| $\int\sqrt{x^2+a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2+a^2}+\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{x^2-a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2-a^2}-\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2-a^2}\right\rvert+C$ | $a>0$, $\lvert x\rvert>a$ |
| $\int\frac{1}{\sin x}\ \mathrm{d}x=\ln\left\lvert\tan\frac{x}{2}\right\rvert+C$ | $\sin x\ne0$; intervalos sin singularidades |
| $\int\frac{1}{\cos x}\ \mathrm{d}x=\ln\left\lvert\tan\left(\frac{x}{2}+\frac{\pi}{4}\right)\right\rvert+C$ | $\cos x\ne0$; intervalos sin singularidades |

## Comprobar una fórmula

Deriva el miembro derecho para comprobar cualquier fórmula. Para potencias se aplica la regla de la potencia a la inversa.

El argumento de un logaritmo debe ser adimensional; aquí x se considera adimensional salvo que se indique una escala. Respeta las condiciones de dominio y signo.

<a id="section-6"></a>
## 6. Elegir y comprobar una fórmula

Primero identifique la variable después del diferencial (dx, dt o dθ). Un coeficiente es constante solo si no depende de esa variable. En integrales indefinidas sume C; en definidas calcule F(b) − F(a). Compruebe derivando.

### Ejemplo A — desplazamiento desde la velocidad

Para v(t) = 3 mm/s + (4 mm/s²)t entre 0 y 2 s, integramos término a término:

$$
\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}
=14\ \mathrm{mm}.
$$

El resultado es 14 mm, no 14 mm/s: integrar velocidad con respecto al tiempo da desplazamiento.

### Ejemplo B — trabajo de una fuerza variable

Resorte F(x) = kx con k = 200 N/m, estirado de 0 a 0.01 m:

$$
\int_0^{0.01\ \mathrm{m}}(200\ \mathrm{N/m})x\ \mathrm{d}x
=\left[(100\ \mathrm{N/m})x^2\right]_0^{0.01\ \mathrm{m}}=0.01\ \mathrm{J}.
$$

El trabajo es 0.01 J. No debe usarse la fuerza final para todo el recorrido.

### Ejemplo C — logaritmo de una función simple

Una primitiva de 1/x es ln|x|. Con x adimensional de 1 a 2:

$$
\int_1^2\frac1x\ \mathrm{d}x=[\ln x]_1^2=\ln2-\ln1=\ln2\approx0.693.
$$

Resultado: ln 2 ≈ 0.693. x es una razón, no una longitud.
