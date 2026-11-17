# 적분 공식표

**언어:** [en](../en/INTEGRAL_TABLE.md) · [fr](../fr/INTEGRAL_TABLE.md) · [de](../de/INTEGRAL_TABLE.md) · [it](../it/INTEGRAL_TABLE.md) · [es](../es/INTEGRAL_TABLE.md) · [pt](../pt/INTEGRAL_TABLE.md) · [zh](../zh/INTEGRAL_TABLE.md) · [ja](../ja/INTEGRAL_TABLE.md) · [nb](../nb/INTEGRAL_TABLE.md) · [ru](../ru/INTEGRAL_TABLE.md) · [ko](INTEGRAL_TABLE.md) · [fi](../fi/INTEGRAL_TABLE.md) · [pl](../pl/INTEGRAL_TABLE.md)

**이 페이지의 단위(예제 전에 설명):** `s` — 초; `mm` — 밀리미터 = 0.001 m; `mm/s` — 밀리미터 / 초 — 선속도; `mm/s²` — 밀리미터 / 초² — 가속도; `N` — 뉴턴; `m` — 미터; `N/m` — 뉴턴 / 미터 — 강성; `J` — 줄. [단위 전체 목록](UNITS.md).

[README](README.md) · [도함수 공식표](DERIVATIVE_TABLE.md) · [미적분 기초](notes/00-calculus-foundations.md) · [기호](SYMBOLS.md) · [삼각함수](TRIGONOMETRY.md)

부정적분에는 적분상수 $C$를 더합니다. 매개변수 $a$는 상수이며, 삼각함수의 각도는 라디안으로 표시합니다. 적분식은 함수가 정의되는 구간에서 사용해야 합니다.

## 목차

- [거듭제곱과 로그](#section-1)
- [지수함수](#section-2)
- [삼각함수](#section-3)
- [유리함수와 역삼각함수](#section-4)
- [근호와 역수](#section-5)
- [공식 선택과 검증](#section-6)

먼저 다항식 적분을 익힌 뒤 선택적으로 삼각함수와 근호 공식을 사용하세요. 모든 부정적분에는 적분상수 $C$를 더합니다. 로그의 인수는 무차원이어야 하며, 별도 기준 척도가 없으면 이 표의 $x$는 무차원입니다. 정의역 조건을 반드시 지키세요.

<a id="section-1"></a>
## 1. 기본 거듭제곱과 로그

| 공식 | 조건 |
| --- | --- |
| $\int 1\ \mathrm{d}x=x+C$ | 모든 실수 $x$ |
| $\int x^n\ \mathrm{d}x=\frac{x^{n+1}}{n+1}+C$ | $n\ne-1$; 실수 거듭제곱의 정의역 확인 |
| $\int\frac{1}{x}\ \mathrm{d}x=\ln\lvert x\rvert+C$ | $x\ne0$ |

<a id="section-2"></a>
## 2. 지수함수

| 공식 | 조건 |
| --- | --- |
| $\int \mathrm{e}^{x}\ \mathrm{d}x=\mathrm{e}^{x}+C$ | 모든 실수 $x$ |
| $\int a^x\ \mathrm{d}x=\frac{a^x}{\ln a}+C$ | $a>0$, $a\ne1$ |

<a id="section-3"></a>
## 3. 삼각함수

| 공식 | 조건 |
| --- | --- |
| $\int\sin x\ \mathrm{d}x=-\cos x+C$ | $x$는 라디안 단위 |
| $\int\cos x\ \mathrm{d}x=\sin x+C$ | $x$는 라디안 단위 |
| $\int\frac{1}{\cos^2 x}\ \mathrm{d}x=\tan x+C$ | $\cos x\ne0$ |
| $\int\frac{1}{\sin^2 x}\ \mathrm{d}x=-\cot x+C$ | $\sin x\ne0$ |

<a id="section-4"></a>
## 4. 유리함수와 역삼각함수

| 공식 | 조건 |
| --- | --- |
| $\int\frac{1}{1+x^2}\ \mathrm{d}x=\arctan x+C$ | 모든 실수 $x$ |
| $\int\frac{1}{\sqrt{1-x^2}}\ \mathrm{d}x=\arcsin x+C$ | $\lvert x\rvert<1$ |
| $\int\frac{1}{a^2+x^2}\ \mathrm{d}x=\frac{1}{a}\arctan\frac{x}{a}+C$ | $a>0$ |
| $\int\frac{1}{a^2-x^2}\ \mathrm{d}x=\frac{1}{2a}\ln\left\lvert\frac{a+x}{a-x}\right\rvert+C$ | $a>0$, $x\ne\pm a$ |
| $\int\frac{1}{\sqrt{a^2-x^2}}\ \mathrm{d}x=\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |

<a id="section-5"></a>
## 5. 근호와 역수

| 공식 | 조건 |
| --- | --- |
| $\int\frac{1}{\sqrt{x^2+a^2}}\ \mathrm{d}x=\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{a^2-x^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{a^2-x^2}+\frac{a^2}{2}\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |
| $\int\sqrt{x^2+a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2+a^2}+\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{x^2-a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2-a^2}-\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2-a^2}\right\rvert+C$ | $a>0$, $\lvert x\rvert>a$ |
| $\int\frac{1}{\sin x}\ \mathrm{d}x=\ln\left\lvert\tan\frac{x}{2}\right\rvert+C$ | $\sin x\ne0$; 특이점을 가로지르지 않는 구간에서만 |
| $\int\frac{1}{\cos x}\ \mathrm{d}x=\ln\left\lvert\tan\left(\frac{x}{2}+\frac{\pi}{4}\right)\right\rvert+C$ | $\cos x\ne0$; 특이점을 가로지르지 않는 구간에서만 |

## 적분식 검산

부정적분의 오른쪽을 미분하면 원래 적분 함수가 나와야 합니다. 예를 들어 거듭제곱 공식의 지수와 계수를 역으로 미분해 확인하세요. 정적분은 원시함수 $F$를 구한 다음 $F(b)-F(a)$를 계산합니다.

<a id="section-6"></a>
## 6. 공식 선택과 검증

먼저 미분 기호 뒤의 적분 변수($\mathrm{d}x$, $\mathrm{d}t$, $\mathrm{d}\theta$)를 확인합니다. 실제 상수인 계수만 상수로 취급하세요. 부정적분에는 $C$를 더하고, 정적분에는 $F(b)-F(a)$를 사용합니다. 답을 미분해 검산합니다.

### 예제 A — 측정한 속도로부터 변위 계산

간단한 축 모델에서 $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$이고 시간은 0–2 s입니다. 각 항을 적분합니다.

$$
\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}
=14\ \mathrm{mm}.
$$

결과는 14 mm이지 14 mm/s가 아닙니다. 시간에 대해 속도를 적분했으므로 변위가 됩니다.

### 예제 B — 선형으로 증가하는 힘이 한 일

스프링 힘이 $F(x)=kx$, 강성이 $k=200\ \mathrm{N/m}$이고 0에서 0.01 m까지 늘어났다면 다음과 같습니다.

$$
\int_0^{0.01\ \mathrm{m}}(200\ \mathrm{N/m})x\ \mathrm{d}x
=\left[(100\ \mathrm{N/m})x^2\right]_0^{0.01\ \mathrm{m}}=0.01\ \mathrm{J}.
$$

결과는 0.01 J입니다. 변위에 대해 힘을 적분하면 기계적 일이 됩니다. 최종 힘에 전체 이동 거리를 곱하면 실제보다 크게 계산합니다.

### 예제 C — 간단한 변화율에서 나오는 로그

$1/x$의 원시함수는 $\ln|x|$입니다. 무차원 비율 $x$가 1에서 2로 변할 때:

$$
\int_1^2\frac1x\ \mathrm{d}x=[\ln x]_1^2=\ln2-\ln1=\ln2\approx0.693.
$$

결과는 $\ln2\approx0.693$입니다. 이는 미터 단위 길이의 로그가 아닙니다. 여기서 $x$는 무차원입니다.
