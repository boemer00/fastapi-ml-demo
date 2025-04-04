from pydantic import Field
from pydantic_settings import BaseSettings
import os
from pathlib import Path

# Get the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    # API settings
    API_KEY: str = Field("test-api-key", env="API_KEY")
    ENVIRONMENT: str = "development"

    # Model settings
    MODEL_DIR: str = str(BASE_DIR)  # Look in project root instead of app/models
    MODEL_FILENAME: str = Field("iris_model.joblib", env="MODEL_FILE")

    class Config:
        env_file = ".env"
        case_sensitive = True

# Create settings instance
settings = Settings()

# Ensure model directory exists
os.makedirs(settings.MODEL_DIR, exist_ok=True)
