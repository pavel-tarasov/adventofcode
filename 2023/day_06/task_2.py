with open("input.txt") as file:
    while True:
        line = file.readline()

        if line == "":
            print("file processed")
            break

        if line.startswith("Time:"):
            race_time = int(
                "".join([el.strip(" ") for el in line.split(":")[1].split()])
            )

        if line.startswith("Distance:"):
            race_max_distance = int(
                "".join([el.strip(" ") for el in line.split(":")[1].split()])
            )

winning_combination = 0
for i in range(race_time + 1):
    hold_time = i
    boat_speed = i
    moving_time = race_time - hold_time
    distance = moving_time * boat_speed
    if distance > race_max_distance:
        winning_combination += 1

print(f"task 2 result: {winning_combination}")
