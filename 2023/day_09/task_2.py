def extrapolate_backwards(numbers: list[int]) -> int:
    if set(numbers) == {0}:
        return 0
    else:
        diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
        return numbers[0] - extrapolate_backwards(diffs)


sum_ = 0
with open("input.txt") as file:
    while True:
        line = file.readline().rstrip("\n")

        if line == "":
            print("file processed")
            break

        initial_numbers = list(map(int, line.split(" ")))
        sum_ += extrapolate_backwards(initial_numbers)


print(f"task 2 result: {sum_}")
