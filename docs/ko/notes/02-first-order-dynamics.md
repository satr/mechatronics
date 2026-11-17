# 2. 일차 동역학, 토크와 회전 에너지

**언어:** [en](../../en/notes/02-first-order-dynamics.md) · [fr](../../fr/notes/02-first-order-dynamics.md) · [de](../../de/notes/02-first-order-dynamics.md) · [it](../../it/notes/02-first-order-dynamics.md) · [es](../../es/notes/02-first-order-dynamics.md) · [pt](../../pt/notes/02-first-order-dynamics.md) · [zh](../../zh/notes/02-first-order-dynamics.md) · [ja](../../ja/notes/02-first-order-dynamics.md) · [nb](../../nb/notes/02-first-order-dynamics.md) · [ru](../../ru/notes/02-first-order-dynamics.md) · [ko](02-first-order-dynamics.md) · [fi](../../fi/notes/02-first-order-dynamics.md) · [pl](../../pl/notes/02-first-order-dynamics.md)

**이 페이지의 단위(예제 전에 설명):** `s` — 초; `mm/s` — 밀리미터 / 초 — 선속도; `kg` — 킬로그램; `m` — 미터; `rad/s` — 라디안 / 초 — 각속도; `N` — 뉴턴; `N·m` — 뉴턴 · 미터 — 토크; `J` — 줄; `rpm` — 분당 회전수; `kg·m²` — 킬로그램 · 미터² — 관성 모멘트; `N·m·s/rad` — 뉴턴 · 미터 · 초 / 라디안 — 속도에 대한 이득; `%` — 퍼센트(100분의 1); `rad` — 라디안. [단위 전체 목록](../UNITS.md).

[미적분 복습](00-calculus-foundations.md) · [적분표](../INTEGRAL_TABLE.md) · [목차](../README.md) · [공식 요약](../CHEATSHEET.md) · [연습](../exercises/README.md) · [이전 장](01-motion-calculus.md)

> **정확도 안내:** 다음 모터 모델은 부하, 마찰, 지연, 전압 제한, 포화 및 고차 동역학이 없는 이상적인 비례 토크 제어를 가정합니다. 모든 모터에 적용되는 일반 법칙이 아닙니다.

## 빠른 복습

- **시정수(time constant)** $\tau$는 일차 시스템이 새로운 평형값에 접근하는 속도를 나타냅니다.
- 수치 계산의 시간 간격 `dt`는 근사 정확도에 영향을 주지만 물리적 시정수 $\tau$를 바꾸지 않습니다.
- 이상적인 회전 시스템에서 관성 모멘트 $J$와 비례 토크 계수 $K$에 대해 $\tau=J/K$입니다.
- $J/K$가 같으면 속도 응답이 같을 수 있지만 필요한 토크와 저장되는 운동 에너지는 다릅니다.

## 내용

- [1. 일차 속도 응답](#section-1)
- [2. 시정수를 결정하는 요소](#section-2)
- [3. 수치 시간 간격과 시정수](#section-3)
- [4. 측정 데이터에서 시정수 추정](#section-4)
- [5. 토크와 회전 에너지](#section-5)
- [6. 직접 실험](#section-6)
- [7. 추가 설명](#section-7)
  - [63.2 %, 86.5 %, 95.0 %의 유도](#time-constant-derivation)
  - [오일러 수치의 유도](#euler-values-derivation)

[SI 단위와 표기](../SYMBOLS.md)

<a id="section-1"></a>
## 1. 일차 속도 응답

목표 속도 $u$가 일정하고 실제 속도가 $v$, 시정수가 $\tau>0$라고 합시다. 속도 오차 $\varepsilon(t)=u-v(t)$는 그리스 문자 엡실론으로 나타냅니다. 자연지수함수는 $\exp(z)=\mathrm{e}^z$이며 $\mathrm{e}\approx2.71828$은 **오일러 수**이지 속도 오차가 아닙니다. 혼동하지 않도록 다른 기호를 사용합니다.


$$
\frac{dv}{dt}=\frac{u-v}{\tau},\qquad
v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right).
$$


$u$와 초기 속도 $v_0$가 일정한 조건에서 위 식의 정확한 해는 두 번째 식입니다. 시정수 하나가 지나면 초기값에서 최종값까지 변화량의 $1-\exp(-1)\approx63.2\ \%$가 완료됩니다. 두 시정수에서는 86.5 %, 세 시정수에서는 95.0 %입니다. 따라서 $\tau=2\ \mathrm{s}$라면 2초 후 변화량의 약 63.2 %에 도달한다는 뜻이지 **정확히 목표에 도달한다는 뜻은 아닙니다**.

![일차 시스템의 정규화된 계단 응답](../../../assets/figures/first_order_response.svg)

[백분율의 유도 과정](#time-constant-derivation).

<a id="section-2"></a>
## 2. 시정수를 결정하는 요소

매우 단순화한 회전 시스템에 뉴턴의 회전 운동 법칙을 적용하면

$$
J\frac{d\omega}{dt}=M.
$$

$J$는 관성 모멘트(kg·m²), $\omega$는 각속도(rad/s), $M$은 **실제 순토크**(N·m)입니다. 제어기는 전기 구동 명령을 계산하지만 물리적 토크는 모터가 발생시킵니다. 소프트웨어 자체가 토크를 생성한다고 표현하면 부정확합니다.

모터와 드라이브가 속도 오차에 비례하는 토크를 낼 수 있다고 가정합니다.

$$
M=K(u-\omega).
$$

이 회전 운동 예제에서 $u$는 1절의 선속도 목표값(mm/s)이 아니라 **목표 각속도**(rad/s)를 뜻합니다. $u$와 $\omega$는 같은 각속도 단위를 사용해야 합니다. 그렇지 않으면 $u-\omega$와 토크 식의 차원이 맞지 않습니다.

여기서 $K$는 토크/속도오차 비례계수이며 단위는 N·m·s/rad입니다. 이 가정 아래에서

$$
\frac{d\omega}{dt}=\frac{K}{J}(u-\omega),\qquad \tau=\frac{J}{K}.
$$

$K$가 일정할 때 $J$를 두 배로 늘리면 $\tau$가 두 배가 되고 같은 속도 오차에서 가속도는 감소합니다. $J$와 $K$를 함께 두 배로 늘리면 $\tau$는 같지만 동일한 오차에서 필요한 토크는 두 배가 됩니다. **$J$는 마찰력이 아닙니다.** 각속도의 변화에 대한 저항을 나타내는 관성 모멘트입니다. 실제 모델에는 부하 토크, 마찰, 전기 동역학, 비선형 전류 제한과 추가 상태 변수가 필요할 수 있습니다.

제어기는 드라이브에 명령을 내리고, 물리적 토크는 모터가 생성하는 이상화된 피드백 구조입니다.

![이상적인 제어기·드라이브·모터 피드백 구조](../../../assets/figures/control_loop.svg)

<a id="section-3"></a>
## 3. 수치 시간 간격과 시정수

일차 방정식에 명시적 오일러 방법을 적용하면

$$
v_{n+1}=v_n+\frac{u-v_n}{\tau}\ dt.
$$

$u=10\ \mathrm{mm/s}$, $v_0=0$, $\tau=1\ \mathrm{s}$일 때 1초 후의 결과는 다음과 같습니다.

| 방법 | $v(1\ \mathrm{s})$ |
| --- | ---: |
| 오일러, $dt=0.1\ \mathrm{s}$ | $6.513\ \mathrm{mm/s}$ |
| 오일러, $dt=0.01\ \mathrm{s}$ | $6.340\ \mathrm{mm/s}$ |
| 정확한 해 | $6.321\ \mathrm{mm/s}$ |

`dt`를 바꾸면 계산 갱신 횟수가 달라집니다. 실제 모델의 모터가 빨라지는 것은 아닙니다. 수치 안정성과 오차는 `dt`, $\tau$, 선택한 적분법에 좌우됩니다. [수치의 계산 과정](#euler-values-derivation).

<a id="section-4"></a>
## 4. 측정 데이터에서 시정수 추정

0에서 1000 rpm으로 변화하는 깨끗한 일차 계단 응답에서 2초 후 약 632 rpm에 도달했다면 $\tau\approx2\ \mathrm{s}$라고 추정할 수 있습니다. 반드시 **초기 정상값에서 최종 정상값까지의 변화량**의 63.2 %를 사용하세요. 명령의 절대값에 63.2 %를 곱하는 것이 항상 맞지는 않습니다. 실제 측정에는 잡음, 샘플링 오차, 지연, 오버슈트가 있을 수 있습니다.

**코드가 반환하는 시간의 의미:** [`estimate_tau`](../../../exercises/02_first_order_response.py)는 목표값이 변한 시각을 기준으로 시간표시가 **엄격히 증가하는** 측정값을 받습니다. 전체 변화량의 63.2 %에 도달했다고 **처음 관측된 샘플의 시각**을 반환하며, 알려진 측정 분해능의 절반을 반올림 허용 오차로 사용합니다. 1 s에 측정한 뒤 2 s 샘플에서 처음 문턱을 넘었다면, 실제 교차는 **두 샘플 사이**에 발생했을 수 있습니다. 따라서 2 s는 샘플 간격에 제한된 추정값이지 정확한 곡선 피팅 결과가 아닙니다. 문턱을 넘은 뒤에도 잘못된 측정값, 중복 시각, 역순 시각은 거부합니다. 문턱에 도달하지 않으면 `None`을 반환합니다.

**측정 분해능이 중요합니다:** `estimate_tau`의 `resolution`은 **전체 속도 변화량의 절댓값보다 작아야** 합니다. 속도가 0에서 10 rpm으로 변하지만 표시값이 10 rpm 단위로만 바뀐다면 63.2 % 문턱을 지나는 시각을 신뢰성 있게 추정할 수 없습니다. 함수는 첫 샘플에서 문턱을 넘었다는 잘못된 결과를 내는 대신 입력을 거부합니다. 분해능이 충분하더라도 추정값은 샘플링 간격의 제한을 받습니다.

<a id="section-5"></a>
## 5. 토크와 회전 에너지

각가속도 $\alpha=d\omega/dt$에 대해

$$
M=J\alpha,\qquad E=\frac12J\omega^2.
$$

$\omega=10\ \mathrm{rad/s}$에서 $J=2\ \mathrm{kg}\cdot\mathrm{m}^2$이면 $E=100\ \mathrm{J}$입니다. $J$를 두 배로 하면 200 J이고, $J$가 일정할 때 $\omega$를 두 배로 하면 에너지는 네 배가 됩니다. 이는 **기계적 운동 에너지**이며 전원에서 소비한 전기 에너지가 아닙니다. 손실과 효율을 고려해야 합니다.

<a id="section-6"></a>
## 6. 직접 실험

[`02_first_order_response.py`](../../../exercises/02_first_order_response.py)와 [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py)를 실행하세요. 선택적으로 [`plot_models.py`](../../../exercises/plot_models.py)로 그래프를 생성할 수 있습니다. 모두 가상 수치를 사용하며 하드웨어 인터페이스가 없습니다.


<a id="section-7"></a>
## 7. 추가 설명(선택)

### 오일러 계산이 불안정해지는 조건

이 일차 방정식에서 한 번의 오일러 계산은 **남은 속도 오차**에 $1-dt/\tau$를 곱합니다. 수렴하려면 $0<dt<2\tau$여야 합니다. $\tau<dt<2\tau$에서는 계산값이 목표를 중심으로 진동하면서 수렴합니다. 이는 **수치적 방법의 성질**이지 실제 모터가 진동한다는 뜻이 아닙니다. 정확도를 높이려면 시간 간격을 줄이세요.

### 토크 모델의 한계

보다 일반적인 식은

$$
J\frac{d\omega}{dt}=M_{\text{motor}}-M_{\text{load}}-M_{\text{friction}}.
$$

$\tau=J/K$는 순토크가 $K(u-\omega)$라는 특별한 이상화에서만 성립합니다. 실제 드라이브의 포화, 센서 지연, 마찰, 추가 전기 상태는 응답을 바꿉니다.

### 에너지와 출력

$J$가 일정할 때 회전 운동 에너지 변화는 $\Delta E=\frac12J(\omega_2^2-\omega_1^2)$이고 순간 **기계 출력**은 $P=M\omega$입니다. 두 식만으로는 실제 전기 입력 에너지를 구할 수 없습니다.

<a id="time-constant-derivation"></a>
### 63.2 %, 86.5 %, 95.0 %가 나오는 이유

이 비율과 지수함수는 **같은 방정식**에서 나옵니다. 오차를 $\varepsilon(t)=u-v(t)$로 정의합니다. 여기서 $\varepsilon$은 오일러 수 $\mathrm{e}$와 다릅니다. $u$가 일정하면 $d\varepsilon/dt=-dv/dt$이므로

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

변수분리 단계에서는 $\varepsilon$으로 나누므로 초기 오차가 0이 아닌 경우를 가정합니다. $u=v_0$이면 오차는 항상 0이고, 원래 미분방정식에서 상수해 $v(t)=u$를 바로 얻습니다.

$$
f(t)=\frac{v(t)-v_0}{u-v_0}=1-\exp\!\left(-\frac{t}{\tau}\right),\qquad (u\ne v_0).
$$

| 시간 | 완료된 변화 비율 $f(t)$ |
| ---: | ---: |
| $\tau$ | $1-\exp(-1)=0.63212056\ldots\approx63.2\ \%$ |
| $2\tau$ | $1-\exp(-2)=0.86466472\ldots\approx86.5\ \%$ |
| $3\tau$ | $1-\exp(-3)=0.95021293\ldots\approx95.0\ \%$ |

0에서 1000 rpm으로 변할 때 각각 약 632, 865, 950 rpm에 해당합니다. 이상적인 모델은 목표값에 점근적으로 접근합니다.

<a id="euler-values-derivation"></a>
### 오일러 수치의 계산 과정

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
