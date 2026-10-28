"""Модель задач и операции над списком (To-Do)."""
from dataclasses import dataclass


@dataclass
class Task:
    """Одна задача: номер, название и признак выполнения."""

    id: int
    title: str
    done: bool = False


class TodoList:
    """Список задач, хранящийся в памяти."""

    def __init__(self, tasks=None):
        self.tasks = list(tasks or [])

    def _next_id(self):
        return max((t.id for t in self.tasks), default=0) + 1

    def add_task(self, title):
        """Добавляет задачу и возвращает её."""
        title = title.strip()
        if not title:
            raise ValueError("Название задачи не может быть пустым")
        task = Task(self._next_id(), title)
        self.tasks.append(task)
        return task

    def list_tasks(self, only_open=False):
        return [t for t in self.tasks if not (only_open and t.done)]
