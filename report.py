import streamlit as st
from pdf_generator import generate_pdf

st.title("📄 Report")

if "score" not in st.session_state:

    st.warning("Please analyze a video first.")

    st.stop()

positive=st.session_state["positive"]

negative=st.session_state["negative"]

neutral=st.session_state["neutral"]

score=st.session_state["score"]

p=len(positive)

n=len(negative)

ne=len(neutral)

total=p+n+ne

st.subheader("Professional Report")

st.write("Generate a professional PDF report.")

if st.button("📄 Generate Report"):

    generate_pdf(

        "SentiTube_Report.pdf",

        score,

        p,

        n,

        ne,

        total

    )

    st.success("Report Generated Successfully!")

    with open("SentiTube_Report.pdf","rb") as pdf:

        st.download_button(

            "⬇ Download PDF",

            pdf,

            file_name="SentiTube_Report.pdf"

        )