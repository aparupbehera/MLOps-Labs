"""
Unittest tests for TextAnalyzer class
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from text_analyzer import TextAnalyzer


class TestTextAnalyzer(unittest.TestCase):
    """Test suite for TextAnalyzer using unittest."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.analyzer = TextAnalyzer()
    
    def test_word_count_empty(self):
        """Test word count with empty text."""
        self.analyzer.set_text("")
        self.assertEqual(self.analyzer.word_count(), 0)
    
    def test_word_count_single_word(self):
        """Test word count with single word."""
        self.analyzer.set_text("Hello")
        self.assertEqual(self.analyzer.word_count(), 1)
    
    def test_word_count_multiple_words(self):
        """Test word count with multiple words."""
        self.analyzer.set_text("Hello world from Python")
        self.assertEqual(self.analyzer.word_count(), 4)
    
    def test_character_count_without_spaces(self):
        """Test character count excluding spaces."""
        self.analyzer.set_text("Hello World")
        self.assertEqual(self.analyzer.character_count(include_spaces=False), 10)
    
    def test_character_count_with_spaces(self):
        """Test character count including spaces."""
        self.analyzer.set_text("Hello World")
        self.assertEqual(self.analyzer.character_count(include_spaces=True), 11)
    
    def test_sentence_count_single_sentence(self):
        """Test sentence count with single sentence."""
        self.analyzer.set_text("This is a sentence.")
        self.assertEqual(self.analyzer.sentence_count(), 1)
    
    def test_sentence_count_multiple_sentences(self):
        """Test sentence count with multiple sentences."""
        self.analyzer.set_text("Hello! How are you? I am fine.")
        self.assertEqual(self.analyzer.sentence_count(), 3)
    
    def test_average_word_length(self):
        """Test average word length calculation."""
        self.analyzer.set_text("Hi hello")
        self.assertEqual(self.analyzer.average_word_length(), 3.5)
    
    def test_most_common_words(self):
        """Test finding most common words."""
        self.analyzer.set_text("the cat and the dog and the bird")
        common = self.analyzer.most_common_words(n=2)
        self.assertEqual(common[0], ('the', 3))
        self.assertEqual(common[1], ('and', 2))
    
    def test_unique_word_count(self):
        """Test counting unique words."""
        self.analyzer.set_text("the cat the dog the bird")
        self.assertEqual(self.analyzer.unique_word_count(), 4)
    
    def test_contains_word_case_insensitive(self):
        """Test word search case insensitive."""
        self.analyzer.set_text("Hello World")
        self.assertTrue(self.analyzer.contains_word("hello"))
        self.assertTrue(self.analyzer.contains_word("WORLD"))
        self.assertFalse(self.analyzer.contains_word("python"))
    
    def test_contains_word_case_sensitive(self):
        """Test word search case sensitive."""
        self.analyzer.set_text("Hello World")
        self.assertTrue(self.analyzer.contains_word("Hello", case_sensitive=True))
        self.assertFalse(self.analyzer.contains_word("hello", case_sensitive=True))
    
    def test_set_text(self):
        """Test setting new text."""
        self.analyzer.set_text("Initial text")
        self.assertEqual(self.analyzer.word_count(), 2)
        self.analyzer.set_text("New text here")
        self.assertEqual(self.analyzer.word_count(), 3)
    
    def test_get_statistics(self):
        """Test getting comprehensive statistics."""
        self.analyzer.set_text("Hello world. How are you?")
        stats = self.analyzer.get_statistics()
        self.assertEqual(stats['word_count'], 5)
        self.assertEqual(stats['sentence_count'], 2)
        self.assertIn('unique_words', stats)
    
    def test_initialization_with_text(self):
        """Test initializing analyzer with text."""
        analyzer = TextAnalyzer("Test initialization")
        self.assertEqual(analyzer.word_count(), 2)


class TestTextAnalyzerEdgeCases(unittest.TestCase):
    """Test suite for edge cases."""
    
    def test_empty_string_statistics(self):
        """Test statistics with empty string."""
        analyzer = TextAnalyzer("")
        stats = analyzer.get_statistics()
        self.assertEqual(stats['word_count'], 0)
        self.assertEqual(stats['unique_words'], 0)
    
    def test_special_characters(self):
        """Test text with special characters."""
        analyzer = TextAnalyzer("Hello!!! World??? Test...")
        self.assertGreater(analyzer.word_count(), 0)
    
    def test_numbers_in_text(self):
        """Test text containing numbers."""
        analyzer = TextAnalyzer("I have 5 apples and 10 oranges")
        self.assertEqual(analyzer.word_count(), 7)


if __name__ == '__main__':
    unittest.main()
