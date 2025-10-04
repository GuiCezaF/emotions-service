import asyncio
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager

from app.core.consumer import consume_frames
from app.routes import health_route
from app.settings import bool_env, envs

DEBUG = bool_env(envs("DEBUG", default="false"))

@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(consume_frames())
    print("Consumer task started")
    try:
        yield
    finally:
        task.cancel()
        print("Consumer task cancelled")

app = FastAPI(debug=DEBUG, lifespan=lifespan)

app.include_router(health_route.router, prefix="/health", tags=["Health"])

