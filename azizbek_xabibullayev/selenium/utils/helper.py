from datetime import datetime


def parse_date(date_input: str) -> str:
    try:
        parsed_date = datetime.strptime(date_input, "%Y-%m-%d")
        return parsed_date.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Incorrect date format: {date_input}. Example 'YYYY-MM-DD'.")
