# 6. ROS 2: hajautettu robottiohjelmisto ja rajapinnat

**Languages:** [en](../../en/notes/06-ros2-foundations.md) · [fr](../../fr/notes/06-ros2-foundations.md) · [de](../../de/notes/06-ros2-foundations.md) · [it](../../it/notes/06-ros2-foundations.md) · [es](../../es/notes/06-ros2-foundations.md) · [pt](../../pt/notes/06-ros2-foundations.md) · [zh](../../zh/notes/06-ros2-foundations.md) · [ja](../../ja/notes/06-ros2-foundations.md) · [nb](../../nb/notes/06-ros2-foundations.md) · [ru](../../ru/notes/06-ros2-foundations.md) · [ko](../../ko/notes/06-ros2-foundations.md) · [fi](06-ros2-foundations.md) · [pl](../../pl/notes/06-ros2-foundations.md)

**Tämän sivun yksiköt (selitetty ennen esimerkkejä):** `m` — metri; `s` — sekunti. [Yksikköluettelo](../UNITS.md).

[Course index](../README.md) · [Coordinate frames](04-coordinate-frames.md) · [Jacobian](05-velocity-jacobian.md) · [Docker lab](../../../ros2/README.md)

> **Safety:** Vain synteettinen ohjelmistoharjoitus. Älä käytä esimerkkiä oikean robotin tai koneen ohjaamiseen. ROS-viestintä ei korvaa kinematiikkaa, reaaliaikaista säätöä eikä laitteiston turvallisuustoimintoja.

ROS 2 (Robot Operating System 2) yhdistää robotin hajautettuja ohjelmistokomponentteja. Backend-kehittäjälle solmu (node) muistuttaa loogista laskentakomponenttia, aihe (topic) tyypitettyä asynkronista tapahtumavirtaa ja palvelu (service) RPC-kutsua. Vertaus ei ole täydellinen: ROS 2 käyttää tavallisesti DDS-pohjaista hajautettua löytämistä ilman pakollista keskitettyä välittäjää.

![ROS 2 publisher and subscriber linked through a typed topic; a CLI process calls a service](../../../assets/figures/ros2-topic-service.svg)

![ROS 2 -ohjelmistokerrokset ja erillinen laitteiston turvallisuusraja](../../../assets/figures/ros2-software-layers.svg)

*Viestintäjärjestelmä ei korvaa aikakriittistä laiteohjausta tai itsenäisiä turvatoimia.*

## Oppimispolku

1. [Arkkitehtuuri, middleware ja ROS graph](#section-1)
2. [Nodes, topics ja tyypitetyt messages](#section-2)
3. [Services, actions ja parameters](#section-3)
4. [Packages, workspaces, colcon ja ament](#section-4)
5. [ROS 2 CLI -tarkastelu](#section-5)
6. [Launch-tiedostot](#section-6)
7. [tf2 ja koordinaatistot (coordinate frames)](#section-7)
8. [URDF ja robot_state_publisher](#section-8)
9. [ros2_control ja laitteistoraja](#section-9)
10. [QoS, DDS discovery ja Docker](#section-10)
11. [Harjoitus: kaksi solmua, topic, service ja launch](#section-11)
12. [Sanasto ja rajoitukset](#section-12)

<a id="section-1"></a>

## 1. Arkkitehtuuri, middleware ja ROS graph

**Ongelma:** Kameran, paikannuksen ja suunnittelun on toimittava erillisinä mutta yhteensopivina palveluina. ROS 1 käytti keskitettyä masteria nimien löytämiseen; ROS 2 käyttää RMW-abstraktiota ja yleensä DDS/RTPS-järjestelmää löytääkseen osallistujat ilman ROS 1 -masteria. ROS graph on havaittujen solmujen, aiheiden, palvelujen ja toimintojen joukko. Solmu on looginen osa: samassa prosessissa voi olla useita solmuja ja prosesseja voi olla eri koneissa. Löytäminen ei ole tunnistautumista.

<a id="section-2"></a>

## 2. Nodes, topics ja tyypitetyt messages

**Ongelma:** Jatkuva mittaustieto pitää välittää monelle vastaanottajalle. Publisher julkaisee tyypitettyjä viestejä topicissa ja subscriber vastaanottaa ne asynkronisesti. std_msgs/msg/String sisältää kentän string data ja sama rajapinta toimii Pythonissa ja C++:ssa. /sample_source lähettää viestejä aiheeseen /training/status, /sample_monitor vastaanottaa ja laskee niitä. Jonon depth 10 ei tarkoita pysyvää historiaa: uusi tilaaja saa yleensä tulevat viestit.

**Esimerkki discoveryn etenemisestä:** Oletetaan, että `/sample_source` ehti julkaista `sample 1` ennen kuin `/sample_monitor` havaittiin. Harjoituksen `volatile`-historia ei automaattisesti toista tätä vanhaa viestiä. Monitori voi aluksi vastata `received 0 samples` vaikka publisher lähettää edelleen. Laskuri voi kasvaa vasta yhteensopivien endpoints-yhteyspisteiden löydyttyä. Julkaistu järjestysnumero ja vastaanotettujen viestien määrä mittaavat eri asioita; kumpikaan ei ole transaktion kuittaus.

**Mitä CLI kertoo:** `ros2 topic list -t` näyttää löydettyjen topicien nimet ja tyypit, **ei** todista viestin toimitusta subscriberille. `ros2 topic info /training/status -v` näyttää havaitut endpoints-yhteyspisteet sekä tarjotun ja pyydetyn QoS:n. Nolla subscriberia voi tarkoittaa, ettei tilaajaa ole, **tai** että discovery on kesken. Jos endpoints näkyvät mutta data ei kulje, tarkista tyypit, QoS, prosessilokit ja `ROS_DOMAIN_ID`. Nämä ovat tilannekuvia, eivät toimitustakuita. Suorita komennot harjoituksen containerin sisällä.

<a id="section-3"></a>

## 3. Services, actions ja parameters

**Ongelma:** Erota datavirta, lyhyt kysely ja pitkä tehtävä. Service käyttää request/response-mallia: /training/count toteuttaa std_srvs/srv/Trigger-rajapinnan ja palauttaa success- sekä message-kentät. Action käyttää goal-, feedback-, result- ja cancel-käsitteitä esimerkiksi navigointiin. Parameter on solmun omistama asetus; interval_s=1.0 luetaan ajastimen luomisessa. Arvon muuttaminen myöhemmin ei automaattisesti rakenna ajastinta uudelleen. Uusintayrityksen turvallisuus on sovelluksen vastuulla.

Valinta riippuu vastauksesta, toiminnon kestosta ja virhetilanteista. Näillä rajapinnoilla on eri tarkoitukset:

| Mekanismi | Tiedonkulku | Sopii tilanteeseen | Ei tarkoita |
| --- | --- | --- | --- |
| Topic | Julkaisija → 0..N tilaajaa | Jatkuva tilatieto tai telemetria | Pysyvää lokia tai vahvistettua transaktiota |
| Service | Pyyntö → vastaus | Lyhyt kysely tai rajattu toiminto | Taattua commitia tai pitkää tehtävää |
| Action | Tavoite → palaute/tulos, mahdollinen peruutus | Navigointi tai pitkä laskenta | Jaksottaista anturivirtaa |
| Parameter | Solmun oma arvo | Asetus kuten `interval_s` | Yhteistä globaalia hajautettua tietokantaa |

Tässä esimerkissä `/training/status` on topic, `/training/count` service ja `interval_s` solmun parametri. Sovellus ei toteuta actionia. Servicen aikakatkaisu ei todista, ettei palvelin suorittanut pyyntöä; turvallinen uudelleenyritys riippuu toiminnon merkityksestä.

<a id="section-4"></a>

## 4. Packages, workspaces, colcon ja ament

**Ongelma:** Rakenna riippuvuudet ja suoritettavat solmut toistettavasti. package.xml kuvaa paketin, ament_python ja ament_cmake liittävät sen koontijärjestelmään. Workspace sisältää tavallisesti src-, build-, install- ja log-kansiot. colcon ohjaa koontia eikä siirrä viestejä. Ota ensin käyttöön ROS-underlay, sitten workspace-overlay. telemetry_demo rekisteröi setup.py:ssä kaksi ohjelman käynnistyspistettä ja asentaa launch-tiedoston.

Varsinaisessa `ros2/Dockerfile`-tiedostossa **levykuvan rakentaminen** (`RUN`) ja **kontin käynnistys** (`CMD`) ovat eri vaiheita. Rakennettaessa ladataan vain ROS-underlay ennen kuin `colcon` kokoaa paketin:

**Levykuvan rakentaminen (`RUN`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
colcon build --packages-select telemetry_demo
```

**Kontin käynnistys (`CMD`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
source /opt/training_ws/install/setup.bash
exec ros2 launch telemetry_demo demo.launch.py
```

Käynnistyksessä uusi komentotulkki lataa ROS-underlayn **uudelleen**, sitten workspacen overlayn, ja käynnistää launch-tiedoston. `package.xml` ilmoittaa riippuvuudet; `setup.py` asentaa Pythonin käynnistyspisteet ja launch-tiedoston. `build/` ja `install/` sisältävät tuotettuja tiedostoja, eivät lähdekoodia muokattavaksi. Onnistunut koonti ei vielä takaa sovelluksen valmiutta.

<a id="section-5"></a>

## 5. ROS 2 CLI -tarkastelu

**Ongelma:** Näe hajautetun järjestelmän todellinen tila. ros2 node list/info näyttää solmut, topic list/info/echo virrat, interface show viestityypit, service list/call, action list ja param get muut rajapinnat. Harjoituksessa näkyvät /sample_source, /sample_monitor, /training/status ja /training/count. Sovellus ei sisällä actionia. Jos viestejä ei näy, tarkista nimet, tyypit, QoS ja ROS_DOMAIN_ID.

Seuraavat CLI-komennot suoritetaan kontissa ROS-ympäristön aktivoinnin jälkeen:

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

## 6. Launch-tiedostot

**Ongelma:** Käynnistä monta prosessia samalla konfiguraatiolla. demo.launch.py palauttaa LaunchDescription-olion, jossa on kaksi launch_ros.actions.Node-toimintoa ja parametri interval_s=1.0. Launch voi käyttää argumentteja, nimiavaruuksia, remappingia ja toisia tiedostoja. Prosessin käynnistyminen ei tarkoita palvelun olevan heti valmis; discovery ja uudelleenyritykset hoidetaan erikseen.

**Tarkista valmius havainnoimalla:** `launch_ros.actions.Node` käynnistää kaksi **prosessia**, mutta DDS-löydettävyys ja ensimmäinen `/training/status`-viesti tulevat vasta sen jälkeen. Heti tehty `/training/count`-kutsu voi perustellusti palauttaa `received 0 samples`; laskuri kasvaa myöhemmin. Tämä ei todista kadonnutta transaktiota: service laskee vain monitorin vastaanottamat näytteet. `interval_s=1.0` luetaan ajastimen luonnissa eikä muuta jo toimivan ajastimen jaksoa automaattisesti.

<a id="section-7"></a>

## 7. tf2 ja koordinaatistot (coordinate frames)

**Ongelma:** Muunna kameran camera_link-koordinaateissa havaittu piste base_link- tai map-koordinaatteihin. tf2 säilyttää ja hakee aikaleimattuja siirto- ja kiertomuunnoksia. Kiinteät asennukset käyttävät staattisia ja liikkuvat nivelet dynaamisia muunnoksia. Parent/child-suhteiden ja aikaleimojen on täsmättävä. tf2 ei itse ratkaise suoraa tai käänteistä kinematiikkaa eikä reittisuunnittelua; katso koordinaatisto- ja Jacobian-luvut.

[Coordinate frames](04-coordinate-frames.md) · [Velocity and Jacobian](05-velocity-jacobian.md)

**Esimerkki koordinaatistoketjusta (ei pakollinen rakenne):** `map → odom → base_link → camera_link`. Kiinteästi runkoon asennetun kameran muunnos on `static`, mutta liikkuvan alustan muunnokset ovat `dynamic`. Kun kamera havaitsee pisteen `camera_link`-koordinaatistossa hetkellä *t*, tf2:n on löydettävä ketju `map`-koordinaatistoon **juuri mittaushetkellä**. Puuttuva koordinaatisto, katkennut puu tai puuttuva ajankohta aiheuttaa lookup-/extrapolation-virheen. Uusimman muunnoksen käyttäminen vanhaan havaintoon voi antaa väärät koordinaatit.

**Esimerkki muunnoksen suunnasta ja käänteismuunnoksesta.** Olkoon `base_link` (B) emokoordinaatisto ja `tool` (T) lapsikoordinaatisto. Ilman suhteellista kiertoa ja 0.1 m siirtymällä emon positiiviseen X-suuntaan työkalun origo on **B:n koordinaateissa perusorigon edessä**. T:stä katsottuna sama etäisyys on vastakkaismerkkinen:

$$
{}^{B}\mathbf p_{T}=(0.1, 0, 0)\ \mathrm{m},\qquad
{}^{T}\mathbf p_{B}=(-0.1, 0, 0)\ \mathrm{m}\quad (R=I).
$$

Pelkkä etumerkin vaihtaminen toimii vain, kun koordinaatistojen **suunta on sama**. Yleensä pistettä muunnettaessa tarvitaan sekä kierto että siirto. Käänteismuunnoksen on kumottava **molemmat**; aidon kiertomatriisin käänteismatriisi on $R^T$:

$$
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT},\qquad
\mathbf p_T=R_{BT}^{T}(\mathbf p_B-\mathbf t_{BT}),\qquad
\mathbf t_{TB}=-R_{BT}^{T}\mathbf t_{BT}.
$$

Toisessa asennossa T on kierretty +90° yhteisen Z-akselin ympäri, mutta siirtymä B:ssä pysyy (0.1 m, 0 m). B:n origo ilmaistuna T:ssä on silloin (0 m, +0.1 m), **ei** (−0.1 m, 0 m). Samalla matriisilla muunnetaan myös piste (0 m, 0.05 m) T:stä B:hen:

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

Koordinaatistot ja muunnokset **kuvaavat koordinaatteja**, eivät anna moottorille liikkumiskäskyjä. ROS 2:n siirtymissä käytetään yleensä metrejä; [koordinaatistojen opetusluku](04-coordinate-frames.md#section-3) käyttää millimetrejä, joten yksiköt on muunnettava ennen lukujen yhdistämistä. Staattiset muunnokset kuvaavat kiinteitä asennuksia ja dynaamiset tulevat tilaa päivittäviltä komponenteilta. Historialliset mittaukset edellyttävät mittaushetken muunnosta ja puuttuvien tietojen käsittelyä.

<a id="section-8"></a>

## 8. URDF ja robot_state_publisher

**Ongelma:** Kuvaa robotin rakenne yhteisesti käytettävällä mallilla. URDF määrittää links-, joints-, origot, akselit sekä valinnaiset visual/collision/inertial-ominaisuudet. robot_state_publisher yhdistää URDF:n nivelen asentoihin (yleensä /joint_states, sensor_msgs/msg/JointState) ja julkaisee muunnokset. URDF ei mittaa enkoodereita, simuloi tai ratkaise käänteistä kinematiikkaa. Pidä m, rad, akselit ja ajat yhtenäisinä.

**Muunnosten alkuperä:** URDF kuvaa `fixed`-nivelet ja liikkuvat nivelet. `robot_state_publisher` julkaisee kiinteästä geometriasta `static`-muunnokset ja käyttää `/joint_states`-viestin (`sensor_msgs/msg/JointState`) nivelasentoja liikkuvien nivelten `dynamic`-muunnoksiin. URDF **ei mittaa** nivelasentoja eikä korvaa puuttuvia anturitietoja. Pituudet ilmoitetaan metreinä, kulmat radiaaneina ja aikaleimojen on oltava johdonmukaisia.

<a id="section-9"></a>

## 9. ros2_control ja laitteistoraja

**Ongelma:** Erota säätöalgoritmit laiteajureista. ros2_control tarjoaa controller managerin, state interfaces (asento/nopeus), command interfaces (asento/nopeus/effort) ja laitteistoabstraktiot. Suunnittelija→säädin→laiterajapinta→laite, paluutieto kulkee tilarajapinnoissa. ROS-viesti ei takaa kovaa reaaliaikaisuutta, virranrajoitusta tai turvallista pysäytystä. Tässä esimerkissä ei ohjata toimilaitteita.

[First-order dynamics](02-first-order-dynamics.md) · [Feedback PID](03-feedback-control.md)

**Controller managerin tehtävä:** `controller_manager` hallitsee säätimien elinkaarta ja resurssienhallinnan kautta niiden pääsyä tilarajapintoihin (state interfaces) ja komentorajapintoihin (command interfaces). Säädin voi lukea mitattua tilaa, esimerkiksi kuvitteellista `joint1/position`-arvoa; aktiivinen säädin voi varata yhteensopivan komentorajapinnan tavoitearvon kirjoittamiseen. Mitattu tila ei ole sama kuin pyydetty arvo, eivätkä kaksi säädintä voi vapaasti varata samaa jo käytössä olevaa komentorajapintaa. Aktivointi ja resurssien omistus ovat eri asia kuin topic discovery.

**Harjoituksen rajaus:** `/training/status` ja `/training/count` havainnollistavat vain topic- ja service-viestintää, **eivät `ros2_control`-järjestelmää**. Kumpikaan node ei ole säädin, eikä harjoituksessa käynnistetä `controller_manager`-komponenttia, laiterajapintaa tai suljettua säätöpiiriä. Onnistunut smoke test ei siis testaa säätimien elinkaarta, reaaliaikaisuutta eikä laiteturvallisuutta. Katso [ros2_controlin virallinen johdanto](https://control.ros.org/jazzy/doc/getting_started/getting_started.html).

**Jatkoharjoitus: ros2_control ja TF2 ilman GUI:ta virtuaalinivelellä:** [Jatkoharjoitus: ros2_control ja TF2 ilman GUI:ta virtuaalinivelellä](07-ros2-control-lab.md). Uusi harjoitus kattaa URDF:n, GenericSystemin, komennot, tilat, /joint_states-aiheen, TF2:n, QoS:n ja ARM64-lataajan vianmäärityksen; oikeita laitteita ei ohjata.

**Seuraava askel: kokonaisarkkitehtuuri.** [Viiden vaiheen Mermaid-kaavio](08-ros2-robot-architecture.md) yhdistää havainnoinnin, aikaleimatun TF2:n, suunnittelun, ohjauksen ja palautteen. Laitteistoketju on käsitteellinen.

<a id="section-10"></a>

## 10. QoS, DDS discovery ja Docker

**Ongelma:** Selvitä viestihäviöt ja näkymättömät solmut. QoS-asetuksiin kuuluvat reliable/best_effort, volatile/transient_local, history ja depth. Jos subscriber vaatii enemmän luotettavuutta kuin publisher tarjoaa, viestejä ei välttämättä tule oikeasta nimestä ja tyypistä huolimatta. DDS käyttää usein UDP-multicastia ja dynaamisia portteja; Docker Desktop, VPN ja palomuurit voivat estää löytämisen. ROS_DOMAIN_ID:n on vastattava. Harjoitus toimii yhdessä kontissa ilman etuoikeuksia tai isännän portteja.

**Esimerkki yhteensopimattomasta QoS-asetuksesta:** Publisher tarjoaa `best_effort`-toimituksen, mutta subscriber vaatii `reliable`-tason. Vaikka topicin nimi ja viestityyppi täsmäisivät ja päätepisteet näkyisivät, tilaaja voi jäädä **ilman viestejä**, koska pyydettyä takuuta ei tarjota. Päinvastoin `best_effort`-tilaaja voi vastaanottaa `reliable`-julkaisijalta, kun muut QoS-asetukset ovat yhteensopivia. `volatile` ei toista aiempia viestejä; `transient_local` voi tarjota rajatun historian edelleen saatavilla olevalta yhteensopivalta julkaisijalta, **ei pysyvää hajautettua lokia**.

**Vianhaku järjestyksessä:** Tarkista `ROS_DOMAIN_ID=42` saman kontin sisällä ja suorita `ros2 node list`, `ros2 topic info /training/status -v` (päätepisteet ja QoS) sekä `docker compose logs demo` (prosessien tila). Jos graafi on edelleen tyhjä, tarkista RMW/DDS, verkkoliitännät ja palomuuri. TCP-porttien julkaisu ei ratkaise yleisesti DDS-ongelmia; eri koneiden välistä liikennettä ei ole testattu.

[ROS 2 Jazzy -version virallinen QoS-dokumentaatio](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)

[Vaihtoehto: virallinen ROS-image ilman Composea tai omaa Dockerfileä](../../../ros2/PLAIN_DOCKER.md)

<a id="section-11"></a>

## 11. Harjoitus: kaksi solmua, topic, service ja launch

Käynnistä docker compose up --build -d. Lokeissa pitäisi näkyä lähetettyjä ja vastaanotettuja sample-viestejä sekä kasvava laskuri. Palvelu vastaa success=True ja esimerkiksi received 12 samples; numero riippuu ajankohdasta. Erillinen [GitHub Actionsin Docker-smoketesti](../../../.github/workflows/ros2-live-smoke.yml) **käynnisti sovelluksen oikeasti yhdessä kontissa** ja tarkisti molemmat ROS-solmut, tyypitetyn viestin vastaanoton aiheesta `/training/status` sekä palvelun `/training/count` vastauksen. Tavallinen tarkistus-CI ei suorita ROSia. Testit eivät varmista DDS-yhteyksiä eri koneiden välillä, determinististä reaaliaikatoimintaa, fyysisiä laitteita tai lukijan paikallista Docker-asennusta.

[Source, expected results and troubleshooting](../../../ros2/README.md). From the repository root:

Opiskele järjestyksessä: ensin asennetut `demo_nodes_cpp`-talker ja `demo_nodes_py`-listener, sitten repositorion oma `telemetry_demo` ja vasta lopuksi `ros2_control`. Dockerfile asentaa tavalliset demot APT:llä ja rakentaa `telemetry_demo`-paketin `colcon`-työkalulla. Avaa vuorovaikutteiseen käyttöön **yksi Bash-shell** ja source ympäristöt **kerran jokaista uutta shelliä kohti**; erillinen `docker compose exec` ei peri `CMD`-prosessin shell-ympäristöä.

Käynnistä kontti isäntäkoneessa ja avaa vuorovaikutteinen shell:

```bash
cd ros2
docker compose up --build -d
docker compose logs --tail=20 demo
docker compose exec demo bash
```

Lataa ympäristöt kerran kontin sisällä (ei isäntäkoneessa) ja tarkista ROS-graafi:

```bash
echo "$ROS_DISTRO"
ros2 node list
ros2 service call /training/count std_srvs/srv/Trigger "{}"
exit
```

Palaa `exit`-komennolla isäntäkoneeseen ja lopeta:

```bash
docker compose down
```

**CI:n luottamusraja:** ROS 2:n todellinen Docker-savukoe käynnistyy nyt automaattisesti vasta, kun asiaankuuluvat muutokset on yhdistetty `main`-haaraan, tai manuaalisesti `workflow_dispatch`-toiminnolla `main`-haarassa. Sitä ei suoriteta `pull_request`-muutoksille, sillä muuten runner-isäntä ajaisi PR:n muokkaamaa Bash-skriptiä ja Dockerfile-ohjeita suoraan. Eristetyt Python-tarkistukset ennen yhdistämistä eivät korvaa oikeaa ROS-ajoa. Muutokset on arvioitava riippumattomasti ennen yhdistämistä ja ajotestin tulos tarkistettava sen jälkeen.

<a id="section-12"></a>

## 12. Sanasto ja rajoitukset

- **Node / prosessi:** Node on nimetty looginen ROS-osa; yhdessä käyttöjärjestelmäprosessissa voi toimia useita solmuja.
- **ROS graph:** Kulloinkin löydettyjen viestintäpisteiden joukko, ei pysyvä keskitetty rekisteri tai käyttöoikeuksien tarkistus.
- **Topic:** Nimetty asynkroninen tietovirta, jossa voi olla useita julkaisijoita ja tilaajia.
- **Message:** ROS-rajapinnan määrittämä tyypitetty tietorakenne, ei mikä tahansa Python- tai C++-olio.
- **Publisher / subscriber:** Topic-viestien lähettäjä ja vastaanottaja; toimitus vaatii discovery-toiminnon ja yhteensopivan QoS:n.
- **Service:** Tyypitetty lyhyt pyyntö/vastaus; timeout ei todista, ettei palvelin suorittanut toimintoa.
- **Action:** Tavoite, feedback, tulos ja peruutuspyyntö; peruutuspyyntö ei takaa välitöntä pysähtymistä.
- **Parameter:** Yksittäisen solmun omistama asetus; muutos ei automaattisesti päivitä jo luotua ajastinta.
- **RMW / DDS:** RMW abstrahoi väliohjelmiston; DDS on yleinen löytämis- ja siirtotekniikka, ei itsessään tunnistautuminen.
- **colcon / ament:** Workspace-koonnin ohjaus / ROS-paketin koonti-integraatio, ei viestinvälityskerros.
- **Launch:** Käynnistettävien prosessien ja asetusten kuvaus; käynnistyminen ei takaa valmiutta.
- **tf2:** Aikaleimattujen koordinaattimuunnosten infrastruktuuri, ei käänteisen kinematiikan ratkaisija.
- **URDF / robot_state_publisher:** Robotin rakennemalli / muunnosten julkaisu mallin ja nykyisten niveltilojen avulla.
- **ros2_control:** Säätimien elinkaari ja resurssien hallitsemat state/command-rajapinnat; ei osa tätä topic/service-harjoitusta.
- **QoS:** Pyydettyjen ja tarjottujen toimitus- ja historiakäytäntöjen yhteensopivuus, ei pysyvä tapahtumaloki tai turvallisuussertifikaatti.

**Versiot tarkistettu 13. marraskuuta 2026:** ROS 2 Jazzy LTS:n tuki jatkuu toukokuuhun 2029 ja Lyrical LTS:n toukokuuhun 2031. Docker-tunniste ei lukitse muuttumatonta levykuvan digest-arvoa eikä apt-pakettiversioita.

**Primary sources:** [ROS 2 releases](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst) · [Jazzy documentation](https://docs.ros.org/en/jazzy/) · [tf2](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html) · [URDF](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html) · [ros2_control](https://control.ros.org/jazzy/)
