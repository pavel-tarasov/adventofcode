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

bad_updates = []
for update in updates:
    pages_before = set()
    for j, page in enumerate(update):
        if ordering_rules.get(page):
            pages_expected_after = ordering_rules[page]
            if pages_expected_after.intersection(pages_before) != set():
                bad_updates.append(update)
                break
        pages_before.add(page)

new_updates = []
for i, update in enumerate(bad_updates):
    print(update)
    new_update = []
    pages_before = dict()
    for j, page in enumerate(update):
        print(page)
        if ordering_rules.get(page):
            pages_expected_after = ordering_rules[page]
            print(pages_expected_after)
            wrong_pages = {
                new_page: k
                for k, new_page in enumerate(new_update)
                if new_page in pages_expected_after
            }
            if wrong_pages != {}:
                left_position = min(wrong_pages.values())
                new_update.insert(left_position, page)
                continue
        new_update.append(page)
        pages_before[page] = j
    new_updates.append(new_update)

print("------------")
print("new updates:")
for update in new_updates:
    print(update)
    assert len(update) % 2 == 1
    result += update[len(update) // 2]

print(f"task 2 result: {result}")
