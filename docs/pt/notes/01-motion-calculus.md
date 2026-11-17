# 1. Movimento, derivadas e integrais


**Ler esta página em:** [en](../../en/notes/01-motion-calculus.md) · [fr](../../fr/notes/01-motion-calculus.md) · [de](../../de/notes/01-motion-calculus.md) · [it](../../it/notes/01-motion-calculus.md) · [es](../../es/notes/01-motion-calculus.md) · [pt](01-motion-calculus.md) · [zh](../../zh/notes/01-motion-calculus.md) · [ja](../../ja/notes/01-motion-calculus.md) · [nb](../../nb/notes/01-motion-calculus.md) · [ru](../../ru/notes/01-motion-calculus.md) · [ko](../../ko/notes/01-motion-calculus.md) · [fi](../../fi/notes/01-motion-calculus.md) · [pl](../../pl/notes/01-motion-calculus.md)

**Unidades aqui utilizadas (explicadas antes dos exemplos):** `s` — segundo; `mm` — milímetro = 0.001 m; `mm/s` — milímetro / segundo — velocidade linear; `mm/s²` — milímetro / segundo² — aceleração; `%` — percentagem (uma centésima parte). [Glossário de unidades](../UNITS.md).

**Fundamentos:** [0. Fundamentos de derivadas, diferenciais e integrais](00-calculus-foundations.md) · [Tabela de integrais](../INTEGRAL_TABLE.md)

[README](../README.md) · [Resumo de fórmulas](../CHEATSHEET.md) · [Exercícios Python](../exercises/README.md) · [Dinâmica de primeira ordem e rotação](02-first-order-dynamics.md)

> **Aviso:** Este material educativo com assistência de IA pode conter erros, traduções imprecisas ou pressupostos incorretos. A utilização é por conta e risco de quem o consulta. Confirme os cálculos de forma independente e nunca utilize os exemplos para controlar máquinas reais.

## Revisão rápida

A distância percorrida é o comprimento total do trajeto; o deslocamento corresponde à posição final menos a inicial. A rapidez (speed) não é negativa; a velocidade vetorial (velocity) inclui direção. A derivada da posição fornece a velocidade instantânea e a integral da velocidade com sinal fornece o deslocamento.

**Termos ingleses:**

- distância percorrida (distance traveled)
- deslocamento (displacement)
- rapidez (speed)
- velocidade vetorial (velocity)
- derivada (derivative)
- integral (integral)
- integração numérica (numerical integration)
- método de Euler explícito (explicit Euler method)

## Nesta página

- [1. Exemplo de movimento](#section-1)
- [2. Derivada e velocidade instantânea](#section-2)
- [3. Integral e deslocamento](#section-3)
- [4. Integração numérica](#section-4)
- [5. Experimentar](#section-5)
- [6. Informação adicional (opcional)](#section-6)
  - [Por que a derivada de 2t² é 4t](#power-rule-derivation)
  - [Como calcular os deslocamentos da tabela](#motion-values-derivation)

[Unidades SI e ponto decimal](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Exemplo de movimento

Para unidades, demonstrações e limites numéricos, consulte a [Informação adicional](#section-6).

Um eixo virtual move-se a $+3\ \mathrm{mm/s}$ durante dois segundos e depois a $-3\ \mathrm{mm/s}$ durante mais dois. O deslocamento é $+6-6=0\ \mathrm{mm}$, mas a distância percorrida é $12\ \mathrm{mm}$. No movimento circular, a direção da velocidade vetorial muda mesmo quando a rapidez é constante.

$$
\overline{v}=\frac{x(t_2)-x(t_1)}{t_2-t_1}.
$$

$$
\text{rapidez média}=\frac{\text{distância total percorrida}}{t_2-t_1}.
$$

Durante **os quatro segundos completos**, a velocidade média com sinal e a rapidez média têm **valores diferentes**. O eixo regressa ao ponto inicial apesar de percorrer 12 mm:

$$
\overline{v}_x=\frac{0\ \mathrm{mm}}{4\ \mathrm{s}}=0\ \mathrm{mm/s}
$$

$$
\overline{\lvert v\rvert}=\frac{12\ \mathrm{mm}}{4\ \mathrm{s}}=3\ \mathrm{mm/s}
$$

Assim, a rapidez média **não é necessariamente o módulo da velocidade vetorial média**. Numa volta circular completa, a velocidade vetorial média também é zero, embora a distância percorrida e a rapidez média sejam positivas.

<a id="section-2"></a>

## 2. Derivada e velocidade instantânea

Para $x(t)=2t^2\ \mathrm{mm}$, com $t$ em segundos, $v(t)=4t\ \mathrm{mm/s}$. **De onde vem o 4?** A regra da potência dá $d(t^2)/dt=2t$; portanto, $2t^2$ resulta em $2\cdot2t=4t$. [Cálculo completo e unidades](#power-rule-derivation). Em $t=1\ \mathrm{s}$, a velocidade instantânea é $4\ \mathrm{mm/s}$. A diferença finita progressiva fornece $6$, $4.2$ e $4.02\ \mathrm{mm/s}$ com passos $dt=1$, $0.1$ e $0.01\ \mathrm{s}$.

$$
v(t)=\frac{dx}{dt},\qquad v(t)\approx\frac{x(t+dt)-x(t)}{dt}.
$$

**Porque um passo demasiado pequeno pode falhar:** em $t=1\ \mathrm{s}$, a derivada exata de $x(t)=2t^2$ é $4\ \mathrm{mm/s}$. Com $dt=1e-17\ \mathrm{s}$, o tipo `float` de Python arredonda `t + dt` de volta a `t`: as posições calculadas coincidem e a diferença indicaria erradamente velocidade nula. Em escalas ainda menores, ambas as posições podem arredondar para zero apesar de a derivada não ser zero. O exemplo [`forward_derivative`](../../../exercises/01_motion_and_integral.py) agora lança `ValueError` em vez desse falso zero. O método continua a calcular uma diferença finita; escolha um passo resolúvel numericamente, em vez de o reduzir sem limite.

<a id="section-3"></a>

## 3. Integral e deslocamento

A integral da velocidade com sinal pode ser negativa ou nula; a integral do seu módulo dá uma distância não negativa. Para $v(t)=2t\ \mathrm{mm/s}$ entre $0$ e $2\ \mathrm{s}$, o deslocamento exato é $4\ \mathrm{mm}$.

$$
\Delta x=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t,\qquad
s=\int_{t_1}^{t_2}|v(t)|\ \mathrm{d}t.
$$

Geometricamente, o primeiro integral representa a área com sinal sob a curva velocidade–tempo. **Este exemplo é diferente do da secção 2.** Aí, a posição $x(t)=2t^2$ tem derivada $v(t)=4t$. Para demonstrar a integração, escolhe-se aqui deliberadamente outra velocidade: $v(t)=2t$. A posição correspondente é $x(t)=t^2+C$ (com unidades coerentes). Não se devem confundir as duas leis do movimento.

<a id="section-4"></a>

## 4. Integração numérica

Deslocamento exato e aproximação de Euler pelo início do intervalo (dados sintéticos).

![Deslocamento exato e aproximação de Euler pelo início do intervalo (dados sintéticos)](../../../assets/figures/euler_vs_exact.svg)

O método de Euler explícito usa a velocidade **no início** de cada intervalo, não a média exata. Para esta velocidade crescente, subestima o deslocamento: com $dt=0.5$, $0.1$ e $0.01\ \mathrm{s}$ obtêm-se $3$, $3.8$ e $3.98\ \mathrm{mm}$ (exato: $4\ \mathrm{mm}$). A regra dos trapézios é exata neste caso linear.

$$
x_{n+1}=x_n+v(t_n)\ dt.
$$

| `dt` (s) | Euler (mm) |
| ---: | ---: |
| 0.5 | 3.000 |
| 0.1 | 3.800 |
| 0.01 | 3.980 |
| Exato | 4.000 |


[Cálculo de 3; 3.8 e 3.98.](#motion-values-derivation)

<a id="section-5"></a>

## 5. Experimentar

Execute o programa de movimento e diminua $dt$. Por que motivo uma viagem de ida e volta pode ter deslocamento nulo mas distância percorrida positiva?

[01_motion_and_integral.py](../../../exercises/01_motion_and_integral.py)

<a id="section-6"></a>

## 6. Informação adicional (opcional)

### Unidades e coeficientes

Se $t$ estiver em segundos, $x(t)=2t^2$ mm é uma escrita abreviada: o coeficiente tem unidades $2\ \mathrm{mm/s^2}$. Assim, $v(t)=4t$ exprime-se em mm/s. Confirme as unidades.

### Limites da aproximação

Uma diferença finita (finite difference) estima a derivada num intervalo não nulo. Um passo menor reduz muitas vezes o erro de discretização, mas um passo minúsculo pode amplificar erros de arredondamento ou ruído. Euler usa o valor no início do passo.

### Movimento em várias dimensões

Para o vetor posição $\mathbf r(t)$, $\mathbf v=d\mathbf r/dt$; a rapidez é $\|\mathbf v\|$ e a distância percorrida $s=\int\|\mathbf v(t)\|dt$.


<a id="power-rule-derivation"></a>

### Por que a derivada de $2t^2$ é $4t$



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

### Como calcular os deslocamentos da tabela

$$
a=2\ \mathrm{mm/s^2},\qquad v(t)=at,\qquad 0\le t\le2\ \mathrm{s}.
$$

$$
\Delta x=\int_{0}^{2\ \mathrm{s}}at\ \mathrm{d}t
=\left[\frac{at^2}{2}\right]_{0}^{2\ \mathrm{s}}
=4\ \mathrm{mm}.
$$



O símbolo $\sum$ (sigma maiúsculo grego, **somatório** / summation) indica a adição dos termos. Em $\sum_{n=0}^{N-1}(2nh)h$, o índice $n$ percorre $0; 1; \ldots; N-1$: são $N$ parcelas. É semelhante a um ciclo Python `for` que acumula contribuições. Por exemplo, $\sum_{n=1}^{3}n=1+2+3=6$. [← Símbolos explicados](../SYMBOLS.md#summation).

$$
h=\frac{dt}{1\ \mathrm{s}},\qquad N=\frac{2}{h}.
$$

$$
x_{\mathrm{Euler}}(2\ \mathrm{s})
=\left[\sum_{n=0}^{N-1}(2nh)h\right]\ \mathrm{mm}
=\left[h^2N(N-1)\right]\ \mathrm{mm}
=(4-2h)\ \mathrm{mm}.
$$

Aqui `h` é o valor numérico do passo `dt` em segundos (`dt = 0.5 s` implica `h = 0.5`); `N` é o número de passos. O resultado é uma **distância em milímetros**.



Com $dt=0.5$, $0.1$ e $0.01$ segundos, obtêm-se $3$, $3.8$ e $3.98$ milímetros. Supõe-se que $2/dt$ é inteiro.
