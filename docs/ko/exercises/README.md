# Python 연습 문제 — 한국어

**다른 언어:** [en](../../en/exercises/README.md) · [fr](../../fr/exercises/README.md) · [de](../../de/exercises/README.md) · [it](../../it/exercises/README.md) · [es](../../es/exercises/README.md) · [pt](../../pt/exercises/README.md) · [zh](../../zh/exercises/README.md) · [ja](../../ja/exercises/README.md) · [nb](../../nb/exercises/README.md) · [ru](../../ru/exercises/README.md) · [ko](README.md) · [fi](../../fi/exercises/README.md) · [pl](../../pl/exercises/README.md)

[목차](../README.md) · [운동](../notes/01-motion-calculus.md) · [동역학](../notes/02-first-order-dynamics.md) · [공식 요약](../CHEATSHEET.md)

기본 Python 예제 세 개는 표준 라이브러리만 사용합니다. 그래프는 NumPy와 Matplotlib를 사용하며, 선택 사항인 로컬 노트북에는 JupyterLab이 필요합니다. [Python 공식 다운로드](https://www.python.org/downloads/) · [venv 공식 문서](https://docs.python.org/3/library/venv.html).

핵심 스크립트를 실행하는 데 추가 패키지를 설치할 필요는 없습니다. Windows에서는 가상 환경 활성화 전 `python3` 대신 `py -3`를 사용하거나, 활성화 후 `python`을 사용하세요.

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
python3 -m unittest discover -s tests -v
```

**Python 소스 코드**

- [운동과 적분](../../../exercises/01_motion_and_integral.py)
- [일차 응답](../../../exercises/02_first_order_response.py)
- [회전 에너지](../../../exercises/03_rotation_energy.py)
- [그래프 생성](../../../exercises/plot_models.py) — NumPy와 Matplotlib 필요

## 그래프와 노트북을 위한 선택적 로컬 환경

위의 기본 스크립트는 추가 패키지가 필요하지 않습니다. 그래프 또는 JupyterLab을 사용할 때만 저장소 루트에서 가상 환경을 만드세요. [공식 venv 문서](https://docs.python.org/3/library/venv.html)와 [Python Packaging 안내서](https://packaging.python.org/en/latest/tutorials/installing-packages/)를 참고하세요.

**macOS / Linux:**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

**Windows (PowerShell):**

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

선택적 의존성은 [requirements.txt](../../../requirements.txt)에 있습니다. 소스 코드를 검토한 후 저장소 루트에서 기본 스크립트를 실행하세요.

## 추가 연습

1. $x(t)=2t^2$에서 $v(t)=4t$를 유도하고 유한차분과 비교하세요.
2. $t$를 초 단위로 두고 $v(t)=(3+4t)\ \mathrm{mm/s}$를 $0$초부터 $2$초까지 적분해 변위 $14\ \mathrm{mm}$를 확인하세요.
3. $\tau=0.5$ s인 일차 시스템을 $\Delta t=0.05$ s와 $0.5$ s로 시뮬레이션하고, 각 경우의 결과를 해석해와 비교하여 수치 오차를 확인하세요.
4. $L_1=L_2=0.1$ m, $q_1=0$, $q_2=90^\circ$에서 끝점 $(0.1, 0.1)$ m를 계산하세요.
5. 출력 포화가 있는 PID 시뮬레이션에서 적분 누적을 관찰하세요.

이 예제는 교육용 시뮬레이션입니다. 실제 CNC나 로봇의 구동 명령으로 사용하지 마세요.

