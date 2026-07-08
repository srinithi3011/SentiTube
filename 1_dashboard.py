import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from recommendation import generate_recommendations

st.set_page_config(page_title="Dashboard", layout="wide")

# Load CSS
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

st.title("📊 Creator Dashboard")
st.markdown("""
Welcome to the Creator Analytics Dashboard.

View your audience sentiment, engagement and overall creator health.
""")

if "score" not in st.session_state:
    st.warning("Please analyze a video first.")
    st.stop()

positive = st.session_state["positive"]
negative = st.session_state["negative"]
neutral = st.session_state["neutral"]

score = st.session_state["score"]

p = len(positive)
n = len(negative)
ne = len(neutral)

total = p + n + ne
st.markdown("❤️ Creator Health Score")

st.progress(int(score))

st.markdown(f"""
<div class="metric-card">

<div class="metric-title">
❤️ Creator Health Score
</div>

<div class="metric-value">
{score}%
</div>

</div>
""",
unsafe_allow_html=True)

col1,col2,col3,col4 = st.columns(4)

for col, emoji, title, value in zip(

    [col1,col2,col3,col4],

    ["😊","😐","😡","💬"],

    ["Positive","Neutral","Negative","Total"],

    [p,ne,n,total]

):

    with col:

        st.markdown(f"""
        <div class="metric-card">

        <div style="font-size:30px;">
        {emoji}
        </div>

        <div class="metric-title">
        {title}
        </div>

        <div class="metric-value">
        {value}
        </div>

        </div>
        """,
        unsafe_allow_html=True)
data = pd.DataFrame({

    "Sentiment":[
        "Positive",
        "Neutral",
        "Negative"
    ],

    "Count":[
        p,
        ne,
        n
    ]
})

pie = px.pie(

    data,

    values="Count",

    names="Sentiment",

    hole=0.5,

    title="Sentiment Distribution"
)

st.plotly_chart(
    pie,
    use_container_width=True
)
bar = px.bar(

    data,

    x="Sentiment",

    y="Count",

    text="Count",

    title="Comment Analysis"
)

st.plotly_chart(

    bar,

    use_container_width=True
)
st.divider()

st.header("📈 Advanced Creator Analytics")
engagement = min(100, int((total / 25)))

satisfaction = score

community = min(100, int((p / total) * 100))

activity = min(100, int(total / 30))

performance = int((engagement + satisfaction) / 2)

creator_rating = round(score / 20, 1)
c1, c2 = st.columns(2)

with c1:

    st.metric(
        "⭐ Creator Rating",
        f"{creator_rating}/5"
    )

    st.progress(creator_rating / 5)

    st.metric(
        "❤️ Audience Satisfaction",
        f"{satisfaction}%"
    )

    st.progress(satisfaction / 100)

    st.metric(
        "📈 Engagement",
        f"{engagement}%"
    )

    st.progress(engagement / 100)

with c2:

    st.metric(
        "💬 Community Activity",
        f"{activity}%"
    )

    st.progress(activity / 100)

    st.metric(
        "🔥 Popularity",
        f"{community}%"
    )

    st.progress(community / 100)

    st.metric(
        "🎯 Performance",
        f"{performance}%"
    )

    st.progress(performance / 100)
    st.divider()

st.header("🎯 Audience Mood Meter")
fig = go.Figure(
    go.Indicator(
        mode="gauge+number",

        value=score,

        title={
            "text": "Creator Health Score"
        },

        gauge={

            "axis": {
                "range": [0,100]
            },

            "bar": {
                "color":"deepskyblue"
            },

            "steps":[

                {
                    "range":[0,40],
                    "color":"#ef4444"
                },

                {
                    "range":[40,70],
                    "color":"#facc15"
                },

                {
                    "range":[70,100],
                    "color":"#22c55e"
                }

            ]
        }
    )
)
st.plotly_chart(
    fig,
    use_container_width=True
)
if score >= 90:
    st.success("🎉 Your audience absolutely loves this content!")

elif score >= 75:
    st.info("👍 Your audience is highly satisfied.")

elif score >= 50:
    st.warning("🙂 Audience response is average.")

else:
    st.error("⚠️ Audience response needs improvement.")
st.divider()

st.header("📺 Video Performance")
details = st.session_state.get("video_details")

if details:

    views = int(details["views"])
    likes = int(details["likes"])
    comments = int(details["comments"])
    like_ratio = (likes / views) * 100 if views else 0

comment_ratio = (comments / views) * 100 if views else 0

engagement_rate = ((likes + comments) / views) * 100 if views else 0

viral_score = min(
    100,
    int(engagement_rate * 12)
)
c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "👀 Views",
    f"{views:,}"
)

c2.metric(
    "👍 Likes",
    f"{likes:,}"
)

c3.metric(
    "💬 Comments",
    f"{comments:,}"
)

c4.metric(
    "🔥 Viral Score",
    f"{viral_score}%"
)
c1, c2, c3 = st.columns(3)

c1.metric(
    "❤️ Like Ratio",
    f"{like_ratio:.2f}%"
)

c2.metric(
    "💬 Comment Ratio",
    f"{comment_ratio:.2f}%"
)

c3.metric(
    "📈 Engagement",
    f"{engagement_rate:.2f}%"
)
st.divider()

st.markdown("## 📈 Audience Satisfaction")

if score >= 80:

    st.success("★★★★★ Outstanding Audience Satisfaction")

elif score >= 60:

    st.info("★★★★☆ Good Audience Satisfaction")

elif score >= 40:

    st.warning("★★★☆☆ Average Audience Satisfaction")

else:

    st.error("★★☆☆☆ Needs Improvement")
    
st.markdown("📈 Summary")

st.info(f"""
Out of **{total}** analyzed comments:

😊 Positive : **{p}**

😐 Neutral : **{ne}**

😡 Negative : **{n}**

❤️ Creator Health Score : **{score}%**
""")
st.markdown("## 🤖 AI Quick Summary")

if score >= 80:

    st.markdown("""
<div class="summary-card">

The audience response is overwhelmingly positive.

Your viewers appreciate the quality of the content and engagement.

Keep producing similar content consistently.

</div>
""",
unsafe_allow_html=True)

elif score >= 60:

    st.markdown("""
<div class="summary-card">

The audience generally likes your content.

A few improvements could further increase engagement.

</div>
""",
unsafe_allow_html=True)

else:

    st.markdown("""
<div class="summary-card">

Audience feedback is mixed.

Review negative comments carefully and improve future videos.

</div>
""",
unsafe_allow_html=True)
    st.divider()

st.header("🏆 Overall Performance")

if performance >= 90:

    st.success("🏆 Outstanding Performance")

elif performance >= 75:

    st.info("🥇 Excellent Performance")

elif performance >= 60:

    st.warning("🥈 Good Performance")

else:

    st.error("🥉 Needs Improvement")

    st.divider()

st.header("🤖 AI Recommendations")

recommendations = generate_recommendations(
    score,
    positive,
    neutral,
    negative,
    engagement_rate
)

for rec in recommendations:
    st.success(rec)