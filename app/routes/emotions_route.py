from fastapi import APIRouter

from app.services.emotion_service import EmotionService
from app.types.emotions_request import EmotionRequest


router = APIRouter()
service = EmotionService()

# @router.post("/", response_model=EmotionResponse)
@router.post("/detect")
def detect_emotion(data: EmotionRequest):
    return service.process_emotion(data)
