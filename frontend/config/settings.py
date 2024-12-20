from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class DBSettings(BaseSettings):
    db_name: str
    echo: bool = False

    @property
    def url(self) -> str:
        """
        Возвращает строку для подключения к базе данных.
        """
        return f"sqlite:///{self.db_name}.sqlite3"


class BotSettings(BaseSettings):
    token: str


class RedisSettings(BaseSettings):
    redis_host: str


class ApiSettings(BaseSettings):
    api_host: str
    port: int

    @property
    def url(self):
        return f"{self.api_host}:{self.port}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )
    db: DBSettings = DBSettings()
    bot: BotSettings = BotSettings()
    redis: RedisSettings = RedisSettings()
    api: ApiSettings = ApiSettings()


settings = Settings()
