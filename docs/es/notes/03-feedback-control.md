# 3. Control realimentado: PID, muestreo, saturación y par de sujeción

**Idiomas:** [en](../../en/notes/03-feedback-control.md) · [fr](../../fr/notes/03-feedback-control.md) · [de](../../de/notes/03-feedback-control.md) · [it](../../it/notes/03-feedback-control.md) · [es](03-feedback-control.md) · [pt](../../pt/notes/03-feedback-control.md) · [zh](../../zh/notes/03-feedback-control.md) · [ja](../../ja/notes/03-feedback-control.md) · [nb](../../nb/notes/03-feedback-control.md) · [ru](../../ru/notes/03-feedback-control.md) · [ko](../../ko/notes/03-feedback-control.md) · [fi](../../fi/notes/03-feedback-control.md) · [pl](../../pl/notes/03-feedback-control.md)

**Unidades empleadas aquí (definidas antes de los ejemplos):** `rpm` — revolución por minuto; `A` — amperio; `s` — segundo; `rpm/s` — revolución por minuto / segundo — aceleración angular; `A/rpm` — amperio / (revolución por minuto) — ganancia por velocidad; `A/(rpm·s)` — amperio / (revolución por minuto · segundo) — ganancia integral; `A·s/rpm` — amperio · segundo / (revolución por minuto) — ganancia derivativa; `N·m` — newton · metro — par de torsión; `kg` — kilogramo; `m` — metro; `N` — newton. [Glosario de unidades](../UNITS.md).

[README](../README.md) · [Math foundations](00-calculus-foundations.md) · [First-order dynamics](02-first-order-dynamics.md) · [Trigonometry](../TRIGONOMETRY.md)

> **Modelo educativo:** No conecte estos algoritmos simplificados a motores ni máquinas reales.

## Contenido

- [1. Control de velocidad en lazo cerrado](#section-1)
- [2. P: acción proporcional](#section-2)
- [3. I: error acumulado y consigna de corriente](#section-3)
- [4. D: variación del error y ruido del sensor](#section-4)
- [5. Muestreo, saturación y anti-windup](#section-5)
- [6. Sujeción de una articulación bajo gravedad](#section-6)
- [7. Comprobaciones y límites](#section-7)

<a id="section-1"></a>
## 1. Control de velocidad en lazo cerrado

Un **controlador realimentado (feedback controller)** compara consigna y medición. Con 1000 rpm deseadas y 950 rpm medidas, error +50 rpm. En este ejemplo PID emite una **consigna de corriente que genera par**, no una orden de sumar amperios al valor anterior.

$$
\varepsilon(t)=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}},
\qquad I_{\mathrm{set}}=u_P+u_I+u_D.
$$

El accionamiento puede tener un lazo interno de corriente que ajusta tensión o PWM. Otros sistemas entregan par, tensión o PWM; la consigna de corriente no es universal.

<a id="section-2"></a>
## 2. P: acción proporcional

**P (proportional)** responde al error **actual**. Sin feedforward ni sesgo, una carga constante exige par y corriente distintos de cero. Si el error es cero, P emite cero; puede quedar **error estacionario (steady-state error)**.

$$
u_P=K_p\varepsilon,\quad [K_p]=\mathrm{A/rpm}.
$$

<a id="section-3"></a>
## 3. I: error acumulado y consigna de corriente

**I (integral)** acumula el error con el tiempo en un único estado, no guarda una lista histórica. Error positivo: aumenta; cero: mantiene; negativo: disminuye. Puede mantener corriente con velocidad correcta.

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

Con dt = 1 s, Kp = 0.02 A/rpm y Ki = 0.002 A/(rpm·s), tres muestras con error +50 rpm dan 50, 100, 150 rpm·s e I = 0.10, 0.20, 0.30 A. Error cero mantiene 0.30 A; −20 rpm durante 1 s lleva a 0.26 A y otro segundo a 0.22 A. −0.04 A es el **cambio por paso**, no la nueva consigna absoluta.

El programa muestra la integral acumulada, el término I y la consigna total de corriente. La tabla añade el error y el término P para poder comprobar cada paso. Las muestras están separadas por 1 s y la integral empieza en cero.

| k | Velocidad medida (rpm) | ε (rpm) | z (rpm·s) | u_P (A) | u_I (A) | I_set (A) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 950 | +50 | 50 | +1.00 | +0.10 | +1.10 |
| 2 | 950 | +50 | 100 | +1.00 | +0.20 | +1.20 |
| 3 | 950 | +50 | 150 | +1.00 | +0.30 | +1.30 |
| 4 | 1000 | 0 | 150 | 0.00 | +0.30 | +0.30 |
| 5 | 1020 | −20 | 130 | −0.40 | +0.26 | −0.14 |
| 6 | 1020 | −20 | 110 | −0.40 | +0.22 | −0.18 |

A 1020 rpm el error es −20 rpm: P vale −0.40 A, mientras que I todavía vale +0.26 A. Su suma es una **consigna con signo de −0.14 A**; en el paso siguiente es −0.18 A. El cambio del término I (−0.04 A por paso) no es la consigna total. Son valores del modelo didáctico, no ajustes de un accionamiento real.

<a id="section-4"></a>
## 4. D: variación del error y ruido del sensor

**D (derivative)** responde a la **velocidad de cambio del error**. Con consigna fija, un motor que acelera reduce el error y genera un aporte D negativo capaz de reducir el overshoot. D no es la velocidad. Un salto de medición de 8 rpm en 0.01 s aparenta 800 rpm/s.

$$
u_D=K_d\frac{\mathrm{d}\varepsilon}{\mathrm{d}t},\quad [K_d]=\mathrm{A\cdot s/rpm},\qquad
\frac{\Delta\omega}{\Delta t}=\frac{8\ \mathrm{rpm}}{0.01\ \mathrm{s}}=800\ \mathrm{rpm/s}.
$$

La derivada del error tiene unidades rpm/s. Como la contribución D es una consigna de corriente en A, la ganancia `K_d` debe compensar rpm/s: sus unidades son A·s/rpm y el producto se expresa en A.

El **filtrado derivativo (derivative filtering)** reduce ruido rápido, pero añade retardo. A menudo se deriva la medida en vez de la consigna para evitar una reacción brusca por cambios de referencia.

<a id="section-5"></a>
## 5. Muestreo, saturación y anti-windup

El **período de muestreo (sampling period)** importa: con error constante 20 rpm, 100 pasos de 0.01 s o 10 de 0.1 s acumulan ambos 20 rpm·s en 1 s. Si se olvida dt, el controlador rápido acumula diez veces más.

$$
z_{k+1}=z_k+\varepsilon_k\ \Delta t.
$$

Con corriente limitada, la petición puede superar el máximo. Si I sigue aumentando aparece **integral windup**, y puede haber overshoot cuando disminuye la carga. **Anti-windup** bloquea el aumento que empeora la saturación o corrige el estado según la salida aplicada. Se debe limitar la consigna **total**, incluida P.

<a id="section-6"></a>
## 6. Sujeción de una articulación bajo gravedad

La **constante de par Kt (motor torque constant)** define par por amperio de corriente generadora de par, en N·m/A. Con Kt = 0.1 N·m/A y 2 A se obtienen 0.2 N·m, respetando la convención del fabricante.

$$
M_{\mathrm{motor}}=K_t I,\qquad [K_t]=\mathrm{N\cdot m/A}.
$$

Una masa m a distancia L de una articulación horizontal genera par gravitatorio de módulo mgL|cos θ|. Para equilibrio, par motor y par de carga tienen signos contrarios; puede necesitarse corriente aun con error de posición nulo. Un freno o transmisión realmente autoblocante puede mantener sin corriente; **Harmonic Drive** no garantiza autobloqueo.

$$
J\alpha=M_{\mathrm{motor}}+M_{\mathrm{load}},\quad
\alpha=0\ \Longrightarrow\ M_{\mathrm{motor}}=-M_{\mathrm{load}},
$$
$$
|M_g|=mgL|\cos\theta|.
$$

En BLDC **outrunner** gira la carcasa externa; en **inrunner**, el rotor interior. Rotor significa parte móvil y estator, parte fija.

<a id="section-7"></a>
## 7. Comprobaciones y límites

Los valores de corriente son ilustrativos; no son ajustes para hardware real. Se requieren protecciones, límites, filtrado, calibración y pruebas seguras.

[Math foundation](00-calculus-foundations.md) · [Trigonometry table](../TRIGONOMETRY.md) · [First-order dynamics](02-first-order-dynamics.md)
