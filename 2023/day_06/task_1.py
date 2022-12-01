time_list = []
distance_list = []
with open("input.txt") as file:
    while True:
        line = file.readline()

        if line == "":
            print("file processed")
            break

        if line.startswith("Time:"):
            time_list = [int(el.strip(" ")) for el in line.split(":")[1].split()]

        if line.startswith("Distance:"):
            distance_list = [int(el.strip(" ")) for el in line.split(":")[1].split()]

ways_to_win = []
for race_index in range(len(time_list)):
    race_time = time_list[race_index]
    race_max_distance = distance_list[race_index]

    winning_combination = 0
    for i in range(race_time + 1):
        hold_time = i
        boat_speed = i
        moving_time = race_time - hold_time
        distance = moving_time * boat_speed
        print(hold_time, distance)
        if distance > race_max_distance:
            winning_combination += 1
    ways_to_win.append(winning_combination)

result = 1
for w in ways_to_win:
    result *= w

print(f"task 1 result: {result}")
