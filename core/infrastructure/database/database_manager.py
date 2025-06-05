from typing import AsyncGenerator, Callable, Dict, Type, TypeVar

from fastapi import Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config import DatabaseSettings, database_settings

T = TypeVar("T")


class DatabaseManager:
    def __init__(
        self,
        config: DatabaseSettings,
        echo: bool = False,
        repositories: list[Type] = None,
    ):
        self.engine = self.create_engine(config, echo=echo)
        self.session_pool = self.create_session_pool()
        self._repository_registry: Dict[str, Type] = {}
        if repositories:
            for repo_class in repositories:
                self.register_repository(repo_class)

    @staticmethod
    def create_engine(config: DatabaseSettings, echo: bool = False) -> AsyncEngine:
        try:
            engine = create_async_engine(
                config.postgresql_url,
                echo=echo,
            )
            return engine
        except Exception as e:
            raise

    def create_session_pool(self) -> async_sessionmaker[AsyncSession]:
        session_pool = async_sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )
        return session_pool

    async def get_db_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Provide an AsyncSession for database operations."""
        async with self.session_pool() as session:
            try:
                yield session
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise
            except Exception as e:
                await session.rollback()
                raise

    def register_repository(self, repository_class: Type[T]) -> None:
        """Register a repository class for dynamic instantiation."""
        if not hasattr(repository_class, "__name__"):
            raise ValueError("Repository class must have a __name__ attribute")
        self._repository_registry[repository_class.__name__] = repository_class

    def get_repository(self, repository_class: Type[T], session: AsyncSession) -> T:
        """Get an instance of the specified repository class with the given session."""
        repo_class = self._repository_registry.get(repository_class.__name__)
        if not repo_class:
            raise ValueError(f"Repository {repository_class.__name__} not registered")
        return repo_class(session)

    def get_repo(self, repository_class: Type[T]) -> Callable[[AsyncSession], T]:
        """Create a dependency that returns a repository instance for the given class."""

        def dependency(session: AsyncSession = Depends(self.get_db_session)) -> T:
            return self.get_repository(repository_class, session)

        return dependency

    def get_registered_repositories(self) -> list[str]:
        """Return a list of registered repository names."""
        return list(self._repository_registry.keys())


db_manager = DatabaseManager(
    database_settings,
    echo=True,
    repositories=[],
)
