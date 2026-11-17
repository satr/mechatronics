# 7. GUI 없는 ROS 2 Jazzy: 가상 관절과 TF2

**Languages:** [en](../../en/notes/07-ros2-control-lab.md) · [fr](../../fr/notes/07-ros2-control-lab.md) · [de](../../de/notes/07-ros2-control-lab.md) · [it](../../it/notes/07-ros2-control-lab.md) · [es](../../es/notes/07-ros2-control-lab.md) · [pt](../../pt/notes/07-ros2-control-lab.md) · [zh](../../zh/notes/07-ros2-control-lab.md) · [ja](../../ja/notes/07-ros2-control-lab.md) · [nb](../../nb/notes/07-ros2-control-lab.md) · [ru](../../ru/notes/07-ros2-control-lab.md) · [ko](../../ko/notes/07-ros2-control-lab.md) · [fi](../../fi/notes/07-ros2-control-lab.md) · [pl](../../pl/notes/07-ros2-control-lab.md)

[실행 예제와 전체 진단](../../../ros2/control_lab/README.md) · [ROS 2](06-ros2-foundations.md) · [ko](../README.md)

> **Simulation-only / mock hardware.** No real actuators.

지원되는 AMD64 또는 ARM64의 Ubuntu Noble ROS 2 Jazzy Docker 컨테이너에서 실행합니다. Gazebo, RViz, 데스크톱, 실제 모터가 필요 없습니다. 기존 topic/service 예제는 변경하지 않습니다.

**전체 시스템:** [다섯 단계 그림과 이중 언어 용어표](08-ros2-robot-architecture.md)는 이 mock 실습의 위치를 보여 줍니다. 카메라, 플래너, 서보 펌웨어, 실제 하드웨어는 **실행하지 않습니다**.

## 1. URDF, hardware and state

URDF는 부모 `base_link`, +Z 축 회전 관절 `joint_1`으로 연결된 `arm_link`, X 방향 +0.2 m의 고정 `tool_mount`와 `tool`을 정의합니다. `mock_components/GenericSystem`은 `joint_1/position` 명령·상태 인터페이스만 제공합니다. 컨트롤러가 명령을 쓰고 `joint_state_broadcaster`가 상태를 게시하며 `robot_state_publisher`가 TF2를 계산합니다.

[arm.urdf](../../../ros2/control_lab/arm.urdf) · [controllers.yaml](../../../ros2/control_lab/controllers.yaml) · [control.launch.py](../../../ros2/control_lab/control.launch.py) · [Dockerfile](../../../ros2/control_lab/Dockerfile)

[대안: Compose나 사용자 Dockerfile 없이 공식 ROS 이미지 실행](../../../ros2/PLAIN_DOCKER.md)

## 2. Packages and environment

공식 ROS 이미지가 `ROS_DISTRO`를 이미 설정하므로 호스트나 컨테이너에서 덮어쓰지 마세요. Dockerfile은 컨트롤러를 설치하고 대화형 Bash에서 ROS를 자동으로 설정합니다. 아래는 설치 확인 명령입니다. 수동 설치는 Docker 가이드를 참고하세요.

```bash
echo "$ROS_DISTRO"
dpkg-query -W ros-${ROS_DISTRO}-ros2-control ros-${ROS_DISTRO}-ros2-controllers
ros2 pkg prefix controller_manager
ros2 pkg prefix joint_state_broadcaster
ros2 pkg prefix joint_trajectory_controller
ros2 pkg prefix forward_command_controller
ros2 pkg executables controller_manager
# Expected executables: ros2_control_node, spawner, unspawner, hardware_spawner
```

**실습 Dockerfile이 이미 필요한 패키지를 설치합니다.** 아래 명령은 설치 여부만 확인하며 빌드한 컨테이너 안에서 재설치하지 않습니다. 별도 Jazzy 환경의 수동 설치는 전체 실습 가이드를 참조하세요.

## 3. Docker and CLI verification

```bash
# On host, from repository root:
docker build -t training-ros-control -f ros2/control_lab/Dockerfile ros2/control_lab
docker run -d --name training-ros-control -e ROS_DOMAIN_ID=43 training-ros-control
docker exec -it training-ros-control bash
# In container: interactive Bash loads ROS via ~/.bashrc.
ros2 control list_controllers
ros2 control list_hardware_interfaces
ros2 topic pub --once /forward_position_controller/commands std_msgs/msg/Float64MultiArray '{data: [1.0]}'
ros2 topic echo /joint_states --once
ros2 run tf2_ros tf2_echo base_link tool
```

**Expected synthetic result:** `joint_1/position [available] [claimed]`; `/joint_states` position = 1.0 rad; unconfigured velocity/effort = `NaN` possible. Tool: X ≈ 0.108 m, Y ≈ 0.168 m, Z = 0 m, yaw ≈ 57.296°, from X = 0.2 cos(1.0), Y = 0.2 sin(1.0). Rad is the SI unit of angle; m is metre.

## 4. Frames, time and DDS QoS

유효한 TF2 트리에서 각 자식 프레임의 부모는 하나입니다. 변환은 평행이동과 회전을 결합하고 `base_link → arm_link → tool`로 합성하며 반대 방향에는 역변환을 사용합니다. URDF 고정 관절은 `/tf_static`, 회전·직동·연속 관절은 상태가 있을 때 `/tf`에 게시합니다. 원시 `TFMessage`는 시간 정보가 있는 기록이며 `tf2_echo`는 시간 버퍼를 조회해 결과를 계산합니다. DDS `transient_local`은 영구 보관이 아닙니다. CLI 자동 QoS와 명시적 durability가 다를 때 `--qos-reliability reliable`도 시험합니다.

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

## 5. ARM64 shared-library diagnostics

ARM64에서 `robot_state_publisher`가 `pluginlib::LibraryLoadException`으로 종료되었습니다. 로더는 `libsdformat14.so.14`를 찾지 못했고 `ldd`는 `libgz-math7.so.7`도 해결하지 못했습니다. 그러나 SDFormat은 이미 `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/`에 있었고 APT에 `libsdformat14`가 없었습니다. core, `/robot_description`, 단독 publisher, `ldd`, vendor 경로, `LD_LIBRARY_PATH`를 확인합니다. ROS를 source하고 실제 존재하는 경로만 임시 추가합니다. ABI가 다른 symlink나 core 공개는 금지입니다. 이후 기동은 확인했지만 수정 명령은 불명확합니다.

```bash
# Only if core file exists:
file core
du -h core
ros2 node list
ros2 topic info /robot_description -v
ulimit -c 0
source /opt/ros/${ROS_DISTRO}/setup.bash
# Stop a healthy isolated publisher with Ctrl+C before proceeding.
ros2 run robot_state_publisher robot_state_publisher /opt/control_lab/arm.urdf
ldd /opt/ros/${ROS_DISTRO}/lib/libsdformat_urdf_plugin.so
find /opt/ros/${ROS_DISTRO}/opt -name 'libsdformat14.so*' -o -name 'libgz-math7.so*'
printf '%s\n' "$LD_LIBRARY_PATH"
for vendor in sdformat_vendor gz_math_vendor gz_utils_vendor; do
  dir="/opt/ros/${ROS_DISTRO}/opt/$vendor/lib"
  if [ -d "$dir" ]; then
    export LD_LIBRARY_PATH="$dir${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
  fi
done
ldd /opt/ros/${ROS_DISTRO}/lib/libsdformat_urdf_plugin.so
```

**조건부 라이브러리 경로 복구(확인된 영구 수정이 아님):** [임시 복구 단계](../../../ros2/control_lab/README.md#temporary-recovery-for-a-missing-vendor-library)를 따릅니다. `ldd`를 확인하고 ROS를 source한 뒤 존재하는 vendor 디렉터리만 추가하여 **같은 셸**에서 다시 검사합니다.

## 6. Limits and verification

`GenericSystem`은 명령을 상태로 복사할 뿐 모터, 엔코더, PID, 동역학, 안전 정지가 아닙니다. 실제 서보에는 측정, 드라이버, 피드백 제어와 보호가 필요합니다. `ForwardCommandController`는 이를 보장하지 않습니다. 정적 테스트는 실제 Docker ROS 실행과 다릅니다.

[실행 예제와 전체 진단](../../../ros2/control_lab/README.md) · [Official ros2_control](https://control.ros.org/jazzy/) · [ROS QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
