# Life CLI

CLI-приложение для управления задачами и расходами.

Проект построен как multi-file структура с разделением логики на модули.

---

## Возможности

### Tasks (задачи)

- add — добавить задачу
- show — показать все задачи
- find — поиск:
  - `done` → выполненные
  - `notdone` → невыполненные
  - текст → поиск по названию
- done — переключить статус (done / not done)
- edit — изменить текст задачи
- delete — удалить задачу

---

### Expenses (расходы)

- add — добавить расход (name, amount, category)
- show — показать все расходы
- total — общая сумма
- by_category — сумма по категории
- edit — изменить расход
- delete — удалить расход

---

## Запуск

```bash
python main.py
```

---

## Режимы

При запуске:

```
mode (tasks / expenses / exit):
```

---

## Пример работы (Tasks)

```
mode: tasks

command: add
task: buy bread

command: show
1. [ ] buy bread

command: done
task num: 1
task marked as done

command: find
find: done
1. [x] buy bread

command: edit
task num: 1
new task: buy milk

command: delete
task num: 1
task deleted
```

---

## Пример работы (Expenses)

```
mode: expenses

command: add
name: bread
amount: 12
category: food

command: show
1. bread – 12 – food

command: total
total: 12

command: by_category
by_category: food
food: 12

command: edit
expense num: 1
name: milk
amount: 15
category: food

command: delete
expense num: 1
expense deleted
```

---

## Хранение данных

- `tasks.json` — задачи
- `expenses.json` — расходы
- данные сохраняются автоматически
- сохраняются между запусками

---

## Обработка ошибок

- пустой ввод → обрабатывается
- неверные числа → обрабатываются
- неверные команды → показывается список доступных
- выбор по номеру проверяется

---

## Структура проекта

- `main.py` — управление режимами
- `tasks.py` — логика задач (CRUD + find + edit)
- `expenses.py` — логика расходов
- `utils.py` — ввод и валидация

---

## Цель проекта

Практика backend-базы:

- работа со списками и словарями
- фильтрация данных (find)
- работа с JSON
- разделение кода на модули
- базовая архитектура CLI-приложения
