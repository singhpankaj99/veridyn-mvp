# app.py main controller app
import streamlit as st
from config import questions
from components.question_block import render_question
from components.summary import show_summary

st.set_page_config(page_title="Veridyn – Varnika", layout="centered")
st.title("🎓 Veridyn – Study Abroad Decision Assistant")
st.markdown("Guided by Varnika. Step into your clarity.")
st.markdown("---")

# Initialize state
if "user_context" not in st.session_state:
    st.session_state.user_context = {}

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

q_idx = st.session_state.question_index
total = len(questions)

# Progress bar
progress = int((q_idx / total) * 100)
st.sidebar.markdown("### 🧭 Your Progress")
st.sidebar.progress(progress)

# Show previous answers
st.markdown("### 💬 Varnika's Guidance")
for i in range(q_idx):
    q = questions[i]
    ans = st.session_state.user_context.get(f"q{i+1}", "[Not answered]")
    if isinstance(ans, list):
        ans = ", ".join(ans)
    st.markdown(f"**Varnika:** {q}\n👉 You: _{ans}_")
    st.markdown("---")

# Ask current or show summary
if q_idx < total:
    ans, valid = render_question(q_idx, st.session_state.user_context)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Previous"):
            st.session_state.user_context[f"q{q_idx+1}"] = ans
            st.session_state.question_index = max(0, q_idx - 1)

    with col2:
        if st.button("Next") and valid:
            st.session_state.user_context[f"q{q_idx+1}"] = ans
            st.session_state.question_index += 1
else:
    show_summary(st.session_state.user_context)
