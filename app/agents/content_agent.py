from app.services.llm import call_llm


def run_content_agent(strategy_output, platform):

    platform = platform.lower()

    content_type = strategy_output.get(
        "content_type",
        "standard"
    ).lower()

from app.services.llm import call_llm


def run_content_agent(strategy_output, platform):

    platform = platform.lower()

    content_type = strategy_output.get(
        "content_type",
        "standard"
    ).lower()

    if platform == "instagram":

        prompt = f"""
You are a nutrition content creator for WholeBite.

Strategy:
{strategy_output}

CRITICAL:

Return ONLY a valid JSON object.

Do not explain.
Do not reason.
Do not add notes.
Do not add comments.
Do not add markdown.

Output MUST begin with {{
Output MUST end with }}

If any text appears outside JSON,
the response is invalid.

{{
    "platform": "instagram",
    "content_type": "{content_type}",
    "hook": "...",
    "content": "...",
    "caption": "...",
    "hashtags": ["#...", "#...", "#...", "#...", "#..."]
}}
"""

    else:

        prompt = f"""
You are a LinkedIn nutrition creator.

Strategy:
{strategy_output}

Return ONLY valid JSON.

{{
    "platform": "linkedin",
    "content_type": "{content_type}",
    "post": "...",
    "hashtags": ["#...", "#...", "#...", "#...", "#..."]
}}
"""

    return call_llm(
        prompt,
        model="llama3:latest"
    )
