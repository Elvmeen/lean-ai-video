from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import uuid4

@dataclass
class VideoJob:
    id: str
    status: str
    video_url: str | None = None
    message: str | None = None

class VideoProvider(ABC):
    @abstractmethod
    async def generate(self, prompt: str, aspect_ratio: str, duration: int) -> VideoJob: ...

    @abstractmethod
    async def status(self, job_id: str) -> VideoJob: ...

class MockVideoProvider(VideoProvider):
    async def generate(self, prompt: str, aspect_ratio: str, duration: int) -> VideoJob:
        return VideoJob(id=str(uuid4()), status="queued", message="Provider ready. Connect a real video API key to generate.")

    async def status(self, job_id: str) -> VideoJob:
        return VideoJob(id=job_id, status="queued", message="Waiting for a configured provider.")


def get_video_provider() -> VideoProvider:
    # V1 defaults safely to mock. Plug fal/Veo/etc. here without touching the UI/routes.
    return MockVideoProvider()
