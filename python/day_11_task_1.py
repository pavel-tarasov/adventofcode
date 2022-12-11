import math


class Monkey:
    def __init__(
        self,
        number: int,
        items: list,
        operation: str,
        test_value: int,
        target_true: int,
        target_false: int,
    ):
        self.number = number
        self.items = items
        self.operation = operation
        self.test_value = test_value
        self.target_true = target_true
        self.target_false = target_false
        self.times_inspected = 0

    def turn(self):
        while len(self.items) != 0:
            # inspect
            old = self.items[0]
            new_worry_level = eval(self.operation)
            # get bored
            final_worry_level = math.floor(new_worry_level / 3)
            # check
            if final_worry_level % self.test_value == 0:
                monkeys[self.target_true].get_item(final_worry_level)
            else:
                monkeys[self.target_false].get_item(final_worry_level)
            del self.items[0]
            self.times_inspected += 1

    def get_item(self, item):
        self.items.append(item)


monkeys = {}
with open("../inputs/day_11.txt") as file:
    while True:
        lines = []
        lines.append(file.readline().replace("\n", ""))
        lines.append(file.readline().replace("\n", ""))
        lines.append(file.readline().replace("\n", ""))
        lines.append(file.readline().replace("\n", ""))
        lines.append(file.readline().replace("\n", ""))
        lines.append(file.readline().replace("\n", ""))
        lines.append(file.readline().replace("\n", ""))

        if lines[0] == "":
            print("file processed")
            break

        number_parsed = int(lines[0].split(" ")[1][:-1])
        items_parsed = [
            int(item) for item in lines[1].replace("  Starting items: ", "").split(", ")
        ]
        operation_parsed = lines[2].replace("  Operation: new = ", "")
        test_value_parsed = int(lines[3].replace("  Test: divisible by ", ""))
        target_true_parsed = int(lines[4].replace("    If true: throw to monkey ", ""))
        target_false_parsed = int(
            lines[5].replace("    If false: throw to monkey ", "")
        )
        monkeys[number_parsed] = Monkey(
            number=number_parsed,
            items=items_parsed,
            operation=operation_parsed,
            test_value=test_value_parsed,
            target_true=target_true_parsed,
            target_false=target_false_parsed,
        )

print(sorted(monkeys.items()))

for round_index in range(20):
    print(f"round: {round_index + 1}")
    for index, monkey in sorted(monkeys.items()):
        monkey.turn()
    for index, monkey in sorted(monkeys.items()):
        print(f"  Monkey {monkey.number}: {monkey.items}")

for index, monkey in sorted(monkeys.items()):
    print(f"Monkey {monkey.number} inspected items {monkey.times_inspected} times.")

inspections_list = sorted(
    [monkey.times_inspected for monkey in monkeys.values()], reverse=True
)

print(f"task 1 result: {inspections_list[0] * inspections_list[1]}")
