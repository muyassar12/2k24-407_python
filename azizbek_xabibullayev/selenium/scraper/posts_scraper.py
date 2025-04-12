import time

from selenium.webdriver.common.by import By


def scrape_posts(
        url: str,
        driver,
        options
):
    driver.get(url)

    time.sleep(2)

    posts = []
    post_elements = driver.find_elements(By.XPATH, '//*[@class="post"]')

    for post in post_elements:
        title = post.find_element(By.XPATH, './/h2').text
        content = post.find_element(By.XPATH, './/p').text
        posts.append({'title': title, 'content': content})

    # Close the WebDriver
    driver.quit()

    return posts
