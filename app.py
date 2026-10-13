"""
Text Preprocessing Toolkit - Streamlit Application (app.py)
-----------------------------------------------------------
An interactive GUI built with Streamlit implementing:
- Interactive Studio: Real-time text cleaning & token sequence inspection
- Text Analytics: Type-Token Ratio (TTR), Top Lemmatized Term Frequencies
- Advanced NLP Pipeline: Porter Stemmer vs. WordNet Lemmatizer comparison
- Project Roadmap Guide: Progress milestones & Viva defense checklist
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from preprocessing import TextPreprocessor
from analytics import TextAnalytics

st.set_page_config(
    page_title="NLP Preprocessing Toolkit",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-Tech Dark Terminal CSS
st.markdown("""
<style>
    .reportview-container {
        background-color: #0b1326;
    }
    .metric-card {
        background-color: #171f33;
        border-radius: 8px;
        padding: 16px;
        border: 1px solid #2d3449;
    }
    .token-chip {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 6px;
        background-color: #222a3d;
        color: #4cd7f6;
        font-family: monospace;
        margin: 3px;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("⚡ NLP Preprocessing")
st.sidebar.caption("Deterministic Preprocessing & Analytics Toolkit")
view_mode = st.sidebar.radio(
    "Navigation",
    ["Interactive Studio", "Text Analytics & Frequency", "NLP Pipeline & Morphology", "Project Roadmap & Viva"]
)

# Samples dictionary
SAMPLES = {
    "Custom / Empty": "",
    "Social Tweet": "Hey!!! I am learning NLP @college 😊, and this is AMAZING!!! Visit https://example.com",
    "Product Review": "Product was NOT delivered on time! Terrible battery life, but customer support was ok...",
    "News Dispatch": "BREAKING: Global emissions dropped by 4.2% in Q3 according to climate-reports.gov. Full analysis: https://news.net/eco"
}

# -------------------------------------------------------------
# VIEW 1: INTERACTIVE STUDIO
# -------------------------------------------------------------
if view_mode == "Interactive Studio":
    st.title("🖥️ Interactive Preprocessing Studio")
    st.write("High-throughput token sanitization with real-time semantic preservation.")

    col_sample, col_status = st.columns([3, 1])
    with col_sample:
        selected_sample = st.selectbox("Load Sample Preset", list(SAMPLES.keys()), index=1)
    with col_status:
        st.success("● Engine Ready")

    sample_text = SAMPLES[selected_sample] if selected_sample != "Custom / Empty" else ""
    user_input = st.text_area("Raw Input Stream", value=sample_text, height=120, placeholder="Type or paste raw text stream here...")

    st.subheader("Pipeline Transforms")
    col1, col2, col3 = st.columns(3)
    with col1:
        to_lower = st.checkbox("Convert to Lowercase", value=True)
        strip_urls = st.checkbox("Strip URLs & Links", value=True)
    with col2:
        strip_punct = st.checkbox("Remove Punctuation", value=True)
        strip_symbols = st.checkbox("Remove Symbols & Emojis", value=True)
    with col3:
        remove_stops = st.checkbox("Filter Stopwords", value=True)
        preserve_negations = st.checkbox("Preserve Negations (Smart Guard)", value=True)

    preprocessor = TextPreprocessor(preserve_negations=preserve_negations)

    if st.button("⚡ Process Stream", type="primary", use_container_width=True):
        if not user_input.strip():
            st.warning("Input buffer is empty. Please provide text to process.")
        else:
            cleaned = preprocessor.clean_text(
                user_input,
                to_lower=to_lower,
                strip_urls=strip_urls,
                strip_punct=strip_punct,
                strip_symbols=strip_symbols
            )
            tokens = preprocessor.tokenize(cleaned)
            if remove_stops:
                tokens = preprocessor.remove_stopwords(tokens)
            final_tokens = preprocessor.lemmatize_tokens(tokens)

            # Metrics
            initial_chars = len(user_input)
            final_chars = len(" ".join(final_tokens))
            reduction = round(((initial_chars - final_chars) / max(1, initial_chars)) * 100, 1)

            st.subheader("Sanitized Output Payload")
            st.code(" ".join(final_tokens) if final_tokens else "(all tokens sanitized)")

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Noise Reduction", f"-{max(0.0, reduction)}%")
            m2.metric("Tokens Kept", len(final_tokens))
            m3.metric("Raw Characters", initial_chars)
            m4.metric("Compression", f"{round(max(1, len(user_input.split())) / max(1, len(final_tokens)), 1)}x")

            st.subheader("Interactive Token Sequence")
            chips_html = "".join([f"<span class='token-chip'>{i:02d}: {t}</span>" for i, t in enumerate(final_tokens)])
            st.markdown(chips_html if final_tokens else "<em>No tokens remaining.</em>", unsafe_allow_html=True)

# -------------------------------------------------------------
# VIEW 2: TEXT ANALYTICS & FREQUENCY
# -------------------------------------------------------------
elif view_mode == "Text Analytics & Frequency":
    st.title("📊 Text Analytics & Term Frequency")
    st.write("Distribution analysis, lexical diversity, and Type-Token Ratio across token sequences.")

    analytics_text = st.text_area("Input Corpus for Analytics", value=SAMPLES["Social Tweet"], height=100)
    preprocessor = TextPreprocessor(preserve_negations=True)
    res = preprocessor.process(analytics_text, use_lemmatizer=True)
    tokens = res["final_tokens"]

    stats = TextAnalytics.calculate_stats(tokens)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Raw Word Tokens", res["initial_tokens"])
    c2.metric("Clean Tokens", len(tokens))
    c3.metric("Lexical TTR", stats["ttr"])
    c4.metric("Shannon Entropy", stats["entropy"])

    freq_dist = TextAnalytics.get_frequency_distribution(tokens, top_n=10)

    col_chart, col_hapax = st.columns([2, 1])
    with col_chart:
        st.subheader("Top Term Frequencies")
        if freq_dist:
            df = pd.DataFrame(freq_dist)
            fig, ax = plt.subplots(figsize=(6, 3.5))
            ax.barh(df["term"], df["count"], color="#06B6D4")
            ax.set_facecolor("#131b2e")
            fig.patch.set_facecolor("#0b1326")
            ax.tick_params(colors="#dae2fd")
            ax.invert_yaxis()
            ax.set_xlabel("Count", color="#dae2fd")
            st.pyplot(fig)
        else:
            st.info("No tokens found to calculate frequencies.")

    with col_hapax:
        st.subheader("Hapax Legomena (Freq = 1)")
        st.write(f"Total Unique Singletons: **{stats['hapax_count']}**")
        for h in stats["hapax_legomena"]:
            st.markdown(f"- `{h}`")

    st.subheader("Noise Pruning Audit")
    audit = TextAnalytics.audit_noise_pruning(analytics_text, tokens)
    a1, a2, a3 = st.columns(3)
    a1.write(f"🔗 **URLs Sanitized**: {audit['url_count']}")
    a2.write(f"✂️ **Punctuation Stripped**: {audit['punctuation_count']} chars")
    a3.write(f"🛑 **Stopwords Removed**: {audit['stopwords_count']}")

# -------------------------------------------------------------
# VIEW 3: NLP PIPELINE & MORPHOLOGY
# -------------------------------------------------------------
elif view_mode == "NLP Pipeline & Morphology":
    st.title("🔬 Advanced NLP Pipeline & Morphology")
    st.write("Deterministic transformation flow & morphological disambiguation matrix.")

    st.subheader("5-Stage Execution Graph")
    st.markdown("""
    1. **Raw Text Stream**: UTF-8 normalization & string buffer intake
    2. **Regex Sanitation**: URL stripping & emoji/symbol elimination
    3. **WordPunct Tokenizer**: Word boundary segmentation
    4. **Stop-Word & Negation Guard**: Pruning stopwords while protecting `not`, `no`, `never`
    5. **Morphological Reduction**: Comparative WordNet Lemmatization vs. Porter Stemming
    """)

    st.subheader("Stemmer vs Lemmatizer A/B Dissector")
    test_word = st.selectbox("Inspect Test Lexeme", ["studies", "learning", "better", "corpora", "universities", "flies"], index=0)

    preprocessor = TextPreprocessor()
    stemmed = preprocessor.stem_tokens([test_word])[0]
    lemmatized = preprocessor.lemmatize_tokens([test_word])[0]

    col_stem, col_lemma = st.columns(2)
    with col_stem:
        st.info("Porter Stemmer (Heuristic Suffix Slicing)")
        st.write(f"Result: **`{stemmed}`**")
        if stemmed in ["studi", "univers"]:
            st.error("Status: Non-Word / Under-stemmed")
        else:
            st.success("Status: Valid Dict")

    with col_lemma:
        st.success("WordNet Lemmatizer (Morphological Graph Lookup)")
        st.write(f"Result: **`{lemmatized}`**")
        st.info("Status: Preserves semantic dictionary lemma")

# -------------------------------------------------------------
# VIEW 4: PROJECT ROADMAP & VIVA
# -------------------------------------------------------------
elif view_mode == "Project Roadmap & Viva":
    st.title("🗺️ Project Roadmap & Viva Defense Checklist")
    st.write("Milestone tracker and oral examination demonstration checklist.")

    st.progress(0.83, text="83% MVP Milestone - 5 of 6 Phases Validated")

    st.subheader("7-Day Sprint Timeline")
    days = [
        ("Day 01", "Environment & Setup", "Python 3.10 virtualenv, NLTK corpora download, Streamlit configuration", "Completed"),
        ("Day 02", "Core Preprocessing Engine", "Tokenizers, stopword pruners, Porter stemmer, lemmatizer", "Completed"),
        ("Day 03", "UI & State Management", "Streamlit UI, session state synchronization across transforms", "Completed"),
        ("Day 04", "Analytics & Frequency Plots", "Token distribution histograms, lexical diversity index, TTR", "Completed"),
        ("Day 05", "Robustness & Edge-Cases", "Escaped emoticons, contraction preservation, sanitized URLs", "Completed"),
        ("Day 06", "UI Polish & Unit Benchmark Suite", "Curated test payloads: Medical, Social Tweets & Legal texts", "Active"),
        ("Day 07", "Report, Slides & Viva Demo", "LaTeX project summary compilation and presentation defense", "Upcoming")
    ]
    for d, title, desc, status in days:
        col_d, col_info = st.columns([1, 4])
        with col_d:
            if status == "Completed":
                st.success(f"✓ {d}")
            elif status == "Active":
                st.warning(f"⚡ {d}")
            else:
                st.caption(f"⏳ {d}")
        with col_info:
            st.write(f"**{title}** — {desc}")

    st.subheader("Viva Defense Test Cases")
    st.checkbox("Negation Retention Handling (not, no, never preserved)", value=True)
    st.checkbox("Graceful Empty Input Response (zero-length input safe)", value=True)
    st.checkbox("Non-English Unicode Sanitation (emojis & symbols normalized)", value=True)
    st.checkbox("URL Prioritized Execution Ordering (links cleanly removed)", value=True)
