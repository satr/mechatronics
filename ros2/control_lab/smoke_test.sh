#!/usr/bin/env bash
# Trusted-main, single-container ROS Jazzy end-to-end smoke; never run untrusted PR Docker code on host.
set -euo pipefail
cd "$(dirname "$0")/../.."
image="training-ros-control-smoke"
container="training-ros-control-smoke-$$"
cleanup() {
  code=$?
  if (( code != 0 )); then docker logs --tail 100 "$container" 2>/dev/null || true; fi
  docker rm -f "$container" >/dev/null 2>&1 || true
}
trap cleanup EXIT

docker build -t "$image" -f ros2/control_lab/Dockerfile ros2/control_lab
docker run -d --name "$container" -e ROS_DOMAIN_ID=43 "$image" >/dev/null
inside() { docker exec "$container" bash -lc "source /opt/ros/\${ROS_DISTRO}/setup.bash && $1"; }

echo 'Waiting for both active controllers and the claimed position interface...'
ready=0
deadline=$((SECONDS + 90))
while (( SECONDS < deadline )); do
  if controllers="$(inside 'timeout 5s ros2 control list_controllers' 2>/dev/null)" &&
     grep -Eq '^joint_state_broadcaster[[:space:]]+joint_state_broadcaster/JointStateBroadcaster[[:space:]]+active' <<< "$controllers" &&
     grep -Eq '^forward_position_controller[[:space:]]+forward_command_controller/ForwardCommandController[[:space:]]+active' <<< "$controllers"; then
    ready=1
    break
  fi
  sleep 2
done
if (( ready != 1 )); then echo 'Controller activation deadline exceeded' >&2; exit 1; fi
echo "$controllers"

interfaces="$(inside 'timeout 8s ros2 control list_hardware_interfaces')"
grep -Eq 'joint_1/position[[:space:]]+\[available\][[:space:]]+\[claimed\]' <<< "$interfaces"
echo "$interfaces"

inside "timeout 15s ros2 topic pub --once /forward_position_controller/commands std_msgs/msg/Float64MultiArray '{data: [1.0]}'"

echo 'Waiting for feedback = 1.0 rad...'
feedback=0
deadline=$((SECONDS + 30))
while (( SECONDS < deadline )); do
  output="$(inside 'timeout 6s ros2 topic echo --once /joint_states' 2>/dev/null)" || { sleep 1; continue; }
  if printf '%s\n' "$output" | python3 -c '
import re, sys
s=sys.stdin.read()
assert re.search(r"name:\s*\n\s*- joint_1", s)
assert re.search(r"position:\s*\n\s*- 1(?:\.0+)?(?:\s|$)", s)
' >/dev/null 2>&1; then feedback=1; break; fi
  sleep 1
done
if (( feedback != 1 )); then echo 'Expected position state not observed' >&2; exit 1; fi
echo "$output"

# tf2_echo streams until interrupted: timeout code 124 is normal here.
transform="$(inside 'timeout 9s ros2 run tf2_ros tf2_echo base_link tool' 2>&1)" || true
printf '%s\n' "$transform" | python3 -c '
import math, re, sys
s=sys.stdin.read()
matches=re.findall(r"Translation:\s*\[\s*([-+\d.eE]+),\s*([-+\d.eE]+),\s*([-+\d.eE]+)\s*\]",s)
assert matches, "no tf2 translation printed"
xyz=tuple(map(float,matches[-1]))
expected=(0.2*math.cos(1),0.2*math.sin(1),0)
assert all(abs(a-b)<0.005 for a,b in zip(xyz,expected)), (xyz,expected)
'
echo 'PASS: ROS controller claimed position; 1.0 rad feedback; synthetic TF base_link -> tool.'
