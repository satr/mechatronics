# Tabela de derivadas

**Idiomas:** [en](../en/DERIVATIVE_TABLE.md) · [fr](../fr/DERIVATIVE_TABLE.md) · [de](../de/DERIVATIVE_TABLE.md) · [it](../it/DERIVATIVE_TABLE.md) · [es](../es/DERIVATIVE_TABLE.md) · [pt](DERIVATIVE_TABLE.md) · [zh](../zh/DERIVATIVE_TABLE.md) · [ja](../ja/DERIVATIVE_TABLE.md) · [nb](../nb/DERIVATIVE_TABLE.md) · [ru](../ru/DERIVATIVE_TABLE.md) · [ko](../ko/DERIVATIVE_TABLE.md) · [fi](../fi/DERIVATIVE_TABLE.md) · [pl](../pl/DERIVATIVE_TABLE.md)

**Unidades aqui utilizadas (explicadas antes dos exemplos):** `s` — segundo; `mm` — milímetro = 0.001 m; `mm/s` — milímetro / segundo — velocidade linear; `mm/s²` — milímetro / segundo² — aceleração. [Glossário de unidades](UNITS.md).

[Índice do curso](README.md) · [Tabela de integrais](INTEGRAL_TABLE.md) · [Fundamentos de cálculo](notes/00-calculus-foundations.md)

Se $u$ e $v$ dependem de $x$ e $a$ é constante, os apóstrofos indicam a derivada em relação a $x$. Os ângulos medem-se em radianos. A derivada está definida somente onde existe o limite correspondente. Para funções compostas aplica-se a regra da cadeia (chain rule). Aqui $u'=\frac{\mathrm{d}u}{\mathrm{d}x}$ e $v'=\frac{\mathrm{d}v}{\mathrm{d}x}$.

## Regras

| Função | Derivada | Condições |
| --- | --- | --- |
| $c$ | $0$ | $c$ constante |
| $x$ | $1$ | — |
| $x^n$ | $nx^{n-1}$ | $n$ real; onde a função está definida e é derivável |
| $u+v$ | $u'+v'$ | — |
| $au$ | $au'$ | $a$ constante |
| $uv$ | $u'v+uv'$ | regra do produto |
| $\frac{u}{v}$ | $\frac{u'v-uv'}{v^2}$ | $v\ne0$ |
| $f(u)$ | $f'(u)u'$ | regra da cadeia |
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

## Exemplos

**Regra da cadeia (chain rule):** Para $y=(3x^2+1)^4$, definimos $u=3x^2+1$. Assim, $u'=6x$ e

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=4u^3u'=24x(3x^2+1)^3.
$$

**Velocidade e aceleração:** Para a posição $x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2$, a derivada no tempo dá a velocidade e a derivada desta dá a aceleração:

$$
v(t)=\frac{\mathrm{d}x}{\mathrm{d}t}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t,
$$

$$
a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=4\ \mathrm{mm/s^2}.
$$

Em $t=2\ \mathrm{s}$, a velocidade é $11\ \mathrm{mm/s}$. É um exemplo matemático, não uma instrução de controlo de máquinas.

**Função inversa (inverse function):** Se $y=f^{-1}(x)$, $f$ é derivável em $y$ e $f'(y)\ne0$, então $(f^{-1})'(x)=1/f'(y)$ num ramo localmente invertível.
