# Ejercicios de Python

**Leer esta página en:** [en](../../en/exercises/README.md) · [fr](../../fr/exercises/README.md) · [de](../../de/exercises/README.md) · [it](../../it/exercises/README.md) · [es](README.md) · [pt](../../pt/exercises/README.md) · [zh](../../zh/exercises/README.md) · [ja](../../ja/exercises/README.md) · [nb](../../nb/exercises/README.md) · [ru](../../ru/exercises/README.md) · [ko](../../ko/exercises/README.md) · [fi](../../fi/exercises/README.md) · [pl](../../pl/exercises/README.md)

[Contenido](../README.md) · [Movimiento, derivadas e integrales](../notes/01-motion-calculus.md) · [Dinámica de primer orden y rotación](../notes/02-first-order-dynamics.md) · [Formulario de consulta rápida](../CHEATSHEET.md)

> **Advertencia:** Este material didáctico elaborado con ayuda de IA puede contener errores, traducciones inexactas o supuestos incorrectos. Su uso es bajo responsabilidad propia. Verifica los cálculos de manera independiente y no emplees los ejemplos para controlar maquinaria real.

Los tres ejercicios básicos solo necesitan la biblioteca estándar. Los gráficos usan NumPy y Matplotlib; el cuaderno local opcional usa JupyterLab. Consulte [Python oficial](https://www.python.org/downloads/) y [la guía de venv](https://docs.python.org/3/library/venv.html).

Los programas básicos no requieren instalar bibliotecas adicionales:

**Windows:** use `py -3` antes de activar el venv y `python` después.

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
python3 -m unittest discover -s tests -v
```

**Archivos Python para leer o ejecutar localmente**

- [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py)
- [`02_first_order_response.py`](../../../exercises/02_first_order_response.py)
- [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py)
- [`plot_models.py`](../../../exercises/plot_models.py) (NumPy, Matplotlib)

## Entorno local opcional para gráficos y cuaderno

Los scripts básicos no requieren paquetes adicionales. Solo para gráficos o JupyterLab, cree un entorno virtual en la raíz del repositorio. Consulte la [documentación oficial de venv](https://docs.python.org/3/library/venv.html) y [Python Packaging](https://packaging.python.org/en/latest/tutorials/installing-packages/).

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

Las dependencias opcionales figuran en [requirements.txt](../../../requirements.txt). Revise el código fuente antes de ejecutar los scripts básicos desde la raíz del repositorio.
