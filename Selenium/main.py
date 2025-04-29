import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from database import save_to_db

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_page_load_timeout(180)  # Sahifa yuklanishi uchun vaqtni oshirdik (180 soniya)
    return driver, WebDriverWait(driver, 30)

def find_and_click_project(driver, wait):
    driver.get("https://shaxzodbek.com/")
    time.sleep(2)

    project_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Projects")))
    project_link.click()
    print("🔍 'Projects' bo'limiga o'tildi.")
    time.sleep(2)

    cards = driver.find_elements(By.CSS_SELECTOR, "h3 a")
    for card in cards:
        if "Portfolio Website" in card.text:
            print(f"✅ '{card.text}' topildi. Ichkariga ketyapmiz...")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
            time.sleep(1)
            card.click()
            return

    raise Exception("❌ 'Portfolio Website' kartasi topilmadi!")

def extract_project_data(driver, wait):
    try:
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".project-header h1"))).text
    except:
        print("❌ Title topilmadi.")
        raise

    date_range = driver.find_element(By.CSS_SELECTOR, ".project-date").text.strip()
    type_badge = driver.find_element(By.CSS_SELECTOR, ".type-badge").text.strip()
    public_date = f"{date_range} | {type_badge}"

    image_url = driver.find_element(By.CSS_SELECTOR, ".project-featured-image img").get_attribute("src")
    description = driver.find_element(By.CSS_SELECTOR, ".project-description").text.strip()

    return title, public_date, image_url, description

def main():
    driver, wait = setup_driver()
    try:
        find_and_click_project(driver, wait)
        time.sleep(2)

        title, public_date, image_url, description = extract_project_data(driver, wait)

        print("\n----- Ma'lumotlar -----")
        print("Title:", title)
        print("Public Date:", public_date)
        print("Image URL:", image_url)
        print("Description:", description)

        save_to_db(title, public_date, image_url, description)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
