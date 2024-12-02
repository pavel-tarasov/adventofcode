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


def check_report_with_dampener(report: list[int]) -> bool:
    if check_report(report):
        return True
    else:
        for i in range(len(report)):
            new_report = report.copy()
            del new_report[i]
            if check_report(new_report):
                return True
    return False


result = 0
with open("input.txt") as file:
    while True:
        line = file.readline().rstrip("\n")

        if line == "":
            print("file processed")
            break

        current_report = list(map(int, line.split(" ")))
        if check_report_with_dampener(current_report):
            result += 1


print(f"task 2 result: {result}")
