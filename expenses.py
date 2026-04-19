import json
from utils import input_non_empty
from utils import input_num


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

commands = ("add", "show", "total", "by_category", "delete", "edit", "exit", "help")


def calc_category_total(expenses, category_name):
    total = 0
    found = False

    for expense in expenses:
        if expense["category"] == category_name:
            total += expense["amount"]
            found = True

    return total, found


def calc_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def print_expense(num, expense):
    print(f"{num}. {expense['name']} – {expense['amount']} – {expense['category']}")


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

    for num, expense in enumerate(expenses, 1):
        print_expense(num, expense)


def total_expenses():
    print(f"total: {calc_total(expenses)}")


def by_category():
    category_name = input_non_empty("\nby_category: ")

    total, found = calc_category_total(expenses, category_name)

    if not found:
        print("category not found")
    else:
        print(f"{category_name}: {total}")


def delete_expense():
    num = input_num(expenses, "expense")

    if num is None:
        return

    del expenses[num - 1]
    save_expenses(expenses)

    print("expense deleted")


def edit_expense():
    if not expenses:
        print("no expenses")
        return

    num = input_num(expenses, "expense")

    if num is None:
        return

    expense = expenses[num - 1]
    print_expense(num, expense)

    name = input("\nname: ").strip()
    if not name:
        name = expense["name"]
    expense["name"] = name

    while True:
        amount_str = input_non_empty("\namount: ")
        try:
            amount = int(amount_str)
            if amount <= 0:
                print("amount must be greater than 0")
                continue
            expense["amount"] = amount
            break
        except ValueError:
            print("only integers allowed")

    category = input("\ncategory: ").strip()
    if not category:
        category = expense["category"]
    expense["category"] = category

    print("expense updated")
    save_expenses(expenses)


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

        elif command == "edit":
            edit_expense()


if __name__ == "__main__":
    main_expenses()
