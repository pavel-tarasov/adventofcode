result = 0
ordering_rules = {}
updates = []
with open("input.txt") as file:
    rules_ended = False
    while True:
        line = file.readline().rstrip("\n")

        if line == "":
            if not rules_ended:
                rules_ended = True
                continue
            else:
                print("file processed")
                break

        if not rules_ended:
            number_before, number_after = tuple(map(int, line.split("|")))
            if ordering_rules.get(number_before):
                if number_after in ordering_rules[number_before]:
                    raise Exception("Duplicated rules")
                else:
                    ordering_rules[number_before].add(number_after)
            else:
                ordering_rules[number_before] = {number_after}
        else:
            updates.append(list(map(int, line.split(","))))

for update in updates:
    pages_before = set()
    bad_update = False
    for i, page in enumerate(update):
        if ordering_rules.get(page):
            pages_expected_after = ordering_rules[page]
            if pages_expected_after.intersection(pages_before) != set():
                bad_update = True
                break
        pages_before.add(page)

    if not bad_update:
        assert len(update) % 2 == 1
        result += update[len(update) // 2]

print(f"task 1 result: {result}")
