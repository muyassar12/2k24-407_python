import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pagination(driver):
    try:
        current_url = driver.current_url

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[@class="pagination-link" and contains(text(), "Next")]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        ActionChains(driver).move_to_element(element).click().perform()
        print("Navigating to next page.")

        WebDriverWait(driver, 10).until(
            lambda d: d.current_url != current_url
        )
        time.sleep(2)
        return True
    except Exception:
        print("No more pages to scrape.")
        return False
