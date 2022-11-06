import psycopg2
from psycopg2.extras import RealDictCursor

try:
    conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Pretender93*',
                            cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection was successful!")
except Exception as error:
    print("Connecting to database failed")
    print(error)


def create_table():
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS players (
        player_id SERIAL PRIMARY KEY,
        player_name VARCHAR(255) NOT NULL,
        player_age INTEGER NOT NULL,
        player_nationality VARCHAR(255) NOT NULL,
        player_rating INTEGER NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW());
    """)
    conn.commit()

