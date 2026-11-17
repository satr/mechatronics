"""Guard the sampled-threshold explanation alongside the estimation code.

Marker parity is not a translation-equivalence proof.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TauSampleObservationParity(unittest.TestCase):
    def test_localized_examples_explain_sampled_not_exact_crossing(self):
        locales = sorted(path.name for path in (ROOT / "docs").iterdir()
                         if path.is_dir())
        self.assertTrue(locales)
        for locale in locales:
            with self.subTest(locale=locale):
                document = (ROOT / "docs" / locale / "notes" /
                            "02-first-order-dynamics.md").read_text(encoding="utf-8")
                before, after = '<a id="section-4"></a>', '<a id="section-5"></a>'
                self.assertEqual(document.count(before), 1)
                self.assertEqual(document.count(after), 1)
                section = document.split(before, 1)[1].split(after, 1)[0]
                for token in ("63.2", "estimate_tau", "None", "resolution",
                              "10 rpm",
                              "../../../exercises/02_first_order_response.py"):
                    self.assertIn(token, section)
                # New example should make explicit that time stamps, rather
                # than a fitted crossing instant, are reported.
                self.assertIn("1 s", section)
                self.assertIn("2 s", section)


if __name__ == "__main__":
    unittest.main()
