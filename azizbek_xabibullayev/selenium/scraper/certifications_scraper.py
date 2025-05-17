from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List, Dict
from scraper.pagination import pagination


def scrape_certifications(url: str, driver) -> List[Dict]:
    posts = []
    print(f"Scraping started for URL: {url}")

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        while True:
            try:
                article_elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'certification-card'))
                )
                print(f"Found {len(article_elements)} projects on this page.")

                for article in article_elements:
                    certifications_data = {
                        'content_type': 'certifications',
                        'title': '',
                        'image_url': '',
                        'text': '',
                        'publish_date': '',
                        'link': '',
                        'tools_type': ''
                    }

                    try:
                        certifications_data['image_url'] = article.find_element(
                            By.CSS_SELECTOR, '.certification-image img'
                        ).get_attribute('src')

                        certifications_data['title'] = article.find_element(
                            By.CSS_SELECTOR, '.certification-content h4 a'
                        ).text

                        certifications_data["link"] = article.find_element(
                            By.CSS_SELECTOR, '.certification-content h4 a'
                        ).get_attribute('href')

                        certifications_data['publish_date'] = article.find_element(
                            By.CSS_SELECTOR, '.certification-date'
                        ).text

                        certifications_data['text'] = article.find_element(
                            By.CSS_SELECTOR, '.certification-content p'
                        ).text

                        certifications_data['tools_type'] = None

                        posts.append(certifications_data)

                    except Exception as e:
                        print(f"Error processing article: {e}")
                        continue
            except Exception as e:
                print(f"Unexpected error finding articles: {e}")
                break

            if not pagination(driver):
                break
    except Exception as e:
        print(f"General error during scraping: {e}")
    finally:
        print(f"Scraping completed. Found {len(posts)} posts.")
        return posts
