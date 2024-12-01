result = None
list_a = []
list_b = []
occurrences = []
with open("input.txt") as file:
    while True:
        line = file.readline()

        if line == "":
            print("file processed")
            break

        # print(line)
        a, b = line.split("   ")
        list_a.append(int(a))
        list_b.append(int(b))

# print(list_a[0])
# print(list_b[0])
assert len(list_a) == len(list_b)
# list_a.sort()
# list_b.sort()
for a in list_a:
    count = list_b.count(a)
    print(f"{a} occurs {count} times")
    occurrences.append(a * count)

result = sum(occurrences)
print(f"task 2 result: {result}")
