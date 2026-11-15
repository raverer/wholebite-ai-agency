from app.services.llm import call_llm

def run_critic_agent(output):

    prompt = f"""
You are a harsh content critic.

Content:
{output}

Return JSON:

{{
  "score": 1-10,
  "issues": ["...", "..."],
  "improvements": ["...", "..."]
}}
"""

    return call_llm(prompt, model="llama3:latest")