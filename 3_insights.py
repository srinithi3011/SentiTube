import streamlit as st
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from ai_summary import generate_summary
from emotion import detect_emotion

st.set_page_config(
    page_title="AI Insights",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Load CSS ---------------- #

try:
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except FileNotFoundError:
    pass


# ---------------- Title ---------------- #

st.title("🤖 AI Insights")
st.caption("Advanced Artificial Intelligence Analysis of Audience Behaviour")


# ---------------- Check Session ---------------- #

if "positive" not in st.session_state:
    st.warning("Please analyze a YouTube video first.")
    st.stop()


# ---------------- Get Data ---------------- #

positive = st.session_state["positive"]
neutral = st.session_state["neutral"]
negative = st.session_state["negative"]
score = st.session_state["score"]

p = len(positive)
ne = len(neutral)
n = len(negative)

total = p + ne + n


# ---------------- Audience Mood ---------------- #

st.header("🎯 Audience Mood")

if score >= 90:

    st.success(
        "😍 Outstanding Audience Response\n\n"
        "Your viewers loved the content. "
        "This video has an excellent overall sentiment."
    )

elif score >= 75:

    st.info(
        "😊 Mostly Positive Audience\n\n"
        "Most viewers enjoyed the video with only a few negative opinions."
    )

elif score >= 50:

    st.warning(
        "😐 Mixed Audience Opinion\n\n"
        "Some viewers liked the content while others suggested improvements."
    )

else:

    st.error(
        "😡 Negative Audience Response\n\n"
        "Many viewers were dissatisfied. Review feedback carefully."
    )


st.divider()


# ---------------- Statistics ---------------- #

st.header("📊 Audience Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "😊 Positive",
        p
    )

with c2:
    st.metric(
        "😐 Neutral",
        ne
    )

with c3:
    st.metric(
        "😡 Negative",
        n
    )

with c4:
    st.metric(
        "❤️ Creator Health",
        f"{score}%"
    )


# ---------------- Extra Metrics ---------------- #

st.subheader("📈 Sentiment Distribution")

col1, col2, col3 = st.columns(3)

positive_percent = round((p / total) * 100, 1) if total else 0
neutral_percent = round((ne / total) * 100, 1) if total else 0
negative_percent = round((n / total) * 100, 1) if total else 0

with col1:
    st.progress(positive_percent / 100)
    st.caption(f"Positive : {positive_percent}%")

with col2:
    st.progress(neutral_percent / 100)
    st.caption(f"Neutral : {neutral_percent}%")

with col3:
    st.progress(negative_percent / 100)
    st.caption(f"Negative : {negative_percent}%")

st.divider()
# ======================================================
# 🤖 AI Topic Analysis
# ======================================================

st.header("🤖 AI Topic Analysis")

all_comments = positive + neutral + negative

text = " ".join(all_comments).lower()

words = re.findall(r"\b[a-zA-Z]{4,}\b", text)

stop_words = {
    "this","that","with","have","your","from",
    "they","were","been","there","their",
    "would","could","should","video","videos",
    "really","very","just","what","when",
    "where","which","will","good","great",
    "nice","awesome","love","make","made",
    "also","much","more","like","thank",
    "thanks","best","youtube"
}

filtered = [
    w for w in words
    if w not in stop_words
]

top = Counter(filtered).most_common(10)

if len(top) == 0:
    st.warning("No keywords found.")
else:

    maximum = top[0][1]

    icons = [
        "🎥",
        "📚",
        "🎯",
        "💡",
        "🚀",
        "🎵",
        "🎮",
        "⭐",
        "📱",
        "💬"
    ]

    for i, (word, count) in enumerate(top):

        percentage = int((count / maximum) * 100)

        if percentage >= 80:
            level = "🔥 Trending Topic"

        elif percentage >= 60:
            level = "📈 Frequently Discussed"

        elif percentage >= 40:
            level = "💬 Popular"

        else:
            level = "📌 Mentioned"

        st.markdown(
            f"""
<div style="
background:linear-gradient(135deg,#111827,#1f2937);
padding:20px;
border-radius:18px;
margin-bottom:20px;
border-left:6px solid #00C2FF;
box-shadow:0 8px 20px rgba(0,0,0,.25);
">

<h3 style="color:white;margin-bottom:10px;">
{icons[i]} {word.title()}
</h3>

<p style="color:#7dd3fc;">
{level}
</p>

</div>
""",
            unsafe_allow_html=True
        )

        st.progress(percentage/100)

        c1, c2 = st.columns([5,1])

        with c1:
            st.caption(f"Popularity Score : {percentage}%")

        with c2:
            st.metric(
                "Mentions",
                count
            )

st.divider()

# ======================================================
# ☁️ AI Word Cloud
# ======================================================

st.header("☁️ AI Word Cloud")

if text.strip():

    wordcloud = WordCloud(
        width=1400,
        height=600,
        background_color="white",
        colormap="viridis",
        max_words=200
    ).generate(text)

    fig, ax = plt.subplots(figsize=(14,6))

    ax.imshow(
        wordcloud,
        interpolation="bilinear"
    )

    ax.axis("off")

    st.pyplot(fig)

else:

    st.info("Not enough words to generate Word Cloud.")

st.divider()

# ======================================================
# 😊 Emotion Analysis
# ======================================================

st.header("😊 Emotion Analysis")

emotion_result = detect_emotion(all_comments)

if emotion_result:

    st.bar_chart(emotion_result)

    c1, c2 = st.columns(2)

    with c1:

        dominant = max(
            emotion_result,
            key=emotion_result.get
        )

        st.success(
            f"Dominant Emotion : **{dominant}**"
        )

    with c2:

        st.metric(
            "Detected Emotions",
            len(emotion_result)
        )

else:

    st.info("Emotion analysis unavailable.")

st.divider()
# ======================================================
# 🤖 AI Smart Summary
# ======================================================

st.header("🤖 AI Smart Summary")

summary = generate_summary(
    positive,
    neutral,
    negative,
    score
)

st.success(summary)

st.divider()

# ======================================================
# 💡 AI Recommendations
# ======================================================

st.header("💡 AI Recommendations")

recommendations = []

if score >= 90:

    recommendations.extend([
        "🏆 Outstanding audience response.",
        "🎯 Continue producing similar content.",
        "📅 Maintain your current upload schedule.",
        "❤️ Your viewers are highly satisfied."
    ])

elif score >= 75:

    recommendations.extend([
        "👍 Audience enjoys your content.",
        "🎬 Improve thumbnails for even better CTR.",
        "💬 Reply to viewer comments more often.",
        "🚀 Increase upload consistency."
    ])

elif score >= 50:

    recommendations.extend([
        "🙂 Audience opinion is mixed.",
        "📊 Review negative comments carefully.",
        "🎤 Improve presentation style.",
        "✨ Make the introduction more engaging."
    ])

else:

    recommendations.extend([
        "⚠ Audience satisfaction is low.",
        "🎥 Improve video quality.",
        "🎙 Upgrade microphone/audio quality.",
        "📚 Focus on audience interests."
    ])

if n > p:
    recommendations.append("🔴 High negative feedback detected. Investigate recurring issues.")

if p > n:
    recommendations.append("🟢 Positive audience sentiment is dominant. Keep this content style.")

if ne > p:
    recommendations.append("🟡 Many viewers are neutral. Increase engagement with stronger hooks.")

for rec in recommendations:
    st.success(rec)

st.divider()

# ======================================================
# 🏆 Overall Creator Verdict
# ======================================================

st.header("🏆 Overall Creator Verdict")

if score >= 90:

    verdict = "🌟 Excellent"

    color = "green"

elif score >= 75:

    verdict = "🥇 Very Good"

    color = "blue"

elif score >= 60:

    verdict = "🥈 Good"

    color = "orange"

elif score >= 40:

    verdict = "🥉 Average"

    color = "gold"

else:

    verdict = "⚠ Needs Improvement"

    color = "red"

st.markdown(
    f"""
<div style="
background:linear-gradient(135deg,#111827,#1f2937);
padding:30px;
border-radius:20px;
text-align:center;
border:3px solid {color};
box-shadow:0px 10px 25px rgba(0,0,0,.30);
">

<h2 style="color:white;">
{verdict}
</h2>

<h1 style="color:#38bdf8;">
Creator Health Score
</h1>

<h1 style="font-size:60px;color:white;">
{score}%
</h1>

</div>
""",
unsafe_allow_html=True
)

st.divider()

# ======================================================
# 📈 Audience Satisfaction Meter
# ======================================================

st.header("📈 Audience Satisfaction")

bar = "🟩" * int(score / 10)
empty = "⬜" * (10 - int(score / 10))

st.markdown(
    f"""
### {bar}{empty}

## {score}% Audience Satisfaction
"""
)

st.divider()

# ======================================================
# 📌 Final AI Observation
# ======================================================

st.header("📌 Final AI Observation")

if score >= 85:

    st.success("""
### 🎉 AI Conclusion

This video has received an overwhelmingly positive response.

The audience appreciated the content, presentation, and overall quality.

The creator should continue producing similar videos while maintaining consistency.
""")

elif score >= 65:

    st.info("""
### 😊 AI Conclusion

The audience generally liked the video.

Some improvements in engagement and presentation can further improve performance.
""")

else:

    st.error("""
### ⚠ AI Conclusion

Audience response indicates several areas for improvement.

Focus on quality, presentation, editing, and viewer feedback before producing similar content.
""")

st.divider()

# ======================================================
# ❤️ Footer
# ======================================================

st.markdown(
"""
<div style='text-align:center;color:gray;padding:20px;'>

Made with ❤️ using Artificial Intelligence

<b>SentiTube AI Creator Analytics Platform</b>

</div>
""",
unsafe_allow_html=True
)