from core.internal.routers import default_router

from .router import Routes

__routers__ = Routes(routers=(default_router.router,))