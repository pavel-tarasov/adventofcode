food = {}
current_elf = 1
with open("../inputs/day_1.txt") as file:
    while True:
        line = file.readline()

        if line == "\n":
            print("go to next elf")
            current_elf += 1
            continue

        if line == "":
            print("file processed")
            break

        val = int(line.replace("\n", ""))

        if food.get(current_elf) is None:
            food[current_elf] = val
        else:
            food[current_elf] += val

food_sorted = sorted(food.values(), reverse=True)
print(food_sorted)

print(f"task 1 result: {food_sorted[0]}")
print(f"task 2 result: {sum(food_sorted[0:3])}")
