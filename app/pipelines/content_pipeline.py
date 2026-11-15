from app.agents.strategy_agent import run_strategy_agent
from app.agents.hook_agent import run_hook_agent
from app.agents.content_agent import run_content_agent
from app.agents.planner_agent import run_planner_agent
from app.agents.format_agent import run_format_agent
from app.agents.trend_agent import get_trending_keyword
from app.agents.trend_fusion_agent import fuse_goal_and_trend
from app.agents.goal_validator import validate_goal

from app.services.audience_selector import get_audience_from_keyword
from app.services.memory import update_memory

from app.utils.formatter import format_linkedin_post


def run_content_pipeline(input_data):

    # ==========================================
    # TREND COLLECTION
    # ==========================================

    trend_keyword = get_trending_keyword()

    audience = get_audience_from_keyword(
        trend_keyword
    )

    input_data["trend_keyword"] = trend_keyword
    input_data["audience"] = audience

    # ==========================================
    # TREND FUSION
    # ==========================================

    fusion = fuse_goal_and_trend(
        input_data.get("goal"),
        trend_keyword
    )

    input_data["trend_category"] = fusion["trend_category"]
    input_data["fused_topic"] = fusion["fused_topic"]

    # ==========================================
    # CONTENT PLANNER
    # ==========================================

    planner = run_planner_agent(input_data)

    input_data["planner"] = planner

    print("===================================")
    print("TREND KEYWORD:", trend_keyword)
    print("TREND CATEGORY:", fusion["trend_category"])
    print("FUSED TOPIC:", fusion["fused_topic"])
    print("AUDIENCE:", audience)
    print("===================================")

    # ==========================================
    # STRATEGY
    # ==========================================

    strategy = run_strategy_agent(input_data)

    # ==========================================
    # MERGE PLANNER OUTPUT
    # ==========================================

    if isinstance(planner, dict):

        strategy["planner"] = planner

        strategy["recommended_format"] = planner.get(
            "recommended_format"
        )

        strategy["alternate_formats"] = planner.get(
            "alternate_formats",
            []
        )

        strategy["content_pillar"] = planner.get(
            "content_pillar"
        )

        strategy["emotion"] = planner.get(
            "emotion"
        )

        strategy["cta"] = planner.get(
            "cta"
        )

        strategy["funnel_stage"] = planner.get(
            "funnel_stage"
        )

        strategy["difficulty"] = planner.get(
            "difficulty"
        )

        strategy["virality"] = planner.get(
            "virality"
        )

    # ==========================================
    # FALLBACK STRATEGY
    # ==========================================

    if "error" in strategy:

        strategy = {
            "platform": input_data.get("platform"),
            "content_type": input_data.get(
                "content_type",
                "standard"
            ),
            "topic": input_data.get("goal"),
            "core_problem": "Unable to generate strategy",
            "content_angle": "Practical nutrition advice"
        }

    # Save original goal

    strategy["original_goal"] = input_data.get("goal")

    # ==========================================
    # GOAL VALIDATION
    # ==========================================

    is_valid = validate_goal(
        input_data.get("goal"),
        strategy.get("topic")
    )

    if not is_valid:

        print("Goal Validation Failed. Fixing topic...")

        strategy["topic"] = input_data.get("goal")

    # ==========================================
    # HOOK GENERATION
    # ==========================================

    hooks = run_hook_agent(strategy)

    # ==========================================
    # CONTENT GENERATION
    # ==========================================

    content = run_content_agent(
        strategy,
        input_data.get("platform")
    )

    # ==========================================
    # INSERT SELECTED HOOK
    # ==========================================

    if (
        hooks
        and isinstance(hooks, dict)
        and hooks.get("selected_hook")
    ):
        content["hook"] = hooks["selected_hook"]

    # ==========================================
    # OPTIONAL FORMATTER
    # ==========================================

    try:
        content = run_format_agent(content)
    except Exception:
        pass

    # ==========================================
    # LINKEDIN FORMATTING
    # ==========================================

    if (
        content.get("platform", "").lower() == "linkedin"
        and content.get("post")
    ):
        content["post"] = format_linkedin_post(
            content["post"]
        )

    # ==========================================
    # MEMORY
    # ==========================================

    update_memory(
        strategy,
        content
    )

    # ==========================================
    # RESPONSE
    # ==========================================

    return {
        "trend_keyword": trend_keyword,
        "audience": audience,
        "trend_category": fusion["trend_category"],
        "planner": planner,
        "strategy": strategy,
        "hooks": hooks,
        "content": content
    }