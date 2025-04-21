from psycopg2 import Error
from typing import List, Dict
from db.db_manager import get_db_connection
from utils.json_saver import backup_missing_data_to_json


def table_checker() -> bool:
    connection = get_db_connection()
    if not connection:
        print("Error: Failed to connect to database.")
        return False

    cursor = None
    try:
        cursor = connection.cursor()
        check_table_query = """
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_schema = 'public' AND table_name = 'content_cards'
            );
        """
        cursor.execute(check_table_query)
        table_exists = cursor.fetchone()[0]

        if table_exists:
            return True

        print("content_cards table does not exist. Creating new table...")
        create_table_query = """
            CREATE TABLE content_cards (
                id SERIAL PRIMARY KEY,
                content_type VARCHAR(50) NOT NULL,
                title TEXT NOT NULL,
                image_url TEXT NOT NULL,
                text TEXT NOT NULL,
                publish_date TEXT NOT NULL,
                link TEXT,
                tools_type TEXT
            );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully.")
        return True

    except Error as e:
        print(f"Error checking or creating table: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def insert_content_cards(content_list: List[Dict]) -> None:
    if not content_list:
        print("Error: Content list is empty.")
        return

    if not table_checker():
        print("Error: Database table setup failed. Process ended.")
        return

    valid_content_types = {"post", "projects", "certifications"}
    missing_data = {}

    connection = get_db_connection()
    if not connection:
        print("Error: Failed to connect to database. Saving all data to JSON.")
        for content in content_list:
            missing_data[content["title"]] = content
        if missing_data:
            backup_missing_data_to_json(missing_data)
        return

    cursor = None
    success_count = 0
    content_type = ''
    try:
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO content_cards (content_type, title, image_url, text, publish_date, link, tools_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """

        for content in content_list:
            content_type = content.get('content_type', '').lower()
            title = content.get('title')
            image_url = content.get('image_url')
            text = content.get('text')
            publish_date = content.get('publish_date')
            link = content.get('link')
            tools_type = content.get('tools_type')

            if content_type not in valid_content_types:
                print(f"Error: Invalid content type '{content_type}' for '{title}'. Valid types: {valid_content_types}")
                missing_data[title] = content
                continue

            if not all([title, image_url, text, publish_date]):
                print(f"Error: Missing required fields for '{title}'")
                missing_data[title] = content
                continue

            try:
                cursor.execute(insert_query, (content_type, title, image_url, text, publish_date, link, tools_type))
                connection.commit()
                success_count += 1
            except Error as e:
                print(f"Error saving '{title}': {e}")
                missing_data[title] = content
                connection.rollback()

    except Error as e:
        print(f"Database error: {e}")
        connection.rollback()
    finally:
        if success_count > 0:
            print(f"{content_type} - successfully saved {success_count} records.")
        else:
            print("No records were saved successfully.")
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    if missing_data:
        print("Missing data found. Saving to JSON.")
        if backup_missing_data_to_json(missing_data):
            print("Missing data saved successfully to JSON.")
        else:
            print("Failed to save missing data to JSON.")
