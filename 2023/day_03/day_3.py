NUMBERS = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
DOT = 46


class Number:
    def __init__(
        self,
        digits: list[str],
        start_position: int,
        end_position: int,
        line_number: int,
    ):
        self.value = int("".join(digits))
        self.start_position = start_position
        self.end_position = end_position
        self.line_number = line_number

    def __str__(self):
        return f"{self.value} ({self.line_number}:{self.start_position}-{self.end_position})"


class Char:
    def __init__(self, char: str, position: int, line_number: int):
        self.char = char
        self.position = position
        self.line_number = line_number

    def __str__(self):
        return f"{self.char} ({self.line_number}:{self.position})"


line = ""
i = 0
number_objects = []
char_objects = []
with open("input.txt") as file:
    while True:
        i += 1
        line = file.readline().rstrip("\n")

        if line == "":
            print("file processed")
            break

        current_number_digits = []
        current_number_start = None
        for j, char in enumerate(line, start=1):
            if ord(char) == DOT:
                if current_number_start:
                    number_objects.append(
                        Number(
                            digits=current_number_digits,
                            start_position=current_number_start,
                            end_position=j - 1,
                            line_number=i,
                        )
                    )
                    current_number_digits = []
                    current_number_start = None
            elif ord(char) in NUMBERS:
                current_number_digits.append(char)
                if not current_number_start:
                    current_number_start = j
            else:
                if current_number_start:
                    number_objects.append(
                        Number(
                            digits=current_number_digits,
                            start_position=current_number_start,
                            end_position=j - 1,
                            line_number=i,
                        )
                    )
                    current_number_digits = []
                    current_number_start = None
                char_objects.append(Char(char=char, position=j, line_number=i))

        if current_number_start:
            number_objects.append(
                Number(
                    digits=current_number_digits,
                    start_position=current_number_start,
                    end_position=j,
                    line_number=i,
                )
            )

selected_numbers = []
for number_object in number_objects:
    for char_object in char_objects:
        if char_object.line_number in range(
            number_object.line_number - 1, number_object.line_number + 2
        ) and char_object.position in range(
            number_object.start_position - 1, number_object.end_position + 2
        ):
            selected_numbers.append(number_object)
            break

gears = []
for char_object in char_objects:
    if char_object.char == "*":
        neighbours = []
        for number_object in number_objects:
            if char_object.line_number in range(
                number_object.line_number - 1, number_object.line_number + 2
            ) and char_object.position in range(
                number_object.start_position - 1, number_object.end_position + 2
            ):
                neighbours.append(number_object)
        if len(neighbours) == 2:
            gears.append(neighbours[0].value * neighbours[1].value)


print(f"task 1 result: {sum([number.value for number in selected_numbers])}")
print(f"task 2 result: {sum(gears)}")
