# Краткий справочник формул

**Читать эту страницу на языке:** [en](../en/CHEATSHEET.md) · [fr](../fr/CHEATSHEET.md) · [de](../de/CHEATSHEET.md) · [it](../it/CHEATSHEET.md) · [es](../es/CHEATSHEET.md) · [pt](../pt/CHEATSHEET.md) · [zh](../zh/CHEATSHEET.md) · [ja](../ja/CHEATSHEET.md) · [nb](../nb/CHEATSHEET.md) · [ru](CHEATSHEET.md) · [ko](../ko/CHEATSHEET.md) · [fi](../fi/CHEATSHEET.md) · [pl](../pl/CHEATSHEET.md)

**Единицы этой темы (объяснены до примеров):** `s` — секунда; `m` — метр; `m/s` — метр / секунда — линейная скорость; `rad/s` — радиан / секунда — угловая скорость; `kg·m²` — килограмм · метр² — момент инерции; `N·m` — ньютон · метр — крутящий момент; `N·m·s/rad` — ньютон · метр · секунда / радиан — коэффициент усиления по скорости; `J` — джоуль; `mm` — миллиметр = 0.001 m; `mm/s` — миллиметр / секунда — линейная скорость; `%` — процент (одна сотая). [Полный справочник единиц](UNITS.md).

[Содержание](README.md) · [Движение, производные и интегралы](notes/01-motion-calculus.md) · [Динамика первого порядка и вращение](notes/02-first-order-dynamics.md) · [Упражнения на Python](exercises/README.md)

> **Предупреждение:** Эти учебные материалы подготовлены с помощью ИИ и могут содержать ошибки, неточные переводы или неверные допущения. Использование — на собственный риск. Проверяйте расчёты независимо. **Не применяйте примеры для управления реальными станками, двигателями и роботами.**

| Краткое повторение | Краткий справочник формул |
| --- | --- |
| Перемещение | $\Delta x=x_2-x_1$ |
| Пройденный путь | $s=\int_{t_1}^{t_2}\lvert v(t)\rvert\ \mathrm{d}t\ge 0$ |
| Средняя векторная скорость | $\overline{v}=\frac{\Delta x}{\Delta t}$ |
| Средняя путевая скорость | $\frac{s}{\Delta t}$ |
| Мгновенная скорость | $v(t)=\frac{dx}{dt}$ |
| Явный метод Эйлера | $x_{n+1}=x_n+v_n\ dt$ |
| Динамика первого порядка | $\frac{dv}{dt}=\frac{u-v}{\tau}$ |
| Ошибка скорости (speed error) | $\varepsilon(t)=u-v(t)$ |
| Постоянная времени | $t=\tau$: $1-\exp(-1)\approx63.2\ \%$ |
| Результирующий крутящий момент | $M=J\alpha$ |
| Момент инерции и коэффициент | $\tau=\frac{J}{K}$ (Только для идеализированной модели момента) |
| Кинетическая энергия вращения | $E=\frac{1}{2}J\omega^2$ |

**Обозначения:** $\varepsilon$ — ошибка скорости (speed error); $\mathrm{e}\approx2.71828$ — число Эйлера (Euler’s number); $\exp(z)=\mathrm{e}^{z}$ — экспонента.

**Единицы (SI):**

| Обозначение | Термин | Единица |
| --- | --- | --- |
| `t, dt, τ` | Время | s (second) |
| `x` | Положение | m (meter) |
| `v` | Скорость | m/s (meter per second) |
| `ω` | Угловая скорость | rad/s (radian per second) |
| `J` | Момент инерции | kg·m² (kilogram square meter) |
| `M` | Крутящий момент | N·m (newton meter) |
| `K` | Коэффициент момента | N·m·s/rad |
| `E` | Энергия | J (joule) |

Точка `·` означает умножение единиц, а не перечисление через запятую. Заданная скорость $u$ относится к линейному или вращательному движению в зависимости от модели.

## Ограничения

Не путайте модуль скорости с векторной скоростью, путь с перемещением, $dt$ с $\tau$. Формула $\tau=\frac{J}{K}$ справедлива только для явно указанной модели; механическая энергия — не полное электропотребление.

**Английские термины:**

- путь (distance traveled)
- перемещение (displacement)
- модуль скорости (speed)
- вектор скорости (velocity)
- производная (derivative)
- интеграл (integral)
- численное интегрирование (numerical integration)
- явный метод Эйлера (explicit Euler method)

**Английские термины:**

- система первого порядка (first-order system)
- постоянная времени (time constant)
- шаг по времени (time step)
- момент инерции (moment of inertia)
- крутящий момент (torque)
- коэффициент регулятора (controller gain)
- угловое ускорение (angular acceleration)
- идентификация системы (system identification)
- кинетическая энергия вращения (rotational kinetic energy)

Подробнее: [производные и численные методы](notes/01-motion-calculus.md#section-6), [допущения модели и устойчивость метода Эйлера](notes/02-first-order-dynamics.md#section-7).


[Почему именно эти проценты? Подробный расчёт.](notes/02-first-order-dynamics.md#time-constant-derivation)

[Как вычислены 3; 3.8 и 3.98.](notes/01-motion-calculus.md#motion-values-derivation)


## Математические символы и обозначения

**Σ / ∑ (суммирование / summation)** означает сложить несколько слагаемых: $\sum_{n=1}^{3}n=1+2+3=6$. [Другие символы](SYMBOLS.md).


## Таблица интегралов

[0. Основы анализа: производные, дифференциалы и интегралы](notes/00-calculus-foundations.md) · [Таблица интегралов](INTEGRAL_TABLE.md)


## Обратная связь: PID, ток и удержание нагрузки

| $\varepsilon=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}}$ | $u_P=K_p\varepsilon$, $u_I=K_i\int\varepsilon\ \mathrm{d}t$ |
| --- | --- |
| $M_{\mathrm{motor}}=K_t I$ | $\lvert M_g\rvert=mgL\lvert\cos\theta\rvert$ |

[Обратная связь: PID, ток и удержание нагрузки](notes/03-feedback-control.md) · [Таблица sin/cos/tan/arctan и механические примеры](TRIGONOMETRY.md)

<a id="joint-velocity"></a>
## Вращение, скорость и матрица Якоби

Угловая скорость измеряется в rad/s. Если длина задана в mm, линейная скорость будет в mm/s.

$$
v_x=-L\sin Q\cdot\dot Q,\qquad v_y=L\cos Q\cdot\dot Q
$$

$$
\det J=L_1L_2\sin Q_2
$$

[Вращение, скорость и матрица Якоби](notes/05-velocity-jacobian.md)
