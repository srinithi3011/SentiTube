import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="Comment Explorer",
    page_icon="💬",
    layout="wide"
)

try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

st.title("💬 AI Comment Explorer")

if "positive" not in st.session_state:
    st.warning("Please analyze a video first.")
    st.stop()

positive = st.session_state["positive"]
neutral = st.session_state["neutral"]
negative = st.session_state["negative"]

search = st.text_input(
    "🔍 Search Comments",
    placeholder="Type any keyword..."
)

tab1, tab2, tab3 = st.tabs(
    [
        "🟢 Positive",
        "🟡 Neutral",
        "🔴 Negative"
    ]
)

PAGE_SIZE = 15


def show_comments(comments, sentiment):

    if search:
        comments = [
            c for c in comments
            if search.lower() in c.lower()
        ]

    st.write(f"### {len(comments)} Comments")

    if not comments:
        st.info("No comments found.")
        return

    total_pages = max(1, (len(comments)-1)//PAGE_SIZE+1)

    page = st.number_input(
        "Page",
        1,
        total_pages,
        1,
        key=sentiment
    )

    start = (page-1)*PAGE_SIZE
    end = start+PAGE_SIZE

    current = comments[start:end]

    badge = {
        "Positive":"badge-positive",
        "Neutral":"badge-neutral",
        "Negative":"badge-negative"
    }

    emoji = {
        "Positive":"🟢 Positive",
        "Neutral":"🟡 Neutral",
        "Negative":"🔴 Negative"
    }

    names = [
        "Anonymous Viewer",
        "YouTube User",
        "Creator Fan",
        "Subscriber",
        "Viewer"
    ]

    for comment in current:

        name = random.choice(names)

        st.markdown(
            f"""
<div class="comment-card">

<div class="comment-header">

<div class="avatar">👤</div>

<div>

<div class="username">{name}</div>

<div class="time">Recently</div>

</div>

</div>

<div class="comment-text">

{comment}

</div>

<div class="comment-footer">

<span class="sentiment-badge {badge[sentiment]}">

{emoji[sentiment]}

</span>

</div>

</div>
""",
            unsafe_allow_html=True
        )

    df = pd.DataFrame(comments, columns=["Comment"])

    st.download_button(
        "📥 Download Comments",
        df.to_csv(index=False),
        file_name=f"{sentiment.lower()}_comments.csv",
        mime="text/csv",
        use_container_width=True
    )


with tab1:
    show_comments(positive, "Positive")

with tab2:
    show_comments(neutral, "Neutral")

with tab3:
    show_comments(negative, "Negative")