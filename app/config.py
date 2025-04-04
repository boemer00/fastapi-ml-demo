from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import os
from pathlib import Path

# Get the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    # API settings
    API_KEY: str = Field(
        "test-api-key",
        description="API key for authentication",
        json_schema_extra={"env_name": "API_KEY"}
    )
    ENVIRONMENT: str = "development"

    # Model settings
    MODEL_DIR: str = str(BASE_DIR / "app" / "models")
    MODEL_FILENAME: str = "iris_model.joblib"

    # Use SettingsConfigDict instead of the inner Config class
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

# Create settings instance
settings = Settings()

# Ensure model directory exists
os.makedirs(settings.MODEL_DIR, exist_ok=True)
