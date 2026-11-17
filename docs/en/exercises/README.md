# Python exercises — English

**Read this page in:** [en](README.md) · [fr](../../fr/exercises/README.md) · [de](../../de/exercises/README.md) · [it](../../it/exercises/README.md) · [es](../../es/exercises/README.md) · [pt](../../pt/exercises/README.md) · [zh](../../zh/exercises/README.md) · [ja](../../ja/exercises/README.md) · [nb](../../nb/exercises/README.md) · [ru](../../ru/exercises/README.md) · [ko](../../ko/exercises/README.md) · [fi](../../fi/exercises/README.md) · [pl](../../pl/exercises/README.md)

[Contents](../README.md) · [Motion](../notes/01-motion-calculus.md) · [Dynamics](../notes/02-first-order-dynamics.md) · [Cheat sheet](../CHEATSHEET.md)

The three basic examples use only the Python standard library. Graphs use NumPy and Matplotlib; the optional local notebook uses JupyterLab. See the [official Python installation page](https://www.python.org/downloads/) and [venv documentation](https://docs.python.org/3/library/venv.html).

The core scripts do not require any package installation:

**Windows:** replace `python3` with `py -3` before activating a virtual environment, or use `python` in an activated venv.

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
python3 -m unittest discover -s tests -v
```

**Python source files (available for local use or reading)**

- [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py)
- [`02_first_order_response.py`](../../../exercises/02_first_order_response.py)
- [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py)
- [`plot_models.py`](../../../exercises/plot_models.py) (NumPy, Matplotlib)

## Optional local environment for plots and notebooks

The basic scripts above need no extra packages. Only for optional plots or JupyterLab, create a virtual environment from the repository root. Refer to the [official venv guide](https://docs.python.org/3/library/venv.html) and [Python Packaging guide](https://packaging.python.org/en/latest/tutorials/installing-packages/).

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

Optional dependencies are listed in [requirements.txt](../../../requirements.txt). Check each source file before executing the basic scripts from the repository root.
