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
        """Возвращает задачи; при only_open=True — только невыполненные."""
        return [t for t in self.tasks if not (only_open and t.done)]

    def _find(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise LookupError(f"Задача №{task_id} не найдена")

    def complete_task(self, task_id):
        """Отмечает задачу выполненной."""
        task = self._find(task_id)
        task.done = True
        return task

    def delete_task(self, task_id):
        """Удаляет задачу из списка."""
        self.tasks.remove(self._find(task_id))
