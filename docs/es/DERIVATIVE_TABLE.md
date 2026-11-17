# Tabla de derivadas

**Idiomas:** [en](../en/DERIVATIVE_TABLE.md) · [fr](../fr/DERIVATIVE_TABLE.md) · [de](../de/DERIVATIVE_TABLE.md) · [it](../it/DERIVATIVE_TABLE.md) · [es](DERIVATIVE_TABLE.md) · [pt](../pt/DERIVATIVE_TABLE.md) · [zh](../zh/DERIVATIVE_TABLE.md) · [ja](../ja/DERIVATIVE_TABLE.md) · [nb](../nb/DERIVATIVE_TABLE.md) · [ru](../ru/DERIVATIVE_TABLE.md) · [ko](../ko/DERIVATIVE_TABLE.md) · [fi](../fi/DERIVATIVE_TABLE.md) · [pl](../pl/DERIVATIVE_TABLE.md)

**Unidades empleadas aquí (definidas antes de los ejemplos):** `s` — segundo; `mm` — milímetro = 0.001 m; `mm/s` — milímetro / segundo — velocidad lineal; `mm/s²` — milímetro / segundo² — aceleración. [Glosario de unidades](UNITS.md).

[Índice del curso](README.md) · [Tabla de integrales](INTEGRAL_TABLE.md) · [Fundamentos del cálculo](notes/00-calculus-foundations.md)

Si $u$ y $v$ dependen de $x$ y $a$ es constante, las primas indican derivación respecto a $x$. Los ángulos se miden en radianes. La derivada se define solo donde existe el límite correspondiente. Para funciones compuestas se usa la regla de la cadena (chain rule). Aquí $u'=\frac{\mathrm{d}u}{\mathrm{d}x}$ y $v'=\frac{\mathrm{d}v}{\mathrm{d}x}$.

## Reglas

| Función | Derivada | Condiciones |
| --- | --- | --- |
| $c$ | $0$ | $c$ constante |
| $x$ | $1$ | — |
| $x^n$ | $nx^{n-1}$ | $n$ real; donde la función está definida y es derivable |
| $u+v$ | $u'+v'$ | — |
| $au$ | $au'$ | $a$ constante |
| $uv$ | $u'v+uv'$ | regla del producto |
| $\frac{u}{v}$ | $\frac{u'v-uv'}{v^2}$ | $v\ne0$ |
| $f(u)$ | $f'(u)u'$ | regla de la cadena |
| $\frac{1}{u}$ | $-\frac{u'}{u^2}$ | $u\ne0$ |
| $\sqrt{u}$ | $\frac{u'}{2\sqrt{u}}$ | $u>0$ |
| $\exp(u)$ | $\exp(u)u'$ | — |
| $a^u$ | $a^u\ln(a)u'$ | $a>0$ |
| $\ln(u)$ | $\frac{u'}{u}$ | $u>0$ |
| $\ln\lvert u\rvert$ | $\frac{u'}{u}$ | $u\ne0$ |
| $\sin(u)$ | $\cos(u)u'$ | — |
| $\cos(u)$ | $-\sin(u)u'$ | — |
| $\tan(u)$ | $\frac{u'}{\cos^2(u)}$ | $\cos(u)\ne0$ |
| $\arcsin(u)$ | $\frac{u'}{\sqrt{1-u^2}}$ | $-1<u<1$ |
| $\arccos(u)$ | $-\frac{u'}{\sqrt{1-u^2}}$ | $-1<u<1$ |
| $\arctan(u)$ | $\frac{u'}{1+u^2}$ | — |
| $\mathrm{arsinh}(u)$ | $\frac{u'}{\sqrt{1+u^2}}$ | — |

## Ejemplos

**Regla de la cadena (chain rule):** Para $y=(3x^2+1)^4$, tomamos $u=3x^2+1$. Entonces $u'=6x$ y

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=4u^3u'=24x(3x^2+1)^3.
$$

**Velocidad y aceleración:** Para la posición $x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2$, su derivada temporal es la velocidad y la siguiente derivada es la aceleración:

$$
v(t)=\frac{\mathrm{d}x}{\mathrm{d}t}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t,
$$

$$
a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=4\ \mathrm{mm/s^2}.
$$

En $t=2\ \mathrm{s}$, la velocidad es $11\ \mathrm{mm/s}$. Es un ejemplo matemático, no una instrucción para controlar maquinaria.

**Función inversa (inverse function):** Si $y=f^{-1}(x)$, $f$ es derivable en $y$ y $f'(y)\ne0$, entonces $(f^{-1})'(x)=1/f'(y)$ en una rama localmente invertible.
