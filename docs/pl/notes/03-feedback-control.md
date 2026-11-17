# 3. Sterowanie ze sprzężeniem zwrotnym: PID, próbkowanie, nasycenie i moment utrzymujący

**Języki:** [en](../../en/notes/03-feedback-control.md) · [fr](../../fr/notes/03-feedback-control.md) · [de](../../de/notes/03-feedback-control.md) · [it](../../it/notes/03-feedback-control.md) · [es](../../es/notes/03-feedback-control.md) · [pt](../../pt/notes/03-feedback-control.md) · [zh](../../zh/notes/03-feedback-control.md) · [ja](../../ja/notes/03-feedback-control.md) · [nb](../../nb/notes/03-feedback-control.md) · [ru](../../ru/notes/03-feedback-control.md) · [ko](../../ko/notes/03-feedback-control.md) · [fi](../../fi/notes/03-feedback-control.md) · [pl](03-feedback-control.md)

**Jednostki tej lekcji (przed przykładami):** `rpm` — obroty na minutę, spoza SI; `A` — amper; `s` — sekunda; `rpm/s` — zmiana prędkości obrotowej na sekundę; `A/rpm` — wzmocnienie proporcjonalne; `A/(rpm·s)` — wzmocnienie całkujące; `A·s/rpm` — wzmocnienie różniczkujące; `N·m` — niutonometr (moment siły); `kg` — kilogram; `m` — metr; `N` — niuton. [Pełny słownik jednostek](../UNITS.md).

[Spis treści](../README.md) · [Podstawy analizy](00-calculus-foundations.md) · [Dynamika pierwszego rzędu](02-first-order-dynamics.md) · [Trygonometria](../TRIGONOMETRY.md)

> **Model edukacyjny:** nie podłączaj tych uproszczonych algorytmów do prawdziwych silników ani maszyn.

## Spis treści

- [1. Regulacja prędkości w zamkniętej pętli](#section-1)
- [2. P: reakcja proporcjonalna](#section-2)
- [3. I: błąd skumulowany i zadana wartość prądu](#section-3)
- [4. D: pochodna błędu i szum czujnika](#section-4)
- [5. Okres próbkowania, nasycenie i anti-windup](#section-5)
- [6. Utrzymanie przegubu robota przeciw sile ciężkości](#section-6)
- [7. Sprawdzenie i ograniczenia](#section-7)

<a id="section-1"></a>
## 1. Regulacja prędkości w zamkniętej pętli

Regulator ze sprzężeniem zwrotnym (feedback controller) porównuje wartość zadaną z pomiarem czujnika. Jeśli zadana prędkość silnika to 1000 rpm, a zmierzona 950 rpm, błąd wynosi +50 rpm. Regulator PI/PID zamienia ten błąd na polecenie. W naszym modelu poleceniem jest **zadany prąd wytwarzający moment** w amperach, a nie nakaz dodania tylu amperów do poprzedniego zmierzonego prądu.

$$
\varepsilon(t)=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}},
\qquad I_{\mathrm{set}}=u_P+u_I+u_D.
$$

Napęd może mieć osobną pętlę regulacji prądu, która zmienia napięcie lub PWM, aby śledzić wartość zadaną prądu. W innych układach wyjściem regulatora bywa napięcie, moment czy PWM. Nie zakładaj, że każdy napęd udostępnia zadawanie prądu.

<a id="section-2"></a>
## 2. P: reakcja proporcjonalna

Człon P reaguje na błąd **w bieżącej chwili**. W prostym modelu bez sterowania wyprzedzającego ani przesunięcia sygnału stałe obciążenie wymaga niezerowego momentu silnika, a więc i prądu. Gdy błąd prędkości jest dokładnie zerowy, człon P również daje zero. Regulacja samym P może zatem ustalić się z trwałym błędem.

$$
u_P=K_p\varepsilon,\quad [K_p]=\mathrm{A/rpm}.
$$

<a id="section-3"></a>
## 3. I: błąd skumulowany i zadany prąd

Człon I całkuje błąd w czasie. Przechowuje jeden skumulowany stan, a nie listę wszystkich poprzednich błędów. Gdy błąd dodatni się utrzymuje, całka rośnie; przy błędzie zerowym pozostaje stała; przy ujemnym maleje. W ten sposób regulator może nadal wytwarzać niezerowe zadanie momentu, nawet gdy prędkość osiągnie cel.

$$
z(t)=\int_0^t\varepsilon(s)\ \mathrm{d}s,\quad u_I=K_i z(t),\quad [K_i]=\mathrm{A/(rpm\cdot s)}.
$$

```python
integral = 0.0  # saved between controller iterations
for speed in [950, 950, 950, 1000, 1020, 1020]:
    error = 1000 - speed       # rpm
    integral += error * 1.0   # rpm*s; dt = 1 s
    p_command = 0.02 * error # amperes
    i_command = 0.002 * integral # amperes
    current_setpoint = p_command + i_command
    print(round(integral), round(i_command, 2), round(current_setpoint, 2))
```

Dla przykładowego regulatora z `dt = 1 s`, `Kp = 0.02 A/rpm` i `Ki = 0.002 A/(rpm·s)` stały błąd +50 rpm przez trzy próbki daje skumulowane całki 50, 100, 150 rpm·s i człony I równe 0.10, 0.20, 0.30 A. Przy zerowym błędzie człon I zostaje na 0.30 A. Sekunda z błędem −20 rpm zmniejsza go do 0.26 A, a następna do 0.22 A. Zmiana −0.04 A to **przyrost w jednym kroku**, nie całkowity prąd zadany.

Program drukuje tylko skumulowaną całkę, człon I i całkowite zadanie prądu. Tabela pokazuje dodatkowo człon P, aby można było odtworzyć obliczenia. Między próbkami mija jedna sekunda, a akumulator zaczyna od zera.

| k | Prędkość zmierzona (rpm) | ε (rpm) | z (rpm·s) | u_P (A) | u_I (A) | I_set (A) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 950 | +50 | 50 | +1.00 | +0.10 | +1.10 |
| 2 | 950 | +50 | 100 | +1.00 | +0.20 | +1.20 |
| 3 | 950 | +50 | 150 | +1.00 | +0.30 | +1.30 |
| 4 | 1000 | 0 | 150 | 0.00 | +0.30 | +0.30 |
| 5 | 1020 | −20 | 130 | −0.40 | +0.26 | −0.14 |
| 6 | 1020 | −20 | 110 | −0.40 | +0.22 | −0.18 |

Przy 1020 rpm błąd wynosi −20 rpm: człon P to −0.40 A, ale człon I nadal jest dodatni (+0.26 A). Całkowita zadana wartość prądu jest więc **ujemna i wynosi −0.14 A**. W następnej próbce otrzymujemy −0.18 A. Zmiana członu I (−0.04 A na krok) nie jest tym samym co całkowite polecenie. To obliczenia wyidealizowane, nie nastawy rzeczywistego napędu.

<a id="section-4"></a>
## 4. D: pochodna błędu i szum czujnika

Człon D reaguje na **tempo zmiany błędu**. Przy stałej prędkości zadanej przyspieszanie silnika zmniejsza błąd, a ujemny wkład różniczkujący może ograniczyć przeregulowanie. D nie jest samą prędkością silnika. Skok pomiaru o 8 rpm w ciągu 0.01 s daje pozorną zmianę 800 rpm/s, nawet gdy rzeczywista prędkość prawie się nie zmienia.

$$
u_D=K_d\frac{\mathrm{d}\varepsilon}{\mathrm{d}t},\quad [K_d]=\mathrm{A\cdot s/rpm},\qquad
\frac{\Delta\omega}{\Delta t}=\frac{8\ \mathrm{rpm}}{0.01\ \mathrm{s}}=800\ \mathrm{rpm/s}.
$$

Pochodna błędu ma jednostkę rpm/s. Ponieważ wyjście członu D jest prądem w A, wzmocnienie musi skompensować rpm/s: `K_d` ma jednostkę A·s/rpm, a jego iloczyn z pochodną błędu daje ampery.

Filtrowanie pochodnej zmniejsza szum wysokoczęstotliwościowy, ale nadmierne filtrowanie opóźnia reakcję. Często różniczkuje się pomiar zamiast wartości zadanej, aby uniknąć impulsu pochodnej przy skokowej zmianie polecenia; znaki i wzmocnienia muszą być zgodne z architekturą regulatora.

<a id="section-5"></a>
## 5. Okres próbkowania, nasycenie i anti-windup

Regulator cyfrowy aktualizuje wyjście co skończony okres. Przy stałym błędzie 20 rpm przez jedną sekundę 100 próbek przy `dt = 0.01 s` i 10 próbek przy `dt = 0.1 s` dają ten sam wynik całkowania 20 rpm·s. Pominięcie mnożenia przez `dt` spowodowałoby dziesięć razy większy przyrost w szybszym regulatorze. Rzeczywiste strojenie zależy także od opóźnień, szumu i dynamiki napędu.

$$
z_{k+1}=z_k+\varepsilon_k\ \Delta t.
$$

Przy ograniczeniu wykonawczym zadany prąd może przekroczyć dozwoloną wartość. Jeśli podczas nasycenia całka nadal rośnie (**integral windup**), po zmniejszeniu obciążenia może pojawić się duże przeregulowanie. **Anti-windup** może zatrzymać całkowanie, kiedy sygnał nasycony byłby dalej zwiększany w stronę ograniczenia, albo skorygować stan wewnętrzny na podstawie różnicy między poleceniem żądanym i zastosowanym. Ograniczaj **całe** polecenie i poprawnie uwzględniaj człon P.

<a id="section-6"></a>
## 6. Utrzymanie przegubu robota przeciw sile ciężkości

Stała momentu silnika `Kt` oznacza moment na jednostkę **prądu wytwarzającego moment**: `Kt` w N·m/A, prąd w A, moment w N·m. Na przykład `Kt = 0.1 N·m/A` i prąd 2 A dają 0.2 N·m, przy zachowaniu konwencji producenta dotyczącej pomiaru prądu.

$$
M_{\mathrm{motor}}=K_t I,\qquad [K_t]=\mathrm{N\cdot m/A}.
$$

Dźwignia z masą $m$ w odległości $L$ od poziomej osi przegubu doświadcza momentu grawitacyjnego o wartości $mgL|\cos\theta|$, gdy θ mierzymy od poziomu. W spoczynku moment silnika musi przeciwdziałać momentowi obciążenia tak, aby ich suma ze znakami była równa zero. Przegub utrzymujący ciężar może wymagać niezerowego prądu nawet przy zerowym błędzie położenia. Hamulec mechaniczny lub rzeczywiście samohamowna przekładnia mogą utrzymać obciążenie bez prądu; przekładnia falowa (harmonic drive) **nie jest z definicji samohamowna**.

$$
J\alpha=M_{\mathrm{motor}}+M_{\mathrm{load}},\quad
\alpha=0\ \Longrightarrow\ M_{\mathrm{motor}}=-M_{\mathrm{load}},
$$
$$
|M_g|=mgL|\cos\theta|.
$$

Silnik BLDC typu **outrunner** obraca zewnętrzną obudową, natomiast typu **inrunner** ma wewnętrzny wirnik. Wirnik (rotor) zawsze oznacza część obracającą się, stojan (stator) — nieruchomą. Ich rozmieszczenie promieniowe nie zmienia definicji.

<a id="section-7"></a>
## 7. Sprawdzenie i ograniczenia

We wszystkich przykładach prądy są wyidealizowane i nie stanowią instrukcji ustawiania rzeczywistych urządzeń. Prawdziwy napęd wymaga poprawnej definicji prądu, ograniczeń, kalibracji enkodera, ochrony termicznej, filtrów, anti-windup, blokad bezpieczeństwa i bezpiecznych testów. Wzmocnienia PID działające w jednym modelu nie są uniwersalne.

[Podstawy analizy](00-calculus-foundations.md) · [Tablica trygonometryczna](../TRIGONOMETRY.md) · [Dynamika pierwszego rzędu](02-first-order-dynamics.md)
