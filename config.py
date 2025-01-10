from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

class Settings:
    SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "database.sqlite")  # Path to SQLite database file
    DATABASE_URL = f"sqlite:///{SQLITE_DB_PATH}"  # SQLite connection string

    EMAIL_SENDER: str = os.getenv("EMAIL_SENDER")
    SENDGRID_API_KEY: str = os.getenv("SENDGRID_API_KEY")
    EMAIL_RECIPIENT: str = os.getenv("EMAIL_RECIPIENT")

settings = Settings()

logger.info(f"EMAIL_SENDER: {settings.EMAIL_SENDER}")
logger.info(f"SENDGRID_API_KEY: {settings.SENDGRID_API_KEY}")
logger.info(f"EMAIL_RECIPIENT: {settings.EMAIL_RECIPIENT}")
