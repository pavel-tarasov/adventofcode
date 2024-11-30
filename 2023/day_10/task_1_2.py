import copy
from typing import Self


class Maze:
    def __init__(self, maze_map: list[str]):
        self.map = maze_map
        self.max_row = len(maze_map) - 1
        self.max_column = len(maze_map[0]) - 1

    def __str__(self):
        result = ""
        for row in self.map:
            result += row + "\n"
        return result


class Position:
    def __init__(self, maze: Maze, row: int, column: int):
        self.maze = maze
        self.row = row
        self.column = column
        self._update_tile()

    def __str__(self):
        return f"{self.tile} ({self.row}:{self.column})"

    def coordinates(self) -> str:
        return f"{self.row}:{self.column}"

    def _update_tile(self):
        self.tile = self.maze.map[self.row][self.column]

    def check_north_path(self) -> bool:
        if self.row - 1 >= 0:
            if self.tile == "S":
                new_position = self.maze.map[self.row - 1][self.column]
                if new_position in ("|", "7", "F"):
                    return True
                else:
                    return False
            else:
                if self.tile in ("|", "L", "J"):
                    return True
                else:
                    return False
        else:
            return False

    def check_north_tile(self) -> bool:
        if self.row - 1 >= 0:
            return True
        else:
            return False

    def to_north(self) -> Self:
        new_position = copy.copy(self)
        new_position.row -= 1
        new_position._update_tile()
        return new_position

    def check_west_path(self) -> bool:
        if self.column - 1 >= 0:
            if self.tile == "S":
                new_position = self.maze.map[self.row][self.column - 1]
                if new_position in ("-", "L", "F"):
                    return True
                else:
                    return False
            else:
                if self.tile in ("-", "J", "7"):
                    return True
                else:
                    return False
        else:
            return False

    def check_west_tile(self) -> bool:
        if self.column - 1 >= 0:
            return True
        else:
            return False

    def to_west(self) -> Self:
        new_position = copy.copy(self)
        new_position.column -= 1
        new_position._update_tile()
        return new_position

    def check_south_path(self) -> bool:
        if self.row + 1 <= self.maze.max_row:
            if self.tile == "S":
                new_position = self.maze.map[self.row + 1][self.column]
                if new_position in ("|", "L", "J"):
                    return True
                else:
                    return False
            else:
                if self.tile in ("|", "7", "F"):
                    return True
                else:
                    return False
        else:
            return False

    def check_south_tile(self) -> bool:
        if self.row + 1 <= self.maze.max_row:
            return True
        else:
            return False

    def to_south(self) -> Self:
        new_position = copy.copy(self)
        new_position.row += 1
        new_position._update_tile()
        return new_position

    def check_east_path(self) -> bool:
        if self.column + 1 <= self.maze.max_column:
            if self.tile == "S":
                new_position = self.maze.map[self.row][self.column + 1]
                if new_position in ("-", "J", "7"):
                    return True
                else:
                    return False
            else:
                if self.tile in ("-", "L", "F"):
                    return True
                else:
                    return False
        else:
            return False

    def check_east_tile(self) -> bool:
        if self.column + 1 <= self.maze.max_column:
            return True
        else:
            return False

    def to_east(self) -> Self:
        new_position = copy.copy(self)
        new_position.column += 1
        new_position._update_tile()
        return new_position

    def check_directions(self) -> list:
        directions = []
        if self.check_north_path():
            directions.append("north")
        if self.check_west_path():
            directions.append("west")
        if self.check_south_path():
            directions.append("south")
        if self.check_east_path():
            directions.append("east")
        return directions


def fill_maze(
    maze_f: Maze, path: dict[str:Position], current_position: Position
) -> None:
    if maze_f.map[current_position.row][
        current_position.column
    ] != "O" and not path.get(current_position.coordinates()):
        new_row = (
            maze_f.map[current_position.row][: current_position.column]
            + "O"
            + maze_f.map[current_position.row][current_position.column + 1 :]
        )
        # print(maze.map[position.row])
        # print(new_row)
        maze_f.map[current_position.row] = new_row

        # next_position_f = None
        if current_position.check_north_tile():
            next_position_f = current_position.to_north()
            fill_maze(maze_f, path, next_position_f)
        if current_position.check_west_tile():
            next_position_f = current_position.to_west()
            fill_maze(maze_f, path, next_position_f)
        if current_position.check_south_tile():
            next_position_f = current_position.to_south()
            fill_maze(maze_f, path, next_position_f)
        if current_position.check_east_tile():
            next_position_f = current_position.to_east()
            fill_maze(maze_f, path, next_position_f)

        # if next_position_f is None:
        #     raise Exception("WTF 3")


start_position = None
maze_map = []
with open("test_input_3.txt") as file:
    while True:
        line = file.readline().rstrip("\n")

        if line == "":
            print("file processed")
            break

        maze_map.append(line)

maze = Maze(maze_map=maze_map)
print(maze)

for i, row in enumerate(maze.map):
    if "S" in row:
        start_position = Position(maze=maze, row=i, column=row.find("S"))


positions = {start_position.coordinates(): start_position}
position = start_position
source_position = None
i = 0
while True:
    # if i > 100:
    #     break

    if str(position) == str(start_position) and i > 0:
        break

    # print(
    #     f"position: {position}, "
    #     f"directions: {len(position.check_directions())} ({position.check_directions()})"
    # )
    if len(position.check_directions()) > 2:
        raise Exception("WTF 1")

    next_position = None
    if next_position is None and position.check_north_path():
        if str(source_position) != str(position.to_north()):
            next_position = position.to_north()
            # print("to north")
    if next_position is None and position.check_west_path():
        if str(source_position) != str(position.to_west()):
            next_position = position.to_west()
            # print("to west")
    if next_position is None and position.check_south_path():
        if str(source_position) != str(position.to_south()):
            next_position = position.to_south()
            # print("to south")
    if next_position is None and position.check_east_path():
        if str(source_position) != str(position.to_east()):
            next_position = position.to_east()
            # print("to east")

    if next_position is None:
        raise Exception("WTF 2")

    positions[position.coordinates()] = position

    i += 1
    source_position = position
    position = next_position

# print(i)
if i % 2 == 0:
    result = i // 2
else:
    result = (i // 2) + 1

print(f"task 1 result: {result}")

for i, row in enumerate(maze.map):
    for j, tile in enumerate(row):
        if i == 0 or i == maze.max_row or j == 0 or j == maze.max_column:
            pos = Position(maze=maze, row=i, column=j)
            # if not positions.get(pos.coordinates()):
            #     print(pos)
            fill_maze(maze, positions, pos)
print(maze)


result_2 = 0
print(f"task 2 result: {result_2}")
