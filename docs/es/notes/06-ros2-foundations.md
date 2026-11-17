# 6. ROS 2: software robótico distribuido e interfaces

**Languages:** [en](../../en/notes/06-ros2-foundations.md) · [fr](../../fr/notes/06-ros2-foundations.md) · [de](../../de/notes/06-ros2-foundations.md) · [it](../../it/notes/06-ros2-foundations.md) · [es](06-ros2-foundations.md) · [pt](../../pt/notes/06-ros2-foundations.md) · [zh](../../zh/notes/06-ros2-foundations.md) · [ja](../../ja/notes/06-ros2-foundations.md) · [nb](../../nb/notes/06-ros2-foundations.md) · [ru](../../ru/notes/06-ros2-foundations.md) · [ko](../../ko/notes/06-ros2-foundations.md) · [fi](../../fi/notes/06-ros2-foundations.md) · [pl](../../pl/notes/06-ros2-foundations.md)

**Unidades empleadas aquí (definidas antes de los ejemplos):** `m` — metro; `s` — segundo. [Glosario de unidades](../UNITS.md).

[Course index](../README.md) · [Coordinate frames](04-coordinate-frames.md) · [Jacobian](05-velocity-jacobian.md) · [Docker lab](../../../ros2/README.md)

> **Safety:** Solo ejemplo de software sintético. No utilices este código para controlar robots o máquinas reales. ROS no sustituye la cinemática, el control de tiempo real ni los mecanismos de seguridad del hardware.

ROS 2 (Robot Operating System 2) conecta componentes de software distribuidos en un robot. Para quien programa backend, un nodo se parece a un proceso, un topic a un flujo de eventos tipados y un servicio a una RPC. La comparación es aproximada: normalmente se utiliza DDS para el descubrimiento distribuido, sin un broker central obligatorio.

![ROS 2 publisher and subscriber connected by a typed topic; a CLI client calls a service](../../../assets/figures/ros2-topic-service.svg)

![Capas de software ROS 2 y límite de seguridad del hardware](../../../assets/figures/ros2-software-layers.svg)

*La comunicación no sustituye el control de bajo nivel ni las medidas independientes de seguridad.*

## Ruta de aprendizaje

1. [Arquitectura, middleware y grafo ROS](#section-1)
2. [Nodos, topics y mensajes tipados](#section-2)
3. [Servicios, acciones y parámetros](#section-3)
4. [Paquetes, workspaces, colcon y ament](#section-4)
5. [Inspección con ROS 2 CLI](#section-5)
6. [Archivos launch](#section-6)
7. [tf2 y marcos de coordenadas](#section-7)
8. [URDF y robot_state_publisher](#section-8)
9. [ros2_control y límite de hardware](#section-9)
10. [QoS, descubrimiento DDS y Docker](#section-10)
11. [Práctica: publisher, subscriber, service y launch](#section-11)
12. [Glosario y límites](#section-12)

<a id="section-1"></a>

## 1. Arquitectura, middleware y grafo ROS

**Problema:** sensores, localización y planificación necesitan contratos independientes. ROS 1 usaba un master central para descubrir nombres. ROS 2 utiliza RMW y habitualmente DDS/RTPS para descubrir participantes sin aquel master. El grafo ROS contiene nodos, topics, servicios y acciones descubiertos. Un nodo es lógico; varios pueden compartir proceso, y los procesos pueden vivir en distintos equipos. El descubrimiento no es un sistema de autorización.

<a id="section-2"></a>

## 2. Nodos, topics y mensajes tipados

**Problema:** enviar medidas continuas a múltiples consumidores sin polling. Un publisher publica mensajes en un topic; los subscribers los reciben de forma asíncrona. std_msgs/msg/String define el campo string data, contrato compartido por Python y C++. /sample_source publica en /training/status; /sample_monitor suscribe y cuenta. Una cola de profundidad 10 no es almacenamiento duradero: un suscriptor nuevo normalmente ve mensajes futuros.

**Ejemplo de descubrimiento:** supongamos que `/sample_source` publicó `sample 1` antes de que se descubriera `/sample_monitor`. Con el historial `volatile` de este laboratorio, el mensaje anterior no se reproduce automáticamente. El monitor puede responder inicialmente `received 0 samples` aunque el publisher siga enviando. El contador puede aumentar cuando se descubren endpoints compatibles. La secuencia publicada y el número de mensajes recibidos miden cosas distintas; ninguno confirma una transacción.

**Qué demuestra la CLI:** `ros2 topic list -t` muestra nombres y tipos de topics descubiertos, **no** demuestra recepción por subscribers. `ros2 topic info /training/status -v` permite ver endpoints descubiertos y QoS ofrecidas/solicitadas. Cero suscriptores puede significar ausencia de ellos **o** descubrimiento aún incompleto. Si aparecen endpoints pero no llegan mensajes, comprobar tipos, QoS, registros de procesos y `ROS_DOMAIN_ID`. Son instantáneas de estado, no garantías de entrega. Ejecutar estos comandos dentro del contenedor del laboratorio.

<a id="section-3"></a>

## 3. Servicios, acciones y parámetros

**Problema:** diferenciar flujo, consulta breve y tarea larga. Service usa request/response: /training/count con std_srvs/srv/Trigger devuelve success y message. Action gestiona goal, feedback, result y cancel, por ejemplo navegación. Parameter es configuración del nodo: interval_s=1.0 se lee al crear el temporizador. Cambiar el parámetro después no reconstruye el temporizador automáticamente. Los reintentos requieren evaluar idempotencia.

La elección depende del tipo de respuesta, duración y fallos posibles. Estos mecanismos no son intercambiables:

| Mecanismo | Interacción | Uso adecuado | No equivale a |
| --- | --- | --- | --- |
| Topic | Publisher → 0..N subscribers | Telemetría continua | Registro persistente o transacción confirmada |
| Service | Solicitud → respuesta | Consulta breve u operación limitada | Commit garantizado o tarea larga |
| Action | Meta → feedback/resultado, cancelación opcional | Navegación o cálculo prolongado | Flujo periódico de sensor |
| Parameter | Valor propio de un nodo | Configuración como `interval_s` | Base de datos global distribuida |

En este ejemplo, `/training/status` es un topic, `/training/count` un service y `interval_s` un parámetro del nodo; no hay ninguna action de aplicación. Un timeout del servicio no demuestra que el servidor no haya ejecutado la petición: los reintentos dependen de la semántica de la operación.

<a id="section-4"></a>

## 4. Paquetes, workspaces, colcon y ament

**Problema:** compilar y distribuir dependencias y ejecutables reproduciblemente. package.xml declara metadatos; ament_python y ament_cmake integran el sistema de construcción. Un workspace suele tener src, build, install y log. colcon organiza la compilación; no transporta mensajes. Hay que cargar el entorno ROS (underlay) y después el workspace (overlay). telemetry_demo publica dos entry points en setup.py e instala un launch.

En el `ros2/Dockerfile` real, la **construcción de imagen** (`RUN`) y el **arranque del contenedor** (`CMD`) son fases diferentes. Durante la construcción se carga únicamente el underlay de ROS antes de compilar con `colcon`:

**Construcción de imagen (`RUN`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
colcon build --packages-select telemetry_demo
```

**Arranque del contenedor (`CMD`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
source /opt/training_ws/install/setup.bash
exec ros2 launch telemetry_demo demo.launch.py
```

Al arrancar, otra shell vuelve a cargar el underlay, después el overlay del workspace, y ejecuta el archivo launch. `package.xml` declara dependencias; `setup.py` instala los puntos de entrada Python y el archivo launch. `build/` e `install/` son artefactos generados, no carpetas para editar fuentes. Una compilación correcta no prueba que la aplicación esté lista.

<a id="section-5"></a>

## 5. Inspección con ROS 2 CLI

**Problema:** observar el grafo real. ros2 node list/info inspecciona nodos; topic list/info/echo examina mensajes; interface show consulta tipos; service list/call, action list y param get inspeccionan el resto. El ejemplo contiene /sample_source, /sample_monitor, /training/status y /training/count. No define ninguna acción propia. Ante datos ausentes revisa nombres, tipos, QoS y ROS_DOMAIN_ID.

Comandos CLI dentro del contenedor con el entorno ROS activado:

```bash
ros2 node list
ros2 node info /sample_source
ros2 topic list -t
ros2 topic info /training/status -v
ros2 topic echo /training/status
ros2 interface show std_msgs/msg/String
ros2 service list -t
ros2 service call /training/count std_srvs/srv/Trigger "{}"
ros2 action list
ros2 param get /sample_source interval_s
```

<a id="section-6"></a>

## 6. Archivos launch

**Problema:** reproducir arranque de varios procesos y sus parámetros. demo.launch.py devuelve LaunchDescription con dos launch_ros.actions.Node e interval_s=1.0. Los launch aceptan argumentos, namespaces, remapping e inclusiones. Arrancar procesos no garantiza que sus servicios ya estén listos; readiness, errores y reintentos se gestionan por separado.

**Observar la disponibilidad:** `launch_ros.actions.Node` inicia dos **procesos**, pero el descubrimiento DDS y el primer mensaje `/training/status` llegan después. Una llamada inmediata a `/training/count` puede responder normalmente `received 0 samples`; luego el contador aumenta. No demuestra pérdida de una transacción: el servicio solo cuenta mensajes recibidos por el monitor. `interval_s=1.0` se lee al crear el temporizador; no reconfigura automáticamente el periodo mientras funciona.

<a id="section-7"></a>

## 7. tf2 y marcos de coordenadas

**Problema:** traducir una detección de camera_link a base_link o map. tf2 conserva transformaciones temporales con rotación y traslación; los montajes fijos utilizan transformaciones estáticas. Los frames padre-hijo y timestamps deben coincidir. tf2 no resuelve por sí mismo cinemática directa/inversa ni planificación. Consulta los capítulos sobre coordenadas y Jacobiano para las matemáticas.

[Coordinate frames](04-coordinate-frames.md) · [Velocity and Jacobian](05-velocity-jacobian.md)

**Ejemplo de cadena de marcos (no obligatoria):** `map → odom → base_link → camera_link`. Una cámara montada de forma rígida tiene una transformación `static`; la base móvil requiere transformaciones `dynamic`. Para expresar en `map` un punto observado en `camera_link` en el instante *t*, tf2 debe encontrar la cadena **para el tiempo de la medición**. Un marco inexistente, un árbol desconectado o un tiempo no disponible produce un error de lookup/extrapolation; usar la transformación más reciente para una observación antigua puede dar coordenadas incorrectas.

**Ejemplo del sentido de la transformación y de la inversa.** Sea `base_link` (B) el marco padre y `tool` (T) el marco hijo. Sin giro relativo, una traslación de 0.1 m a lo largo del X positivo del padre sitúa el origen de la herramienta **por delante del origen de la base expresado en B**. En las coordenadas de T, el desplazamiento inverso tiene signo opuesto:

$$
{}^{B}\mathbf p_{T}=(0.1, 0, 0)\ \mathrm{m},\qquad
{}^{T}\mathbf p_{B}=(-0.1, 0, 0)\ \mathrm{m}\quad (R=I).
$$

Este cambio de signo solo basta cuando los ejes mantienen **la misma orientación**. En general, una transformación combina giro y traslación. La inversa debe deshacer **ambos**; para una matriz de rotación válida, la inversa es $R^T$:

$$
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT},\qquad
\mathbf p_T=R_{BT}^{T}(\mathbf p_B-\mathbf t_{BT}),\qquad
\mathbf t_{TB}=-R_{BT}^{T}\mathbf t_{BT}.
$$

En otra pose, giramos T +90° alrededor del eje Z común conservando la traslación (0.1 m, 0 m) en B. El origen de B expresado en T está en (0 m, +0.1 m), **no** en (−0.1 m, 0 m). Las mismas matrices convierten el punto (0 m, 0.05 m) de T a B:

$$
R_{BT}=\begin{bmatrix}0 & -1\\1 & 0\end{bmatrix},\quad
\mathbf t_{BT}=\begin{bmatrix}0.1\\0\end{bmatrix}\ \mathrm{m},\quad
\mathbf t_{TB}=\begin{bmatrix}0\\0.1\end{bmatrix}\ \mathrm{m}.
$$

$$
\mathbf p_T=\begin{bmatrix}0\\0.05\end{bmatrix}\ \mathrm{m}
\Longrightarrow
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT}
=\begin{bmatrix}0.05\\0\end{bmatrix}\ \mathrm{m}.
$$

Los marcos y transformaciones **describen coordenadas**, no son órdenes de movimiento. En ROS 2, las traslaciones se expresan convencionalmente en metros; la [lección de sistemas de coordenadas](04-coordinate-frames.md#section-3) usa milímetros y requiere conversión antes de combinar ejemplos. Una transformación estática describe una fijación invariable; las dinámicas las publican componentes con estados cambiantes. Para medidas antiguas se necesita la transformación en el instante de medición y gestionar la falta de datos.

<a id="section-8"></a>

## 8. URDF y robot_state_publisher

**Problema:** definir una estructura mecánica compartida. URDF describe links, joints, ejes, orígenes y propiedades opcionales visual/collision/inertial. robot_state_publisher combina URDF con posiciones articulares, habitualmente sensor_msgs/msg/JointState en /joint_states, para publicar transforms. URDF no proporciona datos del encoder, simulación ni solución de cinemática inversa. Verifica metros, radianes y ejes.

**Origen de las transformaciones:** URDF define articulaciones `fixed` y móviles. `robot_state_publisher` publica transformaciones `static` de las articulaciones fijas y calcula transformaciones `dynamic` de las móviles a partir de las posiciones en `/joint_states` (`sensor_msgs/msg/JointState`). URDF **no mide** posiciones articulares ni recrea datos ausentes. Las dimensiones deben estar en metros, los ángulos en radianes y las marcas de tiempo deben ser coherentes.

<a id="section-9"></a>

## 9. ros2_control y límite de hardware

**Problema:** separar lógica de control y drivers. ros2_control aporta controller manager, interfaces de estado (posición/velocidad), interfaces de comando (posición/velocidad/effort) y abstracciones de hardware. El planificador produce referencias, el controlador usa feedback y la interfaz conecta con el dispositivo. Un mensaje ROS no garantiza tiempo real, límites de corriente ni parada segura. Este ejemplo no utiliza actuadores.

[First-order dynamics](02-first-order-dynamics.md) · [Feedback PID](03-feedback-control.md)

**Función del gestor de controladores:** `controller_manager` administra el ciclo de vida de los controladores y, mediante el gestor de recursos, el acceso a interfaces de estado (state interfaces) y de comando (command interfaces). Un controlador puede leer un estado medido como el `joint1/position` hipotético; un controlador activo puede reservar una interfaz de comando compatible para escribir la consigna. El valor medido no es la consigna y dos controladores no pueden apropiarse libremente de la misma interfaz de comando ocupada. Por tanto, activar controladores y asignar recursos no equivale a descubrir topics.

**Límite de este laboratorio:** `/training/status` y `/training/count` muestran un topic y un service, **no `ros2_control`**. Ninguno de los dos nodos es un controlador y el laboratorio no ejecuta `controller_manager`, ni interfaces de hardware ni un lazo de control cerrado. Pasar el smoke test no valida el ciclo de vida, los tiempos de control ni la seguridad del dispositivo. Consulta la [introducción oficial a ros2_control](https://control.ros.org/jazzy/doc/getting_started/getting_started.html).

**Práctica: ros2_control y TF2 sin GUI con articulación virtual:** [Práctica: ros2_control y TF2 sin GUI con articulación virtual](07-ros2-control-lab.md). El nuevo laboratorio cubre URDF, GenericSystem, comandos, estados, /joint_states, TF2, QoS y diagnóstico del cargador ARM64; no controla hardware real.

**Siguiente paso: arquitectura completa.** El [diagrama Mermaid ROS 2 de cinco etapas](08-ros2-robot-architecture.md) conecta percepción, TF2 con tiempo, planificación, control y realimentación. La parte de hardware es conceptual.

<a id="section-10"></a>

## 10. QoS, descubrimiento DDS y Docker

**Problema:** entender pérdidas de datos y nodos invisibles. QoS incluye reliable/best_effort, volatile/transient_local, history y depth. Si un subscriber exige más garantías de las que ofrece el publisher, puede no recibir mensajes. DDS suele usar multicast UDP y puertos dinámicos; VPN, firewall y Docker Desktop pueden interferir. ROS_DOMAIN_ID debe coincidir. El laboratorio ejecuta todo en un solo contenedor sin privilegios ni puertos expuestos; no valida conexión entre máquinas.

**Ejemplo de QoS incompatible:** si un publisher ofrece `best_effort` pero un subscriber solicita `reliable`, pueden coincidir el nombre y tipo del topic y aparecer los endpoints en el grafo, pero el suscriptor **no recibe mensajes** porque exige una garantía que no se ofrece. En sentido inverso, un suscriptor `best_effort` puede recibir de un publisher `reliable` si las otras políticas QoS son compatibles. `volatile` no recupera mensajes previos; `transient_local` puede retener una historia limitada mientras haya un publisher compatible, **no un registro distribuido persistente**.

**Diagnóstico por orden:** comprobar `ROS_DOMAIN_ID=42` dentro del mismo contenedor; ejecutar `ros2 node list`, luego `ros2 topic info /training/status -v` para revisar endpoints y QoS, y `docker compose logs demo` para comprobar procesos. Si el grafo sigue vacío, investigar RMW/DDS, interfaces y cortafuegos. Publicar puertos TCP no soluciona universalmente DDS; este ejemplo no prueba varios equipos.

[Documentación oficial de ROS 2 Jazzy sobre QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)

[Alternativa: imagen ROS oficial sin Compose ni Dockerfile propio](../../../ros2/PLAIN_DOCKER.md)

<a id="section-11"></a>

## 11. Práctica: publisher, subscriber, service y launch

docker compose up --build -d inicia el ejemplo. Los logs deberían mostrar mensajes publicados y recibidos con un contador creciente. El servicio responde con success=True y texto como received 12 samples; el número varía con el tiempo. Un [smoke test Docker independiente en GitHub Actions](../../../.github/workflows/ros2-live-smoke.yml) **sí ejecutó la aplicación dentro de un solo contenedor**: comprobó ambos nodos ROS, recibió un mensaje tipado de `/training/status` y obtuvo respuesta de `/training/count`. El CI ordinario no ejecuta ROS. Estas pruebas no validan DDS entre varios equipos, tiempos deterministas, hardware real ni la instalación local de Docker del lector.

[Complete source, expected results and diagnostics](../../../ros2/README.md). From the repository root:

Para aprender por pasos, empieza con el talker `demo_nodes_cpp` y el listener `demo_nodes_py` instalados en la imagen; después inspecciona el paquete propio `telemetry_demo` y finalmente `ros2_control`. El Dockerfile instala las demos con APT y construye `telemetry_demo` mediante `colcon`. Abre **una sola shell Bash interactiva** y carga los entornos **una vez por shell nueva**: un proceso `docker compose exec` separado no hereda el entorno de `CMD`.

En el host inicia el contenedor y abre una shell interactiva:

```bash
cd ros2
docker compose up --build -d
docker compose logs --tail=20 demo
docker compose exec demo bash
```

Dentro del contenedor, no en el host, carga una vez ambos entornos y revisa el grafo:

```bash
echo "$ROS_DISTRO"
ros2 node list
ros2 service call /training/count std_srvs/srv/Trigger "{}"
exit
```

Tras `exit`, en el host limpia el contenedor:

```bash
docker compose down
```

**Límite de confianza del CI:** la prueba real de ROS 2 en Docker ahora se ejecuta automáticamente solo cuando los cambios llegan a `main`, o mediante `workflow_dispatch` sobre `main`. No se ejecuta para las revisiones `pull_request`, porque eso permitiría ejecutar en el host del runner scripts Bash y Dockerfiles modificados en el PR. Las pruebas Python aisladas antes de integrar el cambio no equivalen a ejecutar ROS. Hace falta una revisión independiente antes de integrar y comprobar la prueba real después.

<a id="section-12"></a>

## 12. Glosario y límites

- **Node / proceso:** un nodo es un componente ROS lógico con nombre; un proceso del sistema puede alojar varios nodos.
- **ROS graph:** conjunto de endpoints descubiertos en ese momento, no un registro central ni un sistema de autorización.
- **Topic:** flujo asíncrono con nombre y varios posibles publishers y subscribers.
- **Message:** estructura de datos tipada definida por una interfaz ROS, no un objeto arbitrario de Python o C++.
- **Publisher / subscriber:** emisor y receptor de mensajes; se requieren descubrimiento y QoS compatible para entregarlos.
- **Service:** petición y respuesta tipadas para una interacción breve; un timeout no demuestra que el servidor no actuó.
- **Action:** objetivo con feedback, resultado y solicitud de cancelación; cancelar no garantiza una parada inmediata.
- **Parameter:** valor propio de un nodo; cambiarlo no reconfigura automáticamente un temporizador existente.
- **RMW / DDS:** RMW abstrae el middleware; DDS suele encargarse del descubrimiento y transporte, no autentica por sí solo.
- **colcon / ament:** orquestación de compilación del workspace / integración de paquetes ROS, no middleware de mensajes.
- **Launch:** descripción de procesos y configuración que deben iniciarse; inicio no implica disponibilidad.
- **tf2:** infraestructura para transformaciones entre marcos con marcas de tiempo, no un solver de cinemática inversa.
- **URDF / robot_state_publisher:** descripción estructural del robot / publicación de transformaciones a partir del modelo y estados articulares.
- **ros2_control:** ciclo de vida de controladores e interfaces state/command gestionadas; no forma parte del laboratorio topic/service.
- **QoS:** compatibilidad y políticas de entrega e historial; ni registro persistente ni certificación de seguridad.

**Versiones comprobadas el 13 de noviembre de 2026:** ROS 2 Jazzy LTS tiene soporte hasta mayo de 2029 y Lyrical LTS hasta mayo de 2031. La etiqueta Docker no fija un digest inmutable de la imagen ni versiones concretas de los paquetes apt.

**Primary sources:** [ROS 2 releases](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst) · [Jazzy documentation](https://docs.ros.org/en/jazzy/) · [tf2](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html) · [URDF](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html) · [ros2_control](https://control.ros.org/jazzy/)
