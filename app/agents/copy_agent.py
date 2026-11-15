from app.services.llm import call_llm


def run_copy_agent(brand, strategy):

    platform = brand.get("platform", "instagram")

    # -------- STYLE -------- #
    if platform == "instagram":
        style_instruction = """
You are an Instagram fitness content creator.

Write:
- Short, punchy lines
- Strong hook in first line
- Very easy to read
- Slightly aggressive tone
- Use real food examples (roti, dal, paneer)
- No long paragraphs

Focus:
- Scroll stopping
- Relatable
- Visual thinking
"""
        output_format = """
Generate:
- instagram_caption
- hashtags
"""

    else:
        style_instruction = """
You are a LinkedIn content strategist.

Write:
- Insight-driven content
- Slight storytelling
- Clear explanation
- Professional but simple tone
- No fluff

Focus:
- Value
- Clarity
- Practical advice
"""
        output_format = """
Generate:
- linkedin_caption
- hashtags
"""

    # -------- PROMPT -------- #
    prompt = f"""
{style_instruction}

Brand:
{brand}

Strategy:
{strategy}

{output_format}

Return ONLY valid JSON.
Do not add explanation.
Do not add markdown.
If output is not JSON, the system will break.
Do NOT add explanation.
"""

    return call_llm(prompt, model="llama3:latest")