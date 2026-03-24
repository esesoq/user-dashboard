import os
import json
from datetime import datetime
from typing import Dict, Any, Optional

def load_json_file(file_path: str) -> Dict[str, Any]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json_file(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def format_timestamp(timestamp: Optional[str] = None) -> str:
    if timestamp is None:
        timestamp = datetime.now().isoformat()
    return timestamp

def create_directory_if_not_exists(directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)

def sanitize_filename(filename: str) -> str:
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename