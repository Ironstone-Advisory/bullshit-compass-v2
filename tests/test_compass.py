import json
import subprocess
import sys
import unittest
from pathlib import Path
from compass_v2 import BullshitCompass, phrase_matches

ROOT = Path(__file__).resolve().parents[1]


class CalibrationTests(unittest.TestCase):
    def setUp(self):
        self.compass = BullshitCompass()

    def test_expected_bands_and_separation(self):
        samples = json.loads((ROOT / 'calibration/samples.json').read_text())
        scores = {}
        for sample in samples:
            with self.subTest(sample=sample['id']):
                score = self.compass.analyze(sample['text'])['overall_score']
                scores[sample['id']] = score
                low, high = sample['expected_band']
                self.assertGreaterEqual(score, low)
                self.assertLessEqual(score, high)
        self.assertGreater(scores['fog_reported'], scores['plain_deadline'] + .5)

    def test_repeat_length_invariance(self):
        for text in ['We deliver the report on Friday.',
                     'Holistic synergies move the needle.',
                     'Our world-class team will deliver the report on Friday.']:
            expected = self.compass.analyze(text)['overall_score']
            self.assertAlmostEqual(expected, self.compass.analyze((text + ' ') * 100)['overall_score'])

    def test_mixture_is_length_weighted(self):
        plain, fog = 'The report arrives on Friday.', 'Holistic synergies move the needle.'
        a, b = self.compass.analyze(plain), self.compass.analyze(fog)
        result = self.compass.analyze(plain + ' ' + fog)
        expected = (a['overall_score'] * a['word_count'] + b['overall_score'] * b['word_count']) / (a['word_count'] + b['word_count'])
        self.assertAlmostEqual(expected, result['overall_score'], places=5)

    def test_hyphens_spaces_and_case(self):
        scores = [self.compass.analyze(s)['overall_score'] for s in
                  ['VALUE-ADDED next-generation', 'value added next generation', 'Value–added next‑generation']]
        self.assertEqual(scores, [1.0] * 3)

    def test_phrase_boundaries_and_counts(self):
        self.assertEqual(phrase_matches('value. Added', ['value added']), [])
        self.assertEqual(phrase_matches('synergistically', ['synergistic']), [])
        matches = phrase_matches('value-added value-added', ['value', 'value added'])
        self.assertEqual(len(matches), 2)
        self.assertEqual(sum(m['token_count'] for m in matches), 4)

    def test_offsets_preserve_original(self):
        text = 'Our NEXT‑GENERATION work is value-added.'
        for m in self.compass.analyze(text)['indicators']['BLI']['matches']:
            self.assertEqual(text[m['start']:m['end']], m['text'])

    def test_related_sentences_not_tautology(self):
        text = 'The database contains customer records. The database contains invoice records.'
        self.assertEqual(self.compass.analyze(text)['indicators']['TCR']['score'], 0)

    def test_adjacent_repetition_not_all_pairs(self):
        a, b = 'The report arrives on Friday.', 'The invoice arrives on Monday.'
        self.assertEqual(self.compass.analyze(a + ' ' + b + ' ' + a)['indicators']['TCR']['score'], 0)
        result = self.compass.analyze(a + ' ' + a)
        self.assertEqual(result['indicators']['TCR']['score'], 1)
        self.assertEqual(result['overall_score'], 0)

    def test_no_fabricated_semantic_scores(self):
        result = self.compass.analyze('The result may change after further research.')
        for indicator in ['ISI', 'SDS', 'PRM', 'EPF', 'OOI', 'DPO', 'EA', 'DC', 'RR']:
            self.assertIsNone(result['indicators'][indicator]['score'])
            self.assertEqual(result['indicators'][indicator]['status'], 'not_assessed')
        self.assertEqual(result['LGC']['status'], 'manual_context_required')
        self.assertNotIn('clear and substantive', result['interpretation'].lower())

    def test_empty_input_not_clear(self):
        for text in ['', '   ', '...!?']:
            self.assertIsNone(self.compass.analyze(text)['overall_score'])
        with self.assertRaises(TypeError):
            self.compass.analyze(None)

    def test_context_allowlist(self):
        self.assertEqual(BullshitCompass(['value-added']).analyze('Value added')['overall_score'], 0)

    def test_cli_and_legacy_tuple(self):
        text = 'Holistic synergies move the needle.'
        result = subprocess.run([sys.executable, str(ROOT / 'compass_v2.py')], input=text,
                                capture_output=True, text=True, check=True)
        score, analysis = self.compass.calculate_bullshit_index(text)
        self.assertEqual(json.loads(result.stdout), analysis)
        self.assertEqual(score, analysis['overall_score'])


if __name__ == '__main__':
    unittest.main()
