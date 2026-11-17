"""Offline tests: inspect submitted file bytes without running PR source."""
import base64
import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "trusted_pr_audit_test", ROOT / "tools" / "trusted_pr_audit.py"
)
# The script imports the base-branch policy under the tools path.
import sys
sys.path.insert(0, str(ROOT / "tools"))
trusted = importlib.util.module_from_spec(spec)
spec.loader.exec_module(trusted)


class TrustedPullRequestAuditTests(unittest.TestCase):
    def test_rejects_submitted_dynamic_code_from_blob_data(self):
        sha = "a" * 40
        received = []

        def fetch_blob(blob_sha):
            received.append(blob_sha)
            return "import os\n"

        errors, review = trusted.inspect_changed_files(
            [{"filename": "exercises/nested/new_lesson.py",
              "status": "added", "sha": sha}],
            fetch_blob,
        )
        self.assertEqual(received, [sha])
        self.assertTrue(any("non-allowlisted import" in e for e in errors))
        self.assertEqual(review, [])

    def test_nested_executable_uses_trusted_policy(self):
        self.assertTrue(trusted.is_executable_example(Path("exercises/nested/test.py")))
        self.assertTrue(trusted.is_executable_example(
            Path("ros2/demo_pkg/telemetry_demo/nested/test.py")))
        self.assertFalse(trusted.is_executable_example(Path("docs/en/README.md")))

    def test_reports_security_sensitive_edits_without_executing_them(self):
        calls = []
        changed = [
            {"filename": "tools/check_executable_sources.py",
             "status": "modified", "sha": "b" * 40},
            {"filename": ".github/workflows/validate.yml",
             "status": "modified", "sha": "c" * 40},
        ]
        errors, notes = trusted.inspect_changed_files(
            changed, lambda sha: calls.append(sha)
        )
        self.assertFalse(errors)
        self.assertEqual(len(notes), 2)
        self.assertEqual(calls, [])

    def test_review_flags_all_ros_source_and_host_executable_changes(self):
        # The ROS smoke test runs a repository shell script and Docker build.
        # Any changed ROS file must be highlighted for human review, even if
        # it is not Python and cannot be checked using Python AST parsing.
        for name in (
            "ros2/smoke_test.sh", "ros2/Dockerfile",
            "ros2/compose.yaml", "ros2/demo_pkg/package.xml",
            "ros2/demo_pkg/setup.cfg", ".github/workflows/new.yml",
            ".github/dependabot.yml", "tools/validate_repository.py",
            "scripts/helper.sh", "setup.command",
        ):
            with self.subTest(name=name):
                self.assertTrue(trusted.needs_independent_review(Path(name)))
                errors, notes = trusted.inspect_changed_files(
                    [{"filename": name, "status": "modified",
                      "sha": "a" * 40}], lambda _sha: "")
                self.assertEqual(errors, [])
                self.assertEqual(len(notes), 1)
        self.assertFalse(trusted.needs_independent_review(Path("docs/en/README.md")))

    def test_base_policy_inspects_changed_markdown_and_svg_as_data(self):
        sha = "a" * 40
        for name, source, must_reject in (
            ("docs/en/README.md", "## Section\\n", False),
            ("docs/en/README.md", "<iframe/>\\n", True),
            ("README.md", "[link](javascript:example)\\n", True),
            ("assets/figures/example.svg",
             '<svg xmlns="http://www.w3.org/2000/svg"><rect width="1"/></svg>',
             False),
            ("assets/figures/example.svg",
             '<svg xmlns="http://www.w3.org/2000/svg"><script/></svg>',
             True),
        ):
            with self.subTest(path=name, reject=must_reject):
                calls = []
                def read_only_blob(blob_sha):
                    calls.append(blob_sha)
                    return source
                errors, review_notes = trusted.inspect_changed_files(
                    [{"filename": name, "status": "modified", "sha": sha}],
                    read_only_blob)
                self.assertEqual(calls, [sha])
                self.assertEqual(bool(errors), must_reject)
                self.assertEqual(review_notes, [])

    def test_passive_source_detection_is_extension_based(self):
        for name in ("docs/en/README.md", "README.md",
                     "assets/figures/example.svg", "nested/new-guide.MD"):
            self.assertTrue(trusted.is_passive_content_source(Path(name)))
        for name in ("exercises/simple.py", "ros2/smoke_test.sh",
                     "notebooks/lesson.ipynb"):
            self.assertFalse(trusted.is_passive_content_source(Path(name)))

    def test_rejects_invalid_metadata_and_unreadable_example(self):
        changed = [
            {"filename": "../outside.py", "status": "added", "sha": "a" * 40},
            {"filename": "ros2/demo_pkg/telemetry_demo/new.py",
             "status": "added", "sha": "not-a-sha"},
            {"filename": "exercises/bad.py", "status": "modified",
             "sha": "a" * 40},
        ]
        def corrupt(_sha):
            raise ValueError("Untrusted blob response")
        errors, _ = trusted.inspect_changed_files(changed, corrupt)
        self.assertEqual(len(errors), 3)

    def test_base_policy_accepts_reviewed_math_and_rejects_exec(self):
        sha = "a" * 40
        for source, accepted in (
            ("import math\nprint(math.sqrt(4))\n", True),
            ("exec('pass')\n", False),
        ):
            with self.subTest(source=source):
                errors, _ = trusted.inspect_changed_files(
                    [{"filename": "exercises/simple.py",
                      "status": "modified", "sha": sha}],
                    lambda _sha: source,
                )
                self.assertEqual(not bool(errors), accepted)

    def test_fetcher_decodes_blob_and_checks_size(self):
        raw = b"print('data only')\n"
        calls = []
        def request_json(path):
            calls.append(path)
            return {
                "encoding": "base64", "size": len(raw),
                "content": base64.b64encode(raw).decode("ascii"),
            }
        fetch = trusted.blob_fetcher(request_json)
        self.assertEqual(fetch("a" * 40), raw.decode("utf-8"))
        self.assertEqual(calls, ["git/blobs/" + "a" * 40])
        with self.assertRaises(ValueError):
            fetch("invalid")

    def test_pagination_and_bounds(self):
        pages = []
        def request_json(path):
            pages.append(path)
            return [{"filename": "README.md"}]
        self.assertEqual(len(trusted.pull_request_files(request_json, 5)), 1)
        self.assertEqual(pages, ["pulls/5/files?per_page=100&page=1"])
        with self.assertRaises(ValueError):
            trusted.pull_request_files(request_json, 0)


if __name__ == "__main__":
    unittest.main()
