# 6. ROS 2：分布式机器人软件与通信接口

**Languages:** [en](../../en/notes/06-ros2-foundations.md) · [fr](../../fr/notes/06-ros2-foundations.md) · [de](../../de/notes/06-ros2-foundations.md) · [it](../../it/notes/06-ros2-foundations.md) · [es](../../es/notes/06-ros2-foundations.md) · [pt](../../pt/notes/06-ros2-foundations.md) · [zh](06-ros2-foundations.md) · [ja](../../ja/notes/06-ros2-foundations.md) · [nb](../../nb/notes/06-ros2-foundations.md) · [ru](../../ru/notes/06-ros2-foundations.md) · [ko](../../ko/notes/06-ros2-foundations.md) · [fi](../../fi/notes/06-ros2-foundations.md) · [pl](../../pl/notes/06-ros2-foundations.md)

**本页使用的单位（示例前先解释）:** `m` — 米; `s` — 秒. [完整单位表](../UNITS.md).

[Course index](../README.md) · [Coordinate frames](04-coordinate-frames.md) · [Jacobian](05-velocity-jacobian.md) · [Docker lab](../../../ros2/README.md)

> **Safety:** 本章只使用合成数据和软件模拟，不得据此控制真实机器人或设备。ROS 通信不能代替运动学、实时控制与硬件安全机制。

ROS 2（Robot Operating System 2）为机器人的分布式软件组件提供通信和工具。对后端开发者，可以把节点（node）理解为逻辑计算组件，把话题（topic）理解为有类型的异步数据流，把服务（service）理解为请求/响应接口。但它不是普通的 HTTP 服务或中央消息代理：ROS 2 通常通过 DDS 分布式发现通信端点。

![ROS 2 publisher and subscriber linked through a typed topic; a CLI process calls a service](../../../assets/figures/ros2-topic-service.svg)

![ROS 2 软件层次与底层硬件安全边界](../../../assets/figures/ros2-software-layers.svg)

*通信中间件不能替代设备实时控制和独立的安全机制。*

## 学习路线

1. [架构、middleware 与 ROS graph](#section-1)
2. [Nodes、topics 与类型化 messages](#section-2)
3. [Services、actions 与 parameters](#section-3)
4. [Packages、workspaces、colcon 与 ament](#section-4)
5. [通过 ROS 2 CLI 观察系统](#section-5)
6. [Launch files 启动配置](#section-6)
7. [tf2 与坐标系（coordinate frames）](#section-7)
8. [URDF 与 robot_state_publisher](#section-8)
9. [ros2_control 与硬件边界](#section-9)
10. [QoS、DDS discovery 与 Docker](#section-10)
11. [实践：两个节点、topic、service 与 launch](#section-11)
12. [术语与限制](#section-12)

<a id="section-1"></a>

## 1. 架构、middleware 与 ROS graph

**工程问题：** 摄像头、定位、规划与执行模块需要独立开发，又能互相交换数据。ROS 1 使用中心 master 进行名称发现；ROS 2 采用 RMW（ROS Middleware）抽象层，通常借助 DDS/RTPS 在没有 ROS 1 master 的情况下发现参与者。ROS graph 是已发现的节点、话题、服务和动作的集合。节点不一定等于进程：一个进程可包含多个节点，进程也可分布在不同主机。发现不是身份认证。

<a id="section-2"></a>

## 2. Nodes、topics 与类型化 messages

**工程问题：** 一份周期测量数据要提供给多个消费者。发布者（publisher）向 topic 发送有类型的消息，订阅者（subscriber）异步接收。std_msgs/msg/String 具有 string data 字段；Python 和 C++ 使用同一接口定义。/sample_source 向 /training/status 发布 sample N，/sample_monitor 接收并计数。队列深度 10 不代表持久存储，新订阅者通常只能看到之后的消息。

**发现过程示例：** 假设 `/sample_source` 在发现 `/sample_monitor` 之前已经发布了 `sample 1`。本实验使用 `volatile` 历史策略，因此不会自动补发这条旧消息。即使 publisher 还在继续发送，监视节点也可能首先返回 `received 0 samples`。发现兼容的 endpoints 后，接收计数才可能增加。发送序列号与接收计数反映不同事实，都不是事务确认。

**CLI 能证明什么：** `ros2 topic list -t` 显示已发现的 topic 名称和消息类型，**不能证明 subscriber 已收到消息**。`ros2 topic info /training/status -v` 显示发现的 endpoints 及其提供/请求的 QoS。看到零个订阅者，可能是没有运行订阅者，**也可能**是发现尚未完成。如果存在 endpoints 却没有数据，先检查类型和 QoS 兼容性，再查进程日志和 `ROS_DOMAIN_ID`。这些命令提供当前状态快照，不保证消息交付。请在实验容器内运行。

<a id="section-3"></a>

## 3. Services、actions 与 parameters

**工程问题：** 区分连续数据、短请求与长任务。Service 使用 request/response；/training/count 采用 std_srvs/srv/Trigger 返回 success 与 message。Action 有 goal、feedback、result 与 cancel，适合导航目标等持续任务。Parameter 属于某个节点：interval_s=1.0 在启动时创建定时器；运行中修改参数不会自动重建定时器。请求超时和重试是否安全，需要应用逻辑决定。

应根据持续时间、是否需要响应及失败语义选择通信机制，不能只看接口名称：

| 机制 | 通信方式 | 适合场景 | 不等同于 |
| --- | --- | --- | --- |
| Topic | 发布者 → 0..N 个订阅者 | 连续状态或遥测 | 持久日志或已确认的事务 |
| Service | 请求 → 响应 | 短查询或有界操作 | 保证完成的远程事务或长任务 |
| Action | 目标 → 反馈/结果，可取消 | 较长的导航或计算任务 | 周期性传感器流 |
| Parameter | 由节点持有的值 | 如 `interval_s` 的配置 | 全局分布式配置数据库 |

本例中 `/training/status` 使用 topic，`/training/count` 使用 service，`interval_s` 是节点参数；没有实现应用 action。Service 超时不代表服务器没有执行过请求，是否安全重试要由具体操作的语义决定。

<a id="section-4"></a>

## 4. Packages、workspaces、colcon 与 ament

**工程问题：** 可重复地构建并安装节点及依赖。package.xml 保存包元数据；ament_python 或 ament_cmake 负责构建集成。Workspace 通常包含 src、build、install、log。colcon 组织构建，并非通信协议。进入新的 shell 时先 source ROS underlay，再 source workspace overlay。本例 telemetry_demo 的 setup.py 注册两个可执行入口，并安装 launch 文件。

真实的 `ros2/Dockerfile` 把**镜像构建**（`RUN`）和**容器启动**（`CMD`）分成两个阶段。构建阶段先加载 ROS underlay，再由 `colcon` 编译软件包：

**镜像构建（`RUN`）：**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
colcon build --packages-select telemetry_demo
```

**容器启动（`CMD`）：**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
source /opt/training_ws/install/setup.bash
exec ros2 launch telemetry_demo demo.launch.py
```

容器启动时使用新的 shell **再次**加载 ROS underlay，然后加载已经构建的 workspace overlay 并运行 launch 文件。`package.xml` 声明依赖，`setup.py` 安装 Python 可执行入口和 launch 文件。`build/` 与 `install/` 是生成的产物，不应直接修改其中的源码。构建成功并不保证 ROS 图已经就绪。

<a id="section-5"></a>

## 5. 通过 ROS 2 CLI 观察系统

**工程问题：** 检查实际运行的图，而非只看配置。ros2 node list/info 查询节点，topic list/info/echo 查询数据流，interface show 显示消息定义，service list/call、action list、param get 查询其他端点。应能看到 /sample_source、/sample_monitor、/training/status 和 /training/count。本例没有应用 action。若没有数据，逐项检查名称、类型、QoS 和 ROS_DOMAIN_ID。

进入容器并 source 环境后，可以使用这些 CLI 命令：

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

## 6. Launch files 启动配置

**工程问题：** 一次启动多个进程并保持参数一致。demo.launch.py 返回 LaunchDescription，包含两个 launch_ros.actions.Node，并向发布者传入 interval_s=1.0。Launch 支持参数、命名空间、remapping 与嵌套文件。进程启动不等于服务立即就绪，发现、健康状态和重试属于应用设计。

**应观察就绪状态，不能只看进程启动：** `launch_ros.actions.Node` 会启动两个**进程**，随后 DDS 才发现节点，`/training/status` 才出现第一条消息。此时立即调用 `/training/count` 完全可能返回 `received 0 samples`，稍后计数才会增加。这不代表事务丢失：service 只统计监视节点收到的消息。`interval_s=1.0` 在创建计时器时读取，运行期间不会自动重设其周期。

<a id="section-7"></a>

## 7. tf2 与坐标系（coordinate frames）

**工程问题：** 把 camera_link 下的观测换算到 base_link 或 map。tf2 管理带时间戳的坐标变换，包括旋转和平移；固定装配使用静态变换，活动关节需要动态变换。父子坐标系、时间及单位必须一致。tf2 不会自动求解正逆运动学或规划轨迹；数学推导请参见坐标系和 Jacobian 章节。

[Coordinate frames](04-coordinate-frames.md) · [Velocity and Jacobian](05-velocity-jacobian.md)

**坐标链示例（不是 ROS 强制规定的结构）：** `map → odom → base_link → camera_link`。刚性安装的摄像头相对底盘有 `static` 变换，移动中的底盘需要 `dynamic` 变换。若摄像头在时刻 *t* 通过 `camera_link` 观测到一点，tf2 必须查询**测量时间对应的**到 `map` 的完整变换链。若坐标系不存在、树不连通，或该时间的数据不可用，就会出现 lookup/extrapolation 错误；不能直接用最新变换替代历史观测时刻的变换。

**变换方向与逆变换的完整例子。** 设 `base_link`（B）为父坐标系，`tool`（T）为子坐标系。若无相对旋转，并且沿父坐标系正 X 方向平移 0.1 m，表示工具原点在 **B 中的坐标比基座原点沿 X 正向多 0.1 m**。反过来用 T 表示基座原点，则位移符号相反：

$$
{}^{B}\mathbf p_{T}=(0.1, 0, 0)\ \mathrm{m},\qquad
{}^{T}\mathbf p_{B}=(-0.1, 0, 0)\ \mathrm{m}\quad (R=I).
$$

只有两套坐标轴的**方向相同**时，简单取反平移才成立。一般的坐标变换同时包含旋转与平移，逆变换必须撤销**这两部分**；对于有效的旋转矩阵，逆矩阵为 $R^T$：

$$
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT},\qquad
\mathbf p_T=R_{BT}^{T}(\mathbf p_B-\mathbf t_{BT}),\qquad
\mathbf t_{TB}=-R_{BT}^{T}\mathbf t_{BT}.
$$

再考虑另一种姿态：T 绕共同的 Z 轴旋转 +90°，但在 B 中仍平移 (0.1 m, 0 m)。此时基座原点在 T 中的坐标是 (0 m, +0.1 m)，**不是** (−0.1 m, 0 m)。同样的矩阵还可将 T 中的点 (0 m, 0.05 m) 变换到 B：

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

坐标系与变换只是**描述坐标关系**，并不会向电机发出移动命令。ROS 2 的平移量通常按米表示；前面的[坐标系课程](04-coordinate-frames.md#section-3)使用毫米，合并例题之前必须换算。静态变换描述固定安装关系，动态变换由提供最新状态的组件发布。处理历史测量时应使用测量时刻的变换，并处理该时间戳的数据缺失。

<a id="section-8"></a>

## 8. URDF 与 robot_state_publisher

**工程问题：** 让所有软件共享机械结构描述。URDF 定义 link、joint、原点、轴和可选的 visual/collision/inertial 属性。robot_state_publisher 根据 URDF 和关节位置（通常是 /joint_states 上的 sensor_msgs/msg/JointState）发布变换。URDF 本身不是传感器、模拟器或逆运动学求解器。注意 m、rad、关节轴和时间戳。

**变换从哪里来：** URDF 描述 `fixed` 和可移动的 joint。`robot_state_publisher` 根据固定关节几何发布 `static` 变换，根据 `/joint_states`（`sensor_msgs/msg/JointState`）上的关节位置发布移动关节的 `dynamic` 变换。URDF **不会测量**关节位置，也不会补全缺失的传感数据。尺寸、角度和时间戳应分别采用一致的米、弧度和时间基准。

<a id="section-9"></a>

## 9. ros2_control 与硬件边界

**工程问题：** 把规划和控制器与设备驱动解耦。ros2_control 提供 controller manager、状态接口（位置、速度）、命令接口（位置、速度、effort）以及硬件抽象。典型链路是规划器→控制器→硬件接口→设备，并通过状态接口反馈。发送 ROS 消息并不保证实时性、限流或安全停机；此模拟例子没有执行器。

[First-order dynamics](02-first-order-dynamics.md) · [Feedback PID](03-feedback-control.md)

**controller manager 的实际职责：** `controller_manager` 管理控制器的生命周期，并通过资源管理器协调状态接口（state interfaces）和命令接口（command interfaces）的使用。控制器可以读取测量状态，例如假设模型中的 `joint1/position`；激活的控制器可以占用兼容的命令接口，写入期望值。实际测量值不等于目标值，两个控制器也不能随意同时占用同一个已被占用的命令接口。因此，控制器的激活与资源分配不是简单的 topic 发现。

**本实验的边界：** `/training/status` 和 `/training/count` 仅展示 topic 与 service，**没有使用 `ros2_control`**。这两个 node 都不是控制器；实验不启动 `controller_manager`，没有硬件接口，也没有闭环控制。即使 smoke test 通过，也不能据此证明控制器生命周期、实时性能或设备安全性。参见 [ros2_control 官方入门文档](https://control.ros.org/jazzy/doc/getting_started/getting_started.html)。

**后续实践：无 GUI 的 ros2_control、TF2 和虚拟关节:** [后续实践：无 GUI 的 ros2_control、TF2 和虚拟关节](07-ros2-control-lab.md). 新实验介绍 URDF、GenericSystem、命令、状态、/joint_states、TF2、QoS 和 ARM64 加载器诊断；不控制真实设备。

**下一步：机器人整体架构。** [五阶段 ROS 2 Mermaid 图](08-ros2-robot-architecture.md)串联感知、带时间戳的 TF2、运动规划、控制和反馈。硬件路径仅作概念说明。

<a id="section-10"></a>

## 10. QoS、DDS discovery 与 Docker

**工程问题：** 诊断消息丢失和节点不可见。QoS 包括 reliable/best_effort、volatile/transient_local、history 与 depth。订阅者要求的可靠性若高于发布者提供的等级，即使名称类型一致也可能没有消息。DDS 往往使用 UDP multicast 与动态端口；Docker Desktop、VPN 和防火墙可能影响发现。ROS_DOMAIN_ID 必须匹配。本实验所有组件位于同一个无特权容器，不代表跨主机网络已经验证。

**QoS 不兼容示例：** publisher 提供 `best_effort`，subscriber 却请求 `reliable`。即使 topic 名称和消息类型匹配，图中能发现端点，订阅者也可能**完全收不到数据**，因为所请求的可靠性高于发布者所提供的。反过来，`best_effort` 订阅者可以连接 `reliable` 发布者，前提是其他 QoS 策略也兼容。`volatile` 不会重放过去的数据；`transient_local` 只能从仍然可用的兼容发布者获得有限的保留历史，**不是持久分布式日志**。

**排查顺序：** 在同一个容器内确认 `ROS_DOMAIN_ID=42`，然后执行 `ros2 node list`、`ros2 topic info /training/status -v`（检查端点和 QoS）以及 `docker compose logs demo`（检查进程日志）。如果图仍不可见，再检查 RMW/DDS、网络接口和防火墙。单纯映射 TCP 端口不能普遍解决 DDS 问题；本例没有验证跨主机通信。

[ROS 2 Jazzy 官方 QoS 文档](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)

[替代方案：无需 Compose 和自定义 Dockerfile 的官方 ROS 镜像](../../../ros2/PLAIN_DOCKER.md)

<a id="section-11"></a>

## 11. 实践：两个节点、topic、service 与 launch

运行 docker compose up --build -d，日志应持续显示发布和接收的 sample，计数逐步增加。Service 返回 success=True 和 received 12 samples 一类文本，具体数字取决于运行时间。[独立的 GitHub Actions Docker 冒烟测试](../../../.github/workflows/ros2-live-smoke.yml) 已**在单个容器内实际启动**该应用，确认两个 ROS 节点、`/training/status` 上的类型化消息及 `/training/count` 的服务响应。普通静态 CI 不运行 ROS。这些验证不包括跨主机 DDS 通信、确定性实时性能、真实硬件或读者本地的 Docker 环境。

[Source, expected results and troubleshooting](../../../ros2/README.md). From the repository root:

按顺序学习：先运行镜像已安装的 `demo_nodes_cpp` talker 和 `demo_nodes_py` listener，然后查看仓库自建的 `telemetry_demo` 软件包，最后进入 `ros2_control`。Dockerfile 使用 APT 安装标准示例，用 `colcon` 构建 `telemetry_demo`。交互学习只需打开**一个 Bash shell**，每个新 shell 各执行一次环境加载；独立的 `docker compose exec` 进程不会继承容器 `CMD` 的 shell 环境。

在宿主机上启动容器并打开交互式 shell：

```bash
cd ros2
docker compose up --build -d
docker compose logs --tail=20 demo
docker compose exec demo bash
```

在容器内部（不是宿主机）仅加载一次环境并查看 ROS 图：

```bash
echo "$ROS_DISTRO"
ros2 node list
ros2 service call /training/count std_srvs/srv/Trigger "{}"
exit
```

执行 `exit` 回到宿主机后，再清理容器：

```bash
docker compose down
```

**CI 信任边界：** ROS 2 Docker 实际冒烟测试现在只会在相关修改进入 `main` 后自动执行，或通过在 `main` 上手动触发 `workflow_dispatch` 执行。它**不会对 `pull_request` 提交直接运行**，否则 GitHub 宿主 runner 就会执行 PR 提供的 Bash 脚本和 Dockerfile。合并前隔离运行的 Python 测试不能代替真正的 ROS 运行测试。合并前应进行独立代码审查，并在合并后核对实际 ROS 测试结果。

<a id="section-12"></a>

## 12. 术语与限制

- **Node / process（节点 / 进程）：** 节点是有名称的 ROS 逻辑组件，一个操作系统进程可以容纳多个节点。
- **ROS graph（ROS 图）：** 当前发现的通信端点集合，不是永久的中央注册表，也不是权限验证机制。
- **Topic（话题）：** 有名称的异步数据流，可以有多个发布者和订阅者。
- **Message（消息）：** 由 ROS interface 定义的类型化数据结构，而非任意 Python 或 C++ 对象。
- **Publisher / subscriber（发布者 / 订阅者）：** 发送或接收话题消息；需要先发现端点并满足 QoS 兼容性。
- **Service（服务）：** 适合短交互的类型化请求与响应；超时不能证明服务端没有执行操作。
- **Action（动作）：** 包含目标、feedback、结果和取消请求；请求取消不等于保证立即停止。
- **Parameter（参数）：** 归单个节点所有的配置值；修改后并不会自动重建已创建的计时器。
- **RMW / DDS：** RMW 抽象通信中间件；DDS 常用于发现与传输，本身不等于身份认证。
- **colcon / ament：** 工作空间构建协调工具 / ROS 包构建集成，不是消息传输层。
- **Launch（启动描述）：** 描述进程和启动配置；启动成功不代表 ROS graph 已准备就绪。
- **tf2：** 带时间戳的坐标系变换基础设施，不是逆运动学求解器。
- **URDF / robot_state_publisher：** 机器人结构模型 / 根据模型和当前关节状态发布坐标变换。
- **ros2_control：** 管理控制器生命周期及 state/command 接口；本 topic/service 实验不包含它。
- **QoS：** 请求与提供的传输策略兼容性、交付及历史设置；不是持久事件日志或安全认证。

**版本信息（2026 年 11 月 13 日核实）：** ROS 2 Jazzy LTS 支持至 2029 年 5 月，Lyrical LTS 支持至 2031 年 5 月。Docker 标签没有固定不可变镜像 digest 或 apt 软件包版本。

**Primary sources:** [ROS 2 releases](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst) · [Jazzy documentation](https://docs.ros.org/en/jazzy/) · [tf2](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html) · [URDF](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html) · [ros2_control](https://control.ros.org/jazzy/)
