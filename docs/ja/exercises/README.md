# Python 演習

**このページの言語を切り替える:** [en](../../en/exercises/README.md) · [fr](../../fr/exercises/README.md) · [de](../../de/exercises/README.md) · [it](../../it/exercises/README.md) · [es](../../es/exercises/README.md) · [pt](../../pt/exercises/README.md) · [zh](../../zh/exercises/README.md) · [ja](README.md) · [nb](../../nb/exercises/README.md) · [ru](../../ru/exercises/README.md) · [ko](../../ko/exercises/README.md) · [fi](../../fi/exercises/README.md) · [pl](../../pl/exercises/README.md)

[目次](../README.md) · [運動・微分・積分](../notes/01-motion-calculus.md) · [一次系の動特性と回転](../notes/02-first-order-dynamics.md) · [公式早見表](../CHEATSHEET.md)

> **注意：** 本教材は AI を利用して作成されており、誤り、不正確な翻訳、誤った仮定が含まれる可能性があります。利用は自己責任で行い、数式と計算を独立に確認してください。**実機のモーターや工作機械の制御に使用しないでください。**

3 つの基本演習は Python 標準ライブラリのみで動作します。グラフには NumPy と Matplotlib、任意のローカルノートブックには JupyterLab を使用します。[Python 公式サイト](https://www.python.org/downloads/)と [venv の説明](https://docs.python.org/3/library/venv.html)を参照してください。

基本的な演習には追加ライブラリは不要です：

**Windows：**venv を有効にする前は `py -3`、有効にした後は `python` を使います。

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
python3 -m unittest discover -s tests -v
```

**閲覧またはローカル実行できる Python ファイル**

- [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py)
- [`02_first_order_response.py`](../../../exercises/02_first_order_response.py)
- [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py)
- [`plot_models.py`](../../../exercises/plot_models.py) (NumPy, Matplotlib)

## グラフとノートブック用の任意のローカル環境

上の基本スクリプトには追加パッケージは不要です。グラフや JupyterLab を使う場合のみ、リポジトリのルートで仮想環境を作成します。[公式 venv ドキュメント](https://docs.python.org/3/library/venv.html)と [Python Packaging ガイド](https://packaging.python.org/en/latest/tutorials/installing-packages/)を参照してください。

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

任意の依存パッケージは [requirements.txt](../../../requirements.txt) に記載されています。ソースを確認してからリポジトリのルートで上の基本スクリプトを実行してください。
