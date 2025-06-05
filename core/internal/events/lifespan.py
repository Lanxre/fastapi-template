from fastapi import FastAPI
from contextlib import asynccontextmanager
from config import server_settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Server start on {server_settings.host}:{server_settings.port}")
    yield
    print("Server shutting down...")