from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class EmotionResponse(BaseModel):
    user_id: UUID
    timestamp: datetime
    emotion: str
    confidence: float
