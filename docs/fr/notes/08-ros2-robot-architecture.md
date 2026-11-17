# 8. Architecture robot ROS 2 : cinq étapes

**Langues:** [en](../../en/notes/08-ros2-robot-architecture.md) · [fr](08-ros2-robot-architecture.md) · [de](../../de/notes/08-ros2-robot-architecture.md) · [it](../../it/notes/08-ros2-robot-architecture.md) · [es](../../es/notes/08-ros2-robot-architecture.md) · [pt](../../pt/notes/08-ros2-robot-architecture.md) · [zh](../../zh/notes/08-ros2-robot-architecture.md) · [ja](../../ja/notes/08-ros2-robot-architecture.md) · [nb](../../nb/notes/08-ros2-robot-architecture.md) · [ru](../../ru/notes/08-ros2-robot-architecture.md) · [ko](../../ko/notes/08-ros2-robot-architecture.md) · [fi](../../fi/notes/08-ros2-robot-architecture.md) · [pl](../../pl/notes/08-ros2-robot-architecture.md)

[Fondements de ROS 2](06-ros2-foundations.md) · [Laboratoire d'articulation virtuelle](07-ros2-control-lab.md) · [Sommaire](../README.md)

> **Conceptuel uniquement.** Aucun contrôle d'équipement réel ni garantie de sécurité.

Les cinq noms anglais du tableau correspondent exactement aux noms du [diagramme Mermaid modifiable commun](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram). Chaque étape est une fonction, **pas nécessairement un nœud ROS unique**. Le schéma est conceptuel et ne constitue ni un robot exécutable ni un dispositif de sécurité.

## Cinq étapes fonctionnelles

| Étape en anglais | Terme français | Responsabilités et composants ROS |
| --- | --- | --- |
| **1. Perception** | Perception | Le driver caméra publie `sensor_msgs/msg/Image` et l'heure d'acquisition ; un détecteur applicatif estime la pose de l'objet dans `camera_link`. |
| **2. Coordinate Transformation** | Transformation de coordonnées | L'application interroge `tf2_ros.Buffer.lookup_transform` pour obtenir la pose dans `base_link` à l'instant de l'image. Le montage de la caméra doit être décrit par URDF ou par un diffuseur statique. |
| **3. Motion Planning** | Planification du mouvement | Un planificateur tel que MoveIt 2 utilise la cible, le modèle et l'état du robot pour produire une trajectoire articulaire. |
| **4. Motion Control** | Commande du mouvement | Un `joint_trajectory_controller` configuré accepte `FollowJointTrajectory`, écrit les interfaces de commande et pilote la consigne vers firmware et moteur. |
| **5. Feedback** | Retour d'état | L'encodeur alimente la boucle servo locale et les interfaces d'état. `joint_state_broadcaster` publie `/joint_states` ; `robot_state_publisher` publie `/tf` et `/tf_static` à partir d'URDF et de l'état. Un contrôleur peut lire l'état directement. |

## Distinguer les interfaces

**Ne pas confondre les flux :** URDF décrit la structure et éventuellement les interfaces `ros2_control`, sans commander les moteurs. TF2 interroge les transformations, pas le mouvement. Une commande est une consigne, l'état est une mesure ; l'absence de `/joint_states` n'implique pas forcément l'arrêt du servo local.

**Exercice distinct :** le joint virtuel utilise `forward_position_controller` et `mock_components/GenericSystem`, pas un contrôleur de trajectoire, une caméra ou un moteur réel. Le schéma complet reste conceptuel.

**Extensions ultérieures :** supervision des défauts, watchdog, QoS, synchronisation temporelle, diagnostics, temps réel et simulation. Conserver les cinq noms d'étape.

## Source commune et ressources complémentaires

[Ouvrir et modifier le diagramme Mermaid commun](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) · [Référence ROS 2](06-ros2-foundations.md) · [Exercice avec contrôleur simulé](07-ros2-control-lab.md)
