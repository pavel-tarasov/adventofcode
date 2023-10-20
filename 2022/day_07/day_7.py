task_1_result = 0
task_2_result = 0


class Directory:
    def __init__(self, name, parent_dir=None):
        self.name = name
        self.files = []
        self.child_dirs = []
        self.parent_dir = parent_dir
        self.size = 0
        self.total_size = 0

    def add(self, input):
        if input.split(" ")[0] == "dir":
            self.child_dirs.append(Directory(input.split(" ")[1], self))
        else:
            self.files.append(
                {"size": input.split(" ")[0], "name": input.split(" ")[1]}
            )
            self.size += int(input.split(" ")[0])

    def calc_total_size(self):
        indirect_size = 0
        for child in self.child_dirs:
            indirect_size += child.calc_total_size()
        self.total_size = self.size + indirect_size
        return self.total_size


def less_100000(node: Directory):
    size_sum = 0
    for child in node.child_dirs:
        size_sum += less_100000(child)
    if node.total_size <= 100000:
        return size_sum + node.total_size
    else:
        return size_sum


def best_to_remove(node: Directory, desired_space, top_size):
    for child in node.child_dirs:
        top_size = best_to_remove(child, desired_space, top_size)
    if desired_space <= node.total_size <= top_size:
        return node.total_size
    else:
        return top_size


with open("day_7.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            print("file processed")
            break

        if line.split(" ")[0] == "$":
            command = line.split(" ")[1]
            if command == "cd":
                target_dir_name = line.split(" ")[2]
                if target_dir_name == "/":
                    current_dir = Directory(target_dir_name)
                elif target_dir_name == "..":
                    current_dir = current_dir.parent_dir
                else:
                    for child in current_dir.child_dirs:
                        if child.name == target_dir_name:
                            current_dir = child
                            break
        else:
            current_dir.add(line)

while current_dir.parent_dir is not None:
    current_dir = current_dir.parent_dir

total_disk_size = 70000000
current_used_space = current_dir.calc_total_size()
free_space = total_disk_size - current_used_space
free_space_needed = 30000000
space_to_be_freed = free_space_needed - free_space

print(f"task 1 result: {less_100000(current_dir)}")
print(
    f"task 2 result: "
    f"{best_to_remove(current_dir, space_to_be_freed, current_used_space)}"
)
