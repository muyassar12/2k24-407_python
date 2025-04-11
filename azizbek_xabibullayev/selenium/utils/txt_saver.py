import json
from datetime import datetime
from typing import Optional

def backup_to_json(content_type: str,
                 title: str,
                 image_url: str,
                 text: str,
                 publish_date: str,
                 link: Optional[str] = None,
                 tools_type: Optional[str] = None,
                 filename: str = "backup_content_cards.json") -> bool:
    try:
        card_data = {
            "content_type": content_type,
            "title": title,
            "image_url": image_url,
            "text": text,
            "publish_date": publish_date,
            "link": link,
            "tools_type": tools_type,
            "saved_at": datetime.now().isoformat()
        }
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        data.append(card_data)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return True
    except Exception:
        return False