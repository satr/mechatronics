# 1. 運動・微分・積分


**このページの言語を切り替える:** [en](../../en/notes/01-motion-calculus.md) · [fr](../../fr/notes/01-motion-calculus.md) · [de](../../de/notes/01-motion-calculus.md) · [it](../../it/notes/01-motion-calculus.md) · [es](../../es/notes/01-motion-calculus.md) · [pt](../../pt/notes/01-motion-calculus.md) · [zh](../../zh/notes/01-motion-calculus.md) · [ja](01-motion-calculus.md) · [nb](../../nb/notes/01-motion-calculus.md) · [ru](../../ru/notes/01-motion-calculus.md) · [ko](../../ko/notes/01-motion-calculus.md) · [fi](../../fi/notes/01-motion-calculus.md) · [pl](../../pl/notes/01-motion-calculus.md)

**このページの単位（例の前に説明）:** `s` — 秒; `mm` — ミリメートル = 0.001 m; `mm/s` — ミリメートル / 秒 — 線速度; `mm/s²` — ミリメートル / 秒² — 加速度; `%` — パーセント（百分の一）. [単位一覧](../UNITS.md).

**基礎:** [0. 微積分の基礎：導関数・微分・積分](00-calculus-foundations.md) · [積分公式表](../INTEGRAL_TABLE.md)

[README](../README.md) · [公式早見表](../CHEATSHEET.md) · [Python 演習](../exercises/README.md) · [一次系の動特性と回転](02-first-order-dynamics.md)

> **注意：** 本教材は AI を利用して作成されており、誤り、不正確な翻訳、誤った仮定が含まれる可能性があります。利用は自己責任で行い、数式と計算を独立に確認してください。**実機のモーターや工作機械の制御に使用しないでください。**

## 要点

移動距離は軌跡の全長、変位は最終位置から初期位置を引いた値です。速さ（speed）は非負ですが、速度（velocity）は向きを含み、座標軸に沿って負にもなります。位置を時間で微分すると瞬間速度が得られ、符号付き速度を積分すると変位が得られます。

**英語の専門用語：**

- 移動距離 (distance traveled)
- 変位 (displacement)
- 速さ (speed)
- 速度ベクトル (velocity)
- 導関数 (derivative)
- 積分 (integral)
- 数値積分 (numerical integration)
- 陽的オイラー法 (explicit Euler method)

## このページの目次

- [1. 運動の例](#section-1)
- [2. 微分と瞬間速度](#section-2)
- [3. 積分と変位](#section-3)
- [4. 数値積分](#section-4)
- [5. 演習](#section-5)
- [6. 発展的な説明（任意）](#section-6)
  - [なぜ 2t² の微分が 4t になるのか](#power-rule-derivation)
  - [表中の変位の計算](#motion-values-derivation)

**単位の説明（units）：** 時間は秒（s、second）、位置はミリメートル（mm、millimeter）、速度はミリメートル毎秒（mm/s、millimeter per second）で表します。詳しくは[公式早見表](../CHEATSHEET.md)を参照してください。

[SI 単位と小数点の説明](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. 運動の例

単位、導出、数値計算上の注意点は[発展的な説明](#section-6)を参照してください。

仮想軸が $+3\ \mathrm{mm/s}$ で２秒進み、続いて $-3\ \mathrm{mm/s}$ で２秒戻ると、変位は $+6-6=0\ \mathrm{mm}$、移動距離は $12\ \mathrm{mm}$ です。円運動では速さが一定でも、速度ベクトルの向きは変化します。

$$
\overline{v}=\frac{x(t_2)-x(t_1)}{t_2-t_1}.
$$

$$
\text{平均の速さ}=\frac{\text{総移動距離}}{t_2-t_1}.
$$

**4 秒間全体**で計算すると、符号付きの平均速度と平均の速さは**異なる値**になります。軸は出発点に戻りますが、移動距離は 12 mm です。

$$
\overline{v}_x=\frac{0\ \mathrm{mm}}{4\ \mathrm{s}}=0\ \mathrm{mm/s}
$$

$$
\overline{\lvert v\rvert}=\frac{12\ \mathrm{mm}}{4\ \mathrm{s}}=3\ \mathrm{mm/s}
$$

したがって平均の速さは**平均速度ベクトルの大きさと常に等しいわけではありません**。円を一周して出発点に戻る場合も平均速度ベクトルはゼロですが、移動距離と平均の速さは正になります。

<a id="section-2"></a>

## 2. 微分と瞬間速度

$x(t)=2t^2\ \mathrm{mm}$（$t$ は秒）なら $v(t)=4t\ \mathrm{mm/s}$. **なぜ 4 になる？** べき乗の微分法則（power rule）より $d(t^2)/dt=2t$ です。したがって $2t^2$ の微分は $2\cdot2t=4t$ です。[詳しい計算と単位](#power-rule-derivation)。 です。$t=1\ \mathrm{s}$ での瞬間速度は $4\ \mathrm{mm/s}$ です。前進差分で $dt=1$、$0.1$、$0.01\ \mathrm{s}$ とすると、推定値はそれぞれ $6$、$4.2$、$4.02\ \mathrm{mm/s}$ になります。

$$
v(t)=\frac{dx}{dt},\qquad v(t)\approx\frac{x(t+dt)-x(t)}{dt}.
$$

**時間刻みを小さくしすぎると失敗する理由：** $t=1\ \mathrm{s}$ での $x(t)=2t^2$ の厳密な導関数は $4\ \mathrm{mm/s}$ です。しかし $dt=1e-17\ \mathrm{s}$ にすると、Python の `float` は `t + dt` を元の `t` に丸めます。二つの位置が等しくなり、差分から誤って速度ゼロが得られます。さらに小さな値の領域では、導関数がゼロでなくても両方の位置がアンダーフローによってゼロになる場合があります。練習関数 [`forward_derivative`](../../../exercises/01_motion_and_integral.py) は、こうした場合に誤ったゼロではなく `ValueError` を出します。有限差分法自体は変えず、無制限に刻みを小さくするのではなく表現可能な刻みを選びます。

<a id="section-3"></a>

## 3. 積分と変位

符号付き速度の積分は負またはゼロになり得ますが、速度の絶対値の積分は非負の移動距離です。$0$～$2\ \mathrm{s}$ で $v(t)=2t\ \mathrm{mm/s}$ の場合、正確な変位は $4\ \mathrm{mm}$ です。

$$
\Delta x=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t,\qquad
s=\int_{t_1}^{t_2}|v(t)|\ \mathrm{d}t.
$$

幾何学的には、符号付き速度の積分は速度–時間グラフの下の符号付き面積です。**これは第2節とは別の運動モデルです。** 第2節の位置 $x(t)=2t^2$ を微分すると速度は $v(t)=4t$ になります。一方、この積分の説明では、意図的に異なる速度 $v(t)=2t$ を用いています。これに対応する位置は $x(t)=t^2+C$ です（単位は一貫させます）。$2t^2$ の微分を $2t$ として扱うことはできません。

<a id="section-4"></a>

## 4. 数値積分

厳密な変位と左端点を使うオイラー近似の比較（合成データ）。

![厳密な変位と左端点を使うオイラー近似の比較（合成データ）。](../../../assets/figures/euler_vs_exact.svg)

陽的オイラー法は各時間区間の**始点**の速度を使い、区間の真の平均速度は使いません。この増加速度の例では変位を過小評価し、$dt=0.5$、$0.1$、$0.01\ \mathrm{s}$ で $3$、$3.8$、$3.98\ \mathrm{mm}$ です（正確値 $4\ \mathrm{mm}$）。速度が時間に対して一次関数なので、台形則はこの例では正確です。

$$
x_{n+1}=x_n+v(t_n)\ dt.
$$

| `dt` (s) | Euler (mm) |
| ---: | ---: |
| 0.5 | 3.000 |
| 0.1 | 3.800 |
| 0.01 | 3.980 |
| 厳密解 | 4.000 |


[3、3.8、3.98 の計算を参照。](#motion-values-derivation)

<a id="section-5"></a>

## 5. 演習

運動プログラムを実行して $dt$ を小さくしてください。往復運動の変位がゼロでも移動距離が正なのはなぜでしょうか。

[01_motion_and_integral.py](../../../exercises/01_motion_and_integral.py)

<a id="section-6"></a>

## 6. 発展的な説明（任意）

### 係数と単位

$t$ が秒なら $x(t)=2t^2$ mm は省略表記で、係数には $2\ \mathrm{mm/s^2}$ の単位があります。したがって $v(t)=4t$ の単位は mm/s です。式に数値を代入する前に単位を確認します。

### 近似の限界

有限差分 (finite difference) はゼロでない時間幅を用いた導関数の近似です。刻みを減らすと一般に打切り誤差は減りますが、極端に小さい刻みは丸め誤差や測定雑音を増幅することがあります。オイラー法は刻みの最初の値を使います。

### 多次元の運動

位置ベクトル $\mathbf r(t)$ について速度は $\mathbf v=d\mathbf r/dt$、速さは $\|\mathbf v\|$、移動距離は $s=\int\|\mathbf v(t)\|dt$ です。


<a id="power-rule-derivation"></a>

### なぜ $2t^2$ の微分が $4t$ になるのか



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

### 表中の変位の計算

$$
a=2\ \mathrm{mm/s^2},\qquad v(t)=at,\qquad 0\le t\le2\ \mathrm{s}.
$$

$$
\Delta x=\int_{0}^{2\ \mathrm{s}}at\ \mathrm{d}t
=\left[\frac{at^2}{2}\right]_{0}^{2\ \mathrm{s}}
=4\ \mathrm{mm}.
$$



記号 $\sum$（ギリシャ大文字の sigma、**総和記号** / summation）は、項を順番に足し合わせる意味です。$\sum_{n=0}^{N-1}(2nh)h$ では、添字 $n$ が $0; 1; \ldots; N-1$ と動き、全部で $N$ 項あります。Python の `for` ループで加算を繰り返すことに相当します。例えば $\sum_{n=1}^{3}n=1+2+3=6$ です。 [← 記号の説明](../SYMBOLS.md#summation).

$$
h=\frac{dt}{1\ \mathrm{s}},\qquad N=\frac{2}{h}.
$$

$$
x_{\mathrm{Euler}}(2\ \mathrm{s})
=\left[\sum_{n=0}^{N-1}(2nh)h\right]\ \mathrm{mm}
=\left[h^2N(N-1)\right]\ \mathrm{mm}
=(4-2h)\ \mathrm{mm}.
$$

ここで `h` は時間刻み `dt` を秒（s、second）で表した数値（`dt = 0.5 s` なら `h = 0.5`）、`N` はステップ数です。結果は**ミリメートル（mm、millimetre）単位の変位**です。



ここで $t$ は秒（s、second）、$v$ はミリメートル毎秒（mm/s、millimeter per second）です。$dt=0.5$、$0.1$、$0.01$ 秒の場合、変位はそれぞれ $3$、$3.8$、$3.98$ ミリメートル（mm、millimeter）です。$2/dt$ が整数であると仮定します。
