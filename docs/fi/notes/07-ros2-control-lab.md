# 7. ROS 2 Jazzy ilman GUI:ta: virtuaalinivel ja TF2

**Languages:** [en](../../en/notes/07-ros2-control-lab.md) · [fr](../../fr/notes/07-ros2-control-lab.md) · [de](../../de/notes/07-ros2-control-lab.md) · [it](../../it/notes/07-ros2-control-lab.md) · [es](../../es/notes/07-ros2-control-lab.md) · [pt](../../pt/notes/07-ros2-control-lab.md) · [zh](../../zh/notes/07-ros2-control-lab.md) · [ja](../../ja/notes/07-ros2-control-lab.md) · [nb](../../nb/notes/07-ros2-control-lab.md) · [ru](../../ru/notes/07-ros2-control-lab.md) · [ko](../../ko/notes/07-ros2-control-lab.md) · [fi](../../fi/notes/07-ros2-control-lab.md) · [pl](../../pl/notes/07-ros2-control-lab.md)

[Suoritettava laboratorio ja vianmääritys](../../../ros2/control_lab/README.md) · [ROS 2](06-ros2-foundations.md) · [fi](../README.md)

> **Simulation-only / mock hardware.** No real actuators.

Erillinen Ubuntu Noble Docker -laboratorio ROS 2 Jazzylla tuetulla AMD64- tai ARM64-alustalla. Ei Gazeboa, RViziä, työpöytää tai moottoria. Nykyinen topic/service-harjoitus säilyy.

**Kokonaisuus:** [Viiden vaiheen kaavio ja kaksikielinen sanasto](08-ros2-robot-architecture.md) sijoittavat mock-harjoituksen laajempaan järjestelmään. Kameraa, suunnittelijaa, servon laiteohjelmistoa tai oikeaa laitteistoa **ei käytetä**.

## 1. URDF, hardware and state

URDF yhdistää vanhemman `base_link` nivelen `joint_1` kautta +Z-akselin ympäri kappaleeseen `arm_link` ja kiinnittää `tool`-kehyksen `tool_mount`-liitoksella +0.2 m X-suunnassa. `mock_components/GenericSystem` tarjoaa vain `joint_1/position`-komento- ja tilarajapinnan. Ohjain kirjoittaa komennon, `joint_state_broadcaster` julkaisee tilan ja `robot_state_publisher` tuottaa TF2-muunnokset.

[arm.urdf](../../../ros2/control_lab/arm.urdf) · [controllers.yaml](../../../ros2/control_lab/controllers.yaml) · [control.launch.py](../../../ros2/control_lab/control.launch.py) · [Dockerfile](../../../ros2/control_lab/Dockerfile)

[Vaihtoehto: virallinen ROS-image ilman Composea tai omaa Dockerfileä](../../../ros2/PLAIN_DOCKER.md)

## 2. Packages and environment

Virallinen ROS-image määrittää jo `ROS_DISTRO`-muuttujan; älä korvaa sitä. Dockerfile asentaa ohjaimet ja lataa ROSin automaattisesti interaktiiviseen Bashiin. Komennot tarkistavat paketit; Docker-opas neuvoo manuaalisen asennuksen.

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

**Harjoituksen Dockerfile asentaa paketit jo valmiiksi.** Seuraavat komennot vain tarkistavat ne, eikä valmiiseen konttiin pidä asentaa niitä uudestaan. Erillisen Jazzy-ympäristön valinnaiset asennusohjeet ovat koko oppaassa.

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

Kelvollisessa TF2-puussa lapsikehyksellä on yksi vanhempi. Muunnos yhdistää siirron ja kierron; ketju on `base_link → arm_link → tool`, vastakkaiseen suuntaan käytetään inverssiä. Kiinteät URDF-nivelet julkaistaan `/tf_static`-aiheessa, kiertyvät, liukuvat ja jatkuvat `/tf`-aiheessa, kun tilat ovat käytettävissä. Raaka `TFMessage` sisältää aikaleimatut tiedot, mutta `tf2_echo` kysyy aikapuskurista lasketun tuloksen. DDS `transient_local` ei ole pysyvä arkisto. Jos CLI:n automaattinen QoS eroaa durability-valinnasta, testaa `--qos-reliability reliable`.

```bash
ros2 topic info /tf_static -v
ros2 topic echo --once /tf_static
ros2 topic echo --once --qos-durability transient_local --qos-reliability reliable /tf_static
ros2 topic info /tf -v
ros2 topic echo --once /tf
```

## 5. ARM64 shared-library diagnostics

ARM64-tilanteessa `robot_state_publisher` kaatui `pluginlib::LibraryLoadException`-virheeseen: lataaja ei löytänyt `libsdformat14.so.14`-kirjastoa, ja `ldd` ilmoitti myös `libgz-math7.so.7`-virheen. SDFormat oli jo hakemistossa `/opt/ros/${ROS_DISTRO}/opt/sdformat_vendor/lib/`, mutta APT ei tarjonnut `libsdformat14`-pakettia. Tutki core, `/robot_description`, erillinen publisher, `ldd`, vendor-polut ja `LD_LIBRARY_PATH`. Source ROS ja lisää vain löytyneet hakemistot tilapäisesti. Älä tee väärän ABI:n symlinkkejä tai julkaise corea. Myöhempi käynnistys onnistui, mutta täsmällinen korjauskomento jäi tuntemattomaksi.

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

**Ehdollinen kirjastopolun palautus (ei vahvistettu pysyvä korjaus):** seuraa [tilapäisiä ohjeita](../../../ros2/control_lab/README.md#temporary-recovery-for-a-missing-vendor-library). Tarkista ensin `ldd`, source ROS, lisää vain olemassa olevat vendor-hakemistot ja tarkista uudelleen **samassa shellissä**.

## 6. Limits and verification

`GenericSystem` kopioi komennon tilaan ilman moottoria, enkooderia, PID:tä, dynamiikkaa tai turvallista pysäytystä. Todellinen servo tarvitsee mittauksen, ajurin, takaisinkytkennän ja suojauksen. `ForwardCommandController` ei takaa tätä. Staattinen testi ja ROS Docker -käyttötesti ovat eri asioita.

[Suoritettava laboratorio ja vianmääritys](../../../ros2/control_lab/README.md) · [Official ros2_control](https://control.ros.org/jazzy/) · [ROS QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)
