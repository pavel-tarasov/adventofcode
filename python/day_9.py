task_1_result = 0
task_2_result = 0


class Rope:
    def __init__(self):
        self.head_position = [0, 0]
        self.tail_position = [0, 0]
        self.tail_position_history = set()

    def is_touching(self):
        if (
            abs(self.head_position[0] - self.tail_position[0]) <= 1
            and abs(self.head_position[1] - self.tail_position[1]) <= 1
        ):
            return True
        return False

    def move_head(self, direction):
        previous_head_position = self.head_position.copy()
        if direction == "R":
            self.head_position[0] += 1
        if direction == "L":
            self.head_position[0] -= 1
        if direction == "U":
            self.head_position[1] += 1
        if direction == "D":
            self.head_position[1] -= 1

        self.move_tail(previous_head_position)

    def move_tail(self, previous_head_position):
        if not self.is_touching():
            self.tail_position = previous_head_position
        self.track_tail()

    def track_tail(self):
        self.tail_position_history.add((self.tail_position[0], self.tail_position[1]))


rope = Rope()
with open("../inputs/day_9.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            print("file processed")
            break

        direction, steps = line.split(" ")
        for i in range(int(steps)):
            rope.move_head(direction)

print(f"task 1 result: {len(rope.tail_position_history)}")
print(f"task 2 result: {task_2_result}")
