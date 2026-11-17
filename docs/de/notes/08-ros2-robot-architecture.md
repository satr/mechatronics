# 8. ROS-2-Roboterarchitektur: fünf Stufen

**Sprachen:** [en](../../en/notes/08-ros2-robot-architecture.md) · [fr](../../fr/notes/08-ros2-robot-architecture.md) · [de](08-ros2-robot-architecture.md) · [it](../../it/notes/08-ros2-robot-architecture.md) · [es](../../es/notes/08-ros2-robot-architecture.md) · [pt](../../pt/notes/08-ros2-robot-architecture.md) · [zh](../../zh/notes/08-ros2-robot-architecture.md) · [ja](../../ja/notes/08-ros2-robot-architecture.md) · [nb](../../nb/notes/08-ros2-robot-architecture.md) · [ru](../../ru/notes/08-ros2-robot-architecture.md) · [ko](../../ko/notes/08-ros2-robot-architecture.md) · [fi](../../fi/notes/08-ros2-robot-architecture.md) · [pl](../../pl/notes/08-ros2-robot-architecture.md)

[ROS-2-Grundlagen](06-ros2-foundations.md) · [Virtuelles Gelenklabor](07-ros2-control-lab.md) · [Übersicht](../README.md)

> **Nur konzeptionell.** Keine reale Geräteansteuerung und keine Sicherheitsgarantie.

Die fünf englischen Bezeichnungen stimmen genau mit dem [gemeinsamen editierbaren Mermaid-Diagramm](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) überein. Eine Stufe ist eine **Funktion und nicht zwingend ein einzelner ROS-Knoten**. Das Diagramm ist konzeptionell, keine lauffähige Roboter- oder Sicherheitssteuerung.

## Fünf Funktionsstufen

| Englische Stufe | Deutscher Begriff | Aufgaben und ROS-Komponenten |
| --- | --- | --- |
| **1. Perception** | Wahrnehmung | Ein Kameratreiber liefert `sensor_msgs/msg/Image` samt Aufnahmezeit; ein Anwendungsdetektor schätzt die Objektpose in `camera_link`. |
| **2. Coordinate Transformation** | Koordinatentransformation | Die Anwendung nutzt `tf2_ros.Buffer.lookup_transform`, um die Pose zum Aufnahmezeitpunkt nach `base_link` zu transformieren. Die Kameramontage muss durch URDF oder statische TF-Daten beschrieben sein. |
| **3. Motion Planning** | Bewegungsplanung | Ein Planer, etwa MoveIt 2, erzeugt aus Zielpose, Modell und Roboterzustand eine Gelenktrajektorie. |
| **4. Motion Control** | Bewegungssteuerung | Ein konfigurierter `joint_trajectory_controller` nimmt `FollowJointTrajectory` an, schreibt Kommandoschnittstellen und übergibt Sollwerte an Antrieb und Motor. |
| **5. Feedback** | Rückmeldung | Der Encoder speist die lokale Servoschleife und Hardware-Zustandsschnittstellen. `joint_state_broadcaster` sendet `/joint_states`; `robot_state_publisher` erzeugt mit URDF `/tf` und `/tf_static`. Controller können Zustände direkt lesen. |

## Schnittstellen unterscheiden

**Datenwege unterscheiden:** URDF beschreibt Gelenke und mögliche `ros2_control`-Schnittstellen, bewegt jedoch keinen Motor. TF2 fragt Transformationen ab. Befehle sind Sollwerte, State Interfaces liefern Messwerte; fehlendes `/joint_states` beweist keinen Ausfall der lokalen Servoregelung.

**Bestehendes Labor:** Die virtuelle Achse nutzt `forward_position_controller` und `mock_components/GenericSystem`, nicht den Trajektoriencontroller, eine Kamera oder echte Hardware. Die Gesamtarchitektur bleibt konzeptionell.

**Spätere Erweiterungen:** Fehlerüberwachung, Watchdog, QoS, Zeitsynchronisation, Diagnose, Echtzeit und Simulation. Die fünf Stufennamen beibehalten.

## Gemeinsame Quelle und weitere Informationen

[Gemeinsames Mermaid-Architekturdiagramm öffnen und bearbeiten](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) · [ROS-2-Referenz](06-ros2-foundations.md) · [Übung mit virtuellem Controller](07-ros2-control-lab.md)
