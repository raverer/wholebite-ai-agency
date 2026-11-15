from typing import Optional, List, Dict, Any
from datetime import datetime

from pydantic import BaseModel, Field

from app.contracts import (
    ContentRequest,
    TrendOutput,
    PlannerOutput,
    FormatOutput,
    StrategyOutput,
    HookOutput,
    InstagramOutput,
    LinkedInOutput,
    QualityOutput,
    RepurposeOutput
)


# =====================================================
# EXECUTION STEP
# =====================================================

class ExecutionStep(BaseModel):
    agent: str
    status: str
    timestamp: str
    message: str


# =====================================================
# PIPELINE METADATA
# =====================================================

class PipelineMetadata(BaseModel):

    pipeline_version: str = "2.0"

    model_used: str = "phi3"

    started_at: str = Field(
        default_factory=lambda: datetime.now().isoformat()
    )

    finished_at: Optional[str] = None

    generation_time: Optional[float] = None

    retries: int = 0

    total_tokens: Optional[int] = None

    total_cost: Optional[float] = None

    status: str = "running"


# =====================================================
# PIPELINE CONTEXT
# =====================================================

class PipelineContext(BaseModel):

    """
    Shared state of the entire AI Agency.

    Every agent receives this object,
    updates its own section,
    and returns it.
    """

    # -----------------------------------------
    # ORIGINAL USER REQUEST
    # -----------------------------------------

    request: ContentRequest

    # -----------------------------------------
    # TREND
    # -----------------------------------------

    trend: Optional[TrendOutput] = None

    # -----------------------------------------
    # PLANNER
    # -----------------------------------------

    planner: Optional[PlannerOutput] = None

    # -----------------------------------------
    # FORMAT
    # -----------------------------------------

    format: Optional[FormatOutput] = None

    # -----------------------------------------
    # STRATEGY
    # -----------------------------------------

    strategy: Optional[StrategyOutput] = None

    # -----------------------------------------
    # HOOKS
    # -----------------------------------------

    hooks: Optional[HookOutput] = None

    # -----------------------------------------
    # INSTAGRAM
    # -----------------------------------------

    instagram: Optional[InstagramOutput] = None

    # -----------------------------------------
    # LINKEDIN
    # -----------------------------------------

    linkedin: Optional[LinkedInOutput] = None

    # -----------------------------------------
    # REPURPOSE
    # -----------------------------------------

    repurpose: Optional[RepurposeOutput] = None

    # -----------------------------------------
    # QUALITY
    # -----------------------------------------

    quality: Optional[QualityOutput] = None

    # -----------------------------------------
    # EXECUTION HISTORY
    # -----------------------------------------

    history: List[ExecutionStep] = Field(
        default_factory=list
    )

    # -----------------------------------------
    # SHARED DATA
    # -----------------------------------------

    shared: Dict[str, Any] = Field(
        default_factory=dict
    )

    # -----------------------------------------
    # METADATA
    # -----------------------------------------

    metadata: PipelineMetadata = Field(
        default_factory=PipelineMetadata
    )

    # =====================================================
    # HELPER METHODS
    # =====================================================

    def add_step(
        self,
        agent: str,
        message: str,
        status: str = "completed"
    ):

        self.history.append(

            ExecutionStep(

                agent=agent,

                status=status,

                timestamp=datetime.now().isoformat(),

                message=message

            )

        )

    def set_shared(
        self,
        key: str,
        value: Any
    ):

        self.shared[key] = value

    def get_shared(
        self,
        key: str,
        default=None
    ):

        return self.shared.get(key, default)