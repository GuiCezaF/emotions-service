from datetime import datetime
from pydantic import BaseModel

class EmotionRequest(BaseModel):

  correlation_id: str
  timestamp: datetime
  frame: str  # Base64 encoded image frame

