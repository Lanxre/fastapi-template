from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_file_encoding="utf-8"
    )

    @classmethod
    def load(cls) -> "ServerSettings":
        return cls()

class ServerSettings(ConfigBase):
    model_config = ConfigBase.model_config | SettingsConfigDict(env_prefix="server_")

    host: str
    port: int
    

class DatabaseSettings(ConfigBase):
    model_config = ConfigBase.model_config | SettingsConfigDict(env_prefix="db_")

    name: str
    user: str
    password: str

    @property
    def postgresql_url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@localhost:5432/{self.name}"


server_settings = ServerSettings.load()
database_settings = DatabaseSettings.load()