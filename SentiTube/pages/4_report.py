import streamlit as st
from collections import Counter
import re
from pdf_generator import create_pdf

st.set_page_config(
    page_title="AI Creator Report",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Creator Report")

if "score" not in st.session_state:
    st.warning("Please analyze a video first.")
    st.stop()

# ===========================
# Get Data
# ===========================

details = st.session_state["video_details"]

positive = st.session_state["positive"]
neutral = st.session_state["neutral"]
negative = st.session_state["negative"]

score = st.session_state["score"]

p = len(positive)
ne = len(neutral)
n = len(negative)

total = p + ne + n

# ===========================
# Preview
# ===========================

st.subheader("❤️ Creator Health Score")

st.metric(
    "Overall Score",
    f"{score}%"
)

st.divider()

st.subheader("📊 Sentiment Summary")

c1, c2, c3 = st.columns(3)

c1.metric("😊 Positive", p)
c2.metric("😐 Neutral", ne)
c3.metric("😡 Negative", n)

st.divider()

# ===========================
# AI Summary
# ===========================

if score >= 90:

    summary = (
        "The audience response is outstanding. "
        "Most viewers appreciated the explanation, presentation "
        "and overall content quality."
    )

elif score >= 75:

    summary = (
        "Audience response is highly positive. "
        "Minor improvements can further increase engagement."
    )

elif score >= 60:

    summary = (
        "Overall audience response is good. "
        "Review viewer suggestions for future improvements."
    )

else:

    summary = (
        "Audience response indicates improvements are needed "
        "to increase viewer satisfaction."
    )

st.subheader("🤖 AI Summary")

st.info(summary)

st.divider()

# ===========================
# Recommendations
# ===========================

recommendations = []

if score >= 80:

    recommendations = [

        "Continue producing similar content.",

        "Maintain upload consistency.",

        "Reply to audience comments.",

        "Keep engaging with viewers."

    ]

elif score >= 60:

    recommendations = [

        "Improve thumbnails.",

        "Increase audience interaction.",

        "Improve audio quality.",

        "Review viewer feedback."

    ]

else:

    recommendations = [

        "Improve video quality.",

        "Enhance presentation style.",

        "Address repeated negative feedback.",

        "Focus on audience interests."

    ]

st.subheader("💡 AI Recommendations")

for rec in recommendations:
    st.write(f"✅ {rec}")

st.divider()

# ===========================
# Top Keywords
# ===========================

comments = positive + neutral + negative

text = " ".join(comments).lower()

words = re.findall(r"\b[a-zA-Z]{4,}\b", text)

stop_words = {
    "this","that","with","have","your",
    "from","video","really","very",
    "just","good","great","nice",
    "love","make","made","also"
}

filtered = [

    w

    for w in words

    if w not in stop_words

]

keywords = [

    word

    for word, count in Counter(filtered).most_common(5)

]

st.subheader("🔥 Top Audience Topics")

st.write(" • ".join(keywords))

st.divider()

# ===========================
# Generate PDF
# ===========================

if st.button("📄 Generate Professional Report"):

    create_pdf(

        "SentiTube_Report.pdf",

        details,

        score,

        positive,

        neutral,

        negative,

        keywords,

        summary,

        recommendations

    )

    st.success("✅ Professional Report Generated!")

    with open("SentiTube_Report.pdf", "rb") as pdf:

        st.download_button(

            "⬇ Download PDF Report",

            pdf,

            file_name="SentiTube_Report.pdf",

            mime="application/pdf"

        )