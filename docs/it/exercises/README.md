# Esercizi Python

**Leggi questa pagina in:** [en](../../en/exercises/README.md) · [fr](../../fr/exercises/README.md) · [de](../../de/exercises/README.md) · [it](README.md) · [es](../../es/exercises/README.md) · [pt](../../pt/exercises/README.md) · [zh](../../zh/exercises/README.md) · [ja](../../ja/exercises/README.md) · [nb](../../nb/exercises/README.md) · [ru](../../ru/exercises/README.md) · [ko](../../ko/exercises/README.md) · [fi](../../fi/exercises/README.md) · [pl](../../pl/exercises/README.md)

[Indice](../README.md) · [Moto, derivate e integrali](../notes/01-motion-calculus.md) · [Dinamica del primo ordine e rotazione](../notes/02-first-order-dynamics.md) · [Formulario rapido](../CHEATSHEET.md)

> **Avvertenza:** Questi materiali didattici, elaborati anche con l'IA, possono contenere errori, traduzioni imprecise e ipotesi non valide. L'uso è a proprio rischio. Verificare i calcoli in modo indipendente; non utilizzare gli esempi per controllare macchine reali.

I tre esercizi di base usano solo la libreria standard. I grafici richiedono NumPy e Matplotlib; il notebook locale facoltativo usa JupyterLab. Consultare [Python ufficiale](https://www.python.org/downloads/) e [la guida venv](https://docs.python.org/3/library/venv.html).

Gli esempi di base non richiedono librerie aggiuntive:

**Windows:** prima di attivare il venv usare `py -3`, dopo l’attivazione `python`.

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
python3 -m unittest discover -s tests -v
```

**File Python per lettura o esecuzione locale**

- [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py)
- [`02_first_order_response.py`](../../../exercises/02_first_order_response.py)
- [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py)
- [`plot_models.py`](../../../exercises/plot_models.py) (NumPy, Matplotlib)

## Ambiente locale facoltativo per grafici e notebook

Gli script di base non richiedono pacchetti aggiuntivi. Solo per grafici o JupyterLab creare un ambiente virtuale nella directory principale del repository. Consultare la [documentazione ufficiale venv](https://docs.python.org/3/library/venv.html) e [Python Packaging](https://packaging.python.org/en/latest/tutorials/installing-packages/).

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

Le dipendenze facoltative sono elencate in [requirements.txt](../../../requirements.txt). Controllare il codice sorgente prima di eseguire gli script di base dalla directory principale del repository.
