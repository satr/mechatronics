# 0. Fundamentos de cálculo: derivadas, limites e integrais na mecânica

**Idiomas:** [en](../../en/notes/00-calculus-foundations.md) · [fr](../../fr/notes/00-calculus-foundations.md) · [de](../../de/notes/00-calculus-foundations.md) · [it](../../it/notes/00-calculus-foundations.md) · [es](../../es/notes/00-calculus-foundations.md) · [pt](00-calculus-foundations.md) · [zh](../../zh/notes/00-calculus-foundations.md) · [ja](../../ja/notes/00-calculus-foundations.md) · [nb](../../nb/notes/00-calculus-foundations.md) · [ru](../../ru/notes/00-calculus-foundations.md) · [ko](../../ko/notes/00-calculus-foundations.md) · [fi](../../fi/notes/00-calculus-foundations.md) · [pl](../../pl/notes/00-calculus-foundations.md)

A **exponencial natural** é $\exp(x)=\mathrm{e}^{x}$, em que o **número de Euler** é $\mathrm{e}\approx2.71828$. Descreve crescimento ou decaimento contínuo; $\exp(0)=1$ e $\exp(-1)\approx0.3679$. O logaritmo natural $\ln$ é a função inversa: $\ln(\exp(x))=x$. Consulte o [guia de símbolos](../SYMBOLS.md).

**Unidades aqui utilizadas (explicadas antes dos exemplos):** `s` — segundo; `mm` — milímetro = 0.001 m; `mm/s` — milímetro / segundo — velocidade linear; `mm/s²` — milímetro / segundo² — aceleração; `kg·m²` — quilograma · metro² — momento de inércia; `rad/s` — radiano / segundo — velocidade angular; `rad/s²` — radiano / segundo² — aceleração angular; `N·m` — newton · metro — binário (torque); `W` — watt; `rpm` — rotação por minuto; `N/m` — newton / metro — rigidez; `mm³/s` — milímetro³ / segundo — caudal volumétrico; `%` — percentagem (uma centésima parte); `m` — metro; `kg` — quilograma; `N` — newton; `J` — joule; `rad` — radiano. [Glossário de unidades](../UNITS.md).

[README](../README.md) · [Integral table](../INTEGRAL_TABLE.md) · [Trigonometry table](../TRIGONOMETRY.md) · [Motion](01-motion-calculus.md) · [Dynamics](02-first-order-dynamics.md) · [Symbols](../SYMBOLS.md)

> **Modelo educativo:** Verifique modelos e unidades; não use código demonstrativo em máquinas reais.

A **derivada (derivative)** indica a taxa instantânea de variação; a **segunda derivada (second derivative)** mostra como essa taxa muda. A **integral (integral)** acumula variações. Um **limite (limit)** define a taxa instantânea; um **logaritmo (logarithm)** permite descobrir o tempo numa resposta exponencial.

Estas ferramentas aparecem em eixos de máquinas, servomotores, articulações de robôs, molas e sensores. Comecemos pelo problema físico e depois escolhemos a regra e as unidades.

## Conteúdo

- [1. Da medição à equação](#section-1)
- [2. Limites e primeiras derivadas](#section-2)
- [3. Primeira e segunda derivadas: eixo em movimento](#section-3)
- [4. Regra da cadeia: energia de rotação](#section-4)
- [5. Exponenciais e logaritmos: tempo de resposta](#section-5)
- [6. Integrais: deslocamento e trabalho mecânico](#section-6)
- [7. Exemplo adicional: esfera em expansão](#section-7)
- [8. Unidades, verificações e exercícios](#section-8)

<a id="section-1"></a>
## 1. Da medição à equação

| Pergunta física | Ferramenta matemática |
| --- | --- |
| Quão depressa se move o eixo **agora**? | Primeira derivada $dx/dt$ |
| Como varia a velocidade? | Segunda derivada $d^2x/dt^2$ |
| Quando a resposta chega a 90 %? | Logaritmo $\ln$ |
| Qual o deslocamento em 2 s? | Integral definida $\int v\ \mathrm{d}t$ |
| Qual o trabalho de uma força variável? | Integral $\int F\ \mathrm{d}x$ |

<a id="section-2"></a>
## 2. Limites e primeiras derivadas

Uma **diferença finita (finite difference)** entre duas medições dá a taxa média no intervalo. A derivada é o limite dessa taxa quando o intervalo tende a zero.

$$
v(t)=\frac{dx}{dt}=\lim_{h\to0}\frac{x(t+h)-x(t)}{h}.
$$

Para $x(t)=a t^2$, com $a=2\ \mathrm{mm/s^2}$, desenvolvemos o numerador antes do limite:

$$
\frac{x(t+h)-x(t)}h=\frac{a[(t+h)^2-t^2]}h=a(2t+h)\longrightarrow 2at.
$$

O fator $h$ é cancelado **antes** de fazer $h$ tender a zero. Em $t=1\ \mathrm{s}$, a velocidade instantânea é $4\ \mathrm{mm/s}$. Não substituímos diretamente a forma indeterminada $0/0$.

**Regras de derivação (differentiation rules)**: $c$ e $n$ constantes; argumentos trigonométricos em radianos.

| Regra | Fórmula |
| --- | --- |
| Constante | $\frac{d}{dt}c=0$ |
| Potência | $\frac{d}{dt}t^n=n t^{n-1}$ |
| Coeficiente e soma | $(cf+g)'=cf'+g'$ |
| Produto | $(fg)'=f' g+fg'$ |
| Quociente, $g\ne0$ | $\left(\frac{f}{g}\right)'=\frac{f' g-fg'}{g^2}$ |
| Composição | $\frac{d}{dt}f(g(t))=f'(g(t))g'(t)$ |
| Exponencial | $\frac{d}{dt}\exp(t)=\exp(t)$ |
| Logaritmo natural, $t>0$ | $\frac{d}{dt}\ln t=\frac1t$ |
| Seno / cosseno | $\frac{d}{dt}\sin t=\cos t$, $\frac{d}{dt}\cos t=-\sin t$ |

![Declive da posição e área sob velocidade](../../../assets/figures/calculus_slope_area.svg)

<a id="section-3"></a>
## 3. Primeira e segunda derivadas: eixo em movimento

Um carro começa em 2 mm com velocidade inicial 3 mm/s e aceleração constante 4 mm/s². A sua posição é:

$$
x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2.
$$

**Primeira derivada**: velocidade. A constante desaparece, o termo linear dá 3 mm/s e o termo quadrático fica linear no tempo.

$$
v(t)=\frac{dx}{dt}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t.
$$

**Segunda derivada**: aceleração. Derivamos de novo. Em 2 s: posição 16 mm, velocidade 11 mm/s e aceleração 4 mm/s².

$$
a(t)=\frac{d^2x}{dt^2}=\frac{dv}{dt}=4\ \mathrm{mm/s^2}.
$$

A segunda derivada tem unidades comprimento/tempo²; **não** é o quadrado da primeira derivada.

<a id="section-4"></a>
## 4. Regra da cadeia: energia de rotação

Um volante em rotação armazena energia cinética. Se $\omega$ depende do tempo, a energia $E$ varia através dela: a **regra da cadeia (chain rule)**.

$$
E(\omega)=\frac12J\omega^2,\quad \omega=\omega(t),
$$
$$
\frac{dE}{dt}=\frac{dE}{d\omega}\frac{d\omega}{dt}=J\omega\alpha=M\omega=P.
$$

Para $J=0.01\ \mathrm{kg\cdot m^2}$, $\omega=10\ \mathrm{rad/s}$, $\alpha=2\ \mathrm{rad/s^2}$, o binário $J\alpha$ é $0.02\ \mathrm{N\cdot m}$ e a potência mecânica instantânea é $0.2\ \mathrm{W}$. Resulta $P=M\omega$.

<a id="section-5"></a>
## 5. Exponenciais e logaritmos: tempo de resposta

Num modelo simples de primeira ordem, a velocidade aproxima-se exponencialmente do valor final. $\tau$ é a **constante de tempo (time constant)**, em segundos.

$$
\omega(t)=\omega_\infty\bigl(1-\exp(-t/\tau)\bigr),\quad t\ge0,\ \tau>0.
$$

Esta expressão pressupõe uma **velocidade angular inicial nula**, $\omega(0)=0$, e um valor final constante $\omega_\infty$. Quando a velocidade inicial é $\omega_0\ne0$, a resposta geral do mesmo sistema de primeira ordem é:

$$
\omega(t)=\omega_\infty+(\omega_0-\omega_\infty)\exp(-t/\tau).
$$

**Exemplo com velocidade inicial não nula:** sejam $\omega_0=200\ \mathrm{rpm}$, $\omega_\infty=1000\ \mathrm{rpm}$ e $\tau=0.5\ \mathrm{s}$. Após uma constante de tempo ($t=0.5\ \mathrm{s}$):

$$
\omega(\tau)=1000+(200-1000)\exp(-1)\approx705.7\ \mathrm{rpm}.
$$

Completou-se **63.2 % da variação de 800 rpm**, não 63.2 % do valor final de 1000 rpm. Em $t=0$ a fórmula devolve 200 rpm; com o tempo aproxima-se de 1000 rpm. Isto é um cálculo teórico, não um comando para um motor.

A exponencial descreve a fração de erro restante. Para encontrar **quando** resta certa fração, utilizamos o **logaritmo natural (natural logarithm)** $\ln$, inverso de $\exp$. O argumento $0.1$ não tem dimensão.

$$
\exp(-t/\tau)=0.1
\quad\Longrightarrow\quad
-\frac{t}{\tau}=\ln(0.1)
\quad\Longrightarrow\quad
t=-\tau\ln(0.1)=\tau\ln(10)\approx2.303\tau.
$$

Ao completar 90 % da mudança, resta 10 % do erro inicial. Com $\tau=0.5\ \mathrm{s}$, o modelo ideal dá cerca de 1.151 s. Sistemas reais têm limites e atrasos.

A derivada de $\ln z$ é $1/z$ para $z>0$; para $z=z(t)$ também multiplicamos por $dz/dt$. O argumento de um logaritmo físico deve ser adimensional.

$$
\ln(1)=0,\quad \ln(\mathrm{e})=1,\quad \ln(\mathrm{e}^{z})=z,\quad \frac{d}{dz}\ln z=\frac1z\ (z>0).
$$

<a id="section-6"></a>
## 6. Integrais: deslocamento e trabalho mecânico

A **integral indefinida (indefinite integral)** encontra primitivas (antiderivatives) mais a constante $C$. A **integral definida (definite integral)** dá a variação acumulada num intervalo.

$$
\int 4t\ \mathrm{d}t=2t^2+C,\qquad \int t^n\ \mathrm{d}t=\frac{t^{n+1}}{n+1}+C\ (n\ne-1).
$$

**Deslocamento.** A posição inicial é $x_0=2\ \mathrm{mm}$ e $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$. Calculemos a deslocação de 0 a 2 s:

$$
\Delta x=\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
$$
$$
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}=6\ \mathrm{mm}+8\ \mathrm{mm}=14\ \mathrm{mm}.
$$

O deslocamento é 14 mm; juntando a posição inicial obtemos $x(2)=16\ \mathrm{mm}$. Velocidade negativa reduz deslocamento com sinal, não a distância percorrida.

**Trabalho da mola.** Uma mola linear ideal com $k=200\ \mathrm{N/m}$ é esticada de 0 a 0.01 m. A força aumenta com a extensão, portanto integramos os pequenos trabalhos:

$$
F(x)=kx,\qquad W=\int_0^{0.01\ \mathrm{m}}kx\ \mathrm{d}x
=\left[\frac{kx^2}{2}\right]_0^{0.01\ \mathrm{m}}
=\frac{200\ \mathrm{N/m}}2(0.01\ \mathrm{m})^2=0.01\ \mathrm{J}.
$$

O trabalho é 0.01 J. Multiplicar a força final $F=2\ \mathrm{N}$ por todo o percurso daria incorretamente 0.02 J: a força não é constante.

<a id="section-7"></a>
## 7. Exemplo adicional: esfera em expansão

**Exemplo opcional de regra da cadeia.** O volume da esfera depende do raio, que pode variar no tempo — a mesma estrutura da energia do volante dependente da velocidade angular.

$$
V(r)=\frac43\pi r^3,\qquad \frac{dV}{dt}=\frac{dV}{dr}\frac{dr}{dt}=4\pi r^2\frac{dr}{dt}.
$$

Para $r=10\ \mathrm{mm}$ e $dr/dt=1\ \mathrm{mm/s}$, $400\pi\approx1256.64\ \mathrm{mm^3/s}$. Se $r(t)=10\ \mathrm{mm}+(1\ \mathrm{mm/s^2})t^2$, em 2 s: $r=14\ \mathrm{mm}$, $dr/dt=4\ \mathrm{mm/s}$ e $3136\pi\approx9852.03\ \mathrm{mm^3/s}$.

<a id="section-8"></a>
## 8. Unidades, verificações e exercícios

**Verificações:** derivada de posição em m/s, segunda em m/s²; integral de força ao longo do percurso em N·m = J; constante $C$ em integrais indefinidas; derivada local versus integral acumulada; diferencial $\mathrm{d}t$ distinto do passo finito `dt` do programa.

**Exercícios:** (1) Para $x(t)=5\ \mathrm{mm}+(2\ \mathrm{mm/s})t+(1\ \mathrm{mm/s^2})t^2$, velocidade e aceleração em 3 s. (2) Para $\tau=1\ \mathrm{s}$, tempo até 90 %? (3) Deslocamento a 4 mm/s durante 2 s. **Respostas:** 8 mm/s e 2 mm/s²; aproximadamente 2.303 s; 8 mm.

**Resoluções detalhadas:**

1. $v(t)=\frac{dx}{dt}=2\ \mathrm{mm/s}+2(1\ \mathrm{mm/s^2})t$; $v(3\ \mathrm{s})=2+2\cdot3=8\ \mathrm{mm/s}$. $a(t)=\frac{dv}{dt}=2\ \mathrm{mm/s^2}$.
2. $f(t)=1-\exp(-t/\tau)=0.9$; $\exp(-t/\tau)=0.1$; $t=-\tau\ln(0.1)=\tau\ln(10)$. $\tau=1\ \mathrm{s}$; $t\approx2.303\ \mathrm{s}$.
3. $\Delta x=\int_0^{2\ \mathrm{s}}(4\ \mathrm{mm/s})\ \mathrm{d}t=(4\ \mathrm{mm/s})(2\ \mathrm{s})=8\ \mathrm{mm}$.


[Integral reference](../INTEGRAL_TABLE.md) · [Trigonometry](../TRIGONOMETRY.md) · [Next: motion](01-motion-calculus.md) · [Python exercises](../exercises/README.md)
