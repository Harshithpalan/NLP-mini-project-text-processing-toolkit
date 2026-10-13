"""
Text Preprocessing Pipeline
Demonstrating regex sanitization, tokenization, stopword removal with negation preservation,
and stemming vs. lemmatization.
"""

import sys
import io
import re

# Ensure standard output supports UTF-8 on Windows
if sys.platform.startswith("win"):
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')

import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Step 0: Ensure corpora resources
print("Downloading required NLTK corpora...")
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
print("Corpora ready.")

class NLPPipeline:
    def __init__(self, custom_stops=None):
        self.tokenizer = WordPunctTokenizer()
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        
        # Preserve context negations for sentiment analysis integrity
        negations = {'not', 'nor', 'neither', 'never', 'no'}
        base_stops = set(stopwords.words('english')) - negations
        if custom_stops:
            base_stops.update(custom_stops)
        self.stop_words = base_stops

    def clean_regex(self, text: str) -> str:
        # 1. Remove URLs (http, https, www)
        text = re.sub(r'https?://\S+|www\.\S+', ' ', text)
        # 2. Keep only alphabetic characters and whitespace (strips emojis, punctuation, symbols)
        text = re.sub(r'[^a-zA-Z\s]', ' ', text)
        # 3. Collapse multiple spaces and convert to lowercase
        text = re.sub(r'\s+', ' ', text)
        return text.lower().strip()

    def process(self, raw_text: str, use_lemmatizer: bool = True):
        clean = self.clean_regex(raw_text)
        tokens = self.tokenizer.tokenize(clean)
        filtered = [t for t in tokens if t not in self.stop_words]
        
        if use_lemmatizer:
            return [self.lemmatizer.lemmatize(t) for t in filtered]
        return [self.stemmer.stem(t) for t in filtered]

if __name__ == "__main__":
    pipeline = NLPPipeline(custom_stops=['exam', 'semester', 'college'])
    
    samples = {
        "Social Tweet": "Hey!!! I am learning NLP @college 😊, and this is AMAZING!!! Visit https://example.com",
        "Product Review": "Product was NOT delivered on time! Terrible battery life, but customer support was ok...",
        "News Dispatch": "BREAKING: Global emissions dropped by 4.2% in Q3 according to climate-reports.gov. Full analysis: https://news.net/eco"
    }

    print("=" * 60)
    print("TEXT PREPROCESSING PIPELINE EXECUTION")
    print("=" * 60)

    for name, text in samples.items():
        print(f"\n[Test Case: {name}]")
        print(f"Raw Input:  {text}")
        clean_text = pipeline.clean_regex(text)
        print(f"Cleaned:    {clean_text}")
        lemmas = pipeline.process(text, use_lemmatizer=True)
        stems = pipeline.process(text, use_lemmatizer=False)
        print(f"Lemmatized: {lemmas}")
        print(f"Stemmed:    {stems}")
    
    print("\n" + "=" * 60)
    print("PIPELINE TEST COMPLETED SUCCESSFULLY")
    print("=" * 60)
