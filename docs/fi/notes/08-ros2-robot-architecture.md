# 8. ROS 2 -robottiarkkitehtuuri: viisi toiminnallista vaihetta

**Kielet:** [en](../../en/notes/08-ros2-robot-architecture.md) · [fr](../../fr/notes/08-ros2-robot-architecture.md) · [de](../../de/notes/08-ros2-robot-architecture.md) · [it](../../it/notes/08-ros2-robot-architecture.md) · [es](../../es/notes/08-ros2-robot-architecture.md) · [pt](../../pt/notes/08-ros2-robot-architecture.md) · [zh](../../zh/notes/08-ros2-robot-architecture.md) · [ja](../../ja/notes/08-ros2-robot-architecture.md) · [nb](../../nb/notes/08-ros2-robot-architecture.md) · [ru](../../ru/notes/08-ros2-robot-architecture.md) · [ko](../../ko/notes/08-ros2-robot-architecture.md) · [fi](08-ros2-robot-architecture.md) · [pl](../../pl/notes/08-ros2-robot-architecture.md)

[ROS 2:n perusteet](06-ros2-foundations.md) · [Virtuaalinivelen harjoitus](07-ros2-control-lab.md) · [Sisällys](../README.md)

> **Vain käsitteellinen kuvaus.** Ei oikean laitteen ohjausta eikä turvallisuustakuuta.

Viisi englanninkielistä vaihenimeä ovat täsmälleen samat kuin [yhteisessä muokattavassa Mermaid-kaaviossa](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram). Vaihe on **toiminto, ei välttämättä yksittäinen ROS-solmu**. Kaavio on käsitteellinen, ei valmiin robotin ohjaus- tai turvajärjestelmä.

## Viisi toiminnallista vaihetta

| Englanninkielinen vaihe | Suomennos | Tehtävät ja ROS-komponentit |
| --- | --- | --- |
| **1. Perception** | Havainnointi | Kamera-ajuri julkaisee kuvaushetken sisältävän `sensor_msgs/msg/Image`-viestin; sovelluksen tunnistin arvioi kohteen sijainnin `camera_link`-koordinaatistossa. |
| **2. Coordinate Transformation** | Koordinaattimuunnos | Sovellus käyttää `tf2_ros.Buffer.lookup_transform`-kyselyä ja muuntaa kohteen sijainnin kuvaushetkellä `base_link`-koordinaatistoon. Kameran kiinnitys tarvitsee URDF:n tai staattisen TF:n. |
| **3. Motion Planning** | Liikkeen suunnittelu | MoveIt 2:n kaltainen suunnittelija muodostaa tavoitteen, mallin ja tilan perusteella niveltrajektorin. |
| **4. Motion Control** | Liikkeen ohjaus | Konfiguroitu `joint_trajectory_controller` vastaanottaa `FollowJointTrajectory`-toiminnon, kirjoittaa komentoarvot laiterajapintoihin ja välittää tavoitteet servolle ja moottorille. |
| **5. Feedback** | Takaisinkytkentä | Enkooderi syöttää paikallista servosilmukkaa ja laitteiston tilarajapintoja. `joint_state_broadcaster` julkaisee `/joint_states`; `robot_state_publisher` muodostaa URDF:n ja tilan avulla `/tf`- ja `/tf_static`-viestit. Ohjain voi lukea tilan suoraan. |

## Rajapintojen erottaminen

**Erota tietovirrat:** URDF kuvaa rakenteen ja mahdolliset `ros2_control`-rajapinnat, mutta ei ohjaa moottoria. TF2 hakee muunnoksia. Komento on tavoite, tila on mittaus; `/joint_states`-viestin puuttuminen ei todista paikallisen servon pysähtyneen.

**Olemassa oleva harjoitus:** virtuaalinivel käyttää `forward_position_controller`- ja `mock_components/GenericSystem`-komponentteja eikä oikeaa trajektoriohjainta, kameraa, MoveIt 2:ta tai moottoria. Laajempi kaavio on käsitteellinen.

**Myöhemmät laajennukset:** watchdog, häiriöt, QoS, aikaleimat, diagnostiikka, reaaliaikaisuus ja simulointi. Säilytä viisi englanninkielistä vaihenimeä.

## Yhteinen lähde ja lisälukemista

[Avaa ja muokkaa yhteistä Mermaid-arkkitehtuurikaaviota](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) · [ROS 2 -viite](06-ros2-foundations.md) · [Simuloidun ohjaimen harjoitus](07-ros2-control-lab.md)
