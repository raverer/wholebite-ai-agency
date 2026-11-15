from typing import Type, TypeVar

from pydantic import BaseModel

from app.core.prompt_loader import prompt_loader
from app.core.json_parser import parse_json
from app.core.logger import logger
from app.services.llm import call_llm


T = TypeVar("T", bound=BaseModel)


class LLMEngine:

    """
    Central AI Engine

    Responsibilities

    • Load Prompt
    • Inject Variables
    • Call LLM
    • Parse JSON
    • Validate Contract
    • Retry on JSON failure
    """

    def generate(
        self,
        prompt_name: str,
        variables: dict,
        output_model: Type[T],
        model: str = "phi3"
    ) -> T:

        prompt = prompt_loader.load(prompt_name)

        for key, value in variables.items():

            prompt = prompt.replace(
                "{{" + key + "}}",
                str(value)
            )

        logger.info(f"Running prompt: {prompt_name}")

        response = call_llm(
            prompt,
            model=model
        )

        try:

            data = parse_json(response)

        except Exception:

            logger.warning(
                "JSON parsing failed. Retrying..."
            )

            repair_prompt = f"""
Return ONLY valid JSON.

Do not explain anything.

Previous response:

{response}
"""

            repaired = call_llm(
                repair_prompt,
                model=model
            )

            data = parse_json(repaired)

        result = output_model(**data)

        logger.info(
            f"{prompt_name} completed successfully."
        )

        return result


llm_engine = LLMEngine()