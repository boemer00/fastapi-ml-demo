from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pathlib import Path

# Get the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    # API settings
    API_KEY: str = "test-api-key"
    ENVIRONMENT: str = "development"

    # Model settings
    MODEL_DIR: str = str(BASE_DIR)  # Look in project root instead of app/models
    MODEL_FILENAME: str = "iris_model.joblib"

    # Using modern Pydantic V2 config approach
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        env_file_encoding='utf-8',
        extra='ignore'
    )

# Create settings instance
settings = Settings()

# Ensure model directory exists
os.makedirs(settings.MODEL_DIR, exist_ok=True)
