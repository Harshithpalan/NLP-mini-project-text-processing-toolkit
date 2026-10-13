"""
Text Analytics & Frequency Engine (analytics.py)
-----------------------------------------------
Computes lexical statistics, Type-Token Ratio (TTR),
term frequency distributions, Hapax Legomena, and noise pruning metrics.
"""

import math
from collections import Counter
from typing import List, Dict, Any, Tuple


class TextAnalytics:
    """Calculates frequency distributions and information-theoretic metrics."""

    @staticmethod
    def calculate_stats(tokens: List[str]) -> Dict[str, Any]:
        """Calculates basic token statistics and Type-Token Ratio."""
        total_tokens = len(tokens)
        if total_tokens == 0:
            return {
                "total_tokens": 0,
                "unique_tokens": 0,
                "ttr": 0.0,
                "entropy": 0.0,
                "hapax_count": 0,
                "hapax_legomena": []
            }

        counts = Counter(tokens)
        unique_tokens = len(counts)
        ttr = round(unique_tokens / total_tokens, 4)

        # Shannon Entropy
        entropy = 0.0
        for count in counts.values():
            p = count / total_tokens
            if p > 0:
                entropy -= p * math.log2(p)
        entropy = round(entropy, 4)

        # Hapax Legomena (terms appearing exactly once)
        hapax = [term for term, count in counts.items() if count == 1]

        return {
            "total_tokens": total_tokens,
            "unique_tokens": unique_tokens,
            "ttr": ttr,
            "entropy": entropy,
            "hapax_count": len(hapax),
            "hapax_legomena": hapax
        }

    @staticmethod
    def get_frequency_distribution(tokens: List[str], top_n: int = 10) -> List[Dict[str, Any]]:
        """Returns the sorted top-N frequency distribution with percentages."""
        if not tokens:
            return []

        total = len(tokens)
        counts = Counter(tokens)
        top_items = counts.most_common(top_n)

        max_count = top_items[0][1] if top_items else 1

        dist = []
        for term, count in top_items:
            pct = round((count / total) * 100, 1)
            bar_width = round((count / max_count) * 100, 1)
            dist.append({
                "term": term,
                "count": count,
                "percentage": pct,
                "relative_bar_pct": bar_width
            })

        return dist

    @staticmethod
    def audit_noise_pruning(raw_text: str, cleaned_tokens: List[str]) -> Dict[str, Any]:
        """Identifies what specific noise items were pruned."""
        import re

        urls = re.findall(r'https?://\S+|www\.\S+', raw_text, flags=re.IGNORECASE)
        punct = re.findall(r'[^\w\s]', raw_text)
        
        raw_words = re.findall(r'\b[a-zA-Z]+\b', raw_text.lower())
        cleaned_set = set(cleaned_tokens)
        stopwords_found = [w for w in raw_words if w not in cleaned_set and len(w) > 1]
        
        return {
            "urls_removed": urls,
            "url_count": len(urls),
            "punctuation_chars": punct,
            "punctuation_count": len(punct),
            "stopwords_detected": list(set(stopwords_found))[:10],
            "stopwords_count": len(stopwords_found)
        }
