task_1_result = 0
task_2_result = 0

with open("../inputs/day_6.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            print("file processed")
            break

print(f"task 1 result: {task_1_result}")
print(f"task 2 result: {task_2_result}")
