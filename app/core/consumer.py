import asyncio
import json
from app.core.redis import redis, REDIS_LIST, REDIS_CHANNEL
from app.services.emotion_service import EmotionService


async def consume_frames():
    """Loop para consumir frames da lista no Redis e responder no canal Pub/Sub"""
    service = EmotionService()
    while True:
        try:
            frame = await redis.brpop(REDIS_LIST, timeout=5)
            if frame:
                _, payload = frame
                data = json.loads(payload)

                result = service.process_emotion(data)
                await redis.publish(REDIS_CHANNEL, result)

        except Exception as e:
            print(f"[FastAPI] Erro no consumo: {e}")
            await asyncio.sleep(1)
