# 🧠 Certification Scraper & PostgreSQL Storage

This project is a Python-based automation tool that uses Selenium to scrape certification data from [shaxzodbek.com](https://shaxzodbek.com/) and saves it to a PostgreSQL database. It's useful for building personal dashboards, collecting educational records, or practicing data extraction and integration using web scraping.

---

## 🚀 Features

- 🔍 Scrapes the latest certification info (title, obtained date, image URL, description)
- 🧭 Navigates multiple layers of the website using Selenium
- 📸 Extracts structured data using XPath and CSS Selectors
- 💾 Saves data into a PostgreSQL database
- 🛡 Avoids duplicate entries using a conditional insert
- ✅ Automatically creates the table if it doesn't exist

---

## 🧰 Technologies Used

| Tool              | Description                                  |
|-------------------|----------------------------------------------|
| Python            | Programming language                         |
| Selenium          | Web browser automation                       |
| psycopg2          | PostgreSQL database connector for Python     |
| webdriver-manager | Manages and updates ChromeDriver             |
| PostgreSQL        | Relational database                          |



