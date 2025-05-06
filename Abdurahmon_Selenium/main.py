# main file
from selenium.webdriver.chrome.options import Options
from db import get_connection, create_table_if_not_exists
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import time
chrome_options = Options()
# DB connection
conn = get_connection()
cursor = conn.cursor()
create_table_if_not_exists()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://shaxzodbek.com/")

try:
    certifications_link = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Certifications"))
    )
    certifications_link.click()

    found = False
    while not found:
        time.sleep(2)
        cards = driver.find_elements(By.CLASS_NAME, "certification-content")

        for card in cards:
            if "PDP Academy" in card.text:
                print("topildi")
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
                time.sleep(1)

                card.find_element(By.LINK_TEXT, "PDP Academy").click()
                driver.save_screenshot("./screenshot.png")
                time.sleep(5)

                header = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//main/section/div/header/h3"))
                ).text

                date = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//main/section/div/header/div/div"))
                ).text

                img = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//main/section/div/div[1]/div[1]/img"))
                ).get_attribute("src")

                desc = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//main/section/div/div[1]/div[2]"))
                ).text
                # Insert
                cursor.execute("""
                    INSERT INTO certifications (header, date, image, description)
                    VALUES (%s, %s, %s, %s)
                """, (header, date, img, desc))
                conn.commit()
                time.sleep(2)
                print("PDP Academy DB ga muvaffaqiyatli saqlandi")
                found = True
                break

        if not found:
            try:
                next_btn = WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Next"))
                )
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_btn)
                time.sleep(1)
                next_btn.click()
            except TimeoutException:
                print("PDP Academy topilmadi")
                break

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()
    driver.quit()