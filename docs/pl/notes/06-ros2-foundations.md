# 6. ROS 2: rozproszone oprogramowanie robota — od grafu do interfejsów sprzętowych

**Języki:** [en](../../en/notes/06-ros2-foundations.md) · [fr](../../fr/notes/06-ros2-foundations.md) · [de](../../de/notes/06-ros2-foundations.md) · [it](../../it/notes/06-ros2-foundations.md) · [es](../../es/notes/06-ros2-foundations.md) · [pt](../../pt/notes/06-ros2-foundations.md) · [zh](../../zh/notes/06-ros2-foundations.md) · [ja](../../ja/notes/06-ros2-foundations.md) · [nb](../../nb/notes/06-ros2-foundations.md) · [ru](../../ru/notes/06-ros2-foundations.md) · [ko](../../ko/notes/06-ros2-foundations.md) · [fi](../../fi/notes/06-ros2-foundations.md) · [pl](06-ros2-foundations.md)

**Jednostki używane w tej lekcji (objaśnione przed przykładami):** `m` — metr (długość); `s` — sekunda (czas). [Pełny słownik jednostek](../UNITS.md).

[Spis treści](../README.md) · [Układy współrzędnych](04-coordinate-frames.md) · [Prędkość i jakobian](05-velocity-jacobian.md) · [Laboratorium Docker](../../../ros2/README.md)

> **Zakres:** to wyłącznie pojęcia i symulacja programowa. Polecenia i przykłady nie nadają się do sterowania prawdziwymi robotami. Komunikacja ROS nie zastępuje bezpieczeństwa sprzętowego, sterowania ruchem, kinematyki ani projektowania czasu rzeczywistego.

ROS 2 to środowisko i ekosystem służące **łączeniu rozproszonych komponentów oprogramowania robota**. Jeśli znasz backend, możesz myśleć o węzłach jak o procesach wystawiających typowane asynchroniczne strumienie i interfejsy żądanie–odpowiedź. To przydatna analogia, ale ROS 2 nie jest HTTP, płaszczyzną sterowania Kubernetes ani obowiązkowym centralnym brokerem. Wykorzystuje **graf** wykrywanych punktów komunikacji ponad warstwą pośredniczącą; typowe konfiguracje używają DDS/RTPS. Biblioteki realizują algorytmy, natomiast ROS zapewnia komunikację, cykl życia i narzędzia.

![Graf ROS 2: publikujący i subskrybent jednego tematu oraz klient i serwer usługi.](../../../assets/figures/ros2-topic-service.svg)

![Warstwy oprogramowania ROS 2 oddzielone od niskopoziomowego sprzętu i bezpieczeństwa.](../../../assets/figures/ros2-software-layers.svg)

*Warstwy aplikacyjne i middleware są odrębne od mechanizmów czasowych urządzenia i zabezpieczeń.*

## Ścieżka nauki

1. [Architektura i graf ROS](#section-1)
2. [Węzły, tematy i komunikaty typowane](#section-2)
3. [Usługi, akcje i parametry](#section-3)
4. [Pakiety, obszary robocze, colcon i ament](#section-4)
5. [CLI: wykrywanie i diagnoza grafu](#section-5)
6. [Pliki launch i konfiguracja](#section-6)
7. [tf2 i układy współrzędnych](#section-7)
8. [URDF i robot_state_publisher](#section-8)
9. [ros2_control i granica sprzętowa](#section-9)
10. [QoS, wykrywanie DDS i sieć Docker](#section-10)
11. [Uruchomienie niewielkiej kompletnej aplikacji](#section-11)
12. [Słownik, ograniczenia i źródła](#section-12)

<a id="section-1"></a>
## Lekcja 1. Architektura: graf nie jest centralnym serwerem

**Problem inżynierski:** robot łączy oprogramowanie kamer, lokalizacji, planowania, wizualizacji i napędów, często na różnych komputerach. Komponenty potrzebują zgodnych interfejsów, nie muszą być jednym ogromnym programem.

**ROS** oznacza Robot Operating System, ale nie jest jądrem systemu ani systemem operacyjnym. ROS 1 zwykle używał centralnego *mastera* do wykrywania nazw i innej architektury transportowej. ROS 2 stosuje warstwę abstrakcji middleware (**RMW**) nad implementacjami opartymi często na **DDS** (*Data Distribution Service*). Uczestnicy mogą wykrywać się bez centralnego mastera ROS 1. Rozproszone wykrywanie nie oznacza jednak, że każda sieć zadziała automatycznie.

**Graf ROS (ROS graph)** to aktualnie wykryty zbiór węzłów, tematów, usług i akcji. Węzeł jest logicznym komponentem obliczeniowym; w jednym procesie może działać kilka węzłów, a jeden węzeł może udostępniać wiele punktów komunikacji. Procesy mogą działać lokalnie lub na wielu komputerach. Przestrzenie nazw, remapping i domeny ROS pomagają izolować grupy węzłów. Nie traktuj wykrywania jako mechanizmu autoryzacji ani ochrony bezpieczeństwa.

**Porównanie z backendem:** temat przypomina typowany strumień zdarzeń, usługa — RPC, plik launch — konfigurację nadzorcy procesów, a QoS — ustawienia polityki dostarczania. Są to przybliżenia: wykrywanie DDS i ROS QoS różnią się od Kafka, HTTP i brokerów kolejek.

<a id="section-2"></a>
## Lekcja 2. Węzły, tematy i komunikaty

**Problem inżynierski:** czujnik albo symulacja wytwarza serię pomiarów, których potrzebuje wielu odbiorców bez odpytywania producenta.

**Publikujący (publisher)** wysyła typowane komunikaty przez nazwany **temat (topic)**, a **subskrybent (subscriber)** odbiera je asynchronicznie. Nazwa `/training/status` nie jest unikalnym adresem gniazda: mechanizm wykrywania dopasowuje zgodnych publikujących i subskrybentów. Typ musi się zgadzać, na przykład `std_msgs/msg/String` zawiera jedno pole `string data`. Wygenerowane wiązania Pythona i C++ udostępniają tę samą definicję interfejsu ROS — nie przesyła się dowolnych obiektów środowiska uruchomieniowego języka.

Ćwiczenie uruchamia **dwa oddzielne procesy**. `/sample_source` publikuje `sample 1`, `sample 2`, ...; `/sample_monitor` subskrybuje i zwiększa licznik. Oba ustawiają głębokość 10, ale żaden nie tworzy trwałego archiwum. Nowi subskrybenci zwykle otrzymują **przyszłe** próbki. W czasie startu licznik odebranych próbek może się różnić od numeru sekwencji publikującego.

**Kiedy wybrać temat:** ciągły status, obrazy, stany przegubów, odometria lub telemetria. Temat nie jest właściwą abstrakcją dla żądania z jedną natychmiastową odpowiedzią ani dla długiej operacji wymagającej anulowania i statusu zakończenia.

**Przykład wykrywania:** załóżmy, że `/sample_source` nadał już `sample 1`, zanim `/sample_monitor` został wykryty. Przy historii `volatile` starsza próbka nie zostanie automatycznie odtworzona. Monitor może początkowo zwrócić `received 0 samples` mimo ciągłej pracy publikującego. Gdy zgodne punkty komunikacji się wykryją, licznik może rosnąć. Numer publikowanej sekwencji i liczba odebranych próbek opisują różne rzeczy; żadna nie oznacza transakcji z potwierdzeniem.

**Co potwierdza CLI:** `ros2 topic list -t` wyświetla wykryte nazwy i typy tematów, ale **nie dowodzi**, że subskrybent otrzymuje dane. `ros2 topic info /training/status -v` podaje wykryte punkty i ich oferowane/żądane QoS. Zero subskrypcji może oznaczać brak subskrybenta **albo** niezakończone wykrywanie. Jeżeli punkty istnieją, a danych brak, sprawdź typy komunikatów i zgodność QoS, następnie logi i `ROS_DOMAIN_ID`. Są to tylko obserwacje chwilowe, nie gwarancja dostarczenia. Uruchamiaj polecenia w kontenerze ćwiczeniowym, nie w odrębnej sieci hosta.

<a id="section-3"></a>
## Lekcja 3. Usługi, akcje i parametry

**Problem inżynierski:** strumienie danych, szybkie zapytania i długo wykonywane operacje różnią się sposobem komunikacji i obsługi błędów.

| Mechanizm | Przepływ | Zastosowanie | Nie należy utożsamiać z |
| --- | --- | --- | --- |
| Topic | Publikujący → 0..N subskrybentów | Powtarzalny stan / telemetria | Trwała kolejka lub transakcja z potwierdzeniem |
| Service | Klient → żądanie → serwer → odpowiedź | Krótkie zapytanie lub ograniczona operacja | Gwarantowany zdalny commit albo długie zadanie |
| Action | Klient → cel; serwer → postęp/wynik; opcjonalne anulowanie | Cel nawigacyjny lub długie obliczenie | Zwykły okresowy strumień czujnika |
| Parameter | Nazwana wartość należąca do węzła | Konfiguracja, np. okres próbkowania | Globalna rozproszona baza danych |

Monitor udostępnia `/training/count` jako `std_srvs/srv/Trigger`. Żądanie nie ma pól; odpowiedź zawiera `success` (wartość logiczna) i `message` (tekst), na przykład `received 12 samples`. Dostępność usługi i zwrócony stan to osobne kwestie. Usługa może przekroczyć limit czasu, a kod aplikacji musi zdecydować, czy ponowienie żądania jest bezpieczne. Dla akcji powtarzanie celu i anulowanie także wymagają jawnej polityki aplikacyjnej.

Publikujący deklaruje parametr `double` o nazwie `interval_s=1.0`, odczytywany przy starcie. Późniejsza zmiana parametru **nie przebudowuje automatycznie timera**: aplikacja musi obsłużyć zmianę. Parametr należy do węzła, a nie do globalnej bazy konfiguracji.

<a id="section-4"></a>
## Lekcja 4. Pakiety, obszary robocze, colcon i ament

**Problem inżynierski:** aplikacja robota łączy wersjonowane biblioteki, programy węzłów, wygenerowane typy komunikatów, pliki launch i zależności uruchomieniowe.

**Pakiet (package)** jest jednostką budowania, instalowania i wykrywania. **Obszar roboczy (workspace)** ma zwykle katalogi `src/`, `build/`, `install/` i `log/`. Narzędzie **colcon** koordynuje kompilację pakietów. **ament_python** i **ament_cmake** są integracjami systemów budowania, a nie magistralą komunikatów. Środowisko zawiera zainstalowaną bazę ROS (**underlay**) i ewentualnie nakładkę lokalnego obszaru roboczego (**overlay**).

W przykładzie `ros2/demo_pkg/package.xml` deklaruje `rclpy`, `std_msgs`, `std_srvs` i zależności uruchamiania. Plik `setup.py` wystawia skrypty konsolowe `sample_source`, `sample_monitor` i instaluje plik launch. W rzeczywistym `ros2/Dockerfile` **budowanie obrazu** (`RUN`) i **start kontenera** (`CMD`) to różne etapy. Podczas budowania źródłujemy jedynie underlay ROS, zanim `colcon` skompiluje pakiet:

**Budowanie obrazu (`RUN`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
colcon build --packages-select telemetry_demo
```

**Start kontenera (`CMD`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
source /opt/training_ws/install/setup.bash
exec ros2 launch telemetry_demo demo.launch.py
```

Gdy kontener rusza, nowa powłoka ponownie ładuje środowisko ROS (underlay), potem overlay zbudowanego obszaru i uruchamia plik launch. `package.xml` deklaruje zależności, natomiast `setup.py` instaluje dwa punkty wejścia Pythona i plik launch. `build/` oraz `install/` to wygenerowane katalogi, nie miejsce edycji źródeł. Pomyślna kompilacja sama nie potwierdza działania wykrywania w runtime.

W nowej powłoce zawsze ładuj **najpierw underlay, potem overlay**. Jeśli zainstalowany pakiet nie jest wykrywany, przyczyną bywa błędne załadowanie środowiska, brak instalacji plików danych lub problem przy budowaniu. Katalog `install` zawiera wynik budowania, nie kod źródłowy.

<a id="section-5"></a>
## Lekcja 5. CLI: sprawdzaj to, co naprawdę działa

**Problem inżynierski:** w rozproszonym programie potrzebujesz ustalić, które komponenty faktycznie działają, zamiast ufać samej konfiguracji.

Po uruchomieniu [laboratorium Docker](../../../ros2/README.md) wykonaj poniższe polecenia **wewnątrz działającego kontenera**, po załadowaniu ROS i obszaru roboczego:

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
ros2 param list /sample_source
ros2 param get /sample_source interval_s
```

Oczekiwane są dwa węzły aplikacji, temat `/training/status [std_msgs/msg/String]`, nowe wiadomości tekstowe, usługa `/training/count [std_srvs/srv/Trigger]`, odpowiedź ze zmieniającym się licznikiem oraz `Double value is: 1.0`. W demonstracji **nie ma własnej akcji**. CLI może chwilowo pojawić się jako dodatkowy węzeł. Jeśli `ros2 topic echo` nie wypisuje niczego, być może czeka na następną próbkę; przerwij Ctrl+C.

Najpierw sprawdzaj **nazwy i typy**, potem **liczbę punktów komunikacji i QoS**, a następnie **domenę i wykrywanie sieciowe**. Pusty graf nie dowodzi, że wszystkie procesy są wyłączone — możesz być w innej domenie ROS lub sieci kontenera.

<a id="section-6"></a>
## Lekcja 6. Pliki launch

**Problem inżynierski:** uruchamianie wielu węzłów z odpowiednimi nazwami, parametrami i ustawieniami startowymi powinno być powtarzalne.

Opis startowy Pythona tworzy akcje `launch_ros.actions.Node` i uruchamia niezależne programy. `launch/demo.launch.py` uruchamia producenta i monitor, przekazując `interval_s=1.0` do producenta. Uruchom `ros2 launch telemetry_demo demo.launch.py` po załadowaniu środowiska albo użyj gotowego polecenia kontenera.

Pliki launch mogą włączać inne pliki launch, definiować argumenty, przestrzenie nazw, remapping tematów i parametry. **Start nie gwarantuje gotowości**: kolejność uruchamiania, wykrywanie, pierwsze dane i ponowienia nadal mają znaczenie. Rozróżniaj uruchomienie dwóch *węzłów* od uruchomienia dwóch *procesów*; w tym przykładzie uruchamiane są oba.

**Obserwuj gotowość zamiast jej zakładać:** `launch_ros.actions.Node` uruchamia dwa **procesy**, a wykrywanie grafu DDS i pierwsza próbka `/training/status` pojawiają się później. Natychmiastowe wywołanie `/training/count` może prawidłowo zwrócić `received 0 samples`, a późniejsze większą liczbę. Nie dowodzi to utraty transakcji: usługa podaje tylko licznik próbek odebranych przez monitor. `interval_s=1.0` określa timer w chwili tworzenia, a nie mechanizm zmiany okresu w trakcie działania.

<a id="section-7"></a>
## Lekcja 7. tf2 i układy współrzędnych

**Problem inżynierski:** kamera wykrywa punkt we własnym układzie, ale nawigacja i manipulacja potrzebują współrzędnych w bazie lub świecie.

**Układ odniesienia (frame)** to nazwany układ współrzędnych, np. `map`, `odom`, `base_link`, `camera_link`. **tf2** przechowuje zależności transformacji ze znacznikami czasu i odpowiada na zapytania dotyczące konkretnego czasu. Transformacje obejmują obrót i przesunięcie; poprawne drzewo ramek ma spójne relacje rodzic–dziecko. Transformacje statyczne (static) nadają się do nieruchomych mocowań, a ruchome przeguby wymagają dynamicznych (dynamic). Ważne są synchronizacja czasu oraz błędy wyszukiwania (lookup) lub ekstrapolacji (extrapolation).

Matematykę przeliczenia punktu lokalnego na współrzędne świata znajdziesz w [lekcji o układach](04-coordinate-frames.md). Pochodne i prędkości końcówki omówiono w [lekcji o jakobianie](05-velocity-jacobian.md). **tf2 to infrastruktura publikowania i odpytywania transformacji; sam nie wyprowadza kinematyki prostej/odwrotnej ani nie planuje ruchu.** Te obliczenia są wykonywane w innych komponentach.

**Przykładowy łańcuch (nieobowiązkowy):** `map → odom → base_link → camera_link`. Kamera sztywno zamocowana do bazy ma **statyczną** transformację montażową, a poruszająca się baza wymaga transformacji **dynamicznych**. Aby zinterpretować punkt z `camera_link` zaobserwowany w chwili *t*, tf2 potrzebuje łańcucha do `map` **w czasie pomiaru**. Brak ramki, niespójne drzewo lub nieosiągalny znacznik czasu powodują błąd wyszukiwania/ekstrapolacji. Bezrefleksyjne użycie najnowszej transformacji może błędnie pozycjonować historyczne pomiary.

**Przykład kierunku transformacji i odwrotności.** `base_link` (B) to układ nadrzędny, a `tool` (T) podrzędny. Bez obrotu względnego i z przesunięciem 0.1 m wzdłuż dodatniej osi X rodzica początek narzędzia znajduje się **przed początkiem bazy, gdy opisujemy go w B**. Ten sam odcinek w układzie T ma przeciwny znak:

$$
{}^{B}\mathbf p_{T}=(0.1, 0, 0)\ \mathrm{m},\qquad
{}^{T}\mathbf p_{B}=(-0.1, 0, 0)\ \mathrm{m}\quad (R=I).
$$

Proste odwrócenie znaku działa wyłącznie wtedy, gdy oba układy mają **taką samą orientację**. Ogólnie współrzędne punktu wynikają z obrotu i translacji. Transformacja odwrotna musi cofnąć zarówno przesunięcie, **jak i obrót**; $R^T$ jest odwrotnością poprawnej macierzy obrotu:

$$
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT},\qquad
\mathbf p_T=R_{BT}^{T}(\mathbf p_B-\mathbf t_{BT}),\qquad
\mathbf t_{TB}=-R_{BT}^{T}\mathbf t_{BT}.
$$

W innej pozie obróćmy T o +90° wokół wspólnej osi Z, przy zachowanym przesunięciu (0.1 m, 0 m) w B. Początek B opisany w T wynosi wtedy (0 m, +0.1 m), **a nie** (−0.1 m, 0 m). Te same macierze przeliczają punkt (0 m, 0.05 m) w T:

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

Ramki i transformacje opisują współrzędne, nie polecenia ruchu narzędzia. W ROS 2 translacje podajemy w metrach; osobna [lekcja o układach współrzędnych](04-coordinate-frames.md#section-3) celowo używa milimetrów, więc trzeba przeliczyć wartości przed łączeniem przykładów. Transformacja statyczna opisuje niezmienne mocowanie; dynamiczna powinna pochodzić od właściwego źródła stanu. Pomiary historyczne odczytuj z ich znacznikami czasu i obsługuj brak danych.

<a id="section-8"></a>
## Lekcja 8. URDF i robot_state_publisher

**Problem inżynierski:** wiele narzędzi potrzebuje wspólnego opisu korpusów i przegubów robota, zamiast osobnego kodowania mechanizmu w każdym programie.

**URDF** (*Unified Robot Description Format*) opisuje człony (links) i przeguby (joints), ich początki i osie, relacje stałe oraz ruchome, a opcjonalnie też własności wizualne, kolizyjne i bezwładnościowe. **robot_state_publisher** wykorzystuje model URDF i położenia przegubów (zwykle `sensor_msgs/msg/JointState` na `/joint_states`) do publikowania transformacji ramek. Przeguby sztywne mogą tworzyć transformaty statyczne, a ruchome zależą od stanu przegubów. Drzewo TF jest wynikiem modelu i pomiarów.

Sam URDF **nie** dostarcza pomiarów przegubów, testów kolizji, sterowania ze sprzężeniem zwrotnym, algorytmu kinematyki odwrotnej ani symulacji fizyki. Układy współrzędnych, jednostki (zwykle metry i radiany), kolejność przegubów i znaczniki czasu muszą być spójne. Później możesz wizualizować *syntetyczny* model URDF dwóch członów; pierwsze laboratorium Docker celowo nie wymaga robota ani sterownika.

**Skąd pochodzą transformaty:** URDF opisuje przeguby `fixed` i ruchome. `robot_state_publisher` używa stałej geometrii do tworzenia transformacji `static`, a położeń z `/joint_states` (`sensor_msgs/msg/JointState`) do transformacji `dynamic` dla ruchomych przegubów. Plik URDF nie mierzy położenia przegubów ani nie tworzy brakujących pomiarów; poprawna geometria nie naprawi brakujących czy przestarzałych stanów. Zachowuj metry, radiany i spójne znaczniki czasu.

<a id="section-9"></a>
## Lekcja 9. ros2_control i granica sprzętowa

**Problem inżynierski:** planery wysokiego poziomu nie powinny być na sztywno związane z konkretnym sterownikiem silnika, a cykle aktualizacji sterownika nie mogą zależeć od zwykłego strumienia tematów o niegwarantowanym czasie dostarczenia.

**ros2_control** definiuje zarządzanie kontrolerami, **interfejsy stanu (state interfaces)** (np. pomiar położenia i prędkości przegubu), **interfejsy poleceń (command interfaces)** (np. wartości zadane położenia, prędkości lub momentu) oraz wymienne abstrakcje sprzętowe. Typowy łańcuch: planer lub węzeł nadzorczy → menedżer/kontroler → interfejs sprzętowy → urządzenie/obiekt, ze sprzężeniem zwrotnym przez interfejsy stanu. Ograniczenia bezpieczeństwa, watchdog, elektronika mocy, protokoły urządzeń i deterministyczne cykle niskiego poziomu to osobne zadania projektowe.

Węzeł ROS nadający temat z prędkością **nie gwarantuje** deterministycznego czasu, regulacji prądu ani bezpiecznego zatrzymania. Ograniczenia czasu rzeczywistego wymagają projektowania i weryfikacji w rzeczywistym stosie sterowania, często niżej niż zwykła aplikacja ROS. Ten rozdział nie zawiera sterowników, prawdziwych poleceń silnika, nastaw regulatora ani zgody na użycie demonstracji ze sprzętem.

Znaczenie fizyczne momentu i sprzężenia zwrotnego omówiono w [dynamice pierwszego rzędu](02-first-order-dynamics.md) oraz [sterowaniu PID](03-feedback-control.md).

**Rola menedżera kontrolerów:** `controller_manager` zarządza cyklem życia kontrolerów, a poprzez menedżera zasobów dostępem do interfejsów stanu i poleceń. Kontroler może odczytywać stan, np. `joint1/position`; aktywny kontroler może zarezerwować zgodny interfejs poleceń, aby wpisać żądaną wartość. Stan zmierzony nie jest poleceniem, a konkurencyjne kontrolery nie mogą po prostu przejąć już zarezerwowanego interfejsu. Liczą się więc aktywacja i własność zasobów, nie tylko wykrywanie tematów.

**Granice tego laboratorium:** `/training/status` i `/training/count` demonstrują temat i usługę, a nie `ros2_control`. Żaden z węzłów nie jest kontrolerem i ćwiczenie nie uruchamia `controller_manager`, interfejsu sprzętowego ani zamkniętej pętli sterowania. Pomyślny smoke test nie sprawdza cyklu życia kontrolerów, czasu fizycznego ani bezpieczeństwa urządzenia. Zobacz [oficjalne wprowadzenie do ros2_control](https://control.ros.org/jazzy/doc/getting_started/getting_started.html).

**Kolejne ćwiczenie: ros2_control i TF2 bez GUI z wirtualnym przegubem:** [Kolejne ćwiczenie: ros2_control i TF2 bez GUI z wirtualnym przegubem](07-ros2-control-lab.md). Nowe laboratorium obejmuje URDF, GenericSystem, polecenia, stany, /joint_states, TF2, QoS i diagnostykę loadera ARM64; nie steruje prawdziwym sprzętem.

**Następny krok: cała architektura robota.** [Edytowalny diagram Mermaid w pięciu etapach](08-ros2-robot-architecture.md) łączy percepcję, TF2 zależny od czasu, planowanie, sterowanie i sprzężenie zwrotne. Ścieżka sprzętu jest koncepcyjna.

<a id="section-10"></a>
## Lekcja 10. QoS, wykrywanie DDS i Docker

**Problem inżynierski:** przy różnych szybkościach publikujących i odbierających, a także wielu komputerach, trzeba dobrać opóźnienia i dostępność oraz zrozumieć, dlaczego graf może pozostać niewidoczny.

Zasady **QoS** (*Quality of Service*) obejmują niezawodność (`reliable` albo `best_effort`), trwałość historii (`volatile` albo `transient_local`), historię i głębokość kolejki. Zgodność jest kierunkowa: subskrybent żądający silniejszych gwarancji dostarczenia niż oferuje publikujący może **nie otrzymać żadnej wiadomości**, mimo identycznej nazwy i typu tematu. Większe kolejki przechowują więcej próbek, lecz nie tworzą nieskończonego trwałego dziennika ani gwarancji exactly-once. Strumień czujnika może preferować świeże dane, natomiast krytyczny interfejs poleceń wymaga osobno zaprojektowanego protokołu end-to-end.

**Wykrywanie DDS** zwykle obejmuje multicast i wybór interfejsu, a wymiana danych może używać dynamicznych portów UDP. Komunikacja na jednym hoście i w jednym kontenerze bywa prostsza niż przez mosty Dockera, maszyny wirtualne Docker Desktop, VPN-y, zapory lub wiele hostów. `ROS_DOMAIN_ID` musi się zgadzać; przykład stosuje `42`. **Opublikowanie portów TCP kontenera nie jest uniwersalnym rozwiązaniem problemów sieci DDS.** Wpływ mają też implementacja RMW/DDS i konfiguracja środowiska.

Dostarczona usługa Compose uruchamia publikującego, subskrybenta i CLI **w jednym kontenerze**. Nie wystawia portów hosta i nie używa sieci hosta, urządzeń ani trybu uprzywilejowanego. Nie testuje komunikacji DDS między hostami. Zanim zmienisz sieć, diagnozuj poleceniami `ros2 node list`, `ros2 topic info -v`, `docker compose logs demo` i sprawdź zmienne środowiskowe.

**Przykład niezgodności QoS:** publikujący oferuje `best_effort`, lecz subskrybent żąda `reliable`. Nazwa tematu i typ komunikatu mogą pasować, a wykrywanie pokazywać punkty komunikacji, jednak subskrybent **nie dostaje danych**, ponieważ żądana gwarancja nie jest oferowana. W przeciwną stronę subskrybent `best_effort` może zaakceptować publikującego `reliable`, jeśli pozostałe polityki QoS są zgodne. `volatile` nie odtwarza wcześniejszych próbek; `transient_local` pozwala oferować ograniczoną historię, póki zgodny publikujący jest dostępny, ale **nie** jest trwałym wspólnym dziennikiem zdarzeń.

**Diagnostyka w kolejności:** sprawdź `ROS_DOMAIN_ID=42` **wewnątrz tego samego kontenera**; uruchom `ros2 node list`, następnie `ros2 topic info /training/status -v` i przeanalizuj punkty oraz QoS, a potem `docker compose logs demo` dla procesów. Gdy graf jest niewidoczny, zbadaj wybór RMW/DDS, interfejsy kontenera i topologię zapór/sieci. Samo otwarcie portów TCP nie naprawia automatycznie DDS. To laboratorium nie sprawdza komunikacji wielohostowej.

[Alternatywa: oficjalny obraz ROS bez Compose i własnego Dockerfile](../../../ros2/PLAIN_DOCKER.md)

<a id="section-11"></a>
## Lekcja 11. Kompletna aplikacja syntetyczna

Skorzystaj z [laboratorium krok po kroku w Dockerze z ROS 2 Jazzy](../../../ros2/README.md). Znajdziesz w nim wszystkie źródła, `Dockerfile`, `compose.yaml`, manifest pakietu, publikującego, subskrybenta z usługą, konfigurację launch, polecenia, oczekiwane wyniki i diagnostykę. [Osobny workflow z testem ROS na żywo w Dockerze](../../../.github/workflows/ros2-live-smoke.yml) uruchamiał już tę aplikację **w jednym kontenerze** na runnerze GitHub Actions: sprawdził dwa węzły, odbiór typowanego komunikatu `/training/status` i pomyślne wywołanie `/training/count`. Zwykły job walidacji **nie uruchamia ROS**. Żaden z testów nie potwierdza wykrywania DDS między hostami, deterministycznego czasu, sprzętu ani instalacji Dockera na komputerze czytelnika.

Skrócona procedura, uruchamiana z katalogu głównego repozytorium:

Ucz się kolejno: od zainstalowanego talkera `demo_nodes_cpp` i listenera `demo_nodes_py`, następnie poznaj własny pakiet `telemetry_demo`, a na końcu przejdź do `ros2_control`. Dockerfile instaluje standardowe demonstracje przez APT i buduje `telemetry_demo` przez `colcon`. Do nauki interaktywnej otwórz **jedną powłokę Bash** i załaduj środowisko **raz w każdej nowej powłoce**: oddzielny `docker compose exec` nie dziedziczy środowiska powłoki z `CMD`.

Na hoście uruchom kontener i otwórz interaktywną powłokę:

```bash
cd ros2
docker compose up --build -d
docker compose logs --tail=20 demo
docker compose exec demo bash
```

W kontenerze (nie na hoście) załaduj środowiska raz i sprawdź graf ROS:

```bash
echo "$ROS_DISTRO"
ros2 node list
ros2 service call /training/count std_srvs/srv/Trigger "{}"
exit
```

Po `exit` wróć na host i zakończ działanie:

```bash
docker compose down
```

Publikujący wysyła kolejne napisy, subskrybent zlicza otrzymane, a usługa zwraca bieżącą liczbę. Nie uczestniczą żadne silniki, czujniki, interfejsy sprzętowe ani prywatna konfiguracja.

**Granica zaufania CI:** test ROS 2 w Dockerze jest uruchamiany automatycznie dopiero po przeniesieniu odpowiednich zmian do `main` albo ręcznie przez `workflow_dispatch` z `main`. Celowo **nie** działa dla przychodzących zmian `pull_request`, ponieważ runner hosta wykonywałby wtedy Bash i Dockerfile kontrolowane przez PR. Zwykłe izolowane testy Python PR nie zastępują rzeczywistego testu ROS. Przed merge potrzebna jest niezależna weryfikacja zmian, a po merge trzeba sprawdzić wynik testu live.

<a id="section-12"></a>
## Słownik i ograniczenia

- **Węzeł / proces (node / process):** węzeł jest nazwanym, logicznym komponentem ROS; proces systemowy może zawierać kilka węzłów.
- **Graf ROS (ROS graph):** bieżący zbiór wykrytych punktów komunikacji, a nie trwały centralny rejestr ani system autoryzacji.
- **Temat (topic):** nazwany strumień asynchroniczny z wieloma możliwymi publikującymi i subskrybentami.
- **Komunikat (message):** typowana struktura danych tematu, definiowana interfejsem ROS, a nie tożsamością obiektu Pythona czy C++.
- **Publikujący / subskrybent (publisher / subscriber):** nadawca i odbiorca komunikatów; przed dostarczaniem wymagane jest wykrywanie i zgodne QoS.
- **Usługa (service):** typowane żądanie i odpowiedź dla krótkiej interakcji; timeout nie dowodzi, że serwer niczego nie wykonał.
- **Akcja (action):** interfejs celu z postępem, wynikiem i anulowaniem; żądanie anulowania nie gwarantuje natychmiastowego zatrzymania.
- **Parametr (parameter):** wartość należąca do węzła; jej zmiana nie aktualizuje automatycznie istniejącego timera.
- **RMW / DDS:** RMW ujednolica implementację middleware; DDS to częsta technologia wykrywania i transportu, sama w sobie nie jest mechanizmem uwierzytelnienia.
- **colcon / ament:** narzędzie budowania obszaru roboczego / integracja budowania pakietów ROS; nie jest middleware komunikacji.
- **Launch:** opis uruchamianych procesów, nazw i konfiguracji; uruchomienie nie oznacza gotowości grafu.
- **tf2:** infrastruktura transformacji układów współrzędnych ze znacznikami czasu, nie solver kinematyki odwrotnej.
- **URDF / robot_state_publisher:** opis struktury robota / komponent publikujący transformacje z modelu i aktualnych stanów przegubów.
- **ros2_control:** zarządzanie cyklem życia kontrolerów i zasobami interfejsów stanu/poleceń; nieużywane w laboratorium tematu/usługi.
- **QoS:** zgodność zasad żądanych/oferowanych, dostarczanie i historia; nie jest trwałym dziennikiem zdarzeń ani certyfikacją bezpieczeństwa.

**Status dystrybucji sprawdzony 2026-11-13:** Jazzy LTS (maj 2024 – maj 2029), Lyrical LTS (maj 2026 – maj 2031). Wsparcie Kilted kończy się w grudniu 2026, a Rolling może wprowadzać zmiany niekompatybilne. Przewodnik określa **dystrybucję ROS**, nie każdą warstwę obrazu Dockera czy wersję pakietu apt.

**Źródła podstawowe:** [oficjalna tabela dystrybucji](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst), [dokumentacja ROS 2 Jazzy](https://docs.ros.org/en/jazzy/), [ustawienia QoS](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html), [poradniki tf2](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html), [URDF](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html), [dokumentacja ros2_control](https://control.ros.org/jazzy/).
