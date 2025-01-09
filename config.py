from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

class Settings:
    SQLITE_DB_PATH = "database.sqlite"  # Path to SQLite database file
    DATABASE_URL = f"sqlite:///{SQLITE_DB_PATH}"  # SQLite connection string

    EMAIL_SENDER: str = os.getenv("EMAIL_SENDER")
    EMAIL_PASSWORD: str = os.getenv("EMAIL_PASSWORD")
    EMAIL_RECIPIENT: str = os.getenv("EMAIL_RECIPIENT")

settings = Settings()

logger.info(f"EMAIL_SENDER: {settings.EMAIL_SENDER}")
logger.info(f"EMAIL_PASSWORD: {settings.EMAIL_PASSWORD}")