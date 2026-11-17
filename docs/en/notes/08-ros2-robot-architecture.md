# 8. ROS 2 robot architecture: five stages

**Languages:** [en](08-ros2-robot-architecture.md) · [fr](../../fr/notes/08-ros2-robot-architecture.md) · [de](../../de/notes/08-ros2-robot-architecture.md) · [it](../../it/notes/08-ros2-robot-architecture.md) · [es](../../es/notes/08-ros2-robot-architecture.md) · [pt](../../pt/notes/08-ros2-robot-architecture.md) · [zh](../../zh/notes/08-ros2-robot-architecture.md) · [ja](../../ja/notes/08-ros2-robot-architecture.md) · [nb](../../nb/notes/08-ros2-robot-architecture.md) · [ru](../../ru/notes/08-ros2-robot-architecture.md) · [ko](../../ko/notes/08-ros2-robot-architecture.md) · [fi](../../fi/notes/08-ros2-robot-architecture.md) · [pl](../../pl/notes/08-ros2-robot-architecture.md)

[ROS 2 foundations](06-ros2-foundations.md) · [Virtual joint lab](07-ros2-control-lab.md) · [Index](../README.md)

> **Simulation-only / conceptual.** No physical control or safety guarantee.

The five English stage names below are identical to the labels in the [shared, editable Mermaid diagram](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram). Each stage is a function, **not necessarily one ROS process or node**. The diagram is an illustrative architecture, not a runnable robot or safety design.

## Five functional stages

| English stage | Local term | Responsibilities and ROS components |
| --- | --- | --- |
| **1. Perception** | Perception | Camera driver publishes `sensor_msgs/msg/Image` with acquisition time; an application detector estimates object pose in `camera_link`. |
| **2. Coordinate Transformation** | Coordinate transformation | The application uses `tf2_ros.Buffer.lookup_transform` to convert camera-frame pose into `base_link` at the image timestamp. `robot_state_publisher` or a static broadcaster must supply camera mounting transforms. |
| **3. Motion Planning** | Motion planning | A planner (e.g. MoveIt 2) uses the target pose, robot model and state to produce a joint trajectory. |
| **4. Motion Control** | Motion control | A configured `joint_trajectory_controller` accepts `FollowJointTrajectory`, writes hardware command interfaces, and sends requested motion to servo firmware and motor. |
| **5. Feedback** | Feedback | An encoder feeds a local servo loop and hardware state interfaces. `joint_state_broadcaster` publishes `/joint_states`; `robot_state_publisher` uses URDF and joint states to publish `/tf` and `/tf_static`. Controllers may read state directly. |

## Distinguishing the interfaces

**Do not conflate the arrows:** URDF describes robot structure and optionally ros2_control interfaces; it does not command motors. TF2 queries transforms, it does not actuate a robot. Commands are requested values, state interfaces report measured values; loss of `/joint_states` does not necessarily mean the firmware servo has stopped.

**Existing reproducible lab:** The separate virtual joint example uses `forward_position_controller` and `mock_components/GenericSystem`, **not** the trajectory controller, camera, MoveIt 2 or real motor and encoder. The diagram's wider architecture is conceptual.

**Extensions:** Introduce failure supervision, watchdogs, QoS, time synchronization, diagnostics, real-time constraints and simulation as later, independently explained additions. Keep the five stage labels unchanged.

## Shared source and additional reading

[Open and edit the single Mermaid architecture diagram](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) · [ROS 2 reference](06-ros2-foundations.md) · [Mock controller practice](07-ros2-control-lab.md)
