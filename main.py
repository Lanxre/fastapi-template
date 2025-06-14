import asyncio

import uvicorn
from fastapi import FastAPI

from config import server_settings
from core.configuration.server import Server
from core.internal.events.lifespan import lifespan


def create_app() -> FastAPI:
    application = FastAPI(lifespan=lifespan)
    return Server(app=application).get_app()


async def main():
    config = uvicorn.Config(
        app=create_app(),
        host=server_settings.host,
        port=server_settings.port
    )

    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())