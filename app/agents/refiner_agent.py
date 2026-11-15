from app.services.llm import call_llm

def run_refiner_agent(content_output, critic_output):

    prompt = f"""
You are a creative director.

Content:
{content_output}

Critic:
{critic_output}

Improve it.
Return ONLY valid JSON.
Do not add explanation.
Do not add markdown.
If output is not JSON, the system will break.

Output JSON:
{{
  "final_slides": [...],
  "final_caption": "...",
  "final_hashtags": [...]
}}
"""

    return call_llm(prompt, model="llama3:latest")
