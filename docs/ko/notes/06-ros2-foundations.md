# 6. ROS 2: 분산 로봇 소프트웨어와 통신 인터페이스

**Languages:** [en](../../en/notes/06-ros2-foundations.md) · [fr](../../fr/notes/06-ros2-foundations.md) · [de](../../de/notes/06-ros2-foundations.md) · [it](../../it/notes/06-ros2-foundations.md) · [es](../../es/notes/06-ros2-foundations.md) · [pt](../../pt/notes/06-ros2-foundations.md) · [zh](../../zh/notes/06-ros2-foundations.md) · [ja](../../ja/notes/06-ros2-foundations.md) · [nb](../../nb/notes/06-ros2-foundations.md) · [ru](../../ru/notes/06-ros2-foundations.md) · [ko](06-ros2-foundations.md) · [fi](../../fi/notes/06-ros2-foundations.md) · [pl](../../pl/notes/06-ros2-foundations.md)

**이 페이지의 단위(예제 전에 설명):** `m` — 미터; `s` — 초. [단위 전체 목록](../UNITS.md).

[Course index](../README.md) · [Coordinate frames](04-coordinate-frames.md) · [Jacobian](05-velocity-jacobian.md) · [Docker lab](../../../ros2/README.md)

> **Safety:** 합성 데이터로 이루어진 소프트웨어 학습 예제입니다. 실제 로봇이나 장비를 제어하지 마세요. ROS 메시징은 운동학, 실시간 제어 및 하드웨어 안전 기능을 대신하지 않습니다.

ROS 2(Robot Operating System 2)는 로봇의 분산 소프트웨어 구성요소를 연결하는 프레임워크입니다. 백엔드 개발자에게 노드(node)는 논리적 계산 구성요소, 토픽(topic)은 형식이 정해진 비동기 이벤트 스트림, 서비스(service)는 요청/응답 RPC에 비유할 수 있습니다. 하지만 중앙 브로커가 필수인 구조는 아니며 일반적으로 DDS 기반 분산 탐색을 사용합니다.

![ROS 2 publisher and subscriber linked through a typed topic; a CLI process calls a service](../../../assets/figures/ros2-topic-service.svg)

![ROS 2 소프트웨어 계층과 별도의 저수준 하드웨어 안전 경계](../../../assets/figures/ros2-software-layers.svg)

*메시징 미들웨어는 장치 제어나 독립적인 안전 기능을 대체하지 않습니다.*

## 학습 순서

1. [아키텍처, middleware와 ROS graph](#section-1)
2. [Nodes, topics와 형식화된 messages](#section-2)
3. [Services, actions와 parameters](#section-3)
4. [Packages, workspaces, colcon과 ament](#section-4)
5. [ROS 2 CLI로 그래프 관찰하기](#section-5)
6. [Launch files](#section-6)
7. [tf2와 좌표계(coordinate frames)](#section-7)
8. [URDF와 robot_state_publisher](#section-8)
9. [ros2_control과 하드웨어 경계](#section-9)
10. [QoS, DDS discovery와 Docker](#section-10)
11. [실습: 두 노드, topic, service와 launch](#section-11)
12. [용어와 제한사항](#section-12)

<a id="section-1"></a>

## 1. 아키텍처, middleware와 ROS graph

**문제:** 카메라, 위치 추정, 계획 시스템이 하나의 거대한 프로세스가 되지 않고 협력해야 합니다. ROS 1은 이름 탐색에 중앙 master를 사용했지만 ROS 2는 RMW(ROS Middleware) 추상화와 일반적으로 DDS/RTPS를 통해 중앙 ROS 1 master 없이 참여자를 찾습니다. ROS graph는 탐색된 노드, 토픽, 서비스, 액션으로 구성됩니다. 노드는 논리 단위이므로 여러 노드가 한 프로세스에 존재할 수 있고 프로세스는 여러 컴퓨터에 분산될 수 있습니다. 탐색은 인증 기능이 아닙니다.

<a id="section-2"></a>

## 2. Nodes, topics와 형식화된 messages

**문제:** 지속적인 측정값을 여러 소비자에게 보내야 합니다. Publisher는 타입이 정의된 메시지를 topic으로 발행하고 subscriber는 비동기로 받습니다. std_msgs/msg/String에는 string data 필드가 있으며 Python과 C++가 공통 인터페이스를 사용합니다. /sample_source는 /training/status에 sample N을 보내고 /sample_monitor는 수신 횟수를 기록합니다. depth 10은 영구 기록이 아니며 새 구독자는 보통 이후 메시지만 받습니다.

**탐색 과정 예시:** `/sample_monitor`가 발견되기 전에 `/sample_source`가 `sample 1`을 이미 발행했다고 가정합니다. 이 실습은 기록 정책이 `volatile`이므로 지난 메시지를 새 구독자에게 자동 재전송하지 않습니다. 따라서 publisher가 계속 동작해도 monitor는 처음에 `received 0 samples`를 반환할 수 있습니다. 호환되는 endpoints가 서로 발견된 후에야 수신 수가 증가할 수 있습니다. 발행한 시퀀스 번호와 받은 메시지 수는 서로 다른 수치이며 둘 다 트랜잭션 확인이 아닙니다.

**CLI 결과가 뜻하는 범위:** `ros2 topic list -t`는 발견된 topic의 이름과 메시지 타입을 보여 주지만 **subscriber가 데이터를 받았다는 증거는 아닙니다**. `ros2 topic info /training/status -v`는 발견된 endpoints와 제공/요청 QoS를 보여 줍니다. 구독자가 0개라는 결과는 구독자가 없는 경우 **또는** discovery가 끝나지 않은 경우일 수 있습니다. Endpoints가 보이는데 수신이 안 되면 타입, QoS, 프로세스 로그, `ROS_DOMAIN_ID`를 확인합니다. 이 명령들은 현재 상태의 스냅샷이지 전달 보증이 아닙니다. 실습 컨테이너 안에서 실행하세요.

<a id="section-3"></a>

## 3. Services, actions와 parameters

**문제:** 스트림, 짧은 질의, 긴 작업을 구분합니다. Service는 request/response로 동작합니다. /training/count는 std_srvs/srv/Trigger를 사용하여 success와 message를 반환합니다. Action은 goal, feedback, result, cancel을 제공하므로 내비게이션 목표 등에 적합합니다. Parameter는 노드 소유의 설정값입니다. interval_s=1.0은 타이머를 만들 때 읽으며 이후 변경해도 타이머가 자동 재생성되지 않습니다. 재시도와 멱등성은 애플리케이션에서 결정해야 합니다.

응답, 실행 시간, 실패 시 처리가 어떻게 다른지에 따라 통신 방식을 선택해야 합니다. 서로 바꿔 쓸 수 없습니다.

| 방식 | 흐름 | 적절한 용도 | 혼동하면 안 되는 것 |
| --- | --- | --- | --- |
| Topic | 발행자 → 0..N 구독자 | 지속적인 상태·텔레메트리 | 영구 로그나 확인된 트랜잭션 |
| Service | 요청 → 응답 | 짧은 조회나 제한된 동작 | 커밋 보장 또는 장시간 작업 |
| Action | 목표 → 피드백/결과, 선택적 취소 | 긴 탐색이나 계산 | 주기적인 센서 데이터 스트림 |
| Parameter | 노드가 소유하는 값 | `interval_s` 같은 설정 | 공유 글로벌 설정 데이터베이스 |

이 실습에서 `/training/status`는 topic, `/training/count`는 service, `interval_s`는 노드 파라미터입니다. 애플리케이션 action은 구현되지 않았습니다. Service 타임아웃이 서버에서 요청을 처리하지 않았다는 뜻은 아니며 재시도 가능 여부는 작업의 의미에 달려 있습니다.

<a id="section-4"></a>

## 4. Packages, workspaces, colcon과 ament

**문제:** 의존성과 실행 파일을 재현 가능하게 빌드합니다. package.xml은 패키지 메타데이터를 기록하고 ament_python/ament_cmake가 빌드 시스템과 연결합니다. Workspace에는 일반적으로 src, build, install, log가 있습니다. colcon은 빌드 도구이며 메시지 전송 계층이 아닙니다. ROS underlay를 먼저 source하고 작업공간 overlay를 다음에 source합니다. telemetry_demo는 setup.py에 두 실행 엔트리와 launch 파일을 등록합니다.

실제 `ros2/Dockerfile`에서 **이미지 빌드**(`RUN`)와 **컨테이너 시작**(`CMD`)은 별개의 단계입니다. 빌드 중에는 ROS underlay만 로드한 다음 `colcon`으로 패키지를 빌드합니다.

**이미지 빌드(`RUN`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
colcon build --packages-select telemetry_demo
```

**컨테이너 시작(`CMD`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
source /opt/training_ws/install/setup.bash
exec ros2 launch telemetry_demo demo.launch.py
```

컨테이너 시작 시 새 셸이 ROS underlay를 **다시** 로드하고, 빌드한 workspace overlay를 로드한 뒤 launch 파일을 실행합니다. `package.xml`은 의존성을 선언하고 `setup.py`는 Python 실행 진입점과 launch 파일을 설치합니다. `build/`와 `install/`은 생성 산출물이며 소스 코드를 직접 수정하는 곳이 아닙니다. 빌드 성공만으로 그래프가 준비되었다고 할 수는 없습니다.

<a id="section-5"></a>

## 5. ROS 2 CLI로 그래프 관찰하기

**문제:** 설정 파일 대신 실제 동작 상태를 확인합니다. ros2 node list/info는 노드, topic list/info/echo는 스트림, interface show는 타입을 보여 주며 service list/call, action list, param get이 다른 엔드포인트를 조사합니다. /sample_source, /sample_monitor, /training/status, /training/count를 확인할 수 있습니다. 애플리케이션 action은 구현되어 있지 않습니다. 데이터가 없으면 이름, 타입, QoS와 ROS_DOMAIN_ID부터 확인합니다.

컨테이너 내부에서 ROS 환경을 source한 뒤 다음 CLI를 실행합니다:

```bash
ros2 node list
ros2 node info /sample_source
ros2 topic list -t
ros2 topic info /training/status -v
ros2 topic echo /training/status
ros2 interface show std_msgs/msg/String
ros2 service list -t
ros2 service call /training/count std_srvs/srv/Trigger "{}"
ros2 action list
ros2 param get /sample_source interval_s
```

<a id="section-6"></a>

## 6. Launch files

**문제:** 여러 프로세스를 동일한 설정으로 시작합니다. demo.launch.py는 두 launch_ros.actions.Node가 들어 있는 LaunchDescription을 반환하며 interval_s=1.0을 전달합니다. Launch는 인수, namespace, remapping, 다른 launch 파일 포함을 지원합니다. 프로세스 시작이 서비스 준비 완료를 뜻하지 않으므로 탐색, 상태 확인과 재시도 정책이 필요합니다.

**준비 상태를 실제로 관찰해야 합니다:** `launch_ros.actions.Node`가 두 **프로세스**를 시작해도 DDS 탐색과 첫 `/training/status` 메시지는 그 후에 발생합니다. 즉시 `/training/count`를 호출하면 `received 0 samples`가 정상적으로 반환될 수 있으며, 나중에 카운트가 늘어납니다. 이는 트랜잭션 손실이 아니라 monitor가 받은 메시지만 보고하기 때문입니다. `interval_s=1.0`은 타이머 생성 시에 읽으며 실행 중 주기를 자동으로 바꾸지 않습니다.

<a id="section-7"></a>

## 7. tf2와 좌표계(coordinate frames)

**문제:** camera_link 기준 관측값을 base_link 또는 map으로 변환합니다. tf2는 회전과 병진을 포함한 시간 기준 변환을 저장하고 조회합니다. 고정된 장착 관계에는 정적 변환, 움직이는 관절에는 동적 변환이 필요합니다. 부모-자식 프레임과 타임스탬프를 일치시켜야 합니다. tf2 자체는 정/역기구학 계산이나 경로 계획을 수행하지 않습니다. 수학적 배경은 기존 좌표계 및 Jacobian 장을 참고하세요.

[Coordinate frames](04-coordinate-frames.md) · [Velocity and Jacobian](05-velocity-jacobian.md)

**프레임 연결 예시(필수 구조는 아님):** `map → odom → base_link → camera_link`. 본체에 고정된 카메라에는 `static` 변환을 사용하고, 이동하는 본체에는 `dynamic` 변환이 필요합니다. 시각 *t*에 `camera_link`에서 관측한 점을 `map`으로 옮기려면 tf2가 **그 관측 시각의** 전체 변환 체인을 조회해야 합니다. 프레임이 없거나 체인이 끊겼거나 해당 시각의 데이터가 없으면 lookup/extrapolation 오류가 발생합니다. 과거 측정에 최신 변환을 무조건 적용하면 잘못된 좌표가 나올 수 있습니다.

**변환 방향과 역변환 계산 예시.** `base_link`(B)를 부모 좌표계, `tool`(T)을 자식 좌표계라고 합시다. 상대 회전이 없고 부모의 +X 방향으로 0.1 m 이동해 있으면 도구 원점은 **B 좌표로 표현했을 때 기준 원점보다 +X 쪽**에 있습니다. 반대로 T 좌표로 기준 원점을 표현하면 부호가 반대입니다.

$$
{}^{B}\mathbf p_{T}=(0.1, 0, 0)\ \mathrm{m},\qquad
{}^{T}\mathbf p_{B}=(-0.1, 0, 0)\ \mathrm{m}\quad (R=I).
$$

부호만 뒤집어도 되는 경우는 **두 좌표계의 방향이 같을 때뿐**입니다. 일반적인 점 변환에는 회전과 이동이 함께 있고, 역변환은 **둘 다** 되돌려야 합니다. 올바른 회전 행렬의 역행렬은 $R^T$입니다.

$$
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT},\qquad
\mathbf p_T=R_{BT}^{T}(\mathbf p_B-\mathbf t_{BT}),\qquad
\mathbf t_{TB}=-R_{BT}^{T}\mathbf t_{BT}.
$$

다른 자세에서 T를 공통 Z축 주위로 +90° 회전시키고 B 기준 이동 (0.1 m, 0 m)은 유지합시다. 이제 T 좌표에서 본 B 원점은 (0 m, +0.1 m)이며 **(−0.1 m, 0 m)이 아닙니다**. 같은 행렬로 T의 점 (0 m, 0.05 m)을 B로 변환합니다.

$$
R_{BT}=\begin{bmatrix}0 & -1\\1 & 0\end{bmatrix},\quad
\mathbf t_{BT}=\begin{bmatrix}0.1\\0\end{bmatrix}\ \mathrm{m},\quad
\mathbf t_{TB}=\begin{bmatrix}0\\0.1\end{bmatrix}\ \mathrm{m}.
$$

$$
\mathbf p_T=\begin{bmatrix}0\\0.05\end{bmatrix}\ \mathrm{m}
\Longrightarrow
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT}
=\begin{bmatrix}0.05\\0\end{bmatrix}\ \mathrm{m}.
$$

좌표계와 변환은 **좌표 관계에 대한 설명**이지 실제 구동 명령이 아닙니다. ROS 2의 이동량은 통상 미터 단위를 사용합니다. [좌표계 강의](04-coordinate-frames.md#section-3)는 밀리미터를 쓰므로 예제를 합칠 때 단위를 변환해야 합니다. 정적 변환은 고정 장착 관계를, 동적 변환은 상태를 갱신하는 구성 요소의 출력을 나타냅니다. 과거 측정값은 측정 시각의 변환을 사용하며 데이터가 없는 경우도 처리해야 합니다.

<a id="section-8"></a>

## 8. URDF와 robot_state_publisher

**문제:** 로봇의 기계 구조를 하나의 모델로 공유합니다. URDF는 link, joint, 원점, 축과 선택적인 visual/collision/inertial 속성을 기술합니다. robot_state_publisher는 URDF와 관절 위치(보통 /joint_states의 sensor_msgs/msg/JointState)를 결합해 변환을 발행합니다. URDF 자체가 엔코더 값을 측정하거나 시뮬레이션 및 역기구학을 제공하지는 않습니다. m, rad, 축 방향과 시간을 일관되게 사용합니다.

**변환의 출처:** URDF는 `fixed` 관절과 움직이는 관절의 구조를 정의합니다. `robot_state_publisher`는 고정 관절의 구조에서 `static` 변환을 만들고 `/joint_states`(`sensor_msgs/msg/JointState`)로 받은 관절 위치로 움직이는 관절의 `dynamic` 변환을 발행합니다. URDF 자체는 **관절 위치를 측정하지 않으며**, 빠진 센서 값도 채우지 않습니다. 길이는 미터, 각도는 라디안, 타임스탬프는 일관되게 사용합니다.

<a id="section-9"></a>

## 9. ros2_control과 하드웨어 경계

**문제:** 제어 알고리즘과 장치 드라이버를 분리합니다. ros2_control은 controller manager, 상태 인터페이스(position/velocity), 명령 인터페이스(position/velocity/effort), 하드웨어 추상화를 제공합니다. 계획기→제어기→하드웨어 인터페이스→장치로 이어지고 측정 상태가 피드백됩니다. ROS 메시지를 보낸다고 실시간 주기, 전류 제한, 안전 정지가 보장되지는 않습니다. 이 예제에는 실제 액추에이터가 없습니다.

[First-order dynamics](02-first-order-dynamics.md) · [Feedback PID](03-feedback-control.md)

**controller manager의 역할:** `controller_manager`는 컨트롤러의 수명 주기를 관리하고 리소스 매니저를 통해 상태 인터페이스(state interfaces)와 명령 인터페이스(command interfaces)의 접근을 조정합니다. 컨트롤러는 가상의 예인 `joint1/position` 같은 측정 상태를 읽을 수 있고, 활성화된 컨트롤러는 호환되는 명령 인터페이스를 점유하여 목표값을 기록할 수 있습니다. 측정값은 목표값과 같지 않으며, 이미 점유된 명령 인터페이스를 여러 컨트롤러가 임의로 동시에 점유할 수 없습니다. 이는 단순한 topic 탐색과 다른 문제입니다.

**이 실습의 범위:** `/training/status`와 `/training/count`는 topic과 service만 보여 주며 **`ros2_control` 예제가 아닙니다**. 두 node 모두 컨트롤러가 아니며 `controller_manager`, 하드웨어 인터페이스, 폐루프 제어를 실행하지 않습니다. smoke test가 통과해도 컨트롤러 수명 주기, 실시간 제어 성능 또는 장치 안전성이 검증되는 것은 아닙니다. [ros2_control 공식 소개](https://control.ros.org/jazzy/doc/getting_started/getting_started.html)를 참고하세요.

**다음 실습: GUI 없는 ros2_control, TF2, 가상 관절:** [다음 실습: GUI 없는 ros2_control, TF2, 가상 관절](07-ros2-control-lab.md). 새 실습은 URDF, GenericSystem, 명령, 상태, /joint_states, TF2, QoS, ARM64 로더 진단을 다루며 실제 장비는 제어하지 않습니다.

**다음 단계: 전체 로봇 아키텍처.** [다섯 단계 Mermaid 그림](08-ros2-robot-architecture.md)은 인지, 시간 기준 TF2, 계획, 제어 및 피드백을 연결합니다. 실제 하드웨어 경로는 개념적입니다.

<a id="section-10"></a>

## 10. QoS, DDS discovery와 Docker

**문제:** 메시지 누락과 노드 탐색 실패를 구분합니다. QoS에는 reliable/best_effort, volatile/transient_local, history, depth가 있습니다. Subscriber가 publisher보다 강한 보장을 요구하면 이름과 타입이 맞아도 메시지를 받지 못할 수 있습니다. DDS는 UDP 멀티캐스트와 동적 포트를 자주 사용하므로 Docker Desktop, VPN, 방화벽이 탐색을 방해할 수 있습니다. ROS_DOMAIN_ID를 일치시켜야 합니다. 데모는 호스트 포트나 특권 없이 한 컨테이너 내부에서만 동작합니다.

**QoS 불일치 예시:** publisher가 `best_effort`를 제공하지만 subscriber가 `reliable`을 요구하면 topic 이름과 메시지 타입이 일치하고 엔드포인트가 탐색되어도 **메시지를 받지 못할 수 있습니다**. 반대로 다른 QoS 조건이 호환된다면 `best_effort` subscriber는 `reliable` publisher에서 메시지를 받을 수 있습니다. `volatile`은 과거 메시지를 재전송하지 않습니다. `transient_local`은 연결 가능한 호환 publisher가 보관한 제한된 기록을 전달할 수 있지만 **영구적인 분산 로그가 아닙니다**.

**진단 순서:** 동일한 컨테이너에서 `ROS_DOMAIN_ID=42`를 확인한 뒤 `ros2 node list`, `ros2 topic info /training/status -v`(엔드포인트와 QoS 확인), `docker compose logs demo`(프로세스 로그)를 점검합니다. 그래프가 여전히 보이지 않으면 RMW/DDS, 네트워크 인터페이스와 방화벽을 확인하세요. TCP 포트 노출만으로 모든 DDS 문제가 해결되지는 않습니다. 이 실습은 여러 호스트 간 통신을 검증하지 않습니다.

[ROS 2 Jazzy 공식 QoS 문서](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)

[대안: Compose나 사용자 Dockerfile이 없는 공식 ROS 이미지](../../../ros2/PLAIN_DOCKER.md)

<a id="section-11"></a>

## 11. 실습: 두 노드, topic, service와 launch

docker compose up --build -d로 시작하면 로그에 sample 발행과 수신, 증가하는 카운터가 나타나야 합니다. Service는 success=True와 received 12 samples 같은 메시지를 반환하며 수치는 실행 시간에 따라 달라집니다. [별도의 GitHub Actions Docker 스모크 테스트](../../../.github/workflows/ros2-live-smoke.yml)는 **단일 컨테이너 안에서 앱을 실제 실행**하여 두 ROS 노드, `/training/status`의 타입 메시지 수신, `/training/count` 서비스 응답을 확인했습니다. 일반 검증 CI는 ROS를 실행하지 않습니다. 다중 컴퓨터 간 DDS, 결정적 실시간 성능, 실제 하드웨어 및 학습자의 로컬 Docker 환경은 검증하지 않았습니다.

[Source, expected results and troubleshooting](../../../ros2/README.md). From the repository root:

학습 순서는 이미지에 설치한 `demo_nodes_cpp` talker와 `demo_nodes_py` listener, 저장소에서 빌드한 `telemetry_demo`, 마지막으로 `ros2_control`입니다. Dockerfile은 APT로 공식 데모를 설치하고 `colcon`으로 `telemetry_demo`를 빌드합니다. 대화형 작업은 **하나의 Bash 셸**에서 환경을 **새 셸마다 한 번만** 불러옵니다. 별도의 `docker compose exec`는 컨테이너 `CMD`의 셸 환경을 상속하지 않습니다.

호스트에서 컨테이너를 시작하고 대화형 셸을 엽니다:

```bash
cd ros2
docker compose up --build -d
docker compose logs --tail=20 demo
docker compose exec demo bash
```

컨테이너 내부에서(호스트가 아님) 환경을 한 번 불러오고 ROS 그래프를 확인합니다:

```bash
echo "$ROS_DISTRO"
ros2 node list
ros2 service call /training/count std_srvs/srv/Trigger "{}"
exit
```

`exit` 후 호스트에서 정리합니다:

```bash
docker compose down
```

**CI 신뢰 경계:** 실제 ROS 2 Docker 스모크 테스트는 관련 변경 사항이 `main`에 반영된 뒤 자동으로 실행되거나 `main`에서 `workflow_dispatch`로 수동 실행됩니다. `pull_request`의 수정 내용에서는 실행하지 않습니다. 그렇지 않으면 PR이 수정한 Bash 스크립트와 Dockerfile을 GitHub 호스트 runner에서 직접 실행할 수 있기 때문입니다. 병합 전 격리된 Python 검사는 ROS 실제 실행 시험을 대체하지 않습니다. 병합 전에 독립적인 코드 검토를 하고, 병합 후 실제 ROS 테스트 결과를 확인해야 합니다.

<a id="section-12"></a>

## 12. 용어와 제한사항

- **Node / process(노드 / 프로세스):** Node는 이름을 가진 논리적인 ROS 구성 요소이며 하나의 운영체제 프로세스에 여러 노드가 있을 수 있습니다.
- **ROS graph:** 현재 발견된 통신 엔드포인트의 집합이며 영구 중앙 등록부나 권한 검사 기능이 아닙니다.
- **Topic(토픽):** 여러 Publisher와 Subscriber가 참여할 수 있는 이름 있는 비동기 데이터 스트림입니다.
- **Message(메시지):** ROS interface가 정의한 타입의 데이터 구조이며 임의의 Python/C++ 객체는 아닙니다.
- **Publisher / subscriber:** 토픽 메시지의 송신자와 수신자입니다. 전달에는 discovery와 호환되는 QoS가 필요합니다.
- **Service(서비스):** 짧은 작업을 위한 타입이 정의된 요청/응답입니다. timeout만으로 서버가 아무 일도 하지 않았다고 단정할 수 없습니다.
- **Action(액션):** 목표, feedback, 결과 및 취소 요청을 다룹니다. 취소 요청이 즉시 정지를 보장하지는 않습니다.
- **Parameter(매개변수):** 개별 노드가 소유한 설정값이며 변경한다고 실행 중인 타이머가 자동으로 갱신되지는 않습니다.
- **RMW / DDS:** RMW는 미들웨어 구현을 추상화하며 DDS는 주로 탐색과 데이터 전송에 사용됩니다. 그 자체가 인증 기능은 아닙니다.
- **colcon / ament:** 워크스페이스 빌드 조정 도구 / ROS 패키지 빌드 통합이며 통신 미들웨어가 아닙니다.
- **Launch:** 시작할 프로세스와 설정을 기술하지만 프로세스가 시작되었다고 통신 준비가 끝난 것은 아닙니다.
- **tf2:** 타임스탬프가 있는 좌표계 변환을 제공하며 역기구학을 계산하는 솔버가 아닙니다.
- **URDF / robot_state_publisher:** 로봇 구조 모델 / 모델과 현재 관절 상태로 변환을 발행하는 구성 요소입니다.
- **ros2_control:** 컨트롤러 수명 주기와 리소스로 관리되는 state/command 인터페이스를 다룹니다. 이 topic/service 실습에는 없습니다.
- **QoS:** 요청/제공 측의 전달 및 기록 정책 호환성이며 영구 이벤트 로그나 안전 인증이 아닙니다.

**버전 확인(2026년 11월 13일):** ROS 2 Jazzy LTS는 2029년 5월까지, Lyrical LTS는 2031년 5월까지 지원됩니다. Docker 태그는 변경 불가능한 이미지 digest 또는 apt 패키지 버전을 고정하지 않습니다.

**Primary sources:** [ROS 2 releases](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst) · [Jazzy documentation](https://docs.ros.org/en/jazzy/) · [tf2](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html) · [URDF](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html) · [ros2_control](https://control.ros.org/jazzy/)
