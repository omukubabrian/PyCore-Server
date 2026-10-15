import os

import mysql.connector
from dotenv import load_dotenv

# Load database settings from .env
load_dotenv()


def get_db_connection(database_name=None):
    """Create and return a MySQL database connection."""
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=database_name or os.getenv("DB_NAME")
    )

    return connection