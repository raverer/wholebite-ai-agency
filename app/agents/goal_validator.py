def validate_goal(goal, topic):

    if not goal or not topic:
        return True

    goal_words = set(
        goal.lower().split()
    )

    topic_words = set(
        topic.lower().split()
    )

    overlap = goal_words.intersection(
        topic_words
    )

    return len(overlap) >= 1