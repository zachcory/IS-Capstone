import psycopg2
from config import Config

def get_db_connection():
    # Connect to the PostgreSQL database using the URL provided in .env
    conn = psycopg2.connect(Config.DATABASE_URL)
    return conn