import time
import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver, WebDriverWait(driver, 30)


def click_element(driver, wait, by, value, scroll=False):
    element = wait.until(EC.element_to_be_clickable((by, value)))
    if scroll:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
    element.click()
    return element


def extract_project_data(driver, wait):
    try:
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".project-header h1"))).text
    except:
        print("❌ Title topilmadi.")
        print("📍 Hozirgi URL:", driver.current_url)
        print(driver.page_source[:1000])  # Sahifa preview
        raise

    date_range = driver.find_element(By.CSS_SELECTOR, ".project-date").text.strip()
    type_badge = driver.find_element(By.CSS_SELECTOR, ".type-badge").text.strip()
    public_date = f"{date_range} | {type_badge}"

    image_url = driver.find_element(By.CSS_SELECTOR, ".project-featured-image img").get_attribute("src")

    project_description = driver.find_element(By.CSS_SELECTOR, ".project-description").text.strip()

    technologies = driver.find_elements(By.CSS_SELECTOR, ".technology-item span")
    tech_list = [tech.text for tech in technologies]
    tech_string = "\n- " + "\n- ".join(tech_list)

    links = driver.find_elements(By.CSS_SELECTOR, ".project-links a")
    link_string = ""
    for link in links:
        label = link.text.replace("\n", " ").strip()
        href = link.get_attribute("href")
        link_string += f"- {label}: {href}\n"

    description = f"""Project Description:
{project_description}

Technologies Used:{tech_string}

Links:
{link_string}"""

    return title, public_date, image_url, description


def save_to_db(title, public_date, image_url, description):
    conn = psycopg2.connect(
        host="localhost",
        database="Database_name",
        user="User",
        password="Password"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS table_name (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            public_date TEXT NOT NULL,
            image_url TEXT,
            description TEXT
        );
    """)

    cur.execute("""
        DELETE FROM table_name
        WHERE title = %s AND public_date = %s;
    """, (title, public_date))

    cur.execute("""
        INSERT INTO table_name (title, public_date, image_url, description)
        VALUES (%s, %s, %s, %s);
    """, (title, public_date, image_url, description))

    conn.commit()
    cur.close()
    conn.close()


def main():
    driver, wait = setup_driver()
    try:
        driver.get("https://shaxzodbek.com/")
        time.sleep(3)

        # "Certificates" bo‘limiga o‘tish
        click_element(driver, wait, By.XPATH, '/html/body/header/div/nav/ul/li[3]/a')
        time.sleep(2)

        # "Next" tugmasini bosish
        next_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Next")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
        time.sleep(1)
        next_button.click()
        time.sleep(3)

        # Loyiha sahifasiga kirish
        click_element(driver, wait, By.XPATH, '/html/body/main/section/div[1]/div/div[3]/div[2]/h3/a', scroll=True)

        # Ma'lumotlarni olish
        title, public_date, image_url, description = extract_project_data(driver, wait)

        # Chop etish
        print("Title:", title)
        print("Public Date:", public_date)
        print("Image URL:", image_url)
        print("Description:", description)

        # Bazaga saqlash
        save_to_db(title, public_date, image_url, description)

        print("✅ Ma'lumotlar bazaga muvaffaqiyatli qo‘shildi.")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
