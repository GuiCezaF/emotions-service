from fastapi import FastAPI

from app.routes import emotions_route, health_route
from app.settings import bool_env, envs

DEBUG = bool_env(envs("DEBUG", default="false"))

app = FastAPI(debug=DEBUG)

app.include_router(health_route.router, prefix="/health", tags=["Health"])
app.include_router(emotions_route.router, prefix="/emotions", tags=["Emotions"])