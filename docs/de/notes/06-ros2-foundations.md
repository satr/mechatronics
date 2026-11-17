# 6. ROS 2: verteilte Robotiksoftware und Schnittstellen

**Languages:** [en](../../en/notes/06-ros2-foundations.md) · [fr](../../fr/notes/06-ros2-foundations.md) · [de](06-ros2-foundations.md) · [it](../../it/notes/06-ros2-foundations.md) · [es](../../es/notes/06-ros2-foundations.md) · [pt](../../pt/notes/06-ros2-foundations.md) · [zh](../../zh/notes/06-ros2-foundations.md) · [ja](../../ja/notes/06-ros2-foundations.md) · [nb](../../nb/notes/06-ros2-foundations.md) · [ru](../../ru/notes/06-ros2-foundations.md) · [ko](../../ko/notes/06-ros2-foundations.md) · [fi](../../fi/notes/06-ros2-foundations.md) · [pl](../../pl/notes/06-ros2-foundations.md)

**Hier verwendete Einheiten (vor den Beispielen erklärt):** `m` — Meter; `s` — Sekunde. [Einheitenverzeichnis](../UNITS.md).

[Course index](../README.md) · [Coordinate frames](04-coordinate-frames.md) · [Jacobian](05-velocity-jacobian.md) · [Docker lab](../../../ros2/README.md)

> **Safety:** Nur synthetisches Software-Lernbeispiel. Nicht zur Steuerung realer Roboter oder Maschinen verwenden. ROS-Kommunikation ersetzt weder Kinematik, Echtzeitregelung noch Hardware-Sicherheitsfunktionen.

ROS 2 (Robot Operating System 2) verbindet verteilte Softwarekomponenten von Robotern. Für Backend-Entwickler ähnelt ein Node einem Prozess, ein Topic einem typisierten Ereignisstrom und ein Service einem RPC. Anders als bei gewöhnlichen Brokern erfolgt die Erkennung typischerweise dezentral über DDS.

![ROS 2 publisher and subscriber connected by a typed topic; a CLI client calls a service](../../../assets/figures/ros2-topic-service.svg)

![ROS-2-Softwareschichten und getrennte Hardware-/Sicherheitsgrenze](../../../assets/figures/ros2-software-layers.svg)

*Middleware ersetzt weder zeitkritische Gerätesteuerung noch unabhängige Sicherheitsfunktionen.*

## Lernpfad

1. [Architektur, Middleware und ROS Graph](#section-1)
2. [Nodes, Topics und typisierte Messages](#section-2)
3. [Services, Actions und Parameters](#section-3)
4. [Packages, Workspaces, colcon und ament](#section-4)
5. [ROS 2 CLI zur Diagnose](#section-5)
6. [Launch-Dateien](#section-6)
7. [tf2 und Koordinatenrahmen](#section-7)
8. [URDF und robot_state_publisher](#section-8)
9. [ros2_control und Hardwaregrenze](#section-9)
10. [QoS, DDS Discovery und Docker](#section-10)
11. [Praxis: zwei Nodes, Topic, Service und Launch](#section-11)
12. [Glossar und Grenzen](#section-12)

<a id="section-1"></a>

## 1. Architektur, Middleware und ROS Graph

**Problem:** Kamera, Lokalisierung und Planung brauchen unabhängige Schnittstellen. ROS 1 nutzte einen zentralen Master zur Namensauflösung; ROS 2 verwendet die RMW-Abstraktion und meist DDS/RTPS, um Teilnehmer ohne ROS-1-Master zu finden. Der ROS Graph zeigt entdeckte Nodes, Topics, Services und Actions. Nodes sind logische Einheiten, mehrere können sich einen Prozess teilen; Prozesse können auf verschiedene Rechner verteilt sein. Discovery ist keine Zugriffskontrolle.

<a id="section-2"></a>

## 2. Nodes, Topics und typisierte Messages

**Problem:** Messwerte an mehrere Verbraucher übertragen, ohne ständig abzufragen. Ein Publisher sendet typisierte Nachrichten an ein Topic; Subscriber empfangen sie asynchron. std_msgs/msg/String besitzt das Feld string data und ist sprachunabhängig definiert. /sample_source sendet auf /training/status, /sample_monitor empfängt und zählt. Queue-Tiefe 10 bedeutet keine dauerhafte Speicherung; neue Abonnenten erhalten normalerweise spätere Nachrichten.

**Beispiel zum Discovery-Ablauf:** Angenommen, `/sample_source` veröffentlicht bereits `sample 1`, bevor `/sample_monitor` entdeckt wurde. Bei der im Labor verwendeten `volatile`-Historie wird diese frühere Nachricht nicht automatisch nachgeliefert. Der Monitor kann zunächst `received 0 samples` melden, obwohl der Publisher weiter arbeitet. Nach der Entdeckung kompatibler Endpunkte kann die Anzahl steigen. Gesendete Sequenznummer und empfangene Anzahl messen Unterschiedliches; beides ist keine Transaktionsbestätigung.

**Was die CLI tatsächlich zeigt:** `ros2 topic list -t` listet entdeckte Topic-Namen und Nachrichtentypen, **nicht** erfolgreiche Zustellung an Subscriber. `ros2 topic info /training/status -v` zeigt gefundene Endpunkte und angebotene/angeforderte QoS. Null Subscribers bedeuten entweder, dass keiner läuft, **oder** dass Discovery noch nicht abgeschlossen ist. Sind Endpunkte sichtbar, kommen aber keine Daten an, prüfe Typ, QoS, Prozesslogs und `ROS_DOMAIN_ID`. Dies sind Momentaufnahmen, keine Zustellgarantie. Die Befehle gehören in den Laborcontainer.

<a id="section-3"></a>

## 3. Services, Actions und Parameters

**Problem:** Datenstrom, kurze Abfrage und lange Aufgabe unterscheiden. Ein Service bietet Request/Response: /training/count verwendet std_srvs/srv/Trigger und liefert success und message. Actions besitzen Goal, Feedback, Result und Cancel, zum Beispiel für Navigation. Parameter gehören zu einzelnen Nodes: interval_s=1.0 legt den Timer bei Start fest. Eine spätere Parameteränderung erzeugt nicht von selbst einen neuen Timer. Für Wiederholungen von Service-Aufrufen muss die Anwendung Idempotenz beachten.

Die Wahl hängt von Antwort, Laufzeit und Fehlerfällen ab. Die Schnittstellen sind nicht austauschbar:

| Mechanismus | Ablauf | Geeignet für | Nicht verwechseln mit |
| --- | --- | --- | --- |
| Topic | Publisher → 0..N Subscriber | Laufende Telemetrie | Dauerhaftem Protokoll oder bestätigter Transaktion |
| Service | Anfrage → Antwort | Kurze Abfrage oder begrenzte Aufgabe | Garantiertem Commit oder langer Aufgabe |
| Action | Ziel → Feedback/Ergebnis, optional Abbruch | Lange Navigation oder Berechnung | Periodischem Sensorstream |
| Parameter | Wert eines Nodes | Konfiguration wie `interval_s` | Globaler verteilter Konfigurationsdatenbank |

Im Beispiel ist `/training/status` ein Topic, `/training/count` ein Service und `interval_s` ein Node-Parameter; eine Action ist nicht implementiert. Ein Timeout beim Service beweist nicht, dass der Server nichts getan hat. Wiederholungen benötigen eine zur Anwendung passende Strategie.

<a id="section-4"></a>

## 4. Packages, Workspaces, colcon und ament

**Problem:** Abhängigkeiten und ausführbare Komponenten reproduzierbar bauen. Ein Package besitzt package.xml, Python-Pakete nutzen ament_python und setup.py; C++ häufig ament_cmake. Der Workspace umfasst src, build, install und log. colcon steuert den Build; ament ist kein Nachrichtentransport. Zuerst ROS-Underlay sourcen, danach den Workspace-Overlay. telemetry_demo installiert zwei Entry Points und eine Launch-Datei.

In der tatsächlichen Datei `ros2/Dockerfile` sind **Image-Build** (`RUN`) und **Containerstart** (`CMD`) getrennte Phasen. Beim Build wird nur das ROS-Underlay geladen, bevor `colcon` das Paket baut:

**Image-Build (`RUN`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
colcon build --packages-select telemetry_demo
```

**Containerstart (`CMD`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
source /opt/training_ws/install/setup.bash
exec ros2 launch telemetry_demo demo.launch.py
```

Beim Containerstart lädt eine neue Shell das Underlay **erneut**, dann den Workspace-Overlay und startet die Launch-Datei. `package.xml` deklariert Abhängigkeiten; `setup.py` installiert die Python-Einstiegspunkte und die Launch-Datei. `build/` und `install/` sind erzeugte Artefakte und kein Platz für Quellcodeänderungen. Ein erfolgreicher Build beweist noch keine Laufzeitbereitschaft.

<a id="section-5"></a>

## 5. ROS 2 CLI zur Diagnose

**Problem:** das tatsächliche verteilte System verstehen. ros2 node list/info zeigt Nodes, topic list/info/echo zeigt Streams, interface show die Datentypen; service list/call, action list und param get prüfen weitere Endpunkte. Im Labor erscheinen /sample_source und /sample_monitor, Topic /training/status und Service /training/count. Keine eigene Action ist implementiert. Leere Ergebnisse können von QoS-Konflikten oder einer abweichenden ROS_DOMAIN_ID kommen.

CLI-Befehle nach dem Sourcen im laufenden Container:

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

## 6. Launch-Dateien

**Problem:** mehrere Prozesse konsistent starten. demo.launch.py liefert LaunchDescription mit zwei launch_ros.actions.Node-Einträgen und setzt interval_s=1.0. Launch unterstützt Argumente, Namensräume, Remapping und inkludierte Dateien. Starten ist keine Readiness-Garantie: Discovery, Retries und Fehlerbehandlung gehören zur Anwendung.

**Bereitschaft beobachten statt annehmen:** `launch_ros.actions.Node` startet zwei **Prozesse**, aber die DDS-Entdeckung und das erste `/training/status`-Sample finden erst danach statt. Ein sofortiger Aufruf von `/training/count` kann gültig `received 0 samples` liefern; später steigt der Zähler. Das beweist keinen Transaktionsverlust: Der Service zählt nur vom Monitor empfangene Samples. `interval_s=1.0` gilt beim Erstellen des Publisher-Timers und passt einen laufenden Timer nicht automatisch an.

<a id="section-7"></a>

## 7. tf2 und Koordinatenrahmen

**Problem:** Kamerakoordinaten in base_link oder map umrechnen. tf2 verwaltet zeitgestempelte Transformationen mit Drehung und Verschiebung; feste Montagen verwenden statische, Gelenke dynamische Transformationen. Eltern-Kind-Beziehungen und Zeitstempel müssen stimmen. tf2 berechnet weder automatisch Vorwärts-/Inverse Kinematik noch Bewegungsplanung. Mathematische Grundlagen stehen in den verlinkten Frame- und Jacobian-Kapiteln.

[Coordinate frames](04-coordinate-frames.md) · [Velocity and Jacobian](05-velocity-jacobian.md)

**Beispiel für eine Frame-Kette (keine vorgeschriebene Struktur):** `map → odom → base_link → camera_link`. Eine fest montierte Kamera hat eine `static`-Transformation zum Grundkörper; der bewegte Grundkörper benötigt `dynamic`-Transformationen. Um einen zum Zeitpunkt *t* in `camera_link` gemessenen Punkt in `map` zu beschreiben, muss tf2 die Transformationen **für genau diesen Messzeitpunkt** finden. Fehlt ein Frame, ist die Baumstruktur unterbrochen oder liegt *t* außerhalb der verfügbaren Daten, entsteht ein Lookup-/Extrapolationsfehler. Die neueste statt der zeitlich passenden Transformation kann falsche Koordinaten liefern.

**Beispiel zur Transformationsrichtung und Umkehrung.** `base_link` (B) ist der Elternrahmen, `tool` (T) der Kindrahmen. Ohne relative Drehung und mit 0.1 m Verschiebung entlang der positiven X-Achse des Elternrahmens liegt der Werkzeugursprung **aus Sicht von B vor dem Basisursprung**. Aus Sicht von T hat derselbe Abstand das umgekehrte Vorzeichen:

$$
{}^{B}\mathbf p_{T}=(0.1, 0, 0)\ \mathrm{m},\qquad
{}^{T}\mathbf p_{B}=(-0.1, 0, 0)\ \mathrm{m}\quad (R=I).
$$

Nur bei **gleicher Orientierung** der Achsen genügt das Negieren der Verschiebung. Allgemein setzt sich eine Punkttransformation aus Drehung und Translation zusammen. Die inverse Transformation muss **beides** umkehren; für eine echte Rotationsmatrix ist $R^T$ die Inverse:

$$
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT},\qquad
\mathbf p_T=R_{BT}^{T}(\mathbf p_B-\mathbf t_{BT}),\qquad
\mathbf t_{TB}=-R_{BT}^{T}\mathbf t_{BT}.
$$

Für eine andere Pose drehe T um +90° um die gemeinsame Z-Achse; die Verschiebung in B bleibt (0.1 m, 0 m). Der Ursprung von B liegt dann in T bei (0 m, +0.1 m), **nicht** bei (−0.1 m, 0 m). Mit diesen Matrizen lässt sich auch ein Punkt (0 m, 0.05 m) aus T nach B umrechnen:

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

Koordinatenrahmen und Transformationen **beschreiben Positionen**, sie geben keine Motorbefehle. In ROS 2 werden Translationen üblicherweise in Metern angegeben; die eigenständige [Koordinatenlektion](04-coordinate-frames.md#section-3) verwendet Millimeter und muss vor einem Vergleich umgerechnet werden. Statische Transformationen beschreiben feste Montagen, dynamische stammen von Komponenten mit Zustandsinformationen. Historische Messungen müssen mit Transformationen zum Messzeitpunkt ausgewertet werden.

<a id="section-8"></a>

## 8. URDF und robot_state_publisher

**Problem:** ein gemeinsames Strukturmodell des Roboters bereitstellen. URDF beschreibt Links, Joints, Achsen, Ursprünge und optionale visuelle, Kollisions- und Trägheitseigenschaften. robot_state_publisher erzeugt aus URDF und Gelenkzuständen (typisch /joint_states vom Typ sensor_msgs/msg/JointState) Frame-Transformationen. URDF liefert keine Sensormessung, Simulation oder IK-Lösung. Meter, Radiant und Achskonventionen beachten.

**Herkunft der Transformationen:** URDF beschreibt `fixed`- und bewegliche Joints. `robot_state_publisher` nutzt die Geometrie fester Joints für `static`-Transformationen und die auf `/joint_states` gelieferten Gelenkpositionen (`sensor_msgs/msg/JointState`) für `dynamic`-Transformationen beweglicher Joints. URDF **misst keine Gelenkpositionen** und erzeugt keine fehlenden Messdaten. Längen in Metern, Winkel in Radiant und Zeitstempel müssen übereinstimmen.

<a id="section-9"></a>

## 9. ros2_control und Hardwaregrenze

**Problem:** Regelungslogik von Gerätetreibern trennen. ros2_control umfasst Controller Manager, State Interfaces (Position/Geschwindigkeit), Command Interfaces (Position/Geschwindigkeit/Effort) und Hardwareabstraktionen. Planer → Controller → Hardwareinterface → Anlage, mit Rückführung der Zustände. Eine ROS-Nachricht garantiert keine harte Echtzeit, keine Strombegrenzung und kein sicheres Stoppen. Das Labor nutzt keine Aktuatoren.

[First-order dynamics](02-first-order-dynamics.md) · [Feedback PID](03-feedback-control.md)

**Aufgabe des Controller Managers:** `controller_manager` verwaltet den Lebenszyklus der Controller und über den Resource Manager deren Zugriff auf State Interfaces und Command Interfaces. Ein Controller kann einen gemessenen Zustand, etwa das beispielhafte `joint1/position`, lesen. Ein aktiver Controller kann ein passendes Command Interface beanspruchen, um einen Sollwert zu schreiben. Istwert und Sollwert sind nicht dasselbe; mehrere Controller dürfen ein bereits belegtes Command Interface nicht beliebig gleichzeitig beanspruchen. Controller-Aktivierung und Ressourcenbelegung sind deshalb mehr als ROS-Topic-Discovery.

**Grenze dieses Labors:** `/training/status` und `/training/count` zeigen lediglich Topic und Service, **nicht `ros2_control`**. Keiner der beiden Nodes ist ein Controller; das Labor verwendet weder `controller_manager` noch Hardware Interface oder geschlossenen Regelkreis. Der erfolgreiche Smoke-Test prüft weder Controller-Lebenszyklus noch Echtzeitverhalten oder Gerätesicherheit. Siehe die [offizielle ros2_control-Einführung](https://control.ros.org/jazzy/doc/getting_started/getting_started.html).

**Praxislabor: ros2_control und TF2 ohne GUI mit virtuellem Gelenk:** [Praxislabor: ros2_control und TF2 ohne GUI mit virtuellem Gelenk](07-ros2-control-lab.md). Das neue Labor erklärt URDF, GenericSystem, Befehle, Zustände, /joint_states, TF2, QoS und die ARM64-Loaderdiagnose; es steuert keine echte Hardware.

**Nächster Schritt: Roboterarchitektur.** Das [editierbare Mermaid-Diagramm mit fünf Stufen](08-ros2-robot-architecture.md) verbindet Wahrnehmung, zeitbezogenes TF2, Planung, Steuerung und Rückmeldung. Die Hardwarekette bleibt konzeptionell.

<a id="section-10"></a>

## 10. QoS, DDS Discovery und Docker

**Problem:** verlorene Nachrichten und unsichtbare Knoten verstehen. QoS umfasst reliable/best_effort, volatile/transient_local sowie History und Depth. Verlangt ein Subscriber mehr als ein Publisher anbieten kann, fließen keine Daten. DDS verwendet häufig UDP-Multicast und dynamische Ports; Docker Desktop, VPN und Firewalls beeinflussen Discovery. ROS_DOMAIN_ID muss passen. Alles läuft hier in einem Container ohne Host-Ports oder Privilegien; das beweist keine Rechner-übergreifende Kommunikation.

**Beispiel für inkompatible QoS:** Bietet ein Publisher nur `best_effort` an, während ein Subscriber `reliable` verlangt, können Topic-Name und Nachrichtentyp übereinstimmen und Endpunkte sichtbar sein, ohne dass der Subscriber **Nachrichten empfängt**. Umgekehrt kann ein `best_effort`-Subscriber einen `reliable`-Publisher nutzen, wenn die übrigen QoS-Richtlinien kompatibel sind. `volatile` liefert keine historischen Nachrichten; `transient_local` kann eine begrenzte Historie eines verfügbaren kompatiblen Publishers anbieten, ist aber **kein dauerhaftes verteiltes Log**.

**Diagnose in Reihenfolge:** Innerhalb desselben Containers `ROS_DOMAIN_ID=42` prüfen, dann `ros2 node list`, `ros2 topic info /training/status -v` für Endpunkte und QoS sowie `docker compose logs demo` für den Prozesszustand ausführen. Bei leerem Graphen RMW/DDS, Netzwerkschnittstellen und Firewall prüfen. Das Freigeben von TCP-Ports löst DDS-Probleme nicht allgemein; Kommunikation zwischen Rechnern ist hier nicht getestet.

[Offizielle ROS 2 Jazzy-Dokumentation zu QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)

[Alternative: offizielles ROS-Image ohne Compose oder eigenes Dockerfile](../../../ros2/PLAIN_DOCKER.md)

<a id="section-11"></a>

## 11. Praxis: zwei Nodes, Topic, Service und Launch

docker compose up --build -d startet die Simulation. Logs sollten veröffentlichte und empfangene Samples zeigen; der Zähler wächst mit der Zeit. Der Service liefert success=True und beispielsweise received 12 samples, abhängig vom Startzeitpunkt. Ein [separater Docker-Smoke-Test in GitHub Actions](../../../.github/workflows/ros2-live-smoke.yml) hat die Anwendung tatsächlich **in einem Container** gestartet: beide ROS-Nodes, eine typisierte Nachricht auf `/training/status` und die Antwort von `/training/count` wurden geprüft. Der normale Validierungsjob führt ROS nicht aus. Weder dieser Test noch die normalen Prüfungen belegen DDS zwischen Rechnern, deterministisches Timing, reale Hardware oder die Docker-Installation des Lesers.

[Complete source, expected results and diagnostics](../../../ros2/README.md). From the repository root:

Für eine sinnvolle Lernreihenfolge zuerst den installierten `demo_nodes_cpp`-Talker mit `demo_nodes_py`-Listener starten, dann das eigene Paket `telemetry_demo` untersuchen und erst danach `ros2_control`. Das Dockerfile installiert die Standarddemos per APT und baut `telemetry_demo` mit `colcon`. Für interaktive Befehle **eine Bash-Shell** öffnen und die ROS-Umgebungen **einmal pro neuer Shell** laden: Ein eigenes `docker compose exec` erbt nicht die Shell-Umgebung des Container-`CMD`.

Auf dem Host den Container starten und eine interaktive Shell öffnen:

```bash
cd ros2
docker compose up --build -d
docker compose logs --tail=20 demo
docker compose exec demo bash
```

Im Container (nicht auf dem Host) die Umgebungen einmal laden und den Graph untersuchen:

```bash
echo "$ROS_DISTRO"
ros2 node list
ros2 service call /training/count std_srvs/srv/Trigger "{}"
exit
```

Nach `exit` wieder auf dem Host aufräumen:

```bash
docker compose down
```

**CI-Vertrauensgrenze:** Der echte ROS-2-Docker-Smoke-Test startet nun automatisch nur nach Änderungen auf `main`, oder manuell über `workflow_dispatch` auf `main`. Für eingehende `pull_request`-Änderungen läuft er absichtlich **nicht**, da der Host-Runner sonst vom PR veränderte Bash-Skripte und Dockerfiles direkt ausführen würde. Die isolierten Python-Prüfungen vor dem Merge ersetzen keinen laufenden ROS-Test. Änderungen vorher unabhängig prüfen und das Live-Ergebnis nach dem Merge kontrollieren.

<a id="section-12"></a>

## 12. Glossar und Grenzen

- **Node / Prozess:** Ein Node ist eine benannte logische ROS-Einheit; ein Betriebssystemprozess kann mehrere Nodes enthalten.
- **ROS graph:** Aktuell entdeckte Kommunikationsteilnehmer und Endpunkte, keine zentrale Registry oder Zugriffskontrolle.
- **Topic:** Benannter asynchroner Stream mit mehreren möglichen Publishern und Subscribern.
- **Message:** Typisierte Datenstruktur aus einer ROS-Schnittstellendefinition, kein beliebiges Python- oder C++-Objekt.
- **Publisher / Subscriber:** Sender und Empfänger von Topic-Nachrichten; Discovery und kompatible QoS sind für die Zustellung nötig.
- **Service:** Typisierte kurze Anfrage/Antwort; ein Timeout beweist nicht, dass der Server nichts ausgeführt hat.
- **Action:** Ziel mit Feedback, Ergebnis und Abbruchanfrage; eine Abbruchanfrage garantiert keinen sofortigen Stopp.
- **Parameter:** Wert eines einzelnen Nodes; seine Änderung konfiguriert einen laufenden Timer nicht automatisch neu.
- **RMW / DDS:** RMW abstrahiert die Middleware; DDS ist eine häufige Discovery-/Transporttechnik, keine eigene Authentifizierung.
- **colcon / ament:** Workspace-Build-Orchestrierung / ROS-Paket-Build-Integration, kein Nachrichtentransport.
- **Launch:** Beschreibung zu startender Prozesse und Konfiguration; Start bedeutet nicht Bereitschaft.
- **tf2:** Zeitgestempelte Koordinatentransformationen, kein Inverskinematik-Solver.
- **URDF / robot_state_publisher:** Robotermodell / Transform-Publikation aus Modell und aktuellen Gelenkzuständen.
- **ros2_control:** Controller-Lebenszyklus und verwaltete State-/Command-Interfaces; nicht Teil dieses Topic/Service-Labors.
- **QoS:** Kompatibilität, Zustellung und Verlaufsrichtlinien, weder dauerhaftes Eventlog noch Sicherheitszertifizierung.

**Versionsstand (13.11.2026):** ROS 2 Jazzy LTS wird bis Mai 2029, Lyrical LTS bis Mai 2031 unterstützt. Das verwendete Docker-Tag legt keinen unveränderlichen Image-Digest oder feste apt-Paketversionen fest.

**Primary sources:** [ROS 2 releases](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst) · [Jazzy documentation](https://docs.ros.org/en/jazzy/) · [tf2](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html) · [URDF](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html) · [ros2_control](https://control.ros.org/jazzy/)
