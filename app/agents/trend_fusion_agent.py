def fuse_goal_and_trend(goal, trend_keyword):

    goal = (goal or "").lower()
    trend = (trend_keyword or "").lower()

    category = "general"

    if "protein" in trend:
        category = "protein"

    elif "gut" in trend:
        category = "gut_health"

    elif "cholesterol" in trend:
        category = "cholesterol"

    elif "meal prep" in trend:
        category = "meal_prep"

    fused_topic = goal

    if category == "protein":
        fused_topic = f"High Protein {goal}"

    elif category == "gut_health":
        fused_topic = f"{goal} for Better Gut Health"

    elif category == "cholesterol":
        fused_topic = f"{goal} for Heart Health"

    return {
        "trend_category": category,
        "fused_topic": fused_topic
    }