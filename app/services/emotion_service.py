from fer import FER
from app.utils.base64 import base64_to_image
from app.types.emotions_request import EmotionRequest
from app.types.emotions_response import EmotionResponse


class EmotionService:
    def __init__(self):
        self._detector = FER(mtcnn=True)

    def process_emotion(self, data: EmotionRequest) -> EmotionResponse:
        try:
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

            return response.model_dump_json()

        except Exception as e:
            raise Exception(f"Error processing emotion: {e}")
