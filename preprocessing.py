"""
NLP Preprocessing Engine (preprocessing.py)
-------------------------------------------
Implements deterministic text sanitization, tokenization,
stopword filtering with smart negation retention, and
morphological transformations (Porter Stemmer and WordNet Lemmatizer).
"""

import sys
import io
import re
from typing import List, Set, Optional

# Ensure UTF-8 output on Windows
if sys.platform.startswith("win"):
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')

import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Auto-download required corpora
for corpus in ['stopwords', 'wordnet', 'omw-1.4']:
    nltk.download(corpus, quiet=True)


class TextPreprocessor:
    """Configurable text preprocessing pipeline."""

    DEFAULT_NEGATIONS = {'not', 'no', 'never', 'neither', 'nor', 'cannot'}

    def __init__(self, custom_stops: Optional[Set[str]] = None, preserve_negations: bool = True):
        self.tokenizer = WordPunctTokenizer()
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.preserve_negations = preserve_negations

        # Base English stopwords
        self.base_stops = set(stopwords.words('english'))
        if self.preserve_negations:
            self.base_stops -= self.DEFAULT_NEGATIONS

        if custom_stops:
            self.stop_words = self.base_stops.union({w.lower() for w in custom_stops})
        else:
            self.stop_words = set(self.base_stops)

    def clean_text(
        self,
        text: str,
        to_lower: bool = True,
        strip_urls: bool = True,
        strip_punct: bool = True,
        strip_symbols: bool = True
    ) -> str:
        """Sanitizes raw text using deterministic regex transformations."""
        if not text or not text.strip():
            return ""

        # 1. Strip URLs first to avoid splitting on punctuation in URLs
        if strip_urls:
            text = re.sub(r'https?://\S+|www\.\S+', ' ', text, flags=re.IGNORECASE)

        # 2. Lowercase if requested
        if to_lower:
            text = text.lower()

        # 3. Strip Symbols & Emojis (@mentions, hashtags, unicode pictographs)
        if strip_symbols:
            text = re.sub(r'[@#]', '', text)
            # Remove emojis and non-alphanumeric unicode symbols
            text = re.sub(
                r'[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]',
                '',
                text
            )

        # 4. Strip Punctuation
        if strip_punct:
            text = re.sub(r'[^\w\s]', ' ', text)

        # Collapse whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def tokenize(self, text: str) -> List[str]:
        """Tokenize string into individual token list."""
        if not text:
            return []
        return [t for t in self.tokenizer.tokenize(text) if t.strip()]

    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """Filter out stopwords while respecting negation preservation."""
        return [t for t in tokens if t.lower() not in self.stop_words]

    def stem_tokens(self, tokens: List[str]) -> List[str]:
        """Apply Porter stemming to token list."""
        return [self.stemmer.stem(t) for t in tokens]

    def lemmatize_tokens(self, tokens: List[str], pos: str = 'n') -> List[str]:
        """Apply WordNet lemmatization to token list."""
        return [self.lemmatizer.lemmatize(t, pos=pos) for t in tokens]

    def process(
        self,
        raw_text: str,
        use_lemmatizer: bool = True,
        remove_stops: bool = True
    ) -> dict:
        """Execute full preprocessing pipeline and return structured audit payload."""
        initial_chars = len(raw_text) if raw_text else 0
        raw_tokens = raw_text.strip().split() if raw_text and raw_text.strip() else []
        initial_tokens_count = len(raw_tokens)

        # Clean
        cleaned_text = self.clean_text(raw_text)
        tokens = self.tokenize(cleaned_text)

        # Filter stopwords
        filtered_tokens = self.remove_stopwords(tokens) if remove_stops else tokens

        # Morphological reduction
        if use_lemmatizer:
            final_tokens = self.lemmatize_tokens(filtered_tokens)
        else:
            final_tokens = self.stem_tokens(filtered_tokens)

        final_text = " ".join(final_tokens)
        final_chars = len(final_text)

        reduction_pct = 0.0
        if initial_chars > 0:
            reduction_pct = round(((initial_chars - final_chars) / initial_chars) * 100, 1)

        dropped_count = max(0, initial_tokens_count - len(final_tokens))
        compression = round(initial_tokens_count / len(final_tokens), 2) if final_tokens else 1.0

        return {
            "raw_input": raw_text,
            "cleaned_text": cleaned_text,
            "final_tokens": final_tokens,
            "final_text": final_text,
            "initial_chars": initial_chars,
            "final_chars": final_chars,
            "initial_tokens": initial_tokens_count,
            "final_tokens_count": len(final_tokens),
            "dropped_tokens": dropped_count,
            "noise_reduction_pct": max(0.0, reduction_pct),
            "compression_ratio": compression,
            "mode": "lemmatization" if use_lemmatizer else "stemming"
        }
