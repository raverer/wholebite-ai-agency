from fastapi import FastAPI
from pydantic import BaseModel
from app.pipelines.content_pipeline import run_content_pipeline

app = FastAPI()


# 🔹 Input Schema (THIS CREATES INPUT BOX IN /docs)
from typing import Optional

class ContentInput(BaseModel):
    brand: str
    niche: str
    audience: Optional[str] = None
    platform: str
    goal: str
    content_type: str

@app.get("/")
def home():
    return {"message": "AI Agency Running"}


# 🔹 Dynamic endpoint
@app.post("/generate")
def generate_content(input_data: ContentInput):

    result = run_content_pipeline(input_data.dict())

    return result