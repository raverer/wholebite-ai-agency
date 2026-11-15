from app.services.llm import call_llm


def run_format_agent(input_data, planner_output):

    prompt = f"""
You are the Creative Director of WholeBite.

Your ONLY responsibility is deciding the BEST content format.

DO NOT write captions.
DO NOT write content.
DO NOT write hooks.
DO NOT write strategy.

--------------------------------------------------

INPUT

Platform:
{input_data.get("platform")}

Goal:
{input_data.get("goal")}

Content Type:
{input_data.get("content_type")}

Audience:
{input_data.get("audience")}

Trend Keyword:
{input_data.get("trend_keyword")}

Planner Recommendation:
{planner_output}

--------------------------------------------------

AVAILABLE FORMATS

Instagram

- Reel
- Carousel
- Static Post
- Story

LinkedIn

- Thought Leadership
- Case Study
- Story
- Educational Post
- Poll
- Document

--------------------------------------------------

FORMAT SELECTION RULES

Instagram

Use Reel when:

- meal prep
- recipes
- food demonstrations
- grocery shopping
- before/after
- transformations
- quick tips
- practical food
- trending topics
- habits
- "how to"

Use Carousel when:

- myths
- educational
- lists
- mistakes
- comparisons
- pain points
- step-by-step
- psychology
- nutrition education

Use Static Post when:

- quotes
- reminders
- announcements
- promotions

Use Story when:

- polls
- quizzes
- engagement
- behind the scenes

--------------------------------------------------

LinkedIn

Thought Leadership

- opinions
- productivity
- leadership
- nutrition philosophy

Case Study

- transformation
- success stories
- client examples

Educational

- explain concepts
- myths
- science
- frameworks

Poll

- engagement

Document

- long educational guides

--------------------------------------------------

Return ONLY valid JSON.

{{
    "primary_format":"...",
    "secondary_format":"...",
    "reason":"...",
    "estimated_engagement":"Low | Medium | High",
    "recommended_length":"...",
    "visual_priority":"Low | Medium | High"
}}

NO markdown.

NO explanation.

ONLY JSON.
"""

    return call_llm(
        prompt,
        model="phi3"
    )