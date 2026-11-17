# 8. ROS 2-robotarkitektur: fem funksjonstrinn

**Språk:** [en](../../en/notes/08-ros2-robot-architecture.md) · [fr](../../fr/notes/08-ros2-robot-architecture.md) · [de](../../de/notes/08-ros2-robot-architecture.md) · [it](../../it/notes/08-ros2-robot-architecture.md) · [es](../../es/notes/08-ros2-robot-architecture.md) · [pt](../../pt/notes/08-ros2-robot-architecture.md) · [zh](../../zh/notes/08-ros2-robot-architecture.md) · [ja](../../ja/notes/08-ros2-robot-architecture.md) · [nb](08-ros2-robot-architecture.md) · [ru](../../ru/notes/08-ros2-robot-architecture.md) · [ko](../../ko/notes/08-ros2-robot-architecture.md) · [fi](../../fi/notes/08-ros2-robot-architecture.md) · [pl](../../pl/notes/08-ros2-robot-architecture.md)

[Grunnleggende ROS 2](06-ros2-foundations.md) · [Laboratorium for virtuelt ledd](07-ros2-control-lab.md) · [Oversikt](../README.md)

> **Kun konseptuelt.** Ingen styring av fysisk utstyr eller sikkerhetsgaranti.

De fem engelske trinnnavnene nedenfor er identiske med navnene i det [felles redigerbare Mermaid-diagrammet](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram). Hvert trinn er en **funksjon, ikke nødvendigvis en egen ROS-node**. Diagrammet er konseptuelt, ikke kjørbar maskinvarekontroll eller en sikkerhetsløsning.

## Fem funksjonstrinn

| Engelsk trinn | Norsk begrep | Ansvar og ROS-komponenter |
| --- | --- | --- |
| **1. Perception** | Persepsjon | Kameradriveren publiserer `sensor_msgs/msg/Image` med opptakstid; en applikasjonsdetektor anslår objektets posisjon i `camera_link`. |
| **2. Coordinate Transformation** | Koordinattransformasjon | Applikasjonen bruker `tf2_ros.Buffer.lookup_transform` til å oversette posisjonen til `base_link` ved opptakstidspunktet. Kamerafestet må finnes i URDF eller statisk TF. |
| **3. Motion Planning** | Bevegelsesplanlegging | En planlegger, for eksempel MoveIt 2, bruker mål, robotmodell og tilstand for å lage en leddbane. |
| **4. Motion Control** | Bevegelseskontroll | En konfigurert `joint_trajectory_controller` mottar `FollowJointTrajectory`, skriver kommandogrensesnitt og sender ønsket bevegelse til servo og motor. |
| **5. Feedback** | Tilbakemelding | Enkoderverdier går både til den lokale servosløyfen og maskinvarens tilstandsgrensesnitt. `joint_state_broadcaster` publiserer `/joint_states`; `robot_state_publisher` lager `/tf` og `/tf_static` fra URDF og leddtilstander. Kontrollere kan lese tilstand direkte. |

## Skille mellom grensesnitt

**Skill mellom flytene:** URDF beskriver roboten og mulige `ros2_control`-grensesnitt, men sender ingen motorkommandoer. TF2 slår opp transformasjoner. Kommando er ønsket verdi, tilstand er måling; tapt `/joint_states` beviser ikke at lokal servostyring stoppet.

**Eksisterende øvelse:** det virtuelle leddet bruker `forward_position_controller` og `mock_components/GenericSystem`, ikke banekontrolleren, kamera, MoveIt 2 eller ekte maskinvare. Helhetsdiagrammet er konseptuelt.

**Senere utvidelser:** feilhåndtering, watchdog, QoS, tidssynkronisering, diagnostikk, sanntid og simulering. Behold de fem engelske trinnnavnene.

## Felles kilde og videre lesning

[Åpne og rediger det felles Mermaid-diagrammet](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) · [ROS 2-referanse](06-ros2-foundations.md) · [Øvelse med simulert kontroller](07-ros2-control-lab.md)
