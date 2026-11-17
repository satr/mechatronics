# Exercícios Python

**Ler esta página em:** [en](../../en/exercises/README.md) · [fr](../../fr/exercises/README.md) · [de](../../de/exercises/README.md) · [it](../../it/exercises/README.md) · [es](../../es/exercises/README.md) · [pt](README.md) · [zh](../../zh/exercises/README.md) · [ja](../../ja/exercises/README.md) · [nb](../../nb/exercises/README.md) · [ru](../../ru/exercises/README.md) · [ko](../../ko/exercises/README.md) · [fi](../../fi/exercises/README.md) · [pl](../../pl/exercises/README.md)

[Índice](../README.md) · [Movimento, derivadas e integrais](../notes/01-motion-calculus.md) · [Dinâmica de primeira ordem e rotação](../notes/02-first-order-dynamics.md) · [Resumo de fórmulas](../CHEATSHEET.md)

> **Aviso:** Este material educativo com assistência de IA pode conter erros, traduções imprecisas ou pressupostos incorretos. A utilização é por conta e risco de quem o consulta. Confirme os cálculos de forma independente e nunca utilize os exemplos para controlar máquinas reais.

Os três exercícios básicos usam apenas a biblioteca padrão. Os gráficos usam NumPy e Matplotlib; o notebook local opcional usa JupyterLab. Consulte [Python oficial](https://www.python.org/downloads/) e [a documentação venv](https://docs.python.org/3/library/venv.html).

Os exemplos básicos não exigem bibliotecas externas:

**Windows:** use `py -3` antes de ativar o venv e `python` depois.

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
python3 -m unittest discover -s tests -v
```

**Arquivos Python para leitura ou execução local**

- [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py)
- [`02_first_order_response.py`](../../../exercises/02_first_order_response.py)
- [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py)
- [`plot_models.py`](../../../exercises/plot_models.py) (NumPy, Matplotlib)

## Ambiente local opcional para gráficos e notebook

Os scripts básicos não precisam de pacotes adicionais. Apenas para gráficos ou JupyterLab, crie um ambiente virtual na raiz do repositório. Veja a [documentação oficial do venv](https://docs.python.org/3/library/venv.html) e o [guia Python Packaging](https://packaging.python.org/en/latest/tutorials/installing-packages/).

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

As dependências opcionais estão em [requirements.txt](../../../requirements.txt). Execute os três scripts básicos a partir da raiz do repositório, após revisar o código.
