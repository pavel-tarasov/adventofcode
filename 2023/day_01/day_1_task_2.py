DIGITS = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "0": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_all(string: str, substring: str):
    index = string.find(substring)
    while index != -1:
        yield index
        index = string.find(substring, index + len(substring))


calibration_values = []
with open("input.txt") as file:
    while True:
        line = file.readline()

        if line == "":
            print("file processed")
            break

        digits_in_line = []
        for digit in DIGITS.keys():
            current_digit_occurrences = list(find_all(line, digit))

            digits_in_line.extend(
                [(digit_index, digit) for digit_index in current_digit_occurrences]
            )

        first_digit = DIGITS[sorted(digits_in_line, key=lambda a: a[0])[0][1]]
        last_digit = DIGITS[
            sorted(digits_in_line, key=lambda a: a[0], reverse=True)[0][1]
        ]

        if first_digit and last_digit:
            calibration_values.append(int(str(first_digit) + str(last_digit)))


print(f"task 2 result: {sum(calibration_values)}")
