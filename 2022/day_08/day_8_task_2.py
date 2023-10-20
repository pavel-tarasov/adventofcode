task_2_result = 0

grid = []
with open("day_8.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            print("file processed")
            break
        grid.append(list(line))

y_max = len(grid)
x_max = len(grid[0])
scenic_score = []
for i in range(y_max):
    for j in range(x_max):
        # up
        visible_up = 0
        for k in reversed(range(i)):
            if grid[i][j] > grid[k][j]:
                visible_up += 1
            else:
                visible_up += 1
                break
        # down
        visible_down = 0
        for k in range(i + 1, y_max):
            if grid[i][j] > grid[k][j]:
                visible_down += 1
            else:
                visible_down += 1
                break
        # left
        visible_left = 0
        for k in reversed(range(j)):
            if grid[i][j] > grid[i][k]:
                visible_left += 1
            else:
                visible_left += 1
                break
        # right
        visible_right = 0
        for k in range(j + 1, x_max):
            if grid[i][j] > grid[i][k]:
                visible_right += 1
            else:
                visible_right += 1
                break

        scenic_score.append(visible_up * visible_down * visible_left * visible_right)

print(f"task 2 result: {max(scenic_score)}")
