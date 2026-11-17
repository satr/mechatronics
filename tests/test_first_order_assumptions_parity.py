"""Maintain visible, model-specific accuracy assumptions in each translation."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = tuple(sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir()))

# Distinct translated phrases for the central assumptions in the canonical lesson.
MODEL_TERMS = {
    "en": ("ideal proportional torque control", "load", "friction",
           "delays", "voltage limits", "saturation", "higher-order dynamics"),
    "ru": ("пропорциональное управление крутящим моментом", "нагрузки", "трения",
           "задержек", "ограничений напряжения", "насыщения", "более высокого порядка"),
    "de": ("proportionale Drehmomentregelung", "Last", "Reibung",
           "Verzögerungen", "Spannungsgrenzen", "Sättigung", "höherer Ordnung"),
    "fr": ("commande proportionnelle idéale du couple", "charge", "frottement",
           "retard", "limite de tension", "saturation", "ordre supérieur"),
    "it": ("controllo proporzionale ideale della coppia", "carico", "attrito",
           "ritardi", "limiti di tensione", "saturazione", "ordine superiore"),
    "es": ("control proporcional ideal del par", "carga", "fricción",
           "retardos", "límites de tensión", "saturación", "orden superior"),
    "pt": ("controlo proporcional ideal do binário", "carga", "atrito",
           "atrasos", "limites de tensão", "saturação", "ordem superior"),
    "zh": ("理想比例转矩控制", "负载", "摩擦",
           "延迟", "电压限制", "饱和", "更高阶"),
    "ja": ("理想的な比例トルク制御", "負荷", "摩擦",
           "遅延", "電圧制限", "飽和", "高次"),
    "nb": ("proporsjonal momentregulering", "last", "friksjon",
           "forsinkelser", "spenningsgrenser", "metning", "høyere orden"),
    "ko": ("이상적인 비례 토크 제어", "부하", "마찰",
           "지연", "전압 제한", "포화", "고차 동역학"),
    "fi": ("ideaalisen verrannollisen momenttiohjauksen", "kuormaa", "kitkaa",
           "viiveitä", "jänniterajoja", "kyllästymistä",
           "korkeamman kertaluvun dynamiikkaa"),
    "pl": ("idealny moment proporcjonalny do błędu prędkości", "obciążenia", "tarcie",
           "opóźnienia", "ograniczenia napięcia", "nasycenie",
           "dynamikę wyższych rzędów"),
}


class FirstOrderAssumptionParity(unittest.TestCase):
    def test_model_specific_assumptions_appear_before_first_lesson(self):
        self.assertEqual(set(LOCALES), set(MODEL_TERMS))
        for locale in LOCALES:
            with self.subTest(locale=locale):
                text = (ROOT / "docs" / locale / "notes" /
                        "02-first-order-dynamics.md").read_text(encoding="utf-8")
                front = text.split('<a id="section-1"></a>', 1)[0]
                self.assertIn("> ", front)
                for phrase in MODEL_TERMS[locale]:
                    self.assertIn(phrase, front)
                # A translation must not silently rely on the English wording.
                if locale != "en":
                    self.assertNotIn(
                        "The motor model below assumes ideal proportional", front
                    )


if __name__ == "__main__":
    unittest.main()
