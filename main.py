import tasks
import expenses

while True:
    mode = input("mode (tasks / expenses / exit): ")

    if not mode:
        print("input is empty")
        continue

    elif mode == "tasks":
        tasks.main_tasks()

    elif mode == "expenses":
        expenses.main_expenses()

    elif mode == "exit":
        break

    else:
        print("invalid mode")
