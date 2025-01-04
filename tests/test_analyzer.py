import unittest
from src.analyzer import analyze_text

class TestTextAnalyzer(unittest.TestCase):

    def test_word_count(self):
        text = "This is a test."
        result = analyze_text(text)
        self.assertEqual(result['word_count'], 5)

    def test_sentence_count(self):
        text = "This is a test. Here's another sentence."
        result = analyze_text(text)
        self.assertEqual(result['sentence_count'], 2)

    def test_character_count(self):
        text = "Hello!"
        result = analyze_text(text)
        self.assertEqual(result['character_count'], 6)

    def test_most_frequent_word(self):
        text = "apple apple banana"
        result = analyze_text(text)
        self.assertEqual(result['word_frequency']['apple'], 2)

if __name__ == '__main__':
    unittest.main()
