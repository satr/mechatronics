# 8. Architettura ROS 2 di un robot: cinque fasi

**Lingue:** [en](../../en/notes/08-ros2-robot-architecture.md) · [fr](../../fr/notes/08-ros2-robot-architecture.md) · [de](../../de/notes/08-ros2-robot-architecture.md) · [it](08-ros2-robot-architecture.md) · [es](../../es/notes/08-ros2-robot-architecture.md) · [pt](../../pt/notes/08-ros2-robot-architecture.md) · [zh](../../zh/notes/08-ros2-robot-architecture.md) · [ja](../../ja/notes/08-ros2-robot-architecture.md) · [nb](../../nb/notes/08-ros2-robot-architecture.md) · [ru](../../ru/notes/08-ros2-robot-architecture.md) · [ko](../../ko/notes/08-ros2-robot-architecture.md) · [fi](../../fi/notes/08-ros2-robot-architecture.md) · [pl](../../pl/notes/08-ros2-robot-architecture.md)

[Fondamenti di ROS 2](06-ros2-foundations.md) · [Laboratorio del giunto virtuale](07-ros2-control-lab.md) · [Indice](../README.md)

> **Solo concettuale.** Nessun controllo di dispositivi reali né garanzia di sicurezza.

I cinque nomi inglesi sono identici alle etichette del [diagramma Mermaid condiviso e modificabile](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram). Una fase è una **funzione, non necessariamente un singolo nodo ROS**. Lo schema è concettuale, non rappresenta un robot operativo o un sistema di sicurezza.

## Cinque fasi funzionali

| Fase in inglese | Termine italiano | Responsabilità e componenti ROS |
| --- | --- | --- |
| **1. Perception** | Percezione | Il driver della camera pubblica `sensor_msgs/msg/Image` e il tempo di acquisizione; un detector applicativo stima la posa in `camera_link`. |
| **2. Coordinate Transformation** | Trasformazione delle coordinate | L'applicazione usa `tf2_ros.Buffer.lookup_transform` per tradurre la posa in `base_link` al momento dell'immagine. Il montaggio della camera deve avere una trasformazione URDF o statica. |
| **3. Motion Planning** | Pianificazione del movimento | Un planner come MoveIt 2 usa obiettivo, modello e stato per produrre una traiettoria dei giunti. |
| **4. Motion Control** | Controllo del movimento | Il `joint_trajectory_controller` configurato accetta `FollowJointTrajectory`, scrive le interfacce di comando e trasmette riferimenti a firmware e motore. |
| **5. Feedback** | Retroazione | L'encoder alimenta il servo locale e le interfacce di stato. `joint_state_broadcaster` pubblica `/joint_states`; `robot_state_publisher` usa URDF e stati per `/tf` e `/tf_static`. Il controller può leggere lo stato direttamente. |

## Distinguere le interfacce

**Distinguere i flussi:** URDF descrive collegamenti, giunti e possibili interfacce `ros2_control`, ma non comanda il motore. TF2 consulta trasformazioni. Un comando è un riferimento, una state interface riporta una misura; l'assenza di `/joint_states` non prova che il servo locale sia fermo.

**Laboratorio esistente:** il giunto virtuale usa `forward_position_controller` e `mock_components/GenericSystem`, non il controller di traiettoria, MoveIt 2 o un motore reale. L'architettura completa è concettuale.

**Estensioni successive:** watchdog, guasti, QoS, sincronizzazione, diagnostica, real-time e simulazione. Conservare i cinque nomi delle fasi.

## Sorgente condivisa e approfondimenti

[Aprire e modificare il diagramma Mermaid comune](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) · [Riferimento ROS 2](06-ros2-foundations.md) · [Esercizio con controllore simulato](07-ros2-control-lab.md)
