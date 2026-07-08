import streamlit as st

st.set_page_config(
    page_title="Features",
    page_icon="✨",
    layout="wide"
)

st.title("✨ SentiTube Features")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### 😊 Sentiment Analysis

Analyze YouTube comments into:

- Positive
- Neutral
- Negative
""")

with col2:
    st.success("""
### ❤️ Creator Health Score

AI calculates an overall creator score based on audience sentiment.
""")

with col3:
    st.warning("""
### 📄 Professional PDF

Generate a downloadable report for presentations and analysis.
""")

st.markdown("---")

col4, col5, col6 = st.columns(3)

with col4:
    st.info("""
### 💬 Comment Explorer

Browse all comments by sentiment.
""")

with col5:
    st.success("""
### 🤖 AI Insights

Receive recommendations based on audience reactions.
""")

with col6:
    st.warning("""
### 🌍 Multi-language Ready

Designed to support multiple languages in future updates.
""")