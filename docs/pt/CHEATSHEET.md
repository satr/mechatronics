# Resumo de fórmulas

**Ler esta página em:** [en](../en/CHEATSHEET.md) · [fr](../fr/CHEATSHEET.md) · [de](../de/CHEATSHEET.md) · [it](../it/CHEATSHEET.md) · [es](../es/CHEATSHEET.md) · [pt](CHEATSHEET.md) · [zh](../zh/CHEATSHEET.md) · [ja](../ja/CHEATSHEET.md) · [nb](../nb/CHEATSHEET.md) · [ru](../ru/CHEATSHEET.md) · [ko](../ko/CHEATSHEET.md) · [fi](../fi/CHEATSHEET.md) · [pl](../pl/CHEATSHEET.md)

**Unidades aqui utilizadas (explicadas antes dos exemplos):** `s` — segundo; `m` — metro; `m/s` — metro / segundo — velocidade linear; `rad/s` — radiano / segundo — velocidade angular; `kg·m²` — quilograma · metro² — momento de inércia; `N·m` — newton · metro — binário (torque); `N·m·s/rad` — newton · metro · segundo / radiano — ganho por velocidade; `J` — joule; `mm` — milímetro = 0.001 m; `mm/s` — milímetro / segundo — velocidade linear; `%` — percentagem (uma centésima parte). [Glossário de unidades](UNITS.md).

[Índice](README.md) · [Movimento, derivadas e integrais](notes/01-motion-calculus.md) · [Dinâmica de primeira ordem e rotação](notes/02-first-order-dynamics.md) · [Exercícios Python](exercises/README.md)

> **Aviso:** Este material educativo com assistência de IA pode conter erros, traduções imprecisas ou pressupostos incorretos. A utilização é por conta e risco de quem o consulta. Confirme os cálculos de forma independente e nunca utilize os exemplos para controlar máquinas reais.

| Revisão rápida | Resumo de fórmulas |
| --- | --- |
| Deslocamento | $\Delta x=x_2-x_1$ |
| Distância percorrida | $s=\int_{t_1}^{t_2}\lvert v(t)\rvert\ \mathrm{d}t\ge 0$ |
| Velocidade vetorial média | $\overline{v}=\frac{\Delta x}{\Delta t}$ |
| Rapidez média | $\frac{s}{\Delta t}$ |
| Velocidade instantânea | $v(t)=\frac{dx}{dt}$ |
| Método de Euler | $x_{n+1}=x_n+v_n\ dt$ |
| Dinâmica de primeira ordem | $\frac{dv}{dt}=\frac{u-v}{\tau}$ |
| Erro de velocidade | $\varepsilon(t)=u-v(t)$ |
| Constante de tempo | $t=\tau$: $1-\exp(-1)\approx63.2\ \%$ |
| Binário resultante | $M=J\alpha$ |
| Inércia e ganho | $\tau=\frac{J}{K}$ (Apenas no modelo idealizado de binário) |
| Energia cinética de rotação | $E=\frac{1}{2}J\omega^2$ |

**Notação:** $\varepsilon$ é o erro de velocidade (speed error); $\mathrm{e}\approx2.71828$ é o número de Euler (Euler’s number); $\exp(z)=\mathrm{e}^{z}$.

**Unidades (SI):**

| Símbolo | Grandeza | Unidade SI |
| --- | --- | --- |
| `t, dt, τ` | Tempo | s (second) |
| `x` | Posição | m (meter) |
| `v` | Velocidade | m/s (meter per second) |
| `ω` | Velocidade angular | rad/s (radian per second) |
| `J` | Momento de inércia | kg·m² (kilogram square meter) |
| `M` | Binário | N·m (newton meter) |
| `K` | Ganho do binário | N·m·s/rad |
| `E` | Energia | J (joule) |

O ponto `·` representa multiplicação. A referência $u$ é velocidade linear ou angular, conforme o modelo.

## Avisos

Não confundir rapidez com velocidade vetorial, distância com deslocamento, nem $dt$ com $\tau$. A expressão $\tau=\frac{J}{K}$ só vale para o modelo indicado; energia mecânica não é consumo elétrico.

**Termos ingleses:**

- distância percorrida (distance traveled)
- deslocamento (displacement)
- rapidez (speed)
- velocidade vetorial (velocity)
- derivada (derivative)
- integral (integral)
- integração numérica (numerical integration)
- método de Euler explícito (explicit Euler method)

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

Para aprofundar: [derivadas](notes/01-motion-calculus.md#section-6) e [limites do modelo](notes/02-first-order-dynamics.md#section-7).


[Por que exatamente essas percentagens? Veja o cálculo.](notes/02-first-order-dynamics.md#time-constant-derivation)

[Cálculo de 3; 3.8 e 3.98.](notes/01-motion-calculus.md#motion-values-derivation)


## Símbolos e notação

**Σ / ∑ (somatório / summation)** soma vários termos: $\sum_{n=1}^{3}n=1+2+3=6$. [Outros símbolos](SYMBOLS.md).


## Tabela de integrais

[0. Fundamentos de derivadas, diferenciais e integrais](notes/00-calculus-foundations.md) · [Tabela de integrais](INTEGRAL_TABLE.md)


## Controlo por realimentação: PID e binário de sustentação

| $\varepsilon=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}}$ | $u_P=K_p\varepsilon$, $u_I=K_i\int\varepsilon\ \mathrm{d}t$ |
| --- | --- |
| $M_{\mathrm{motor}}=K_t I$ | $\lvert M_g\rvert=mgL\lvert\cos\theta\rvert$ |

[Controlo por realimentação: PID e binário de sustentação](notes/03-feedback-control.md) · [Tabela trigonométrica e exemplos mecânicos](TRIGONOMETRY.md)

<a id="joint-velocity"></a>
## Rotação, velocidade e jacobiano

Velocidades angulares em rad/s e velocidades lineares em mm/s para comprimentos em mm.

$$
v_x=-L\sin Q\cdot\dot Q,\qquad v_y=L\cos Q\cdot\dot Q
$$

$$
\det J=L_1L_2\sin Q_2
$$

[Rotação, velocidade e jacobiano](notes/05-velocity-jacobian.md)
