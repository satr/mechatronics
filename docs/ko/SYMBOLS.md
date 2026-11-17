# 기호와 표기법

**언어:** [en](../en/SYMBOLS.md) · [fr](../fr/SYMBOLS.md) · [de](../de/SYMBOLS.md) · [it](../it/SYMBOLS.md) · [es](../es/SYMBOLS.md) · [pt](../pt/SYMBOLS.md) · [zh](../zh/SYMBOLS.md) · [ja](../ja/SYMBOLS.md) · [nb](../nb/SYMBOLS.md) · [ru](../ru/SYMBOLS.md) · [ko](SYMBOLS.md) · [fi](../fi/SYMBOLS.md) · [pl](../pl/SYMBOLS.md)

**이 페이지의 단위(예제 전에 설명):** `s` — 초; `mm` — 밀리미터 = 0.001 m; `mm/s` — 밀리미터 / 초 — 선속도; `kg·m²` — 킬로그램 · 미터² — 관성 모멘트; `N·m` — 뉴턴 · 미터 — 토크; `N·m·s/rad` — 뉴턴 · 미터 · 초 / 라디안 — 속도에 대한 이득; `rpm` — 분당 회전수; `rad/s` — 라디안 / 초 — 각속도; `%` — 퍼센트(100분의 1). [단위 전체 목록](UNITS.md).

[목차](README.md) · [공식 요약](CHEATSHEET.md) · [운동](notes/01-motion-calculus.md) · [동역학](notes/02-first-order-dynamics.md)

## 내용

- [Σ: 합을 나타내는 대문자 시그마](#summation)
- [헷갈리기 쉬운 기호](#different-symbols)
- [Markdown 수식 구분자](#math-delimiters)
- [소수점, SI 단위 및 수학 표기](#si-notation)

<a id="summation"></a>
## Σ / ∑ — 합산

$\sum$는 그리스 대문자 **시그마(sigma)**이며 **합산(summation)**을 의미합니다. $\sum_{n=0}^{N-1}(2nh)h$에서는 $n$이 $0, 1,\ldots,N-1$의 값을 가지므로 총 $N$개 항을 더합니다. Python의 `for` 반복문에서 매번 한 항을 더하는 것과 같습니다. 예를 들어 $\sum_{n=1}^{3}n=1+2+3=6$입니다. 위아래 첨자는 합산 범위를 지정합니다.

<a id="different-symbols"></a>
## 비슷하지만 의미가 다른 기호

소문자 $\varepsilon(t)$ (엡실론)는 속도 오차이고, 직립체 상수 $\mathrm{e}\approx2.71828$은 자연로그의 밑인 오일러 수입니다. $\tau$ (타우)는 시정수, $\omega$ (오메가)는 각속도, $\alpha$ (알파)는 각가속도, $\Delta$ (델타)는 변화량을 나타냅니다. 소문자 $\sigma$ (시그마)는 별개의 기호로, 다른 문맥에서 표준편차나 응력을 뜻하기도 합니다. 기호의 의미는 항상 해당 장의 정의를 확인하세요.

<a id="math-delimiters"></a>
## Markdown 원문에 달러 기호가 보이는 이유

Markdown **소스**에서 `$...$`는 인라인 수식, `$$...$$`는 독립 수식 블록을 나타냅니다. 이 기호들은 수학식의 일부가 아니라 서식 구분자입니다. GitHub에서 렌더링된 문서에는 달러 기호가 그대로 표시되지 않아야 합니다. 표시된다면 소스 보기 모드인지, 링크 제목 안에 수식이 들어갔는지, Markdown 구문이 잘못됐는지 확인하세요. 이 문서의 탐색 링크는 수식 표기 대신 일반 텍스트를 사용합니다.

[GitHub 수식 작성 문서](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

<a id="si-notation"></a>
## 소수점, SI 단위 및 수학적 간격

번역문에서도 소수는 `0.5`, `3.8`, `63.2 %`처럼 **점**으로 표기합니다. 쉼표는 목록을 구분하지만 숫자와 단위 또는 미분 기호를 구분하지 않습니다. 값과 단위 사이에는 공백을 둡니다: `1 s`, `4 mm`, `10 mm/s`. 복합 단위에서 곱셈은 가운데점으로 나타냅니다(`kg·m²`, `N·m·s/rad`). 나눗셈 기호 주변에는 공백을 넣지 않습니다(`mm/s`, `mm / s`가 아님). 가운데점은 소수점이 아니라 곱셈을 뜻합니다. `1 N·m`는 1 뉴턴미터입니다.

수식에서는 `\mathrm{kg}\cdot\mathrm{m}^2`처럼 쓰고, 미분은 쉼표 뒤의 `dt`가 아니라 `\mathrm{d}t`로 나타냅니다. 표기 규칙의 근거는 [BIPM SI 브로셔](https://www.bipm.org/en/publications/si-brochure)이며 이 저장소에서는 허용되는 소수점 표기 중 점을 일관되게 사용합니다. Python에서 `dt`는 **유한한 시간 간격**이고 적분식의 $\mathrm{d}t$는 **미분소**입니다.

### rpm과 rad/s

`rpm`은 분당 회전수(revolutions per minute)이며 일반적으로 쓰이는 **비SI 단위**입니다. 각속도의 SI 표기는 `rad/s`(초당 라디안)입니다. 환산식은 `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`이므로 `1000 rpm ≈ 104.72 rad/s`입니다.
