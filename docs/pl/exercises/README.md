# Ćwiczenia w Pythonie — polska wersja

**Języki:** [en](../../en/exercises/README.md) · [fr](../../fr/exercises/README.md) · [de](../../de/exercises/README.md) · [it](../../it/exercises/README.md) · [es](../../es/exercises/README.md) · [pt](../../pt/exercises/README.md) · [zh](../../zh/exercises/README.md) · [ja](../../ja/exercises/README.md) · [nb](../../nb/exercises/README.md) · [ru](../../ru/exercises/README.md) · [ko](../../ko/exercises/README.md) · [fi](../../fi/exercises/README.md) · [pl](README.md)

[Spis treści](../README.md) · [Ruch](../notes/01-motion-calculus.md) · [Dynamika](../notes/02-first-order-dynamics.md) · [Ściąga ze wzorami](../CHEATSHEET.md)

Trzy podstawowe przykłady wymagają wyłącznie standardowej biblioteki Pythona. Do tworzenia wykresów służą NumPy i Matplotlib; opcjonalny notebook lokalny korzysta z JupyterLab. Zobacz [oficjalną stronę instalacji Pythona](https://www.python.org/downloads/) i [dokumentację venv](https://docs.python.org/3/library/venv.html).

Podstawowe programy nie wymagają dodatkowych pakietów.

**Windows:** przed aktywowaniem środowiska wirtualnego używaj `py -3` zamiast `python3`; w aktywnym środowisku możesz używać polecenia `python`.

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
python3 -m unittest discover -s tests -v
```

**Pliki źródłowe Pythona (do czytania i uruchamiania lokalnie)**

- [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py)
- [`02_first_order_response.py`](../../../exercises/02_first_order_response.py)
- [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py)
- [`plot_models.py`](../../../exercises/plot_models.py) — wymaga NumPy i Matplotlib.

## Opcjonalne środowisko do wykresów i notebooków

Powyższe skrypty działają bez instalowania zewnętrznych pakietów. Tylko na potrzeby opcjonalnych wykresów i JupyterLab utwórz środowisko wirtualne w katalogu głównym repozytorium. Korzystaj z [oficjalnej instrukcji venv](https://docs.python.org/3/library/venv.html) oraz [podręcznika instalowania pakietów](https://packaging.python.org/en/latest/tutorials/installing-packages/).

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

Opcjonalne zależności wymieniono w [requirements.txt](../../../requirements.txt). Zanim uruchomisz program, przeczytaj jego kod. Polecenia wykonuj z katalogu głównego repozytorium.
