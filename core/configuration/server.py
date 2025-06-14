from fastapi import FastAPI

from .routers import __routers__


class Server:
    __app: FastAPI

    def __init__(self, app: FastAPI):
        self.__app = app
        self.__register_routes(app)

    def get_app(self) -> FastAPI:
        return self.__app

    @staticmethod
    def __register_routes(app: FastAPI) -> None:
        __routers__.register_routes(app)