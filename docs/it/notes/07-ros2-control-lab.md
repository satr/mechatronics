# 7. ROS 2 Jazzy senza GUI: giunto virtuale e TF2

**Languages:** [en](../../en/notes/07-ros2-control-lab.md) · [fr](../../fr/notes/07-ros2-control-lab.md) · [de](../../de/notes/07-ros2-control-lab.md) · [it](../../it/notes/07-ros2-control-lab.md) · [es](../../es/notes/07-ros2-control-lab.md) · [pt](../../pt/notes/07-ros2-control-lab.md) · [zh](../../zh/notes/07-ros2-control-lab.md) · [ja](../../ja/notes/07-ros2-control-lab.md) · [nb](../../nb/notes/07-ros2-control-lab.md) · [ru](../../ru/notes/07-ros2-control-lab.md) · [ko](../../ko/notes/07-ros2-control-lab.md) · [fi](../../fi/notes/07-ros2-control-lab.md) · [pl](../../pl/notes/07-ros2-control-lab.md)

[Laboratorio eseguibile e diagnosi](../../../ros2/control_lab/README.md) · [ROS 2](06-ros2-foundations.md) · [it](../README.md)

> **Simulation-only / mock hardware.** No real actuators.

Laboratorio Docker Ubuntu Noble con ROS 2 Jazzy per AMD64 o ARM64 supportati. Nessun Gazebo, RViz, desktop o motore. L'esempio topic/service rimane invariato.

**Sistema completo:** il [diagramma in cinque fasi con glossario bilingue](08-ros2-robot-architecture.md) colloca il laboratorio mock. Qui **non** vengono eseguiti camera, planner, firmware servo o hardware reale.

## 1. URDF, hardware and state

L'URDF collega il padre `base_link` a `arm_link` con `joint_1` rotativo attorno a +Z; `tool_mount` fissa `tool` a +0.2 m su X. `mock_components/GenericSystem` offre solo comando e stato `joint_1/position`. Il controller invia il riferimento, `joint_state_broadcaster` pubblica lo stato, `robot_state_publisher` costruisce TF2.

[arm.urdf](../../../ros2/control_lab/arm.urdf) · [controllers.yaml](../../../ros2/control_lab/controllers.yaml) · [control.launch.py](../../../ros2/control_lab/control.launch.py) · [Dockerfile](../../../ros2/control_lab/Dockerfile)

[Alternativa: immagine ROS ufficiale senza Compose o Dockerfile personalizzato](../../../ros2/PLAIN_DOCKER.md)

## 2. Packages and environment

L'immagine ROS ufficiale definisce già `ROS_DISTRO`: non reimpostarlo. Il Dockerfile installa i controller e carica ROS nelle shell Bash interattive. Le istruzioni seguenti controllano i pacchetti; la guida Docker spiega l'installazione manuale.

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

**Il Dockerfile del laboratorio installa già questi pacchetti.** I comandi seguenti servono solo a verificarli, non a reinstallarli nel container costruito. Per un ambiente Jazzy separato consulta la procedura opzionale nella guida completa.

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

In un albero TF2 valido ogni figlio ha un solo padre. Le trasformazioni combinano traslazione e rotazione: composizione lungo `base_link → arm_link → tool`, inversione nel verso opposto. Giunti fissi su `/tf_static`, rotativi, prismatici e continui su `/tf` quando disponibili gli stati. Il `TFMessage` grezzo contiene dati temporizzati; `tf2_echo` interroga il buffer e calcola il risultato. DDS `transient_local` non equivale a memoria permanente. Se il QoS automatico differisce dal flag di durabilità, provare anche `--qos-reliability reliable`.

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

## 5. ARM64 shared-library diagnostics

Su ARM64 `robot_state_publisher` è terminato con `pluginlib::LibraryLoadException`: il loader non risolveva `libsdformat14.so.14`, e `ldd` anche `libgz-math7.so.7`. SDFormat esisteva già in `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/` e APT non offriva `libsdformat14`. Esaminare core, `/robot_description`, publisher isolato, `ldd`, percorsi vendor e `LD_LIBRARY_PATH`. Caricare ROS e aggiungere temporaneamente solo directory presenti. Niente collegamenti ABI falsi o caricamenti di core. Avvio successivo confermato, comando di riparazione esatto ignoto.

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

**Ripristino condizionale dei percorsi libreria (non una soluzione permanente confermata):** segui la [procedura temporanea](../../../ros2/control_lab/README.md#temporary-recovery-for-a-missing-vendor-library). Controlla `ldd`, carica ROS, aggiungi solo directory vendor presenti, ricontrolla `ldd` e riavvia nella **stessa shell**.

## 6. Limits and verification

`GenericSystem` copia il comando nello stato senza motore, encoder, PID, dinamica o arresto sicuro. Un servo reale richiede sensore, driver, controllo retroazionato e protezioni. `ForwardCommandController` da solo non li garantisce. I test statici non sono test Docker ROS dal vivo.

[Laboratorio eseguibile e diagnosi](../../../ros2/control_lab/README.md) · [Official ros2_control](https://control.ros.org/jazzy/) · [ROS QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
