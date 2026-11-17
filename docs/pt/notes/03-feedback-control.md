# 3. Controlo por realimentação: PID, amostragem e binário de sustentação

**Idiomas:** [en](../../en/notes/03-feedback-control.md) · [fr](../../fr/notes/03-feedback-control.md) · [de](../../de/notes/03-feedback-control.md) · [it](../../it/notes/03-feedback-control.md) · [es](../../es/notes/03-feedback-control.md) · [pt](03-feedback-control.md) · [zh](../../zh/notes/03-feedback-control.md) · [ja](../../ja/notes/03-feedback-control.md) · [nb](../../nb/notes/03-feedback-control.md) · [ru](../../ru/notes/03-feedback-control.md) · [ko](../../ko/notes/03-feedback-control.md) · [fi](../../fi/notes/03-feedback-control.md) · [pl](../../pl/notes/03-feedback-control.md)

**Unidades aqui utilizadas (explicadas antes dos exemplos):** `rpm` — rotação por minuto; `A` — ampere; `s` — segundo; `rpm/s` — rotação por minuto / segundo — aceleração angular; `A/rpm` — ampere / (rotação por minuto) — ganho por velocidade; `A/(rpm·s)` — ampere / (rotação por minuto · segundo) — ganho integral; `A·s/rpm` — ampere · segundo / (rotação por minuto) — ganho derivativo; `N·m` — newton · metro — binário (torque); `kg` — quilograma; `m` — metro; `N` — newton. [Glossário de unidades](../UNITS.md).

[README](../README.md) · [Math foundations](00-calculus-foundations.md) · [First-order dynamics](02-first-order-dynamics.md) · [Trigonometry](../TRIGONOMETRY.md)

> **Modelo educativo:** Não ligue estes algoritmos simplificados a motores nem a máquinas reais.

## Conteúdo

- [1. Controlo fechado de velocidade](#section-1)
- [2. P: ação proporcional](#section-2)
- [3. I: erro acumulado e referência de corrente](#section-3)
- [4. D: variação do erro e ruído do sensor](#section-4)
- [5. Amostragem, saturação e anti-windup](#section-5)
- [6. Sustentar uma articulação sob gravidade](#section-6)
- [7. Verificações e limitações](#section-7)

<a id="section-1"></a>
## 1. Controlo fechado de velocidade

Um **controlador realimentado (feedback controller)** compara referência e medição. Para 1000 rpm desejadas e 950 rpm medidas, o erro é +50 rpm. Neste exemplo o PID produz uma **referência de corrente geradora de binário**, não uma variação a adicionar à corrente anterior.

$$
\varepsilon(t)=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}},
\qquad I_{\mathrm{set}}=u_P+u_I+u_D.
$$

O acionamento pode incluir uma malha interna de corrente que altera a tensão ou PWM. Outros sistemas usam referência de binário, tensão ou PWM; não se deve assumir corrente como interface universal.

<a id="section-2"></a>
## 2. P: ação proporcional

**P (proportional)** reage ao erro **atual**. Sem feedforward ou deslocamento de comando, a carga constante exige binário e corrente diferentes de zero. Com erro exatamente zero, P é zero; pode existir **erro estacionário (steady-state error)**.

$$
u_P=K_p\varepsilon,\quad [K_p]=\mathrm{A/rpm}.
$$

<a id="section-3"></a>
## 3. I: erro acumulado e referência de corrente

**I (integral)** acumula o erro no tempo numa única variável, sem guardar a lista de erros anteriores. Erro positivo aumenta, zero mantém, negativo diminui. Pode continuar a pedir corrente mesmo com velocidade correta.

$$
z(t)=\int_0^t\varepsilon(s)\ \mathrm{d}s,\quad u_I=K_i z(t),\quad [K_i]=\mathrm{A/(rpm\cdot s)}.
$$

```python
integral = 0.0  # saved between controller iterations
for speed in [950, 950, 950, 1000, 1020, 1020]:
    error = 1000 - speed       # rpm
    integral += error * 1.0   # rpm*s; dt = 1 s
    p_command = 0.02 * error # amperes
    i_command = 0.002 * integral # amperes
    current_setpoint = p_command + i_command
    print(round(integral), round(i_command, 2), round(current_setpoint, 2))
```

Com dt = 1 s, Kp = 0.02 A/rpm e Ki = 0.002 A/(rpm·s), três amostras com erro +50 rpm dão 50, 100, 150 rpm·s e I = 0.10, 0.20, 0.30 A. Erro zero conserva 0.30 A; −20 rpm durante 1 s reduz para 0.26 A, mais um segundo para 0.22 A. −0.04 A é a **mudança por passo**, não a referência absoluta.

O programa imprime apenas o integral acumulado, a parcela I e a referência total de corrente. A tabela acrescenta o erro e a parcela P para tornar cada passo verificável. As amostras estão separadas por 1 s e o integral começa em zero.

| k | Velocidade medida (rpm) | ε (rpm) | z (rpm·s) | u_P (A) | u_I (A) | I_set (A) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 950 | +50 | 50 | +1.00 | +0.10 | +1.10 |
| 2 | 950 | +50 | 100 | +1.00 | +0.20 | +1.20 |
| 3 | 950 | +50 | 150 | +1.00 | +0.30 | +1.30 |
| 4 | 1000 | 0 | 150 | 0.00 | +0.30 | +0.30 |
| 5 | 1020 | −20 | 130 | −0.40 | +0.26 | −0.14 |
| 6 | 1020 | −20 | 110 | −0.40 | +0.22 | −0.18 |

A 1020 rpm, o erro é −20 rpm: P vale −0.40 A e I ainda é +0.26 A. A soma é uma **referência de corrente com sinal de −0.14 A** e passa a −0.18 A na amostra seguinte. A mudança da parcela I (−0.04 A por passo) não é a referência total. Estes valores são apenas do modelo didático, não configurações de equipamento real.

<a id="section-4"></a>
## 4. D: variação do erro e ruído do sensor

**D (derivative)** responde à **taxa de variação do erro**. Com referência constante, quando o motor acelera o erro diminui, e a contribuição D negativa pode reduzir o overshoot. D não é a própria velocidade. Um salto de medição de 8 rpm em 0.01 s aparenta 800 rpm/s.

$$
u_D=K_d\frac{\mathrm{d}\varepsilon}{\mathrm{d}t},\quad [K_d]=\mathrm{A\cdot s/rpm},\qquad
\frac{\Delta\omega}{\Delta t}=\frac{8\ \mathrm{rpm}}{0.01\ \mathrm{s}}=800\ \mathrm{rpm/s}.
$$

A derivada do erro tem unidades rpm/s. Como a contribuição D é um valor pedido de corrente em A, o ganho `K_d` tem de compensar rpm/s: as suas unidades são A·s/rpm e o produto fica em A.

A **filtragem da derivada (derivative filtering)** reduz ruído rápido, mas acrescenta atraso. Costuma derivar-se a medição, não o setpoint, para evitar impulsos no comando.

<a id="section-5"></a>
## 5. Amostragem, saturação e anti-windup

O **período de amostragem (sampling period)** importa: erro constante 20 rpm, 100 passos de 0.01 s ou 10 de 0.1 s acumulam 20 rpm·s em 1 s. Sem dt, o controlador rápido acumula dez vezes mais.

$$
z_{k+1}=z_k+\varepsilon_k\ \Delta t.
$$

Se o comando exceder o limite de corrente, I pode continuar a crescer: **integral windup**, com possível overshoot quando a carga diminuir. **Anti-windup** interrompe a acumulação que agrava a saturação ou corrige o estado pela saída aplicada. O limite é para a referência **total**, incluindo P.

<a id="section-6"></a>
## 6. Sustentar uma articulação sob gravidade

A **constante de binário Kt (motor torque constant)** é binário por ampere de corrente geradora de binário, em N·m/A. Com Kt = 0.1 N·m/A e 2 A obtêm-se 0.2 N·m, segundo a convenção do fabricante.

$$
M_{\mathrm{motor}}=K_t I,\qquad [K_t]=\mathrm{N\cdot m/A}.
$$

Uma massa m à distância L do eixo horizontal produz binário gravitacional de módulo mgL|cos θ|. Em equilíbrio, os momentos motor e carga são opostos; pode ser necessária corrente mesmo com erro de posição zero. Um travão ou transmissão verdadeiramente autoblocante pode sustentar sem corrente; **Harmonic Drive** não é intrinsecamente autoblocante.

$$
J\alpha=M_{\mathrm{motor}}+M_{\mathrm{load}},\quad
\alpha=0\ \Longrightarrow\ M_{\mathrm{motor}}=-M_{\mathrm{load}},
$$
$$
|M_g|=mgL|\cos\theta|.
$$

Num BLDC **outrunner** gira a carcaça exterior; num **inrunner** gira o rotor interior. Rotor é parte móvel e estator é parte fixa.

<a id="section-7"></a>
## 7. Verificações e limitações

As correntes são valores didáticos, não configurações de equipamento real. São necessárias proteções, limites, filtragem, calibração e testes seguros.

[Math foundation](00-calculus-foundations.md) · [Trigonometry table](../TRIGONOMETRY.md) · [First-order dynamics](02-first-order-dynamics.md)
