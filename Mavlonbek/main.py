import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

from db import get_connection, create_certification_table
def save_certification_to_db(data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO certifications (header, date, image, description)
        VALUES (?, ?, ?, ?)
    """, (data["header"], data["date"], data["image"], data["description"]))
    conn.commit()
    cur.close()
    conn.close()
    print(" Ma'lumotlar SQLite bazaga saqlandi.")
def start_browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    return driver
def scrape_pdp_certification(driver):
    driver.get("https://shaxzodbek.com/")

    try:
        certifications_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Certifications"))
        )
        certifications_link.click()
    except TimeoutException:
        print(" 'Certifications' havolasi topilmadi.")
        return None

    while True:
        time.sleep(2)
        cards = driver.find_elements(By.CLASS_NAME, "certification-content")
        for card in cards:
            if "PDP Academy" in card.text:
                print("PDP Academy topildi.")
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
                time.sleep(1)
                card.find_element(By.LINK_TEXT, "PDP Academy").click()

                time.sleep(2)

                data = {
                    "header": WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//main/section/div/header/h3"))
                    ).text,
                    "date": WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//main/section/div/header/div/div"))
                    ).text,
                    "image": WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//main/section/div/div[1]/div[1]/img"))
                    ).get_attribute("src"),
                    "description": WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//main/section/div/div[1]/div[2]"))
                    ).text,
                }
                return data

        try:
            next_btn = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Next"))
            )
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_btn)
            next_btn.click()
        except TimeoutException:
            print(" PDP Academy topilmadi.")
            break

    return None
def main():
    create_certification_table()
    driver = start_browser()

    try:
        data = scrape_pdp_certification(driver)
        if data:
            save_certification_to_db(data)
        else:
            print(" Ma'lumot topilmadi.")
    except Exception as e:
        print("Xatolik yuz berdi:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
