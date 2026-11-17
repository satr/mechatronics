# 7. ROS 2 Jazzy bez GUI: wirtualny przegub i TF2

**Languages:** [en](../../en/notes/07-ros2-control-lab.md) · [fr](../../fr/notes/07-ros2-control-lab.md) · [de](../../de/notes/07-ros2-control-lab.md) · [it](../../it/notes/07-ros2-control-lab.md) · [es](../../es/notes/07-ros2-control-lab.md) · [pt](../../pt/notes/07-ros2-control-lab.md) · [zh](../../zh/notes/07-ros2-control-lab.md) · [ja](../../ja/notes/07-ros2-control-lab.md) · [nb](../../nb/notes/07-ros2-control-lab.md) · [ru](../../ru/notes/07-ros2-control-lab.md) · [ko](../../ko/notes/07-ros2-control-lab.md) · [fi](../../fi/notes/07-ros2-control-lab.md) · [pl](../../pl/notes/07-ros2-control-lab.md)

[Wykonywalne laboratorium i diagnostyka](../../../ros2/control_lab/README.md) · [ROS 2](06-ros2-foundations.md) · [pl](../README.md)

> **Simulation-only / mock hardware.** No real actuators.

Osobne laboratorium Docker Ubuntu Noble z ROS 2 Jazzy dla obsługiwanych AMD64 lub ARM64. Bez Gazebo, RViz, pulpitu czy silnika. Dotychczasowy przykład topic/service pozostaje bez zmian.

**Cały system:** [Diagram pięciu etapów i dwujęzyczny słownik](08-ros2-robot-architecture.md) pokazują miejsce laboratorium mock. Kamera, planista, firmware serwa i prawdziwy silnik **nie** działają w tym przykładzie.

## 1. URDF, hardware and state

URDF łączy rodzica `base_link` z `arm_link` przez obrotowy `joint_1` wokół +Z oraz mocuje `tool` przegubem stałym `tool_mount` w odległości +0.2 m wzdłuż X. `mock_components/GenericSystem` oferuje tylko interfejs polecenia i stanu `joint_1/position`. Kontroler wpisuje polecenie, `joint_state_broadcaster` publikuje stan, `robot_state_publisher` oblicza TF2.

[arm.urdf](../../../ros2/control_lab/arm.urdf) · [controllers.yaml](../../../ros2/control_lab/controllers.yaml) · [control.launch.py](../../../ros2/control_lab/control.launch.py) · [Dockerfile](../../../ros2/control_lab/Dockerfile)

[Alternatywa: oficjalny obraz ROS bez Compose i własnego Dockerfile](../../../ros2/PLAIN_DOCKER.md)

## 2. Packages and environment

Oficjalny obraz ROS już ustawia `ROS_DISTRO`; nie nadpisuj tej zmiennej. Dockerfile instaluje kontrolery i automatycznie ładuje ROS w interaktywnym Bash. Polecenia sprawdzają pakiety; poradnik Dockera opisuje instalację ręczną.

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

**Dockerfile tego laboratorium już instaluje wymagane pakiety.** Poniższe polecenia tylko sprawdzają ich obecność; nie instaluj ich ponownie w gotowym kontenerze. Opcjonalną instalację dla osobnego środowiska Jazzy opisano w pełnym poradniku.

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

W poprawnym drzewie TF2 każdy potomek ma jednego rodzica. Transformacja obejmuje przesunięcie i obrót; składamy je wzdłuż `base_link → arm_link → tool`, a w drugą stronę stosujemy odwrotność. Stałe przeguby URDF są na `/tf_static`, obrotowe, przesuwne i ciągłe na `/tf` po otrzymaniu stanów. Surowy `TFMessage` zawiera dane ze znacznikami czasu; `tf2_echo` pyta bufor czasu o obliczony wynik. DDS `transient_local` nie jest trwałym archiwum. Jeśli automatyczny QoS CLI różni się od jawnej durability, sprawdź też `--qos-reliability reliable`.

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

## 5. ARM64 shared-library diagnostics

Na ARM64 `robot_state_publisher` uległ awarii z `pluginlib::LibraryLoadException`: loader nie widział `libsdformat14.so.14`, a `ldd` zgłaszał też `libgz-math7.so.7`. SDFormat już istniał w `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/`, lecz APT nie miał `libsdformat14`. Sprawdź core, `/robot_description`, osobny publisher, `ldd`, ścieżki vendor i `LD_LIBRARY_PATH`. Załaduj ROS i tymczasowo dodaj tylko istniejące katalogi. Nie twórz niezgodnych symlinków ABI ani nie publikuj core. Późniejszy start potwierdzono, ale dokładny sposób naprawy jest nieznany.

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

**Warunkowe przywracanie ścieżki bibliotek (niepotwierdzona trwała naprawa):** wykonaj [kroki tymczasowe](../../../ros2/control_lab/README.md#temporary-recovery-for-a-missing-vendor-library). Najpierw sprawdź `ldd`, załaduj ROS, dodaj tylko istniejące katalogi vendor i sprawdź ponownie w **tej samej powłoce**.

## 6. Limits and verification

`GenericSystem` kopiuje polecenie do stanu bez silnika, enkodera, PID, dynamiki i bezpiecznego zatrzymania. Prawdziwe serwo wymaga pomiaru, napędu, pętli regulacji i ochrony. `ForwardCommandController` nie daje tej gwarancji. Test statyczny nie jest testem ROS w Dockerze.

[Wykonywalne laboratorium i diagnostyka](../../../ros2/control_lab/README.md) · [Official ros2_control](https://control.ros.org/jazzy/) · [ROS QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
