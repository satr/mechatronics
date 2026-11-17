# 公式早見表

**このページの言語を切り替える:** [en](../en/CHEATSHEET.md) · [fr](../fr/CHEATSHEET.md) · [de](../de/CHEATSHEET.md) · [it](../it/CHEATSHEET.md) · [es](../es/CHEATSHEET.md) · [pt](../pt/CHEATSHEET.md) · [zh](../zh/CHEATSHEET.md) · [ja](CHEATSHEET.md) · [nb](../nb/CHEATSHEET.md) · [ru](../ru/CHEATSHEET.md) · [ko](../ko/CHEATSHEET.md) · [fi](../fi/CHEATSHEET.md) · [pl](../pl/CHEATSHEET.md)

**このページの単位（例の前に説明）:** `s` — 秒; `m` — メートル; `m/s` — メートル / 秒 — 線速度; `rad/s` — ラジアン / 秒 — 角速度; `kg·m²` — キログラム · メートル² — 慣性モーメント; `N·m` — ニュートン · メートル — トルク; `N·m·s/rad` — ニュートン · メートル · 秒 / ラジアン — 速度に対するゲイン; `J` — ジュール; `mm` — ミリメートル = 0.001 m; `mm/s` — ミリメートル / 秒 — 線速度; `%` — パーセント（百分の一）. [単位一覧](UNITS.md).

[目次](README.md) · [運動・微分・積分](notes/01-motion-calculus.md) · [一次系の動特性と回転](notes/02-first-order-dynamics.md) · [Python 演習](exercises/README.md)

> **注意：** 本教材は AI を利用して作成されており、誤り、不正確な翻訳、誤った仮定が含まれる可能性があります。利用は自己責任で行い、数式と計算を独立に確認してください。**実機のモーターや工作機械の制御に使用しないでください。**

| 要点 | 公式早見表 |
| --- | --- |
| 変位 | $\Delta x=x_2-x_1$ |
| 移動距離 | $s=\int_{t_1}^{t_2}\lvert v(t)\rvert\ \mathrm{d}t\ge 0$ |
| 平均速度（ベクトル） | $\overline{v}=\frac{\Delta x}{\Delta t}$ |
| 平均の速さ | $\frac{s}{\Delta t}$ |
| 瞬間速度 | $v(t)=\frac{dx}{dt}$ |
| 陽的オイラー法 | $x_{n+1}=x_n+v_n\ dt$ |
| 一次遅れ系 | $\frac{dv}{dt}=\frac{u-v}{\tau}$ |
| 速度誤差（speed error） | $\varepsilon(t)=u-v(t)$ |
| 時定数 | $t=\tau$: $1-\exp(-1)\approx63.2\ \%$ |
| 正味トルク | $M=J\alpha$ |
| 慣性モーメントと比例係数 | $\tau=\frac{J}{K}$ (理想化トルクモデルに限る) |
| 回転運動エネルギー | $E=\frac{1}{2}J\omega^2$ |

**記号：** $\varepsilon$ は速度誤差（speed error）、$\mathrm{e}\approx2.71828$ はネイピア数（Euler’s number）、$\exp(z)=\mathrm{e}^{z}$ です。

**単位 (SI):**

| 記号 | 意味 | 単位（SI） |
| --- | --- | --- |
| `t, dt, τ` | 時間 (time) | 秒（s、second） |
| `x` | 位置 (position) | メートル（m、meter） |
| `v` | 速さ (speed) | メートル毎秒（m/s、meter per second） |
| `ω` | 角速度 (angular velocity) | ラジアン毎秒（rad/s、radian per second） |
| `J` | 慣性モーメント (moment of inertia) | キログラム平方メートル（kg·m²、kilogram square meter） |
| `M` | トルク (torque) | ニュートンメートル（N·m、newton meter） |
| `K` | トルクゲイン (torque gain) | ニュートンメートル秒/ラジアン（N·m·s/rad） |
| `E` | エネルギー (energy) | ジュール（J、joule） |

中黒 `·` は単位の積を表し、列挙する読点ではありません。目標値 $u$ は直線モデルでは速度、回転モデルでは角速度です。

## 注意事項

速さと向きを含む速度、移動距離と変位、$dt$ と $\tau$ を混同しないでください。$\tau=\frac{J}{K}$ は明示したトルクモデルの仮定に限られます。機械的エネルギーは電力消費量と同じではありません。

**英語の専門用語：**

- 移動距離 (distance traveled)
- 変位 (displacement)
- 速さ (speed)
- 速度ベクトル (velocity)
- 導関数 (derivative)
- 積分 (integral)
- 数値積分 (numerical integration)
- 陽的オイラー法 (explicit Euler method)

**英語の専門用語：**

- 一次系 (first-order system)
- 時定数 (time constant)
- 時間刻み (time step)
- 慣性モーメント (moment of inertia)
- トルク (torque)
- 制御器ゲイン (controller gain)
- 角加速度 (angular acceleration)
- システム同定 (system identification)
- 回転運動エネルギー (rotational kinetic energy)

詳しくは[微分と積分の説明](notes/01-motion-calculus.md#section-6)、[モデルの仮定と安定性](notes/02-first-order-dynamics.md#section-7)を参照してください。


[これらの割合はどう求める？ 計算を参照。](notes/02-first-order-dynamics.md#time-constant-derivation)

[3、3.8、3.98 の計算を参照。](notes/01-motion-calculus.md#motion-values-derivation)


## 数式の記号と表記

**Σ / ∑（総和 / summation）** は項の和です。例えば $\sum_{n=1}^{3}n=1+2+3=6$。[他の記号](SYMBOLS.md)。


## 積分公式表

[0. 微積分の基礎：導関数・微分・積分](notes/00-calculus-foundations.md) · [積分公式表](INTEGRAL_TABLE.md)


## フィードバック制御：PID と保持トルク

| $\varepsilon=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}}$ | $u_P=K_p\varepsilon$, $u_I=K_i\int\varepsilon\ \mathrm{d}t$ |
| --- | --- |
| $M_{\mathrm{motor}}=K_t I$ | $\lvert M_g\rvert=mgL\lvert\cos\theta\rvert$ |

[フィードバック制御：PID と保持トルク](notes/03-feedback-control.md) · [三角関数表と力学の例](TRIGONOMETRY.md)

<a id="joint-velocity"></a>
## 回転、速度、ヤコビ行列

角速度は rad/s、長さが mm の場合、線速度は mm/s です。

$$
v_x=-L\sin Q\cdot\dot Q,\qquad v_y=L\cos Q\cdot\dot Q
$$

$$
\det J=L_1L_2\sin Q_2
$$

[回転、速度、ヤコビ行列](notes/05-velocity-jacobian.md)
