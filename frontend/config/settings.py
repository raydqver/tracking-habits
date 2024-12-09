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


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )
    db: DBSettings = DBSettings()
    bot: BotSettings = BotSettings()


settings = Settings()
