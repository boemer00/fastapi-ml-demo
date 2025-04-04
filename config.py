from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    API_KEY: str = Field("test_api_key_for_ci", env="API_KEY")
    ENVIRONMENT: str = "development"
    MODEL_FILE: str = "iris_model.joblib"

    class Config:
        env_file = ".env"
        case_sensitive = True

# Create settings instance
settings = Settings()
