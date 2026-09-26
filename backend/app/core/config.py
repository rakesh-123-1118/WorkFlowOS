from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "WorkFlowOS"
    environment: str = "development"
    debug: bool = True
    mongo_uri: str = "mongodb://admin:password@localhost:27017/workflowos?authSource=admin"
    mongo_db_name: str = "workflowos"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
