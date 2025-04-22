# logic/scoring.py
def calculate_score(user_context):
    goal = user_context.get("q1", "")
    finance = user_context.get("q2", 0)
    urgency = user_context.get("q4", 0)

    goal_score = 8 if goal in ["Career switch", "Move abroad permanently"] else 5
    readiness_score = int(finance)
    urgency_score = int(urgency)

    overall = round((goal_score + readiness_score + urgency_score) / 3, 1)
    return overall
