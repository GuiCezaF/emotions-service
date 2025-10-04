import redis.asyncio as aioredis

# Conexão única para toda a app
redis = aioredis.from_url("redis://redis:6379", decode_responses=True)

REDIS_LIST = "emotion_frames"
REDIS_CHANNEL = "emotion_results"
