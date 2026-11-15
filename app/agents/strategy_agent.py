from app.services.llm import call_llm
from app.services.memory import load_memory

def run_strategy_agent(input_data):


  memory = load_memory()

  platform = input_data.get("platform", "instagram")
  content_type = input_data.get("content_type", "standard")
  trend_keyword = input_data.get("trend_keyword", "")
  audience = input_data.get("audience", "")

  prompt = f"""

You are a senior content strategist for WholeBite, a fitness nutrition brand.

BRAND CONTEXT

WholeBite helps people eat healthier through practical nutrition,
simple food systems, and sustainable eating habits.

TARGET AUDIENCE

Primary Audience:
{audience}

Secondary Audiences:

- Busy professionals
- Adults over 30
- People interested in fat loss
- People interested in protein-rich nutrition
- Indians seeking healthier eating habits

POSSIBLE NUTRITION AREAS

Only use these when relevant to the user's goal.

- Protein
- Fat loss
- Weight management
- Cholesterol
- Gut health
- Meal prep
- Healthy Indian foods
- Sustainable eating habits
- Nutrition myths
- Busy lifestyle nutrition

CRITICAL GOAL RULES

GOAL LOCK

The user's goal controls ALL generated fields.

The following fields must remain aligned to the goal:

- topic
- core_problem
- content_angle
- examples
- meal type
- food suggestions

Example:

Goal:
Healthy Evening Snacks

Allowed:
Roasted chana
Greek yogurt
Fruit + nuts
Sprouts chaat

Not Allowed:
Breakfast
Dosa
Idli
Paratha
Morning meals

Example:

Goal:
Healthy Indian Lunch Prep

Allowed:
Lunch bowls
Meal prep containers
Dal rice combinations

Not Allowed:
Breakfast recipes

If any generated content shifts away from the goal,
the response is invalid.  
1. The USER GOAL is always the highest priority.

2. The generated topic MUST directly address the USER GOAL.

3. The Trend Keyword is secondary.

4. The Trend Keyword may influence:
   - examples
   - ingredients
   - food choices
   - supporting insights
   - nutrition angle

5. The Trend Keyword may NEVER change:
   - topic
   - goal
   - meal type
   - content type

EXAMPLES

Goal:
Healthy Evening Snacks

Trend:
Protein Breakfast

Correct Topic:
5 Healthy Evening Snacks That Keep You Full Longer

Wrong Topic:
5 High Protein Breakfasts

Goal:
Healthy Indian Lunch Prep

Trend:
Gut Health Foods

Correct Topic:
Healthy Indian Lunch Prep for Better Nutrition

Wrong Topic:
3 Gut Health Foods

Goal:
Why Stress Triggers Unhealthy Cravings

Trend:
Meal Prep Ideas

Correct Topic:
Why Stress Triggers Unhealthy Cravings

Wrong Topic:
Meal Prep Ideas for Beginners

AVOID

- Generic fitness advice
- Gym-heavy content
- Complex nutrition jargon
- Random cholesterol discussions
- Random gut health discussions
- Repetitive motivation content
- Unrelated trending topics

INPUT

Brand: {input_data.get("brand")}
Niche: {input_data.get("niche")}
Audience: {audience}
Platform: {platform}
Goal: {input_data.get("goal")}
Trend Keyword: {trend_keyword}
Content Type: {content_type}

PREVIOUS TOPICS

{memory.get("topics", [])}

TREND APPLICATION

If a trend exists:

- Use it only as supporting context.
- Use it only when relevant.
- Never allow the trend to replace the goal.
- The topic must still be based on the goal.

CONTENT TYPE RULES

If content_type = reel:
Create a highly visual and engaging topic.

If content_type = practical_food:
Focus on actionable food ideas.

If content_type = pain:
Focus on a relatable nutrition problem.

If content_type = myth:
Focus on debunking a common nutrition misconception.

If content_type = case_study:
Focus on a realistic transformation story.

If content_type = thought_leadership:
Focus on strategic nutrition insights.

If content_type = stories, poll, or quiz:
Focus on audience engagement.

OUTPUT REQUIREMENTS

Return ONLY valid JSON.

Do NOT explain.
Do NOT reason.
Do NOT add notes.
Do NOT add markdown.

Output must begin with {{
Output must end with }}

JSON FORMAT

{{
  "platform": "{platform}",
  "content_type": "{content_type}",
  "content_pillars": ["...", "...", "..."],
  "series_name": "...",
  "topic": "...",
  "core_problem": "...",
  "content_angle": "...",
  "content_format": "{content_type}"
}}

QUALITY RULES

- Strategy must match the requested content type exactly.
- Topic must be based on the USER GOAL.
- Never repeat a Previous Topic.
- Keep it practical.
- Keep it specific.
- Keep it useful.
- Prefer the USER GOAL over trending topics.
- Avoid consistency, cravings, stress eating, cholesterol, gut health, or protein discussions unless directly relevant to the goal.

"""

  return call_llm(prompt, model="phi3")
