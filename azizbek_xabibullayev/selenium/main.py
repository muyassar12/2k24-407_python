from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from db.init_db import insert_content_cards
from scraper.certifications_scraper import scrape_certifications
from scraper.posts_scraper import scrape_posts
from scraper.projects_scraper import scrape_projects

main_data = {}


def main_func():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    try:
        posts = scrape_posts("https://shaxzodbek.com/post/", driver)
        main_data["posts"] = posts
        projects = scrape_projects("https://shaxzodbek.com/projects/", driver)
        main_data["projects"] = projects
        certifications = scrape_certifications("https://shaxzodbek.com/certifications/", driver)
        main_data["certifications"] = certifications
        print("\n")
        insert_content_cards(main_data["posts"])
        print("\n")
        insert_content_cards(main_data["projects"])
        print("\n")
        insert_content_cards(main_data["certifications"])
        print("\n")
    finally:
        driver.quit()


if __name__ == "__main__":
    main_func()
