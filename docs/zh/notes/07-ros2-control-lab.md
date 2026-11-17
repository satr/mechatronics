# 7. ROS 2 Jazzy 无 GUI 实验：虚拟关节与 TF2

**Languages:** [en](../../en/notes/07-ros2-control-lab.md) · [fr](../../fr/notes/07-ros2-control-lab.md) · [de](../../de/notes/07-ros2-control-lab.md) · [it](../../it/notes/07-ros2-control-lab.md) · [es](../../es/notes/07-ros2-control-lab.md) · [pt](../../pt/notes/07-ros2-control-lab.md) · [zh](../../zh/notes/07-ros2-control-lab.md) · [ja](../../ja/notes/07-ros2-control-lab.md) · [nb](../../nb/notes/07-ros2-control-lab.md) · [ru](../../ru/notes/07-ros2-control-lab.md) · [ko](../../ko/notes/07-ros2-control-lab.md) · [fi](../../fi/notes/07-ros2-control-lab.md) · [pl](../../pl/notes/07-ros2-control-lab.md)

[可执行实验与完整诊断](../../../ros2/control_lab/README.md) · [ROS 2](06-ros2-foundations.md) · [zh](../README.md)

> **Simulation-only / mock hardware.** No real actuators.

在 Ubuntu Noble 的 ROS 2 Jazzy Docker 容器中运行，适用于受支持的 AMD64 或 ARM64。无需 Gazebo、RViz、桌面或真实电机；原 topic/service 示例不变。

**整体系统：**[五阶段图与双语术语表](08-ros2-robot-architecture.md)说明本 mock 实验的作用。本实验**不**运行相机、规划器、伺服固件或真实硬件。

## 1. URDF, hardware and state

URDF 定义父坐标系 `base_link`、绕 +Z 旋转的 `joint_1`、子坐标系 `arm_link`，以及通过固定的 `tool_mount` 沿 X 偏移 +0.2 m（米，metre）的 `tool`。`mock_components/GenericSystem` 仅提供 `joint_1/position` 命令与状态接口。控制器写入命令、广播器发布状态，`robot_state_publisher` 计算 TF2。

[arm.urdf](../../../ros2/control_lab/arm.urdf) · [controllers.yaml](../../../ros2/control_lab/controllers.yaml) · [control.launch.py](../../../ros2/control_lab/control.launch.py) · [Dockerfile](../../../ros2/control_lab/Dockerfile)

[替代方案：无需 Compose 或自定义 Dockerfile，直接运行官方 ROS 镜像](../../../ros2/PLAIN_DOCKER.md)

## 2. Packages and environment

官方 ROS 镜像已经定义 `ROS_DISTRO`，不要在宿主机或容器中覆盖。准备好的 Dockerfile 会安装控制器，并在交互式 Bash 中自动加载 ROS。以下命令用于检查软件包；手动安装参见 Docker 指南。

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

**实验 Dockerfile 已经安装这些软件包。** 以下命令只检查安装情况，不要在构建完成的容器中重复安装。独立的 Jazzy 环境可参考完整实验指南中的可选手动安装。

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

有效 TF2 树中每个子坐标系只有一个父坐标系。变换包括平移和旋转；按 `base_link → arm_link → tool` 组合，反向查询则求逆。固定 URDF 关节发布到 `/tf_static`，旋转、移动及连续关节在有状态数据时发布到 `/tf`。原始 `TFMessage` 包含带时间戳的记录；`tf2_echo` 查询时间缓存并计算结果。DDS `transient_local` 并非永久存储。如果 CLI 自动 QoS 与显式 durability 不同，还要试 `--qos-reliability reliable`。

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

## 5. ARM64 shared-library diagnostics

一次 ARM64 故障中，`robot_state_publisher` 因 `pluginlib::LibraryLoadException` 崩溃：加载器看不到 `libsdformat14.so.14`，而 `ldd` 还报告 `libgz-math7.so.7`。其实 SDFormat 已在 `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/`，APT 没有 `libsdformat14` 候选。检查 core、`/robot_description`、独立 publisher、`ldd`、vendor 路径和 `LD_LIBRARY_PATH`。加载 ROS，临时添加确实存在的目录。不要创建 ABI 不兼容的符号链接或上传 core。后续启动成功，但具体修复命令未确认。

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

**条件性库搜索路径修复（并非已确认的永久修复）：** 请参阅[临时恢复步骤](../../../ros2/control_lab/README.md#temporary-recovery-for-a-missing-vendor-library)。先用 `ldd` 检查，再加载 ROS，仅临时加入已存在的 vendor 目录；在**同一 shell** 中重新检查并运行。

## 6. Limits and verification

`GenericSystem` 只是把命令理想化地映射到状态；它不是电机、编码器、PID、动力学或安全停止。真实伺服需要测量、驱动器、闭环及故障保护。`ForwardCommandController` 本身不能保证这些。静态检查与真实 Docker ROS 测试不同。

[可执行实验与完整诊断](../../../ros2/control_lab/README.md) · [Official ros2_control](https://control.ros.org/jazzy/) · [ROS QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
