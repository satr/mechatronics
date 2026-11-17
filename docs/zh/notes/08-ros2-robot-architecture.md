# 8. ROS 2 机器人架构：五个功能阶段

**语言:** [en](../../en/notes/08-ros2-robot-architecture.md) · [fr](../../fr/notes/08-ros2-robot-architecture.md) · [de](../../de/notes/08-ros2-robot-architecture.md) · [it](../../it/notes/08-ros2-robot-architecture.md) · [es](../../es/notes/08-ros2-robot-architecture.md) · [pt](../../pt/notes/08-ros2-robot-architecture.md) · [zh](08-ros2-robot-architecture.md) · [ja](../../ja/notes/08-ros2-robot-architecture.md) · [nb](../../nb/notes/08-ros2-robot-architecture.md) · [ru](../../ru/notes/08-ros2-robot-architecture.md) · [ko](../../ko/notes/08-ros2-robot-architecture.md) · [fi](../../fi/notes/08-ros2-robot-architecture.md) · [pl](../../pl/notes/08-ros2-robot-architecture.md)

[ROS 2 基础](06-ros2-foundations.md) · [虚拟关节实验](07-ros2-control-lab.md) · [目录](../README.md)

> **仅用于概念学习。** 不控制真实设备，也不提供安全保证。

下面五个英文阶段名与[共享、可编辑的 Mermaid 架构图](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram)完全一致。每个阶段是**功能，不一定对应单个 ROS 节点或进程**。这只是概念示意，不是可用于实机的控制或安全系统。

## 五个功能阶段

| 英文阶段名 | 中文译名 | 职责与 ROS 组件 |
| --- | --- | --- |
| **1. Perception** | 感知 | 相机驱动发布带采集时间戳的 `sensor_msgs/msg/Image`；应用检测节点在 `camera_link` 中估计物体位姿。 |
| **2. Coordinate Transformation** | 坐标变换 | 应用通过 `tf2_ros.Buffer.lookup_transform`，按图像采集时间将物体位姿转换到 `base_link`。相机的固定安装变换必须由 URDF 或静态 TF 发布者提供。 |
| **3. Motion Planning** | 运动规划 | MoveIt 2 等规划器使用目标、机器人模型和当前状态生成关节轨迹。 |
| **4. Motion Control** | 运动控制 | 配置好的 `joint_trajectory_controller` 接收 `FollowJointTrajectory`，向硬件命令接口写入目标，再交给驱动固件和电机。 |
| **5. Feedback** | 反馈 | 编码器既反馈给本地伺服闭环，也经硬件状态接口提供测量值。`joint_state_broadcaster` 发布 `/joint_states`；`robot_state_publisher` 结合 URDF 发布 `/tf`、`/tf_static`。控制器也可直接读取状态接口。 |

## 区分接口与数据流

**区分各条路径：**URDF 描述关节、连杆和可选 `ros2_control` 接口，本身不发电机命令。TF2 查询变换，不负责运动控制。命令是期望值，状态是测量值；`/joint_states` 丢失并不必然表示底层伺服已停止。

**已有虚拟实验：** 使用的是 `forward_position_controller` 和 `mock_components/GenericSystem`，不是轨迹控制器、MoveIt 2 或真实编码器、电机。完整机器人架构仍为概念图。

**未来扩展：**故障监测、watchdog、QoS、时间同步、诊断、实时调度与仿真；保持五个英文阶段标签不变。

## 共享源码与参考资料

[打开并编辑共用 Mermaid 架构图](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) · [ROS 2 参考资料](06-ros2-foundations.md) · [模拟控制器练习](07-ros2-control-lab.md)
