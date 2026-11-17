# 8. Архитектура робота ROS 2: пять этапов

**Языки:** [en](../../en/notes/08-ros2-robot-architecture.md) · [fr](../../fr/notes/08-ros2-robot-architecture.md) · [de](../../de/notes/08-ros2-robot-architecture.md) · [it](../../it/notes/08-ros2-robot-architecture.md) · [es](../../es/notes/08-ros2-robot-architecture.md) · [pt](../../pt/notes/08-ros2-robot-architecture.md) · [zh](../../zh/notes/08-ros2-robot-architecture.md) · [ja](../../ja/notes/08-ros2-robot-architecture.md) · [nb](../../nb/notes/08-ros2-robot-architecture.md) · [ru](08-ros2-robot-architecture.md) · [ko](../../ko/notes/08-ros2-robot-architecture.md) · [fi](../../fi/notes/08-ros2-robot-architecture.md) · [pl](../../pl/notes/08-ros2-robot-architecture.md)

[Основы ROS 2](06-ros2-foundations.md) · [Лаборатория виртуального сустава](07-ros2-control-lab.md) · [Оглавление](../README.md)

> **Только концептуальная схема.** Она не управляет настоящим оборудованием и не гарантирует безопасность.

Пять английских названий ниже **точно совпадают** с названиями блоков в [общей редактируемой Mermaid-схеме](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram). Этап обозначает **функцию системы, а не обязательно отдельный ROS-узел или процесс**. Это концептуальная схема, не программа управления настоящим роботом и не система безопасности.

## Пять функциональных этапов

| Английское название | Русский перевод | Функции и компоненты ROS |
| --- | --- | --- |
| **1. Perception** | Восприятие | Драйвер камеры публикует `sensor_msgs/msg/Image` со временем съёмки. Прикладной детектор вычисляет положение объекта в системе `camera_link`. |
| **2. Coordinate Transformation** | Преобразование координат | Приложение запрашивает `tf2_ros.Buffer.lookup_transform` и переводит координаты объекта из `camera_link` в `base_link` на **момент съёмки**, а не получения сообщения. Преобразование крепления камеры должно поступать из URDF или статического TF-публикатора. |
| **3. Motion Planning** | Планирование движения | Планировщик, например MoveIt 2, использует цель, модель робота и его текущее состояние для формирования траектории суставов. |
| **4. Motion Control** | Управление движением | Настроенный `joint_trajectory_controller` принимает action `FollowJointTrajectory`, выдаёт задания через command interfaces в драйвер/прошивку сервопривода и далее двигателю. |
| **5. Feedback** | Обратная связь | Энкодер передаёт измерения в локальный контур сервопривода и через драйвер в state interfaces. `joint_state_broadcaster` публикует `/joint_states`; `robot_state_publisher` использует URDF и состояния суставов, публикуя `/tf` и `/tf_static`. Контроллер также может читать state interfaces напрямую. |

## Различие между интерфейсами и потоками

**Не смешивай пути:** URDF описывает звенья, суставы и при необходимости интерфейсы `ros2_control`, но не управляет двигателем. TF2 отвечает на запросы преобразований, не посылает команд движения. Command interface — заданное значение, state interface — измеренное; отсутствие `/joint_states` не доказывает остановку локального сервоконтроллера.

**Граница существующей лаборатории:** там используется `forward_position_controller` вместе с `mock_components/GenericSystem`, **не** `joint_trajectory_controller`, камера, MoveIt 2 или реальный двигатель с энкодером. Полная схема пока иллюстрирует возможную архитектуру, а не испытанный робот.

**Возможные расширения:** watchdog и обработка ошибок, QoS/DDS, синхронизация часов, диагностика, real-time и симуляция. Пять названий этапов остаются неизменными.

## Общий исходник и дополнительные материалы

[Открыть и изменить общую схему Mermaid](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) · [Справочник ROS 2](06-ros2-foundations.md) · [Практика с имитацией контроллера](07-ros2-control-lab.md)
