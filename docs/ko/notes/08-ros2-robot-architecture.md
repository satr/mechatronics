# 8. ROS 2 로봇 아키텍처: 다섯 기능 단계

**언어:** [en](../../en/notes/08-ros2-robot-architecture.md) · [fr](../../fr/notes/08-ros2-robot-architecture.md) · [de](../../de/notes/08-ros2-robot-architecture.md) · [it](../../it/notes/08-ros2-robot-architecture.md) · [es](../../es/notes/08-ros2-robot-architecture.md) · [pt](../../pt/notes/08-ros2-robot-architecture.md) · [zh](../../zh/notes/08-ros2-robot-architecture.md) · [ja](../../ja/notes/08-ros2-robot-architecture.md) · [nb](../../nb/notes/08-ros2-robot-architecture.md) · [ru](../../ru/notes/08-ros2-robot-architecture.md) · [ko](08-ros2-robot-architecture.md) · [fi](../../fi/notes/08-ros2-robot-architecture.md) · [pl](../../pl/notes/08-ros2-robot-architecture.md)

[ROS 2 기초](06-ros2-foundations.md) · [가상 관절 실습](07-ros2-control-lab.md) · [목차](../README.md)

> **개념 설명용입니다.** 실제 장치를 제어하지 않으며 안전을 보장하지 않습니다.

아래 다섯 영어 단계 이름은 [공유 편집 가능한 Mermaid 다이어그램](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram)의 레이블과 정확히 같습니다. 단계는 **기능이며 반드시 하나의 ROS 노드를 뜻하지 않습니다**. 실제 로봇의 실행 가능한 제어나 안전 설계가 아니라 개념도입니다.

## 다섯 기능 단계

| 영어 단계명 | 한국어 번역 | 역할과 ROS 구성 요소 |
| --- | --- | --- |
| **1. Perception** | 인지 | 카메라 드라이버가 촬영 시각이 포함된 `sensor_msgs/msg/Image`를 발행하고 응용 탐지 노드는 `camera_link`에서 객체 자세를 추정합니다. |
| **2. Coordinate Transformation** | 좌표 변환 | 응용 프로그램이 `tf2_ros.Buffer.lookup_transform`을 사용하여 이미지 촬영 시점의 객체 자세를 `base_link`로 변환합니다. 카메라 장착 위치는 URDF 또는 정적 TF로 제공해야 합니다. |
| **3. Motion Planning** | 동작 계획 | MoveIt 2 같은 플래너가 목표, 로봇 모델, 현재 상태를 사용하여 관절 궤적을 만듭니다. |
| **4. Motion Control** | 동작 제어 | 설정된 `joint_trajectory_controller`는 `FollowJointTrajectory`를 받아 하드웨어 명령 인터페이스로 드라이브와 모터에 목표 값을 전달합니다. |
| **5. Feedback** | 피드백 | 엔코더는 로컬 서보 루프와 하드웨어 상태 인터페이스에 측정값을 공급합니다. `joint_state_broadcaster`는 `/joint_states`를, `robot_state_publisher`는 URDF에 따라 `/tf`와 `/tf_static`을 발행합니다. 컨트롤러가 상태를 직접 읽을 수도 있습니다. |

## 인터페이스와 데이터 흐름 구분

**경로를 구분하세요:** URDF는 구조와 선택적 `ros2_control` 인터페이스를 설명할 뿐 모터를 움직이지 않습니다. TF2는 좌표 변환을 조회합니다. 명령은 목표 값이고 상태는 측정 값입니다. `/joint_states`가 끊겼다고 로컬 서보가 반드시 멈춘 것은 아닙니다.

**기존 가상 실습:** `forward_position_controller`와 `mock_components/GenericSystem`을 사용하며 궤적 컨트롤러, MoveIt 2, 실제 센서나 모터는 실행하지 않습니다. 전체 그림은 개념적입니다.

**추가 학습:** watchdog, 오류 처리, QoS, 시간 동기화, 진단, 실시간 처리와 시뮬레이션. 다섯 영어 단계 이름을 유지합니다.

## 공유 원본 및 참고 자료

[공통 Mermaid 아키텍처 다이어그램 열기 및 편집](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) · [ROS 2 참고 자료](06-ros2-foundations.md) · [모의 컨트롤러 실습](07-ros2-control-lab.md)
