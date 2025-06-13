from contextlib import asynccontextmanager

from fastapi import FastAPI

from config import server_settings
from logger.logger_builder import LoggerBuilder

logger = LoggerBuilder("LifeSpan").add_stream_handler().build()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Server start on {server_settings.host}:{server_settings.port}")
    yield
    logger.info("Server shutting down...")
