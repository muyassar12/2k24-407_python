import time
import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === Selenium bilan sahifani ochamiz ===
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://shaxzodbek.com/")

# Kirish tugmasini bosamiz
login_button = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/nav/ul/li[4]/a")))
login_button.click()

# Kirish sahifasida scroll qilish
login_button2 = WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div[2]/a[1]")))
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", login_button2)
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/div[2]/a[1]")))
login_button2.click()

# Sertifikat sahifasiga o‘tamiz
login_button3 = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/div[1]/div/div[3]/div[2]/h4/a")))
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", login_button3)
login_button3.click()
time.sleep(2)

# === Sahifadagi kerakli ma’lumotlarni avtomatik olish ===
title = driver.find_element(By.CSS_SELECTOR, ".certification-header h3").text
obtained_date = driver.find_element(By.CLASS_NAME, "certification-date").text.replace("Obtained: ", "")
image_url = driver.find_element(By.CSS_SELECTOR, ".certification-image img").get_attribute("src")
description = driver.find_element(By.CLASS_NAME, "certification-description").text.strip()

# === Konsolga chop etish (tekshirish uchun) ===
print("Title:", title)
print("Obtained Date:", obtained_date)
print("Image URL:", image_url)
print("Description:", description)

# === PostgreSQL bazaga ulanish ===
conn = psycopg2.connect(
    host="localhost",  # yoki RDS/PostgreSQL host
    database="selenium",
    user="postgres",
    password="admin1234"
)
cur = conn.cursor()

# SQL query yuborish
cur.execute("""
    INSERT INTO certifications (title, public_date, image_url, description)
    VALUES (%s, %s, %s, %s);
""", (title, obtained_date, image_url, description))

# O'zgarishlarni saqlaymiz va ulanishni yopamiz
conn.commit()
cur.close()
conn.close()

print("✅ Sertifikat ma'lumotlari muvaffaqiyatli qo‘shildi.")