import re


result = None
memory_string = ""
with open("input.txt") as file:
    while True:
        line = file.readline()
        memory_string += line

        if line == "":
            print("file processed")
            break

print(memory_string)

commands = re.findall("mul\(\d+,\d+\)", memory_string)
print(commands)

sum = 0
for command in commands:
    a, b = list(map(int, command.strip("mul()").split(",")))
    sum += a * b

print(f"task 1 result: {sum}")
