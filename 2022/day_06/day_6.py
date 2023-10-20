from collections import deque

task_1_result = 0
task_2_result = 0

with open("day_6.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            print("file processed")
            break
        signal = list(line)

window_packet = deque(maxlen=4)
window_message = deque(maxlen=14)
for i, character in enumerate(signal, start=1):
    window_packet.append(character)
    window_message.append(character)
    if len(set(window_packet)) == 4 and task_1_result == 0:
        print("start-of-packet marker is detected!")
        task_1_result = i

    if len(set(window_message)) == 14 and task_2_result == 0:
        print("start-of-message marker is detected!")
        task_2_result = i

print(f"task 1 result: {task_1_result}")
print(f"task 2 result: {task_2_result}")
