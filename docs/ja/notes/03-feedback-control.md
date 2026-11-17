# 3. フィードバック制御：PID・サンプリング・飽和・保持トルク

**言語:** [en](../../en/notes/03-feedback-control.md) · [fr](../../fr/notes/03-feedback-control.md) · [de](../../de/notes/03-feedback-control.md) · [it](../../it/notes/03-feedback-control.md) · [es](../../es/notes/03-feedback-control.md) · [pt](../../pt/notes/03-feedback-control.md) · [zh](../../zh/notes/03-feedback-control.md) · [ja](03-feedback-control.md) · [nb](../../nb/notes/03-feedback-control.md) · [ru](../../ru/notes/03-feedback-control.md) · [ko](../../ko/notes/03-feedback-control.md) · [fi](../../fi/notes/03-feedback-control.md) · [pl](../../pl/notes/03-feedback-control.md)

**このページの単位（例の前に説明）:** `rpm` — 毎分回転数; `A` — アンペア; `s` — 秒; `rpm/s` — 毎分回転数 / 秒 — 角加速度; `A/rpm` — アンペア / (毎分回転数) — 速度に対するゲイン; `A/(rpm·s)` — アンペア / (毎分回転数 · 秒) — 積分ゲイン; `A·s/rpm` — アンペア · 秒 / (毎分回転数) — 微分ゲイン; `N·m` — ニュートン · メートル — トルク; `kg` — キログラム; `m` — メートル; `N` — ニュートン. [単位一覧](../UNITS.md).

[README](../README.md) · [Math foundations](00-calculus-foundations.md) · [First-order dynamics](02-first-order-dynamics.md) · [Trigonometry](../TRIGONOMETRY.md)

> **学習モデル:** これらの簡略化したアルゴリズムを実際のモーターや機械に接続しないでください。

## 目次

- [1. 閉ループ速度制御](#section-1)
- [2. P：比例動作](#section-2)
- [3. I：誤差の蓄積と電流指令](#section-3)
- [4. D：誤差の変化とセンサノイズ](#section-4)
- [5. サンプリング・飽和・アンチワインドアップ](#section-5)
- [6. 重力に抗してロボット関節を保持する](#section-6)
- [7. 検証と制限](#section-7)

<a id="section-1"></a>
## 1. 閉ループ速度制御

**フィードバック制御器（feedback controller）**は目標値と測定値を比較します。目標 1000 rpm、測定 950 rpm なら誤差は +50 rpm。この例の PID 出力は**トルクを生む電流の指令値**であり、直前の電流に加える増分ではありません。

$$
\varepsilon(t)=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}},
\qquad I_{\mathrm{set}}=u_P+u_I+u_D.
$$

駆動装置には電流を追従させる内部電流制御ループがあり、電圧や PWM を変える場合があります。他の機器はトルク・電圧・PWM を指令するため、すべて電流設定とは限りません。

<a id="section-2"></a>
## 2. P：比例動作

**P（proportional）**は**現在の誤差**に応答します。フィードフォワード（feedforward）補償がない単純モデルでは、一定の負荷を支えるのに非ゼロのトルク・電流が必要です。誤差ゼロでは P 出力もゼロなので**定常偏差（steady-state error）**が残り得ます。

$$
u_P=K_p\varepsilon,\quad [K_p]=\mathrm{A/rpm}.
$$

<a id="section-3"></a>
## 3. I：誤差の蓄積と電流指令

**I（integral）**は誤差を時間で積分し、一つの内部状態として保持します。全履歴を配列保存するわけではありません。正誤差で増加、ゼロで維持、負誤差で減少し、正しい速度でも電流指令を維持できます。

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

dt = 1 s、Kp = 0.02 A/rpm、Ki = 0.002 A/(rpm·s) の例。+50 rpm が 3 回続くと積分は 50、100、150 rpm·s、I 出力は 0.10、0.20、0.30 A。誤差ゼロなら 0.30 A を保持します。続いて −20 rpm が 1 s ずつ続くと 0.26、0.22 A になります。−0.04 A は**一回分の変化**で、新しい電流全体ではありません。

プログラムが出力するのは累積積分、I 項、合計電流指令値です。次の表には誤差と P 項も加え、各計算を確認できるようにしました。サンプル間隔は 1 s、積分の初期値はゼロです。

| k | 測定回転数 (rpm) | ε (rpm) | z (rpm·s) | u_P (A) | u_I (A) | I_set (A) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 950 | +50 | 50 | +1.00 | +0.10 | +1.10 |
| 2 | 950 | +50 | 100 | +1.00 | +0.20 | +1.20 |
| 3 | 950 | +50 | 150 | +1.00 | +0.30 | +1.30 |
| 4 | 1000 | 0 | 150 | 0.00 | +0.30 | +0.30 |
| 5 | 1020 | −20 | 130 | −0.40 | +0.26 | −0.14 |
| 6 | 1020 | −20 | 110 | −0.40 | +0.22 | −0.18 |

測定値が 1020 rpm のとき誤差は −20 rpm です。P 項は −0.40 A、I 項はまだ +0.26 A なので、**符号付き合計電流指令は −0.14 A** となり、次のサンプルでは −0.18 A です。I 項の変化（1 ステップにつき −0.04 A）は合計指令値ではありません。これは学習用モデルの計算で、実機の設定値ではありません。

<a id="section-4"></a>
## 4. D：誤差の変化とセンサノイズ

**D（derivative）**は**誤差の変化率**に応答します。目標速度が一定で加速中なら誤差は減り、負の D 項がオーバーシュート（overshoot）を抑える場合があります。D は速度そのものではありません。0.01 s に 8 rpm の測定値ジャンプは見かけ上 800 rpm/s です。

$$
u_D=K_d\frac{\mathrm{d}\varepsilon}{\mathrm{d}t},\quad [K_d]=\mathrm{A\cdot s/rpm},\qquad
\frac{\Delta\omega}{\Delta t}=\frac{8\ \mathrm{rpm}}{0.01\ \mathrm{s}}=800\ \mathrm{rpm/s}.
$$

誤差の時間微分の単位は rpm/s です。D 項の出力は A 単位の電流指令なので、`K_d` の単位は rpm/s を打ち消す A·s/rpm でなければなりません。積の単位は A になります。

**微分フィルタ（derivative filtering）**は高周波ノイズを抑えますが、強すぎると応答が遅れます。目標値の急変によるキックを避けるため、目標ではなく測定値を微分することもあります。

<a id="section-5"></a>
## 5. サンプリング・飽和・アンチワインドアップ

デジタル制御には**サンプリング周期（sampling period）**があります。誤差 20 rpm が 1 s 続く場合、dt = 0.01 s の 100 回でも dt = 0.1 s の 10 回でも積分値は 20 rpm·s。dt を掛け忘れると高速側が 10 倍蓄積します。

$$
z_{k+1}=z_k+\varepsilon_k\ \Delta t.
$$

駆動の電流上限を超えて積分し続けると**積分ワインドアップ（integral windup）**が起き、負荷減少後に大きく超過する恐れがあります。**アンチワインドアップ（anti-windup）**では飽和を悪化させる積分を止めたり、実際の出力との誤差で状態を補正したりします。制限すべきは P を含む**合計指令**です。

<a id="section-6"></a>
## 6. 重力に抗してロボット関節を保持する

**トルク定数 Kt（motor torque constant）**はトルクを生む電流 1 A 当たりのトルクで、単位は N·m/A です。Kt = 0.1 N·m/A、電流 2 A なら 0.2 N·m。メーカーの電流定義に注意します。

$$
M_{\mathrm{motor}}=K_t I,\qquad [K_t]=\mathrm{N\cdot m/A}.
$$

水平関節の支点から距離 L の質量 m が、水平面から角度 θ にあるとき、重力トルクの大きさは mgL|cos θ|。静止状態ではモータと負荷のトルクは符号が反対です。位置誤差ゼロでも保持電流が必要な場合があります。ブレーキや真にセルフロックする機構なら無通電保持できますが、**Harmonic Drive** 自体が常にセルフロックするわけではありません。

$$
J\alpha=M_{\mathrm{motor}}+M_{\mathrm{load}},\quad
\alpha=0\ \Longrightarrow\ M_{\mathrm{motor}}=-M_{\mathrm{load}},
$$
$$
|M_g|=mgL|\cos\theta|.
$$

BLDC の **outrunner** は外側の殻が回り、**inrunner** は内部のロータが回ります。ロータは回転部分、ステータは固定部分です。

<a id="section-7"></a>
## 7. 検証と制限

電流値は教学用で、実機の設定値ではありません。実際には限流、フィルタ、エンコーダ校正、熱保護、安全な検証が必要です。

[Math foundation](00-calculus-foundations.md) · [Trigonometry table](../TRIGONOMETRY.md) · [First-order dynamics](02-first-order-dynamics.md)
