# 7. ROS 2 Jazzy без GUI: виртуальный сустав и TF2

**Languages:** [en](../../en/notes/07-ros2-control-lab.md) · [fr](../../fr/notes/07-ros2-control-lab.md) · [de](../../de/notes/07-ros2-control-lab.md) · [it](../../it/notes/07-ros2-control-lab.md) · [es](../../es/notes/07-ros2-control-lab.md) · [pt](../../pt/notes/07-ros2-control-lab.md) · [zh](../../zh/notes/07-ros2-control-lab.md) · [ja](../../ja/notes/07-ros2-control-lab.md) · [nb](../../nb/notes/07-ros2-control-lab.md) · [ru](../../ru/notes/07-ros2-control-lab.md) · [ko](../../ko/notes/07-ros2-control-lab.md) · [fi](../../fi/notes/07-ros2-control-lab.md) · [pl](../../pl/notes/07-ros2-control-lab.md)

[Исполняемый пример и полная диагностика](../../../ros2/control_lab/README.md) · [ROS 2](06-ros2-foundations.md) · [ru](../README.md)

> **Simulation-only / mock hardware.** No real actuators.

Самостоятельная лабораторная работа в Docker на Ubuntu Noble с ROS 2 Jazzy, для поддерживаемых AMD64 и ARM64. Gazebo, RViz, рабочий стол и настоящий двигатель не нужны. Существующий topic/service пример не изменяется.

**Как лаборатория вписывается в систему:** [схема из пяти этапов и двуязычная легенда](08-ros2-robot-architecture.md) связывают mock-контроллер с остальной архитектурой. Камера, планировщик, прошивка сервопривода и настоящий двигатель в лаборатории **не запускаются**.

## 1. URDF, hardware and state

URDF связывает родительский `base_link` через вращательный сустав `joint_1` вокруг +Z со звеном `arm_link`; неподвижный `tool_mount` крепит `tool` со смещением +0.2 m по X. `mock_components/GenericSystem` даёт только командный интерфейс и интерфейс состояния `joint_1/position`. Контроллер пишет задание, `joint_state_broadcaster` публикует состояние, `robot_state_publisher` строит TF2.

[arm.urdf](../../../ros2/control_lab/arm.urdf) · [controllers.yaml](../../../ros2/control_lab/controllers.yaml) · [control.launch.py](../../../ros2/control_lab/control.launch.py) · [Dockerfile](../../../ros2/control_lab/Dockerfile)

[Альтернатива: официальный образ ROS без Compose и собственного Dockerfile](../../../ros2/PLAIN_DOCKER.md)

## 2. Packages and environment

Официальный образ ROS уже определяет `ROS_DISTRO`. Не переопределяй её ни на хосте, ни в контейнере. Подготовленный Dockerfile устанавливает контроллеры и автоматически загружает ROS в интерактивном Bash. Команды ниже проверяют пакеты; ручная установка описана в отдельной Docker-инструкции.

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

**Dockerfile этой лабораторной работы уже устанавливает необходимые пакеты.** Эти команды только проверяют их наличие; устанавливать всё заново внутри собранного контейнера не нужно. Для отдельной чистой среды Jazzy в полном руководстве приведён необязательный вариант ручной установки.

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

В правильном дереве TF2 у каждого child frame только один parent. Преобразование объединяет перенос и поворот; композиция идёт по `base_link → arm_link → tool`, обратный запрос использует инверсию. Неподвижный сустав URDF публикуется в `/tf_static`, вращательные, поступательные и continuous — в `/tf` при наличии joint states. Исходное `TFMessage` хранит преобразования с timestamps, а `tf2_echo` запрашивает временной buffer и вычисляет составное или обратное преобразование. DDS `transient_local` не является постоянным архивом. Если автоматический CLI QoS отличается от явного durability, попробуй также `--qos-reliability reliable`.

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

## 5. ARM64 shared-library diagnostics

На ARM64 `robot_state_publisher` аварийно завершился с `pluginlib::LibraryLoadException`: загрузчик не видел `libsdformat14.so.14`, а `ldd` не разрешал `libgz-math7.so.7`. SDFormat уже лежал в `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/`, а пакет `libsdformat14` отсутствовал в доступных APT. Исследуй core, `/robot_description`, отдельный publisher, `ldd`, vendor-пути и `LD_LIBRARY_PATH`. Выполни source ROS, временно добавляй только реально существующие каталоги. Не делай несовместимых symlink и не публикуй core dump. Позже запуск состоялся, но точная команда исправления неизвестна.

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

**Условное исправление пути загрузки библиотек (не подтверждённое постоянное решение):** выполни [команды временного восстановления](../../../ros2/control_lab/README.md#temporary-recovery-for-a-missing-vendor-library). Сначала проверь `ldd`, загрузи окружение ROS, временно добавь только существующие vendor-каталоги и снова проверь `ldd`; перезапусти процесс **в этой же оболочке**.

## 6. Limits and verification

`GenericSystem` копирует заданную позицию в состояние без двигателя, энкодера, динамики, PID и безопасной остановки. Настоящий сервопривод требует измерения, драйвера, замкнутого контура и защиты от сбоев. Сам `ForwardCommandController` этого не гарантирует. Статические тесты не равны реальному ROS Docker smoke test.

[Исполняемый пример и полная диагностика](../../../ros2/control_lab/README.md) · [Official ros2_control](https://control.ros.org/jazzy/) · [ROS QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
