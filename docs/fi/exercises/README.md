# Python-harjoitukset — suomi

**Muut kielet:** [en](../../en/exercises/README.md) · [fr](../../fr/exercises/README.md) · [de](../../de/exercises/README.md) · [it](../../it/exercises/README.md) · [es](../../es/exercises/README.md) · [pt](../../pt/exercises/README.md) · [zh](../../zh/exercises/README.md) · [ja](../../ja/exercises/README.md) · [nb](../../nb/exercises/README.md) · [ru](../../ru/exercises/README.md) · [ko](../../ko/exercises/README.md) · [fi](README.md) · [pl](../../pl/exercises/README.md)

[Sisällysluettelo](../README.md) · [Liike](../notes/01-motion-calculus.md) · [Dynamiikka](../notes/02-first-order-dynamics.md) · [Kaavakooste](../CHEATSHEET.md)

Kolme perusesimerkkiä käyttävät vain Pythonin vakiokirjastoa. Kuvaajat käyttävät NumPyä ja Matplotlibia; valinnainen paikallinen notebook käyttää JupyterLabia. [Pythonin virallinen lataussivu](https://www.python.org/downloads/) · [venv-ohje](https://docs.python.org/3/library/venv.html).

Perusskriptit eivät tarvitse erillisiä paketteja. Windowsissa korvaa `python3` komennolla `py -3` ennen virtuaaliympäristön aktivointia tai käytä komentoa `python` aktivoidussa ympäristössä.

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
python3 -m unittest discover -s tests -v
```

**Python-lähdetiedostot**

- [Liike ja integraali](../../../exercises/01_motion_and_integral.py)
- [Ensimmäisen kertaluvun vaste](../../../exercises/02_first_order_response.py)
- [Pyörimisenergia](../../../exercises/03_rotation_energy.py)
- [Kuvaajien piirtäminen](../../../exercises/plot_models.py) — tarvitsee NumPyn ja Matplotlibin

## Valinnainen paikallinen ympäristö kuvaajia ja notebookia varten

Yllä olevat perusskriptit eivät tarvitse lisäpaketteja. Luo virtuaaliympäristö projektin juurihakemistoon vain kuvaajia tai JupyterLabia varten. Katso [virallinen venv-ohje](https://docs.python.org/3/library/venv.html) ja [Python Packaging -opas](https://packaging.python.org/en/latest/tutorials/installing-packages/).

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

Valinnaiset riippuvuudet ovat tiedostossa [requirements.txt](../../../requirements.txt). Tarkista lähdekoodi ennen perusskriptien suorittamista projektin juurihakemistosta.

## Lisäharjoitukset

1. Johda $x(t)=2t^2$-funktiosta nopeus $v(t)=4t$ ja vertaa erotusosamäärään.
2. Kun $t$ mitataan sekunteina, integroi $v(t)=(3+4t)\ \mathrm{mm/s}$ välillä $0$–$2$ s ja varmista siirtymä $14\ \mathrm{mm}$.
3. Simuloi ensimmäisen kertaluvun järjestelmää, jossa $\tau=0.5$ s, aika-askelilla $\Delta t=0.05$ s ja $0.5$ s. Vertaa kummankin aika-askeleen tuloksia analyyttiseen ratkaisuun ja tarkastele numeerista virhettä.
4. Laske kärjen paikka $(0.1, 0.1)$ m, kun $L_1=L_2=0.1$ m, $q_1=0$, $q_2=90^\circ$.
5. Tarkastele integraattorin kertymistä PID-simulaatiossa, jossa ohjaus kyllästyy.

Esimerkit ovat opiskelusimulaatioita. Älä käytä niitä oikeiden CNC-koneiden tai robottien ohjaamiseen.

