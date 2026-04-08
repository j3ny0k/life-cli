import tasks
import expenses

while True:
    mode = input("mode (tasks / expenses / exit): ").lower()

    if not mode:
        print("input is empty")
        print()
        continue

    elif mode == "tasks":
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
