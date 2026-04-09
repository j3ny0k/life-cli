import json
from utils import input_non_empty


def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)


def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


expenses = load_expenses()

commands = ("add", "show", "total", "by_category", "delete", "exit", "help")


def input_num():
    while True:
        try:
            num_str = input_non_empty("\nexpense num: ")
            num = int(num_str)
        except ValueError:
            print("only integers allowed")
            continue

        if not expenses:
            print("no expenses")
            return

        if num < 1 or num > len(expenses):
            print("invalid expense number")
            continue

        return num


def add_expense():
    name = input_non_empty("\nname: ")

    while True:
        amount_str = input_non_empty("\namount: ")
        try:
            amount = int(amount_str)
            if amount <= 0:
                print("amount must be greater than 0")
                continue
            break
        except ValueError:
            print("only integers allowed")

    category = input_non_empty("\ncategory: ")

    expenses.append({"name": name, "amount": amount, "category": category})
    save_expenses(expenses)


def show_expenses():
    if not expenses:
        print("no expenses")
        return

    num = 1

    for expense in expenses:
        name = expense["name"]
        amount = expense["amount"]
        category = expense["category"]

        print(f"{num}. {name} – {amount} – {category}")
        num += 1


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"total: {total}")


def by_category():
    category_name = input_non_empty("\nby_category: ")

    total = 0
    found = False

    for expense in expenses:
        if expense["category"] == category_name:
            total += expense["amount"]
            found = True

    if not found:
        print("category not found")
    else:
        print(f"{category_name}: {total}")


def delete_expense():
    num = input_num()

    if num is None:
        return

    del expenses[num - 1]

    save_expenses(expenses)

    print("expense deleted")


def main_expenses():
    print(f"loaded {len(expenses)} expenses")
    print()
    print('type "help" to show commands')

    while True:
        command = input_non_empty("\ncommand: ").lower()

        if command == "help":
            print("allowed commands:", ", ".join(commands))

        elif command not in commands:
            print("invalid command:", command)
            print("available:", ", ".join(commands))

        elif command == "exit":
            print()
            break

        elif command == "add":
            add_expense()

        elif command == "show":
            show_expenses()

        elif command == "total":
            total_expenses()

        elif command == "by_category":
            by_category()

        elif command == "delete":
            delete_expense()


if __name__ == "__main__":
    main_expenses()
