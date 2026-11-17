"""Static invariants for security workflows; no secrets, scans or Docker executed."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"


def workflow(name):
    return (WORKFLOWS / name).read_text(encoding="utf-8")


class SecurityWorkflowConfigurationTests(unittest.TestCase):
    def test_single_real_project_validation(self):
        self.assertFalse((WORKFLOWS / "ci.yml").exists())
        core = workflow("validate.yml")
        for literal in ("check_executable_sources.py", "unittest discover",
                        "validate_repository.py", "--network none",
                        "--user 65534:65534"):
            self.assertIn(literal, core)

    def test_dependency_scan_uses_real_manifest(self):
        body = workflow("dependency-vulnerability.yml")
        self.assertIn("python -m pip_audit --strict --requirement requirements.txt", body)
        self.assertIn("actions/dependency-review-action@", body)
        self.assertIn("!github.event.repository.private", body)
        self.assertNotIn("pip freeze", body)
        self.assertNotIn("dev,data,ai,pytorch", body)

    def test_snyk_fails_without_secret_and_never_runs_on_pr(self):
        body = workflow("snyk.yml")
        self.assertIn("secrets.SNYK_TOKEN", body)
        self.assertIn('if [ -z "$SNYK_TOKEN" ]', body)
        self.assertIn("exit 1", body)
        self.assertIn("branches: [main]", body)
        self.assertNotIn("pull_request:", body)
        self.assertIn("snyk/actions/python@", body)
        self.assertNotIn("env.SNYK_TOKEN != ''", body)

    def test_codeql_semgrep_private_artifacts_and_public_upload(self):
        codeql = workflow("codeql.yml")
        semgrep = workflow("semgrep.yml")
        for body in (codeql, semgrep):
            self.assertIn("!github.event.repository.private", body)
            self.assertIn("github.event.pull_request.head.repo.fork", body)
            self.assertIn("actions/upload-artifact@", body)
            self.assertIn("security-events: write", body)
            self.assertIn("pull_request:", body)
        self.assertIn("github/codeql-action/init@", codeql)
        self.assertIn("github/codeql-action/analyze@", codeql)
        self.assertIn("'always' || 'never'", codeql)
        self.assertIn("queries: security-extended", codeql)
        self.assertIn("semgrep==1.185.0", semgrep)
        self.assertIn("semgrep scan --config p/python", semgrep)
        self.assertIn("--config p/security-audit", semgrep)
        self.assertIn("--sarif --output semgrep.sarif --error", semgrep)
        self.assertIn("steps.scan.outcome == 'failure'", semgrep)
        self.assertNotIn("semgrep/semgrep-action@", semgrep)
        self.assertNotIn("generateSarif", semgrep)

    def test_docker_image_scan_only_on_trusted_main(self):
        body = workflow("docker-vulnerability.yml")
        self.assertIn("branches: [main]", body)
        self.assertIn("if: github.ref == 'refs/heads/main'", body)
        self.assertNotIn("pull_request:", body)
        for name in ("ros2/Dockerfile", "ros2/control_lab/Dockerfile",
                     "docker build", "aquasecurity/trivy-action@",
                     "ignore-unfixed: true", 'exit-code: "1"',
                     "severity: HIGH,CRITICAL", "matrix.name"):
            self.assertIn(name, body)

    def test_dependabot_points_to_existing_manifest_directories(self):
        config = (ROOT / ".github" / "dependabot.yml").read_text(encoding="utf-8")
        self.assertIn("version: 2", config)
        self.assertEqual(config.count('package-ecosystem: "pip"'), 2)
        self.assertEqual(config.count('package-ecosystem: "docker"'), 2)
        self.assertIn('package-ecosystem: "github-actions"', config)
        for name in ('directory: "/"', 'directory: "/ros2/demo_pkg"',
                     'directory: "/ros2"', 'directory: "/ros2/control_lab"'):
            self.assertIn(name, config)


if __name__ == "__main__":
    unittest.main()
