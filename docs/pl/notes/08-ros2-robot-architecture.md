# 8. Architektura robota ROS 2: pięć etapów

**Języki:** [en](../../en/notes/08-ros2-robot-architecture.md) · [fr](../../fr/notes/08-ros2-robot-architecture.md) · [de](../../de/notes/08-ros2-robot-architecture.md) · [it](../../it/notes/08-ros2-robot-architecture.md) · [es](../../es/notes/08-ros2-robot-architecture.md) · [pt](../../pt/notes/08-ros2-robot-architecture.md) · [zh](../../zh/notes/08-ros2-robot-architecture.md) · [ja](../../ja/notes/08-ros2-robot-architecture.md) · [nb](../../nb/notes/08-ros2-robot-architecture.md) · [ru](../../ru/notes/08-ros2-robot-architecture.md) · [ko](../../ko/notes/08-ros2-robot-architecture.md) · [fi](../../fi/notes/08-ros2-robot-architecture.md) · [pl](08-ros2-robot-architecture.md)

[Podstawy ROS 2](06-ros2-foundations.md) · [Laboratorium wirtualnego przegubu](07-ros2-control-lab.md) · [Spis treści](../README.md)

> **Wyłącznie schemat koncepcyjny.** Bez sterowania rzeczywistym sprzętem i bez gwarancji bezpieczeństwa.

Pięć angielskich nazw etapów jest identycznych jak w [wspólnym edytowalnym diagramie Mermaid](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram). Etap oznacza **funkcję, niekoniecznie pojedynczy węzeł ROS**. Diagram jest koncepcyjny, a nie gotowym układem sterowania ani zabezpieczeń robota.

## Pięć etapów funkcjonalnych

| Angielska nazwa etapu | Polskie tłumaczenie | Zadania i komponenty ROS |
| --- | --- | --- |
| **1. Perception** | Percepcja | Sterownik kamery publikuje `sensor_msgs/msg/Image` ze znacznikiem czasu wykonania obrazu; detektor aplikacyjny szacuje położenie obiektu w `camera_link`. |
| **2. Coordinate Transformation** | Transformacja współrzędnych | Aplikacja wywołuje `tf2_ros.Buffer.lookup_transform`, aby przeliczyć położenie do `base_link` dla chwili wykonania obrazu. Mocowanie kamery musi być opisane przez URDF lub statyczny TF. |
| **3. Motion Planning** | Planowanie ruchu | Planista, np. MoveIt 2, tworzy trajektorię przegubów na podstawie celu, modelu i bieżącego stanu robota. |
| **4. Motion Control** | Sterowanie ruchem | Skonfigurowany `joint_trajectory_controller` odbiera `FollowJointTrajectory` i zapisuje żądane wartości w interfejsach poleceń sterownika serwa i silnika. |
| **5. Feedback** | Sprzężenie zwrotne | Enkoder zasila lokalną pętlę serwa oraz interfejsy stanu. `joint_state_broadcaster` publikuje `/joint_states`, a `robot_state_publisher` korzysta z URDF i stanów, wysyłając `/tf` i `/tf_static`. Kontroler może czytać stan bezpośrednio. |

## Rozróżnienie interfejsów

**Nie myl przepływów:** URDF opisuje robot i opcjonalne interfejsy `ros2_control`, ale nie steruje silnikiem. TF2 odczytuje transformacje. Polecenie to wartość zadana, stan to wartość mierzona; brak `/joint_states` nie dowodzi zatrzymania lokalnego serwa.

**Istniejące laboratorium:** wirtualny przegub używa `forward_position_controller` i `mock_components/GenericSystem`, a nie kontrolera trajektorii, kamery, MoveIt 2 czy prawdziwego silnika. Pełny diagram pozostaje koncepcyjny.

**Przyszłe rozszerzenia:** watchdog, obsługa awarii, QoS, synchronizacja czasu, diagnostyka, czas rzeczywisty i symulacja. Zachowaj pięć angielskich nazw etapów.

## Wspólne źródło i dodatkowe materiały

[Otwórz i edytuj wspólny diagram Mermaid](../../../ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) · [Materiały ROS 2](06-ros2-foundations.md) · [Ćwiczenie ze sterownikiem symulowanym](07-ros2-control-lab.md)
