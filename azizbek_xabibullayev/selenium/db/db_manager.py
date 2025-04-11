import  psycopg2
from psycopg2 import Error
from db.config import DATABASE

def get_db_connection():
    try:
        connection = psycopg2.connect(
            user=DATABASE["user"],
            password=DATABASE["password"],
            host=DATABASE["host"],
            port=DATABASE["port"],
            dbname=DATABASE["dbname"]
        )
        return connection
    except Error as e:
        print(f"Error while connecting to DB: {e}")
        return None