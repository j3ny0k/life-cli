def input_non_empty(prompt, newline_after_error=False):
    while True:
        value = input(prompt)
        if value:
            return value
        print("input is empty")
        if newline_after_error:
            print()
