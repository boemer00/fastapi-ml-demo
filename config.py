from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # Use appropriate defaults for CI/testing environments
    API_KEY: str = Field("test-api-key", env="API_KEY")
    ENVIRONMENT: str = "development"
    MODEL_FILE: str = "iris_model.joblib"

    # Add Vercel-related settings
    VERCEL_TOKEN: str = Field("", env="VERCEL_TOKEN")
    VERCEL_ORG_ID: str = Field("", env="VERCEL_ORG_ID")
    VERCEL_PROJECT_ID: str = Field("", env="VERCEL_PROJECT_ID")

    class Config:
        env_file = ".env"
        case_sensitive = True

# Create settings instance
settings = Settings()
