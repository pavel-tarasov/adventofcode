def check_word(
    position_1: tuple[int, int],
    position_2: tuple[int, int],
    position_3: tuple[int, int],
    position_4: tuple[int, int],
    position_5: tuple[int, int],
) -> (
    tuple[
        tuple[int, int],
        tuple[int, int],
        tuple[int, int],
        tuple[int, int],
        tuple[int, int],
    ]
    | None
):
    """
    M.S
    .A.
    M.S
    """
    global input_data
    try:
        if (
            position_1[1] < 0
            or position_2[1] < 0
            or position_3[1] < 0
            or position_4[1] < 0
            or position_5[1] < 0
        ):
            return None

        letter_1 = input_data[position_1[0]][position_1[1]]
        letter_2 = input_data[position_2[0]][position_2[1]]
        letter_3 = input_data[position_3[0]][position_3[1]]
        letter_4 = input_data[position_4[0]][position_4[1]]
        letter_5 = input_data[position_5[0]][position_5[1]]

        if letter_1 + letter_2 + letter_3 + letter_4 + letter_5 == "MSAMS":
            return (position_1, position_2, position_3, position_4, position_5)
        else:
            return None
    except IndexError:
        return None


def check_cell(position: tuple[int, int]):
    global input_data
    words_found = set()

    # M.S
    # .A.
    # M.S
    correct_word = check_word(
        position_1=(position[0], position[1]),
        position_2=(position[0], position[1] + 2),
        position_3=(position[0] + 1, position[1] + 1),
        position_4=(position[0] + 2, position[1]),
        position_5=(position[0] + 2, position[1] + 2),
    )
    if correct_word is not None:
        words_found.add(correct_word)

    # S.M
    # .A.
    # S.M
    correct_word = check_word(
        position_1=(position[0], position[1]),
        position_2=(position[0], position[1] - 2),
        position_3=(position[0] + 1, position[1] - 1),
        position_4=(position[0] + 2, position[1]),
        position_5=(position[0] + 2, position[1] - 2),
    )
    if correct_word is not None:
        words_found.add(correct_word)

    # S.S
    # .A.
    # M.M
    correct_word = check_word(
        position_1=(position[0], position[1]),
        position_2=(position[0] - 2, position[1]),
        position_3=(position[0] - 1, position[1] + 1),
        position_4=(position[0], position[1] + 2),
        position_5=(position[0] - 2, position[1] + 2),
    )
    if correct_word is not None:
        words_found.add(correct_word)

    # M.M
    # .A.
    # S.S
    correct_word = check_word(
        position_1=(position[0], position[1]),
        position_2=(position[0] + 2, position[1]),
        position_3=(position[0] + 1, position[1] + 1),
        position_4=(position[0], position[1] + 2),
        position_5=(position[0] + 2, position[1] + 2),
    )
    if correct_word is not None:
        words_found.add(correct_word)

    return words_found


input_data = []
with open("input.txt") as file:
    while True:
        line = file.readline().rstrip("\n")

        input_data.append(line)

        if line == "":
            print("file processed")
            break

words_found_total = set()
for i, line in enumerate(input_data):
    for j, char in enumerate(line):
        print(char, end="")
        new_words = check_cell(position=(i, j))
        words_found_total |= new_words
    print("")

for word in sorted(list(words_found_total)):
    print(word)

print(f"task 1 result: {len(words_found_total)}")
