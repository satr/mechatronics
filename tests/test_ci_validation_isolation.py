"""Keep untrusted PR Python checks off the runner host.

These are static workflow-policy checks, not a sandbox penetration test.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ValidationWorkflowIsolationTests(unittest.TestCase):
    def test_pr_python_executes_in_restricted_container(self):
        workflow = (ROOT / ".github/workflows/validate.yml").read_text(encoding="utf-8")
        for token in (
            "pull_request:", "permissions:", "contents: read",
            "persist-credentials: false", "docker run --rm",
            "--network none", "--read-only", "--cap-drop ALL",
            "--security-opt no-new-privileges", "--pids-limit 128",
            "--memory 1g", "--user 65534:65534",
            "dst=/workspace,readonly", "PYTHONDONTWRITEBYTECODE=1",
            "python:3.11-slim-bookworm",
            "python3 tools/check_executable_sources.py",
            "python3 -m unittest discover -s tests -v",
            "python3 tools/validate_repository.py",
        ):
            with self.subTest(token=token):
                self.assertIn(token, workflow)
        self.assertNotIn("actions/setup-python", workflow)
        self.assertNotIn("docker.sock", workflow)


if __name__ == "__main__":
    unittest.main()
