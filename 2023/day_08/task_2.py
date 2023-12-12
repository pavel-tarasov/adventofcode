from typing import Self


class Node:
    def __init__(self, name: str, left_node: Self = None, right_node: Self = None):
        self.name = name
        self.left_node = left_node
        self.right_node = right_node
        if self.name[-1] == "A":
            self.start_node = True
        else:
            self.start_node = False
        if self.name[-1] == "Z":
            self.end_node = True
        else:
            self.end_node = False


def get_node(name: str) -> Node:
    if node := nodes.get(name):
        return node
    else:
        nodes[name] = Node(name=name)
        return nodes[name]


def prime_factorization(number: int) -> dict[int, int]:
    prime_numbers = []
    factor = 2
    while number > 1:
        if number % factor == 0:
            prime_numbers.append(factor)
            number //= factor
        else:
            factor += 1

    prime_numbers_powers = {}
    for prime_number in prime_numbers:
        if prime_numbers_powers.get(prime_number) is None:
            prime_numbers_powers[prime_number] = 1
        else:
            prime_numbers_powers[prime_number] += 1

    return prime_numbers_powers


def find_lcm(numbers: list[int]) -> int:
    lcm = 1
    powers = [prime_factorization(number) for number in numbers]

    prime_numbers = set()
    for power in powers:
        prime_numbers.update(list(power.keys()))

    for prime_number in prime_numbers:
        highest_power = max([power.get(prime_number, 0) for power in powers])
        lcm *= prime_number**highest_power

    return lcm


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

start_nodes = [node for node in nodes.values() if node.start_node]
current_nodes = start_nodes
ends = {}
i = 0
while True:
    ii = i % len(instructions)
    instruction = instructions[ii]

    for j in range(len(current_nodes)):
        if current_nodes[j].end_node:
            if ends.get(j) is None:
                ends[j] = i

        if instruction == "L":
            current_nodes[j] = current_nodes[j].left_node
        if instruction == "R":
            current_nodes[j] = current_nodes[j].right_node

    if len(ends) == len(current_nodes):
        break

    i += 1

print(i)
print(f"{ends=}")

print(f"task 2 result: {find_lcm(list(ends.values()))}")
