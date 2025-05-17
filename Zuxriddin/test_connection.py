import psycopg2
from config import DB_CONFIG


def test_connection():
    try:
        print("Attempting to connect with DB_CONFIG:", DB_CONFIG)
        conn = psycopg2.connect(**DB_CONFIG)
        print("Connected to database successfully!")
        conn.close()
    except Exception as e:
        print("Connection failed:", e)


if __name__ == "__main__":
    test_connection()
