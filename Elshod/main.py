# main.py

import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from database import get_connection, create_table_if_not_exists

load_dotenv()

BASE_URL = os.getenv("BASE_URL") or "https://shaxzodbek.com/"
SCREENSHOT_NAME = os.getenv("SCREENSHOT_NAME") or "online_business_post.png"
TARGET_POST_TITLE = "How to Start a Successful Online Business"


def init_driver():
    try:
        options = webdriver.ChromeOptions()
        # Agar headless mode kerak bo'lsa, quyidagi qatorni izohdan chiqaring
        # options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    except WebDriverException as e:
        print(f"Brauzerni ishga tushirishda xatolik: {e}")
        exit(1)


def save_to_postgres(conn, url, screenshot_path):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Projects (header, date, image, description) VALUES (%s, %s, %s, %s);",
                (TARGET_POST_TITLE, time.strftime("%Y-%m-%d"), screenshot_path, f"Topilgan URL: {url}")
            )
            conn.commit()
            print("Maʼlumot PostgreSQL bazasiga saqlandi.")
    except Exception as e:
        print(f"PostgreSQL saqlashda xatolik: {e}")


def scroll_down(driver, amount=300):
    driver.execute_script(f"window.scrollTo(0, {amount});")
    time.sleep(1)


def take_screenshot(driver, filename):
    path = os.path.join(os.getcwd(), filename)
    driver.save_screenshot(path)
    print(f"Skrinshot saqlandi: {path}")
    return path


def goto_blog_section(driver):
    try:
        # Saytga kiramiz
        driver.get(BASE_URL)
        print("Asosiy sahifaga kirildi")

        # Post yoki blog bo'limini topamiz
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)  # Sahifa to'liq yuklanishi uchun kutish

        # Screenshotda ko'ringan Post menyu tugmasini bosish
        try:
            # Menyudagi "Post" tugmasi
            post_link = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Post']"))
            )
            post_link.click()
            print("Post bo'limiga o'tildi")
            time.sleep(3)  # Sahifa yuklanishi uchun kutish
            return True
        except:
            # Agar aniq "Post" tugmasi topilmasa, alternativ qidiruv
            blog_links = driver.find_elements(By.TAG_NAME, "a")
            blog_link = None

            for link in blog_links:
                try:
                    link_text = link.text.lower()
                    if "post" in link_text or "blog" in link_text or "maqola" in link_text:
                        blog_link = link
                        break
                except:
                    continue

            if blog_link:
                blog_link.click()
                print("Blog/Post bo'limiga o'tildi")
                time.sleep(3)  # Sahifa yuklanishi uchun kutish
                return True
            else:
                print("Blog/Post bo'limi topilmadi. Umumiy sahifada qidirishga o'tilmoqda.")
                return True  # Asosiy sahifada davom ettirish

    except Exception as e:
        print(f"Blog bo'limiga o'tishda xatolik: {e}")
        return False


def go_to_next_page(driver):
    try:
        scroll_down(driver, 1000)  # Sahifaning pastki qismiga tushish

        # Sahifadagi "Next" tugmasini qidirish
        try:
            # Aniq "Next" tugmasini qidirish (screenshot'da ko'rsatilgan)
            next_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Next' or contains(text(), 'Next')]"))
            )
            next_button.click()
            print("Next tugmasi bosildi")
            time.sleep(3)  # Sahifa yuklanishi uchun kutish
            return True
        except:
            # Agar aniq "Next" tugmasi topilmasa alternativ qidiruv
            next_buttons = driver.find_elements(By.TAG_NAME, "a")
            next_button = None

            for button in next_buttons:
                try:
                    text = button.text.lower()
                    if "next" in text or "keyingi" in text or "→" in text or "»" in text:
                        next_button = button
                        break
                except:
                    continue

            if next_button:
                print("Keyingi sahifa tugmasi bosildi")
                next_button.click()
                time.sleep(3)  # Sahifa yuklanishi uchun kutish
                return True
            else:
                print("Keyingi sahifa tugmasi topilmadi")
                return False

    except Exception as e:
        print(f"Keyingi sahifaga o'tishda xatolik: {e}")
        return False


def find_and_click_post(driver):
    try:
        # Barcha post kartalarini qidirish - screenshot'dan ko'rinib turibdi
        # Saytda kartalar mavjud (3ta karta post qismida ko'rinadi)

        # Avval sarlavha orqali qidirish
        try:
            target_post = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//h2[contains(text(), '{TARGET_POST_TITLE}')]"))
            )
            target_post.click()
            print(f"Post topildi va bosildi: {TARGET_POST_TITLE}")
            time.sleep(3)
            return True
        except TimeoutException:
            print("Post sarlavha orqali topilmadi. Post cardlarini qidirmoqda...")

        # Karta elementlarini qidirish
        cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'card') or contains(@class, 'post')]")

        if not cards:
            # Alternativ qidiruv
            # Sayt tuzilishini hisobga olib, har qanday sarlavhalarni qidirish
            titles = driver.find_elements(By.XPATH, "//h1 | //h2 | //h3 | //h4 | //article")
            cards = titles

        target_card = None

        # Barcha potentsial kartalar va elementlarni tekshirish
        for card in cards:
            try:
                card_text = card.text
                if TARGET_POST_TITLE.lower() in card_text.lower():
                    target_card = card
                    break

                # Har bir karta ichida linklar yoki sarlavhalarni tekshirish
                elements = card.find_elements(By.XPATH, ".//a | .//h2 | .//h3")
                for element in elements:
                    try:
                        element_text = element.text
                        if TARGET_POST_TITLE.lower() in element_text.lower():
                            target_card = element
                            break
                    except:
                        continue
            except:
                continue

        if target_card:
            print(f"Post topildi: {TARGET_POST_TITLE}")
            target_card.click()
            time.sleep(3)  # Sahifa yuklanishi uchun kutish
            return True

        print(f"'{TARGET_POST_TITLE}' sarlavhali post topilmadi.")
        return False

    except Exception as e:
        print(f"Postni qidirishda xatolik: {e}")
        return False


def main():
    print("Jarayon boshlandi...")
    driver = init_driver()
    conn = get_connection()

    try:
        create_table_if_not_exists()

        # Blog qismiga o'tamiz
        if not goto_blog_section(driver):
            print("Blog bo'limiga o'tib bo'lmadi")
            return

        # Postni qidiramiz
        post_found = find_and_click_post(driver)

        # Agar post topilmasa, keyingi sahifaga o'tib yana qidiramiz
        if not post_found:
            print("Post birinchi sahifada topilmadi. Keyingi sahifaga o'tilmoqda...")
            if go_to_next_page(driver):
                post_found = find_and_click_post(driver)

        if post_found:
            # Screenshot olish va ma'lumotlar bazasiga saqlash
            screenshot_path = take_screenshot(driver, SCREENSHOT_NAME)
            if conn:
                save_to_postgres(conn, driver.current_url, screenshot_path)
            print("Jarayon muvaffaqiyatli yakunlandi.")
        else:
            print(f"'{TARGET_POST_TITLE}' sarlavhali post topilmadi.")

    finally:
        driver.quit()
        if conn:
            conn.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Jarayon to'xtatildi.")