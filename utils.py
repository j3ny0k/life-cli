def input_non_empty(prompt, newline_after_error=False):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("input is empty")
        if newline_after_error:
            print()


def input_num(items, item_name):
    while True:
        try:
            num_str = input_non_empty(f"\n{item_name} num: ")
            num = int(num_str)
        except ValueError:
            print("only integers allowed")
            continue

        if not items:
            print(f"no {item_name}")
            return

        if num < 1 or num > len(items):
            print(f"invalid {item_name} number")
            continue

        return num
