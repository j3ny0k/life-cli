import json
from utils import input_non_empty
from utils import input_num


def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)


def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


tasks = load_tasks()

commands = ("add", "show", "find", "done", "delete", "edit", "help", "exit")


def print_task(num, task):
    done = "[x]" if task["done"] else "[ ]"
    print(f"{num}. {done} {task['title']}")


def add_task():
    title = input_non_empty("\ntask: ")

    tasks.append({"title": title, "done": False})
    save_tasks(tasks)


def show_tasks():
    if not tasks:
        print("no tasks")
        return

    for num, task in enumerate(tasks, 1):
        print_task(num, task)


def find_task():
    if not tasks:
        print("no tasks")
        return

    find = input_non_empty("\nfind: ").lower()
    found = False

    for num, task in enumerate(tasks, 1):
        if find == "done":
            if task["done"]:
                print_task(num, task)
                found = True

        elif find == "notdone":
            if not task["done"]:
                print_task(num, task)
                found = True

        elif find in task["title"].lower():
            print_task(num, task)
            found = True

    if not found:
        print("not found")


def done_task():
    if not tasks:
        print("no tasks")
        return

    num = input_num(tasks, "task")

    if num is None:
        return

    tasks[num - 1]["done"] = not tasks[num - 1]["done"]
    save_tasks(tasks)

    if tasks[num - 1]["done"]:
        print("task marked as done")
    else:
        print("task marked as not done")


def edit_task():
    if not tasks:
        print("no tasks")
        return

    num = input_num(tasks, "task")

    if num is None:
        return

    print_task(num, tasks[num - 1])

    new_task = input_non_empty("\nnew task: ")

    tasks[num - 1]["title"] = new_task

    print("task updated")

    save_tasks(tasks)


def delete_task():
    if not tasks:
        print("no tasks")
        return

    num = input_num(tasks, "task")

    if num is None:
        return

    del tasks[num - 1]

    save_tasks(tasks)

    print("task deleted")


def main_tasks():
    print(f"loaded {len(tasks)} tasks")
    print()
    print("type help to show commands")

    while True:
        command = input_non_empty("\ncommand: ").lower()

        if command not in commands:
            print("invalid command:", command)
            print("available:", ", ".join(commands))

        elif command == "add":
            add_task()

        elif command == "show":
            show_tasks()

        elif command == "find":
            find_task()

        elif command == "done":
            done_task()

        elif command == "edit":
            edit_task()

        elif command == "delete":
            delete_task()

        elif command == "help":
            print("allowed commands:", ", ".join(commands))

        elif command == "exit":
            break


if __name__ == "__main__":
    main_tasks()
