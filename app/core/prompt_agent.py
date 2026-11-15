"""
PromptAgent

Base class for every prompt-driven AI agent.

Responsibilities:
- Load prompts
- Call the LLM
- Validate structured output
- Retry failed generations
- Record execution logs

PlannerAgent
StrategyAgent
CarouselAgent
ReelAgent
LinkedInAgent

all inherit from this class.
"""

import time
from typing import Any, Dict, Type

from pydantic import BaseModel

from app.core.base_agent import BaseAgent
from app.core.llm_engine import llm_engine


class PromptAgent(BaseAgent):

    def __init__(
        self,
        prompt_name: str,
        name: str | None = None
    ):

        super().__init__(name)

        self.prompt_name = prompt_name

    # ======================================================
    # Generate
    # ======================================================

    def generate(

        self,

        variables: Dict[str, Any],

        output_model: Type[BaseModel],

        retries: int = 2

    ) -> BaseModel:

        last_error = None

        for attempt in range(retries + 1):

            try:

                start = time.time()

                result = llm_engine.generate(

                    prompt_name=self.prompt_name,

                    variables=variables,

                    output_model=output_model

                )

                elapsed = round(
                    time.time() - start,
                    2
                )

                print(
                    f"[{self.name}] completed in {elapsed}s"
                )

                return result

            except Exception as e:

                last_error = e

                print(
                    f"[{self.name}] Retry {attempt + 1}/{retries}"
                )

        raise RuntimeError(

            f"{self.name} failed."

        ) from last_error

    # ======================================================
    # Helper Functions
    # ======================================================

    @staticmethod
    def clean_text(text: str) -> str:

        if not text:

            return ""

        return text.strip()

    @staticmethod
    def safe_list(value):

        if value is None:

            return []

        return value

    # ======================================================
    # Execute
    # ======================================================

    def execute(self, context):
        """
        PromptAgent is an abstract helper.

        Child agents must implement execute().
        """

        raise NotImplementedError(
            f"{self.__class__.__name__} must implement execute()."
        )