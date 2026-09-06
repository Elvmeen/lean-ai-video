import httpx
from app.config import settings

async def enhance_prompt(prompt: str) -> str:
    if not settings.gemini_api_key:
        return prompt.strip()
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    params = {"key": settings.gemini_api_key}
    body = {
        "contents": [{"parts": [{"text": (
            "Rewrite this as one concise cinematic AI video prompt. Preserve intent, add camera, lighting, motion and visual detail. Return only the prompt.\n\n" + prompt
        )}]}]
    }
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(url, params=params, json=body)
        r.raise_for_status()
        data = r.json()
    return data["candidates"][0]["content"]["parts"][0]["text"].strip()
