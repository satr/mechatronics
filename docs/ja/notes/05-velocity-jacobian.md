# 5. 回転、線速度、特異姿勢

**Languages:** [en](../../en/notes/05-velocity-jacobian.md) · [fr](../../fr/notes/05-velocity-jacobian.md) · [de](../../de/notes/05-velocity-jacobian.md) · [it](../../it/notes/05-velocity-jacobian.md) · [es](../../es/notes/05-velocity-jacobian.md) · [pt](../../pt/notes/05-velocity-jacobian.md) · [zh](../../zh/notes/05-velocity-jacobian.md) · [ja](05-velocity-jacobian.md) · [nb](../../nb/notes/05-velocity-jacobian.md) · [ru](../../ru/notes/05-velocity-jacobian.md) · [ko](../../ko/notes/05-velocity-jacobian.md) · [fi](../../fi/notes/05-velocity-jacobian.md) · [pl](../../pl/notes/05-velocity-jacobian.md)

**このページの単位（例の前に説明）:** `mm` — ミリメートル = 0.001 m; `mm/s` — ミリメートル / 秒 — 線速度; `rad` — ラジアン; `rad/s` — ラジアン / 秒 — 角速度; `mm/rad` — ミリメートル / ラジアン — ヤコビ行列の係数（角度当たりの長さ）; `°` — 度. [単位一覧](../UNITS.md).

[README](../README.md) · [Trigonometry](../TRIGONOMETRY.md#unit-circle-values) · [Coordinate frames](04-coordinate-frames.md) · [Calculus foundations](00-calculus-foundations.md)

> 学習用の理想モデルです。実機の制御には使用しないでください。

回転するリンクの先端は円弧を描き、瞬間速度はリンク方向でなく接線方向です。最初に幾何学的な意味を示し、次に時間微分、最後に任意の発展内容としてヤコビ行列（Jacobian matrix）を説明します。

## 目次

1. [回転から接線速度へ](#section-1)
2. [微分式の由来](#section-2)
3. [速度と符号の計算例](#section-3)
4. [2リンク：相対角と絶対角](#section-4)
5. [折り畳みと伸長時の特異姿勢](#section-5)
6. [折り畳み付近の3種類の変位](#section-6)
7. [発展：ヤコビ行列と解答付き問題](#section-7)

<a id="section-1"></a>
## 1. 回転から接線速度へ

長さ $L$ の剛体リンクが固定支点 $O$ の周りを回転するとします。時間間隔 $\Delta t>0$ の間の角度変化を $\Delta Q$ とし、**角度はラジアン**で表します。この間に回転方向が変わらなければ、先端は円弧に沿って動きます。その**円弧長**は厳密に $\Delta s=L|\Delta Q|$ です。また回転方向の符号を含む**符号付き円弧距離**は $L\Delta Q$ です。これらは先端の二つの位置を直線で結ぶ変位（弦）とは異なります。

$$
\Delta s=L\lvert\Delta Q\rvert,\qquad
\Delta s_{\mathrm{signed}}=L\Delta Q
$$

円弧長を経過時間で割ると、この区間の**平均の速さ**が得られます。

$$
\overline{v}=\frac{\Delta s}{\Delta t}
=L\left\lvert\frac{\Delta Q}{\Delta t}\right\rvert
$$

**瞬間の速さ**を求めるには $\Delta t\to0$ の極限を取ります。角速度は $\omega=\dot Q=\mathrm{d}Q/\mathrm{d}t$（単位 rad/s）なので、先端の速さは $v=L|\omega|$ です。速度ベクトルは**円の接線方向**、すなわちリンクに垂直です。$Q=45^\circ$ で反時計回り（$\omega>0$）なら先端は左上へ動き、水平速度成分は負、鉛直速度成分は正となります。

$$
v=L\lvert\dot Q\rvert
$$

![Q=45° での接線速度と符号付き成分。](../../../assets/figures/link_tangent_velocity.svg)

*Q=45° での接線速度と符号付き成分。*

<a id="section-2"></a>
## 2. 微分式の由来

座標は角度 Q に依存し、その Q は時間に依存します。連鎖律（chain rule）は1ラジアン当たりの位置変化と1秒当たりの角度変化を掛け合わせます。

$$
x(t)=L\cdot\cos\bigl(Q(t)\bigr),\qquad y(t)=L\cdot\sin\bigl(Q(t)\bigr)
$$

$$
v_x=\frac{\mathrm{d}x}{\mathrm{d}t}
=\frac{\mathrm{d}x}{\mathrm{d}Q}\cdot\frac{\mathrm{d}Q}{\mathrm{d}t}
=-L\cdot\sin(Q)\cdot\dot{Q}
$$

$$
v_y=\frac{\mathrm{d}y}{\mathrm{d}t}
=\frac{\mathrm{d}y}{\mathrm{d}Q}\cdot\frac{\mathrm{d}Q}{\mathrm{d}t}
=L\cdot\cos(Q)\cdot\dot{Q}
$$

角速度 $\dot Q=\mathrm{d}Q/\mathrm{d}t$ の単位は rad/s であり、角度そのものではありません。L が mm のとき vx、vy は mm/s です。三角関数の微分にはラジアンを用います。


$$
\omega=\dot{Q},\qquad \omega_1=\dot{Q}_1,\qquad \omega_2=\dot{Q}_2
$$

<a id="section-3"></a>
## 3. 速度と符号の計算例

L=150 mm、Q=45°、ω=+0.1 rad/s では速度成分の大きさは同じで、左向きと上向きです。ω の符号を反転すると両成分が反転します。Q=0°では vy=15 mm/s、vx=0 です。

$$
Q=45^\circ:\quad v_x=-150\frac{\sqrt2}{2}\cdot0.1\approx-10.61\ \mathrm{mm/s}
$$

$$
v_y=+150\frac{\sqrt2}{2}\cdot0.1\approx+10.61\ \mathrm{mm/s}
$$

$$
\sqrt{v_x^2+v_y^2}=L\lvert\dot Q\rvert=15\ \mathrm{mm/s}
$$

$Q$ の上の点は角度との掛け算ではなく、時間に関する**導関数** $\dot Q$ を意味します。$\omega$ を $-\omega$ に変えると両速度成分の符号が逆転しますが、速さ $L|\omega|$ は変わりません。

<a id="section-4"></a>
## 4. 2リンク：相対角と絶対角

Q1 は世界 +X から測る絶対角、Q2 は肘関節の相対角です。第2リンクの絶対角は Q1+Q2、角速度は ω₁+ω₂ です。

$$
X=L_1\cdot\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)
$$

$$
Y=L_1\cdot\sin(Q_1)+L_2\cdot\sin(Q_1+Q_2)
$$

$$
v_x=-L_1\cdot\sin(Q_1)\cdot\dot{Q}_1
-L_2\cdot\sin(Q_1+Q_2)\cdot(\dot{Q}_1+\dot{Q}_2)
$$

$$
v_y=L_1\cdot\cos(Q_1)\cdot\dot{Q}_1
+L_2\cdot\cos(Q_1+Q_2)\cdot(\dot{Q}_1+\dot{Q}_2)
$$

両方の関節が先端速度に寄与します。第1リンクには $\dot Q_1$、第2リンクには $\dot Q_1+\dot Q_2$ が現れます。第2関節角は第1リンクに対する相対角なので、第2リンクの角速度を $\dot Q_2$ のみで計算してはいけません。

<a id="section-5"></a>
## 5. 折り畳みと伸長時の特異姿勢

L1=100 mm、L2=50 mm の理想2リンクでは半径は50–150 mmです。完全に折り畳んだ状態（Q2=180°）と伸ばした状態（Q2=0°）は特異姿勢で、有限の関節速度から瞬間的な半径方向速度を作れません。

$$
r^2=L_1^2+L_2^2+2L_1L_2\cos(Q_2)
$$

$$
\lvert L_1-L_2\rvert\le r\le L_1+L_2
$$

$$
\frac{\mathrm{d}r}{\mathrm{d}Q_2}
=-\frac{L_1L_2\sin(Q_2)}{r}
$$

この導関数の式は $r>0$ の場合にのみ成り立ちます。2本のリンクが等長（$L_1=L_2$）のとき、基点まで完全に折り畳む位置（$Q_2=180^\circ$）では $r=0$ となり、式はゼロ除算になります。この位置では、半径方向の距離は肘角の**符号付き偏差**に関して微分できません。ここで扱う $L_1=100$ mm、$L_2=50$ mm の異なる長さの場合はこの特例に該当しません。

実機では関節角の制限や衝突によって作業領域がさらに小さくなることがあります。ある位置に到達できても、工具の向きや障害物との安全な間隔が確保できるとは限りません。

<a id="section-6"></a>
## 6. 折り畳み付近の3種類の変位

第1リンクを固定し、δを完全折り畳みからの小さい偏角（ラジアン）とします。固定された第1リンク軸方向の変位と基点からの距離変化は別の量です。

$$
\Delta x_{\mathrm{axis}}=L_2\bigl(1-\cos(\delta)\bigr)
\approx\frac{L_2\delta^2}{2}
$$

$$
\Delta y_{\mathrm{perp}}=L_2\cdot\sin(\delta)\approx L_2\delta
$$

$$
\Delta r=\sqrt{(L_1-L_2)^2+2L_1L_2\bigl(1-\cos(\delta)\bigr)}-(L_1-L_2)
$$

$$
L_1>L_2>0:\qquad
\Delta r\approx\frac{L_1L_2}{2(L_1-L_2)}\delta^2
$$

恒等式 1−cosδ=2sin²(δ/2) と sin(δ/2)≈δ/2 から二乗と係数1/2が現れます。この例では半径変化 ≈50δ² mm、固定軸方向変位 ≈25δ² mm です。

これらの近似は $\delta$ が小さく、ラジアンで測られる場合に限ります。$\delta$ を半分にすると、軸方向と半径方向の**二次**変化はそれぞれ約**4分の1**になりますが、横方向変位は**半分**です。

$$
1-\cos(\delta)=2\sin^2\left(\frac{\delta}{2}\right)
\approx2\left(\frac{\delta}{2}\right)^2=\frac{\delta^2}{2}
$$

![折り畳み付近の軸方向、横方向、半径方向の変位。](../../../assets/figures/folded_displacement_curves.svg)

*折り畳み付近の軸方向、横方向、半径方向の変位。*

折り畳み姿勢の近くで一定の非ゼロ半径方向速度を求めると、δ→0 に伴い必要な関節角速度が増大します。完全に折り畳んだ点では有限の関節速度から瞬時に非ゼロの半径方向速度を得られません。

$$
\left.\frac{\mathrm{d}r}{\mathrm{d}\delta}\right|_{L_1=100,L_2=50}
=\frac{5000\sin(\delta)}{r}
\approx100\delta\ \mathrm{mm/rad}
$$

$$
v_r\approx(100\delta)\dot\delta\ \mathrm{mm/s},
\qquad
\dot\delta\approx\frac{1\ \mathrm{mm/s}}{100\ \mathrm{mm/rad}\cdot\delta}
$$

![特異姿勢付近で必要な肘関節角速度。](../../../assets/figures/folded_radial_speed.svg)

*特異姿勢付近で必要な肘関節角速度。*

<a id="section-7"></a>
## 7. 発展：ヤコビ行列と解答付き問題

ヤコビ行列（Jacobian matrix）は先端座標を関節角で偏微分して得る行列で、関節角速度を先端の線速度へ写像します。関節角から絶対位置を直接求める式ではありません。完全に伸びるか折り畳まれた姿勢では行列式がゼロになり、その近くの逆速度計算は悪条件です。実機には可動域制限、工具オフセット、バックラッシュ、たわみ、衝突の制約もあります。このモデルは学習用です。

$$
v_x=J_{11}\cdot\omega_1+J_{12}\cdot\omega_2
$$

$$
v_y=J_{21}\cdot\omega_1+J_{22}\cdot\omega_2
$$

| 係数 | 速度変換の幾何学的な式 |
| --- | --- |
| $J_{11}$ | $-L_1\sin(Q_1)-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{12}$ | $-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{21}$ | $L_1\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)$ |
| $J_{22}$ | $L_2\cdot\cos(Q_1+Q_2)$ |



**行列式の導出.** 各係数は先端座標 X または Y を関節角 Q1 または Q2（ラジアン）で偏微分したものです。リンク長が mm なら単位は mm/rad で、関節角速度 rad/s を掛けると先端速度 mm/s が得られます。

$$
J_{11}=\frac{\partial X}{\partial Q_1},\qquad
J_{12}=\frac{\partial X}{\partial Q_2}
$$

$$
J_{21}=\frac{\partial Y}{\partial Q_1},\qquad
J_{22}=\frac{\partial Y}{\partial Q_2}
$$

$$
\det J=J_{11}J_{22}-J_{12}J_{21}
$$

$$
\det J=L_1L_2\bigl[\sin(Q_1+Q_2)\cos(Q_1)
-\sin(Q_1)\cos(Q_1+Q_2)\bigr]
$$

$$
\det J=L_1L_2\sin\bigl((Q_1+Q_2)-Q_1\bigr)
$$

行列式の2つの積を展開すると、L2 の二乗の項が相殺されます。正弦の差の公式により Q1 が消えます。

$$
\det J=L_1L_2\sin(Q_2)
$$

![2つの関節の速度寄与をベクトルとして加えると先端速度になります。](../../../assets/figures/two_link_jacobian_velocity.svg)

*2つの関節の速度寄与をベクトルとして加えると先端速度になります。*

### 解答付き計算例

1. 長さ $L=150$ mm のリンクが $Q=0^\circ$ で右を向いています。$\omega=+0.1$ rad/s なら $\sin0^\circ=0$、$\cos0^\circ=1$ より $v_x=-150\cdot0\cdot0.1=0$、$v_y=150\cdot1\cdot0.1=+15$ mm/s。先端は上へ動きます。
2. $Q=45^\circ$、$\omega=-0.1$ rad/s では回転方向が逆になります。$v_x=-150\sin45^\circ\cdot(-0.1)\approx+10.61$ mm/s、$v_y=150\cos45^\circ\cdot(-0.1)\approx-10.61$ mm/s。先端は右下へ動きますが、速さは $L|\omega|=15$ mm/s のままです。
3. $L_1=100$ mm、$L_2=50$ mm、$Q_1=30^\circ$、$Q_2=60^\circ$、$\omega_1=0.1$ rad/s、$\omega_2=0.2$ rad/s のとき、第2リンクの絶対方向は $Q_1+Q_2=90^\circ$、角速度は $\omega_1+\omega_2=0.3$ rad/s です。したがって $v_x=-100\sin30^\circ\cdot0.1-50\sin90^\circ\cdot0.3=-5-15=-20$ mm/s、$v_y=100\cos30^\circ\cdot0.1+50\cos90^\circ\cdot0.3\approx+8.66$ mm/s となります。
4. 折り畳み位置から $\delta=0.02$ rad 開いたとき、第1リンクの**固定軸**方向の変化は約 $25\delta^2=25\cdot0.02^2=0.010$ mm、横方向変位は $50\delta=1.000$ mm、半径方向の増加は $50\delta^2=0.020$ mm です。二つの二次項の係数を混同しないでください。

[三角関数](../TRIGONOMETRY.md) · [座標系](04-coordinate-frames.md) · [微積分の基礎](00-calculus-foundations.md)
