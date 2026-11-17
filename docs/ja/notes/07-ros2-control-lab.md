# 7. GUI なし ROS 2 Jazzy 実習：仮想関節と TF2

**Languages:** [en](../../en/notes/07-ros2-control-lab.md) · [fr](../../fr/notes/07-ros2-control-lab.md) · [de](../../de/notes/07-ros2-control-lab.md) · [it](../../it/notes/07-ros2-control-lab.md) · [es](../../es/notes/07-ros2-control-lab.md) · [pt](../../pt/notes/07-ros2-control-lab.md) · [zh](../../zh/notes/07-ros2-control-lab.md) · [ja](../../ja/notes/07-ros2-control-lab.md) · [nb](../../nb/notes/07-ros2-control-lab.md) · [ru](../../ru/notes/07-ros2-control-lab.md) · [ko](../../ko/notes/07-ros2-control-lab.md) · [fi](../../fi/notes/07-ros2-control-lab.md) · [pl](../../pl/notes/07-ros2-control-lab.md)

[実行可能な実習と詳細診断](../../../ros2/control_lab/README.md) · [ROS 2](06-ros2-foundations.md) · [ja](../README.md)

> **Simulation-only / mock hardware.** No real actuators.

Ubuntu Noble の ROS 2 Jazzy Docker コンテナ（対応する AMD64 または ARM64）で実行します。Gazebo、RViz、デスクトップ、実機モーターは不要です。既存の topic/service 実習は変更しません。

**全体構成：** [五段階の図と二言語用語表](08-ros2-robot-architecture.md)で仮想実習の位置付けを示します。この実習はカメラ、計画器、サーボファームウェア、実機を**動かしません**。

## 1. URDF, hardware and state

URDF は親 `base_link`、+Z 軸回転の `joint_1`、子 `arm_link`、さらに X 方向 +0.2 m（メートル、metre）に固定した `tool_mount` と `tool` を定義します。`mock_components/GenericSystem` は `joint_1/position` の指令と状態だけを提供します。コントローラーが指令し、broadcaster が状態を発行し、`robot_state_publisher` が TF2 を計算します。

[arm.urdf](../../../ros2/control_lab/arm.urdf) · [controllers.yaml](../../../ros2/control_lab/controllers.yaml) · [control.launch.py](../../../ros2/control_lab/control.launch.py) · [Dockerfile](../../../ros2/control_lab/Dockerfile)

[別の手順：Compose や独自 Dockerfile を使わずに公式 ROS イメージを起動](../../../ros2/PLAIN_DOCKER.md)

## 2. Packages and environment

公式 ROS イメージには `ROS_DISTRO` が定義されています。ホストやコンテナで再設定しないでください。Dockerfile がコントローラーを導入し、対話型 Bash で ROS を自動設定します。以下は確認コマンドです。手動導入は Docker ガイドを参照してください。

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

**この実習の Dockerfile で必要なパッケージはすでにインストールされています。** 次のコマンドは確認用であり、ビルド済みコンテナへの再インストールは不要です。別の Jazzy 環境への手動インストールは完全版ガイドを参照してください。

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

正しい TF2 ツリーで子フレームの親は一つだけです。変換は並進と回転で構成され、`base_link → arm_link → tool` の順に合成し、逆向きは逆変換を使います。URDF の固定関節は `/tf_static`、回転・直動・連続関節は状態があるとき `/tf` に発行します。生の `TFMessage` はタイムスタンプ付きデータですが、`tf2_echo` は時刻バッファーを問い合わせて合成結果を示します。DDS `transient_local` は永続ログではありません。自動 QoS と明示的 durability が違う場合 `--qos-reliability reliable` も試します。

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

## 5. ARM64 shared-library diagnostics

ARM64 の事例では `robot_state_publisher` が `pluginlib::LibraryLoadException` で終了し、ローダーから `libsdformat14.so.14` が見えず、`ldd` は `libgz-math7.so.7` も未解決としました。しかし SDFormat は既に `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/` にあり、APT に `libsdformat14` 候補はありませんでした。core、`/robot_description`、単体 publisher、`ldd`、vendor パス、`LD_LIBRARY_PATH` を調べます。ROS を読み込み実在するディレクトリだけ一時追加します。ABI の偽装 symlink や core の公開は禁止です。その後の起動は確認済みですが、実際の修復コマンドは不明です。

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

**条件付きライブラリ検索パスの復旧（恒久的な修正の確認ではない）：** [一時的な復旧手順](../../../ros2/control_lab/README.md#temporary-recovery-for-a-missing-vendor-library)を参照します。まず `ldd` を確認し、ROS を source、存在する vendor ディレクトリだけ追加して、**同じシェル**で再確認します。

## 6. Limits and verification

`GenericSystem` は指令を状態へコピーする理想化モデルで、モーター、エンコーダー、PID、動力学、安全停止ではありません。実サーボには計測、ドライバー、フィードバック制御、保護が必要です。`ForwardCommandController` はこれらを保証しません。静的チェックと実際の Docker ROS テストは別です。

[実行可能な実習と詳細診断](../../../ros2/control_lab/README.md) · [Official ros2_control](https://control.ros.org/jazzy/) · [ROS QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
