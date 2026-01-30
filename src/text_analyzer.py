"""
Text Analyzer Module
Provides functionality to analyze text data including word counts, frequency analysis, and basic statistics.
"""

from collections import Counter
import re


class TextAnalyzer:
    """A class to analyze text content."""
    
    def __init__(self, text: str = ""):
        """
        Initialize the TextAnalyzer with text.
        
        Args:
            text (str): The text to analyze
        """
        self.text = text
    
    def set_text(self, text: str) -> None:
        """Set new text for analysis."""
        self.text = text
    
    def word_count(self) -> int:
        """
        Count the total number of words in the text.
        
        Returns:
            int: Number of words
        """
        if not self.text:
            return 0
        words = self.text.split()
        return len(words)
    
    def character_count(self, include_spaces: bool = False) -> int:
        """
        Count the total number of characters.
        
        Args:
            include_spaces (bool): Whether to include spaces in the count
            
        Returns:
            int: Number of characters
        """
        if include_spaces:
            return len(self.text)
        return len(self.text.replace(" ", ""))
    
    def sentence_count(self) -> int:
        """
        Count the number of sentences in the text.
        
        Returns:
            int: Number of sentences
        """
        if not self.text:
            return 0
        sentences = re.split(r'[.!?]+', self.text)
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
    
    def average_word_length(self) -> float:
        """
        Calculate the average length of words.
        
        Returns:
            float: Average word length
        """
        if not self.text:
            return 0.0
        words = self.text.split()
        if not words:
            return 0.0
        total_length = sum(len(word) for word in words)
        return round(total_length / len(words), 2)
    
    def most_common_words(self, n: int = 5) -> list:
        """
        Find the most common words in the text.
        
        Args:
            n (int): Number of top words to return
            
        Returns:
            list: List of tuples (word, count)
        """
        if not self.text:
            return []
        
        words = re.findall(r'\b\w+\b', self.text.lower())
        word_counts = Counter(words)
        return word_counts.most_common(n)
    
    def unique_word_count(self) -> int:
        """
        Count the number of unique words.
        
        Returns:
            int: Number of unique words
        """
        if not self.text:
            return 0
        words = re.findall(r'\b\w+\b', self.text.lower())
        return len(set(words))
    
    def contains_word(self, word: str, case_sensitive: bool = False) -> bool:
        """
        Check if the text contains a specific word.
        
        Args:
            word (str): The word to search for
            case_sensitive (bool): Whether the search should be case-sensitive
            
        Returns:
            bool: True if word is found, False otherwise
        """
        text = self.text if case_sensitive else self.text.lower()
        search_word = word if case_sensitive else word.lower()
        return search_word in text
    
    def get_statistics(self) -> dict:
        """
        Get comprehensive statistics about the text.
        
        Returns:
            dict: Dictionary containing various text statistics
        """
        return {
            'word_count': self.word_count(),
            'character_count': self.character_count(include_spaces=False),
            'character_count_with_spaces': self.character_count(include_spaces=True),
            'sentence_count': self.sentence_count(),
            'average_word_length': self.average_word_length(),
            'unique_words': self.unique_word_count()
        }
