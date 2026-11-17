# 7. ROS 2 Jazzy sans GUI : articulation virtuelle et TF2

**Languages:** [en](../../en/notes/07-ros2-control-lab.md) · [fr](../../fr/notes/07-ros2-control-lab.md) · [de](../../de/notes/07-ros2-control-lab.md) · [it](../../it/notes/07-ros2-control-lab.md) · [es](../../es/notes/07-ros2-control-lab.md) · [pt](../../pt/notes/07-ros2-control-lab.md) · [zh](../../zh/notes/07-ros2-control-lab.md) · [ja](../../ja/notes/07-ros2-control-lab.md) · [nb](../../nb/notes/07-ros2-control-lab.md) · [ru](../../ru/notes/07-ros2-control-lab.md) · [ko](../../ko/notes/07-ros2-control-lab.md) · [fi](../../fi/notes/07-ros2-control-lab.md) · [pl](../../pl/notes/07-ros2-control-lab.md)

[Laboratoire exécutable et diagnostic](../../../ros2/control_lab/README.md) · [ROS 2](06-ros2-foundations.md) · [fr](../README.md)

> **Simulation-only / mock hardware.** No real actuators.

Laboratoire Docker Ubuntu Noble avec ROS 2 Jazzy, pour AMD64 et ARM64 compatibles. Sans Gazebo, RViz, interface graphique ou moteur. L'ancien exemple topic/service reste intact.

**Architecture complète :** le [diagramme en cinq étapes et le lexique bilingue](08-ros2-robot-architecture.md) situent ce laboratoire mock. Ici, **ni** caméra, planificateur, firmware servo, ni matériel réel ne fonctionnent.

## 1. URDF, hardware and state

L'URDF relie le parent `base_link` à `arm_link` par `joint_1`, une articulation rotative autour de +Z. Le `tool` est fixé par `tool_mount` à +0.2 m sur X. `mock_components/GenericSystem` expose seulement la commande et l'état `joint_1/position`. Le contrôleur écrit la consigne, `joint_state_broadcaster` publie l'état, `robot_state_publisher` calcule TF2.

[arm.urdf](../../../ros2/control_lab/arm.urdf) · [controllers.yaml](../../../ros2/control_lab/controllers.yaml) · [control.launch.py](../../../ros2/control_lab/control.launch.py) · [Dockerfile](../../../ros2/control_lab/Dockerfile)

[Alternative : image ROS officielle sans Compose ni Dockerfile personnalisé](../../../ros2/PLAIN_DOCKER.md)

## 2. Packages and environment

L'image ROS officielle définit déjà `ROS_DISTRO` : ne le redéfinis pas. Le Dockerfile installe les contrôleurs et charge ROS dans les shells Bash interactifs. Les commandes suivantes vérifient les paquets ; la méthode Docker directe explique l'installation manuelle.

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

**Le Dockerfile du laboratoire installe déjà ces paquets.** Les commandes ci-dessous les vérifient seulement ; ne les réinstalle pas dans le conteneur construit. Pour une installation Jazzy indépendante, consulte les instructions facultatives du guide complet.

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

Chaque enfant d'un arbre TF2 valide a un seul parent. La transformation combine translation et rotation; composition via `base_link → arm_link → tool`, inversion dans l'autre sens. Les liaisons fixes vont sur `/tf_static`, les rotatives, prismatiques et continues sur `/tf` avec leurs états. Un `TFMessage` brut contient des transformations horodatées; `tf2_echo` interroge le buffer temporel et calcule le résultat. La durabilité DDS `transient_local` n'est pas un archivage permanent. Tester aussi `--qos-reliability reliable` si le QoS automatique diffère de l'option explicite.

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

## 5. ARM64 shared-library diagnostics

En ARM64, `robot_state_publisher` a quitté avec `pluginlib::LibraryLoadException` : le chargeur ne voyait pas `libsdformat14.so.14` et `ldd` signalait `libgz-math7.so.7`. SDFormat se trouvait pourtant dans `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/`; APT ne proposait pas `libsdformat14`. Diagnostiquer core, `/robot_description`, publisher isolé, `ldd`, chemins vendor et `LD_LIBRARY_PATH`. Charger ROS et n'ajouter temporairement que les dossiers existants. Ne pas publier de core ni créer de liens ABI incompatibles. Le démarrage ultérieur est confirmé, pas la commande exacte.

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

**Récupération conditionnelle du chemin des bibliothèques (pas une réparation permanente confirmée) :** suis les [étapes de récupération temporaire](../../../ros2/control_lab/README.md#temporary-recovery-for-a-missing-vendor-library). Vérifie `ldd`, charge ROS, ajoute uniquement les dossiers vendor existants et revérifie `ldd` avant de relancer dans **le même shell**.

## 6. Limits and verification

`GenericSystem` reflète la consigne dans l'état : pas de moteur, encodeur, PID, dynamique ni arrêt sécurisé. Un vrai servo nécessite mesure, pilote, boucle de régulation et protections. `ForwardCommandController` ne les garantit pas. Les tests statiques ne sont pas une exécution Docker ROS.

[Laboratoire exécutable et diagnostic](../../../ros2/control_lab/README.md) · [Official ros2_control](https://control.ros.org/jazzy/) · [ROS QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
