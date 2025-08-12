from fastapi import FastAPI

from app.settings import bool_env, envs

DEBUG = bool_env(envs("DEBUG", default="false"))

app = FastAPI(debug=DEBUG)

@app.get("/")
def read_root():
    return {"msg": "Hello FastAPI + Alembic"}
