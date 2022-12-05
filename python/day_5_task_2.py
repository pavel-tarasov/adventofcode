import queue


def move(stack_from, stack_to, number):
    tmp_stack = queue.LifoQueue()
    for i in range(number):
        val = stacks[stack_from - 1].get()
        tmp_stack.put(val)
    for i in range(number):
        val = tmp_stack.get()
        stacks[stack_to - 1].put(val)


def put_in_stack(index, val):
    if val not in ("", " "):
        stacks[index].put(val)


task_2_result = 0

stacks = [
    queue.LifoQueue(),
    queue.LifoQueue(),
    queue.LifoQueue(),
    queue.LifoQueue(),
    queue.LifoQueue(),
    queue.LifoQueue(),
    queue.LifoQueue(),
    queue.LifoQueue(),
    queue.LifoQueue(),
]
stack_lines = []
reading_moves = False
with open("../inputs/day_5.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            if reading_moves:
                print("file processed")
                break
            print("stack part processed")
            reading_moves = True

            for stack_line in reversed(stack_lines):
                print(
                    stack_line[1:2],
                    stack_line[5:6],
                    stack_line[9:10],
                    stack_line[13:14],
                    stack_line[17:18],
                    stack_line[21:22],
                    stack_line[25:26],
                    stack_line[29:30],
                    stack_line[33:34],
                )
                if stack_line[1:2] != "1":
                    put_in_stack(0, stack_line[1:2])
                    put_in_stack(1, stack_line[5:6])
                    put_in_stack(2, stack_line[9:10])
                    put_in_stack(3, stack_line[13:14])
                    put_in_stack(4, stack_line[17:18])
                    put_in_stack(5, stack_line[21:22])
                    put_in_stack(6, stack_line[25:26])
                    put_in_stack(7, stack_line[29:30])
                    put_in_stack(8, stack_line[33:34])

            continue

        if not reading_moves:
            stack_lines.append(line)

        if reading_moves:
            _, number, _, stack_from, _, stack_to = line.split(" ")
            move(int(stack_from), int(stack_to), int(number))

task_2_result = (
    stacks[0].get()
    + stacks[1].get()
    + stacks[2].get()
    + stacks[3].get()
    + stacks[4].get()
    + stacks[5].get()
    + stacks[6].get()
    + stacks[7].get()
    + stacks[8].get()
)
print(f"task 2 result: {task_2_result}")
