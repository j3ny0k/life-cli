import tasks
import expenses
from utils import input_non_empty

while True:
    mode = input_non_empty(
        "mode (tasks / expenses / exit): ", newline_after_error=True
    ).lower()

    if mode == "tasks":
        print()
        tasks.main_tasks()

    elif mode == "expenses":
        print()
        expenses.main_expenses()

    elif mode == "exit":
        break

    else:
        print("invalid mode")
        print()
