# Python-Übungen

**Diese Seite lesen auf:** [en](../../en/exercises/README.md) · [fr](../../fr/exercises/README.md) · [de](README.md) · [it](../../it/exercises/README.md) · [es](../../es/exercises/README.md) · [pt](../../pt/exercises/README.md) · [zh](../../zh/exercises/README.md) · [ja](../../ja/exercises/README.md) · [nb](../../nb/exercises/README.md) · [ru](../../ru/exercises/README.md) · [ko](../../ko/exercises/README.md) · [fi](../../fi/exercises/README.md) · [pl](../../pl/exercises/README.md)

[Inhalt](../README.md) · [Bewegung, Ableitungen und Integrale](../notes/01-motion-calculus.md) · [Dynamik erster Ordnung und Rotation](../notes/02-first-order-dynamics.md) · [Formelsammlung](../CHEATSHEET.md)

> **Warnung:** Dieses KI-unterstützte Lernmaterial kann Fehler, falsche Übersetzungen und unzutreffende Annahmen enthalten. Nutzung auf eigenes Risiko. Ergebnisse unabhängig prüfen; Beispiele niemals zur Steuerung realer Maschinen verwenden.

Die drei Grundbeispiele benötigen nur die Python-Standardbibliothek. Für Diagramme werden NumPy und Matplotlib benötigt; für das optionale lokale Notebook JupyterLab. Siehe [Python-Downloads](https://www.python.org/downloads/) und [venv-Dokumentation](https://docs.python.org/3/library/venv.html).

Die Grundprogramme benötigen keine zusätzlichen Pakete:

**Windows:** vor Aktivierung des venv `py -3`, danach `python` verwenden.

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
python3 -m unittest discover -s tests -v
```

**Python-Quelldateien zum Lesen oder lokalen Ausführen**

- [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py)
- [`02_first_order_response.py`](../../../exercises/02_first_order_response.py)
- [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py)
- [`plot_models.py`](../../../exercises/plot_models.py) (NumPy, Matplotlib)

## Optionales lokales Python-Umfeld für Diagramme und Notebook

Für die Grundbeispiele werden keine zusätzlichen Pakete benötigt. Nur für Diagramme oder JupyterLab ein virtuelles Umfeld im Repository-Verzeichnis anlegen. Siehe [offizielle venv-Anleitung](https://docs.python.org/3/library/venv.html) und [Python Packaging](https://packaging.python.org/en/latest/tutorials/installing-packages/).

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

Optionale Abhängigkeiten stehen in [requirements.txt](../../../requirements.txt). Vor dem Starten der Grundbeispiele aus dem Repository-Verzeichnis den Quellcode prüfen.
