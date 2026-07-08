import streamlit as st
from youtube_api import (
    get_video_id,
    get_comments,
    get_video_details
)
from sentiment import analyze
from spam_detector import is_spam

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
st.markdown("""
<div class="hero">

<h1>🎬 SentiTube</h1>

<p>
AI Powered Creator Intelligence Platform
</p>
<p>
Analyze thousands of YouTube comments.
</p>

</div>
""", unsafe_allow_html=True)

# Initialize URL only once
if "video_url" not in st.session_state:
    st.session_state.video_url = ""

url = st.text_input(
    "📺 Paste YouTube Video URL",
    value=st.session_state.video_url,
    placeholder="https://www.youtube.com/watch?v=..."
)

# Save URL whenever it changes
st.session_state.video_url = url

if st.button("🚀 Analyze Video", use_container_width=True):
    st.markdown("<br>", unsafe_allow_html=True)

    if not url.strip():
        st.warning("Please enter a YouTube URL.")
        st.stop()

    try:
        with st.spinner("🔍 Fetching YouTube comments..."):

            video_id = get_video_id(url)
            st.session_state["video_url"] = url
            details = get_video_details(video_id)
            st.session_state["video_details"] = details
            if details:
                 left, right = st.columns([1, 2])
                 with left:
                      st.image(details["thumbnail"], use_container_width=True)
                      with right:
                           st.markdown(f"""## {details["title"]}
                                       📺 Channel: {details["channel"]}
                                       📅 Published: {details["published"]}
    """)
                           c1, c2, c3 = st.columns(3)
                           c1.metric(
                                "👀 Views",
                                f'{int(details["views"]):,}'
                                )
                           c2.metric(
                                "👍 Likes",
                                f'{int(details["likes"]):,}')
                           c3.metric(
                                "💬 Comments",
                                f'{int(details["comments"]):,}'
                                )
                           st.divider()
                           comments = get_comments(video_id, max_comments=3000)
                           spam = []
                           clean = []
                           for comment in comments:
                                if is_spam(comment):
                                      spam.append(comment)
                                else:
                                      clean.append(comment)
                                      comments = clean
                                      st.session_state["spam"] = spam
                           with st.spinner("🤖 Performing AI Sentiment Analysis..."):
                               positive, negative, neutral, score = analyze(comments)
                               st.session_state["comments"] = comments
                               st.session_state["positive"] = positive
                               st.session_state["negative"] = negative
                               st.session_state["neutral"] = neutral
                               st.session_state["score"] = score
                               st.success("✅ Analysis Completed Successfully!")
                               st.session_state["video_details"] = details
                               st.session_state["video_url"] = url
                               st.info(
                        "Now open **Dashboard**, **Comment Explorer**, **AI Insights**, or **Report** from the sidebar."
                        )
    except Exception as e:
        st.error(f"Error: {e}")
        st.markdown("---")
        st.markdown("<br><br>", unsafe_allow_html=True)

col1,col2,col3,col4=st.columns(4)

with col1:

    st.markdown("""
<div class="card">
<h2>3000+</h2>
<p>Comments</p>
</div>
""",unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="card">
<h2>😊</h2>
<p>Sentiment</p>
</div>
""",unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="card">
<h2>🤖</h2>
<p>AI Insights</p>
</div>
""",unsafe_allow_html=True)

with col4:

    st.markdown("""
<div class="card">
<h2>📄</h2>
<p>Professional Report</p>
</div>
""",unsafe_allow_html=True)
