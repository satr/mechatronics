# 数式の記号と表記

**このページの言語を切り替える:** [en](../en/SYMBOLS.md) · [fr](../fr/SYMBOLS.md) · [de](../de/SYMBOLS.md) · [it](../it/SYMBOLS.md) · [es](../es/SYMBOLS.md) · [pt](../pt/SYMBOLS.md) · [zh](../zh/SYMBOLS.md) · [ja](SYMBOLS.md) · [nb](../nb/SYMBOLS.md) · [ru](../ru/SYMBOLS.md) · [ko](../ko/SYMBOLS.md) · [fi](../fi/SYMBOLS.md) · [pl](../pl/SYMBOLS.md)

**このページの単位（例の前に説明）:** `s` — 秒; `mm` — ミリメートル = 0.001 m; `mm/s` — ミリメートル / 秒 — 線速度; `kg·m²` — キログラム · メートル² — 慣性モーメント; `N·m` — ニュートン · メートル — トルク; `N·m·s/rad` — ニュートン · メートル · 秒 / ラジアン — 速度に対するゲイン; `rpm` — 毎分回転数; `rad/s` — ラジアン / 秒 — 角速度; `%` — パーセント（百分の一）. [単位一覧](UNITS.md).

[← README](README.md) · [公式早見表](CHEATSHEET.md) · [運動](notes/01-motion-calculus.md) · [動力学](notes/02-first-order-dynamics.md)

## 目次

- [総和：大文字の sigma](#summation)
- [間違えやすい記号](#different-symbols)
- [Markdown の数式表記](#math-delimiters)
- [小数点・SI 単位・数式の間隔](#si-notation)

<a id="summation"></a>

## Σ / ∑ — 総和 (summation)

記号 $\sum$（ギリシャ大文字の sigma、**総和記号** / summation）は、項を順番に足し合わせる意味です。$\sum_{n=0}^{N-1}(2nh)h$ では、添字 $n$ が $0; 1; \ldots; N-1$ と動き、全部で $N$ 項あります。Python の `for` ループで加算を繰り返すことに相当します。例えば $\sum_{n=1}^{3}n=1+2+3=6$ です。

<a id="different-symbols"></a>

## 似ている記号でも意味は異なる

小文字の $\varepsilon(t)$（epsilon）は速度誤差 (speed error) です。定数 $\mathrm{e}\approx2.71828$ はオイラー数 (Euler’s number) です。$\tau$（tau）は時定数 (time constant)、$\omega$（omega）は角速度 (angular velocity)、$\alpha$（alpha）は角加速度 (angular acceleration)、$\Delta$（delta）は変化量 (change) を表します。小文字の $\sigma$（sigma）は別の記号で、標準偏差や応力など、文脈によって意味が異なります。

<a id="math-delimiters"></a>

## ドル記号 `$` が表示されるのはなぜ？

Markdown の**ソース**では、`$...$` が行内数式、`$$...$$` が独立した数式の区切りです。この記号は数式の内容ではなく、GitHub の通常表示では消えるはずです。表示される場合は、ソース表示やリンク中の数式、Markdown の書式を確認してください。

[GitHub — Markdown / MathJax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

<a id="si-notation"></a>

## 小数点・SI 単位・数式の間隔

全言語版で小数点 `.` を統一します（`0.5`、`3.8`、`63.2 %`）。コンマは列挙の区切りには使えますが、数値と単位の間や被積分関数と `dt` の間には置きません。数値と単位の間には空白を入れます：`1 s`（秒、second）、`4 mm`（ミリメートル、millimetre）、`10 mm/s`（ミリメートル毎秒、millimetres per second）。単位の積は中点 `·`（`kg·m²`、`N·m·s/rad`）、除算の `/` の両側には空白を置きません。数式では `\mathrm{kg}\cdot\mathrm{m}^2`、微分は `\mathrm{d}t` と書きます。[BIPM の SI 文書](https://www.bipm.org/en/publications/si-brochure) で認められた小数点表記です。コードの `dt` は有限の時間刻み（time step）、積分の `\mathrm{d}t` は微分（differential）です。


### rpm and rad/s

`rpm` は **毎分回転数**（revolutions per minute）を表す**非 SI** 単位です。SI の角速度単位は `rad/s`（ラジアン毎秒、radians per second）です。換算は `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`、したがって `1000 rpm ≈ 104.72 rad/s` です。