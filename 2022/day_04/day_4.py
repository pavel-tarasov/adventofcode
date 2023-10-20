sum_1 = 0
sum_2 = 0
with open("day_4.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            print("file processed")
            break

        range_1, range_2 = line.split(",")
        range_1_left, range_1_right = map(int, range_1.split("-"))
        range_2_left, range_2_right = map(int, range_2.split("-"))

        if (range_1_left <= range_2_left and range_1_right >= range_2_right) or (
            range_2_left <= range_1_left and range_2_right >= range_1_right
        ):
            sum_1 += 1

        if (
            (range_1_right >= range_2_left >= range_1_left)
            or (range_1_right >= range_2_right >= range_1_left)
            or (range_2_left <= range_1_right <= range_2_right)
            or (range_2_left <= range_1_left <= range_2_right)
        ):
            sum_2 += 1

print(f"task 1 result: {sum_1}")
print(f"task 2 result: {sum_2}")
