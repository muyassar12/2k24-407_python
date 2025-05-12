# PDP Certification Scraper

This project is a web scraper built using Selenium that extracts certification information from [shaxzodbek.com](https://shaxzodbek.com/), specifically for "PDP Academy", and stores the data in a local SQLite database.

## Features

- Navigates to the "Certifications" section of the website.
- Searches for the PDP Academy certification.
- Extracts data such as:
  - Header
  - Date
  - Image URL
  - Description
- Saves the extracted data to an SQLite database (`certifications.db`).

---

## Project Structure

```plaintext
.
├── db.py                # Handles SQLite database connection and table creation
├── main.py              # Main scraper logic using Selenium
├── requirements.txt     # List of Python dependencies
```

## Step 1
```bash
git clone  git@github.com:Mavlonbek55/2k24-407_python.git
cd 2k24-407_python
```

## Step 2
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

## Step 3
```bash
pip install -r requirements.txt
```

## Step 4
```bash
python main.py
```
