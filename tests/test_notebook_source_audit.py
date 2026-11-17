"""Notebook source must be inspected as data, without running code cells."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import check_executable_sources as policy
import trusted_pr_audit as trusted


def notebook(code="import math\nprint(math.sqrt(4))\n", markdown="# Local math\n",
             *, outputs=None, execution_count=None, kernel="python"):
    return json.dumps({
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {"kernelspec": {"name": "python3", "language": kernel}},
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": [markdown]},
            {"cell_type": "code", "metadata": {}, "source": [code],
             "execution_count": execution_count,
             "outputs": [] if outputs is None else outputs},
        ],
    })


class NotebookSourceAudit(unittest.TestCase):
    def setUp(self):
        self.path = ROOT / "notebooks" / "synthetic.ipynb"

    def test_good_notebook_and_published_file_are_read_only_data(self):
        self.assertEqual(policy.audit_notebook_source(notebook(), self.path), [])
        published = ROOT / "notebooks" / "first_order_response.ipynb"
        self.assertIn(published, policy.audited_notebooks())
        self.assertEqual(policy.audit_notebook_source(
            published.read_text(encoding="utf-8"), published), [])

    def test_rejects_imports_dynamic_execution_and_active_markup(self):
        for source in ("import os\n", "exec('pass')\n", "open('data.txt')\n"):
            with self.subTest(source=source):
                self.assertTrue(policy.audit_notebook_source(
                    notebook(code=source), self.path))
        for markup in ("<script>alert(1)</script>", '<iframe src="x"></iframe>',
                       "<video src='https://example.invalid/sample'></video>",
                       "<img src='https://example.invalid/image.png'>",
                       "[click](javascript:alert(1))", "<div onload='x'>",
                       "[page][ref]\n[ref]: data:image/svg+xml,example",
                       "![diagram][asset]\n[asset]: file:///tmp/pic",
                       "[page][ref]\n[ref]: blob:example"):
            with self.subTest(markup=markup):
                self.assertTrue(policy.audit_notebook_source(
                    notebook(markdown=markup), self.path))

    def test_minimal_notebook_text_and_relative_references_remain_allowed(self):
        good = notebook(
            markdown="# Local model\n"
                     "[first-order chapter][guide]\n"
                     "[guide]: ../docs/en/notes/02-first-order-dynamics.md\n"
                     "Inline mathematics: $v(t)=v_0$.\n")
        self.assertEqual([], policy.audit_notebook_source(good, self.path))

    def test_notebook_code_cannot_call_scientific_file_io(self):
        for code in (
            "import numpy as np\nnp.load('data.npy')\n",
            "import numpy as np\nnp.save('data.npy', [1])\n",
            "import matplotlib.pyplot as plt\nplt.savefig('plot.svg')\n",
        ):
            with self.subTest(code=code):
                errors = policy.audit_notebook_source(
                    notebook(code=code), self.path)
                self.assertTrue(any("prohibited attribute" in issue
                                    for issue in errors))

    def test_direct_import_of_forbidden_api_is_not_hidden_by_alias(self):
        for code in (
            "from numpy import load as reader\nreader('data.npy')\n",
            "from matplotlib.pyplot import savefig as export\n",
        ):
            with self.subTest(code=code):
                failures = policy.audit_notebook_source(
                    notebook(code=code), self.path)
                self.assertTrue(any("prohibited from-import symbol" in e
                                    for e in failures), failures)

    def test_rejects_preexecuted_invalid_or_nonpython_notebooks(self):
        cases = (
            notebook(outputs=[{"output_type": "stream", "text": "unsafe"}]),
            notebook(execution_count=1),
            notebook(kernel="bash"),
            "{ invalid json",
            json.dumps({"nbformat": 3, "cells": []}),
        )
        for candidate in cases:
            with self.subTest(candidate=candidate[:60]):
                self.assertTrue(policy.audit_notebook_source(candidate, self.path))

    def test_notebook_rejects_unreviewed_kernel_and_extension_metadata(self):
        base = json.loads(notebook())
        variants = []
        for extra in ("widgets", "execution", "trusted"):
            bad = json.loads(notebook())
            bad["metadata"][extra] = {"enabled": True}
            variants.append(bad)
        for kernel in ("bash", "python", "unreviewed"):
            bad = json.loads(notebook())
            bad["metadata"]["kernelspec"]["name"] = kernel
            variants.append(bad)
        bad = json.loads(notebook())
        bad["metadata"]["kernelspec"]["extra"] = "unexpected"
        variants.append(bad)
        bad = json.loads(notebook())
        bad["metadata"]["language_info"] = {"name": "python", "extra": 1}
        variants.append(bad)
        bad = json.loads(notebook())
        bad["cells"][0]["metadata"] = {"trusted": True}
        variants.append(bad)
        bad = json.loads(notebook())
        bad["cells"][1]["metadata"] = {"tags": ["parameters"]}
        variants.append(bad)
        bad = json.loads(notebook())
        bad["cells"][0]["attachments"] = {}
        variants.append(bad)
        bad = json.loads(notebook())
        bad["cells"][1]["unexpected_extension_data"] = {}
        variants.append(bad)
        bad = json.loads(notebook())
        bad["cells"][1]["id"] = "../config"
        variants.append(bad)
        bad = json.loads(notebook())
        bad["extra_top_level"] = {}
        variants.append(bad)
        for candidate in variants:
            with self.subTest(candidate=str(candidate)[:120]):
                self.assertTrue(policy.audit_notebook_source(
                    json.dumps(candidate), self.path))

    def test_minimal_notebook_optional_metadata_and_cell_ids(self):
        good = json.loads(notebook())
        good["metadata"]["language_info"] = {"name": "python"}
        good["cells"][0]["id"] = "intro"
        good["cells"][1]["id"] = "code"
        self.assertEqual([], policy.audit_notebook_source(
            json.dumps(good), self.path))

    def test_local_dependency_guidance_matches_repository(self):
        published = ROOT / "notebooks" / "first_order_response.ipynb"
        doc = json.loads(published.read_text(encoding="utf-8"))
        combined = "\n".join("".join(cell["source"]) for cell in doc["cells"])
        self.assertIn("requirements.txt", combined)
        self.assertNotIn("requirements-plot.txt", combined)
        self.assertNotIn("Colab may display", combined)
        self.assertTrue((ROOT / "requirements.txt").exists())
        self.assertTrue((ROOT / "docs/en/notes/02-first-order-dynamics.md").exists())

    def test_trusted_pr_reads_notebook_blob_without_executing_it(self):
        name = Path("notebooks/nested/malicious.ipynb")
        self.assertTrue(trusted.is_executable_example(name))
        self.assertTrue(trusted.is_executable_example(Path("docs/en/synthetic.ipynb")))
        self.assertTrue(trusted.needs_independent_review(Path("docs/en/synthetic.ipynb")))
        self.assertTrue(trusted.needs_independent_review(name))
        sha = "a" * 40
        fetched = []
        def fetch(blob_sha):
            fetched.append(blob_sha)
            return notebook(code="import os\n")
        issues, notes = trusted.inspect_changed_files(
            [{"filename": name.as_posix(), "status": "added", "sha": sha}],
            fetch,
        )
        self.assertEqual(fetched, [sha])
        self.assertTrue(any("non-allowlisted import" in s for s in issues))
        self.assertTrue(any("Independent review required" in s for s in notes))


if __name__ == "__main__":
    unittest.main()
