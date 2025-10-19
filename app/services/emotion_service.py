import uuid
from fer import FER
from app.db.database import SessionLocal
from app.models.emotion import Emotion
from app.types.modality_enum import ModalityEnum
from app.utils.base64 import base64_to_image
from app.types.emotions_request import EmotionRequest
from app.types.emotions_response import EmotionResponse
from sqlalchemy.exc import SQLAlchemyError

class EmotionService:
    def __init__(self):
        self._detector = FER(mtcnn=True)

    def process_emotion(self, data: EmotionRequest) -> EmotionResponse:
        try:
            db = SessionLocal()
            
            user_id = data.get("correlation_id", None)
            timestamp = data.get("timestamp", None)
            frame = data.get("frame", None)
            
            image = base64_to_image(frame)
            emotions = self._detector.detect_emotions(image)

            if not emotions:
                res = EmotionResponse(
                    user_id=user_id,
                    timestamp=timestamp,
                    emotion="unknown",
                    confidence=0.0
                )
                return res.model_dump_json()

            emotion_response = emotions[0].get("emotions", {})

            dominant_emotion = max(emotion_response, key=emotion_response.get)

            confidence_score = emotion_response[dominant_emotion]
            
            response = EmotionResponse(
                user_id=user_id,
                timestamp=timestamp,
                emotion=dominant_emotion,
                confidence=confidence_score
            )
            
            emotion_entry = Emotion(
                id=uuid.uuid4(),
                user_id=user_id,
                modality=ModalityEnum.video,
                emotion=dominant_emotion,
                confidence=confidence_score,
                timestamp=timestamp
            )
            
            db.add(emotion_entry)
            db.commit()
            db.refresh(emotion_entry)

            return response.model_dump_json()
        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database error: {e}")
        except Exception as e:
            raise Exception(f"Error processing emotion: {e}")

        finally:
            db.close()
