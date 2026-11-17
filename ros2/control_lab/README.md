# Headless ROS 2 Jazzy: one virtual joint with ros2_control

**How it fits into a robot:** [The five-stage Mermaid architecture](../ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) distinguishes a trajectory controller, state feedback, TF and the URDF model. The larger diagram is conceptual; this lab implements only a virtual joint with `forward_position_controller`, not perception, MoveIt 2 or a physical drive.

This **synthetic software exercise** extends the existing [ROS 2 topic/service lab](../README.md). It does not control equipment, model a motor or certify a servo loop. No Gazebo, RViz, X server, VNC, XFCE, devices, privileged containers or host networking are required.

**Version:** ROS 2 Jazzy Jalisco on Ubuntu 24.04 (Noble), AMD64 or ARM64/aarch64 when matching official packages and base-image manifests are available. The `ros:jazzy-ros-base` image tag and APT packages are mutable; the procedure is reproducible but not a byte-for-byte locked build. Review the Dockerfile before running it. Docker daemon access is privileged on many hosts: do not add credentials or unsafe mounts.

## 1. Build the image and open one shell

If you want to install the packages manually instead, use the [plain official-image Docker walkthrough](../PLAIN_DOCKER.md). First complete the [standard ROS demos and custom-package lesson](../README.md): official `demo_nodes_cpp` / `demo_nodes_py` → built `telemetry_demo` → this virtual-joint lab. The labs have independent images so that `ros2_control` dependencies are not required for the first two exercises. The control image's [Dockerfile](Dockerfile) installs `ros-${ROS_DISTRO}-ros2-control`, `ros-${ROS_DISTRO}-ros2-controllers`, `robot_state_publisher`, and the other dependencies **at build time**. There is no need to install them again inside the finished container.

From the **repository root on the host**:

```bash
docker build -t training-ros-control -f ros2/control_lab/Dockerfile ros2/control_lab
docker run -d --name training-ros-control --env ROS_DOMAIN_ID=43 training-ros-control
docker exec -it training-ros-control bash
```

The image's `CMD` sources ROS for the launched application. The Dockerfile added the base ROS setup to `/root/.bashrc`. The newly opened **interactive** `docker exec` shell loads it automatically:

```bash
printf 'ROS_DISTRO=%s\n' "$ROS_DISTRO"
ros2 pkg prefix controller_manager
ros2 pkg prefix joint_state_broadcaster
ros2 pkg prefix joint_trajectory_controller
ros2 pkg prefix forward_command_controller
ros2 pkg executables controller_manager
```

Inspect the package/executable output. On the tested configuration the controller-manager executables include `ros2_control_node`, `spawner`, `unspawner` and `hardware_spawner`; installations can differ. The installed `joint_trajectory_controller` is available for inspection but **not used** in this example, which uses `forward_command_controller`. No closed-loop position tracking algorithm is implemented.

**Only for a separate bare Jazzy environment**, not for the already built image, installation would be:

```bash
echo "ROS_DISTRO=$ROS_DISTRO"
source "/opt/ros/$ROS_DISTRO/setup.bash"
apt-get update
apt-get install -y ros-$ROS_DISTRO-ros2-control ros-$ROS_DISTRO-ros2-controllers
```

The official base image already defines `ROS_DISTRO`; never override it from the host to a mismatched release. This is only an optional manual installation reference for a separate non-prepared environment, not a step to repeat in this Docker lab.

## 2. Understand the files

- [arm.urdf](arm.urdf): `base_link` → revolute `joint_1` (rotation about +Z) → `arm_link` → fixed `tool_mount` (offset +0.2 m along local X) → `tool`. The `<ros2_control>` block declares `mock_components/GenericSystem` with only `joint_1/position` command and state interfaces.
- [controllers.yaml](controllers.yaml): `controller_manager` at 50 Hz, `joint_state_broadcaster` and a `ForwardCommandController` named `forward_position_controller`.
- [control.launch.py](control.launch.py): starts `robot_state_publisher`, `ros2_control_node` and two controller spawners. It includes the traditional `~/robot_description` remapping for compatibility; Jazzy's controller manager subscribes directly to `robot_description` in current releases, so inspect the actual resolved topic. Spawners wait for the manager's services; process start order is not readiness.
- [Dockerfile](Dockerfile): installs ROS packages and launches the Python file directly. The existing `ros2/demo_pkg` and telemetry Dockerfile are unaffected.

`robot_state_publisher` publishes the URDF string on `/robot_description`; `ros2_control_node` needs this description before it can load hardware. The `GenericSystem` mock reflects its position command into the state interface without a real driver, dynamics or encoder. `joint_state_broadcaster` reads that state and publishes `/joint_states`. `robot_state_publisher` then uses joint positions to publish the moving transform into `/tf`. The fixed mounting appears in `/tf_static`.

## 3. Observe the complete command-to-TF chain

Keep the container running and enter it using `docker exec -it training-ros-control bash`; the image's `~/.bashrc` sources ROS automatically. Wait until the spawners have activated both controllers:

```bash
ros2 node list
ros2 topic info /robot_description -v
ros2 control list_controllers
ros2 control list_hardware_components
ros2 control list_hardware_interfaces
ros2 topic info /forward_position_controller/commands -v
```

Expected controller states are `joint_state_broadcaster ... active` and `forward_position_controller ... active`. Expect `joint_1/position [available] [claimed]` under command interfaces and `joint_1/position` under state interfaces. The **claimed** flag means the active controller owns the command interface; it does not indicate successful physical movement.

Publish one command (the subscription must be ready):

```bash
ros2 topic pub --once \
  /forward_position_controller/commands \
  std_msgs/msg/Float64MultiArray \
  '{data: [1.0]}'

ros2 topic echo /joint_states --once
ros2 run tf2_ros tf2_echo base_link tool
```

Expected synthetic feedback: `/joint_states` contains `joint_1`, `position: [1.0]` rad; `velocity` and `effort` may contain `.nan` (IEEE NaN) because those state interfaces were **not declared**, not because the position command failed. A late or early `--once` read can catch an old sample; repeat after command propagation if necessary. `tf2_echo` continuously prints the latest available transform, not a raw ROS TF message.

With arm length 0.2 m and `joint_1 = 1.0` rad about Z, the fixed tool offset is rotated into the parent frame:

```text
x = 0.2 * cos(1.0) = 0.10806046 m
y = 0.2 * sin(1.0) = 0.16829420 m
z = 0 m
yaw = 1.0 rad = 57.29578 degrees
```

Allow rounding in `tf2_echo`: translation about `[0.108, 0.168, 0.000]`, yaw about `57.296°`. If the tool stays at zero, inspect the controller state, correct topic type, interface ownership, active publishers and `/joint_states` before suspecting TF. Stop `tf2_echo` with Ctrl+C.

## 4. tf2: direction, time and late subscribers

A transform connects a **parent** coordinate frame with a **child**. In a valid TF tree each child has only one parent; a frame pair can be queried in either direction by mathematical inversion. A transform consists of translation and rotation: to express a point from child in parent coordinates, apply the rotation then add the translation. Chaining `base_link → arm_link → tool` composes transforms; reversing the query computes their inverse. The origin of the tool is at +0.2 m along `arm_link` X **before** joint rotation, not invariably at X=0.2 m in `base_link`.

`robot_state_publisher` sends fixed URDF joints to `/tf_static` and movable revolute, prismatic or continuous joints to `/tf` when the needed joint states are available. Fixed geometry can use `transient_local` durability so compatible late subscribers can receive the most recently held value *while its publisher remains available*. It is not a permanent log. For dynamic transforms, time stamps and tf2's buffered history determine whether a transform at a measurement time can be resolved; extrapolation into missing times fails.

Inspect endpoints before changing QoS:

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

The `/tf_static` message type is `tf2_msgs/msg/TFMessage`, which can contain several `TransformStamped` records. `tf2_echo base_link tool` instead asks a tf2 buffer for a **computed, composed/inverted transform** at an available time, and prints an interpretation. The CLI's automatic QoS choice may differ from specifying only `--qos-durability transient_local`; diagnose explicit `--qos-reliability reliable` and advertised/requested endpoint settings. No QoS choice can recover a publisher that has already disappeared or a missing URDF/joint state.

## 5. ARM64 loader failure: inspect, recover the search path, verify

On some Ubuntu Noble aarch64/Jazzy environments, a `robot_state_publisher` crash can leave `controller_manager` printing `Waiting for data on robot_description topic to finish initialization`, while the spawners wait for `/controller_manager/list_controllers`. This is a **symptom chain**, not proof of a malformed URDF.

If a core dump exists, inspect it locally; do not commit or upload it:

```bash
file core
ls -lh core
du -h core
ros2 node list
ros2 topic info /robot_description -v
```

`ls -lh` reports logical size; `du -h` reports allocated disk blocks, which can be much smaller for a sparse core. `file core` can identify the crashing executable. Only run it when a dump actually exists. For an isolated test in the container:

```bash
ulimit -c 0
source /opt/ros/${ROS_DISTRO}/setup.bash
ros2 run robot_state_publisher robot_state_publisher /opt/control_lab/arm.urdf
```

The positional URDF argument may issue a deprecation warning; the following loader exception is the actual failure if it occurs:

```text
pluginlib::LibraryLoadException
Failed to load libsdformat_urdf_plugin.so
libsdformat14.so.14: cannot open shared object file
```

Diagnose the plugin's linked dependencies and inspect **actual on-disk paths**:

```bash
ldd /opt/ros/${ROS_DISTRO}/lib/libsdformat_urdf_plugin.so
find /opt/ros/${ROS_DISTRO}/opt -name 'libsdformat14.so*' -o -name 'libgz-math7.so*'
printf '%s\n' "$LD_LIBRARY_PATH"
find /opt/ros/${ROS_DISTRO}/opt -path '*/share/*/environment/*' -type f
```

A particular aarch64 Noble experiment found `libsdformat14.so.14` in `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/` even though `ldd` could not resolve it; `libgz-math7.so.7` was also unresolved. Attempting `apt-get install libsdformat14` found **no installable candidate in that configured APT environment**. These observations establish a dynamic-loader visibility problem, not proof the library was absent or that APT installed it.

### Temporary recovery for a missing vendor library

**This is the proposed repair command sequence**, conditional on the library files actually existing on disk. It was not established which specific command repaired the earlier ARM64 environment. The reliable observed facts were: the correct `libsdformat14.so.14` file existed under the ROS SDFormat vendor prefix, but the dynamic loader did not find it; `libgz-math7.so.7` was also unresolved. Therefore blindly installing `libsdformat14` was not the repair.

In the **same container shell** in which the publisher or launch will run, first source the ROS environment and inspect `ldd`; if the vendor directories exist, temporarily prepend them to `LD_LIBRARY_PATH`, then verify `ldd` again. This changes only the present shell and its child processes, **not** a different already-running container process. Restart the launch from this shell if the earlier launch failed.



```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
plugin=/opt/ros/${ROS_DISTRO}/lib/libsdformat_urdf_plugin.so
ldd "$plugin" | grep -E 'sdformat|gz-math|not found' || true

# Only add directories that really exist in this installation:
for vendor in sdformat_vendor gz_math_vendor gz_utils_vendor; do
  dir="/opt/ros/${ROS_DISTRO}/opt/$vendor/lib"
  if [ -d "$dir" ]; then
    export LD_LIBRARY_PATH="$dir${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
  fi
done

# No "not found" lines should remain before retrying the process:
ldd "$plugin" | grep 'not found' || echo 'No unresolved libraries reported by ldd'
```

This is a **session-local diagnostic**, not a universal fix. Locate any remaining unresolved dependency rather than guessing the vendor package name; read the ROS vendor environment hooks. After resolving `ldd`, stop the failed launch and retest the isolated publisher **in this sourced shell** (Ctrl+C when healthy); then run `ros2 launch /opt/control_lab/control.launch.py` from this same shell. Do not reuse the old failed process. If missing dependencies remain, investigate their actual library locations rather than forcing a success message. Do not create symlinks between incompatible `.so` ABI versions, reinstall all of ROS or install unrelated Gazebo/GUI packages. A later successful controller startup was observed after troubleshooting, but the exact shell command that restored library resolution was not independently established; do not present the suggested loop as a proven permanent repair.

## 6. What this does *not* demonstrate

`GenericSystem` is an idealized **mock hardware system**, not a motor, a simulated dynamic plant, a PID controller, or actual encoder feedback. It mirrors an accepted position command into its state. A real servo uses a motor driver and typically an encoder or other sensor to estimate the **actual** joint position; a control loop compares the requested value with measured position and handles errors, effort/current limits, timing, faults and safe stop behavior. The loop might be in firmware, a drive or a ROS controller; `ForwardCommandController` by itself supplies no such guarantee. URDF geometry and TF only interpret positions; they cannot verify real motion.

The [trusted-main Docker CI workflow](../../.github/workflows/ros2-live-smoke.yml) has executed the telemetry graph and the new virtual-joint path successfully on its Linux runner; the control test observed active controllers, 1.0 rad position and the expected tool translation. This does **not** prove a clean ARM64 installation, yaw independently, real equipment or your host's Docker. Ordinary PR Python checks are static; inspect the result for the commit being discussed.

## Sources

- [ROS 2 Jazzy documentation](https://docs.ros.org/en/jazzy/)
- [ros2_control Jazzy controller manager](https://control.ros.org/jazzy/doc/ros2_control/controller_manager/doc/userdoc.html)
- [ros2_control mock components](https://control.ros.org/jazzy/doc/ros2_control/hardware_interface/doc/mock_components_userdoc.html)
- [robot_state_publisher](https://github.com/ros/robot_state_publisher)
- [ROS 2 QoS policies](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)

Clean up from the host after the lab: `docker rm -f training-ros-control`.
