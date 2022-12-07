task_1_result = 0
task_2_result = 0

with open("../inputs/day_9.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            print("file processed")
            break
