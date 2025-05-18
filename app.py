import streamlit as st
from matcher import get_match_score, get_llm_feedback

st.set_page_config(page_title="LLM Resume Matcher", layout="centered")
st.title("🤖 LLM-Powered Resume Matcher (Local)")

resume = st.text_area("📄 Paste your Resume Text", height=300)
jd = st.text_area("💼 Paste Job Description", height=300)

if st.button("🔍 Match Resume to Job"):
    if not resume or not jd:
        st.warning("Please provide both resume and job description.")
    else:
        with st.spinner("Calculating match..."):
            score = get_match_score(resume, jd)
            st.success(f"✅ Match Score: {score}%")

            st.markdown("---")
            st.subheader("💬 Feedback from AI")
            feedback = get_llm_feedback(resume, jd)
            st.write(feedback)
