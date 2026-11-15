# WholeBite AI Agency

## Multi-Agent AI Content Strategy & Creative Production

An AI-powered application developed to support social media content strategy and production for a health, nutrition and wellness brand.

## Live Brand & Social Presence

- Instagram: [@the.wholebite](https://www.instagram.com/the.wholebite/)
- LinkedIn: [The Whole Bite](https://www.linkedin.com/in/the-whole-bite-753697402/)

## Project Overview

The application uses a multi-agent workflow to generate content strategies, hooks, captions and platform-specific content for Instagram and LinkedIn.

Application-generated content was used as the creative foundation for real-world social media publishing. Visual assets were subsequently generated based on the content and published on the brand's social media profiles.

## Active Architecture

- `app/main.py` - FastAPI application
- `app/pipelines/content_pipeline.py` - Main content pipeline
- `app/agents/` - Active AI agent system
- `app/services/llm.py` - Local LLM integration

## Agent Workflow

- Trend collection
- Audience selection
- Content planning
- Strategy generation
- Hook generation
- Content generation
- Format refinement

## Technology Stack

- Python
- FastAPI
- Pydantic
- Ollama
- Llama 3
- Phi-3
- PyTrends
- APScheduler

## Local Setup

1. Clone the repository:

   `git clone https://github.com/raverer/wholebite-ai-agency.git`

2. Enter the project:

   `cd wholebite-ai-agency`

3. Create a virtual environment:

   `python3 -m venv venv`

4. Activate it:

   `source venv/bin/activate`

5. Install dependencies:

   `pip install -r requirements.txt`

6. Install Ollama separately and download models:

   `ollama pull llama3`

   `ollama pull phi3`

7. Start the API:

   `uvicorn app.main:app --reload`

8. Open API documentation:

   `http://127.0.0.1:8000/docs`

## Project Status

The original `app/agents/` pipeline has passed an initial FastAPI generation test using local Ollama models.

Further work includes improving trend relevance, audience preservation, brand adaptability and content quality.

## Author

Rajib Rawal
