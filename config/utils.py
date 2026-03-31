import os
import json
from datetime import datetime
from typing import Dict, Any, Optional

def load_json_file(file_path: str) -> Dict[str, Any]:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON in file {file_path}: {e}")

def save_json_file(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def format_timestamp(timestamp: Optional[str] = None) -> str:
    if timestamp is None:
        timestamp = datetime.now().isoformat()
    return timestamp

def create_directory_if_not_exists(directory: str) -> None:
    os.makedirs(directory, exist_ok=True)

def sanitize_filename(filename: str) -> str:
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def load_json_file_with_default(file_path: str, default: Dict[str, Any]) -> Dict[str, Any]:
    try:
        return load_json_file(file_path)
    except (FileNotFoundError, ValueError):
        return default