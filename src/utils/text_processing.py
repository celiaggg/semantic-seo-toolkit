"""Text processing utilities."""

import re
import string
from typing import List, Dict, Any, Optional
from textstat import flesch_reading_ease, flesch_kincaid_grade
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


class TextProcessor:
    """Text processing utilities for semantic SEO."""
    
    def __init__(self, spacy_model: str = "en_core_web_sm"):
        """Initialize the text processor.
        
        Args:
            spacy_model: spaCy model to use
        """
        try:
            self.nlp = spacy.load(spacy_model)
        except OSError:
            print(f"Warning: {spacy_model} not found. Using basic processing.")
            self.nlp = None
        
        try:
            self.stop_words = set(stopwords.words('english'))
        except LookupError:
            import nltk
            nltk.download('stopwords')
            self.stop_words = set(stopwords.words('english'))
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text.
        
        Args:
            text: Input text
            
        Returns:
            Cleaned text
        """
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove special characters but keep basic punctuation
        text = re.sub(r'[^\w\s.,!?;:-]', '', text)
        
        # Normalize quotes
        text = text.replace('"', '"').replace('"', '"')
        text = text.replace(''', "'").replace(''', "'")
        
        return text.strip()
    
    def extract_sentences(self, text: str) -> List[str]:
        """Extract sentences from text.
        
        Args:
            text: Input text
            
        Returns:
            List of sentences
        """
        if self.nlp:
            doc = self.nlp(text)
            return [sent.text.strip() for sent in doc.sents if sent.text.strip()]
        else:
            return sent_tokenize(text)
    
    def extract_tokens(self, text: str, remove_stopwords: bool = True) -> List[str]:
        """Extract tokens from text.
        
        Args:
            text: Input text
            remove_stopwords: Whether to remove stop words
            
        Returns:
            List of tokens
        """
        if self.nlp:
            doc = self.nlp(text)
            tokens = [token.lemma_.lower() for token in doc if not token.is_space]
        else:
            tokens = word_tokenize(text.lower())
        
        if remove_stopwords:
            tokens = [token for token in tokens if token not in self.stop_words]
        
        return tokens
    
    def calculate_readability(self, text: str) -> Dict[str, float]:
        """Calculate readability metrics.
        
        Args:
            text: Input text
            
        Returns:
            Dictionary of readability metrics
        """
        return {
            "flesch_reading_ease": flesch_reading_ease(text),
            "flesch_kincaid_grade": flesch_kincaid_grade(text),
            "word_count": len(text.split()),
            "sentence_count": len(self.extract_sentences(text)),
            "avg_words_per_sentence": len(text.split()) / len(self.extract_sentences(text))
        }
    
    def extract_phrases(self, text: str, min_length: int = 2, max_length: int = 5) -> List[str]:
        """Extract n-gram phrases from text.
        
        Args:
            text: Input text
            min_length: Minimum phrase length
            max_length: Maximum phrase length
            
        Returns:
            List of phrases
        """
        tokens = self.extract_tokens(text, remove_stopwords=False)
        phrases = []
        
        for n in range(min_length, max_length + 1):
            for i in range(len(tokens) - n + 1):
                phrase = " ".join(tokens[i:i + n])
                phrases.append(phrase)
        
        return phrases
    
    def extract_entities(self, text: str) -> List[Dict[str, Any]]:
        """Extract named entities from text.
        
        Args:
            text: Input text
            
        Returns:
            List of entities with their properties
        """
        if not self.nlp:
            return []
        
        doc = self.nlp(text)
        entities = []
        
        for ent in doc.ents:
            entities.append({
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char,
                "confidence": 1.0  # spaCy doesn't provide confidence by default
            })
        
        return entities