import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Base config
PROJECT_NAME = "LookGlass Automation & Database"
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"

# Event Registry API
EVENT_REGISTRY_API_KEY = os.getenv("EVENT_REGISTRY_API_KEY")
EVENT_REGISTRY_ENDPOINT = "https://eventregistry.org/api/v1/article/getArticles"

# MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "lookglass")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "articles")

# Batch processing
DEFAULT_ARTICLE_BATCH_SIZE = 10

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "lookglass.log"

# Ensure necessary directories exist
LOG_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)