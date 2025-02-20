import os
from dotenv import load_dotenv

# Load environment variables from .env file in the project root.
load_dotenv()

class Config:
    # Flask settings
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    
    # Database connection string.
    # For PostgreSQL use:
    #   postgresql://username:password@host:port/database
    # For MySQL use (if you switch to a MySQL connector):
    #   mysql://username:password@host:port/database
    DATABASE_URL = os.getenv("DATABASE_URL")
    
    # Google Cloud Pub/Sub configuration
    GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
    PUBSUB_TOPIC = os.getenv("PUBSUB_TOPIC")
    PUBSUB_SUBSCRIPTION = os.getenv("PUBSUB_SUBSCRIPTION")
    
    @staticmethod
    def init_app(app):
        # Place for additional initialization if needed
        pass