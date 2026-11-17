# 2. 一次系の動特性と回転


**このページの言語を切り替える:** [en](../../en/notes/02-first-order-dynamics.md) · [fr](../../fr/notes/02-first-order-dynamics.md) · [de](../../de/notes/02-first-order-dynamics.md) · [it](../../it/notes/02-first-order-dynamics.md) · [es](../../es/notes/02-first-order-dynamics.md) · [pt](../../pt/notes/02-first-order-dynamics.md) · [zh](../../zh/notes/02-first-order-dynamics.md) · [ja](02-first-order-dynamics.md) · [nb](../../nb/notes/02-first-order-dynamics.md) · [ru](../../ru/notes/02-first-order-dynamics.md) · [ko](../../ko/notes/02-first-order-dynamics.md) · [fi](../../fi/notes/02-first-order-dynamics.md) · [pl](../../pl/notes/02-first-order-dynamics.md)

**このページの単位（例の前に説明）:** `s` — 秒; `mm/s` — ミリメートル / 秒 — 線速度; `kg` — キログラム; `m` — メートル; `rad/s` — ラジアン / 秒 — 角速度; `N` — ニュートン; `N·m` — ニュートン · メートル — トルク; `J` — ジュール; `rpm` — 毎分回転数; `kg·m²` — キログラム · メートル² — 慣性モーメント; `N·m·s/rad` — ニュートン · メートル · 秒 / ラジアン — 速度に対するゲイン; `%` — パーセント（百分の一）; `rad` — ラジアン. [単位一覧](../UNITS.md).

**基礎:** [0. 微積分の基礎：導関数・微分・積分](00-calculus-foundations.md) · [積分公式表](../INTEGRAL_TABLE.md)

[README](../README.md) · [公式早見表](../CHEATSHEET.md) · [Python 演習](../exercises/README.md) · [運動・微分・積分](01-motion-calculus.md)

> **注意：** 本教材は AI を利用して作成されており、誤り、不正確な翻訳、誤った仮定が含まれる可能性があります。利用は自己責任で行い、数式と計算を独立に確認してください。**実機のモーターや工作機械の制御に使用しないでください。**

> **モーターモデルの仮定：** 理想的な比例トルク制御を想定し、負荷、摩擦、遅延、電圧制限、飽和、高次の動特性を考慮しません。すべてのモーターに当てはまる一般的な説明ではありません。

## 要点

時定数 $\tau$ は、一次系が新しい定常状態に近づく速さを表します。シミュレーションの刻み $dt$ は計算精度に関係し、物理モデル自体の性質ではありません。仮定した理想モデルでは $\tau=\frac{J}{K}$ です。同じ時定数でも必要なトルクやエネルギーは異なり得ます。

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

## このページの目次

- [1. 一次系の応答](#section-1)
- [2. トルクと慣性](#section-2)
- [3. 刻み幅と時定数](#section-3)
- [4. 計測値から時定数を推定する](#section-4)
- [5. 回転エネルギー](#section-5)
- [6. 演習](#section-6)
- [7. 発展的な説明（任意）](#section-7)
  - [63.2 %、86.5 %、95.0 % の由来](#time-constant-derivation)
  - [オイラー法の数値の導出](#euler-values-derivation)

**単位の説明（units）：** 時定数は秒（s、second）、角速度はラジアン毎秒（rad/s、radian per second）、トルクはニュートンメートル（N·m、newton meter）です。詳しくは[公式早見表](../CHEATSHEET.md)を参照してください。

[SI 単位と小数点の説明](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. 一次系の応答

単位、導出、数値計算上の注意点は[発展的な説明](#section-7)を参照してください。

目標速度 $u$ が一定、実速度が $v$、$\tau>0$ の場合、変化量の約 $63.2\ \%$ が $\tau$ 後に、$86.5\ \%$ が $2\tau$ 後に、$95.0\ \%$ が $3\tau$ 後に達成されます。**時刻 $t=\tau$ で目標に完全到達するという意味ではありません。**

**記号について：** $\varepsilon(t)=u-v(t)$ は速度誤差（speed error、ギリシャ文字のイプシロン）です。自然指数関数（exponential function）は $\exp(z)=\mathrm{e}^{z}$ と書き、$\mathrm{e}\approx2.71828$ はネイピア数（Euler’s number）であり、**速度誤差ではありません**。[導出と 63.2 % の計算を見る](#time-constant-derivation)。

$$
\frac{dv}{dt}=\frac{u-v}{\tau}.
$$

$$
v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right).
$$

| 時刻 | 変化の達成割合 |
| --- | ---: |
| $\tau$ | 63.2 % |
| $2\tau$ | 86.5 % |
| $3\tau$ | 95.0 % |

[これらの割合はどう求める？ 計算を参照。](#time-constant-derivation)

![正規化した一次遅れのステップ応答。時定数が１つ経過するごとに残る誤差が約 63.2 % 減ります。](../../../assets/figures/first_order_response.svg)

<a id="section-2"></a>

## 2. トルクと慣性

制御器は電気的な指令を計算し、実際のトルク $M$ はモーターが発生します。モデルでは $J$ を慣性モーメント、$\omega$ を角速度、$K$ を速度誤差に対するトルクの比例係数とします。$K$ が一定で $J$ が２倍なら $\tau$ も２倍になります。$J$ と $K$ をともに２倍にすると $\tau$ は同じですが、同じ誤差で必要なトルクは２倍です。摩擦、負荷、遅れ、電流制限は除外しています。

$$
J\frac{d\omega}{dt}=M,\qquad M=K(u-\omega).
$$

$$
\frac{d\omega}{dt}=\frac{K}{J}(u-\omega),\qquad \tau=\frac{J}{K}.
$$

**単位:** $J$: $\mathrm{kg}\cdot\mathrm{m}^2$; $\omega,u$: $\mathrm{rad/s}$; $M$: $\mathrm{N}\cdot\mathrm{m}$; $K$: $\mathrm{N}\cdot\mathrm{m}\cdot\mathrm{s}/\mathrm{rad}$; $\tau$: s.

理想モデルの記号によるフィードバック系。制御器が指令し、実際のトルクはモーターが発生します。

![理想モデルの記号によるフィードバック系。制御器が指令し、実際のトルクはモーターが発生します。](../../../assets/figures/control_loop.svg)

<a id="section-3"></a>

## 3. 刻み幅と時定数

オイラー法は時間刻み $dt$ ごとに状態を更新します。$dt$ を小さくしてもモデルのモーターは速くならず、数値近似が変わるだけです。$u=10\ \mathrm{mm/s}$、$\tau=1\ \mathrm{s}$、１秒後の結果は、$dt=0.1$ で $6.513$、$dt=0.01$ で $6.340\ \mathrm{mm/s}$、厳密解では $6.321\ \mathrm{mm/s}$ です。

$$
v_{n+1}=v_n+\frac{u-v_n}{\tau}\ dt.
$$

| 方法 | $v(1\ \mathrm{s})$ (mm/s) |
| --- | ---: |
| Euler $dt=0.1\ \mathrm{s}$ | 6.513 |
| Euler $dt=0.01\ \mathrm{s}$ | 6.340 |
| 厳密解 | 6.321 |

[計算の手順を参照。](#euler-values-derivation)

<a id="section-4"></a>

## 4. 計測値から時定数を推定する

目標回転数を 0 から 1000 rpm に変えたとき、計測値が約 632 rpm に達する時刻を調べます。2 秒後なら単純な一次系モデルで $\tau\approx2\ \mathrm{s}$ と推定します。初速度がゼロでない場合は、目標値の 63.2 % ではなく**速度変化全体の 63.2 %** を使います。雑音、遅れ、オーバーシュートがある場合には、より適切なシステム同定 (system identification) が必要です。

**コードが返す時刻の意味：** [`estimate_tau`](../../../exercises/02_first_order_response.py) は目標値を変えた時点を基準に、時刻が**厳密に増加する**測定値を受け取ります。変化量の 63.2 % に達したと**最初に観測されたサンプルの時刻**を返し、既知の測定分解能の半分を丸め許容差とします。1 s に測定し、次の 2 s の測定で初めて閾値を超えた場合、実際の通過は**サンプル間**にあった可能性があります。そのため 2 s はサンプリングに制約された推定値で、厳密な曲線当てはめではありません。閾値通過後であっても、不正な測定値、同時刻、時刻の逆転は拒否されます。通過しなければ `None` を返します。

**測定分解能に注意：** `estimate_tau` に渡す `resolution` は、**速度の全変化量の絶対値より小さく**なければなりません。速度が 0 から 10 rpm に変化しても、表示が 10 rpm 刻みなら、63.2 % の閾値を通過した時刻を信頼して推定できません。この入力は拒否され、最初のサンプルで閾値を越えたという誤った結果は返しません。分解能が十分でも、推定はサンプリング間隔によって制約されます。

<a id="section-5"></a>

## 5. 回転エネルギー

正味トルクは $M=J\alpha$ を満たします。$J=2\ \mathrm{kg}\cdot\mathrm{m}^2$、$\omega=10\ \mathrm{rad/s}$ なら回転運動エネルギーは $100\ \mathrm{J}$ で、$J$ を２倍にすると $200\ \mathrm{J}$ になります。角速度を２倍にするとエネルギーは４倍です。機械的エネルギーと総消費電力量は同じではありません。

$$
M=J\alpha,\qquad \alpha=\frac{d\omega}{dt}.
$$

$$
E=\frac{1}{2}J\omega^2.
$$

<a id="section-6"></a>

## 6. 演習

0 から 1000 rpm への理想的なステップ応答で、２秒後に約 632 rpm なら $\tau\approx2\ \mathrm{s}$ と推定できます。実測のノイズやサンプリングには、より慎重なシステム同定が必要です。演習でオイラー近似と厳密解を比較してください。

[02_first_order_response.py](../../../exercises/02_first_order_response.py) · [03_rotation_energy.py](../../../exercises/03_rotation_energy.py) · [plot_models.py](../../../exercises/plot_models.py)


<a id="section-7"></a>

## 7. 発展的な説明（任意）


### オイラー法の安定性

各ステップで**目標速度との差**は $1-\frac{dt}{\tau}$ 倍になります。収束条件は $0<dt<2\tau$ で、$\tau<dt<2\tau$ では数値結果が目標値を挟んで交互に変化します。実機が振動するという意味ではありません。

### モデルの限界

より一般的には $J\ \frac{d\omega}{dt}=M_{\text{モーター}}-M_{\text{負荷}}-M_{\text{摩擦}}$ です。$\tau=\frac{J}{K}$ は $M_{\text{正味}}=K(u-\omega)$ という特殊な仮定の下だけで成立し、負荷、摩擦、遅れ、電流制限で動作は変わります。

### エネルギーと出力

$J$ が一定なら $\Delta E=\frac{1}{2} J(\omega_2^2-\omega_1^2)$、瞬時の機械的出力 (mechanical power) は $P=M\omega$ です。電気入力の消費量とは一致しません。


<a id="time-constant-derivation"></a>

### 63.2 %、86.5 %、95.0 % の由来

これらの割合と指数関数は**同じ方程式**から導かれます。速度誤差を $\varepsilon(t)=u-v(t)$ と定義します（ネイピア数とは別です）。目標速度 $u$ が一定なら $\frac{d\varepsilon}{dt}=-\frac{dv}{dt}$ なので：

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

変数分離では $\varepsilon$ で割るため、この操作は初期誤差がゼロでないことを仮定します。$u=v_0$ の場合、誤差は常にゼロであり、元の微分方程式から定数解 $v(t)=u$ が直接得られます。

$$
f(t)=\frac{v(t)-v_0}{u-v_0}=1-\exp\!\left(-\frac{t}{\tau}\right),\qquad (u\ne v_0).
$$

| $t$ | $f(t)$ |
| ---: | ---: |
| $\tau$ | $1-\exp(-1)=0.63212056\ldots\approx63.2\ \%$ |
| $2\tau$ | $1-\exp(-2)=0.86466472\ldots\approx86.5\ \%$ |
| $3\tau$ | $1-\exp(-3)=0.95021293\ldots\approx95.0\ \%$ |

例えば 0 から毎分 1000 回転（rpm、revolutions per minute）に変更した場合、時定数の 1 倍、2 倍、3 倍経過後は約 632、865、950 回転/分です。理想モデルでは目標に漸近的に近づきます。

<a id="euler-values-derivation"></a>

### オイラー法の数値の導出

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
