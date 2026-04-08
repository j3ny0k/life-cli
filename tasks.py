import json


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

commands = ("add", "show", "done", "delete", "exit", "help")


def input_num():
    while True:
        try:
            num_str = input("\ntask num: ")
            if not num_str:
                print("input is empty")
                continue
            num = int(num_str)
        except ValueError:
            print("only integers allowed")
            continue

        if not tasks:
            print("no tasks")
            return

        if num < 1 or num > len(tasks):
            print("invalid task number")
            continue

        return num


def add_task():
    while True:
        title = input("\ntask: ")
        if not title:
            print("input is empty")
            continue
        break

    tasks.append({"title": title, "done": False})

    save_tasks(tasks)


def show_tasks():
    if not tasks:
        print("no tasks")
        return

    num = 1
    for task in tasks:
        if task["done"]:
            done = "[x]"
        else:
            done = "[ ]"
        print(f"{num}. {done} {task['title']}")
        num += 1


def done_task():
    num = input_num()

    if num is None:
        return

    tasks[num - 1]["done"] = not tasks[num - 1]["done"]
    save_tasks(tasks)

    if tasks[num - 1]["done"]:
        print("task marked as done")
    else:
        print("task marked as not done")


def delete_task():
    num = input_num()

    if num is None:
        return

    del tasks[num - 1]

    save_tasks(tasks)

    print("task deleted")


def main_tasks():
    print(f"loaded {len(tasks)} tasks")
    print()
    print('type "help" to show commands')

    while True:
        command = input("\ncommand: ").lower()

        if not command:
            print("input is empty")
            continue

        elif command == "help":
            print("allowed commands:", ", ".join(commands))

        elif command not in commands:
            print("invalid command:", command)
            print("available:", ", ".join(commands))

        if command == "exit":
            print()
            break

        elif command == "add":
            add_task()

        elif command == "show":
            show_tasks()

        elif command == "done":
            done_task()

        elif command == "delete":
            delete_task()


if __name__ == "__main__":
    main_tasks()
