import re
from asyncio.constants import FLOW_CONTROL_HIGH_WATER_SSL_READ

result = None
memory_string = ""
with open("input.txt") as file:
    while True:
        line = file.readline()
        memory_string += line

        if line == "":
            print("file processed")
            break

# print(memory_string)

commands = []
for match in re.finditer("mul\(\d+,\d+\)", memory_string):
    commands.append({"position": match.start(), "expression": match.group(0)})
# print(commands)

control_commands = [{"position": 0, "enabled": True}]
for match in re.finditer("do\(\)", memory_string):
    control_commands.append({"position": match.start(), "enabled": True})
    for match in re.finditer("don't\(\)", memory_string):
        control_commands.append({"position": match.start(), "enabled": False})
control_commands.sort(key=lambda e: e["position"])
# print(control_commands)

sum = 0
current_control_position = 0
for command in commands:
    enabled = None
    for i in range(current_control_position, len(control_commands)):
        if (control_commands[i]["position"] <= command["position"]) and (
            i == len(control_commands) - 1
            or command["position"] <= control_commands[i + 1]["position"]
        ):
            enabled = control_commands[i]["enabled"]
            current_control_position = i
            break
    assert enabled is not None
    if enabled:
        a, b = list(map(int, command["expression"].strip("mul()").split(",")))
        sum += a * b

print(f"task 2 result: {sum}")
