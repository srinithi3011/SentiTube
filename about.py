import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="👨",
    layout="wide"
)

st.title("👨 About SentiTube")

st.markdown("---")

st.subheader("🎬 Project Name")

st.write("SentiTube")

st.subheader("📖 Description")

st.write("""
SentiTube is an AI-powered YouTube Comment Analysis platform.

It helps creators understand audience sentiment by analyzing comments and presenting insights through dashboards, reports, and AI-generated recommendations.
""")

st.markdown("---")

st.subheader("🛠 Technologies Used")

st.write("""
- Python
- Streamlit
- YouTube Data API v3
- VADER Sentiment Analysis
- Pandas
- Matplotlib
- ReportLab
""")

st.markdown("---")

st.subheader("👨‍💻 Developed By")

st.write("""
**Srinithi**

B.Tech – Artificial Intelligence & Data Science
""")

st.markdown("---")

st.success("Thank you for using SentiTube! 🎉")