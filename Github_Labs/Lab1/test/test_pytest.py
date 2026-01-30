"""
Pytest tests for TextAnalyzer class
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from text_analyzer import TextAnalyzer


class TestTextAnalyzer:
    """Test suite for TextAnalyzer using pytest."""
    
    def test_word_count_empty(self):
        """Test word count with empty text."""
        analyzer = TextAnalyzer("")
        assert analyzer.word_count() == 0
    
    def test_word_count_single_word(self):
        """Test word count with single word."""
        analyzer = TextAnalyzer("Hello")
        assert analyzer.word_count() == 1
    
    def test_word_count_multiple_words(self):
        """Test word count with multiple words."""
        analyzer = TextAnalyzer("Hello world from Python")
        assert analyzer.word_count() == 4
    
    def test_character_count_without_spaces(self):
        """Test character count excluding spaces."""
        analyzer = TextAnalyzer("Hello World")
        assert analyzer.character_count(include_spaces=False) == 10
    
    def test_character_count_with_spaces(self):
        """Test character count including spaces."""
        analyzer = TextAnalyzer("Hello World")
        assert analyzer.character_count(include_spaces=True) == 11
    
    def test_sentence_count_single_sentence(self):
        """Test sentence count with single sentence."""
        analyzer = TextAnalyzer("This is a sentence.")
        assert analyzer.sentence_count() == 1
    
    def test_sentence_count_multiple_sentences(self):
        """Test sentence count with multiple sentences."""
        analyzer = TextAnalyzer("Hello! How are you? I am fine.")
        assert analyzer.sentence_count() == 3
    
    def test_average_word_length(self):
        """Test average word length calculation."""
        analyzer = TextAnalyzer("Hi hello")
        assert analyzer.average_word_length() == 3.5
    
    def test_most_common_words(self):
        """Test finding most common words."""
        analyzer = TextAnalyzer("the cat and the dog and the bird")
        common = analyzer.most_common_words(n=2)
        assert common[0] == ('the', 3)
        assert common[1] == ('and', 2)
    
    def test_unique_word_count(self):
        """Test counting unique words."""
        analyzer = TextAnalyzer("the cat the dog the bird")
        assert analyzer.unique_word_count() == 4
    
    def test_contains_word_case_insensitive(self):
        """Test word search case insensitive."""
        analyzer = TextAnalyzer("Hello World")
        assert analyzer.contains_word("hello") is True
        assert analyzer.contains_word("WORLD") is True
        assert analyzer.contains_word("python") is False
    
    def test_contains_word_case_sensitive(self):
        """Test word search case sensitive."""
        analyzer = TextAnalyzer("Hello World")
        assert analyzer.contains_word("Hello", case_sensitive=True) is True
        assert analyzer.contains_word("hello", case_sensitive=True) is False
    
    def test_set_text(self):
        """Test setting new text."""
        analyzer = TextAnalyzer("Initial text")
        assert analyzer.word_count() == 2
        analyzer.set_text("New text here")
        assert analyzer.word_count() == 3
    
    def test_get_statistics(self):
        """Test getting comprehensive statistics."""
        analyzer = TextAnalyzer("Hello world. How are you?")
        stats = analyzer.get_statistics()
        assert stats['word_count'] == 5
        assert stats['sentence_count'] == 2
        assert 'unique_words' in stats


@pytest.fixture
def sample_analyzer():
    """Fixture providing a sample TextAnalyzer instance."""
    return TextAnalyzer("The quick brown fox jumps over the lazy dog.")


def test_fixture_word_count(sample_analyzer):
    """Test using pytest fixture."""
    assert sample_analyzer.word_count() == 9
