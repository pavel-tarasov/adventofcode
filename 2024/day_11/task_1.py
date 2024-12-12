def apply_rules(number: int) -> int | list[int]:
    if number == 0:
        return 1
    elif len(string_number := str(number)) % 2 == 0:
        return [
            int(string_number[: int(len(string_number) / 2)]),
            int(string_number[int(len(string_number) / 2) :]),
        ]
    else:
        return number * 2024


total_numbers_in_line = 0
with open("input.txt") as file:
    initial_line = list(map(int, file.readline().rstrip("\n").split(" ")))
    print("file processed")

print(initial_line)
previous_line = initial_line
for blink_index in range(1, 26):
    current_line = []
    for current_number in previous_line:
        new_numbers = apply_rules(current_number)
        if isinstance(new_numbers, int):
            current_line.append(new_numbers)
        else:
            current_line.extend(new_numbers)

    total_numbers_in_line = len(current_line)
    print(f"{blink_index}: {total_numbers_in_line}")
    previous_line = current_line

print(f"task 1 result: {total_numbers_in_line}")
