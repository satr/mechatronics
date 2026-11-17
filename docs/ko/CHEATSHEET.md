# 공식 요약 — 운동과 일차 시스템

**언어:** [en](../en/CHEATSHEET.md) · [fr](../fr/CHEATSHEET.md) · [de](../de/CHEATSHEET.md) · [it](../it/CHEATSHEET.md) · [es](../es/CHEATSHEET.md) · [pt](../pt/CHEATSHEET.md) · [zh](../zh/CHEATSHEET.md) · [ja](../ja/CHEATSHEET.md) · [nb](../nb/CHEATSHEET.md) · [ru](../ru/CHEATSHEET.md) · [ko](CHEATSHEET.md) · [fi](../fi/CHEATSHEET.md) · [pl](../pl/CHEATSHEET.md)

**이 페이지의 단위(예제 전에 설명):** `s` — 초; `m` — 미터; `m/s` — 미터 / 초 — 선속도; `rad/s` — 라디안 / 초 — 각속도; `kg·m²` — 킬로그램 · 미터² — 관성 모멘트; `N·m` — 뉴턴 · 미터 — 토크; `N·m·s/rad` — 뉴턴 · 미터 · 초 / 라디안 — 속도에 대한 이득; `J` — 줄; `mm` — 밀리미터 = 0.001 m; `mm/s` — 밀리미터 / 초 — 선속도; `%` — 퍼센트(100분의 1). [단위 전체 목록](UNITS.md).

[목차](README.md) · [운동](notes/01-motion-calculus.md) · [동역학](notes/02-first-order-dynamics.md) · [연습 문제](exercises/README.md)

> **공학 설계 명세가 아닙니다.** 사용 전에 단위와 이상화 가정을 확인하세요.

| 개념 | 정의 또는 식 |
| --- | --- |
| 변위 | $\Delta x=x_2-x_1$ (부호 있음) |
| 이동 거리 | $s=\int_{t_1}^{t_2}\lvert v(t)\rvert\ \mathrm{d}t\ge 0$ (0 이상) |
| 평균 속도(벡터 성분) | $\bar v=\frac{\Delta x}{\Delta t}$ (1차원에서 부호 있음) |
| 평균 속력 | $\frac{s}{\Delta t}$ (0 이상) |
| 순간 속도 | $v(t)=\frac{dx}{dt}$  |
| 속도로부터 변위 | $\Delta x=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t$  |
| 명시적 오일러 적분 | $x_{n+1}=x_n+v_n\ dt$  |
| 일차 동역학 | $\frac{dv}{dt}=\frac{u-v}{\tau}$  |
| 속도 오차 | $\varepsilon(t)=u-v(t)$  |
| 정확한 계단 응답 | $v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right)$ ($u$가 일정할 때) |
| 시정수 | $t=\tau$일 때 전체 변화량의 약 63.2 %가 완료됨 |
| 단순화된 토크 모델 | $M=K(u-\omega)$  |
| 회전 가속도 | $M=J\alpha,\quad\alpha=\frac{d\omega}{dt}$  |
| 모델의 시정수 | $\tau=\frac{J}{K}$ (토크 모델의 가정 아래에서만) |
| 회전 운동 에너지 | $E=\frac{1}{2}J\omega^2$  |

**표기:** $\varepsilon$은 속도 오차, $\mathrm{e}\approx2.71828$은 오일러 수입니다. $\exp(z)=\mathrm{e}^{z}$는 자연 지수함수이며 두 기호는 서로 관련이 없습니다.

**SI 단위:**

| 기호 | 이름 | 단위 |
| --- | --- | --- |
| `t, dt, τ` | 시간 | s (초) |
| `x` | 위치 | m (미터) |
| `v` | 속력 | m/s (초당 미터) |
| `ω` | 각속도 | rad/s (초당 라디안) |
| `J` | 관성모멘트 | kg·m² |
| `M` | 토크 | N·m |
| `K` | 토크 이득 | N·m·s/rad |
| `E` | 에너지 | J (줄) |

가운데점 `·`는 목록 구분자가 아니라 곱셈을 뜻합니다. 선형 모델에서 $u$는 선속도, 회전 모델에서는 각속도입니다.

**흔한 실수:** 속력과 부호 있는 속도는 다릅니다. 이동 거리와 변위도 다릅니다. 시간 간격 $dt$는 시정수 $\tau$가 아닙니다. 한 시정수가 지났다고 목표값에 완전히 도달한 것은 아닙니다. $J/K$는 모든 모터에 적용되는 일반 법칙이 아닙니다. 기계적 에너지는 전기 입력 소비량과 같지 않습니다.

[미분과 적분에 대한 추가 설명](notes/01-motion-calculus.md#section-6) · [모델 가정과 오일러 안정성](notes/02-first-order-dynamics.md#section-7)

[시정수 백분율 계산](notes/02-first-order-dynamics.md#time-constant-derivation)

[값 3, 3.8 및 3.98의 계산](notes/01-motion-calculus.md#motion-values-derivation)

## 기호와 표기법

**Σ / ∑ (합산)** 는 항들을 더한다는 뜻입니다. 예: $\sum_{n=1}^{3}n=1+2+3=6$. 위아래 범위는 더할 항을 결정합니다. [기호 설명](SYMBOLS.md).

## 적분 참고표

[미적분 기초](notes/00-calculus-foundations.md) · [적분 참고표](INTEGRAL_TABLE.md)

## 피드백 제어: PID와 유지 토크

| $\varepsilon=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}}$ | $u_P=K_p\varepsilon$, $u_I=K_i\int\varepsilon\ \mathrm{d}t$ |
| --- | --- |
| $M_{\mathrm{motor}}=K_t I$ | $\lvert M_g\rvert=mgL\lvert\cos\theta\rvert$ |

[PID와 유지 토크](notes/03-feedback-control.md) · [삼각함수표와 기계 예제](TRIGONOMETRY.md)

<a id="joint-velocity"></a>
## 회전, 속도 및 야코비안

관절 각속도는 rad/s, 길이가 mm일 때 선속도는 mm/s입니다.

$$
v_x=-L\sin Q\cdot\dot Q,\qquad v_y=L\cos Q\cdot\dot Q
$$

$$
\det J=L_1L_2\sin Q_2
$$

[회전, 속도와 야코비안](notes/05-velocity-jacobian.md)
