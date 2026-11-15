import json
import re

from app.agents.strategy_agent import run_strategy_agent
from app.agents.copy_agent import run_copy_agent
from app.agents.design_agent import run_design_agent
from app.agents.critic_agent import run_critic_agent
from app.agents.director_agent import run_director_agent

from app.services.memory import load_memory, save_memory
from app.services.normalizer import normalize_output, clean_text_fields, extract_slides
from app.services.image_prompt_enhancer import enhance_image_prompt


# ---------------- MEMORY ---------------- #
def update_memory(final_output, critic):
    try:
        memory = load_memory()

        score = critic.get("score", 0)
        hook = final_output.get("strategy", {}).get("hook")

        print("CRITIC SCORE:", score)
        print("HOOK:", hook)

        if hook and score >= 7:
            memory.setdefault("hooks", []).append(hook)

        save_memory(memory)

    except Exception as e:
        print("MEMORY ERROR:", str(e))


# ---------------- WORKFLOW ---------------- #
def run_workflow(brand):

    strategy = run_strategy_agent(brand)

    #hooks = run_hook_agent(strategy)

    content = run_content_agent(strategy, hooks)

    #critic = run_critic_agent(content)

    #final = run_director_agent(content, critic)

    design = run_design_agent(final, strategy)

    return {
        "strategy": strategy,
        #"hooks": hooks,
        "content": content,
        #"critic": critic,
        #"final": final,
        "design": design
    }