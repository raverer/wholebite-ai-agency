from app.services.llm import call_llm

def run_design_agent(content_output, strategy):

    prompt = f"""
You are a viral content creative director.

Content:
{content_output}

Create visual ideas.

Return JSON:

{{
  "concept": "...",
  "style": "...",
  "slides": [
    {{
      "slide": 1,
      "visual": "...",
      "scene": "...",
      "emotion": "..."
    }}
  ]
}}

Brand Personality:
- No-BS
- Calls out bad habits
- Practical
- Built for busy professionals
- Feels like a smart friend, not a coach

Visuals should reflect real life:
- home eating
- snacks
- cravings
- late night eating
- not just office scenes

RULES:
- Use office scenes, desks, laptops, tired employees
- Use contrast (lazy vs disciplined)
- Use real-life situations
- NOT just food
- Think like viral reels/carousels
"""
    
    return call_llm(prompt, model="llama3:latest")