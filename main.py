"""Консольный интерфейс менеджера задач."""
import sys
from dataclasses import asdict

from storage import load_tasks, save_tasks
from todo import Task, TodoList

DB_FILE = "tasks.json"
HELP = "Команды: add <текст> | list [--open] | done <id> | delete <id>"


def show(todo, only_open=False):
    for t in todo.list_tasks(only_open):
        mark = "x" if t.done else " "
        print(f"[{mark}] {t.id}. {t.title}")


def main(argv):
    todo = TodoList([Task(**d) for d in load_tasks(DB_FILE)])
    command = argv[0] if argv else "list"
    try:
        if command == "add":
            task = todo.add_task(" ".join(argv[1:]))
            print(f"Добавлена задача №{task.id}: {task.title}")
        elif command == "done":
            task = todo.complete_task(int(argv[1]))
            print(f"Выполнено: {task.title}")
        elif command == "delete":
            todo.delete_task(int(argv[1]))
            print("Задача удалена")
        elif command == "list":
            show(todo, only_open="--open" in argv)
        else:
            print(HELP)
    except (ValueError, LookupError) as error:
        print(f"Ошибка: {error}")
        return 1
    save_tasks(DB_FILE, [asdict(t) for t in todo.tasks])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
