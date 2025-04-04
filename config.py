from pydantic import BaseSettings

class Settings(BaseSettings):
    API_KEY: str = "dummy_key_for_testing"  # Provide a default value
    ENVIRONMENT: str = "development"
    MODEL_FILE: str = "iris_model.joblib"

    class Config:
        env_file = ".env"
        case_sensitive = True

# Create settings instance
settings = Settings()
