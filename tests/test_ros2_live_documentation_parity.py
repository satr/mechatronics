"""ROS 2 localized documentation: distinguish real CI smoke from host/hardware proof."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = tuple(sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir()))
LIVE_WORKFLOW_LINK = "../../../.github/workflows/ros2-live-smoke.yml"

# Previously published false statements in this chapter; retained as tests only.
OUTDATED = (
    "Docker execution was not verified in the authoring environment",
    "Docker execution has not been verified in the authoring environment",
    "Работа контейнера здесь не была проверена непосредственно",
    "Docker wurde in dieser Autorenumgebung nicht ausgeführt",
    "Le conteneur n'a pas été exécuté dans l'environnement de création",
    "Docker non è stato eseguito nell'ambiente di creazione",
    "No se ejecutó Docker en el entorno de autoría",
    "Docker não foi executado no ambiente de autoria",
    "编写环境没有运行 Docker",
    "作成環境では Docker を実行していない",
    "Docker ble ikke kjørt i forfattermiljøet",
    "작성 환경에는 Docker 실행 기능이 없어",
    "Dockeria ei ajettu kirjoitusympäristössä",
    "Runtime Docker execution was not verified",
)


class Ros2DocumentedVerificationScope(unittest.TestCase):
    def test_every_locale_links_actual_live_workflow_without_stale_status(self):
        for locale in LOCALES:
            with self.subTest(locale=locale):
                text = (ROOT / "docs" / locale / "notes" /
                        "06-ros2-foundations.md").read_text(encoding="utf-8")
                part = text.split('<a id="section-11"></a>', 1)[1].split(
                    '<a id="section-12"></a>', 1
                )[0]
                self.assertIn(f"]({LIVE_WORKFLOW_LINK})", part)
                self.assertIn("/training/status", part)
                self.assertIn("/training/count", part)
                for stale in OUTDATED:
                    self.assertNotIn(stale, text)

    def test_live_docker_smoke_is_main_only_not_pr_executable(self):
        # Shell, Compose and Dockerfile content must not be run on a host
        # runner from an unreviewed pull-request head.
        workflow = (ROOT / ".github" / "workflows" /
                    "ros2-live-smoke.yml").read_text(encoding="utf-8")
        triggers = workflow.split("on:", 1)[1].split("jobs:", 1)[0]
        self.assertIn("push:", triggers)
        self.assertIn("branches: [main]", triggers)
        self.assertIn("workflow_dispatch:", triggers)
        self.assertNotIn("pull_request:", triggers)
        self.assertNotIn("pull_request_target:", triggers)
        self.assertIn("if: github.ref == 'refs/heads/main'", workflow)

    def test_each_locale_describes_postmerge_not_pr_live_verification(self):
        for locale in LOCALES:
            with self.subTest(locale=locale):
                body = (ROOT / "docs" / locale / "notes" /
                        "06-ros2-foundations.md").read_text(encoding="utf-8")
                section = body.split('<a id="section-11"></a>', 1)[1].split(
                    '<a id="section-12"></a>', 1)[0]
                for token in ("main", "pull_request", "workflow_dispatch"):
                    self.assertIn(token, section)

    def test_workflow_actually_uses_single_container_smoke_script(self):
        workflow = (ROOT / ".github" / "workflows" /
                    "ros2-live-smoke.yml").read_text(encoding="utf-8")
        script = (ROOT / "ros2" / "smoke_test.sh").read_text(encoding="utf-8")
        self.assertIn("bash ros2/smoke_test.sh", workflow)
        self.assertIn("docker compose up --build -d", script)
        self.assertIn("ros2 topic echo --once /training/status", script)
        self.assertIn("ros2 service call /training/count", script)
        self.assertIn("no host", (ROOT / "ros2" / "README.md").read_text(
            encoding="utf-8").lower())


if __name__ == "__main__":
    unittest.main()
