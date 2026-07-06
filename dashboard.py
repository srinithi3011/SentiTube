import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

st.title("📊 Creator Dashboard")

# Check if analysis has been done
if "score" not in st.session_state:
    st.warning("⚠ Please analyze a YouTube video first from the Home page.")
    st.stop()

# Load data from session
positive = st.session_state["positive"]
negative = st.session_state["negative"]
neutral = st.session_state["neutral"]
score = st.session_state["score"]

p = len(positive)
n = len(negative)
ne = len(neutral)
total = p + n + ne

# --------------------------
# Top Metrics
# --------------------------
st.subheader("📈 Overall Performance")

col1, col2, col3, col4 = st.columns(4)

col1.metric("😊 Positive", p)
col2.metric("😐 Neutral", ne)
col3.metric("😡 Negative", n)
col4.metric("❤️ Health Score", f"{score}%")

st.progress(int(score))

st.divider()

# --------------------------
# Charts
# --------------------------
left, right = st.columns(2)

with left:
    st.subheader("🥧 Sentiment Distribution")

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(
        [p, n, ne],
        labels=["Positive", "Negative", "Neutral"],
        autopct="%1.1f%%",
        startangle=90
    )
    ax.axis("equal")
    st.pyplot(fig)

with right:
    st.subheader("📊 Sentiment Count")

    chart = pd.DataFrame({
        "Sentiment": ["Positive", "Negative", "Neutral"],
        "Count": [p, n, ne]
    })

    st.bar_chart(chart.set_index("Sentiment"))

st.divider()

# --------------------------
# Audience Summary
# --------------------------
st.subheader("📋 Audience Summary")

if score >= 80:
    st.success("🎉 Excellent audience engagement! Your viewers are responding very positively.")

elif score >= 60:
    st.info("🙂 Overall audience response is good with some mixed opinions.")

elif score >= 40:
    st.warning("⚠ Audience response is mixed. Consider reviewing viewer feedback.")

else:
    st.error("❌ Audience response is mostly negative. Improvements are recommended.")

st.write(f"**Total Comments Analysed:** {total}")
st.write(f"**Positive:** {round((p/total)*100,2)}%" if total else "Positive: 0%")
st.write(f"**Neutral:** {round((ne/total)*100,2)}%" if total else "Neutral: 0%")
st.write(f"**Negative:** {round((n/total)*100,2)}%" if total else "Negative: 0%")