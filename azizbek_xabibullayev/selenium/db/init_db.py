import psycopg2
from psycopg2 import Error
from typing import Optional
from utils.helper import *
from db.db_manager import get_db_connection
from utils.txt_saver import backup_to_json

def insert_content_card(
        content_type: str,
        title: str,
        image_url: str,
        text: str,
        publish_date: str,
        link: Optional[str] = None,
        tools_type: Optional[str] = None
) -> bool:
    valid_content_types = {"Post", "Project", "Certification"}
    if content_type not in valid_content_types:
        print(f"wrong content type.\nValid content types: {valid_content_types}")
        return False

    if not title or not image_url or not text:
        print("Error: Some data was not found.")
        return False
    try:
        formatted_date = parse_date(publish_date)
    except ValueError as e:
        print(e)
        return False

    connection = get_db_connection()
    if not connection:
        print("Error: while connecting to db.\ntrying save data to json file.")
        save_to_json = backup_to_json(content_type, title,image_url,text,publish_date,link,tools_type)
        print("data saved successful" if save_to_json else "something went wrong please try again")
        return False
    try:
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO content_cards (content_type, title, image_url, text, publish_date, link, tools_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (content_type, title, image_url, text, formatted_date, link, tools_type))
        connection.commit()
        print(f"'{title}' Added successful")
        return True

    except Error as e:
        print(f"Error while saving data: {e}")
        return False

    finally:
        cursor.close()
        connection.close()
