"""
Neuro Patient Tracker - Configuration Module

Handles environment variables and application settings.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings:
    """Application configuration settings."""
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    
    # Database Configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./neuro_tracker.db")
    
    # Application Settings
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # Output directories
    OUTPUT_DIR: str = "output"
    LOGS_DIR: str = "logs"


settings = Settings()
