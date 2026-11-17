# 6. ROS 2: software robotico distribuito e interfacce

**Languages:** [en](../../en/notes/06-ros2-foundations.md) · [fr](../../fr/notes/06-ros2-foundations.md) · [de](../../de/notes/06-ros2-foundations.md) · [it](06-ros2-foundations.md) · [es](../../es/notes/06-ros2-foundations.md) · [pt](../../pt/notes/06-ros2-foundations.md) · [zh](../../zh/notes/06-ros2-foundations.md) · [ja](../../ja/notes/06-ros2-foundations.md) · [nb](../../nb/notes/06-ros2-foundations.md) · [ru](../../ru/notes/06-ros2-foundations.md) · [ko](../../ko/notes/06-ros2-foundations.md) · [fi](../../fi/notes/06-ros2-foundations.md) · [pl](../../pl/notes/06-ros2-foundations.md)

**Unità usate qui (spiegate prima degli esempi):** `m` — metro; `s` — secondo. [Glossario delle unità](../UNITS.md).

[Course index](../README.md) · [Coordinate frames](04-coordinate-frames.md) · [Jacobian](05-velocity-jacobian.md) · [Docker lab](../../../ros2/README.md)

> **Safety:** Solo modello didattico sintetico: non usare comandi o codice per controllare robot o macchine reali. La comunicazione ROS non sostituisce cinematica, controllo real-time e sicurezza hardware.

ROS 2 (Robot Operating System 2) collega componenti software distribuiti di un robot. Per chi sviluppa backend, un node assomiglia a un processo, un topic a uno stream di eventi tipizzati, un service a una RPC. L'analogia non è esatta: la scoperta usa normalmente DDS senza obbligo di un broker centrale.

![ROS 2 publisher and subscriber connected by a typed topic; a CLI client calls a service](../../../assets/figures/ros2-topic-service.svg)

![Livelli software ROS 2 e confine della sicurezza hardware](../../../assets/figures/ros2-software-layers.svg)

*Il middleware non sostituisce il controllo a basso livello o le protezioni indipendenti.*

## Percorso di apprendimento

1. [Architettura, middleware e ROS graph](#section-1)
2. [Nodes, topics e messaggi tipizzati](#section-2)
3. [Services, actions e parameters](#section-3)
4. [Packages, workspaces, colcon e ament](#section-4)
5. [Ispezione con ROS 2 CLI](#section-5)
6. [Launch files](#section-6)
7. [tf2 e coordinate frames](#section-7)
8. [URDF e robot_state_publisher](#section-8)
9. [ros2_control e confine hardware](#section-9)
10. [QoS, discovery DDS e Docker](#section-10)
11. [Laboratorio: publisher, subscriber, service e launch](#section-11)
12. [Glossario e limitazioni](#section-12)

<a id="section-1"></a>

## 1. Architettura, middleware e ROS graph

**Problema:** sensori, localizzazione e pianificazione devono comunicare senza diventare un unico programma. ROS 1 usava un master centrale per la scoperta dei nomi; ROS 2 usa l'astrazione RMW e di norma DDS/RTPS per scoprire i partecipanti senza quel master. Il ROS graph comprende node, topic, service e action rilevati. I node sono componenti logici; più node possono condividere un processo e processi diversi possono stare su computer differenti. Discovery non equivale ad autorizzazione.

<a id="section-2"></a>

## 2. Nodes, topics e messaggi tipizzati

**Problema:** distribuire misure continue a più consumatori. Un publisher invia messaggi tipizzati a un topic; i subscriber ricevono in modo asincrono. std_msgs/msg/String contiene un campo string data e definisce un contratto comune a Python e C++. /sample_source pubblica su /training/status; /sample_monitor riceve e conta i messaggi. Una coda con depth 10 non è un archivio persistente; i nuovi subscriber ricevono normalmente solo messaggi successivi.

**Esempio di discovery:** supponiamo che `/sample_source` abbia pubblicato `sample 1` prima che `/sample_monitor` sia stato scoperto. Con la cronologia `volatile` usata qui, il messaggio precedente non viene riprodotto automaticamente. Il monitor può inizialmente rispondere `received 0 samples` mentre il publisher continua a inviare. Il conteggio può crescere dopo la scoperta degli endpoint compatibili. Numero di sequenza pubblicato e numero di messaggi ricevuti misurano cose diverse; nessuno dei due è una conferma di transazione.

**Cosa dimostra la CLI:** `ros2 topic list -t` mostra nomi e tipi dei topic scoperti, **non** prova la consegna ai subscriber. `ros2 topic info /training/status -v` mostra endpoint scoperti e QoS offerte/richieste. Zero subscriber può significare che non ce ne sono **oppure** che discovery non è terminata. Se gli endpoint risultano visibili ma non arrivano dati, controllare compatibilità dei tipi, QoS, log e `ROS_DOMAIN_ID`. Sono istantanee, non garanzie di consegna. Eseguire i comandi nel container del laboratorio.

<a id="section-3"></a>

## 3. Services, actions e parameters

**Problema:** distinguere stream, richiesta breve e operazione lunga. Un service esegue request/response; /training/count con std_srvs/srv/Trigger restituisce success e message. Un action offre goal, feedback, result e cancel per attività come navigazione. Un parametro appartiene al node: interval_s=1.0 configura il timer alla partenza. Modificare il parametro non ricrea automaticamente il timer. Retry e idempotenza sono responsabilità applicative.

La scelta dipende dal tipo di risposta, dalla durata e dalle condizioni di errore. Le interfacce non sono intercambiabili:

| Meccanismo | Flusso | Impiego adatto | Da non confondere con |
| --- | --- | --- | --- |
| Topic | Publisher → 0..N subscriber | Telemetria continua | Registro persistente o transazione confermata |
| Service | Richiesta → risposta | Query breve o operazione limitata | Commit garantito o compito lungo |
| Action | Obiettivo → feedback/risultato, annullamento opzionale | Navigazione o calcolo lungo | Stream periodico del sensore |
| Parameter | Valore gestito dal nodo | Configurazione, come `interval_s` | Database globale e condiviso |

Nel laboratorio `/training/status` è un topic, `/training/count` è un service e `interval_s` è un parametro del nodo; non è implementata alcuna action. Un timeout non prova che il server non abbia eseguito la richiesta: l'eventuale ripetizione dipende dalla semantica dell'operazione.

<a id="section-4"></a>

## 4. Packages, workspaces, colcon e ament

**Problema:** costruire componenti e dipendenze in modo ripetibile. package.xml descrive un package; ament_python e ament_cmake integrano il sistema di build. Un workspace contiene in genere src, build, install e log. colcon coordina la compilazione: non trasporta messaggi. Prima si carica l'underlay ROS, poi l'overlay del workspace. Il package telemetry_demo usa setup.py per due eseguibili e installa un launch file.

Nel vero `ros2/Dockerfile`, **build dell'immagine** (`RUN`) e **avvio del container** (`CMD`) sono fasi distinte. Durante il build viene caricato solo l'underlay ROS prima di compilare con `colcon`:

**Build dell'immagine (`RUN`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
colcon build --packages-select telemetry_demo
```

**Avvio del container (`CMD`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
source /opt/training_ws/install/setup.bash
exec ros2 launch telemetry_demo demo.launch.py
```

All'avvio una nuova shell carica **di nuovo** l'underlay, poi l'overlay del workspace e avvia il launch file. `package.xml` dichiara le dipendenze; `setup.py` installa gli entry point Python e il launch file. `build/` e `install/` sono prodotti generati, non directory per modificare i sorgenti. Un build riuscito non dimostra che l'applicazione sia pronta.

<a id="section-5"></a>

## 5. Ispezione con ROS 2 CLI

**Problema:** verificare ciò che è realmente attivo. ros2 node list/info elenca i node; topic list/info/echo analizza i flussi; interface show controlla il tipo; service list/call, action list e param get mostrano altri endpoint. Nel demo compaiono /sample_source, /sample_monitor, /training/status e /training/count. Non è presente un action applicativo. Per dati mancanti controllare anche QoS e ROS_DOMAIN_ID.

Comandi CLI nel container dopo aver caricato l'ambiente ROS:

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

## 6. Launch files

**Problema:** avviare processi e parametri coerenti. demo.launch.py crea una LaunchDescription con due launch_ros.actions.Node e imposta interval_s=1.0. I launch possono includere argomenti, namespace, remapping e altri file. L'avvio non assicura immediata disponibilità: discovery, readiness e retry sono aspetti separati.

**Verificare la disponibilità:** `launch_ros.actions.Node` avvia due **processi**, ma la scoperta DDS e il primo sample di `/training/status` avvengono dopo. Una chiamata immediata a `/training/count` può legittimamente restituire `received 0 samples`; in seguito il contatore può crescere. Non prova la perdita di una transazione: il servizio conta solo i messaggi ricevuti dal monitor. `interval_s=1.0` viene letto alla creazione del timer e non ne modifica automaticamente il periodo durante l'esecuzione.

<a id="section-7"></a>

## 7. tf2 e coordinate frames

**Problema:** trasformare una misura da camera_link a base_link o map. tf2 archivia e interroga trasformazioni con timestamp, rotazione e traslazione. Le connessioni fisse usano transform statici; i giunti mobili richiedono dati dinamici. Albero padre-figlio e tempi devono essere coerenti. tf2 non calcola direttamente cinematica inversa, diretta o planning: vedere le lezioni di coordinate e Jacobiano.

[Coordinate frames](04-coordinate-frames.md) · [Velocity and Jacobian](05-velocity-jacobian.md)

**Esempio di catena dei frame (non obbligatoria):** `map → odom → base_link → camera_link`. Una camera fissata rigidamente al corpo usa una trasformazione `static`; il movimento della base richiede trasformazioni `dynamic`. Per esprimere in `map` un punto osservato in `camera_link` al tempo *t*, tf2 deve trovare l'intera catena **al tempo della misura**. Frame mancanti, un albero disconnesso o tempi non disponibili causano errori di lookup/extrapolation; la trasformazione più recente può essere sbagliata per una misura storica.

**Esempio del verso di trasformazione e del suo inverso.** Sia `base_link` (B) il frame padre e `tool` (T) il frame figlio. Senza rotazione relativa, una traslazione di 0.1 m lungo l'asse X positivo del padre significa che l'origine dell'utensile è **davanti all'origine della base in B**. Visto da T, lo stesso spostamento ha segno opposto:

$$
{}^{B}\mathbf p_{T}=(0.1, 0, 0)\ \mathrm{m},\qquad
{}^{T}\mathbf p_{B}=(-0.1, 0, 0)\ \mathrm{m}\quad (R=I).
$$

Questo semplice cambio di segno vale solo se i frame hanno **la stessa orientazione**. In generale, una trasformazione combina rotazione e traslazione. Per invertirla occorre invertire **entrambe**; per una matrice di rotazione propria, l'inversa è $R^T$:

$$
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT},\qquad
\mathbf p_T=R_{BT}^{T}(\mathbf p_B-\mathbf t_{BT}),\qquad
\mathbf t_{TB}=-R_{BT}^{T}\mathbf t_{BT}.
$$

In un'altra posa, T è ruotato di +90° sull'asse Z comune, mantenendo la traslazione (0.1 m, 0 m) in B. L'origine di B espressa in T è allora (0 m, +0.1 m), **non** (−0.1 m, 0 m). Le stesse matrici portano il punto (0 m, 0.05 m) da T a B:

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

Frame e trasformazioni **descrivono coordinate**, non impartiscono comandi al motore. In ROS 2 le traslazioni usano convenzionalmente i metri; la [lezione sui sistemi di coordinate](04-coordinate-frames.md#section-3) utilizza millimetri e richiede conversione prima di combinare i valori. Le trasformazioni statiche descrivono montaggi fissi; quelle dinamiche provengono da componenti con stati aggiornati. Per misure storiche usare il timestamp della misura e gestire eventuali dati non disponibili.

<a id="section-8"></a>

## 8. URDF e robot_state_publisher

**Problema:** descrivere la struttura meccanica in modo condiviso. URDF rappresenta link, joint, origini, assi e proprietà opzionali visual, collision e inertial. robot_state_publisher usa URDF e le posizioni dei giunti, tipicamente da /joint_states (sensor_msgs/msg/JointState), per pubblicare transform. URDF non legge encoder, non simula e non risolve la cinematica inversa. Attenzione a metri, radianti e convenzioni.

**Da dove arrivano le trasformazioni:** URDF definisce joint `fixed` e mobili. `robot_state_publisher` pubblica trasformazioni `static` per la geometria fissa e calcola trasformazioni `dynamic` per i joint mobili usando le posizioni su `/joint_states` (`sensor_msgs/msg/JointState`). URDF **non misura** le posizioni dei joint e non ricostruisce misure mancanti. Dimensioni in metri, angoli in radianti e timestamp devono essere coerenti.

<a id="section-9"></a>

## 9. ros2_control e confine hardware

**Problema:** separare controllori e driver. ros2_control fornisce controller manager, state interface (posizione/velocità), command interface (posizione/velocità/effort) e astrazioni hardware. Il planner invia riferimenti, il controllore usa lo stato e l'interfaccia dialoga con il dispositivo. Messaggi ROS non garantiscono timing deterministico, limiti di corrente o arresto sicuro. Nessun attuatore è collegato al demo.

[First-order dynamics](02-first-order-dynamics.md) · [Feedback PID](03-feedback-control.md)

**Ruolo del controller manager:** `controller_manager` gestisce il ciclo di vita dei controller e, tramite il resource manager, l'accesso alle interfacce di stato (state interfaces) e di comando (command interfaces). Un controller può leggere uno stato misurato, per esempio l'ipotetico `joint1/position`; un controller attivo può acquisire un'interfaccia di comando compatibile per scrivere il valore richiesto. La misura non coincide con il comando e due controller non possono acquisire liberamente la stessa interfaccia di comando già occupata. L'attivazione e la gestione delle risorse non si riducono alla scoperta dei topic.

**Limite del laboratorio:** `/training/status` e `/training/count` mostrano un topic e un service, **non `ros2_control`**. Nessuno dei due nodi è un controller; il laboratorio non esegue `controller_manager`, non espone interfacce hardware e non chiude un anello di controllo. Il smoke test non verifica il ciclo di vita dei controller, i tempi real-time o la sicurezza dei dispositivi. Vedi [introduzione ufficiale a ros2_control](https://control.ros.org/jazzy/doc/getting_started/getting_started.html).

**Esercizio pratico: ros2_control e TF2 senza GUI con giunto virtuale:** [Esercizio pratico: ros2_control e TF2 senza GUI con giunto virtuale](07-ros2-control-lab.md). Il nuovo laboratorio tratta URDF, GenericSystem, comandi, stati, /joint_states, TF2, QoS e diagnosi del loader ARM64; non controlla dispositivi reali.

**Passo successivo: architettura del robot.** Il [diagramma Mermaid ROS 2 in cinque fasi](08-ros2-robot-architecture.md) collega percezione, TF2 con timestamp, pianificazione, controllo e retroazione. Il percorso hardware resta concettuale.

<a id="section-10"></a>

## 10. QoS, discovery DDS e Docker

**Problema:** comprendere la compatibilità e i nodi non visibili in rete. QoS include reliable/best_effort, volatile/transient_local, history e depth. Un subscriber che richiede garanzie superiori a quelle offerte dal publisher potrebbe non ricevere dati. DDS usa spesso multicast UDP e porte dinamiche; Docker Desktop, VPN e firewall possono bloccare discovery. ROS_DOMAIN_ID deve corrispondere. Tutti i processi del laboratorio sono in un solo container senza privilegi o porte esposte.

**Esempio di QoS incompatibile:** un publisher offre `best_effort`, mentre un subscriber richiede `reliable`. Anche se nome e tipo del topic coincidono e gli endpoint sono visibili, il subscriber può **non ricevere messaggi**, perché richiede una garanzia non offerta. Viceversa, un subscriber `best_effort` può ricevere da un publisher `reliable` se le altre policy QoS sono compatibili. `volatile` non riproduce messaggi precedenti; `transient_local` può conservare una cronologia limitata presso un publisher compatibile disponibile, ma **non è un registro distribuito persistente**.

**Diagnostica in ordine:** verificare `ROS_DOMAIN_ID=42` nello stesso container, poi eseguire `ros2 node list`, `ros2 topic info /training/status -v` per endpoint e QoS e `docker compose logs demo` per i processi. Se il grafo è vuoto, controllare RMW/DDS, interfacce di rete e firewall. Esporre porte TCP non risolve in generale DDS; la comunicazione tra host non è stata verificata.

[Documentazione ufficiale ROS 2 Jazzy sulle policy QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)

[Alternativa: immagine ROS ufficiale senza Compose né Dockerfile proprio](../../../ros2/PLAIN_DOCKER.md)

<a id="section-11"></a>

## 11. Laboratorio: publisher, subscriber, service e launch

Avviare con docker compose up --build -d. Nei log dovrebbero apparire messaggi pubblicati e ricevuti; il contatore aumenta. La risposta del service contiene success=True e un testo come received 12 samples, variabile nel tempo. Un [smoke test Docker separato su GitHub Actions](../../../.github/workflows/ros2-live-smoke.yml) ha realmente avviato l'applicazione **in un solo container**, verificando entrambi i nodi ROS, un messaggio tipizzato su `/training/status` e una risposta dal servizio `/training/count`. Il normale job di validazione non esegue ROS. Questi test non verificano DDS tra più computer, temporizzazione deterministica, hardware reale o l'installazione Docker del lettore.

[Complete source, expected results and diagnostics](../../../ros2/README.md). From the repository root:

Per seguire l'ordine didattico, avvia prima il talker `demo_nodes_cpp` e il listener `demo_nodes_py` installati nell'immagine, poi esamina il pacchetto personalizzato `telemetry_demo` e infine passa a `ros2_control`. Dockerfile installa gli esempi con APT e costruisce `telemetry_demo` con `colcon`. Per lavorare interattivamente apri **una shell Bash** e carica gli ambienti **una volta per nuova shell**: un `docker compose exec` separato non eredita l'ambiente del `CMD`.

Sull'host avvia il container e apri una shell interattiva:

```bash
cd ros2
docker compose up --build -d
docker compose logs --tail=20 demo
docker compose exec demo bash
```

Dentro il container, non sull'host, carica una volta gli ambienti e osserva il grafo:

```bash
echo "$ROS_DISTRO"
ros2 node list
ros2 service call /training/count std_srvs/srv/Trigger "{}"
exit
```

Dopo `exit`, sull'host rimuovi il container:

```bash
docker compose down
```

**Confine di fiducia della CI:** il vero smoke test Docker ROS 2 ora parte automaticamente solo dopo che le modifiche arrivano su `main`, oppure con `workflow_dispatch` su `main`. Non viene eseguito sulle revisioni `pull_request`: altrimenti il runner host eseguirebbe script Bash e Dockerfile controllati dal PR. I controlli Python isolati prima del merge non sostituiscono il test ROS reale. È necessaria una revisione indipendente prima del merge e la verifica del test live dopo.

<a id="section-12"></a>

## 12. Glossario e limitazioni

- **Node / processo:** un nodo è un componente ROS logico con nome; un processo del sistema operativo può ospitare più nodi.
- **ROS graph:** insieme degli endpoint attualmente scoperti, non un registro centrale permanente né un controllo degli accessi.
- **Topic:** flusso asincrono nominato con più publisher e subscriber possibili.
- **Message:** struttura dati tipizzata definita da un'interfaccia ROS, non un oggetto Python o C++ arbitrario.
- **Publisher / subscriber:** produttore e ricevitore di messaggi; discovery e QoS compatibile precedono la consegna.
- **Service:** richiesta e risposta tipizzate per un'interazione breve; un timeout non prova che il server non abbia agito.
- **Action:** obiettivo con feedback, risultato e richiesta di annullamento; annullare non garantisce un arresto immediato.
- **Parameter:** valore appartenente a un nodo; cambiarlo non riconfigura automaticamente un timer già attivo.
- **RMW / DDS:** RMW astrae il middleware; DDS è una tecnologia comune per discovery e trasporto, non autenticazione automatica.
- **colcon / ament:** orchestrazione della build del workspace / integrazione build dei pacchetti ROS, non trasporto messaggi.
- **Launch:** descrizione di processi e configurazioni da avviare; avvio non equivale a disponibilità.
- **tf2:** infrastruttura di trasformazioni fra sistemi di coordinate con timestamp, non un risolutore di cinematica inversa.
- **URDF / robot_state_publisher:** modello strutturale del robot / pubblicazione di trasformazioni usando modello e stati dei giunti.
- **ros2_control:** ciclo di vita dei controller e interfacce state/command gestite; non implementato dal laboratorio topic/service.
- **QoS:** compatibilità e politiche di consegna/storia, non registro persistente né certificazione di sicurezza.

**Versioni verificate il 13 novembre 2026:** ROS 2 Jazzy LTS è supportato fino a maggio 2029 e Lyrical LTS fino a maggio 2031. Il tag Docker non blocca un digest immutabile dell'immagine né le versioni dei pacchetti apt.

**Primary sources:** [ROS 2 releases](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst) · [Jazzy documentation](https://docs.ros.org/en/jazzy/) · [tf2](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html) · [URDF](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html) · [ros2_control](https://control.ros.org/jazzy/)
