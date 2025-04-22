# components/summary.py
import streamlit as st
from config import questions
from logic.scoring import calculate_score

def show_summary(user_context):
    st.success("🎉 You've completed the decision profile!")
    st.header("🧾 Your Perspective Summary")

    for i, q in enumerate(questions):
        answer = user_context.get(f"q{i+1}", "[Not answered]")
        if isinstance(answer, list):
            answer = ", ".join(answer)
        st.markdown(f"**{q}**\n> {answer}")

    st.markdown("---")
    st.header("📊 Preliminary Score (for illustration)")
    score = calculate_score(user_context)
    st.metric("🧠 Veridyn Clarity Score", f"{score}/10")
