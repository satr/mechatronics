# 메카트로닉스 학습 자료 — 한국어

**언어:** [en](../en/README.md) · [fr](../fr/README.md) · [de](../de/README.md) · [it](../it/README.md) · [es](../es/README.md) · [pt](../pt/README.md) · [zh](../zh/README.md) · [ja](../ja/README.md) · [nb](../nb/README.md) · [ru](../ru/README.md) · [ko](README.md) · [fi](../fi/README.md) · [pl](../pl/README.md)

> [!WARNING]
> **주의:** AI의 도움으로 작성한 교육 자료에는 부정확한 내용, 누락 또는 잘못된 가정이 있을 수 있습니다. 수식과 단위를 독립적으로 검증하세요. 실제 장비 제어에 사용하지 마세요.

## 목차

1. [미적분 기초: 도함수, 미분소, 적분](notes/00-calculus-foundations.md)
2. [운동, 속도, 미분과 적분](notes/01-motion-calculus.md)
3. [일차 동역학과 회전 시스템](notes/02-first-order-dynamics.md)
4. [적분 공식표](INTEGRAL_TABLE.md)
5. [도함수 공식표](DERIVATIVE_TABLE.md)
6. [핵심 공식 요약](CHEATSHEET.md)
7. [Python 연습 문제](exercises/README.md)
8. [기호와 표기법](SYMBOLS.md) · [단위 전체 목록](UNITS.md)
9. [삼각함수와 기계 예제](TRIGONOMETRY.md)
10. [피드백 제어: PID와 유지 토크](notes/03-feedback-control.md)
11. [로봇 좌표계: 위치와 회전](notes/04-coordinate-frames.md)
12. [회전, 속도와 특이 자세](notes/05-velocity-jacobian.md)
13. [ROS 2: 아키텍처, 노드와 Docker 실습](notes/06-ros2-foundations.md)

[저장소 홈](../../README.md) · [정확성과 안전](SAFETY.md) · [라이선스](LICENSING.md)

## 학습 방법

짧은 절을 읽고 계산을 직접 재현한 다음, 해당하는 오프라인 Python 예제를 실행하고 결과를 자신의 말로 설명하세요. 이상적인 수학 모델과 실제 물리 시스템을 구별하고, 수식을 재사용하기 전에 가정을 확인하세요.

각 장의 선택적 부록에는 더 자세한 유도 과정과 적용 한계가 있습니다. 그림과 수치 그래프도 포함됩니다. $4t$와 63.2 %의 유도 과정은 해당 장의 상세 설명 링크에서 확인하세요.

**Python 설치 및 가상환경(Windows/macOS/Linux):** [연습 문제 안내](exercises/README.md).

한국어의 모든 학습 장 00–05와 주요 수학 참고 자료를 확장 번역했습니다. **영어 원본은 기준 문서이며**, 번역의 언어적 정확성과 모든 세부 항목의 완전한 일치는 별도 검토가 필요합니다.

## GUI 없는 ROS 2 Jazzy: 가상 관절

[GUI 없는 ROS 2 Jazzy: 가상 관절](notes/07-ros2-control-lab.md) — URDF · TF2 · ros2_control · mock hardware · ARM64.

**ROS 2 로봇 아키텍처:** [다섯 단계와 Mermaid 다이어그램](notes/08-ros2-robot-architecture.md).

**Compose 없이:** [공식 ROS 이미지 직접 실행](../../ros2/PLAIN_DOCKER.md).
