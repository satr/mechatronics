#!/usr/bin/env bash
# Run from any directory on a host with Docker Compose v2.
# This exercises the real ROS 2 graph inside one container; it never accesses hardware.
set -euo pipefail
cd "$(dirname "$0")"
docker compose up --build -d
ros='source /opt/ros/${ROS_DISTRO}/setup.bash && source /opt/training_ws/install/setup.bash && '
inside() { docker compose exec -T demo bash -lc "${ros}$1"; }

echo "Waiting approximately 60 s for both nodes and the service..."
# Each discovery command has its own limit: a hanging ros2 CLI call must not
# defeat the overall startup deadline. One final probe may overrun slightly.
deadline=$((SECONDS + 60))
ready=0
while (( SECONDS < deadline )); do
  if nodes="$(inside 'timeout 4s ros2 node list' 2>/dev/null)" &&
     grep -qx '/sample_source' <<< "$nodes" &&
     grep -qx '/sample_monitor' <<< "$nodes" &&
     inside 'timeout 4s ros2 service list' 2>/dev/null | grep -qx '/training/count'; then
    ready=1
    break
  fi
  if (( SECONDS < deadline )); then sleep 1; fi
done
if (( ready == 0 )); then
  echo "ROS graph not ready after startup deadline; inspect: docker compose logs demo" >&2
  exit 1
fi

echo "Checking typed topic..."
inside 'ros2 topic list -t' | grep -Fx '/training/status [std_msgs/msg/String]'
echo "Checking a real topic sample..."
sample="$(inside 'timeout 12s ros2 topic echo --once /training/status')"
grep -Eq 'data: .?sample [0-9]+' <<< "$sample" || {
  printf 'Unexpected topic output: %s\n' "$sample" >&2
  exit 1
}
echo "$sample"

echo "Calling the real Trigger service..."
response="$(inside 'timeout 12s ros2 service call /training/count std_srvs/srv/Trigger "{}"')"
grep -Eq 'success=(True|true)' <<< "$response" || {
  printf 'Unexpected service response: %s\n' "$response" >&2
  exit 1
}
grep -Eq 'received [1-9][0-9]* samples' <<< "$response" || {
  printf 'Unexpected count response: %s\n' "$response" >&2
  exit 1
}
echo "$response"
echo "PASS: live ROS 2 graph, typed topic and service responded inside Docker."
echo "The container remains running. Stop it with: cd ros2 && docker compose down"
