# Mechatronics Training — Polski

**Języki:** [en](../en/README.md) · [fr](../fr/README.md) · [de](../de/README.md) · [it](../it/README.md) · [es](../es/README.md) · [pt](../pt/README.md) · [zh](../zh/README.md) · [ja](../ja/README.md) · [nb](../nb/README.md) · [ru](../ru/README.md) · [ko](../ko/README.md) · [fi](../fi/README.md) · [pl](README.md)

> [!WARNING]
> **Zastrzeżenie:** Materiały edukacyjne przygotowane z pomocą AI mogą zawierać błędy, nieścisłości, błędne tłumaczenia lub pominięcia. Korzystasz z nich na własne ryzyko. Samodzielnie sprawdzaj wzory i założenia. Żaden z przedstawionych programów nie jest przeznaczony do sterowania rzeczywistymi urządzeniami.

## Spis treści

1. [Podstawy analizy: pochodne, różniczki i całki](notes/00-calculus-foundations.md)
2. [Ruch, prędkość, pochodne i całki](notes/01-motion-calculus.md)
3. [Dynamika pierwszego rzędu i układy obrotowe](notes/02-first-order-dynamics.md)
4. [Tablica całek](INTEGRAL_TABLE.md)
5. [Tablica pochodnych](DERIVATIVE_TABLE.md)
6. [Ściąga ze wzorami](CHEATSHEET.md)
7. [Ćwiczenia w Pythonie](exercises/README.md)
8. [Symbole i oznaczenia](SYMBOLS.md) · [Słownik jednostek SI i innych](UNITS.md)
9. [Trygonometria z przykładami mechanicznymi](TRIGONOMETRY.md)
10. [Sterowanie ze sprzężeniem zwrotnym: PID i moment utrzymujący](notes/03-feedback-control.md)
11. [Układy współrzędnych robota: położenie i obrót](notes/04-coordinate-frames.md)
12. [Ruch obrotowy, prędkość, jakobian i osobliwości](notes/05-velocity-jacobian.md)
13. [ROS 2: architektura, węzły i laboratorium Docker](notes/06-ros2-foundations.md)

[Strona repozytorium](../../README.md) · [Bezpieczeństwo i poprawność](SAFETY.md) · [Licencje](LICENSING.md)

## Jak korzystać z kursu

Czytaj po jednym krótkim rozdziale. Odtwórz obliczenia, uruchom odpowiedni przykład w Pythonie w środowisku lokalnym i spróbuj samodzielnie objaśnić wynik. Zawsze rozróżniaj wyidealizowany model od rzeczywistego układu fizycznego; przed zastosowaniem równania przeczytaj jego założenia.

Te same tematy są dostępne także w pozostałych językach wymienionych w przełączniku na górze strony. Wszystkie odnośniki wewnętrzne w powyższym spisie prowadzą do polskiej edycji. W razie rozbieżności punktem odniesienia jest oryginalna wersja angielska, jednak także ona może zawierać błędy.

Sekcje rozszerzone na końcu lekcji zawierają dodatkowe wyprowadzenia, granice modeli i sprawdzanie wymiarów. Diagramy i przykłady liczbowe ilustrują skąd biorą się współczynniki, między innymi $4t$ oraz $63.2\ \%$.

**Instalacja Pythona oraz środowiska venv (Windows/macOS/Linux):** [instrukcje do ćwiczeń](exercises/README.md).

## ROS 2 Jazzy bez GUI: wirtualny przegub

[ROS 2 Jazzy bez GUI: wirtualny przegub](notes/07-ros2-control-lab.md) — URDF · TF2 · ros2_control · mock hardware · ARM64.

**Architektura robota ROS 2:** [Pięć etapów i diagram Mermaid](notes/08-ros2-robot-architecture.md).

**Bez Compose:** [Uruchom oficjalny obraz ROS bezpośrednio](../../ros2/PLAIN_DOCKER.md).
