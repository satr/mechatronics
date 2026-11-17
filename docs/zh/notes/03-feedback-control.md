# 3. 反馈控制：PID、采样、饱和与保持转矩

**语言:** [en](../../en/notes/03-feedback-control.md) · [fr](../../fr/notes/03-feedback-control.md) · [de](../../de/notes/03-feedback-control.md) · [it](../../it/notes/03-feedback-control.md) · [es](../../es/notes/03-feedback-control.md) · [pt](../../pt/notes/03-feedback-control.md) · [zh](03-feedback-control.md) · [ja](../../ja/notes/03-feedback-control.md) · [nb](../../nb/notes/03-feedback-control.md) · [ru](../../ru/notes/03-feedback-control.md) · [ko](../../ko/notes/03-feedback-control.md) · [fi](../../fi/notes/03-feedback-control.md) · [pl](../../pl/notes/03-feedback-control.md)

**本页使用的单位（示例前先解释）:** `rpm` — 每分钟转数; `A` — 安培; `s` — 秒; `rpm/s` — 每分钟转数 / 秒 — 角加速度; `A/rpm` — 安培 / (每分钟转数) — 速度增益; `A/(rpm·s)` — 安培 / (每分钟转数 · 秒) — 积分增益; `A·s/rpm` — 安培 · 秒 / (每分钟转数) — 微分增益; `N·m` — 牛顿 · 米 — 转矩; `kg` — 千克; `m` — 米; `N` — 牛顿. [完整单位表](../UNITS.md).

[README](../README.md) · [Math foundations](00-calculus-foundations.md) · [First-order dynamics](02-first-order-dynamics.md) · [Trigonometry](../TRIGONOMETRY.md)

> **教学模型:** 不要将这些简化的算法连接到真实电机或机械设备。

## 目录

- [1. 闭环速度控制](#section-1)
- [2. P：比例响应](#section-2)
- [3. I：累计误差与电流设定值](#section-3)
- [4. D：误差变化率与传感器噪声](#section-4)
- [5. 采样周期、饱和与抗积分饱和](#section-5)
- [6. 克服重力保持机器人关节](#section-6)
- [7. 验证与限制](#section-7)

<a id="section-1"></a>
## 1. 闭环速度控制

**反馈控制器（feedback controller）**比较设定值与传感器测量值。目标 1000 rpm、实测 950 rpm 时误差为 +50 rpm。在此例中，PI/PID 输出的是**产生转矩的电流设定值**，不是在上一次电流基础上增加多少安培。

$$
\varepsilon(t)=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}},
\qquad I_{\mathrm{set}}=u_P+u_I+u_D.
$$

驱动器可以有内部电流环，通过调整电压或 PWM 跟踪电流设定。其他系统可能输出转矩、电压或 PWM，因此不能假设所有驱动器接口都是电流设定值。

<a id="section-2"></a>
## 2. P：比例响应

**P（proportional）**根据**当前**误差立即改变命令。在没有前馈（feedforward）或固定补偿的简化模型中，恒定负载需要非零转矩与电流。误差为零时 P 输出为零，因此仅有 P 可能留下**稳态误差（steady-state error）**。

$$
u_P=K_p\varepsilon,\quad [K_p]=\mathrm{A/rpm}.
$$

<a id="section-3"></a>
## 3. I：累计误差与电流设定值

**I（integral）**随时间累计误差。它保存一个状态变量，并非全部历史记录。正误差使其增大，零误差保持，负误差使其减少。因此达到目标速度后它仍可保持非零电流设定值。

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

例：dt = 1 s、Kp = 0.02 A/rpm、Ki = 0.002 A/(rpm·s)。连续三个 +50 rpm 误差使积分状态依次为 50、100、150 rpm·s，I 部分为 0.10、0.20、0.30 A。误差为零时仍为 0.30 A；接着每秒误差为 −20 rpm，依次变成 0.26 A、0.22 A。−0.04 A 是**每步的变化量**，不是新的绝对设定值。

程序输出累积积分、I 项以及总电流设定值。下表再列出误差和 P 项，方便逐步核对计算。相邻采样间隔为 1 s，积分初值为零。

| k | 测得转速 (rpm) | ε (rpm) | z (rpm·s) | u_P (A) | u_I (A) | I_set (A) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 950 | +50 | 50 | +1.00 | +0.10 | +1.10 |
| 2 | 950 | +50 | 100 | +1.00 | +0.20 | +1.20 |
| 3 | 950 | +50 | 150 | +1.00 | +0.30 | +1.30 |
| 4 | 1000 | 0 | 150 | 0.00 | +0.30 | +0.30 |
| 5 | 1020 | −20 | 130 | −0.40 | +0.26 | −0.14 |
| 6 | 1020 | −20 | 110 | −0.40 | +0.22 | −0.18 |

测得速度为 1020 rpm 时，误差为 −20 rpm：P 项是 −0.40 A，而 I 项仍为 +0.26 A，合计得到**带符号的总电流设定值 −0.14 A**；下一步为 −0.18 A。I 项每步变化 −0.04 A，并不等于完整的电流指令。这些数值仅用于教学模型，不能作为真实驱动器的设置。

<a id="section-4"></a>
## 4. D：误差变化率与传感器噪声

**D（derivative）**根据**误差变化率**工作。目标速度不变而实际速度加快时，误差减少，负的 D 部分可缓解超调（overshoot）。D 并不是速度本身。测量值在 0.01 s 跳变 8 rpm，会产生虚假的 800 rpm/s 变化率。

$$
u_D=K_d\frac{\mathrm{d}\varepsilon}{\mathrm{d}t},\quad [K_d]=\mathrm{A\cdot s/rpm},\qquad
\frac{\Delta\omega}{\Delta t}=\frac{8\ \mathrm{rpm}}{0.01\ \mathrm{s}}=800\ \mathrm{rpm/s}.
$$

误差的时间导数单位为 rpm/s。由于 D 项输出的是单位为 A 的电流指令，因此增益 `K_d` 必须抵消 rpm/s，其单位应为 A·s/rpm，两者相乘后单位仍为 A。

**微分滤波（derivative filtering）**能降低高频噪声，但过强会引入延迟。实际算法常对测量值而不是设定值求导，以避免设定值突变时出现 D 脉冲。

<a id="section-5"></a>
## 5. 采样周期、饱和与抗积分饱和

数字控制器具有**采样周期（sampling period）**。恒定误差 20 rpm 持续 1 s，100 个 dt = 0.01 s 步与 10 个 dt = 0.1 s 步都累计 20 rpm·s。若漏乘 dt，采样更快的控制器就会多累计十倍。

$$
z_{k+1}=z_k+\varepsilon_k\ \Delta t.
$$

执行器有电流限幅。若达到限幅后积分继续累加，会产生**积分饱和（integral windup）**，负载减小后可能严重超调。**抗积分饱和（anti-windup）**可禁止使限幅更严重的累加，或根据请求与实际执行命令的差值修正内部状态。需要限制包含 P 在内的**总命令**。

<a id="section-6"></a>
## 6. 克服重力保持机器人关节

**转矩常数 Kt（motor torque constant）**表示每安培产生的转矩，单位 N·m/A。若 Kt = 0.1 N·m/A、电流 2 A，则转矩为 0.2 N·m；应遵守厂商对电流类型的定义。

$$
M_{\mathrm{motor}}=K_t I,\qquad [K_t]=\mathrm{N\cdot m/A}.
$$

质量 m 的载荷在水平关节轴外 L 处、杠杆与水平夹角 θ 时，重力矩大小为 mgL|cos θ|。静止保持时电机转矩与负载转矩应符号相反、合力矩为零。因此即使位置误差为零，保持位置仍可能需要电流。机械制动器或确实自锁的机构可能无需电流；**Harmonic Drive** 并非天然自锁。

$$
J\alpha=M_{\mathrm{motor}}+M_{\mathrm{load}},\quad
\alpha=0\ \Longrightarrow\ M_{\mathrm{motor}}=-M_{\mathrm{load}},
$$
$$
|M_g|=mgL|\cos\theta|.
$$

BLDC 的 **outrunner** 旋转外壳，**inrunner** 旋转内部转子。转子指旋转部分，定子指固定部分，与径向位置无关。

<a id="section-7"></a>
## 7. 验证与限制

所有电流数值均为教学示例，不是实际设备参数。真实驱动器需要合理限幅、滤波、编码器校准、热保护及安全验证。

[Math foundation](00-calculus-foundations.md) · [Trigonometry table](../TRIGONOMETRY.md) · [First-order dynamics](02-first-order-dynamics.md)
