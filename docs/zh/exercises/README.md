# Python 练习

**切换此页语言:** [en](../../en/exercises/README.md) · [fr](../../fr/exercises/README.md) · [de](../../de/exercises/README.md) · [it](../../it/exercises/README.md) · [es](../../es/exercises/README.md) · [pt](../../pt/exercises/README.md) · [zh](README.md) · [ja](../../ja/exercises/README.md) · [nb](../../nb/exercises/README.md) · [ru](../../ru/exercises/README.md) · [ko](../../ko/exercises/README.md) · [fi](../../fi/exercises/README.md) · [pl](../../pl/exercises/README.md)

[目录](../README.md) · [运动、导数与积分](../notes/01-motion-calculus.md) · [一阶动力学与旋转运动](../notes/02-first-order-dynamics.md) · [公式速查表](../CHEATSHEET.md)

> **警告：** 本仓库是人工智能辅助编写的教学资料，可能存在事实错误、公式错误、翻译不准确或不成立的假设。使用者自行承担风险，必须独立验证计算结果。**切勿使用示例程序控制真实机器、电机或机器人。**

三个基础练习只使用 Python 标准库。绘图使用 NumPy 和 Matplotlib；可选的本地笔记本使用 JupyterLab。请参阅 [Python 官方下载](https://www.python.org/downloads/)和 [venv 文档](https://docs.python.org/3/library/venv.html)。

基础练习不需要安装第三方软件包：

**Windows：**激活 venv 前请将 `python3` 换成 `py -3`，激活后使用 `python`。

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
python3 -m unittest discover -s tests -v
```

**可阅读或本地运行的 Python 源文件**

- [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py)
- [`02_first_order_response.py`](../../../exercises/02_first_order_response.py)
- [`03_rotation_energy.py`](../../../exercises/03_rotation_energy.py)
- [`plot_models.py`](../../../exercises/plot_models.py) (NumPy, Matplotlib)

## 用于绘图和笔记本的可选本地环境

上面的基础脚本不需要额外安装软件包。只有绘图或使用 JupyterLab 时，才需要在仓库根目录创建虚拟环境。参见 [Python 官方 venv 文档](https://docs.python.org/3/library/venv.html)和 [Python Packaging 官方指南](https://packaging.python.org/en/latest/tutorials/installing-packages/)。

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

可选依赖列于 [requirements.txt](../../../requirements.txt)。请先检查源码，再从仓库根目录运行上面的基础示例。
