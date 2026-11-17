# 2. Dinâmica de primeira ordem e rotação


**Ler esta página em:** [en](../../en/notes/02-first-order-dynamics.md) · [fr](../../fr/notes/02-first-order-dynamics.md) · [de](../../de/notes/02-first-order-dynamics.md) · [it](../../it/notes/02-first-order-dynamics.md) · [es](../../es/notes/02-first-order-dynamics.md) · [pt](02-first-order-dynamics.md) · [zh](../../zh/notes/02-first-order-dynamics.md) · [ja](../../ja/notes/02-first-order-dynamics.md) · [nb](../../nb/notes/02-first-order-dynamics.md) · [ru](../../ru/notes/02-first-order-dynamics.md) · [ko](../../ko/notes/02-first-order-dynamics.md) · [fi](../../fi/notes/02-first-order-dynamics.md) · [pl](../../pl/notes/02-first-order-dynamics.md)

**Unidades aqui utilizadas (explicadas antes dos exemplos):** `s` — segundo; `mm/s` — milímetro / segundo — velocidade linear; `kg` — quilograma; `m` — metro; `rad/s` — radiano / segundo — velocidade angular; `N` — newton; `N·m` — newton · metro — binário (torque); `J` — joule; `rpm` — rotação por minuto; `kg·m²` — quilograma · metro² — momento de inércia; `N·m·s/rad` — newton · metro · segundo / radiano — ganho por velocidade; `%` — percentagem (uma centésima parte); `rad` — radiano. [Glossário de unidades](../UNITS.md).

**Fundamentos:** [0. Fundamentos de derivadas, diferenciais e integrais](00-calculus-foundations.md) · [Tabela de integrais](../INTEGRAL_TABLE.md)

[README](../README.md) · [Resumo de fórmulas](../CHEATSHEET.md) · [Exercícios Python](../exercises/README.md) · [Movimento, derivadas e integrais](01-motion-calculus.md)

> **Aviso:** Este material educativo com assistência de IA pode conter erros, traduções imprecisas ou pressupostos incorretos. A utilização é por conta e risco de quem o consulta. Confirme os cálculos de forma independente e nunca utilize os exemplos para controlar máquinas reais.

> **Hipóteses do modelo do motor:** Assume-se um controlo proporcional ideal do binário, sem carga, atrito, atrasos, limites de tensão, saturação ou dinâmica de ordem superior. Não é uma descrição universal dos motores.

## Revisão rápida

A constante de tempo $\tau$ caracteriza a rapidez de aproximação ao equilíbrio num sistema de primeira ordem. O passo de simulação $dt$ altera a resolução numérica, não as propriedades físicas. No modelo ideal $\tau=\frac{J}{K}$; a mesma resposta não implica o mesmo binário nem a mesma energia.

**Termos ingleses:**

- sistema de primeira ordem (first-order system)
- constante de tempo (time constant)
- passo temporal (time step)
- momento de inércia (moment of inertia)
- binário (torque)
- ganho do controlador (controller gain)
- aceleração angular (angular acceleration)
- identificação do sistema (system identification)
- energia cinética de rotação (rotational kinetic energy)

## Nesta página

- [1. Resposta de primeira ordem](#section-1)
- [2. Binário e inércia](#section-2)
- [3. Passo numérico e constante de tempo](#section-3)
- [4. Estimar a constante de tempo a partir de medições](#section-4)
- [5. Energia de rotação](#section-5)
- [6. Experimentar](#section-6)
- [7. Informação adicional (opcional)](#section-7)
  - [De onde vêm 63.2 %, 86.5 % e 95.0 %?](#time-constant-derivation)
  - [Como calcular os valores de Euler](#euler-values-derivation)

[Unidades SI e ponto decimal](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Resposta de primeira ordem

Para unidades, demonstrações e limites numéricos, consulte a [Informação adicional](#section-7).

Com velocidade-alvo constante $u$, velocidade atual $v$ e $\tau>0$, o modelo realiza cerca de $63.2\ \%$ da alteração após $\tau$, $86.5\ \%$ após $2\tau$ e $95.0\ \%$ após $3\tau$. Isso não significa atingir exatamente o alvo após uma única constante de tempo.

**Notação:** $\varepsilon(t)=u-v(t)$ é o erro de velocidade (speed error; épsilon grego). A função exponencial natural (exponential function) é $\exp(z)=\mathrm{e}^{z}$, em que $\mathrm{e}\approx2.71828$ é o número de Euler (Euler’s number), **não** o erro. [Dedução e cálculo dos 63.2 %](#time-constant-derivation).

$$
\frac{dv}{dt}=\frac{u-v}{\tau}.
$$

$$
v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right).
$$

| Tempo | Fração da alteração |
| --- | ---: |
| $\tau$ | 63.2 % |
| $2\tau$ | 86.5 % |
| $3\tau$ | 95.0 % |

[Por que exatamente essas percentagens? Veja o cálculo.](#time-constant-derivation)

![Resposta normalizada de primeira ordem: cada constante de tempo elimina cerca de 63.2 % do erro restante.](../../../assets/figures/first_order_response.svg)

<a id="section-2"></a>

## 2. Binário e inércia

O controlador calcula um comando elétrico; o motor produz fisicamente o binário $M$. No modelo $J$ é o momento de inércia, $\omega$ a velocidade angular e $K$ o coeficiente que relaciona o binário com o erro de velocidade. Duplicar $J$ com $K$ constante duplica $\tau$. Duplicar ambos mantém $\tau$ e duplica o binário para o mesmo erro. Atrito, cargas, atrasos e limites de corrente não estão incluídos.

$$
J\frac{d\omega}{dt}=M,\qquad M=K(u-\omega).
$$

$$
\frac{d\omega}{dt}=\frac{K}{J}(u-\omega),\qquad \tau=\frac{J}{K}.
$$

**Unidades:** $J$: $\mathrm{kg}\cdot\mathrm{m}^2$; $\omega,u$: $\mathrm{rad/s}$; $M$: $\mathrm{N}\cdot\mathrm{m}$; $K$: $\mathrm{N}\cdot\mathrm{m}\cdot\mathrm{s}/\mathrm{rad}$; $\tau$: s.

Malha de realimentação simbólica do modelo ideal. O controlador envia um comando; o motor produz o binário físico.

![Malha de realimentação simbólica do modelo ideal. O controlador envia um comando; o motor produz o binário físico](../../../assets/figures/control_loop.svg)

<a id="section-3"></a>

## 3. Passo numérico e constante de tempo

Euler atualiza o estado em intervalos $dt$. Diminuir $dt$ não acelera o motor modelado: apenas altera a precisão da aproximação. Com $u=10\ \mathrm{mm/s}$, $\tau=1\ \mathrm{s}$ e um segundo, Euler produz $6.513$ para $dt=0.1$ ou $6.340\ \mathrm{mm/s}$ para $dt=0.01$; o valor exato é $6.321\ \mathrm{mm/s}$.

$$
v_{n+1}=v_n+\frac{u-v_n}{\tau}\ dt.
$$

| Método | $v(1\ \mathrm{s})$ (mm/s) |
| --- | ---: |
| Euler $dt=0.1\ \mathrm{s}$ | 6.513 |
| Euler $dt=0.01\ \mathrm{s}$ | 6.340 |
| Exato | 6.321 |

[Cálculo dos valores numéricos.](#euler-values-derivation)

<a id="section-4"></a>

## 4. Estimar a constante de tempo a partir de medições

Num degrau de referência de 0 para 1000 rpm, procure quando a velocidade medida atinge cerca de 632 rpm. Se ocorrer aos 2 segundos, o modelo de primeira ordem sugere $\tau\approx2\ \mathrm{s}$. Para uma velocidade inicial diferente de zero, use 63.2 % da **alteração total**. Ruído, atrasos e sobre-elevação tornam menos precisa esta identificação do sistema (system identification).

**O que o código devolve:** a função [`estimate_tau`](../../../exercises/02_first_order_response.py) recebe medições com tempos **estritamente crescentes**, a contar do início do degrau. Devolve o instante da **primeira amostra observada** que atinge o limiar de 63.2 % da variação, com tolerância de metade da resolução de medição conhecida. Se o limiar aparece pela primeira vez aos 2 s e a amostra anterior foi aos 1 s, o cruzamento real pode ter ocorrido **entre amostras**. Assim, 2 s é uma estimativa limitada pela amostragem, não um ajuste exato. Valores inválidos e tempos repetidos ou fora de ordem são rejeitados, mesmo após o limiar; sem cruzamento o resultado é `None`.

**A resolução do sensor importa:** o parâmetro `resolution` de `estimate_tau` tem de ser **menor do que o módulo da variação total de velocidade**. Se a velocidade passa de 0 para 10 rpm, mas o visor muda apenas em passos de 10 rpm, não é possível estimar com fiabilidade a passagem pelo limiar de 63.2 %. A função rejeita estes dados em vez de indicar uma passagem artificial na primeira amostra. Mesmo com resolução suficiente, a estimativa continua limitada pela amostragem.

<a id="section-5"></a>

## 5. Energia de rotação

O binário resultante satisfaz $M=J\alpha$. Com $J=2\ \mathrm{kg}\cdot\mathrm{m}^2$ e $\omega=10\ \mathrm{rad/s}$, a energia de rotação é $100\ \mathrm{J}$; duplicar $J$ dá $200\ \mathrm{J}$. Duplicar $\omega$ quadruplica a energia. A energia mecânica não equivale ao consumo elétrico total.

$$
M=J\alpha,\qquad \alpha=\frac{d\omega}{dt}.
$$

$$
E=\frac{1}{2}J\omega^2.
$$

<a id="section-6"></a>

## 6. Experimentar

Num degrau ideal de 0 para 1000 rpm, alcançar cerca de 632 rpm após dois segundos sugere $\tau\approx2\ \mathrm{s}$. Ruído e amostragem podem exigir identificação mais rigorosa. Compare Euler com a solução exata no programa.

[02_first_order_response.py](../../../exercises/02_first_order_response.py) · [03_rotation_energy.py](../../../exercises/03_rotation_energy.py) · [plot_models.py](../../../exercises/plot_models.py)


<a id="section-7"></a>

## 7. Informação adicional (opcional)


### Estabilidade do método de Euler

Em cada passo, **o erro face à referência** é multiplicado por $1-\frac{dt}{\tau}$. Para haver convergência, é necessário $0<dt<2\tau$; quando $\tau<dt<2\tau$, o valor calculado oscila em torno da referência. Não significa que o motor real oscile.

### Limites do modelo

Um balanço mais geral é $J\ \frac{d\omega}{dt}=M_{\text{motor}}-M_{\text{carga}}-M_{\text{atrito}}$. $\tau=\frac{J}{K}$ só vale sob a hipótese especial $M_{\text{resultante}}=K(u-\omega)$. Carga, atrito, atrasos e limites de corrente podem alterar o comportamento.

### Energia e potência

Para $J$ constante, $\Delta E=\frac{1}{2} J(\omega_2^2-\omega_1^2)$; a potência mecânica instantânea (mechanical power) é $P=M\omega$. Tal não determina o consumo elétrico.


<a id="time-constant-derivation"></a>

### De onde vêm 63.2 %, 86.5 % e 95.0 %?

As percentagens e a exponencial resultam **da mesma equação**. Definimos o erro de velocidade como $\varepsilon(t)=u-v(t)$ (não o número de Euler). Sendo $u$ constante, $\frac{d\varepsilon}{dt}=-\frac{dv}{dt}$:

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

A separação de variáveis divide por $\varepsilon$ e, por isso, pressupõe um erro inicial diferente de zero. Se $u=v_0$, o erro permanece nulo e a equação diferencial original fornece diretamente a solução constante $v(t)=u$.

$$
f(t)=\frac{v(t)-v_0}{u-v_0}=1-\exp\!\left(-\frac{t}{\tau}\right),\qquad (u\ne v_0).
$$

| $t$ | $f(t)$ |
| ---: | ---: |
| $\tau$ | $1-\exp(-1)=0.63212056\ldots\approx63.2\ \%$ |
| $2\tau$ | $1-\exp(-2)=0.86466472\ldots\approx86.5\ \%$ |
| $3\tau$ | $1-\exp(-3)=0.95021293\ldots\approx95.0\ \%$ |

Para um degrau de 0 a 1000 rpm, obtêm-se cerca de 632, 865 e 950 rpm após uma, duas e três constantes de tempo. O modelo ideal aproxima-se assintoticamente da referência.

<a id="euler-values-derivation"></a>

### Como calcular os valores de Euler

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
