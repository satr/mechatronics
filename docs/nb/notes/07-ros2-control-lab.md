# 7. ROS 2 Jazzy uten GUI: virtuelt ledd og TF2

**Languages:** [en](../../en/notes/07-ros2-control-lab.md) · [fr](../../fr/notes/07-ros2-control-lab.md) · [de](../../de/notes/07-ros2-control-lab.md) · [it](../../it/notes/07-ros2-control-lab.md) · [es](../../es/notes/07-ros2-control-lab.md) · [pt](../../pt/notes/07-ros2-control-lab.md) · [zh](../../zh/notes/07-ros2-control-lab.md) · [ja](../../ja/notes/07-ros2-control-lab.md) · [nb](../../nb/notes/07-ros2-control-lab.md) · [ru](../../ru/notes/07-ros2-control-lab.md) · [ko](../../ko/notes/07-ros2-control-lab.md) · [fi](../../fi/notes/07-ros2-control-lab.md) · [pl](../../pl/notes/07-ros2-control-lab.md)

[Kjørbart laboratorium og feilsøking](../../../ros2/control_lab/README.md) · [ROS 2](06-ros2-foundations.md) · [nb](../README.md)

> **Simulation-only / mock hardware.** No real actuators.

Eget Ubuntu Noble Docker-laboratorium med ROS 2 Jazzy på støttet AMD64 eller ARM64. Ingen Gazebo, RViz, skrivebord eller motor. Eksisterende topic/service-eksempel beholdes.

**Hele systemet:** [Femtrinnsdiagrammet med tospråklig ordliste](08-ros2-robot-architecture.md) setter mock-laboratoriet i sammenheng. Kamera, planlegger, servofirmware og ekte maskinvare kjøres **ikke**.

## 1. URDF, hardware and state

URDF kobler forelder `base_link` via rotasjonsleddet `joint_1` rundt +Z til `arm_link`, og fester `tool` med `tool_mount` +0.2 m langs X. `mock_components/GenericSystem` tilbyr bare kommando og tilstand `joint_1/position`. Kontrolleren skriver kommandoen, `joint_state_broadcaster` publiserer tilstanden og `robot_state_publisher` beregner TF2.

[arm.urdf](../../../ros2/control_lab/arm.urdf) · [controllers.yaml](../../../ros2/control_lab/controllers.yaml) · [control.launch.py](../../../ros2/control_lab/control.launch.py) · [Dockerfile](../../../ros2/control_lab/Dockerfile)

[Alternativ: offisielt ROS-image uten Compose eller egen Dockerfile](../../../ros2/PLAIN_DOCKER.md)

## 2. Packages and environment

Det offisielle ROS-imaget definerer allerede `ROS_DISTRO`; ikke overstyr den. Dockerfilen installerer kontrollerne og laster ROS i interaktiv Bash. Kommandoene kontrollerer pakkene; Docker-guiden forklarer manuell installasjon.

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

**Laboratoriets Dockerfile installerer allerede pakkene.** Kommandoene under kontrollerer dem bare; ikke installer dem på nytt i den ferdigbygde containeren. Se den valgfrie installasjonen i hovedveiledningen for et annet Jazzy-miljø.

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

I et gyldig TF2-tre har hvert barn én forelder. Transformasjoner kombinerer translasjon og rotasjon; sammensetning langs `base_link → arm_link → tool`, inversen i motsatt retning. Faste URDF-ledd går på `/tf_static`, dreie-, skyve- og kontinuerlige ledd på `/tf` når tilstanden finnes. Rå `TFMessage` inneholder tidsstempler; `tf2_echo` spør en tidsbuffer og beregner resultatet. DDS `transient_local` er ikke permanent lagring. Hvis automatisk QoS avviker fra eksplisitt durability, prøv også `--qos-reliability reliable`.

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

## 5. ARM64 shared-library diagnostics

På ARM64 krasjet `robot_state_publisher` med `pluginlib::LibraryLoadException`: loaderen fant ikke `libsdformat14.so.14`; `ldd` meldte også `libgz-math7.so.7`. SDFormat lå allerede i `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/`, mens APT manglet `libsdformat14`. Undersøk core, `/robot_description`, isolert publisher, `ldd`, vendor-stier og `LD_LIBRARY_PATH`. Source ROS og legg bare til bekreftede mapper midlertidig. Ingen ABI-feile symlenker eller core-opplasting. Oppstart lyktes senere, men eksakt reparasjonskommando er ukjent.

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

**Betinget gjenoppretting av biblioteksøkesti (ikke bekreftet varig reparasjon):** følg [midlertidig fremgangsmåte](../../../ros2/control_lab/README.md#temporary-recovery-for-a-missing-vendor-library). Sjekk `ldd`, source ROS, legg bare til eksisterende vendor-mapper og kjør `ldd` igjen i **samme skall**.

## 6. Limits and verification

`GenericSystem` speiler kommando til tilstand uten motor, enkoder, PID, dynamikk eller sikker stopp. Reell servo trenger måling, driver, tilbakemeldingssløyfe og beskyttelse. `ForwardCommandController` garanterer ikke dette. Statiske tester er ikke en ekte Docker ROS-kjøring.

[Kjørbart laboratorium og feilsøking](../../../ros2/control_lab/README.md) · [Official ros2_control](https://control.ros.org/jazzy/) · [ROS QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
