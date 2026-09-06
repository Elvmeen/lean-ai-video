# Lean Video

A deliberately lean AI-video web app foundation: public generation without auth, optional account area, pluggable video providers, Gemini prompt enhancement, sharing hooks, and scheduling-ready architecture.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000

## Current behavior

The UI and job API are working. `VIDEO_PROVIDER=mock` is intentionally the default so no paid generation is accidentally triggered. Add a provider implementation under `app/services/` and switch it in `get_video_provider()`.

## Architecture

- FastAPI backend
- Jinja + vanilla JS frontend (no frontend build step)
- Public no-auth generator
- Optional `/app` library/dashboard shell
- Gemini prompt-enhancement hook
- Provider abstraction for fal/Veo/Wan/etc.
- Native Web Share support
- Render deployment blueprint
- Supabase/Cloudinary environment placeholders

## Next integrations

1. Real video provider adapter
2. Supabase auth + metadata persistence
3. Cloudinary video storage
4. OAuth publishing adapters (YouTube/TikTok/Meta)
5. Scheduled publishing worker/cron endpoint

No secrets should be committed. Use environment variables only.
