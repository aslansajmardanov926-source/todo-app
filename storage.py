"""Хранение задач в JSON-файле."""
import json
from pathlib import Path


def save_tasks(path, tasks):
    """Сохраняет список словарей-задач в JSON."""
    text = json.dumps(tasks, ensure_ascii=False, indent=2)
    Path(path).write_text(text, encoding="utf-8")


def load_tasks(path):
    """Читает задачи; если файла нет — возвращает пустой список."""
    file = Path(path)
    if not file.exists():
        return []
    return json.loads(file.read_text(encoding="utf-8"))
