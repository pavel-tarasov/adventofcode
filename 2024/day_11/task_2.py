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


def process_number(line: dict, current_number: int, quantity: int):
    new_numbers = apply_rules(current_number)
    if isinstance(new_numbers, int):
        if line.get(new_numbers):
            line[new_numbers] += quantity
        else:
            line[new_numbers] = quantity
    else:
        for el in new_numbers:
            if line.get(el):
                line[el] += quantity
            else:
                line[el] = quantity


total_numbers_in_line = 0
with open("input.txt") as file:
    initial_line = list(map(int, file.readline().rstrip("\n").split(" ")))
    print("file processed")

print(initial_line)
previous_line = {number: 1 for number in initial_line}
for blink_index in range(1, 76):
    current_line = {}
    for current_number, quantity in previous_line.items():
        process_number(current_line, current_number, quantity)

    total_numbers_in_line = sum([number for number in current_line.values()])
    print(f"{blink_index}: {total_numbers_in_line}")
    previous_line = current_line

print(f"task 2 result: {total_numbers_in_line}")
