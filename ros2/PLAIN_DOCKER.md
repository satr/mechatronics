# ROS 2 in plain Docker — no Compose or custom Dockerfile

An alternative to the prepared labs: use one official ROS Docker image, one persistent container named `ros` and terminal-only commands. **Select a distribution by changing only the official image tag** in the first command. The image already defines `ROS_DISTRO`; do not export it on the host.

**Prerequisites:** Docker Engine or Docker Desktop and network access to the image registry and ROS APT packages. Commands labelled **host** run in the host's terminal; commands labelled **container** run inside the Linux container. No GUI, hardware devices, privileged mode, host networking or private mounts are used. The listed package names are tested for Jazzy, not guaranteed across all ROS releases.

## 1. Create and enter the container (host)

```bash
# To change ROS release, change only the image tag here.
docker run -d --name ros -e ROS_DOMAIN_ID=42 ros:jazzy-ros-base sleep infinity
docker exec -it ros bash
```

The official image provides `ROS_DISTRO` via Docker `ENV`. The separate `ROS_DOMAIN_ID=42` parameter selects a DDS discovery domain; it needs `-e`. The `sleep infinity` process keeps the container running between sessions. `docker exec -it ros` alone is invalid: Docker requires a command such as `bash`. Do not use `--rm` if you want installed packages and files to persist.

## 2. Install the packages and auto-source ROS (container, once)

```bash
: "${ROS_DISTRO:?Official ROS image did not set ROS_DISTRO}"
echo "ROS_DISTRO=$ROS_DISTRO"

apt-get update && apt-get install -y --no-install-recommends \
  ros-${ROS_DISTRO}-demo-nodes-cpp ros-${ROS_DISTRO}-demo-nodes-py \
  python3-colcon-common-extensions ros-${ROS_DISTRO}-rclpy \
  ros-${ROS_DISTRO}-std-msgs ros-${ROS_DISTRO}-std-srvs \
  ros-${ROS_DISTRO}-ros2launch ros-${ROS_DISTRO}-launch-ros \
  ros-${ROS_DISTRO}-ros2-control ros-${ROS_DISTRO}-ros2-controllers \
  ros-${ROS_DISTRO}-ros2controlcli ros-${ROS_DISTRO}-robot-state-publisher \
  ros-${ROS_DISTRO}-tf2-ros

grep -qxF 'source "/opt/ros/${ROS_DISTRO}/setup.bash"' ~/.bashrc ||
  echo 'source "/opt/ros/${ROS_DISTRO}/setup.bash"' >> ~/.bashrc
source ~/.bashrc
ros2 pkg executables demo_nodes_cpp
```

The `~/.bashrc` entry contains **literal** `${ROS_DISTRO}` and is expanded automatically in every **new interactive Bash shell** in this container. A fresh `docker exec` shell does not inherit shell changes made by the container's entrypoint, but it does inherit the image-defined `ROS_DISTRO`. The setup is per user and per container, not a host-wide setting. Noninteractive `bash -c` scripts may need an explicit `source "/opt/ros/${ROS_DISTRO}/setup.bash"`.

## 3. Run nodes in parallel (two host terminals)

**Terminal A — C++ talker:**

```bash
docker exec -it ros bash -ic 'ros2 run demo_nodes_cpp talker'
```

**Terminal B — Python listener:**

```bash
docker exec -it ros bash -ic 'ros2 run demo_nodes_py listener'
```

Both interactive shells load `~/.bashrc` and communicate on `/chatter` within the same container. Stop either node with Ctrl+C. To open another ordinary terminal: `docker exec -it ros bash`.

## 4. Stop and restart (host)

```bash
docker stop ros
docker start ros
docker exec -it ros bash
```

Installed packages, copied files and `~/.bashrc` persist across stop/start. ROS processes launched interactively do not restart automatically. `docker rm ros` would delete the container and its uncommitted filesystem changes.

## 5. Optional: vendor-library loading errors (container)

**Only if a ROS process actually reports a missing shared library.** Actual library sonames depend on the distribution. Inspect a plugin if present and locate its shared libraries:

```bash
plugin="/opt/ros/${ROS_DISTRO}/lib/libsdformat_urdf_plugin.so"
[ ! -f "$plugin" ] || ldd "$plugin" | grep 'not found' || true
find "/opt/ros/${ROS_DISTRO}/opt" \( -name 'libsdformat*.so*' -o -name 'libgz-math*.so*' \)
```

If unresolved libraries exist in the ROS vendor prefix, conditionally make their directories visible in each **new interactive Bash session**:

```bash
grep -qF '# Optional ROS vendor library paths' ~/.bashrc || cat >> ~/.bashrc <<'EOF'
# Optional ROS vendor library paths
for vendor in sdformat_vendor gz_math_vendor gz_utils_vendor; do
  d="/opt/ros/${ROS_DISTRO}/opt/$vendor/lib"
  if [ -d "$d" ]; then export LD_LIBRARY_PATH="$d${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"; fi
done
EOF
source ~/.bashrc
[ ! -f "$plugin" ] || ldd "$plugin" | grep 'not found' || true
```

Do not change the loader path unless the files actually exist. If unresolved dependencies remain, inspect ROS vendor environment hooks instead of guessing a package or creating incompatible ABI symlinks. Retry the failed process in **this shell**, not a process started before the environment change. This is a conditional workaround, **not** a verified universal fix. A past ARM64 Jazzy run had `libsdformat14.so.14` on disk but unavailable to the dynamic linker; the exact repair command was not recorded. [Full investigation](control_lab/README.md#5-arm64-loader-failure-inspect-recover-the-search-path-verify).

## 6. Optional: run this repository's labs without a custom image

**Host, from the cloned repository root:** copy the standalone headless joint lab and enter the existing container:

```bash
docker cp ros2/control_lab/. ros:/opt/control_lab
docker exec -it ros bash
```

**Inside the container:**

```bash
ros2 launch /opt/control_lab/control.launch.py
```

Use a second host terminal with `docker exec -it ros bash` to run `ros2 control list_controllers`, publish the mock position command, and inspect TF2 as explained in the [virtual-joint lab](control_lab/README.md). Do not start duplicate copies of the same nodes in one ROS domain.

For the repository's custom Python package, **host, from the repository root**:

```bash
docker exec ros mkdir -p /opt/training_ws/src
docker cp ros2/demo_pkg ros:/opt/training_ws/src/telemetry_demo
docker exec -it ros bash
```

Then **inside the container**:

```bash
cd /opt/training_ws && colcon build --packages-select telemetry_demo
source /opt/training_ws/install/setup.bash
ros2 launch telemetry_demo demo.launch.py
```

A custom workspace overlay must be sourced **after it has been built**, in addition to the base ROS setup. You may add the overlay's literal setup line below the base line in `~/.bashrc` for subsequent interactive shells. The plain container stores mutable packages and files; it is not a byte-for-byte reproducible image.

For automated reproducibility, the repository also provides the [Compose telemetry demo](README.md) and the [prepared headless ros2_control image](control_lab/README.md). These examples are synthetic and do not control real hardware.

## Primary references

- [Official ROS image and tags](https://hub.docker.com/_/ros)
- [Docker exec](https://docs.docker.com/reference/cli/docker/container/exec/)
- [ROS 2 documentation](https://docs.ros.org/)
- [ros2_control installation](https://control.ros.org/jazzy/doc/getting_started/getting_started.html)
