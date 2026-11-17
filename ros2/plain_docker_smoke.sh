#!/usr/bin/env bash
# End-to-end checks for the plain official-image ROS tutorial.
# Run only on trusted main: this script accesses the host Docker daemon.
set -euo pipefail
cd "$(dirname "$0")/.."

container=ros
cleanup() {
  code=$?
  if (( code != 0 )); then docker logs --tail 60 "$container" 2>/dev/null || true; fi
  docker rm -f "$container" >/dev/null 2>&1 || true
}
trap cleanup EXIT

docker run -d --name "$container" -e ROS_DOMAIN_ID=42 ros:jazzy-ros-base sleep infinity >/dev/null

# The official image must define ROS_DISTRO; never pass it from the host.
docker exec "$container" bash -c ': "${ROS_DISTRO:?missing ROS_DISTRO from image}"; test -f "/opt/ros/${ROS_DISTRO}/setup.bash"'

# Same package list as the tutorial: no Compose or custom Dockerfile.
docker exec "$container" bash -c '
  set -eu
  apt-get update
  apt-get install -y --no-install-recommends \
    ros-${ROS_DISTRO}-demo-nodes-cpp ros-${ROS_DISTRO}-demo-nodes-py \
    python3-colcon-common-extensions ros-${ROS_DISTRO}-rclpy \
    ros-${ROS_DISTRO}-std-msgs ros-${ROS_DISTRO}-std-srvs \
    ros-${ROS_DISTRO}-ros2launch ros-${ROS_DISTRO}-launch-ros \
    ros-${ROS_DISTRO}-ros2-control ros-${ROS_DISTRO}-ros2-controllers \
    ros-${ROS_DISTRO}-ros2controlcli ros-${ROS_DISTRO}-robot-state-publisher \
    ros-${ROS_DISTRO}-tf2-ros
'

docker exec "$container" bash -c '
  grep -qxF '\''source "/opt/ros/${ROS_DISTRO}/setup.bash"'\'' ~/.bashrc ||
    echo '\''source "/opt/ros/${ROS_DISTRO}/setup.bash"'\'' >> ~/.bashrc
'

# bash -ic loads ~/.bashrc, proving newly opened exec shells need no manual source.
docker exec "$container" bash -ic 'ros2 pkg executables demo_nodes_cpp | grep talker'
docker exec "$container" bash -ic 'ros2 pkg executables demo_nodes_py | grep listener'

# Cross-language communication, both processes inside the same plain container.
docker exec -d "$container" bash -ic 'exec ros2 run demo_nodes_cpp talker'
sleep 3
listener="$(docker exec "$container" bash -ic 'timeout 18s ros2 run demo_nodes_py listener' 2>&1)" || true
printf '%s\n' "$listener"
grep -q 'I heard:' <<< "$listener"

# A stopped container retains APT packages and ~/.bashrc.
docker stop "$container" >/dev/null
docker start "$container" >/dev/null
docker exec "$container" bash -ic 'ros2 pkg executables demo_nodes_py | grep listener'

# Copy/run the real repository mock-controller launch without building a new image.
docker cp ros2/control_lab/. "$container:/opt/control_lab"
docker exec "$container" bash -c 'test -f /opt/control_lab/control.launch.py'
docker exec -d "$container" bash -ic 'exec ros2 launch /opt/control_lab/control.launch.py'

ready=0
deadline=$((SECONDS + 90))
while (( SECONDS < deadline )); do
  if controllers="$(docker exec "$container" bash -ic 'timeout 6s ros2 control list_controllers' 2>/dev/null)" &&
    grep -Eq '^joint_state_broadcaster[[:space:]]+joint_state_broadcaster/JointStateBroadcaster[[:space:]]+active' <<< "$controllers" &&
    grep -Eq '^forward_position_controller[[:space:]]+forward_command_controller/ForwardCommandController[[:space:]]+active' <<< "$controllers"; then
    ready=1
    break
  fi
  sleep 2
done
if (( ready != 1 )); then echo "Plain Docker controller did not activate" >&2; exit 1; fi
echo "$controllers"
echo 'PASS: official ROS image, APT, interactive Bash, C++/Python demos, restart, and copied mock-control launch.'
