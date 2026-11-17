# Exercices Python

**Lire cette page en:** [en](../../en/exercises/README.md) · [fr](README.md) · [de](../../de/exercises/README.md) · [it](../../it/exercises/README.md) · [es](../../es/exercises/README.md) · [pt](../../pt/exercises/README.md) · [zh](../../zh/exercises/README.md) · [ja](../../ja/exercises/README.md) · [nb](../../nb/exercises/README.md) · [ru](../../ru/exercises/README.md) · [ko](../../ko/exercises/README.md) · [fi](../../fi/exercises/README.md) · [pl](../../pl/exercises/README.md)

[Sommaire](../README.md) · [Mouvement, dérivées et intégrales](../notes/01-motion-calculus.md) · [Dynamique du premier ordre et rotation](../notes/02-first-order-dynamics.md) · [Aide-mémoire des formules](../CHEATSHEET.md)

> **Avertissement :** Ces ressources pédagogiques assistées par IA peuvent contenir des erreurs, des traductions inexactes et des hypothèses incorrectes. Utilisation à vos risques et périls. Vérifiez les calculs indépendamment et n'utilisez aucun exemple pour piloter des machines réelles.

Les trois exercices de base ne nécessitent que la bibliothèque standard. Les graphiques utilisent NumPy et Matplotlib, et le notebook local facultatif JupyterLab. Voir [Python officiel](https://www.python.org/downloads/) et [la documentation venv](https://docs.python.org/3/library/venv.html).

Les exemples de base ne nécessitent aucune installation de bibliothèque externe :

**Windows :** utilisez `py -3` avant activation du venv, puis `python` après activation.

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
python3 -m unittest discover -s tests -v
```

**Fichiers Python à consulter ou à exécuter localement**

- [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py)
- [`02_first_order_response.py`](../../../exercises/02_first_order_response.py)
- [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py)
- [`plot_models.py`](../../../exercises/plot_models.py) (NumPy, Matplotlib)

## Environnement local facultatif pour graphiques et notebook

Les scripts de base ne nécessitent aucun paquet supplémentaire. Pour les graphiques ou JupyterLab uniquement, créez un environnement virtuel à la racine du dépôt. Voir la [documentation officielle venv](https://docs.python.org/3/library/venv.html) et le [guide Python Packaging](https://packaging.python.org/en/latest/tutorials/installing-packages/).

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

Les dépendances facultatives figurent dans [requirements.txt](../../../requirements.txt). Vérifiez le code source avant de lancer les scripts de base depuis la racine du dépôt.
