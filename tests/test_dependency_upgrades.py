"""Regression tests for version-marked Python dependencies and updated Actions."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DependencyUpgradePolicyTests(unittest.TestCase):
    def test_python_310_to_312_dependencies_are_not_overconstrained(self):
        lines = (ROOT / "requirements.txt").read_text(encoding="utf-8").splitlines()
        specs = [s.strip() for s in lines if s.strip() and not s.startswith("#")]
        for python, expected in (
            ("3.10", ["numpy>=1.26"]),
            ("3.11", ["numpy>=1.26", "matplotlib>=3.11.2", "jupyterlab>=4.6.6"]),
            ("3.12", ["numpy>=2.5.4", "matplotlib>=3.11.2", "jupyterlab>=4.6.6"]),
        ):
            match = []
            for spec in specs:
                requirement, _, marker = spec.partition(";")
                marker = marker.strip()
                if marker:
                    relation = re.fullmatch(r'python_version (>=|<) "(\d+\.\d+)"', marker)
                    self.assertIsNotNone(relation)
                    op, bound = relation.groups()
                    current = tuple(map(int, python.split(".")))
                    value = tuple(map(int, bound.split(".")))
                    if not (current >= value if op == ">=" else current < value):
                        continue
                match.append(requirement.strip())
            self.assertEqual(len(match), 1 if python == "3.10" else 3,
                             (python, match))
            self.assertEqual([x.split(",")[0] for x in match], expected)

    def test_action_version_pins_match_reviewed_dependabot_updates(self):
        w = ROOT / ".github" / "workflows"
        expected = {
            "dependency-vulnerability.yml": (
                "actions/setup-python@6d4fd22b20465ccc0f7354476588e8df7c9ca0e0",
                "actions/dependency-review-action@a1d282b36b6f3519aa1f3fc636f609c47dddb294",
            ),
            "semgrep.yml": (
                "actions/setup-python@6d4fd22b20465ccc0f7354476588e8df7c9ca0e0",
                "actions/upload-artifact@cf430e030ddbb5b0abf93d22962f4752f3646cd9",
            ),
            "codeql.yml": (
                "actions/upload-artifact@cf430e030ddbb5b0abf93d22962f4752f3646cd9",
            ),
            "secret-scan.yml": (
                "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
            ),
        }
        for workflow, needles in expected.items():
            content = (w / workflow).read_text(encoding="utf-8")
            for needle in needles:
                with self.subTest(workflow=workflow,token=needle):
                    self.assertIn(needle, content)

    def test_secret_diagnostics_runs_on_main_and_redacts_values(self):
        content = (ROOT / ".github" / "workflows" /
                   "secret-candidate-diagnostics.yml").read_text(encoding="utf-8")
        self.assertIn("if: github.ref == 'refs/heads/main'", content)
        self.assertIn("--results=unverified --json", content)
        self.assertIn("persist-credentials: false", content)
        self.assertNotIn("pull_request:", content)
        self.assertNotIn('print(obj.get("Raw"', content)
        self.assertIn("pinned_action_sha=", content)
        self.assertNotIn("scanner-version:", content)
        self.assertIn(r"(?:/[\w.-]+)+", content)
        self.assertIn('trap \'rm -f "$report" "$errors"\' EXIT', content)

    def test_trufflehog_pinned_sha_and_cli_versions_are_consistent(self):
        # Dependabot updates the pinned action SHA and release comment, but
        # the action's version input and diagnostic image must also follow.
        # Verify consistency instead of forever hardcoding an older SHA.
        scan = (ROOT / ".github" / "workflows" / "secret-scan.yml").read_text(
            encoding="utf-8"
        )
        action = re.search(
            r"(?m)^\s*uses:\s+trufflesecurity/trufflehog@([a-f0-9]{40})"
            r"\s+# v(\d+\.\d+\.\d+)\s*$",
            scan,
        )
        self.assertIsNotNone(action, "TruffleHog action must be SHA pinned")
        config = re.search(r"(?m)^\s*version:\s*(\d+\.\d+\.\d+)\s*$", scan)
        self.assertIsNotNone(config, "TruffleHog CLI version must be specified")
        self.assertEqual(action.group(2), config.group(1))

        diagnostic = (
            ROOT / ".github" / "workflows" /
            "secret-candidate-diagnostics.yml"
        ).read_text(encoding="utf-8")
        image = re.search(
            r"ghcr\.io/trufflesecurity/trufflehog:(\d+\.\d+\.\d+)",
            diagnostic,
        )
        self.assertIsNotNone(image)
        self.assertEqual(image.group(1), action.group(2))

    def test_pip_audit_resolves_supported_interpreters(self):
        content = (ROOT / ".github" / "workflows" /
                   "dependency-vulnerability.yml").read_text(encoding="utf-8")
        self.assertIn('python-version: ["3.10", "3.11", "3.12"]', content)
        self.assertIn("matrix.python-version", content)


if __name__ == "__main__":
    unittest.main()
