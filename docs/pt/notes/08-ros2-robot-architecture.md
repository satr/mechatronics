# 8. Arquitetura ROS 2 de um robô: cinco etapas

**Idiomas:** [en](../../en/notes/08-ros2-robot-architecture.md) · [fr](../../fr/notes/08-ros2-robot-architecture.md) · [de](../../de/notes/08-ros2-robot-architecture.md) · [it](../../it/notes/08-ros2-robot-architecture.md) · [es](../../es/notes/08-ros2-robot-architecture.md) · [pt](08-ros2-robot-architecture.md) · [zh](../../zh/notes/08-ros2-robot-architecture.md) · [ja](../../ja/notes/08-ros2-robot-architecture.md) · [nb](../../nb/notes/08-ros2-robot-architecture.md) · [ru](../../ru/notes/08-ros2-robot-architecture.md) · [ko](../../ko/notes/08-ros2-robot-architecture.md) · [fi](../../fi/notes/08-ros2-robot-architecture.md) · [pl](../../pl/notes/08-ros2-robot-architecture.md)

[Fundamentos de ROS 2](06-ros2-foundations.md) · [Laboratório de junta virtual](07-ros2-control-lab.md) · [Índice](../README.md)

> **Apenas conceptual.** Não controla equipamento real nem garante segurança.

Os cinco nomes ingleses são idênticos aos do [diagrama Mermaid partilhado e editável](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram). Cada etapa é uma **função, não necessariamente um nó ROS**. É uma arquitetura conceptual, não um robô executável nem um sistema de segurança.

## Cinco etapas funcionais

| Etapa em inglês | Termo português | Responsabilidades e componentes ROS |
| --- | --- | --- |
| **1. Perception** | Perceção | O driver da câmara publica `sensor_msgs/msg/Image` com hora de aquisição; o detector da aplicação estima a pose em `camera_link`. |
| **2. Coordinate Transformation** | Transformação de coordenadas | A aplicação usa `tf2_ros.Buffer.lookup_transform` para transformar a pose em `base_link` no instante de captura. A posição da câmara precisa de URDF ou de transformada estática. |
| **3. Motion Planning** | Planeamento do movimento | Um planeador como MoveIt 2 combina alvo, modelo e estado para produzir uma trajetória de juntas. |
| **4. Motion Control** | Controlo do movimento | O `joint_trajectory_controller` configurado recebe `FollowJointTrajectory`, escreve interfaces de comando e envia referências ao servo e motor. |
| **5. Feedback** | Realimentação | O encoder alimenta a malha servo local e as interfaces de estado. `joint_state_broadcaster` publica `/joint_states`; `robot_state_publisher` usa URDF e estados para `/tf` e `/tf_static`. O controlador pode ler estado diretamente. |

## Distinguir as interfaces

**Distinguir os fluxos:** URDF descreve o robô e interfaces `ros2_control` opcionais; não controla motores. TF2 consulta transformações. Comandos são referências, estados são medidas; a ausência de `/joint_states` não prova que a malha servo tenha parado.

**Laboratório disponível:** a junta virtual usa `forward_position_controller` e `mock_components/GenericSystem`, não o controlador de trajetória, câmara, MoveIt 2 ou motor real. A arquitetura completa é conceptual.

**Extensões futuras:** watchdog, falhas, QoS, sincronização temporal, diagnóstico, tempo real e simulação. Preservar os cinco nomes das etapas.

## Fonte comum e referências adicionais

[Abrir e editar o diagrama Mermaid comum](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) · [Referência ROS 2](06-ros2-foundations.md) · [Prática com controlador simulado](07-ros2-control-lab.md)
