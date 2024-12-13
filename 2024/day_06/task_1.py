def on_position(position: tuple[int, int]) -> str:
    global field
    return field[position[0]][position[1]]


def update_symbol(position: tuple[int, int], new_symbol: str) -> None:
    global field
    field[position[0]][position[1]] = new_symbol


def print_field() -> None:
    global field
    print()
    for line in field:
        for symbol in line:
            print(symbol, end="")
        print()
    print()


def is_valid_position(position: tuple[int, int]) -> bool:
    global field
    if (position[0] < 0 or position[0] > (len(field) - 1)) or (
        position[1] < 0 or position[1] > (len(field[0]) - 1)
    ):
        return False
    else:
        return True


GUARD_SYMBOLS = ["^", ">", "v", "<"]
OBSTRUCTION_SYMBOL = "#"
VISITED_SYMBOL = "X"
field = []
guard_position = (0, 0)
guard_symbol = ""
result = None
i = 0
with open("input.txt") as file:
    while True:
        line = file.readline().rstrip("\n")

        if line == "":
            print("file processed")
            break

        field.append(list(line))

        for j, symbol in enumerate(list(line)):
            if symbol in GUARD_SYMBOLS:
                guard_position = (i, j)
                guard_symbol = symbol
        i += 1

print(f"initial guard position: {guard_position}")

visited_positions = set()
while True:
    # print_field()
    visited_positions.add(guard_position)

    if guard_symbol == "^":
        next_position = (guard_position[0] - 1, guard_position[1])
        next_guard_symbol = ">"
    elif guard_symbol == ">":
        next_position = (guard_position[0], guard_position[1] + 1)
        next_guard_symbol = "v"
    elif guard_symbol == "v":
        next_position = (guard_position[0] + 1, guard_position[1])
        next_guard_symbol = "<"
    elif guard_symbol == "<":
        next_position = (guard_position[0], guard_position[1] - 1)
        next_guard_symbol = "^"
    else:
        raise Exception()

    if not is_valid_position(next_position):
        break
    if on_position(next_position) == OBSTRUCTION_SYMBOL:
        guard_symbol = next_guard_symbol
        update_symbol(guard_position, guard_symbol)
    else:
        update_symbol(guard_position, VISITED_SYMBOL)
        update_symbol(next_position, guard_symbol)
        guard_position = next_position


print(f"task 1 result: {len(visited_positions)}")
