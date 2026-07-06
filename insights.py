import streamlit as st

st.set_page_config(
    page_title="AI Insights",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Insights")

if "score" not in st.session_state:
    st.warning("Please analyze a YouTube video first.")
    st.stop()

positive = st.session_state["positive"]
negative = st.session_state["negative"]
neutral = st.session_state["neutral"]
score = st.session_state["score"]

p = len(positive)
n = len(negative)
ne = len(neutral)
total = p + n + ne

st.metric("❤️ Creator Health Score", f"{score}%")

st.divider()

# Audience Mood
if score >= 80:
    mood = "😍 Excellent"
elif score >= 60:
    mood = "🙂 Good"
elif score >= 40:
    mood = "😐 Mixed"
else:
    mood = "😟 Needs Improvement"

st.subheader("🎯 Audience Mood")
st.success(mood)

st.divider()

st.subheader("📈 AI Analysis")

if p > n:
    st.success("✔ Overall audience reaction is positive.")

if n > p:
    st.error("⚠ Overall audience reaction is negative.")

if ne > p:
    st.info("ℹ Many viewers expressed neutral opinions.")

st.divider()

st.subheader("💡 Recommendations")

if score >= 80:
    st.success("""
✅ Continue making similar content.

✅ Upload consistently.

✅ Maintain the same presentation style.

✅ Engage with viewers in comments.
""")

elif score >= 60:
    st.info("""
• Improve thumbnails.

• Improve titles.

• Ask viewers questions.

• Increase engagement.
""")

else:
    st.error("""
❌ Improve audio quality.

❌ Improve editing.

❌ Shorten long videos.

❌ Focus on viewer feedback.
""")

st.divider()

st.subheader("📊 Sentiment Summary")

st.write(f"😊 Positive Comments : **{p}**")
st.write(f"😐 Neutral Comments : **{ne}**")
st.write(f"😡 Negative Comments : **{n}**")
st.write(f"💬 Total Comments : **{total}**")