import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
driver.get("https://shaxzodbek.com/")
time.sleep(2)
print(driver.title)
time.sleep(2)
driver.quit()