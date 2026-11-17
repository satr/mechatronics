# 7. ROS 2 Jazzy sem GUI: junta virtual e TF2

**Languages:** [en](../../en/notes/07-ros2-control-lab.md) · [fr](../../fr/notes/07-ros2-control-lab.md) · [de](../../de/notes/07-ros2-control-lab.md) · [it](../../it/notes/07-ros2-control-lab.md) · [es](../../es/notes/07-ros2-control-lab.md) · [pt](../../pt/notes/07-ros2-control-lab.md) · [zh](../../zh/notes/07-ros2-control-lab.md) · [ja](../../ja/notes/07-ros2-control-lab.md) · [nb](../../nb/notes/07-ros2-control-lab.md) · [ru](../../ru/notes/07-ros2-control-lab.md) · [ko](../../ko/notes/07-ros2-control-lab.md) · [fi](../../fi/notes/07-ros2-control-lab.md) · [pl](../../pl/notes/07-ros2-control-lab.md)

[Laboratório executável e diagnóstico](../../../ros2/control_lab/README.md) · [ROS 2](06-ros2-foundations.md) · [pt](../README.md)

> **Simulation-only / mock hardware.** No real actuators.

Laboratório Docker Ubuntu Noble com ROS 2 Jazzy para AMD64 ou ARM64 compatíveis. Não precisa de Gazebo, RViz, desktop ou motor. O exemplo topic/service permanece intacto.

**Sistema completo:** o [diagrama de cinco etapas e glossário bilingue](08-ros2-robot-architecture.md) situam este laboratório mock. Aqui **não** se executam câmara, planeador, firmware servo ou equipamento real.

## 1. URDF, hardware and state

O URDF une `base_link` a `arm_link` pela junta rotativa `joint_1` em +Z e fixa `tool` com `tool_mount` a +0.2 m em X. `mock_components/GenericSystem` oferece apenas comando e estado `joint_1/position`. O controlador escreve a referência, `joint_state_broadcaster` publica o estado e `robot_state_publisher` calcula TF2.

[arm.urdf](../../../ros2/control_lab/arm.urdf) · [controllers.yaml](../../../ros2/control_lab/controllers.yaml) · [control.launch.py](../../../ros2/control_lab/control.launch.py) · [Dockerfile](../../../ros2/control_lab/Dockerfile)

[Alternativa: imagem ROS oficial sem Compose ou Dockerfile próprio](../../../ros2/PLAIN_DOCKER.md)

## 2. Packages and environment

A imagem oficial ROS já define `ROS_DISTRO`: não volte a defini-la. O Dockerfile instala os controllers e carrega ROS em Bash interativo. Estes comandos verificam os pacotes; o guia Docker explica a instalação manual.

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

**O Dockerfile do laboratório já instala estes pacotes.** Estes comandos apenas os verificam; não é necessário reinstalá-los no container construído. Para um ambiente Jazzy separado, veja a instalação opcional no guia completo.

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

Uma árvore TF2 válida tem um pai por filho. Transformações combinam translação e rotação; composição em `base_link → arm_link → tool`, inversão no sentido contrário. Juntas fixas vão para `/tf_static`, rotativas, prismáticas e contínuas para `/tf` com estados disponíveis. A mensagem bruta `TFMessage` contém transformações com tempo; `tf2_echo` consulta o buffer temporal e calcula o resultado. DDS `transient_local` não é armazenamento permanente. Se QoS automático e durability explícita diferirem, testar `--qos-reliability reliable`.

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

## 5. ARM64 shared-library diagnostics

Em ARM64, `robot_state_publisher` falhou com `pluginlib::LibraryLoadException`: o loader não encontrou `libsdformat14.so.14` e `ldd` apontou também `libgz-math7.so.7`. SDFormat já estava em `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/` e APT não tinha `libsdformat14`. Examinar core, `/robot_description`, publisher isolado, `ldd`, caminhos vendor e `LD_LIBRARY_PATH`. Carregar ROS e adicionar temporariamente apenas pastas existentes. Nunca symlinks ABI falsos nem upload de core. O arranque posterior foi observado, mas o comando exato não foi comprovado.

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

**Recuperação condicional do caminho de bibliotecas (não é correção permanente confirmada):** siga os [passos temporários](../../../ros2/control_lab/README.md#temporary-recovery-for-a-missing-vendor-library). Confira `ldd`, carregue ROS, adicione só pastas vendor existentes e confira novamente na **mesma shell**.

## 6. Limits and verification

`GenericSystem` espelha referência em estado sem motor, encoder, PID, dinâmica ou paragem segura. Um servo real precisa de medição, driver, malha de controle e proteção. `ForwardCommandController` não garante isso. Teste estático difere de execução real Docker ROS.

[Laboratório executável e diagnóstico](../../../ros2/control_lab/README.md) · [Official ros2_control](https://control.ros.org/jazzy/) · [ROS QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
