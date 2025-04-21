from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List, Dict
from scraper.pagination import pagination


def scrape_projects(url: str, driver) -> List[Dict]:
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
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'project-card'))
                )
                print(f"Found {len(article_elements)} projects on this page.")

                for article in article_elements:
                    projects_data = {
                        'content_type': 'projects',
                        'title': '',
                        'image_url': '',
                        'text': '',
                        'publish_date': '',
                        'link': '',
                        'tools_type': ''
                    }

                    try:
                        projects_data['image_url'] = article.find_element(
                            By.CSS_SELECTOR, '.project-image img'
                        ).get_attribute('src')

                        projects_data['title'] = article.find_element(
                            By.CSS_SELECTOR, '.project-content h3 a'
                        ).text

                        links = article.find_elements(By.CSS_SELECTOR, '.project-links a')
                        projects_data['link'] = ', '.join(
                            [link.get_attribute('href') for link in links if link.get_attribute('href')])

                        projects_data['publish_date'] = article.find_element(
                            By.CSS_SELECTOR, '.project-date'
                        ).text

                        projects_data['text'] = article.find_element(
                            By.CSS_SELECTOR, '.project-content p'
                        ).text

                        type_badge = article.find_element(By.CSS_SELECTOR, '.project-types')
                        tools_type = type_badge.find_elements(By.CSS_SELECTOR, '.type-badge')
                        projects_data['tools_type'] = ', '.join([badge.text.strip() for badge in tools_type])

                        posts.append(projects_data)

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
