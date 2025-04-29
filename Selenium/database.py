import psycopg2

def save_to_db(title, public_date, image_url, description):
    title = title.encode('utf-8', errors='ignore').decode('utf-8')
    public_date = public_date.encode('utf-8', errors='ignore').decode('utf-8')
    description = description.encode('utf-8', errors='ignore').decode('utf-8')

    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="postgres",
            user="postgres",
            password="admin"
        )
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                public_date TEXT NOT NULL,
                image_url TEXT,
                description TEXT
            );
        """)

        cur.execute("""
            DELETE FROM projects
            WHERE title = %s AND public_date = %s;
        """, (title, public_date))

        cur.execute("""
            INSERT INTO projects (title, public_date, image_url, description)
            VALUES (%s, %s, %s, %s);
        """, (title, public_date, image_url, description))

        conn.commit()
        cur.close()
        conn.close()

        print("✅ Ma'lumotlar bazaga muvaffaqiyatli yozildi.")

    except Exception as e:
        print(f"❌ Bazaga yozishda xatolik: {e}")
