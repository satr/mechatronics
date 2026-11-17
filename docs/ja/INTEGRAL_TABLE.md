# 積分公式表

**言語:** [en](../en/INTEGRAL_TABLE.md) · [fr](../fr/INTEGRAL_TABLE.md) · [de](../de/INTEGRAL_TABLE.md) · [it](../it/INTEGRAL_TABLE.md) · [es](../es/INTEGRAL_TABLE.md) · [pt](../pt/INTEGRAL_TABLE.md) · [zh](../zh/INTEGRAL_TABLE.md) · [ja](INTEGRAL_TABLE.md) · [nb](../nb/INTEGRAL_TABLE.md) · [ru](../ru/INTEGRAL_TABLE.md) · [ko](../ko/INTEGRAL_TABLE.md) · [fi](../fi/INTEGRAL_TABLE.md) · [pl](../pl/INTEGRAL_TABLE.md)

**このページの単位（例の前に説明）:** `s` — 秒; `mm` — ミリメートル = 0.001 m; `mm/s` — ミリメートル / 秒 — 線速度; `mm/s²` — ミリメートル / 秒² — 加速度; `N` — ニュートン; `m` — メートル; `N/m` — ニュートン / メートル — 剛性; `J` — ジュール. [単位一覧](UNITS.md).

[README](README.md) · [0. 微積分の基礎：導関数・微分・積分](notes/00-calculus-foundations.md) · [記号](SYMBOLS.md)

不定積分（indefinite integral）には積分定数 +C が付きます。a は定数で、被積分関数が定義される区間で用います。三角関数の角度はラジアン（rad、radian）です。

最初は多項式を練習し、三角関数や根号を含む積分は後で学べます。

## 目次

- [べき関数と対数](#section-1)
- [指数関数](#section-2)
- [三角関数](#section-3)
- [有理式と逆三角関数](#section-4)
- [発展：根号と逆数三角関数](#section-5)
- [公式の選び方と検算](#section-6)

<a id="section-1"></a>
## 1. べき関数と対数

| 積分公式 | 条件・説明 |
| --- | --- |
| $\int 1\ \mathrm{d}x=x+C$ | すべての実数 $x$ |
| $\int x^n\ \mathrm{d}x=\frac{x^{n+1}}{n+1}+C$ | $n\ne-1$; 実数べきの定義域に注意 |
| $\int\frac{1}{x}\ \mathrm{d}x=\ln\lvert x\rvert+C$ | $x\ne0$ |

<a id="section-2"></a>
## 2. 指数関数

| 積分公式 | 条件・説明 |
| --- | --- |
| $\int \mathrm{e}^{x}\ \mathrm{d}x=\mathrm{e}^{x}+C$ | すべての実数 $x$ |
| $\int a^x\ \mathrm{d}x=\frac{a^x}{\ln a}+C$ | $a>0$, $a\ne1$ |

<a id="section-3"></a>
## 3. 三角関数

| 積分公式 | 条件・説明 |
| --- | --- |
| $\int\sin x\ \mathrm{d}x=-\cos x+C$ | $x$ はラジアン |
| $\int\cos x\ \mathrm{d}x=\sin x+C$ | $x$ はラジアン |
| $\int\frac{1}{\cos^2 x}\ \mathrm{d}x=\tan x+C$ | $\cos x\ne0$ |
| $\int\frac{1}{\sin^2 x}\ \mathrm{d}x=-\cot x+C$ | $\sin x\ne0$ |

<a id="section-4"></a>
## 4. 有理式と逆三角関数

| 積分公式 | 条件・説明 |
| --- | --- |
| $\int\frac{1}{1+x^2}\ \mathrm{d}x=\arctan x+C$ | すべての実数 $x$ |
| $\int\frac{1}{\sqrt{1-x^2}}\ \mathrm{d}x=\arcsin x+C$ | $\lvert x\rvert<1$ |
| $\int\frac{1}{a^2+x^2}\ \mathrm{d}x=\frac{1}{a}\arctan\frac{x}{a}+C$ | $a>0$ |
| $\int\frac{1}{a^2-x^2}\ \mathrm{d}x=\frac{1}{2a}\ln\left\lvert\frac{a+x}{a-x}\right\rvert+C$ | $a>0$, $x\ne\pm a$ |
| $\int\frac{1}{\sqrt{a^2-x^2}}\ \mathrm{d}x=\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |

<a id="section-5"></a>
## 5. 発展：根号と逆数三角関数

| 積分公式 | 条件・説明 |
| --- | --- |
| $\int\frac{1}{\sqrt{x^2+a^2}}\ \mathrm{d}x=\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{a^2-x^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{a^2-x^2}+\frac{a^2}{2}\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |
| $\int\sqrt{x^2+a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2+a^2}+\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{x^2-a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2-a^2}-\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2-a^2}\right\rvert+C$ | $a>0$, $\lvert x\rvert>a$ |
| $\int\frac{1}{\sin x}\ \mathrm{d}x=\ln\left\lvert\tan\frac{x}{2}\right\rvert+C$ | $\sin x\ne0$; 特異点をまたがない区間 |
| $\int\frac{1}{\cos x}\ \mathrm{d}x=\ln\left\lvert\tan\left(\frac{x}{2}+\frac{\pi}{4}\right)\right\rvert+C$ | $\cos x\ne0$; 特異点をまたがない区間 |

## 式の確認

右辺を微分して積分公式を確認できます。べき関数では微分則の逆をたどります。

対数の引数は無次元である必要があります。基準尺度がなければ x は無次元とします。± の符号は被積分関数と定義域に合わせて選びます。

<a id="section-6"></a>
## 6. 公式の選び方と検算

まず微分記号（dx、dt、dθ）の変数を確認します。係数はその変数に依存しない場合に限り定数です。不定積分には C を付け、定積分では原始関数 F の F(b) − F(a) を計算します。微分して検算できます。

### 例 A — 速度から変位を求める

0–2 s で v(t) = 3 mm/s + (4 mm/s²)t の各項を積分します。

$$
\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}
=14\ \mathrm{mm}.
$$

結果は 14 mm であり 14 mm/s ではありません。速度の時間積分が変位です。

### 例 B — 変化する力の仕事

ばね F(x) = kx、k = 200 N/m を 0 から 0.01 m まで伸ばします。

$$
\int_0^{0.01\ \mathrm{m}}(200\ \mathrm{N/m})x\ \mathrm{d}x
=\left[(100\ \mathrm{N/m})x^2\right]_0^{0.01\ \mathrm{m}}=0.01\ \mathrm{J}.
$$

仕事は 0.01 J。最終的な力を全距離に掛けるのは誤りです。

### 例 C — 単純な関数から対数

1/x の原始関数は ln|x| です。無次元の x を 1 から 2 まで変化させると：

$$
\int_1^2\frac1x\ \mathrm{d}x=[\ln x]_1^2=\ln2-\ln1=\ln2\approx0.693.
$$

結果は ln 2 ≈ 0.693。x は長さではなく無次元比です。
