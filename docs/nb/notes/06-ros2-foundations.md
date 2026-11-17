# 6. ROS 2: distribuert robotprogramvare og grensesnitt

**Languages:** [en](../../en/notes/06-ros2-foundations.md) · [fr](../../fr/notes/06-ros2-foundations.md) · [de](../../de/notes/06-ros2-foundations.md) · [it](../../it/notes/06-ros2-foundations.md) · [es](../../es/notes/06-ros2-foundations.md) · [pt](../../pt/notes/06-ros2-foundations.md) · [zh](../../zh/notes/06-ros2-foundations.md) · [ja](../../ja/notes/06-ros2-foundations.md) · [nb](06-ros2-foundations.md) · [ru](../../ru/notes/06-ros2-foundations.md) · [ko](../../ko/notes/06-ros2-foundations.md) · [fi](../../fi/notes/06-ros2-foundations.md) · [pl](../../pl/notes/06-ros2-foundations.md)

**Enheter på denne siden (forklart før eksemplene):** `m` — meter; `s` — sekund. [Enhetsoversikt](../UNITS.md).

[Course index](../README.md) · [Coordinate frames](04-coordinate-frames.md) · [Jacobian](05-velocity-jacobian.md) · [Docker lab](../../../ros2/README.md)

> **Safety:** Kun syntetisk programvareøvelse. Ikke bruk eksemplet til å styre virkelige roboter eller maskiner. ROS-kommunikasjon erstatter ikke kinematikk, sanntidsregulering eller maskinvaresikkerhet.

ROS 2 (Robot Operating System 2) binder sammen distribuerte programvarekomponenter i en robot. For en backend-utvikler minner en node om en prosess, et topic om en typet asynkron hendelsesstrøm og en service om RPC. Sammenlikningen har grenser: ROS 2 bruker vanligvis DDS for distribuert oppdagelse, ikke en påkrevd sentral meldingsmegler.

![ROS 2 publisher and subscriber linked through a typed topic; a CLI process calls a service](../../../assets/figures/ros2-topic-service.svg)

![ROS 2-programvarelag og en separat grense mot maskinvare og sikkerhet](../../../assets/figures/ros2-software-layers.svg)

*Meldingsutveksling erstatter ikke tidskritisk lavnivåkontroll eller uavhengige sikkerhetstiltak.*

## Læringsløp

1. [Arkitektur, middleware og ROS graph](#section-1)
2. [Nodes, topics og typede messages](#section-2)
3. [Services, actions og parameters](#section-3)
4. [Packages, workspaces, colcon og ament](#section-4)
5. [Inspeksjon med ROS 2 CLI](#section-5)
6. [Launch-filer](#section-6)
7. [tf2 og koordinatrammer (coordinate frames)](#section-7)
8. [URDF og robot_state_publisher](#section-8)
9. [ros2_control og grensen mot maskinvare](#section-9)
10. [QoS, DDS discovery og Docker](#section-10)
11. [Praksis: to noder, topic, service og launch](#section-11)
12. [Ordliste og begrensninger](#section-12)

<a id="section-1"></a>

## 1. Arkitektur, middleware og ROS graph

**Problem:** Kamera, lokalisering og planlegging skal samarbeide uten å være én stor prosess. ROS 1 brukte en sentral master for navneoppdagelse. ROS 2 bruker RMW-abstraksjonen og vanligvis DDS/RTPS til å finne deltakere uten ROS 1-master. ROS graph er mengden oppdagede nodes, topics, services og actions. Flere logiske nodes kan ligge i samme prosess, mens prosesser kan kjøre på ulike datamaskiner. Oppdagelse er ikke autentisering.

<a id="section-2"></a>

## 2. Nodes, topics og typede messages

**Problem:** Flere mottakere trenger de samme løpende målingene. En publisher sender typede meldinger på et topic; subscribers tar imot asynkront. std_msgs/msg/String har feltet string data og er et felles grensesnitt for Python og C++. /sample_source publiserer på /training/status; /sample_monitor mottar og teller. Kødybde 10 betyr ikke varig lagring; en ny abonnent ser normalt fremtidige meldinger.

**Eksempel på discovery:** Anta at `/sample_source` har publisert `sample 1` før `/sample_monitor` blir oppdaget. Med labens `volatile`-historikk spilles ikke denne eldre meldingen automatisk av for en ny abonnent. Monitoren kan først svare `received 0 samples` selv om publisheren fortsetter å sende. Etter at kompatible endpoints har funnet hverandre, kan tellingen stige. Publisert sekvensnummer og antall mottatte meldinger måler ulike ting; ingen av dem bekrefter en transaksjon.

**Hva CLI faktisk viser:** `ros2 topic list -t` viser oppdagede topic-navn og meldingstyper, **ikke** at subscribers har mottatt meldinger. `ros2 topic info /training/status -v` viser oppdagede endpoints og tilbudt/forespurt QoS. Null subscribers kan bety at ingen kjører, **eller** at discovery ikke er ferdig. Hvis endpoints vises uten data, sjekk typer, QoS, prosesslogger og `ROS_DOMAIN_ID`. Resultatene er øyeblikksbilder, ikke leveringsgarantier. Kjør kommandoene inne i øvelsens container.

<a id="section-3"></a>

## 3. Services, actions og parameters

**Problem:** Skille datastrøm, kort forespørsel og langvarig jobb. En service bruker request/response: /training/count med std_srvs/srv/Trigger returnerer success og message. Actions håndterer goal, feedback, result og cancel, for eksempel navigasjon. Parameters eies av en node: interval_s=1.0 brukes når timeren opprettes. Senere endringer bygger ikke automatisk timeren på nytt. Applikasjonen må vurdere timeout og idempotent retry.

Velg mekanisme etter svarbehov, varighet og feiltilfeller. Grensesnittene kan ikke brukes om hverandre:

| Mekanisme | Flyt | Egnet til | Må ikke forveksles med |
| --- | --- | --- | --- |
| Topic | Publisher → 0..N subscribers | Kontinuerlig telemetri | Varig logg eller bekreftet transaksjon |
| Service | Forespørsel → svar | Kort oppslag eller avgrenset oppgave | Garantert commit eller lang jobb |
| Action | Mål → feedback/resultat, mulig avbrudd | Navigering eller lang beregning | Periodisk sensorstrøm |
| Parameter | Verdi eid av en node | Konfigurasjon som `interval_s` | Global distribuert konfigurasjonsdatabase |

I eksemplet er `/training/status` et topic, `/training/count` en service og `interval_s` en nodeparameter; det finnes ingen applikasjons-action. En tidsavbrutt service-forespørsel betyr ikke at serveren ikke utførte handlingen; om den kan gjentas avhenger av semantikken.

<a id="section-4"></a>

## 4. Packages, workspaces, colcon og ament

**Problem:** Bygge og installere kjørbare komponenter med tydelige avhengigheter. package.xml beskriver pakken; ament_python/ament_cmake integrerer byggesystemet. Et workspace inneholder vanligvis src, build, install og log. colcon bygger pakker, men er ikke meldingstransport. Source først ROS-underlay, deretter workspace-overlay. telemetry_demo registrerer to kjørbare entry points i setup.py og installerer launch-filen.

I den faktiske filen `ros2/Dockerfile` er **image-bygging** (`RUN`) og **oppstart av container** (`CMD`) ulike faser. Under bygging lastes bare ROS-underlay før pakken bygges med `colcon`:

**Image-bygging (`RUN`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
colcon build --packages-select telemetry_demo
```

**Oppstart av container (`CMD`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
source /opt/training_ws/install/setup.bash
exec ros2 launch telemetry_demo demo.launch.py
```

Ved oppstart laster et nytt shell ROS-underlay **på nytt**, deretter workspace-overlay, før launch-filen startes. `package.xml` oppgir avhengigheter; `setup.py` installerer Python-inngangspunkter og launch-filen. `build/` og `install/` er genererte filer, ikke mapper for redigering av kildekode. Et vellykket bygg betyr ikke at appen er klar.

<a id="section-5"></a>

## 5. Inspeksjon med ROS 2 CLI

**Problem:** Finne hva som faktisk kjører. ros2 node list/info viser noder; topic list/info/echo undersøker strømmer; interface show viser typer; service list/call, action list og param get inspiserer andre endepunkter. Eksemplet viser /sample_source, /sample_monitor, /training/status og /training/count. Det finnes ingen egen action. Ved manglende meldinger kontroller navn, type, QoS og ROS_DOMAIN_ID.

CLI-kommandoer i containeren etter at ROS-miljøet er aktivert:

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

## 6. Launch-filer

**Problem:** Starte flere prosesser med samme oppsett. demo.launch.py returnerer LaunchDescription med to launch_ros.actions.Node og sender interval_s=1.0 til publisheren. Launch støtter argumenter, namespaces, remapping og inkludering av andre filer. At prosessen er startet, betyr ikke at alt er klart; discovery, readiness og retries må håndteres separat.

**Kontroller at systemet er klart:** `launch_ros.actions.Node` starter to **prosesser**, men DDS-oppdagelse og den første `/training/status`-meldingen kommer senere. Et øyeblikkelig kall til `/training/count` kan korrekt svare `received 0 samples`; tallet vokser etter hvert. Det er ikke bevis på en tapt transaksjon: servicen rapporterer bare det monitoren har mottatt. `interval_s=1.0` leses når timeren opprettes og endrer ikke automatisk en aktiv timer.

<a id="section-7"></a>

## 7. tf2 og koordinatrammer (coordinate frames)

**Problem:** Gjøre kameramålinger i camera_link om til base_link eller map. tf2 lagrer og slår opp tidsmerkede transformasjoner med rotasjon og translasjon. Faste monteringer bruker statiske, bevegelige ledd dynamiske transformasjoner. Parent/child og tidsstempler må stemme. tf2 løser ikke selv forover-/invers kinematikk eller planlegging. Matematikken finnes i kapitlene om koordinatrammer og Jacobian.

[Coordinate frames](04-coordinate-frames.md) · [Velocity and Jacobian](05-velocity-jacobian.md)

**Eksempel på rammekjede (ikke en påkrevd oppbygning):** `map → odom → base_link → camera_link`. Et kamera som er fast montert på basen, har en `static` transformasjon; en base i bevegelse krever `dynamic` transformasjoner. Et punkt observert i `camera_link` ved tid *t* må transformeres til `map` ved å finne kjeden **for tidspunktet for målingen**. Manglende ramme, brutt kjede eller utilgjengelig tidsstempel gir lookup-/extrapolation-feil. Å bruke den nyeste transformasjonen på gamle målinger kan gi feil koordinater.

**Eksempel på transformasjonsretning og invers.** La `base_link` (B) være foreldrerammen og `tool` (T) barnet. Uten relativ rotasjon og med en forskyvning på 0.1 m langs foreldrens positive X ligger verktøyets origo **foran basens origo i B-koordinater**. Sett fra T har den samme avstanden motsatt fortegn:

$$
{}^{B}\mathbf p_{T}=(0.1, 0, 0)\ \mathrm{m},\qquad
{}^{T}\mathbf p_{B}=(-0.1, 0, 0)\ \mathrm{m}\quad (R=I).
$$

Denne enkle fortegnsvendingen fungerer bare når rammene har **samme orientering**. Generelt omregnes et punkt med rotasjon og translasjon. Den inverse transformasjonen må angre **begge deler**; for en gyldig rotasjonsmatrise er inversen $R^T$:

$$
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT},\qquad
\mathbf p_T=R_{BT}^{T}(\mathbf p_B-\mathbf t_{BT}),\qquad
\mathbf t_{TB}=-R_{BT}^{T}\mathbf t_{BT}.
$$

I en annen posisjon er T rotert +90° om den felles Z-aksen, mens forskyvningen i B fortsatt er (0.1 m, 0 m). Origo til B uttrykt i T blir da (0 m, +0.1 m), **ikke** (−0.1 m, 0 m). De samme matrisene omregner også punktet (0 m, 0.05 m) i T til B:

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

Rammer og transformasjoner **beskriver koordinater**, de er ikke motorstyringskommandoer. I ROS 2 følger translasjoner normalt meterkonvensjonen; [koordinatleksjonen](04-coordinate-frames.md#section-3) bruker millimeter som må konverteres før tallene kombineres. Statiske transformasjoner beskriver faste monteringer, dynamiske publiseres av komponenter som har aktuelle tilstandsdata. Historiske målinger krever transformasjoner ved måletidspunktet, med håndtering av manglende data.

<a id="section-8"></a>

## 8. URDF og robot_state_publisher

**Problem:** Ha én felles beskrivelse av robotmekanismen. URDF beskriver links, joints, origo, akser og valgfrie visual/collision/inertial-egenskaper. robot_state_publisher kombinerer URDF og leddposisjoner (vanligvis sensor_msgs/msg/JointState på /joint_states) og publiserer transformasjoner. URDF gir ikke enkodermålinger, simulering eller invers kinematikk. Hold m, rad og aksekonvensjoner konsistente.

**Hvor transformasjonene kommer fra:** URDF beskriver `fixed` og bevegelige joints. `robot_state_publisher` bruker fast geometri til `static` transformasjoner og posisjoner fra `/joint_states` (`sensor_msgs/msg/JointState`) til `dynamic` transformasjoner for bevegelige joints. URDF **måler ikke** leddposisjonene og gjenskaper ikke manglende måledata. Bruk meter, radianer og konsistente tidsstempler.

<a id="section-9"></a>

## 9. ros2_control og grensen mot maskinvare

**Problem:** Skille reguleringslogikk fra drivere. ros2_control tilbyr controller manager, state interfaces (posisjon/hastighet), command interfaces (posisjon/hastighet/effort) og maskinvareabstraksjoner. Planlegger → kontroller → maskinvaregrensesnitt → enhet, med tilbakemeldinger. En ROS-melding garanterer ikke hard sanntid, strømbegrensning eller sikker stopp. Dette eksemplet styrer ingen aktuatorer.

[First-order dynamics](02-first-order-dynamics.md) · [Feedback PID](03-feedback-control.md)

**Hva controller manager gjør:** `controller_manager` styrer kontrolleres livssyklus og, via ressursbehandleren, tilgangen til tilstandsgrensesnitt (state interfaces) og kommandogrensesnitt (command interfaces). En kontroller kan lese en målt tilstand som det hypotetiske `joint1/position`; en aktiv kontroller kan reservere et kompatibelt kommandogrensesnitt for å skrive en ønsket verdi. Målt verdi er ikke det samme som kommandert verdi, og to kontrollere kan ikke fritt reservere samme kommandogrensesnitt som allerede er i bruk. Aktivering og ressursfordeling er derfor noe annet enn topic discovery.

**Grensen for øvelsen:** `/training/status` og `/training/count` illustrerer topic og service, **ikke `ros2_control`**. Ingen av de to nodene er en kontroller; øvelsen kjører ikke `controller_manager`, maskinvaregrensesnitt eller lukket reguleringssløyfe. En bestått smoke test kontrollerer ikke kontrolleres livssyklus, sanntidsegenskaper eller enhetssikkerhet. Se [offisiell introduksjon til ros2_control](https://control.ros.org/jazzy/doc/getting_started/getting_started.html).

**Praktisk fortsettelse: ros2_control og TF2 uten GUI med virtuelt ledd:** [Praktisk fortsettelse: ros2_control og TF2 uten GUI med virtuelt ledd](07-ros2-control-lab.md). Det nye laboratoriet dekker URDF, GenericSystem, kommandoer, tilstander, /joint_states, TF2, QoS og ARM64-loaderdiagnostikk; det styrer ikke fysisk utstyr.

**Neste trinn: full robotarkitektur.** Det [redigerbare Mermaid-diagrammet med fem trinn](08-ros2-robot-architecture.md) knytter persepsjon, TF2 ved riktig tidspunkt, planlegging, kontroll og tilbakemelding. Maskinvarebanen er konseptuell.

<a id="section-10"></a>

## 10. QoS, DDS discovery og Docker

**Problem:** Forstå tapte meldinger og usynlige noder. QoS omfatter reliable/best_effort, volatile/transient_local, history og depth. Hvis en subscriber krever sterkere garanti enn publisher tilbyr, kan strømmen bli tom selv med riktig navn/type. DDS bruker ofte UDP-multicast og dynamiske porter; Docker Desktop, VPN og brannmurer påvirker discovery. ROS_DOMAIN_ID må samsvare. Hele laben kjøres i én container uten privilegier eller eksponerte host-porter; kommunikasjon på tvers av maskiner er ikke testet.

**Eksempel på inkompatibel QoS:** En publisher tilbyr `best_effort`, mens en subscriber krever `reliable`. Selv om topic-navn og meldingstype stemmer og endepunktene er synlige, kan abonnenten **ikke motta meldinger** fordi kravet er sterkere enn tilbudet. Omvendt kan en `best_effort`-subscriber motta fra en `reliable`-publisher hvis de andre QoS-innstillingene er kompatible. `volatile` spiller ikke av gamle meldinger; `transient_local` kan tilby begrenset historikk fra en tilgjengelig kompatibel publisher, **ikke en varig distribuert logg**.

**Diagnose i rekkefølge:** Bekreft `ROS_DOMAIN_ID=42` inne i samme container, kjør `ros2 node list`, `ros2 topic info /training/status -v` for endepunkter og QoS, og `docker compose logs demo` for prosessene. Hvis grafen er tom, undersøk RMW/DDS, nettverksgrensesnitt og brannmur. Å åpne TCP-porter alene er ingen generell DDS-løsning; kommunikasjon mellom maskiner er ikke testet.

[Offisiell ROS 2 Jazzy-dokumentasjon om QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)

[Alternativ: offisielt ROS-image uten Compose eller egen Dockerfile](../../../ros2/PLAIN_DOCKER.md)

<a id="section-11"></a>

## 11. Praksis: to noder, topic, service og launch

Start med docker compose up --build -d. Loggene skal vise publiserte og mottatte samples med økende antall. Service-svaret har success=True og en tekst som received 12 samples; tallet avhenger av tidspunktet. En [egen Docker-smoketest i GitHub Actions](../../../.github/workflows/ros2-live-smoke.yml) har faktisk **startet applikasjonen i én container** og kontrollert begge ROS-noder, mottak av en typet melding på `/training/status` og et svar fra `/training/count`. Vanlig validerings-CI kjører ikke ROS. Testene bekrefter ikke DDS mellom ulike maskiner, deterministisk sanntidsatferd, fysisk utstyr eller leserens lokale Docker-installasjon.

[Source, expected results and troubleshooting](../../../ros2/README.md). From the repository root:

Lær i denne rekkefølgen: den installerte `demo_nodes_cpp`-talkeren og `demo_nodes_py`-lytteren, deretter repoets egenbygde `telemetry_demo`, til slutt `ros2_control`. Dockerfile installerer standarddemonstrasjonene med APT og bygger `telemetry_demo` med `colcon`. Ved interaktiv bruk åpner du **ett Bash-skall** og laster miljøene **én gang per nytt skall**; en separat `docker compose exec`-prosess arver ikke skallmiljøet fra `CMD`.

Start containeren på verten og åpne et interaktivt skall:

```bash
cd ros2
docker compose up --build -d
docker compose logs --tail=20 demo
docker compose exec demo bash
```

Inne i containeren, ikke på verten, last miljøene én gang og undersøk grafen:

```bash
echo "$ROS_DISTRO"
ros2 node list
ros2 service call /training/count std_srvs/srv/Trigger "{}"
exit
```

Etter `exit`, tilbake på verten, rydd opp:

```bash
docker compose down
```

**Tillitsgrense i CI:** Den faktiske ROS 2 Docker-smoketesten kjøres nå automatisk først etter at relevante endringer når `main`, eller manuelt via `workflow_dispatch` på `main`. Den kjøres ikke for `pull_request`-revisjoner, fordi vertsmaskinens runner ellers ville utført Bash-skript og Dockerfile-instruksjoner som PR-en kontrollerer. Isolerte Python-tester før sammenslåing er ikke det samme som en live ROS-test. Krev uavhengig gjennomgang før sammenslåing og kontroller live-testen etterpå.

<a id="section-12"></a>

## 12. Ordliste og begrensninger

- **Node / prosess:** En node er en navngitt logisk ROS-komponent; én operativsystemprosess kan inneholde flere noder.
- **ROS graph:** Kommunikasjonsendepunkter som er oppdaget nå, ikke et permanent sentralt register eller tilgangskontroll.
- **Topic:** Navngitt asynkron strøm med flere mulige publishers og subscribers.
- **Message:** Typet datastruktur definert av et ROS-grensesnitt, ikke et vilkårlig Python- eller C++-objekt.
- **Publisher / subscriber:** Avsender og mottaker av topic-meldinger; discovery og kompatibel QoS kreves for levering.
- **Service:** Typet forespørsel og svar for korte operasjoner; en timeout beviser ikke at serveren ikke utførte noe.
- **Action:** Mål med feedback, resultat og mulighet for avbestillingsforespørsel; en slik forespørsel garanterer ikke umiddelbar stopp.
- **Parameter:** Verdi som eies av én node; en endring justerer ikke automatisk en timer som allerede er opprettet.
- **RMW / DDS:** RMW skjuler detaljer ved middleware; DDS brukes ofte til discovery og transport, ikke autentisering i seg selv.
- **colcon / ament:** Orkestrering av workspace-bygg / ROS-pakkeintegrasjon, ikke meldingstransport.
- **Launch:** Beskrivelse av prosesser og innstillinger som skal startes; oppstart betyr ikke at grafen er klar.
- **tf2:** Infrastruktur for tidsstemplede koordinattransformasjoner, ikke en løser for invers kinematikk.
- **URDF / robot_state_publisher:** Strukturmodell av roboten / publisering av transformasjoner fra modell og gjeldende leddtilstander.
- **ros2_control:** Kontrolleres livssyklus og ressursstyrte state/command-grensesnitt; ikke vist i denne topic/service-øvelsen.
- **QoS:** Kompatibilitet, levering og historikkregler, ikke en varig hendelseslogg eller sikkerhetsgodkjenning.

**Versjonsstatus kontrollert 13. november 2026:** ROS 2 Jazzy LTS støttes til mai 2029 og Lyrical LTS til mai 2031. Docker-taggen låser verken en uforanderlig image-digest eller apt-pakkeversjonene.

**Primary sources:** [ROS 2 releases](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst) · [Jazzy documentation](https://docs.ros.org/en/jazzy/) · [tf2](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html) · [URDF](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html) · [ros2_control](https://control.ros.org/jazzy/)
