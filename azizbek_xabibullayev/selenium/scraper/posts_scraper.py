from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from typing import List, Dict

from scraper.pagination import pagination


def scrape_posts(url: str, driver) -> List[Dict]:
    posts = []
    print(f"Scraping started for URL: {url}")

    try:
        driver.get(url)
        time.sleep(2)

        while True:
            try:
                article_elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'article-card'))
                )
                print(f"Found {len(article_elements)} articles on this page.")

                for article in article_elements:
                    try:
                        image_url = article.find_element(By.CSS_SELECTOR, '.article-image img').get_attribute('src')

                        title_element = article.find_element(By.CSS_SELECTOR, '.article-content h4 a')
                        title = title_element.text
                        link = title_element.get_attribute('href')

                        publish_date = article.find_element(By.CSS_SELECTOR, '.article-date').text

                        text = article.find_element(By.CSS_SELECTOR, '.article-content p').text

                        tools_type = None

                        post_data = {
                            'content_type': 'Post',
                            'title': title,
                            'image_url': image_url,
                            'text': text,
                            'publish_date': publish_date,
                            'link': link,
                            'tools_type': tools_type
                        }
                        posts.append(post_data)

                    except Exception as e:
                        print(f"Error processing article: {e}")
                        continue

            except Exception:
                print("Error finding articles")
                break
            check_new_page = pagination(driver)
            if not check_new_page:
                break

    except Exception as e:
        print(f"General error during scraping: {e}")

    print(f"Scraping completed. Found {len(posts)} posts.")
    return posts
