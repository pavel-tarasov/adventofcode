LIMITS = {"red": 12, "green": 13, "blue": 14}


def check_cubes(current_set: dict) -> bool:
    possible = True
    for key, value in current_set.items():
        if value > LIMITS[key]:
            possible = False
    return possible


def update_minimal_set(minimal_set: dict, current_set: dict):
    for key, value in current_set.items():
        if value > minimal_set[key]:
            minimal_set[key] = value


possible_games_ids = []
sets_power = []

with open("input.txt") as file:
    while True:
        line = file.readline().rstrip("\n")

        if line == "":
            print("file processed")
            break

        game_id = int(line.split(":")[0].lstrip("Game "))

        possible_game = True
        minimal_set = {"red": 0, "green": 0, "blue": 0}
        for stage in line.split(":")[1].split(";"):
            cubes = {}
            for cube in stage.strip(" ").split(","):
                cubes[cube.strip(" ").split(" ")[1]] = int(
                    cube.strip(" ").split(" ")[0]
                )

            possible_stage = check_cubes(cubes)
            if not possible_stage:
                possible_game = False

            update_minimal_set(minimal_set, cubes)

        if possible_game:
            possible_games_ids.append(game_id)

        power = 1
        for cube in minimal_set.values():
            power *= cube
        sets_power.append(power)

print(f"task 1 result: {sum(possible_games_ids)}")
print(f"task 2 result: {sum(sets_power)}")
