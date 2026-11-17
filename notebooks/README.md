# Optional Jupyter notebook

The source file [`first_order_response.ipynb`](first_order_response.ipynb) can be run locally using JupyterLab. It is a standalone, synthetic example that generates a plot using NumPy and Matplotlib.

From the **repository root**, after creating and activating a Python virtual environment on macOS/Linux (on Windows, use `python -m ...` after activation):

```bash
python3 -m pip install -r requirements.txt
python3 -m jupyter lab
```

Open the notebook in the browser window created by JupyterLab. This launches local software and does not require giving an external notebook website access to your GitHub account.

Review the notebook's code cells before running them. The repository's source auditor parses local notebook cells and rejects saved outputs, but it is not a security sandbox; Python and its dependencies still execute with the user's permissions.

The three basic examples can be run directly with a local Python installation and no third-party packages; see the [exercise guide](../docs/en/exercises/README.md). Do not upload private content or secrets to online code services.