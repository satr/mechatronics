# Упражнения на Python

**Читать эту страницу на языке:** [en](../../en/exercises/README.md) · [fr](../../fr/exercises/README.md) · [de](../../de/exercises/README.md) · [it](../../it/exercises/README.md) · [es](../../es/exercises/README.md) · [pt](../../pt/exercises/README.md) · [zh](../../zh/exercises/README.md) · [ja](../../ja/exercises/README.md) · [nb](../../nb/exercises/README.md) · [ru](README.md) · [ko](../../ko/exercises/README.md) · [fi](../../fi/exercises/README.md) · [pl](../../pl/exercises/README.md)

[Содержание](../README.md) · [Движение, производные и интегралы](../notes/01-motion-calculus.md) · [Динамика первого порядка и вращение](../notes/02-first-order-dynamics.md) · [Краткий справочник формул](../CHEATSHEET.md)

> **Предупреждение:** Эти учебные материалы подготовлены с помощью ИИ и могут содержать ошибки, неточные переводы или неверные допущения. Использование — на собственный риск. Проверяйте расчёты независимо. **Не применяйте примеры для управления реальными станками, двигателями и роботами.**

Три базовых упражнения используют только стандартную библиотеку Python. Для графиков нужны NumPy и Matplotlib, для необязательного локального ноутбука — JupyterLab. См. [официальную установку Python](https://www.python.org/downloads/) и [документацию venv](https://docs.python.org/3/library/venv.html).

Базовые программы не требуют установки сторонних библиотек:

**Windows:** до активации venv замени `python3` на `py -3`, после активации используй `python`.

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
python3 -m unittest discover -s tests -v
```

**Исходные Python-файлы для чтения или локального запуска**

- [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py)
- [`02_first_order_response.py`](../../../exercises/02_first_order_response.py)
- [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py)
- [`plot_models.py`](../../../exercises/plot_models.py) (NumPy, Matplotlib)

## Необязательное окружение для графиков и ноутбука

Базовые скрипты выше не требуют установки пакетов. Только для графиков или JupyterLab создай отдельное окружение из корня репозитория. Подробности — в [официальной документации venv](https://docs.python.org/3/library/venv.html) и [руководстве Python Packaging](https://packaging.python.org/en/latest/tutorials/installing-packages/).

**macOS / Linux:**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

**Windows (PowerShell):**

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Необязательные зависимости перечислены в [requirements.txt](../../../requirements.txt). Перед запуском базовых скриптов из корня репозитория проверь их исходный код.
