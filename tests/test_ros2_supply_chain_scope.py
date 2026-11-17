"""Guard truthful Docker supply-chain claims without pulling or executing images."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Ros2DockerSupplyChainScope(unittest.TestCase):
    def test_mutable_base_and_apt_inputs_are_not_called_reproducible(self):
        dockerfile = (ROOT / "ros2" / "Dockerfile").read_text(encoding="utf-8")
        guide = (ROOT / "ros2" / "README.md").read_text(encoding="utf-8")
        self.assertIn("FROM ros:jazzy-ros-base", dockerfile)
        self.assertIn("apt-get update && apt-get install", dockerfile)
        self.assertIn("base image tag and apt package indexes are mutable",
                      dockerfile.lower())
        self.assertIn("Pinning a verified image digest freezes only", guide)
        self.assertIn("insufficient for byte-for-byte reproducibility", guide)
        self.assertNotIn(
            "for byte-for-byte reproducibility, replace the tag", guide
        )
        self.assertIn(
            "https://docs.docker.com/build/building/best-practices/", guide
        )

    def test_security_docs_do_not_treat_docker_as_a_trust_boundary(self):
        guide = (ROOT / "ros2" / "README.md").read_text(encoding="utf-8")
        security = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
        self.assertIn("Review the Dockerfile and Compose file before building", guide)
        self.assertIn("Docker is not a malware sandbox", guide)
        self.assertIn("https://docs.docker.com/engine/security/", guide)
        self.assertIn("Pinning a base-image digest alone is insufficient",
                      security)
        self.assertIn("https://docs.docker.com/engine/security/", security)
        self.assertIn("independent", security.lower())


if __name__ == "__main__":
    unittest.main()
