# 8. ROS 2 ロボット構成：五つの機能段階

**言語:** [en](../../en/notes/08-ros2-robot-architecture.md) · [fr](../../fr/notes/08-ros2-robot-architecture.md) · [de](../../de/notes/08-ros2-robot-architecture.md) · [it](../../it/notes/08-ros2-robot-architecture.md) · [es](../../es/notes/08-ros2-robot-architecture.md) · [pt](../../pt/notes/08-ros2-robot-architecture.md) · [zh](../../zh/notes/08-ros2-robot-architecture.md) · [ja](08-ros2-robot-architecture.md) · [nb](../../nb/notes/08-ros2-robot-architecture.md) · [ru](../../ru/notes/08-ros2-robot-architecture.md) · [ko](../../ko/notes/08-ros2-robot-architecture.md) · [fi](../../fi/notes/08-ros2-robot-architecture.md) · [pl](../../pl/notes/08-ros2-robot-architecture.md)

[ROS 2 の基礎](06-ros2-foundations.md) · [仮想関節実習](07-ros2-control-lab.md) · [目次](../README.md)

> **概念説明のみ。** 実機の制御も安全保証も行いません。

下の五つの英語ラベルは[共通の編集可能な Mermaid 図](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram)と完全に一致します。段階は**機能であり、ROS ノード一個と同義ではありません**。図は概念モデルで、実機を制御するプログラムや安全設計ではありません。

## 五つの機能段階

| 英語の段階名 | 日本語訳 | 役割と ROS コンポーネント |
| --- | --- | --- |
| **1. Perception** | 知覚 | カメラドライバが撮影時刻付き `sensor_msgs/msg/Image` を発行し、アプリケーション検出器が `camera_link` で物体位置姿勢を推定します。 |
| **2. Coordinate Transformation** | 座標変換 | アプリケーションは `tf2_ros.Buffer.lookup_transform` で撮影時刻の物体位置を `base_link` に変換します。カメラの固定位置は URDF または静的 TF 発行者で供給します。 |
| **3. Motion Planning** | 動作計画 | MoveIt 2 などの計画器が目標、モデル、現在の状態から関節軌道を作ります。 |
| **4. Motion Control** | 動作制御 | 設定済み `joint_trajectory_controller` が `FollowJointTrajectory` を受け取り、ハードウェア指令インターフェース経由でドライブとモータに目標を伝えます。 |
| **5. Feedback** | フィードバック | エンコーダ値はローカルサーボ制御とハードウェア状態インターフェースへ戻ります。`joint_state_broadcaster` は `/joint_states`、`robot_state_publisher` は URDF に基づき `/tf` と `/tf_static` を発行します。コントローラは状態を直接読むこともあります。 |

## インターフェースの区別

**経路の区別：** URDF は構造と任意の `ros2_control` インターフェースを記述するもので、モータ指令ではありません。TF2 は座標変換を問い合わせます。指令は目標値、状態は測定値です。`/joint_states` が途切れてもローカルサーボ停止とは限りません。

**既存の仮想実習：** `forward_position_controller` と `mock_components/GenericSystem` を使用し、軌道コントローラ、カメラ、MoveIt 2、実機は使いません。図全体は概念的です。

**後の拡張：** 安全監視、watchdog、QoS、時刻同期、診断、リアルタイム、シミュレーション。五つの段階名は変更しません。

## 共通ソースと参考資料

[共通 Mermaid 構成図を開いて編集](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) · [ROS 2 参考資料](06-ros2-foundations.md) · [模擬コントローラ実習](07-ros2-control-lab.md)
