import streamlit as st

st.set_page_config(
    page_title="Comment Explorer",
    page_icon="💬",
    layout="wide"
)

st.title("💬 Comment Explorer")

# Check whether analysis has been done
if "positive" not in st.session_state:
    st.warning("⚠ Please analyze a YouTube video first.")
    st.stop()

positive = st.session_state["positive"]
neutral = st.session_state["neutral"]
negative = st.session_state["negative"]

st.markdown("Browse comments by sentiment.")

search = st.text_input("🔍 Search Comments")

tab1, tab2, tab3 = st.tabs(
[
"😊 Positive",
"😐 Neutral",
"😡 Negative"
]
)

# ---------------- Positive ----------------

with tab1:

    st.subheader(f"Positive Comments ({len(positive)})")

    for comment in positive:

        if search.lower() in comment.lower():

            st.success(comment)

# ---------------- Neutral ----------------

with tab2:

    st.subheader(f"Neutral Comments ({len(neutral)})")

    for comment in neutral:

        if search.lower() in comment.lower():

            st.info(comment)

# ---------------- Negative ----------------

with tab3:

    st.subheader(f"Negative Comments ({len(negative)})")

    for comment in negative:

        if search.lower() in comment.lower():

            st.error(comment)