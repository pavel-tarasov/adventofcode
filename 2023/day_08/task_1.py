from typing import Self


class Node:
    def __init__(self, name: str, left_node: Self = None, right_node: Self = None):
        self.name = name
        self.left_node = left_node
        self.right_node = right_node


def get_node(name: str) -> Node:
    if node := nodes.get(name):
        return node
    else:
        nodes[name] = Node(name=name)
        return nodes[name]


instructions = []
nodes = {}
i = 0
with open("input.txt") as file:
    while True:
        i += 1
        line = file.readline().rstrip("\n")

        if line == "" and i > 2:
            print("file processed")
            break

        if i == 1:
            instructions.extend(line)

        if i > 2:
            node_name, node_children = line.split(" = ")
            left_node, right_node = node_children.strip(" ()").split(", ")
            node = get_node(node_name)
            if not node.left_node:
                node.left_node = get_node(left_node)
            if not node.right_node:
                node.right_node = get_node(right_node)

i = 0
start_node = nodes["AAA"]
current_node = start_node
end_node = nodes["ZZZ"]
while True:
    ii = i % len(instructions)
    instruction = instructions[ii]

    if current_node == end_node:
        break

    if instruction == "L":
        current_node = current_node.left_node
    if instruction == "R":
        current_node = current_node.right_node

    i += 1

print(f"task 1 result: {i}")
