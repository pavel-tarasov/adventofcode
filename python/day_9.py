class Rope:
    def __init__(self, length):
        self.body = []
        for i in range(length):
            self.body.append([0, 0])
        self.tail_position_history = set()

    def is_touching(self, index_1, index_2):
        if (
            abs(self.body[index_1][0] - self.body[index_2][0]) <= 1
            and abs(self.body[index_1][1] - self.body[index_2][1]) <= 1
        ):
            return True
        return False

    def is_broken(self):
        for index in range(len(self.body) - 1):
            if not self.is_touching(index, index + 1):
                return True
        return False

    def is_same_column(self, index_1, index_2):
        if self.body[index_1][0] == self.body[index_2][0]:
            return True
        return False

    def is_same_row(self, index_1, index_2):
        if self.body[index_1][1] == self.body[index_2][1]:
            return True
        return False

    def move_head(self, direction):
        head = self.body[0]
        if direction == "R":
            head[0] += 1
        elif direction == "L":
            head[0] -= 1
        elif direction == "U":
            head[1] += 1
        elif direction == "D":
            head[1] -= 1

        self.move_next(0, direction)

    def move_next(self, prev_el_index, direction):
        curr_el_index = prev_el_index + 1
        if curr_el_index < len(self.body):
            if not self.is_touching(prev_el_index, curr_el_index):
                if self.is_same_row(prev_el_index, curr_el_index):
                    if self.body[curr_el_index][0] < self.body[prev_el_index][0]:
                        self.body[curr_el_index][0] += 1
                    else:
                        self.body[curr_el_index][0] -= 1
                elif self.is_same_column(prev_el_index, curr_el_index):
                    if self.body[curr_el_index][1] < self.body[prev_el_index][1]:
                        self.body[curr_el_index][1] += 1
                    else:
                        self.body[curr_el_index][1] -= 1
                else:  # diagonal
                    if (  # U R
                        self.body[curr_el_index][0] < self.body[prev_el_index][0]
                        and self.body[curr_el_index][1] < self.body[prev_el_index][1]
                    ):
                        self.body[curr_el_index][0] += 1
                        self.body[curr_el_index][1] += 1
                    elif (  # U L
                        self.body[curr_el_index][0] > self.body[prev_el_index][0]
                        and self.body[curr_el_index][1] < self.body[prev_el_index][1]
                    ):
                        self.body[curr_el_index][0] -= 1
                        self.body[curr_el_index][1] += 1
                    elif (  # D L
                        self.body[curr_el_index][0] > self.body[prev_el_index][0]
                        and self.body[curr_el_index][1] > self.body[prev_el_index][1]
                    ):
                        self.body[curr_el_index][0] -= 1
                        self.body[curr_el_index][1] -= 1
                    elif (  # D R
                        self.body[curr_el_index][0] < self.body[prev_el_index][0]
                        and self.body[curr_el_index][1] > self.body[prev_el_index][1]
                    ):
                        self.body[curr_el_index][0] += 1
                        self.body[curr_el_index][1] -= 1

            if curr_el_index == len(self.body) - 1:
                self.track_tail()
            self.move_next(curr_el_index, direction)

    def track_tail(self):
        self.tail_position_history.add((self.body[-1][0], self.body[-1][1]))


rope_2 = Rope(2)
rope_10 = Rope(10)
with open("../inputs/day_9.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            print("file processed")
            break

        direction, steps = line.split(" ")
        for i in range(int(steps)):
            rope_2.move_head(direction)
            rope_10.move_head(direction)

print(f"task 1 result: {len(rope_2.tail_position_history)}")
print(f"task 2 result: {len(rope_10.tail_position_history)}")
