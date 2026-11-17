# 8. Arquitectura ROS 2 de un robot: cinco etapas

**Idiomas:** [en](../../en/notes/08-ros2-robot-architecture.md) · [fr](../../fr/notes/08-ros2-robot-architecture.md) · [de](../../de/notes/08-ros2-robot-architecture.md) · [it](../../it/notes/08-ros2-robot-architecture.md) · [es](08-ros2-robot-architecture.md) · [pt](../../pt/notes/08-ros2-robot-architecture.md) · [zh](../../zh/notes/08-ros2-robot-architecture.md) · [ja](../../ja/notes/08-ros2-robot-architecture.md) · [nb](../../nb/notes/08-ros2-robot-architecture.md) · [ru](../../ru/notes/08-ros2-robot-architecture.md) · [ko](../../ko/notes/08-ros2-robot-architecture.md) · [fi](../../fi/notes/08-ros2-robot-architecture.md) · [pl](../../pl/notes/08-ros2-robot-architecture.md)

[Fundamentos de ROS 2](06-ros2-foundations.md) · [Laboratorio de articulación virtual](07-ros2-control-lab.md) · [Índice](../README.md)

> **Solo conceptual.** No controla equipos físicos ni garantiza la seguridad.

Los cinco nombres ingleses coinciden exactamente con el [diagrama Mermaid compartido y editable](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram). Cada etapa es una **función, no necesariamente un solo nodo ROS**. Es un esquema conceptual, no un robot ejecutable ni un sistema de seguridad.

## Cinco etapas funcionales

| Etapa en inglés | Traducción | Funciones y componentes ROS |
| --- | --- | --- |
| **1. Perception** | Percepción | El controlador de cámara publica `sensor_msgs/msg/Image` con instante de captura; un detector de aplicación estima la pose en `camera_link`. |
| **2. Coordinate Transformation** | Transformación de coordenadas | La aplicación usa `tf2_ros.Buffer.lookup_transform` para convertir la pose a `base_link` en el instante de adquisición. La posición de la cámara debe existir en URDF o en una transformación estática. |
| **3. Motion Planning** | Planificación del movimiento | Un planificador como MoveIt 2 usa la meta, el modelo y el estado para producir una trayectoria de articulaciones. |
| **4. Motion Control** | Control del movimiento | Un `joint_trajectory_controller` configurado recibe `FollowJointTrajectory`, escribe interfaces de comandos y envía consignas al servo y al motor. |
| **5. Feedback** | Realimentación | El encoder alimenta el lazo servo local y las interfaces de estado. `joint_state_broadcaster` publica `/joint_states`; `robot_state_publisher` usa URDF y estados para `/tf` y `/tf_static`. El controlador puede leer estado directamente. |

## Distinguir las interfaces

**No mezcles los flujos:** URDF describe el robot y opcionalmente interfaces `ros2_control`; no mueve motores. TF2 consulta transformaciones. El comando es una consigna y el estado es medido; perder `/joint_states` no demuestra que el servo local haya parado.

**Laboratorio disponible:** la articulación virtual usa `forward_position_controller` y `mock_components/GenericSystem`, no un controlador de trayectoria, cámara, MoveIt 2 ni hardware real. La arquitectura completa es conceptual.

**Ampliaciones posteriores:** supervisión de fallos, watchdog, QoS, sincronización temporal, diagnóstico, tiempo real y simulación. Mantén los cinco nombres.

## Fuente común y lecturas adicionales

[Abrir y editar el diagrama Mermaid de arquitectura](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) · [Referencia de ROS 2](06-ros2-foundations.md) · [Práctica del controlador simulado](07-ros2-control-lab.md)
