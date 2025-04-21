import json
from datetime import datetime
from typing import Optional, Dict


def backup_missing_data_to_json(missing_data: Dict[str, Dict], filename: str = "missing_data.json") -> bool:
    try:
        data_to_save = []
        for title, content in missing_data.items():
            content["title"] = title or "NO_TITLE"
            content["saved_at"] = datetime.now().isoformat()
            data_to_save.append(content)
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        existing_data.extend(data_to_save)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Error while backing up missing data: {e}")
        return False
