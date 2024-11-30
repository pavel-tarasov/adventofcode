import copy


class Position:
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    def __str__(self):
        return f"x position: {self.x}; y position: {self.y}"


class Map:
    def __init__(self):
        self.grid = []

    def add_line(self, line):
        self.grid.append(list(line))

    def __str__(self):
        return "\n".join(["".join([str(char) for char in row]) for row in self.grid])


def find_path(map: Map, start_position: Position, target_position: Position) -> int:
    # visit_map=copy.deepcopy(map)
    visit_map = Map()
    height_map = Map()
    for row in map.grid:
        visit_row = []
        height_row = []
        for char in row:
            if char == "S":
                visit_row.append(0)
                height_row.append(ord("a"))
            elif char == "E":
                visit_row.append(-1)
                height_row.append(ord("z"))
            else:
                visit_row.append(-1)
                height_row.append(ord(char))
        visit_map.add_line(visit_row)
        height_map.add_line(height_row)

    print(visit_map)

    wave = [start_position]
    while True:
        for pos in wave:
            print(height_map.grid[pos.x][pos.y])
            print(height_map.grid[pos.x - 1][pos.y - 1])


start_position = None
target_position = None
map = Map()
x = 0
with open("day_12_test.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            print("file processed")
            break

        map.add_line(line)

        y = 0
        for char in list(line):
            if char == "S":
                start_position = Position(x, y)
            elif char == "E":
                target_position = Position(x, y)
            y += 1
        x += 1

print(map)

print(start_position)
print(target_position)

result = find_path(map, start_position, target_position)
print(result)
