# 7. ROS 2 Jazzy headless lab: a virtual joint and TF2

**Languages:** [en](../../en/notes/07-ros2-control-lab.md) · [fr](../../fr/notes/07-ros2-control-lab.md) · [de](../../de/notes/07-ros2-control-lab.md) · [it](../../it/notes/07-ros2-control-lab.md) · [es](../../es/notes/07-ros2-control-lab.md) · [pt](../../pt/notes/07-ros2-control-lab.md) · [zh](../../zh/notes/07-ros2-control-lab.md) · [ja](../../ja/notes/07-ros2-control-lab.md) · [nb](../../nb/notes/07-ros2-control-lab.md) · [ru](../../ru/notes/07-ros2-control-lab.md) · [ko](../../ko/notes/07-ros2-control-lab.md) · [fi](../../fi/notes/07-ros2-control-lab.md) · [pl](../../pl/notes/07-ros2-control-lab.md)

[Executable example and full diagnostics](../../../ros2/control_lab/README.md) · [ROS 2](06-ros2-foundations.md) · [en](../README.md)

> **Simulation-only / mock hardware.** No real actuators.

This independent Ubuntu Noble Docker lab uses ROS 2 Jazzy on supported AMD64 or ARM64. No Gazebo, RViz, GUI, physical motor or driver. The original topic/service lab is unchanged.

**Architecture in context:** The [five-stage diagram and bilingual terminology table](08-ros2-robot-architecture.md) show where this mock lab fits in a possible robot system. This lab does **not** run a camera, planner, servo firmware or real equipment.

## 1. URDF, hardware and state

URDF links parent `base_link` to child `arm_link` with revolute `joint_1` around +Z; fixed `tool_mount` attaches `tool` +0.2 m along X. `mock_components/GenericSystem` provides only the `joint_1/position` command and state interfaces. `ForwardCommandController` accepts a command, `joint_state_broadcaster` publishes the mock state, and `robot_state_publisher` derives TF2.

[arm.urdf](../../../ros2/control_lab/arm.urdf) · [controllers.yaml](../../../ros2/control_lab/controllers.yaml) · [control.launch.py](../../../ros2/control_lab/control.launch.py) · [Dockerfile](../../../ros2/control_lab/Dockerfile)

[Alternative: official ROS image without Compose or a custom Dockerfile](../../../ros2/PLAIN_DOCKER.md)

## 2. Packages and environment

The official ROS image already sets `ROS_DISTRO`; do not override it on the host or in the container. The prepared Dockerfile installs the controllers and auto-sources ROS in interactive Bash. Use the commands below to inspect the installed packages; the plain Docker guide covers manual installation.

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

**The control-lab Dockerfile already installs these packages.** These commands only inspect them; do not install the same packages again inside the built container. If preparing a separate bare Jazzy environment, follow the optional installation instructions in the full lab guide.

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

In a valid TF2 tree each child has one parent. Transforms combine translation and rotation; composition follows `base_link → arm_link → tool`, and inverse queries reverse direction. Fixed joints go to `/tf_static`; revolute, prismatic and continuous joints go to `/tf` when joint states are available. A raw `TFMessage` carries timestamped records; `tf2_echo` queries the time-indexed buffer and shows a computed result. DDS `transient_local` offers retained samples while a compatible publisher is alive, not permanent storage. If explicit durability alone behaves differently from automatic CLI QoS, also specify `--qos-reliability reliable`.

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

## 5. ARM64 shared-library diagnostics

On ARM64, `robot_state_publisher` once crashed with `pluginlib::LibraryLoadException` because the dynamic loader could not resolve `libsdformat14.so.14`; `ldd` also listed `libgz-math7.so.7`. SDFormat already existed under `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/`; APT did not offer `libsdformat14`. Diagnose the core, `/robot_description`, isolated publisher, `ldd`, vendor paths and `LD_LIBRARY_PATH`. Source ROS and temporarily add only directories confirmed to exist. Do not upload core dumps or invent incompatible ABI symlinks. Controller startup later succeeded, but the exact repair command is unknown.

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

**Conditional library-path recovery (not a confirmed permanent repair):** Follow the [temporary recovery steps](../../../ros2/control_lab/README.md#temporary-recovery-for-a-missing-vendor-library). First check `ldd`; source ROS and temporarily prepend only vendor directories that exist, then check `ldd` again and retry in the **same shell**.

## 6. Limits and verification

`GenericSystem` copies a command to state: it is not a motor, encoder, PID, real dynamics or safe stopping. Real servos need measured position, driver, closed-loop regulation and fault protection. `ForwardCommandController` alone guarantees none of these. Static source checks and an actual ROS Docker smoke test are distinct.

[Executable example and full diagnostics](../../../ros2/control_lab/README.md) · [Official ros2_control](https://control.ros.org/jazzy/) · [ROS QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
