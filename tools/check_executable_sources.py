"""Offline AST checks for the user-facing synthetic Python examples.

This is a conservative, reviewable policy for accidental high-risk edits.
It is NOT a Python sandbox or a proof that reviewed code is harmless.
"""
from __future__ import annotations

import ast
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXERCISE_IMPORTS = frozenset({"math", "numpy", "matplotlib.pyplot"})
ROS_RUNTIME_IMPORTS = frozenset({
    "math", "rclpy", "rclpy.node", "rclpy.executors",
    "std_msgs.msg", "std_srvs.srv",
})
ROS_LAUNCH_IMPORTS = frozenset({"launch", "launch_ros.actions"})
ROS_SETUP_IMPORTS = frozenset({"setuptools"})
BLOCKED_NAMES = frozenset({
    "__builtins__", "__loader__", "__spec__", "__import__",
    "eval", "exec", "compile", "open", "input", "breakpoint",
    "getattr", "setattr", "delattr", "globals", "locals", "vars",
})
BLOCKED_ATTRIBUTES = frozenset({
    "system", "popen", "Popen", "check_call", "check_output",
    "eval", "exec", "compile", "open", "unlink", "rmtree",
    "remove", "rename", "replace", "urlopen",
    # Scientific packages are permitted for *computing and plotting*, not
    # for reading arbitrary files or writing plots/data to local paths.
    "load", "save", "savez", "savez_compressed", "loadtxt", "savetxt",
    "genfromtxt", "fromfile", "tofile", "memmap", "open_memmap",
    "imread", "imsave", "savefig", "read_pickle", "to_pickle",
    "read_text", "write_text", "read_bytes", "write_bytes",
    "dump", "dumps",
})


def allowed_imports(path: Path) -> frozenset[str]:
    relative = path.relative_to(ROOT)
    if relative.suffix == ".ipynb" or relative.parts[0] == "exercises":
        return EXERCISE_IMPORTS
    if relative == Path("ros2/demo_pkg/setup.py"):
        return ROS_SETUP_IMPORTS
    if relative.parts[:3] == ("ros2", "demo_pkg", "launch"):
        return ROS_LAUNCH_IMPORTS
    if relative.parts[:3] == ("ros2", "demo_pkg", "telemetry_demo"):
        return ROS_RUNTIME_IMPORTS
    return frozenset()


def audit_source(source: str, path: Path) -> list[str]:
    """Parse but never import or execute the provided source."""
    issues = []
    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError as error:
        return [f"{path}: invalid Python syntax: {error.msg}"]
    allow = allowed_imports(path)
    for node in ast.walk(tree):
        line = getattr(node, "lineno", 1)
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name not in allow:
                    issues.append(f"{path}:{line}: non-allowlisted import {alias.name}")
        elif isinstance(node, ast.ImportFrom):
            if node.level or node.module not in allow or any(
                alias.name == "*" for alias in node.names
            ):
                issues.append(f"{path}:{line}: non-allowlisted from-import")
            else:
                # A forbidden scientific file API is still forbidden when
                # imported directly and renamed: 'from numpy import load
                # as reader' contains no ast.Attribute at its call site.
                for alias in node.names:
                    symbol = alias.name
                    if (symbol in BLOCKED_NAMES or
                            symbol in BLOCKED_ATTRIBUTES or
                            symbol.startswith("__") or symbol.endswith("__")):
                        issues.append(
                            f"{path}:{line}: prohibited from-import symbol {symbol}"
                        )
        elif isinstance(node, ast.Name) and node.id in BLOCKED_NAMES:
            issues.append(f"{path}:{line}: prohibited name {node.id}")
        elif isinstance(node, ast.Attribute):
            # Cooperative ROS Node constructors legitimately use super().__init__.
            super_init = (
                node.attr == "__init__"
                and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name)
                and node.value.func.id == "super"
                and not node.value.args and not node.value.keywords
            )
            if not super_init and (
                node.attr in BLOCKED_ATTRIBUTES
                or node.attr.startswith("__") or node.attr.endswith("__")
            ):
                issues.append(f"{path}:{line}: prohibited attribute {node.attr}")
    return issues



NOTEBOOK_TOP_LEVEL_FIELDS = frozenset({"nbformat", "nbformat_minor", "metadata", "cells"})
NOTEBOOK_METADATA_FIELDS = frozenset({"kernelspec", "language_info"})
NOTEBOOK_KERNELSPEC_FIELDS = frozenset({"name", "language", "display_name"})
NOTEBOOK_LANGUAGE_FIELDS = frozenset({"name"})
NOTEBOOK_CELL_FIELDS = frozenset({"cell_type", "metadata", "source", "id",
                                  "outputs", "execution_count", "attachments"})

MAX_NOTEBOOK_SOURCE_BYTES = 1_000_000
DISALLOWED_NOTEBOOK_MARKUP = (
    # Jupyter's Markdown renderer may differ from GitHub's sanitizer.
    # These notebook cells contain only text and inline mathematics.
    "<script", "<iframe", "<object", "<embed", "<img", "<svg", "<video",
    "<audio", "<source", "<style", "<link", "<form", "<base", "<meta",
    "<math", "<foreignobject", "javascript:", "vbscript:", "data:",
    "file:", "blob:", "onload=", "onerror=", "onclick=",
)


def audit_notebook_source(source: str, path: Path) -> list[str]:
    """Inspect notebook JSON and each code cell without running any cell.

    This checks a limited teaching-notebook format, not notebook-client bugs,
    supply-chain integrity or arbitrary Python behavior.
    """
    if len(source.encode("utf-8")) > MAX_NOTEBOOK_SOURCE_BYTES:
        return [f"{path}: notebook exceeds source-size limit"]
    try:
        notebook = json.loads(source)
    except (ValueError, UnicodeError) as error:
        return [f"{path}: invalid notebook JSON: {error}"]
    if not isinstance(notebook, dict) or notebook.get("nbformat") != 4:
        return [f"{path}: require Jupyter notebook format 4"]
    if set(notebook) - NOTEBOOK_TOP_LEVEL_FIELDS:
        return [f"{path}: unsupported notebook top-level fields"]
    if type(notebook.get("nbformat_minor")) is not int:
        return [f"{path}: notebook minor version must be an integer"]
    meta = notebook.get("metadata")
    if not isinstance(meta, dict) or set(meta) - NOTEBOOK_METADATA_FIELDS:
        return [f"{path}: unsupported notebook metadata"]
    kernel = meta.get("kernelspec")
    if not isinstance(kernel, dict) or set(kernel) - NOTEBOOK_KERNELSPEC_FIELDS \
            or kernel.get("language") != "python" or kernel.get("name") != "python3":
        return [f"{path}: require a minimal Python 3 kernel specification"]
    info = meta.get("language_info")
    if info is not None and (
        not isinstance(info, dict) or set(info) - NOTEBOOK_LANGUAGE_FIELDS
        or info.get("name") != "python"
    ):
        return [f"{path}: unsupported Python language_info metadata"]
    cells = notebook.get("cells")
    if not isinstance(cells, list):
        return [f"{path}: notebook cells must be a list"]

    issues: list[str] = []
    for index, cell in enumerate(cells):
        label = f"{path}:cell[{index}]"
        if not isinstance(cell, dict) or not isinstance(cell.get("metadata"), dict):
            issues.append(f"{label}: invalid cell structure or metadata")
            continue
        # Jupyter extensions can attach display/runtime configuration here.
        # This curriculum uses only empty cell metadata; do not accept
        # unreviewed extension-specific metadata or extra source fields.
        if cell["metadata"] or set(cell) - NOTEBOOK_CELL_FIELDS:
            issues.append(f"{label}: unsupported cell metadata or fields")
        if "id" in cell and (
            not isinstance(cell["id"], str)
            or re.fullmatch(r"[A-Za-z0-9_-]{1,64}", cell["id"]) is None
        ):
            issues.append(f"{label}: invalid cell id")
        raw = cell.get("source")
        if isinstance(raw, str):
            body = raw
        elif isinstance(raw, list) and all(isinstance(line, str) for line in raw):
            body = "".join(raw)
        else:
            issues.append(f"{label}: invalid cell source")
            continue
        kind = cell.get("cell_type")
        if kind == "code":
            if "attachments" in cell:
                issues.append(f"{label}: code-cell attachments are unsupported")
            if cell.get("outputs") != [] or cell.get("execution_count") is not None:
                issues.append(f"{label}: saved execution outputs are forbidden")
            issues.extend(audit_source(body, path))
        elif kind == "markdown":
            if "outputs" in cell or "execution_count" in cell:
                issues.append(f"{label}: Markdown cannot have execution fields")
            if "attachments" in cell:
                issues.append(f"{label}: embedded notebook attachments are forbidden")
            lowered = body.lower()
            if any(marker in lowered for marker in DISALLOWED_NOTEBOOK_MARKUP):
                issues.append(f"{label}: active HTML or script-like markup is forbidden")
        else:
            issues.append(f"{label}: only code and Markdown cells are allowed")
    return issues


def audited_notebooks() -> list[Path]:
    """Find repository notebooks without walking local dependencies or checkpoints."""
    skip = {".git", ".venv", "venv", "node_modules", "__pycache__",
            ".ipynb_checkpoints", "build", "install", "dist", "log", ".tox"}
    paths = []
    for directory, subdirs, filenames in os.walk(ROOT):
        subdirs[:] = [name for name in subdirs if name not in skip]
        for filename in filenames:
            if filename.endswith(".ipynb"):
                paths.append(Path(directory) / filename)
    return sorted(paths)


def audited_files() -> list[Path]:
    """Scan newly added Python files in these execution surfaces too."""
    files = [
        *sorted((ROOT / "exercises").rglob("*.py")),
        *sorted((ROOT / "ros2" / "demo_pkg").rglob("*.py")),
    ]
    return files


def check() -> list[str]:
    python_issues = [
        issue for path in audited_files()
        for issue in audit_source(path.read_text(encoding="utf-8"), path)
    ]
    notebook_issues = [
        issue for path in audited_notebooks()
        for issue in audit_notebook_source(path.read_text(encoding="utf-8"), path)
    ]
    return python_issues + notebook_issues


if __name__ == "__main__":
    errors = check()
    if errors:
        for issue in errors:
            print("ERROR:", issue)
        raise SystemExit(1)
    print(f"AST policy passed for {len(audited_files())} Python scripts and {len(audited_notebooks())} notebooks.")
