task_1_result = 0

grid = []
with open("../inputs/day_8.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            print("file processed")
            break
        grid.append(list(line))

y_max = len(grid)
x_max = len(grid[0])
for i in range(y_max):
    for j in range(x_max):
        # edge
        if i in (0, y_max - 1) or j in (0, x_max - 1):
            task_1_result += 1
            continue

        # up
        for k in reversed(range(i)):
            if grid[i][j] > grid[k][j]:
                visible_up = True
            else:
                visible_up = False
                break
        # down
        for k in range(i + 1, y_max):
            if grid[i][j] > grid[k][j]:
                visible_down = True
            else:
                visible_down = False
                break
        # left
        for k in reversed(range(j)):
            if grid[i][j] > grid[i][k]:
                visible_left = True
            else:
                visible_left = False
                break
        # right
        for k in range(j + 1, x_max):
            if grid[i][j] > grid[i][k]:
                visible_right = True
            else:
                visible_right = False
                break

        if visible_up or visible_down or visible_left or visible_right:
            task_1_result += 1

print(f"task 1 result: {task_1_result}")
