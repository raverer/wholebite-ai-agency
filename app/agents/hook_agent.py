from app.services.llm import call_llm

def run_hook_agent(strategy_output):

    prompt = f"""
You are a viral content expert.

Topic: {strategy_output.get("topic")}
Problem: {strategy_output.get("core_problem")}

Generate 5 hooks.

Rules:
- Max 10 words
- Brutal, direct
- Should feel like calling out the user
- Must sound like real conversation
- No motivational tone

Return JSON:

{{
  "hooks": [
    {{"type": "aggressive", "text": "..."}},
    {{"type": "curiosity", "text": "..."}},
    {{"type": "relatable", "text": "..."}},
    {{"type": "contrarian", "text": "..."}},
    {{"type": "fear", "text": "..."}}
  ],
  "selected_hook": "FULL hook text"
}}
"""

    return call_llm(prompt, model="llama3:latest")