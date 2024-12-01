result = None
list_a = []
list_b = []
diffs = []
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
list_a.sort()
list_b.sort()
for i, a in enumerate(list_a):
    b = list_b[i]
    # print(f"abs({a} - {b}) = {abs(a - b)}")
    diffs.append(abs(a - b))

result = sum(diffs)
print(f"task 1 result: {result}")
