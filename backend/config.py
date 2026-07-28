import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Application configuration for Malawi Agri Advisor.
    """

    APP_NAME = "Malawi Agri Advisor"
    APP_VERSION = "1.0.0"

    # OpenWeather
    OPENWEATHER_API_KEY = os.getenv(
        "OPENWEATHER_API_KEY"
    )

    # Groq
    GROQ_API_KEY = os.getenv(
        "GROQ_API_KEY"
    )

    # AI request timeout
    AI_TIMEOUT = 60
