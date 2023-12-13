def extrapolate(numbers: list[int]) -> int:
    if set(numbers) == {0}:
        return 0
    else:
        diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
        return numbers[-1] + extrapolate(diffs)


sum_ = 0
with open("input.txt") as file:
    while True:
        line = file.readline().rstrip("\n")

        if line == "":
            print("file processed")
            break

        initial_numbers = list(map(int, line.split(" ")))
        sum_ += extrapolate(initial_numbers)


print(f"task 1 result: {sum_}")
