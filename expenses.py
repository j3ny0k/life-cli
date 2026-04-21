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

commands = (
    "add",
    "show",
    "find",
    "total",
    "by_category",
    "delete",
    "edit",
    "help",
    "exit",
)


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


def find_expenses():
    if not expenses:
        print("no expenses")
        return

    find = input_non_empty("\nfind: ").lower()
    found = False

    try:
        int_find = int(find)
    except ValueError:
        int_find = None

    for num, expense in enumerate(expenses, 1):
        if find in expense["name"].lower() or find in expense["category"].lower():
            print_expense(num, expense)
            found = True

        elif int_find is not None and int_find == expense["amount"]:
            print_expense(num, expense)
            found = True

    if not found:
        print("not found")


def total_expenses():
    print(f"total: {calc_total(expenses)}")


def by_category():
    if not expenses:
        print("no expenses")
        return

    category_name = input_non_empty("\nby_category: ")

    total, found = calc_category_total(expenses, category_name)

    if not found:
        print("category not found")
    else:
        print(f"{category_name}: {total}")


def edit_expense():
    if not expenses:
        print("no expenses")
        return

    num = input_num(expenses, "expense")

    if num is None:
        return

    expense = expenses[num - 1]
    print_expense(num, expense)

    updated = False

    new_name = input("\nnew name: ").strip()

    if new_name:
        expense["name"] = new_name
        updated = True

    while True:
        new_amount_str = input("\nnew amount: ").strip()

        if new_amount_str:
            try:
                new_amount = int(new_amount_str)
                if new_amount <= 0:
                    print("amount must be greater than 0")
                    continue
            except ValueError:
                print("only integers allowed")
                continue

            expense["amount"] = new_amount
            updated = True
            break

        else:
            break

    new_category = input("\nnew category: ").strip()

    if new_category:
        expense["category"] = new_category
        updated = True

    if updated:
        print()
        print("expense updated")
    else:
        print()
        print("expense not updated")

    save_expenses(expenses)


def delete_expense():
    if not expenses:
        print("no expenses")
        return

    num = input_num(expenses, "expense")

    if num is None:
        return

    del expenses[num - 1]

    save_expenses(expenses)

    print("expense deleted")


def main_expenses():
    print(f"loaded {len(expenses)} expenses")
    print()
    print("type help to show commands")

    while True:
        command = input_non_empty("\ncommand: ").lower()

        if command not in commands:
            print("invalid command:", command)
            print("available:", ", ".join(commands))

        elif command == "add":
            add_expense()

        elif command == "show":
            show_expenses()

        elif command == "find":
            find_expenses()

        elif command == "total":
            total_expenses()

        elif command == "by_category":
            by_category()

        elif command == "edit":
            edit_expense()

        elif command == "delete":
            delete_expense()

        elif command == "help":
            print("allowed commands:", ", ".join(commands))

        elif command == "exit":
            break


if __name__ == "__main__":
    main_expenses()
