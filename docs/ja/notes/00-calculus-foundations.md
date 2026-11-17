# 0. 微積分の基礎：機械工学の導関数・極限・積分

**言語:** [en](../../en/notes/00-calculus-foundations.md) · [fr](../../fr/notes/00-calculus-foundations.md) · [de](../../de/notes/00-calculus-foundations.md) · [it](../../it/notes/00-calculus-foundations.md) · [es](../../es/notes/00-calculus-foundations.md) · [pt](../../pt/notes/00-calculus-foundations.md) · [zh](../../zh/notes/00-calculus-foundations.md) · [ja](00-calculus-foundations.md) · [nb](../../nb/notes/00-calculus-foundations.md) · [ru](../../ru/notes/00-calculus-foundations.md) · [ko](../../ko/notes/00-calculus-foundations.md) · [fi](../../fi/notes/00-calculus-foundations.md) · [pl](../../pl/notes/00-calculus-foundations.md)

**このページの単位（例の前に説明）:** `s` — 秒; `mm` — ミリメートル = 0.001 m; `mm/s` — ミリメートル / 秒 — 線速度; `mm/s²` — ミリメートル / 秒² — 加速度; `kg·m²` — キログラム · メートル² — 慣性モーメント; `rad/s` — ラジアン / 秒 — 角速度; `rad/s²` — ラジアン / 秒² — 角加速度; `N·m` — ニュートン · メートル — トルク; `W` — ワット; `rpm` — 毎分回転数; `N/m` — ニュートン / メートル — 剛性; `mm³/s` — ミリメートル³ / 秒 — 体積流量; `%` — パーセント（百分の一）; `m` — メートル; `kg` — キログラム; `N` — ニュートン; `J` — ジュール; `rad` — ラジアン. [単位一覧](../UNITS.md).

[README](../README.md) · [Integral table](../INTEGRAL_TABLE.md) · [Trigonometry table](../TRIGONOMETRY.md) · [Motion](01-motion-calculus.md) · [Dynamics](02-first-order-dynamics.md) · [Symbols](../SYMBOLS.md)

> **学習用近似:** モデルと単位を検証し、実機に学習用コードを接続しないでください.

**自然指数関数**は $\exp(x)=\mathrm{e}^{x}$ で、**オイラー数**は $\mathrm{e}\approx2.71828$ です。連続的な増加や減衰を表し、$\exp(0)=1$、$\exp(-1)\approx0.3679$ です。自然対数 $\ln$ はその逆関数で、$\ln(\exp(x))=x$ です。[記号一覧](../SYMBOLS.md)も参照してください。

**導関数（derivative）**は量の瞬間的な変化率、**二階導関数（second derivative）**はその変化率がどう変わるかを示します。**積分（integral）**は小さな変化を蓄積します。**極限（limit）**は瞬間的な変化率を定義し、**対数（logarithm）**は指数応答から時刻を求めるために使います。

これらは工作機械の軸、サーボ、ロボット関節、ばね、センサに現れます。まず物理的な問いを明らかにし、次に計算規則と単位を選びます。

## 目次

- [1. 測定した変化から数式モデルへ](#section-1)
- [2. 極限と一階微分](#section-2)
- [3. 一階・二階微分：移動する機械軸](#section-3)
- [4. 連鎖律：回転エネルギー](#section-4)
- [5. 指数関数と対数：応答時間](#section-5)
- [6. 積分：変位と機械的仕事](#section-6)
- [7. 補足例：膨張する球](#section-7)
- [8. 単位・検算・練習](#section-8)

<a id="section-1"></a>
## 1. 測定した変化から数式モデルへ

| 物理的な問い | 数学的な道具 |
| --- | --- |
| 軸の**現在**の速さは？ | 一階導関数 $dx/dt$ |
| 速度はどう変わる？ | 二階導関数 $d^2x/dt^2$ |
| いつ 90 % に達する？ | 対数 $\ln$ |
| 2 s の変位は？ | 定積分 $\int v\ \mathrm{d}t$ |
| 変化する力の仕事は？ | 積分 $\int F\ \mathrm{d}x$ |

<a id="section-2"></a>
## 2. 極限と一階微分

二つの測定値の**有限差分（finite difference）**からは区間の平均変化率が得られます。区間をゼロへ近づけた極限が導関数です。

$$
v(t)=\frac{dx}{dt}=\lim_{h\to0}\frac{x(t+h)-x(t)}{h}.
$$

位置を $x(t)=a t^2$、$a=2\ \mathrm{mm/s^2}$ とします。極限を取る前に分子を展開します。

$$
\frac{x(t+h)-x(t)}h=\frac{a[(t+h)^2-t^2]}h=a(2t+h)\longrightarrow 2at.
$$

$h$ をゼロに近づける**前**に因子を約分します。$t=1\ \mathrm{s}$ で瞬間速度は $4\ \mathrm{mm/s}$ です。未定義の $0/0$ を直接代入しません。

**主な微分公式（differentiation rules）**：$c$ と $n$ は定数、三角関数の引数はラジアンです。

| 規則 | 式 |
| --- | --- |
| 定数 | $\frac{d}{dt}c=0$ |
| べき乗 | $\frac{d}{dt}t^n=n t^{n-1}$ |
| 係数と和 | $(cf+g)'=cf'+g'$ |
| 積 | $(fg)'=f' g+fg'$ |
| 商，$g\ne0$ | $\left(\frac{f}{g}\right)'=\frac{f' g-fg'}{g^2}$ |
| 合成関数 | $\frac{d}{dt}f(g(t))=f'(g(t))g'(t)$ |
| 指数関数 | $\frac{d}{dt}\exp(t)=\exp(t)$ |
| 自然対数，$t>0$ | $\frac{d}{dt}\ln t=\frac1t$ |
| 正弦 / 余弦 | $\frac{d}{dt}\sin t=\cos t$, $\frac{d}{dt}\cos t=-\sin t$ |

![位置曲線の接線勾配と速度曲線下の面積](../../../assets/figures/calculus_slope_area.svg)

<a id="section-3"></a>
## 3. 一階・二階微分：移動する機械軸

台車は初期位置 2 mm、初速度 3 mm/s、一定加速度 4 mm/s² で動きます。位置関数は次のとおりです。

$$
x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2.
$$

**一階微分**は速度です。定数項は消え、$t$ の項から 3 mm/s が得られ、$t^2$ の項は $t$ の一次式になります。

$$
v(t)=\frac{dx}{dt}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t.
$$

**二階微分**は加速度です。速度をもう一度微分します。2 s では位置 16 mm、速度 11 mm/s、加速度 4 mm/s² です。

$$
a(t)=\frac{d^2x}{dt^2}=\frac{dv}{dt}=4\ \mathrm{mm/s^2}.
$$

二階微分の単位は長さ/時間²であり、一階微分を**二乗することではありません**。

<a id="section-4"></a>
## 4. 連鎖律：回転エネルギー

回転するフライホイールには運動エネルギーが蓄えられます。角速度 $\omega$ が時刻で変わると、エネルギー $E$ もそれに応じて変わります。これが**連鎖律（chain rule）**です。

$$
E(\omega)=\frac12J\omega^2,\quad \omega=\omega(t),
$$
$$
\frac{dE}{dt}=\frac{dE}{d\omega}\frac{d\omega}{dt}=J\omega\alpha=M\omega=P.
$$

$J=0.01\ \mathrm{kg\cdot m^2}$、$\omega=10\ \mathrm{rad/s}$、$\alpha=2\ \mathrm{rad/s^2}$ なら、トルク $J\alpha=0.02\ \mathrm{N\cdot m}$、瞬間的な機械出力は $0.2\ \mathrm{W}$ です。つまり $P=M\omega$ です。

<a id="section-5"></a>
## 5. 指数関数と対数：応答時間

単純な一次遅れ系では、回転速度は指数関数的に最終値へ近づきます。$\tau$ は秒単位の**時定数（time constant）**です。

$$
\omega(t)=\omega_\infty\bigl(1-\exp(-t/\tau)\bigr),\quad t\ge0,\ \tau>0.
$$

この式は**初期角速度がゼロ**、すなわち $\omega(0)=0$ で、目標値 $\omega_\infty$ が一定である場合の式です。初期角速度が $\omega_0\ne0$ のとき、同じ一次遅れモデルの一般解は次のようになります。

$$
\omega(t)=\omega_\infty+(\omega_0-\omega_\infty)\exp(-t/\tau).
$$

**初期角速度がゼロでない場合の計算例：** $\omega_0=200\ \mathrm{rpm}$、$\omega_\infty=1000\ \mathrm{rpm}$、$\tau=0.5\ \mathrm{s}$ とします。時定数が一つ経過した $t=0.5\ \mathrm{s}$ では、

$$
\omega(\tau)=1000+(200-1000)\exp(-1)\approx705.7\ \mathrm{rpm}.
$$

ここで進んだのは**変化量 800 rpm の 63.2 %**であり、最終値 1000 rpm の 63.2 % ではありません。$t=0$ では 200 rpm、時間が十分に経つと 1000 rpm に近づきます。数学的な例でありモータへの指令ではありません。

指数関数は初期誤差の残りの割合を表します。残りの割合から**時刻**を求めるには、$\exp$ の逆関数である**自然対数（natural logarithm）** $\ln$ を使います。$0.1$ は無次元です。

$$
\exp(-t/\tau)=0.1
\quad\Longrightarrow\quad
-\frac{t}{\tau}=\ln(0.1)
\quad\Longrightarrow\quad
t=-\tau\ln(0.1)=\tau\ln(10)\approx2.303\tau.
$$

全変化の 90 % に達すると、誤差の 10 % が残ります。$\tau=0.5\ \mathrm{s}$ なら理想モデルの時間は約 1.151 s です。実機には制限や遅延が加わる場合があります。

$z>0$ のとき $\ln z$ の微分は $1/z$。$z=z(t)$ なら連鎖律で $dz/dt$ も掛けます。物理量の対数を取る際は無次元の比にする必要があります。

$$
\ln(1)=0,\quad \ln(\mathrm{e})=1,\quad \ln(\mathrm{e}^{z})=z,\quad \frac{d}{dz}\ln z=\frac1z\ (z>0).
$$

<a id="section-6"></a>
## 6. 積分：変位と機械的仕事

**不定積分（indefinite integral）**は積分定数 $C$ を含む原始関数（antiderivatives）の族です。**定積分（definite integral）**は区間内の変化の総量です。

$$
\int 4t\ \mathrm{d}t=2t^2+C,\qquad \int t^n\ \mathrm{d}t=\frac{t^{n+1}}{n+1}+C\ (n\ne-1).
$$

**変位の例。** 初期位置 $x_0=2\ \mathrm{mm}$、速度 $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$。0–2 s の変位を求めます。

$$
\Delta x=\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
$$
$$
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}=6\ \mathrm{mm}+8\ \mathrm{mm}=14\ \mathrm{mm}.
$$

変位は 14 mm。初期位置を足して $x(2)=16\ \mathrm{mm}$ です。負の速度は符号付き変位を減らしますが、移動距離は負になりません。

**ばねの仕事。** 剛性 $k=200\ \mathrm{N/m}$ の理想線形ばねを $x=0$ から $x=0.01\ \mathrm{m}$ まで伸ばします。力は伸びとともに増えるため、小区間の仕事を積分します。

$$
F(x)=kx,\qquad W=\int_0^{0.01\ \mathrm{m}}kx\ \mathrm{d}x
=\left[\frac{kx^2}{2}\right]_0^{0.01\ \mathrm{m}}
=\frac{200\ \mathrm{N/m}}2(0.01\ \mathrm{m})^2=0.01\ \mathrm{J}.
$$

仕事は 0.01 J。最終的な力 $F=2\ \mathrm{N}$ を全移動距離に掛けると誤って 0.02 J となります。力が一定でないためです。

<a id="section-7"></a>
## 7. 補足例：膨張する球

**補足の連鎖律。** 球の体積は半径に依存し、半径は時刻に依存します。これはフライホイールのエネルギーと角速度と同じ依存関係です。

$$
V(r)=\frac43\pi r^3,\qquad \frac{dV}{dt}=\frac{dV}{dr}\frac{dr}{dt}=4\pi r^2\frac{dr}{dt}.
$$

$r=10\ \mathrm{mm}$、$dr/dt=1\ \mathrm{mm/s}$ で、体積増加率は $400\pi\approx1256.64\ \mathrm{mm^3/s}$。$r(t)=10\ \mathrm{mm}+(1\ \mathrm{mm/s^2})t^2$ なら、2 s で $r=14\ \mathrm{mm}$、$dr/dt=4\ \mathrm{mm/s}$、結果は $3136\pi\approx9852.03\ \mathrm{mm^3/s}$ です。

<a id="section-8"></a>
## 8. 単位・検算・練習

**検算：** 位置の一階微分は m/s、二階微分は m/s²；力を距離で積分すると N·m = J；不定積分には $C$ が必要；導関数は局所的な変化、積分は蓄積量；数学の微分 $\mathrm{d}t$ とプログラムの有限ステップ `dt` は別物です。

**練習：** (1) $x(t)=5\ \mathrm{mm}+(2\ \mathrm{mm/s})t+(1\ \mathrm{mm/s^2})t^2$ の 3 s での速度と加速度。(2) $\tau=1\ \mathrm{s}$ の一次応答が 90 % に達する時間。(3) 4 mm/s で 2 s 移動した変位。**答え：** 8 mm/s と 2 mm/s²；約 2.303 s；8 mm。

**途中式を含む解答：**

1. $v(t)=\frac{dx}{dt}=2\ \mathrm{mm/s}+2(1\ \mathrm{mm/s^2})t$; $v(3\ \mathrm{s})=2+2\cdot3=8\ \mathrm{mm/s}$. $a(t)=\frac{dv}{dt}=2\ \mathrm{mm/s^2}$.
2. $f(t)=1-\exp(-t/\tau)=0.9$; $\exp(-t/\tau)=0.1$; $t=-\tau\ln(0.1)=\tau\ln(10)$. $\tau=1\ \mathrm{s}$; $t\approx2.303\ \mathrm{s}$.
3. $\Delta x=\int_0^{2\ \mathrm{s}}(4\ \mathrm{mm/s})\ \mathrm{d}t=(4\ \mathrm{mm/s})(2\ \mathrm{s})=8\ \mathrm{mm}$.


[Integral reference](../INTEGRAL_TABLE.md) · [Trigonometry](../TRIGONOMETRY.md) · [Next: motion](01-motion-calculus.md) · [Python exercises](../exercises/README.md)
