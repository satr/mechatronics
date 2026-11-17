# Python-øvelser

**Les denne siden på:** [en](../../en/exercises/README.md) · [fr](../../fr/exercises/README.md) · [de](../../de/exercises/README.md) · [it](../../it/exercises/README.md) · [es](../../es/exercises/README.md) · [pt](../../pt/exercises/README.md) · [zh](../../zh/exercises/README.md) · [ja](../../ja/exercises/README.md) · [nb](README.md) · [ru](../../ru/exercises/README.md) · [ko](../../ko/exercises/README.md) · [fi](../../fi/exercises/README.md) · [pl](../../pl/exercises/README.md)

[Innhold](../README.md) · [Bevegelse, derivasjon og integrasjon](../notes/01-motion-calculus.md) · [Førsteordensdynamikk og rotasjon](../notes/02-first-order-dynamics.md) · [Kort formelsamling](../CHEATSHEET.md)

> **Advarsel:** Dette KI-assisterte lærematerialet kan inneholde feil, unøyaktige oversettelser og ugyldige forutsetninger. Bruk skjer på eget ansvar. Kontroller alle beregninger uavhengig, og bruk aldri eksemplene til å styre virkelige motorer eller maskiner.

De tre grunnøvelsene bruker bare Pythons standardbibliotek. Grafer bruker NumPy og Matplotlib; den valgfrie lokale notatboken bruker JupyterLab. Se [offisiell Python-installasjon](https://www.python.org/downloads/) og [venv-dokumentasjonen](https://docs.python.org/3/library/venv.html).

Grunnøvelsene trenger ingen eksterne biblioteker:

**Windows:** bruk `py -3` før aktivering av venv, og `python` etterpå。

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
python3 -m unittest discover -s tests -v
```

**Python-filer for lesing eller lokal kjøring**

- [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py)
- [`02_first_order_response.py`](../../../exercises/02_first_order_response.py)
- [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py)
- [`plot_models.py`](../../../exercises/plot_models.py) (NumPy, Matplotlib)

## Valgfritt lokalt miljø for grafer og notatbok

De grunnleggende skriptene trenger ingen ekstra pakker. Opprett et virtuelt miljø i rotmappen bare for grafer eller JupyterLab. Se den [offisielle venv-dokumentasjonen](https://docs.python.org/3/library/venv.html) og [Python Packaging-veiledningen](https://packaging.python.org/en/latest/tutorials/installing-packages/).

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

Valgfrie avhengigheter står i [requirements.txt](../../../requirements.txt). Kontroller kildekoden før du kjører de tre grunnskriptene fra rotmappen.
