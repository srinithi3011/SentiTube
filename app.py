import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
from reportlab.pdfgen import canvas
analyzer = SentimentIntensityAnalyzer()

st.set_page_config(
    page_title="SentiTube",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)
with st.sidebar:

    st.image("https://img.icons8.com/color/96/youtube-play.png", width=80)

    st.subheader("🎬 SentiTube")

    st.caption("AI Creator Insight Platform")
    
    st.success("AI Powered")

    st.caption("Version 2.0")
    menu = st.radio("Main Menu",
        [
            "🏠 Home",
            "📊 Dashboard",
            "💬 Comment Explorer",
            "🤖 AI Insights",
            "📄 Report"
        ]
    )

    st.markdown("---")
# Replace with your API key
API_KEY = "AIzaSyCpOtP04dubgsECqScijTIaxor76xO1ZY8"

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

def get_video_id(url):
    parsed = urlparse(url)
    return parse_qs(parsed.query).get("v", [""])[0]

def get_comments(video_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )

    response = request.execute()

    comments = []

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    return comments

def analyze(comments):
    positive = []
    negative = []
    neutral = []

    for comment in comments:
        score = analyzer.polarity_scores(comment)
        compound = score["compound"]

        if compound >= 0.05:
            positive.append(comment)
        elif compound <= -0.05:
            negative.append(comment)
        else:
            neutral.append(comment)

    p = len(positive)
    n = len(negative)
    ne = len(neutral)

    total = p + n + ne

    if total == 0:
        creator_score = 0
    else:
        creator_score = round((p / total) * 100, 2)

    return positive, negative, neutral, creator_score

def generate_pdf(score, p, n, ne, total):
    pdf = canvas.Canvas("SentiTube_Report.pdf")

    pdf.setTitle("SentiTube Report")

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(150, 800, "SentiTube Analysis Report")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 750, f"Total Comments: {total}")
    pdf.drawString(100, 720, f"Positive Comments: {p}")
    pdf.drawString(100, 690, f"Negative Comments: {n}")
    pdf.drawString(100, 660, f"Neutral Comments: {ne}")
    pdf.drawString(100, 630, f"Creator Health Score: {score}/100")

    if score >= 70:
        conclusion = "Audience reaction is mostly positive."
    elif score >= 40:
        conclusion = "Audience reaction is mixed."
    else:
        conclusion = "Audience reaction is mostly negative."

    pdf.drawString(100, 580, "Conclusion:")
    pdf.drawString(100, 550, conclusion)

    pdf.save()


# ---------------- UI ----------------
if menu == "🏠 Home":

    st.title("🎬 SentiTube")

    st.markdown(
    """
# AI Powered YouTube Analytics

Analyze thousands of YouTube comments using Artificial Intelligence.

### Features

✅ Sentiment Analysis

✅ Creator Health Score

✅ AI Insights

✅ Professional Reports

✅ Comment Explorer

---

Paste a YouTube URL below.
"""
    )

    url = st.text_input("📺 YouTube URL")

    analyze = st.button("🚀 Analyze Video")

if analyze:

    video_id = get_video_id(url)

    if video_id == "":
        st.error("Invalid YouTube URL")

    else:
        comments = get_comments(video_id)

        positive_comments, negative_comments, neutral_comments, score = analyze(comments)

        p = len(positive_comments)
        n = len(negative_comments)
        ne = len(neutral_comments)

        total = p + n + ne

        # Comments Table
        df = pd.DataFrame(comments, columns=["Comments"])

        st.subheader("📋 Retrieved Comments")
        st.dataframe(df)
        st.session_state["positive"] = positive_comments
        st.session_state["negative"] = negative_comments
        st.session_state["neutral"] = neutral_comments
                # ---------------- RESULTS ----------------
        st.subheader("📊 Creator Dashboard")
        st.progress(int(score))
        c1,c2,c3,c4=st.columns(4)
        c1.metric("😊 Positive",p)
        c2.metric("😐 Neutral",ne)
        c3.metric("😡 Negative",n)
        c4.metric("❤️ Health Score",f"{score}%")
        st.divider()

        st.markdown("---")

        # Pie Chart
        labels = ["Positive", "Negative", "Neutral"]
        sizes = [p, n, ne]

        fig, ax = plt.subplots(figsize=(5, 5))
        ax.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )
        ax.axis("equal")

        # Bar Chart
        chart_data = pd.DataFrame({
            "Sentiment": ["Positive", "Negative", "Neutral"],
            "Count": [p, n, ne]
        })

        # Display charts side by side
        col1,col2=st.columns([2,2])

with col1:

    st.subheader("🥧 Sentiment Distribution")

    st.pyplot(fig)

with col2:

    st.subheader("📊 Analytics")

    st.bar_chart(chart_data.set_index("Sentiment"))
with left:
            st.subheader("🥧 Sentiment Distribution")
            st.pyplot(fig)

with right:
            st.subheader("📊 Sentiment Count")
            st.bar_chart(chart_data.set_index("Sentiment"))
            st.markdown("---")
            total = p + n + ne
            st.write(f"**Total Comments Analysed:** {total}")
            st.write(f"**Creator Health Score:** {score}/100")
            generate_pdf(score, p, n, ne, total)
            st.success("✅ PDF Report Generated Successfully!")

with open("SentiTube_Report.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_file,
                file_name="SentiTube_Report.pdf",
                mime="application/pdf"
            )
          