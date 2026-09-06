from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.gemini import enhance_prompt
from app.services.video_provider import get_video_provider

router = APIRouter(prefix="/api")
provider = get_video_provider()

class PromptBody(BaseModel):
    prompt: str = Field(min_length=3, max_length=2000)

class GenerateBody(PromptBody):
    aspect_ratio: str = "9:16"
    duration: int = Field(default=5, ge=3, le=15)
    enhance: bool = True

@router.post("/enhance")
async def enhance(body: PromptBody):
    return {"prompt": await enhance_prompt(body.prompt)}

@router.post("/generate")
async def generate(body: GenerateBody):
    prompt = await enhance_prompt(body.prompt) if body.enhance else body.prompt.strip()
    if body.aspect_ratio not in {"9:16", "16:9", "1:1"}:
        raise HTTPException(400, "Unsupported aspect ratio")
    job = await provider.generate(prompt, body.aspect_ratio, body.duration)
    return {"id": job.id, "status": job.status, "prompt": prompt, "message": job.message}

@router.get("/jobs/{job_id}")
async def job(job_id: str):
    result = await provider.status(job_id)
    return result.__dict__

@router.get("/health")
async def health():
    return {"ok": True}
