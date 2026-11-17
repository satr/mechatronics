# 7. ROS 2 Jazzy sin GUI: articulación virtual y TF2

**Languages:** [en](../../en/notes/07-ros2-control-lab.md) · [fr](../../fr/notes/07-ros2-control-lab.md) · [de](../../de/notes/07-ros2-control-lab.md) · [it](../../it/notes/07-ros2-control-lab.md) · [es](../../es/notes/07-ros2-control-lab.md) · [pt](../../pt/notes/07-ros2-control-lab.md) · [zh](../../zh/notes/07-ros2-control-lab.md) · [ja](../../ja/notes/07-ros2-control-lab.md) · [nb](../../nb/notes/07-ros2-control-lab.md) · [ru](../../ru/notes/07-ros2-control-lab.md) · [ko](../../ko/notes/07-ros2-control-lab.md) · [fi](../../fi/notes/07-ros2-control-lab.md) · [pl](../../pl/notes/07-ros2-control-lab.md)

[Laboratorio ejecutable y diagnóstico](../../../ros2/control_lab/README.md) · [ROS 2](06-ros2-foundations.md) · [es](../README.md)

> **Simulation-only / mock hardware.** No real actuators.

Laboratorio Docker Ubuntu Noble con ROS 2 Jazzy para AMD64 o ARM64 compatibles. Sin Gazebo, RViz, escritorio ni motor. Se conserva el ejemplo topic/service.

**Sistema completo:** el [diagrama de cinco etapas y glosario bilingüe](08-ros2-robot-architecture.md) sitúa este laboratorio simulado. Aquí **no** funcionan cámara, planificador, firmware servo ni hardware real.

## 1. URDF, hardware and state

El URDF une el padre `base_link` con `arm_link` mediante el giro `joint_1` alrededor de +Z; `tool_mount` fija `tool` a +0.2 m en X. `mock_components/GenericSystem` solo proporciona comando y estado `joint_1/position`. El controlador escribe la consigna, `joint_state_broadcaster` publica el estado y `robot_state_publisher` calcula TF2.

[arm.urdf](../../../ros2/control_lab/arm.urdf) · [controllers.yaml](../../../ros2/control_lab/controllers.yaml) · [control.launch.py](../../../ros2/control_lab/control.launch.py) · [Dockerfile](../../../ros2/control_lab/Dockerfile)

[Alternativa: imagen ROS oficial sin Compose ni Dockerfile propio](../../../ros2/PLAIN_DOCKER.md)

## 2. Packages and environment

La imagen ROS oficial ya define `ROS_DISTRO`: no la cambies en el host o en el contenedor. El Dockerfile instala los controladores y carga ROS en Bash interactivo. Estos comandos comprueban los paquetes; la guía Docker explica la instalación manual.

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

**El Dockerfile del laboratorio ya instala estos paquetes.** Estos comandos solo los comprueban; no hay que reinstalarlos en el contenedor construido. Para un entorno Jazzy aparte consulta la instalación opcional de la guía completa.

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

En un árbol TF2 válido cada hijo tiene un padre. Una transformación combina traslación y rotación; la composición sigue `base_link → arm_link → tool`, la consulta inversa recorre el sentido contrario. Las uniones fijas se publican en `/tf_static`, las giratorias, prismáticas y continuas en `/tf` cuando hay estados. El `TFMessage` bruto contiene transformaciones con marca de tiempo; `tf2_echo` consulta el búfer temporal y calcula el resultado. DDS `transient_local` no es archivo permanente. Si el QoS automático y el flag de durabilidad difieren, probar también `--qos-reliability reliable`.

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

## 5. ARM64 shared-library diagnostics

En ARM64 `robot_state_publisher` falló con `pluginlib::LibraryLoadException`: no se resolvía `libsdformat14.so.14`, y `ldd` mostraba `libgz-math7.so.7`. SDFormat ya estaba en `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/`, pero APT no ofrecía `libsdformat14`. Revisar core, `/robot_description`, publisher aislado, `ldd`, rutas vendor y `LD_LIBRARY_PATH`. Cargar ROS y añadir temporalmente solo directorios existentes. Nunca falsos enlaces ABI ni subir dumps. Se observó el arranque posterior, no el comando exacto que corrigió el problema.

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

**Recuperación condicional de rutas de bibliotecas (no es una solución permanente confirmada):** sigue los [pasos temporales](../../../ros2/control_lab/README.md#temporary-recovery-for-a-missing-vendor-library). Comprueba `ldd`, carga ROS, añade solo carpetas vendor existentes, vuelve a comprobar y reinicia en **la misma shell**.

## 6. Limits and verification

`GenericSystem` refleja el comando en el estado sin motor, encoder, PID, dinámica ni parada segura. Un servo real requiere medición, driver, lazo de control y protección. `ForwardCommandController` no lo garantiza. Las pruebas estáticas no sustituyen Docker ROS real.

[Laboratorio ejecutable y diagnóstico](../../../ros2/control_lab/README.md) · [Official ros2_control](https://control.ros.org/jazzy/) · [ROS QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
