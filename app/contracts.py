from typing import List, Optional, Dict, Any
from pydantic import BaseModel


# ==========================================================
# USER REQUEST
# ==========================================================

class ContentRequest(BaseModel):
    brand: str
    niche: str
    audience: str
    platform: str
    goal: str
    content_type: str


# ==========================================================
# TREND
# ==========================================================

class TrendOutput(BaseModel):
    keyword: str
    category: str
    audience: str
    search_volume: Optional[str] = None
    competition: Optional[str] = None


# ==========================================================
# PLANNER
# ==========================================================

# ONLY the LLM creates these fields

class PlannerLLMOutput(BaseModel):
    campaign: str
    series: str


# Final planner output after Python merges rule-based fields

class PlannerOutput(BaseModel):
    campaign: str
    series: str

    content_pillar: str

    funnel_stage: str

    emotion: str

    cta: str

    objective: str

    recommended_formats: List[str]

    difficulty: str

    virality_score: int


# ==========================================================
# FORMAT
# ==========================================================

class FormatLLMOutput(BaseModel):
    reason: str


class FormatOutput(BaseModel):
    primary_format: str

    secondary_format: Optional[str] = None

    reason: str

    estimated_engagement: str

    recommended_length: str

    visual_priority: str


# ==========================================================
# STRATEGY
# ==========================================================



# ----------------------------------------------------------
# LLM Output
# ----------------------------------------------------------

class StrategyLLMOutput(BaseModel):

    topic: str

    series_name: str

    content_angle: str

    core_problem: str

    audience_pain: str

    audience_desire: str

    key_message: str

    primary_takeaway: str

    proof_points: List[str]


# ----------------------------------------------------------
# Strategy Output
# ----------------------------------------------------------

class StrategyOutput(BaseModel):

    # Platform Information
    platform: str

    content_type: str

    # Creative Brief
    topic: str

    series_name: str

    content_angle: str

    core_problem: str

    audience_pain: str

    audience_desire: str

    key_message: str

    primary_takeaway: str

    proof_points: List[str]

    # Rule Engine Output
    content_pillar: str

    content_blueprint: List[str]

    tone: str

    story_framework: str

    cta_direction: str

    objective: str

    funnel_stage: str


# ==========================================================
# HOOKS
# ==========================================================

# ==========================================================
# HOOKS
# ==========================================================

class Hook(BaseModel):

    type: str

    text: str

    psychology: str

    engagement_goal: str

    score: int = 0


# ==========================================================
# HOOK LLM OUTPUT
# ==========================================================

class HookLLMOutput(BaseModel):

    hooks: List[Hook]


# ==========================================================
# FINAL HOOK OUTPUT
# ==========================================================

class HookOutput(BaseModel):

    hooks: List[Hook]

    selected_hook: str

# ==========================================================
# CREATIVE DIRECTOR
# ==========================================================

class CreativeLLMOutput(BaseModel):

    campaign_big_idea: str

    creative_angle: str

    opening_style: str

    storytelling_style: str

    emotional_arc: str

    visual_direction: str

    cta_style: str

    writing_style: str


class CreativeOutput(BaseModel):

    campaign_big_idea: str

    creative_angle: str

    opening_style: str

    storytelling_style: str

    emotional_arc: str

    visual_direction: str

    cta_style: str

    writing_style: str

# ==========================================================
# INSTAGRAM CAROUSEL
# ==========================================================



class CarouselSlide(BaseModel):

    slide_number: int

    title: str

    body: str


class InstagramCarouselLLMOutput(BaseModel):

    cover: str

    slides: List[CarouselSlide]

    caption: str

    hashtags: List[str]


class InstagramCarouselOutput(BaseModel):

    platform: str = "Instagram"

    format: str = "Carousel"

    hook: str

    cover: str

    slides: List[CarouselSlide]

    caption: str

    hashtags: List[str]


# ==========================================================
# INSTAGRAM REEL
# ==========================================================

class ReelScene(BaseModel):

    scene_number: int

    visual: str

    voiceover: str


class InstagramReelLLMOutput(BaseModel):

    hook: str

    scenes: List[ReelScene]

    caption: str

    hashtags: List[str]


class InstagramReelOutput(BaseModel):

    platform: str = "Instagram"

    format: str = "Reel"

    hook: str

    scenes: List[ReelScene]

    caption: str

    hashtags: List[str]


# ==========================================================
# LINKEDIN
# ==========================================================



class LinkedInLLMOutput(BaseModel):

    headline: str

    hook: str

    post: str

    hashtags: List[str]


class LinkedInOutput(BaseModel):

    platform: str = "LinkedIn"

    format: str

    headline: str

    hook: str

    post: str

    hashtags: List[str]

# ==========================================================
# REPURPOSE
# ==========================================================



class RepurposeOutput(BaseModel):

    instagram_carousel: Optional[Dict[str, Any]] = None

    instagram_reel: Optional[Dict[str, Any]] = None

    linkedin: Optional[Dict[str, Any]] = None

    blog: Optional[Dict[str, Any]] = None

    newsletter: Optional[Dict[str, Any]] = None

    twitter: Optional[Dict[str, Any]] = None

    facebook: Optional[Dict[str, Any]] = None

    threads: Optional[Dict[str, Any]] = None


# ==========================================================
# QUALITY
# ==========================================================

class QualityOutput(BaseModel):

    passed: bool

    score: int

    feedback: List[str]


# ==========================================================
# PIPELINE
# ==========================================================

class PipelineOutput(BaseModel):

    trend: Optional[TrendOutput] = None

    planner: Optional[PlannerOutput] = None

    format: Optional[FormatOutput] = None

    strategy: Optional[StrategyOutput] = None

    hooks: Optional[HookOutput] = None

    instagram_carousel: Optional[
        InstagramCarouselOutput
    ] = None

    instagram_reel: Optional[
        InstagramReelOutput
    ] = None

    linkedin: Optional[
        LinkedInOutput
    ] = None

    quality: Optional[
        QualityOutput
    ] = None

    repurpose: Optional[
        RepurposeOutput
    ] = None

    metadata: Optional[Dict[str, Any]] = None