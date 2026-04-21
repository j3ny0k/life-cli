# Life CLI

Simple CLI app to manage tasks and expenses.

The project combines two small tools in one program:

- task manager
- expense tracker

Data is saved to local JSON files.

---

## Features

### Tasks

- add task
- show tasks
- find tasks by text or status
- toggle task done / undone
- edit task
- delete task
- tasks are saved to file
- input validation
- invalid task number handling
- empty input handling

### Expenses

- add expense
- show expenses
- find expenses by name, category, or amount
- calculate total expenses
- calculate total by category
- edit expense
- delete expense
- expenses are saved to file
- input validation
- invalid expense number handling
- empty input handling

---

## Usage

Run the program:

```bash
python main.py
```

Choose mode:

```text
mode (tasks / expenses / exit):
```

Available modes:

- `tasks` — open task manager
- `expenses` — open expense tracker
- `exit` — exit the program

---

## Tasks commands

### add

Add a new task.

Example:

```text
command: add
task: buy bread
```

---

### show

Show all tasks.

Example:

```text
1. [ ] buy bread
2. [x] go gym
```

---

### find

Find tasks by text or by status.

You can use:

- any text → search in task title
- `done` → show only completed tasks
- `notdone` → show only not completed tasks

Example:

```text
command: find
find: buy
1. [ ] buy bread
```

---

### done

Toggle task status by number.

Example:

```text
command: done
task num: 1
task marked as done
```

---

### edit

Edit task text by number.

Example:

```text
command: edit
task num: 1
new task: buy milk
task updated
```

---

### delete

Delete a task by number.

Example:

```text
command: delete
task num: 2
task deleted
```

---

### help

Show available commands.

---

### exit

Exit task mode and return to mode selection.

---

## Expenses commands

### add

Add a new expense.

Example:

```text
command: add

name: coffee

amount: 30

category: food
```

---

### show

Show all expenses.

Example:

```text
1. coffee – 30 – food
2. bus – 10 – transport
```

---

### find

Find expenses by name, category, or amount.

Example by text:

```text
command: find

find: food
1. coffee – 30 – food
```

Example by amount:

```text
command: find

find: 30
1. coffee – 30 – food
```

If nothing is found:

```text
not found
```

---

### total

Show total amount of all expenses.

Example:

```text
command: total
total: 40
```

---

### by_category

Show total amount for one category.

Example:

```text
command: by_category

by_category: food
food: 30
```

---

### edit

Edit expense by number.

You can update only the fields you want.
Leave a field empty to keep the old value.

Example:

```text
command: edit

expense num: 1
1. coffee – 30 – food

new name: tea

new amount: 25

new category: food
expense updated
```

---

### delete

Delete an expense by number.

Example:

```text
command: delete

expense num: 2
expense deleted
```

---

### help

Show available commands.

---

### exit

Exit expenses mode and return to mode selection.

---

## Project structure

```text
main.py      # mode selection
tasks.py     # task manager logic
expenses.py  # expense tracker logic
utils.py     # shared input validation helpers
```

---

## Data files

The app uses local JSON files:

```text
tasks.json
expenses.json
```

These files are created automatically when data is saved.

They are local data files and should not be pushed to GitHub.

---

## Notes

- data is saved after changes
- tasks stay after restart
- expenses stay after restart
- task search is case-insensitive
- expense search is case-insensitive for name and category
- expense amount must be a positive integer
- task and expense numbers must be valid integers
- empty input is handled
- invalid command is handled

---

## Status

Finished learning project.

This project practices:

- multi-file Python structure
- CLI architecture
- CRUD operations
- JSON file storage
- input validation
- shared utility functions
