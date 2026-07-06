import streamlit as st
from youtube_api import (
    get_video_id,
    get_comments,
    get_video_details
)
from sentiment import analyze

# ---------------- Page Configuration ---------------- #
st.set_page_config(
    page_title="SentiTube",
    page_icon="🎬",
    layout="wide"
)

# ---------------- Load CSS ---------------- #
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# ---------------- Header ---------------- #
st.title("🎬 SentiTube")
st.subheader("AI Creator Insight Platform")

st.markdown(
    """
### Understand Your Audience with AI

Analyze YouTube comments and generate:

-📊 Creator Health Score -😊 Sentiment Analysis -🤖 AI Insights -📄 Professional PDF Report
"""
)

st.markdown("---")

# ---------------- Input ---------------- #
url = st.text_input(
    "📺 Paste YouTube Video URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

# ---------------- Analyze Button ---------------- #
if st.button("🚀 Analyze Video", use_container_width=True):

    if not url.strip():
        st.warning("Please enter a YouTube URL.")
        st.stop()

    try:
        with st.spinner("🔍 Fetching YouTube comments..."):

            video_id = get_video_id(url)
            details = get_video_details(video_id)
            if details:
                st.image(details["thumbnail"], use_container_width=True)
                st.title(details["title"])
                st.caption(details["channel"])
                c1, c2, c3 = st.columns(3)
                c1.metric("👀 Views", f'{int(details["views"]):,}')
                c2.metric("👍 Likes", f'{int(details["likes"]):,}')
                c3.metric("💬 Comments", f'{int(details["comments"]):,}')
                st.write("📅 Published:", details["published"])
                st.divider()
                comments = get_comments(video_id, max_comments=3000)
                with st.spinner("🤖 Performing AI Sentiment Analysis..."):
                    positive, negative, neutral, score = analyze(comments)
                    st.session_state["comments"] = comments
                    st.session_state["positive"] = positive
                    st.session_state["negative"] = negative
                    st.session_state["neutral"] = neutral
                    st.session_state["score"] = score
                    st.success("✅ Analysis Completed Successfully!")
                    st.info(
                        "Now open **Dashboard**, **Comment Explorer**, **AI Insights**, or **Report** from the sidebar."
                        )
    except Exception as e:
        st.error(f"Error: {e}")
        st.markdown("---")