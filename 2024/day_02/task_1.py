def check_report(report: list[int]) -> bool:
    increasing = False
    decreasing = False
    for i in range(1, len(report)):
        previous_level = report[i - 1]
        current_level = report[i]
        diff = current_level - previous_level
        if diff < 0:
            decreasing = True
        elif diff > 0:
            increasing = True
        else:
            return False
        if diff not in (-3, -2, -1, 1, 2, 3):
            return False
        if increasing and decreasing:
            return False
    return True


result = 0
with open("input.txt") as file:
    while True:
        line = file.readline().rstrip("\n")

        if line == "":
            print("file processed")
            break

        current_report = list(map(int, line.split(" ")))
        if check_report(current_report):
            result += 1


print(f"task 1 result: {result}")
