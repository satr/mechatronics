# 7. ROS 2 Jazzy ohne GUI: virtuelles Gelenk und TF2

**Languages:** [en](../../en/notes/07-ros2-control-lab.md) · [fr](../../fr/notes/07-ros2-control-lab.md) · [de](../../de/notes/07-ros2-control-lab.md) · [it](../../it/notes/07-ros2-control-lab.md) · [es](../../es/notes/07-ros2-control-lab.md) · [pt](../../pt/notes/07-ros2-control-lab.md) · [zh](../../zh/notes/07-ros2-control-lab.md) · [ja](../../ja/notes/07-ros2-control-lab.md) · [nb](../../nb/notes/07-ros2-control-lab.md) · [ru](../../ru/notes/07-ros2-control-lab.md) · [ko](../../ko/notes/07-ros2-control-lab.md) · [fi](../../fi/notes/07-ros2-control-lab.md) · [pl](../../pl/notes/07-ros2-control-lab.md)

[Ausführbares Labor mit Fehlersuche](../../../ros2/control_lab/README.md) · [ROS 2](06-ros2-foundations.md) · [de](../README.md)

> **Simulation-only / mock hardware.** No real actuators.

Eigenständiges Ubuntu-Noble-Docker-Labor mit ROS 2 Jazzy für unterstütztes AMD64 und ARM64. Ohne Gazebo, RViz, Desktop oder Motor. Das Topic/Service-Beispiel bleibt unverändert.

**Gesamtsystem:** Das [Fünf-Stufen-Diagramm mit zweisprachigem Glossar](08-ros2-robot-architecture.md) ordnet das Mock-Labor ein. Kamera, Planer, Servofirmware und echte Hardware laufen hier **nicht**.

## 1. URDF, hardware and state

URDF verbindet den Eltern-Frame `base_link` über das Drehgelenk `joint_1` um +Z mit `arm_link`; `tool_mount` befestigt `tool` bei +0.2 m auf X. `mock_components/GenericSystem` bietet nur Befehls- und Zustandsinterface `joint_1/position`. Der Controller sendet den Sollwert, `joint_state_broadcaster` publiziert Zustand, `robot_state_publisher` erzeugt TF2.

[arm.urdf](../../../ros2/control_lab/arm.urdf) · [controllers.yaml](../../../ros2/control_lab/controllers.yaml) · [control.launch.py](../../../ros2/control_lab/control.launch.py) · [Dockerfile](../../../ros2/control_lab/Dockerfile)

[Alternative: offizielles ROS-Image ohne Compose oder eigenes Dockerfile](../../../ros2/PLAIN_DOCKER.md)

## 2. Packages and environment

Das offizielle ROS-Image definiert `ROS_DISTRO` bereits: nicht erneut setzen. Das Dockerfile installiert die Controller und lädt ROS in interaktiven Bash-Shells automatisch. Die Befehle prüfen die Pakete; die direkte Docker-Anleitung erklärt die manuelle Installation.

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

**Das Labor-Dockerfile installiert diese Pakete bereits.** Die Befehle prüfen sie nur; im fertig gebauten Container ist keine Neuinstallation nötig. Die optionale Installation in einer eigenständigen Jazzy-Umgebung steht im vollständigen Laborhandbuch.

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

Jedes Kind hat in einem gültigen TF2-Baum genau einen Eltern-Frame. Transformationen bestehen aus Translation und Rotation; Verkettung über `base_link → arm_link → tool`, inverse Abfrage in Gegenrichtung. Feste URDF-Gelenke erscheinen auf `/tf_static`, drehbare, verschiebbare und kontinuierliche auf `/tf` mit Joint States. Das rohe `TFMessage` enthält zeitgestempelte Einträge, `tf2_echo` fragt den Zeitpuffer nach einem berechneten Ergebnis. DDS `transient_local` ist kein dauerhaftes Archiv. Bei abweichendem CLI-QoS auch `--qos-reliability reliable` testen.

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

## 5. ARM64 shared-library diagnostics

Auf ARM64 stürzte `robot_state_publisher` mit `pluginlib::LibraryLoadException` ab: Der Loader fand `libsdformat14.so.14` nicht, `ldd` meldete auch `libgz-math7.so.7`. SDFormat lag bereits unter `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/`, APT bot kein `libsdformat14`. Core, `/robot_description`, isolierten Publisher, `ldd`, Vendor-Pfade und `LD_LIBRARY_PATH` prüfen. ROS laden und nur existierende Verzeichnisse vorübergehend ergänzen. Keine falschen ABI-Symlinks oder Core-Uploads. Der spätere Start wurde beobachtet, nicht der genaue Reparaturbefehl.

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

**Bedingte Reparatur des Bibliothekssuchpfads (keine bestätigte dauerhafte Lösung):** siehe die [temporären Schritte](../../../ros2/control_lab/README.md#temporary-recovery-for-a-missing-vendor-library). Erst `ldd` prüfen, ROS laden, nur vorhandene Vendor-Verzeichnisse voranstellen und `ldd` erneut in **derselben Shell** kontrollieren.

## 6. Limits and verification

`GenericSystem` kopiert Sollwert in Zustand ohne Motor, Encoder, PID, Dynamik oder sichere Abschaltung. Ein echter Servo braucht Messung, Treiber, Regelschleife und Schutz. `ForwardCommandController` garantiert das nicht. Statische Prüfungen sind kein echter ROS-Docker-Lauf.

[Ausführbares Labor mit Fehlersuche](../../../ros2/control_lab/README.md) · [Official ros2_control](https://control.ros.org/jazzy/) · [ROS QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
