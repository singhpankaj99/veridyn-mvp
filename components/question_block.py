# components/question_block.py
import streamlit as st
from config import questions

def render_question(q_idx, user_context):
    current_q = questions[q_idx]
    st.markdown(f"**Varnika:** {current_q}")

    user_key = f"q{q_idx+1}"
    stored_val = user_context.get(user_key)
    valid = False
    ans = None

    if q_idx == 0:
        options = [
            "", "Career switch", "Higher salary", "Move abroad permanently",
            "Learn something new", "Status / prestige", "Escape current environment"
        ]
        index = options.index(stored_val) if stored_val in options else 0
        ans = st.selectbox("Select your goal:", options, index=index)
        valid = ans != ""

    elif q_idx == 1:
        ans = st.slider("Rate your financial readiness:", 0, 10, stored_val if stored_val is not None else 5)
        valid = True

    elif q_idx == 2:
        options = ["United States", "United Kingdom", "Germany", "Canada", "Australia", "Stay in current country"]
        default = stored_val if stored_val else []
        ans = st.multiselect("Choose countries:", options, default=default)
        valid = len(ans) > 0

    elif q_idx == 3:
        ans = st.slider("Urgency level:", 0, 10, stored_val if stored_val is not None else 5)
        valid = True

    else:
        ans = st.text_area("Your thoughts:", value=stored_val if stored_val else "")
        valid = ans.strip() != ""

    if not valid:
        st.warning("👈 Please complete this question before continuing.")

    return ans, valid
