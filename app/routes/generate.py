from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from app.services.orchestrator import run_workflow

router = APIRouter()


class BrandInput(BaseModel):
    name: str
    niche: str
    target_audience: str
    tone: str
    platform: Optional[str] = "instagram"
    content_goal: Optional[str] = "general"
    content_type: Optional[str] = "carousel"


class GenerateRequest(BaseModel):
    brand: Optional[BrandInput] = None


@router.post("/generate")
def generate(request: GenerateRequest):

    # If new structure
    if request.brand:
        return run_workflow(request.brand.dict())

    # fallback (old format)
    return run_workflow(request.dict())
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from app.services.orchestrator import run_workflow

router = APIRouter()


class BrandInput(BaseModel):
    name: str
    niche: str
    target_audience: str
    tone: str
    platform: Optional[str] = "instagram"
    content_goal: Optional[str] = "general"
    content_type: Optional[str] = "carousel"


class GenerateRequest(BaseModel):
    brand: Optional[BrandInput] = None


@router.post("/generate")
def generate(request: GenerateRequest):

    # If new structure
    if request.brand:
        return run_workflow(request.brand.dict())

    # fallback (old format)
    return run_workflow(request.dict())