"""
Unit Benchmark Suite (run_pipeline_tests.py)
--------------------------------------------
Validates all requirements and viva checklist test cases:
1. Negation Retention Handling (not, no, never preserved)
2. Graceful Empty Input Handling (zero length doesn't crash)
3. Non-English Unicode / Emoji Sanitation
4. URL Prioritized Execution Ordering
5. WordNet Lemmatization vs Porter Stemming
6. Analytics TTR & Frequency Distribution
"""

import sys
import io
import unittest

if sys.platform.startswith("win"):
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from preprocessing import TextPreprocessor
from analytics import TextAnalytics


class TestNLPPreprocessingToolkit(unittest.TestCase):

    def setUp(self):
        self.preprocessor = TextPreprocessor(preserve_negations=True)

    def test_01_negation_retention(self):
        """Test Case 1: Preserving 'not', 'never', 'neither' for sentiment integrity."""
        raw = "The product is NOT good and was NEVER delivered."
        result = self.preprocessor.process(raw, use_lemmatizer=True)
        tokens = result["final_tokens"]
        self.assertIn("not", tokens)
        self.assertIn("never", tokens)
        print("✓ Test 1 Passed: Negations correctly preserved.")

    def test_02_empty_input_resilience(self):
        """Test Case 2: Gracefully handles empty string and whitespace."""
        for empty_val in ["", "   ", "\n\t"]:
            result = self.preprocessor.process(empty_val)
            self.assertEqual(result["final_tokens_count"], 0)
            self.assertEqual(result["cleaned_text"], "")
        print("✓ Test 2 Passed: Empty input handled safely without exceptions.")

    def test_03_unicode_and_emoji_sanitation(self):
        """Test Case 3: Emojis and special unicode symbols stripped cleanly."""
        raw = "Awesome project! 😊🚀 Testing Unicode #NLP @college"
        clean = self.preprocessor.clean_text(raw)
        self.assertNotIn("😊", clean)
        self.assertNotIn("🚀", clean)
        self.assertNotIn("@", clean)
        self.assertNotIn("#", clean)
        print("✓ Test 3 Passed: Emojis and unicode symbols sanitized.")

    def test_04_url_stripping_prioritized(self):
        """Test Case 4: Complete HTTP/HTTPS links removed before punctuation split."""
        raw = "Inspect results at https://example.com/dataset?id=492&ref=test today."
        clean = self.preprocessor.clean_text(raw)
        self.assertNotIn("http", clean)
        self.assertNotIn("example", clean)
        self.assertIn("inspect results at", clean)
        self.assertIn("today", clean)
        print("✓ Test 4 Passed: URLs stripped accurately without fragment remnants.")

    def test_05_lemmatization_vs_stemming(self):
        """Test Case 5: WordNet Lemmatizer yields valid dictionary words compared to Porter cuts."""
        # e.g., 'studies' -> 'study' (lemma) vs 'studi' (stem)
        lemma_res = self.preprocessor.process("The studies proved effective", use_lemmatizer=True)
        stem_res = self.preprocessor.process("The studies proved effective", use_lemmatizer=False)
        self.assertIn("study", lemma_res["final_tokens"])
        self.assertIn("studi", stem_res["final_tokens"])
        print("✓ Test 5 Passed: Lemmatization preserves dictionary root 'study'; Stemmer produces 'studi'.")

    def test_06_analytics_metrics(self):
        """Test Case 6: Lexical TTR and term frequency calculations."""
        tokens = ["nlp", "machine", "learning", "nlp", "models"]
        stats = TextAnalytics.calculate_stats(tokens)
        self.assertEqual(stats["total_tokens"], 5)
        self.assertEqual(stats["unique_tokens"], 4)
        self.assertEqual(stats["ttr"], 0.8)
        self.assertIn("models", stats["hapax_legomena"])

        dist = TextAnalytics.get_frequency_distribution(tokens)
        self.assertEqual(dist[0]["term"], "nlp")
        self.assertEqual(dist[0]["count"], 2)
        print("✓ Test 6 Passed: Analytics TTR and Frequency correctly computed.")


if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING NLP PREPROCESSING TOOLKIT UNIT BENCHMARKS")
    print("=" * 60)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNLPPreprocessingToolkit)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("\nALL 6 BENCHMARK TESTS PASSED (100% SUCCESS RATE)")
    else:
        sys.exit(1)
