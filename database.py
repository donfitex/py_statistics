import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "bincom_test"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
    )

def save_colour_frequencies(colour_frequencies):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS colour_frequency (
                    id SERIAL PRIMARY KEY,
                    colour VARCHAR(50) UNIQUE NOT NULL,
                    frequency INTEGER NOT NULL CHECK (frequency >= 0)
                );
            """)
            for colour, frequency in colour_frequencies.items():
                cursor.execute("""
                    INSERT INTO colour_frequency (colour, frequency)
                    VALUES (%s, %s)
                    ON CONFLICT (colour)
                    DO UPDATE SET frequency = EXCLUDED.frequency;
                """, (colour, frequency))
        connection.commit()
    finally:
        connection.close()
