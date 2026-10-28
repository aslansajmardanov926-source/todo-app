# TaskMate

Консольный менеджер задач (To-Do) — учебный проект практической работы №9.

## Цель продукта
Помочь студенту вести список дел прямо из терминала.

## Команда
| Участник | Роль |
| --- | --- |
| Участник 1 | Product Owner, разработчик |
| Участник 2 | Scrum Master, разработчик |

## Правила работы с Git
- Ветки: `main` (стабильная), `develop` (интеграция), `feature/<номер-задачи>-<кратко>`.
- Формат коммитов: `feat|fix|docs|refactor|test: описание (TASK-N)`.
- Прямые коммиты в `main` запрещены: изменения только через pull request.

## Запуск
```
python main.py add "Купить молоко"
python main.py list [--open]
python main.py done 1
python main.py delete 1
python -m unittest -v
```
