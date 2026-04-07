# Life CLI

Simple CLI app that combines task management and expense tracking.

---

## Features

### Tasks

- add task
- show tasks
- mark task as done / undone
- delete task
- input validation

### Expenses

- add expense (name, amount, category)
- show all expenses
- total expenses
- total by category
- delete expense
- input validation (including amount > 0)

---

## Usage

Run the program:

```bash
python main.py
```

---

## Modes

When you start the program, choose a mode:

```text
mode (tasks / expenses / exit):
```

---

## Tasks mode

Example:

```text
mode: tasks

command: add
task: buy bread

command: show
1. [ ] buy bread

command: done
task num: 1
task marked as done

command: delete
task num: 1
task deleted

command: exit
```

---

## Expenses mode

Example:

```text
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

command: delete
expense num: 1
expense deleted

command: exit
```

---

## Data storage

- tasks are stored in `tasks.json`
- expenses are stored in `expenses.json`
- data is saved automatically
- data persists after restart

---

## Notes

- empty input is handled
- invalid numbers are handled
- invalid commands are handled
- amount must be greater than 0
- JSON files are local (not pushed to GitHub)
