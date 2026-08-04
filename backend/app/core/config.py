from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "FraudShield AI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    HOST: str = "127.0.0.1"
    PORT: int = 8000

    GEMINI_API_KEY: str = ""
    VIRUSTOTAL_API_KEY: str = ""
    SAFE_BROWSING_API_KEY: str = ""
    URLSCAN_API_KEY: str = ""

    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()