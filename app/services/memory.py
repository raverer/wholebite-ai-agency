import json
import os

MEMORY_FILE = "app/memory/memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "topics": [],
            "hooks": [],
            "posts": [],
            "goals": [],
            "content_types": []
        }

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):
    # Ensure directory exists
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def update_memory(strategy, content):

    memory = load_memory()

    # Backward compatibility for older memory files
    memory.setdefault("topics", [])
    memory.setdefault("hooks", [])
    memory.setdefault("posts", [])
    memory.setdefault("goals", [])
    memory.setdefault("content_types", [])

    # Strategy fields
    topic = strategy.get("topic")
    goal = strategy.get(
    "original_goal",
    strategy.get("topic"))
    content_type = strategy.get("content_type")

    # Content fields
    hook = content.get("hook")
    platform = content.get("platform")

    # Save unique values
    if topic and topic not in memory["topics"]:
        memory["topics"].append(topic)

    if goal and goal not in memory["goals"]:
        memory["goals"].append(goal)

    if content_type and content_type not in memory["content_types"]:
        memory["content_types"].append(content_type)

    if hook and hook not in memory["hooks"]:
        memory["hooks"].append(hook)

    # Save post record
    memory["posts"].append({
        "topic": topic,
        "goal": goal,
        "content_type": content_type,
        "hook": hook,
        "platform": platform
    })

    # Keep only recent history
    memory["posts"] = memory["posts"][-100:]
    memory["topics"] = memory["topics"][-100:]
    memory["hooks"] = memory["hooks"][-100:]
    memory["goals"] = memory["goals"][-100:]
    memory["content_types"] = memory["content_types"][-100:]

    save_memory(memory)