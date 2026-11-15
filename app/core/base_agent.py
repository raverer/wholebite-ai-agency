from abc import ABC, abstractmethod
from typing import Optional

from app.models.pipeline_context import PipelineContext


class BaseAgent(ABC):
    """
    Abstract base class for every agent in the AI Agency.

    Every agent must implement execute().
    """

    def __init__(
        self,
        name: Optional[str] = None
    ):

        self.name = name or self.__class__.__name__

    @abstractmethod
    def execute(
        self,
        context: PipelineContext
    ) -> PipelineContext:
        """
        Execute the agent.
        """
        pass