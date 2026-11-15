from app.services.llm import call_llm

def run_director_agent(output, critic):
    prompt = f"""
You are a top-tier Creative Director for a viral nutrition brand.

Content:
{output}

Critic Feedback:
{critic}

YOUR JOB:
- Do NOT just fix — TRANSFORM the content
- Make it scroll-stopping
- Make it feel like exposing a mistake
- Make it bold, sharp, and real

STRICT RULES:
- Hook must feel like calling out the user
- Use everyday language (no corporate tone)
- NO motivational fluff
- NO generic words like "boost", "optimize", "transform"
- Use real Indian food examples (roti, dal, paneer, rice)

Return ONLY valid JSON.
Do not add explanation.
Do not add markdown.
If output is not JSON, the system will break.

CAROUSEL RULES (VERY IMPORTANT):
- ALWAYS return 5 slides
- DO NOT remove slides
- Each slide must be visually different
- Each slide must follow story:

Slide 1 → Hook (problem)
Slide 2 → Mistake
Slide 3 → Why it's bad
Slide 4 → Correct plate
Slide 5 → Takeaway

OUTPUT FORMAT (STRICT JSON ONLY):

{{
  "strategy": {{
    "topic": "",
    "hook": ""
  }},
  "copy": {{
    "instagram_caption": "",
    "linkedin_caption": "",
    "hashtags": []
  }},
  "design": {{
    "slides": [
      {{"image_prompt": "", "text": ""}},
      {{"image_prompt": "", "text": ""}},
      {{"image_prompt": "", "text": ""}},
      {{"image_prompt": "", "text": ""}},
      {{"image_prompt": "", "text": ""}}
    ]
  }}
}}

IMPORTANT:
- DO NOT output image_prompt outside slides
- DO NOT remove slides
- ONLY return JSON
"""

    return call_llm(prompt, model="llama3:latest")