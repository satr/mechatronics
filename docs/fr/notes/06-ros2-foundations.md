# 6. ROS 2 : architecture distribuée et interfaces robotiques

**Languages:** [en](../../en/notes/06-ros2-foundations.md) · [fr](06-ros2-foundations.md) · [de](../../de/notes/06-ros2-foundations.md) · [it](../../it/notes/06-ros2-foundations.md) · [es](../../es/notes/06-ros2-foundations.md) · [pt](../../pt/notes/06-ros2-foundations.md) · [zh](../../zh/notes/06-ros2-foundations.md) · [ja](../../ja/notes/06-ros2-foundations.md) · [nb](../../nb/notes/06-ros2-foundations.md) · [ru](../../ru/notes/06-ros2-foundations.md) · [ko](../../ko/notes/06-ros2-foundations.md) · [fi](../../fi/notes/06-ros2-foundations.md) · [pl](../../pl/notes/06-ros2-foundations.md)

**Unités utilisées ici (définies avant les exemples):** `m` — mètre; `s` — seconde. [Glossaire des unités](../UNITS.md).

[Course index](../README.md) · [Coordinate frames](04-coordinate-frames.md) · [Jacobian](05-velocity-jacobian.md) · [Docker lab](../../../ros2/README.md)

> **Safety:** Exercice logiciel et synthétique uniquement. Aucune commande ne doit piloter un vrai robot ou une machine : la communication ROS ne remplace pas le contrôle temps réel, la cinématique ni la sûreté matérielle.

ROS 2 (Robot Operating System 2) fournit une infrastructure de communication pour des composants robotiques distribués. Pour un développeur backend, un nœud rappelle un processus, un topic un flux d'événements typés, un service un RPC. La comparaison est imparfaite : les implémentations habituelles de ROS 2 reposent sur DDS et une découverte distribuée, sans broker central obligatoire.

![ROS 2 publisher and subscriber connected by a typed topic; a CLI client calls a service](../../../assets/figures/ros2-topic-service.svg)

![Couches logicielles ROS 2 et frontière de sécurité matérielle](../../../assets/figures/ros2-software-layers.svg)

*La communication distribuée ne remplace pas les contraintes de commande et de sécurité matérielles.*

## Progression des leçons

1. [Architecture, middleware et graphe ROS](#section-1)
2. [Nœuds, topics et messages typés](#section-2)
3. [Services, actions et paramètres](#section-3)
4. [Packages, workspaces, colcon et ament](#section-4)
5. [Inspection par ROS 2 CLI](#section-5)
6. [Fichiers launch](#section-6)
7. [tf2 et repères de coordonnées](#section-7)
8. [URDF et robot_state_publisher](#section-8)
9. [ros2_control et frontière matérielle](#section-9)
10. [QoS, découverte DDS et Docker](#section-10)
11. [Exercice : publisher, subscriber, service et lancement](#section-11)
12. [Glossaire et limites](#section-12)

<a id="section-1"></a>

## 1. Architecture, middleware et graphe ROS

**Problème :** une caméra, la localisation et un planificateur doivent fonctionner indépendamment. ROS 1 utilisait un master central pour découvrir les noms; ROS 2 utilise la couche RMW et généralement DDS/RTPS pour découvrir les participants sans ce master. Le graphe ROS représente les nœuds, topics, services et actions découverts. Un nœud est logique : plusieurs nœuds peuvent partager un processus; les processus peuvent être distribués entre plusieurs machines. La découverte n'est pas une authentification.

<a id="section-2"></a>

## 2. Nœuds, topics et messages typés

**Problème :** diffuser des mesures périodiques sans interroger le producteur. Un publisher envoie des messages vers un topic et plusieurs subscribers peuvent les recevoir. Le type std_msgs/msg/String définit un champ string data, commun aux programmes Python et C++. Le producteur /sample_source publie /training/status; /sample_monitor le reçoit et compte les messages. Une profondeur de file de 10 ne crée pas d'historique persistant; un abonné tardif reçoit les futurs messages.

**Exemple du déroulement de la découverte :** imaginons que `/sample_source` publie `sample 1` avant que `/sample_monitor` soit découvert. Avec l'historique `volatile` de cet exemple, cet ancien message n'est pas rejoué automatiquement. Le moniteur peut d'abord répondre `received 0 samples`, tandis que le publisher continue de fonctionner. Le compteur peut augmenter après la découverte des endpoints compatibles. Le numéro publié et le nombre de messages reçus mesurent des choses différentes ; aucun des deux ne confirme une transaction.

**Ce que montrent les commandes CLI :** `ros2 topic list -t` affiche noms et types des topics découverts, **sans prouver la réception** par un subscriber. `ros2 topic info /training/status -v` affiche les endpoints découverts et les QoS proposées/demandées. Zéro subscriber détecté peut signifier son absence **ou** une découverte encore incomplète. Si les endpoints existent mais qu'aucune donnée n'arrive, vérifier les types, QoS, journaux des processus et `ROS_DOMAIN_ID`. Il s'agit d'instantanés, pas de garanties de livraison. Exécuter ces commandes dans le conteneur de l'exemple.

<a id="section-3"></a>

## 3. Services, actions et paramètres

**Problème :** distinguer flux, requête courte et opération longue. Un service est request/response : /training/count utilise std_srvs/srv/Trigger et renvoie success et message. Une action accepte un objectif (goal), fournit des retours (feedback), un résultat et éventuellement une annulation : utile pour la navigation. Un paramètre est une configuration appartenant au nœud; interval_s=1.0 règle la période à l'initialisation. Le modifier ultérieurement ne reconstruit pas automatiquement le timer. Les retries de services exigent une politique applicative.

Le choix dépend du type de réponse, de la durée et des échecs possibles. Ces interfaces ne sont pas interchangeables :

| Mécanisme | Échange | Usage adapté | À ne pas confondre avec |
| --- | --- | --- | --- |
| Topic | Publisher → 0..N subscribers | Télémétrie continue | Journal durable ou transaction confirmée |
| Service | Requête → réponse | Consultation courte ou opération bornée | Commit garanti ou longue tâche |
| Action | Objectif → feedback/résultat, annulation possible | Navigation ou calcul prolongé | Flux périodique de capteur |
| Parameter | Valeur propre au nœud | Configuration telle que `interval_s` | Base de configuration mondiale partagée |

Dans ce laboratoire, `/training/status` est un topic, `/training/count` un service et `interval_s` un paramètre du nœud ; aucune action applicative n'est créée. Un timeout de service ne prouve pas que le serveur n'a rien exécuté : la politique de nouvelle tentative dépend de l'opération.

<a id="section-4"></a>

## 4. Packages, workspaces, colcon et ament

**Problème :** construire et installer des nœuds et leurs dépendances. Un package possède package.xml et une intégration de compilation ament_python ou ament_cmake. Un workspace comporte généralement src, build, install et log. colcon orchestre la construction; ament n'est pas un transport de messages. Il faut sourcer l'environnement ROS (underlay), puis le workspace (overlay). Notre package telemetry_demo expose deux exécutables via setup.py et installe un launch file.

Dans le véritable `ros2/Dockerfile`, la **construction de l'image** (`RUN`) et le **démarrage du conteneur** (`CMD`) sont distincts. Pendant la construction, seul l'underlay ROS est chargé avant la compilation par `colcon` :

**Construction de l'image (`RUN`) :**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
colcon build --packages-select telemetry_demo
```

**Démarrage du conteneur (`CMD`) :**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
source /opt/training_ws/install/setup.bash
exec ros2 launch telemetry_demo demo.launch.py
```

Au démarrage, un nouveau shell charge **de nouveau** l'underlay, puis l'overlay du workspace et lance le fichier launch. `package.xml` déclare les dépendances ; `setup.py` installe les points d'entrée Python et le launch. `build/` et `install/` contiennent des artefacts générés, pas le code source à modifier. Une compilation réussie ne prouve pas la disponibilité à l'exécution.

<a id="section-5"></a>

## 5. Inspection par ROS 2 CLI

**Problème :** découvrir ce qui tourne réellement. ros2 node list et node info montrent les nœuds; topic list, info et echo inspectent les flux; interface show vérifie les types; service list/call, action list et param get examinent les autres interfaces. Dans l'exemple, on trouve /sample_source, /sample_monitor, /training/status et /training/count. Aucun action applicatif n'est défini. Un topic vide peut révéler une incompatibilité de QoS ou un autre ROS_DOMAIN_ID.

Commandes CLI dans le conteneur après activation de l'environnement ROS :

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

## 6. Fichiers launch

**Problème :** démarrer plusieurs processus avec la même configuration. demo.launch.py produit une LaunchDescription avec deux actions launch_ros.actions.Node et fixe interval_s=1.0. Un launch peut contenir arguments, namespaces, remappings et autres fichiers. Démarrage ne signifie pas disponibilité instantanée : découverte, readiness et réessais restent des responsabilités de l'application.

**Observer la disponibilité :** `launch_ros.actions.Node` démarre les deux **processus**, mais la découverte DDS et le premier échantillon `/training/status` interviennent ensuite. Un appel immédiat de `/training/count` peut renvoyer normalement `received 0 samples` ; le compteur augmente plus tard. Ce n'est pas la preuve d'une transaction perdue : le service compte uniquement les échantillons reçus par le moniteur. `interval_s=1.0` est lu à la création du timer, et ne reconfigure pas automatiquement un timer actif.

<a id="section-7"></a>

## 7. tf2 et repères de coordonnées

**Problème :** convertir des mesures exprimées dans camera_link vers base_link ou map. tf2 publie et recherche les transformations datées entre frames, avec rotation et translation; les montages fixes peuvent utiliser des transformations statiques. Les timestamps et les relations parent-enfant sont essentiels. tf2 ne calcule pas automatiquement la cinématique directe/inverse ni les trajectoires. Les mathématiques se trouvent dans les leçons de repères et du Jacobien liées ci-dessous.

[Coordinate frames](04-coordinate-frames.md) · [Velocity and Jacobian](05-velocity-jacobian.md)

**Exemple de chaîne de repères (non imposée par ROS) :** `map → odom → base_link → camera_link`. Une caméra rigidement fixée au corps a une transformation `static` ; le déplacement du corps implique des transformations `dynamic`. Pour convertir dans `map` un point détecté à l'instant *t* dans `camera_link`, tf2 doit rechercher la chaîne **à l'heure de la mesure**. Un repère absent, un arbre disjoint ou un instant non disponible provoque une erreur de lookup/extrapolation ; utiliser la transformation la plus récente pour une mesure ancienne peut donner une position fausse.

**Exemple du sens d'une transformation et de son inverse.** `base_link` (B) est le repère parent et `tool` (T) le repère enfant. Sans rotation relative et avec une translation de 0.1 m selon l'axe X positif du parent, l'origine de l'outil se trouve **devant celle de la base dans B**. Le même décalage exprimé dans T a le signe opposé :

$$
{}^{B}\mathbf p_{T}=(0.1, 0, 0)\ \mathrm{m},\qquad
{}^{T}\mathbf p_{B}=(-0.1, 0, 0)\ \mathrm{m}\quad (R=I).
$$

Cette simple inversion du signe ne fonctionne que si les axes ont la **même orientation**. En général, convertir les coordonnées d'un point exige une rotation et une translation. La transformation inverse doit annuler **les deux** ; pour une matrice de rotation valide, $R^T$ est son inverse :

$$
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT},\qquad
\mathbf p_T=R_{BT}^{T}(\mathbf p_B-\mathbf t_{BT}),\qquad
\mathbf t_{TB}=-R_{BT}^{T}\mathbf t_{BT}.
$$

Dans une autre pose, tournons T de +90° autour de l'axe Z commun tout en conservant la translation (0.1 m, 0 m) dans B. L'origine de B exprimée dans T se trouve alors en (0 m, +0.1 m), **et non** en (−0.1 m, 0 m). Transformons aussi le point (0 m, 0.05 m) de T vers B :

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

Les repères et transformations **décrivent des coordonnées**, ils ne commandent aucun mouvement. ROS 2 emploie normalement les mètres pour la translation ; le [cours sur les repères](04-coordinate-frames.md#section-3) utilise des millimètres qui doivent être convertis avant de combiner les exemples. Une transformation statique décrit un montage fixe ; une transformation dynamique vient d'un composant produisant l'état. Utiliser l'horodatage de la mesure et gérer l'absence éventuelle de données.

<a id="section-8"></a>

## 8. URDF et robot_state_publisher

**Problème :** partager la description d'un mécanisme. URDF décrit links, joints, axes, origines et propriétés visuelles, de collision et d'inertie facultatives. robot_state_publisher combine URDF et les positions articulaires, généralement sensor_msgs/msg/JointState sur /joint_states, pour publier les frames. URDF ne mesure pas les encodeurs et ne fournit ni simulateur, ni solveur de cinématique inverse. Vérifier mètres, radians et conventions d'axes.

**Origine des transformations :** URDF décrit les articulations `fixed` et mobiles. `robot_state_publisher` utilise la géométrie fixe pour publier des transformations `static`, et les positions publiées sur `/joint_states` (`sensor_msgs/msg/JointState`) pour les transformations `dynamic` des articulations mobiles. URDF **ne mesure pas** les positions et ne recrée pas les observations manquantes. Dimensions en mètres, angles en radians et horodatages doivent rester cohérents.

<a id="section-9"></a>

## 9. ros2_control et frontière matérielle

**Problème :** séparer les contrôleurs des drivers. ros2_control fournit controller manager, interfaces d'état (position/vitesse) et de commande (position/vitesse/effort), et abstractions matérielles. Le planificateur demande un mouvement, le contrôleur traite l'état et une interface communique avec le matériel. La réception d'un message ROS ne garantit ni échéances temps réel, ni limite de courant, ni arrêt sûr. Le présent exercice ne pilote aucun actionneur.

[First-order dynamics](02-first-order-dynamics.md) · [Feedback PID](03-feedback-control.md)

**Rôle du gestionnaire de contrôleurs :** `controller_manager` gère le cycle de vie des contrôleurs et, par l'intermédiaire du gestionnaire de ressources, leur accès aux interfaces d'état (state interfaces) et de commande (command interfaces). Un contrôleur peut lire un état mesuré, par exemple `joint1/position` dans un modèle fictif ; un contrôleur actif peut réserver une interface de commande compatible pour écrire une consigne. La mesure n'est pas la consigne, et deux contrôleurs ne peuvent pas s'approprier librement une même interface de commande déjà réservée. La gestion des ressources va donc au-delà de la découverte des topics.

**Limite du laboratoire :** `/training/status` et `/training/count` illustrent un topic et un service, **pas `ros2_control`**. Aucun des deux nœuds n'est un contrôleur et le laboratoire n'exécute ni `controller_manager`, ni interface matérielle, ni boucle de régulation fermée. La réussite du smoke test ne valide ni le cycle de vie des contrôleurs, ni le temps réel, ni la sécurité des appareils. Voir [l'introduction officielle à ros2_control](https://control.ros.org/jazzy/doc/getting_started/getting_started.html).

**Suite pratique : ros2_control et TF2 sans GUI, avec articulation virtuelle:** [Suite pratique : ros2_control et TF2 sans GUI, avec articulation virtuelle](07-ros2-control-lab.md). Le nouveau laboratoire couvre URDF, GenericSystem, commandes, états, /joint_states, TF2, QoS et diagnostic du chargeur ARM64 ; il ne pilote aucun équipement réel.

**Étape suivante : architecture globale.** Le [diagramme Mermaid ROS 2 en cinq étapes](08-ros2-robot-architecture.md) relie perception, TF2 horodaté, planification, contrôle et retour d'état. La chaîne matérielle reste conceptuelle.

<a id="section-10"></a>

## 10. QoS, découverte DDS et Docker

**Problème :** comprendre pertes et invisibilité réseau. QoS inclut reliable/best_effort, volatile/transient_local, history et depth. Un subscriber qui exige des garanties non offertes peut ne rien recevoir malgré nom et type identiques. DDS utilise souvent multicast UDP et des ports dynamiques; Docker Desktop, VPN et pare-feux compliquent la découverte. Le même ROS_DOMAIN_ID est nécessaire. Notre exemple place tous les processus dans un seul conteneur, sans ports hôte ou privilèges; il ne teste pas le réseau entre machines.

**Exemple d'incompatibilité QoS :** si un publisher offre `best_effort` et qu'un subscriber demande `reliable`, les noms et types peuvent correspondre et les points d'accès être découverts, mais **aucun message n'arrive** : la garantie demandée dépasse celle offerte. À l'inverse, un subscriber `best_effort` peut accepter un publisher `reliable` si les autres politiques QoS sont compatibles. `volatile` ne rejoue pas l'historique ; `transient_local` peut garder quelques messages chez un publisher compatible encore présent, **sans former un journal distribué durable**.

**Diagnostic dans l'ordre :** vérifier `ROS_DOMAIN_ID=42` dans le même conteneur, puis `ros2 node list`, `ros2 topic info /training/status -v` pour les endpoints et QoS et `docker compose logs demo` pour les processus. Si le graphe est toujours vide, examiner RMW/DDS, les interfaces réseau et le pare-feu. Publier des ports TCP ne résout pas universellement DDS ; la communication entre machines n'est pas validée.

[Documentation officielle ROS 2 Jazzy sur QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)

[Alternative : image ROS officielle sans Compose ni Dockerfile personnalisé](../../../ros2/PLAIN_DOCKER.md)

<a id="section-11"></a>

## 11. Exercice : publisher, subscriber, service et lancement

Démarre le conteneur avec docker compose up --build -d. Les logs doivent afficher des échantillons publiés et reçus, avec un compte croissant. La commande de service répond avec success=True et un message tel que received 12 samples; le nombre exact dépend du démarrage. Un [smoke test Docker distinct dans GitHub Actions](../../../.github/workflows/ros2-live-smoke.yml) a réellement lancé l'application **dans un seul conteneur** : il a vérifié les deux nœuds ROS, reçu un message typé sur `/training/status` et obtenu une réponse de `/training/count`. La validation ordinaire n'exécute pas ROS. Ces tests ne valident ni DDS entre plusieurs machines, ni les délais déterministes, ni le matériel réel, ni l'installation Docker du lecteur.

[Complete source, expected results and diagnostics](../../../ros2/README.md). From the repository root:

Pour progresser dans l'ordre, commence par le talker `demo_nodes_cpp` et le listener `demo_nodes_py` installés dans l'image, puis examine le paquet `telemetry_demo` du dépôt, avant de passer à `ros2_control`. Dockerfile installe les démos avec APT et construit `telemetry_demo` avec `colcon`. En mode interactif, ouvre **un shell Bash** et charge les deux environnements **une fois par nouveau shell** : un `docker compose exec` séparé n'hérite pas de l'environnement du `CMD`.

Sur l'hôte, crée le conteneur et ouvre un shell interactif :

```bash
cd ros2
docker compose up --build -d
docker compose logs --tail=20 demo
docker compose exec demo bash
```

Dans le conteneur (pas sur l'hôte), charge les environnements une fois et inspecte le graphe :

```bash
echo "$ROS_DISTRO"
ros2 node list
ros2 service call /training/count std_srvs/srv/Trigger "{}"
exit
```

Après `exit`, revenu sur l'hôte, nettoie le conteneur :

```bash
docker compose down
```

**Frontière de confiance du CI :** le smoke test Docker ROS 2 réel se lance désormais automatiquement uniquement après l'arrivée des modifications dans `main`, ou par `workflow_dispatch` sur `main`. Il ne s'exécute **pas sur les révisions `pull_request`** : sinon le runner hôte exécuterait un script Bash et un Dockerfile contrôlés par le PR. Les tests Python isolés avant fusion ne remplacent pas le test ROS en fonctionnement. Exiger une revue indépendante avant la fusion et vérifier le résultat du test réel après.

<a id="section-12"></a>

## 12. Glossaire et limites

- **Node / processus :** un nœud est un composant ROS logique nommé ; un processus système peut héberger plusieurs nœuds.
- **ROS graph :** ensemble des points de communication actuellement découverts, sans registre central permanent ni autorisation implicite.
- **Topic :** flux asynchrone nommé avec éventuellement plusieurs publishers et subscribers.
- **Message :** structure typée décrite par une interface ROS, et non objet Python ou C++ arbitraire.
- **Publisher / subscriber :** émetteur et récepteur de messages ; découverte et QoS compatibles sont nécessaires à la livraison.
- **Service :** requête/réponse typée pour une interaction courte ; un délai dépassé ne prouve pas l'absence d'exécution.
- **Action :** objectif avec feedback, résultat et demande d'annulation ; demander l'annulation n'assure pas un arrêt immédiat.
- **Parameter :** valeur détenue par un nœud ; sa modification n'ajuste pas automatiquement un minuteur déjà créé.
- **RMW / DDS :** RMW abstrait le middleware ; DDS est une technologie courante de découverte/transport, sans authentification automatique.
- **colcon / ament :** orchestration de compilation du workspace / intégration des paquets ROS, pas transport de messages.
- **Launch :** description des processus à démarrer et de leur configuration ; le démarrage ne garantit pas la disponibilité.
- **tf2 :** gestion de transformations de repères horodatées, pas solveur de cinématique inverse.
- **URDF / robot_state_publisher :** modèle structurel du robot / publication de transformations à partir du modèle et des états articulaires.
- **ros2_control :** cycle de vie des contrôleurs et gestion des interfaces d'état/commande ; absent du laboratoire topic/service.
- **QoS :** compatibilité des politiques de livraison et d'historique ; ni journal durable ni certification de sécurité.

**Versions vérifiées le 13 novembre 2026 :** ROS 2 Jazzy LTS est pris en charge jusqu'en mai 2029 et Lyrical LTS jusqu'en mai 2031. L'étiquette Docker ne fixe ni un digest immuable de l'image ni les versions des paquets apt.

**Primary sources:** [ROS 2 releases](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst) · [Jazzy documentation](https://docs.ros.org/en/jazzy/) · [tf2](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html) · [URDF](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html) · [ros2_control](https://control.ros.org/jazzy/)
