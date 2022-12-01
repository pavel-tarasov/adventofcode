def map_seeds(
    seeds: list[int],
    map_to_process: list[list[int]],
    result_dict: dict,
    previous_seed_map: dict = None,
):
    for seed in seeds:
        if previous_seed_map:
            seed_value = previous_seed_map[seed]
        else:
            seed_value = seed
        found = False
        for destination_start, source_start, range_length in map_to_process:
            if source_start <= seed_value <= source_start + range_length:
                offset = seed_value - source_start
                result_dict[seed] = destination_start + offset
                found = True
                break
        if not found:
            result_dict[seed] = seed_value


seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
category = "seeds"
with open("input.txt") as file:
    while True:
        line = file.readline().rstrip("\n")

        if line == "seed-to-soil map:":
            category = "seed-to-soil"
            continue
        elif line == "soil-to-fertilizer map:":
            category = "soil-to-fertilizer"
            continue
        elif line == "fertilizer-to-water map:":
            category = "fertilizer-to-water"
            continue
        elif line == "water-to-light map:":
            category = "water-to-light"
            continue
        elif line == "light-to-temperature map:":
            category = "light-to-temperature"
            continue
        elif line == "temperature-to-humidity map:":
            category = "temperature-to-humidity"
            continue
        elif line == "humidity-to-location map:":
            category = "humidity-to-location"
            continue
        elif category == "humidity-to-location" and line == "":
            print("file processed")
            break
        elif line == "":
            continue

        if category == "seeds":
            seeds = list(map(int, line.split(" ")[1:]))
        elif category == "seed-to-soil":
            seed_to_soil.append(list(map(int, line.split(" "))))
        elif category == "soil-to-fertilizer":
            soil_to_fertilizer.append(list(map(int, line.split(" "))))
        elif category == "fertilizer-to-water":
            fertilizer_to_water.append(list(map(int, line.split(" "))))
        elif category == "water-to-light":
            water_to_light.append(list(map(int, line.split(" "))))
        elif category == "light-to-temperature":
            light_to_temperature.append(list(map(int, line.split(" "))))
        elif category == "temperature-to-humidity":
            temperature_to_humidity.append(list(map(int, line.split(" "))))
        elif category == "humidity-to-location":
            humidity_to_location.append(list(map(int, line.split(" "))))


soil = {}
map_seeds(seeds=seeds, map_to_process=seed_to_soil, result_dict=soil)

fertilizer = {}
map_seeds(
    seeds=seeds,
    previous_seed_map=soil,
    map_to_process=soil_to_fertilizer,
    result_dict=fertilizer,
)

water = {}
map_seeds(
    seeds=seeds,
    previous_seed_map=fertilizer,
    map_to_process=fertilizer_to_water,
    result_dict=water,
)

light = {}
map_seeds(
    seeds=seeds,
    previous_seed_map=water,
    map_to_process=water_to_light,
    result_dict=light,
)

temperature = {}
map_seeds(
    seeds=seeds,
    previous_seed_map=light,
    map_to_process=light_to_temperature,
    result_dict=temperature,
)

humidity = {}
map_seeds(
    seeds=seeds,
    previous_seed_map=temperature,
    map_to_process=temperature_to_humidity,
    result_dict=humidity,
)

location = {}
map_seeds(
    seeds=seeds,
    previous_seed_map=humidity,
    map_to_process=humidity_to_location,
    result_dict=location,
)

min_location = sorted([loc for loc in location.values()])[0]

print(f"task 1 result: {min_location}")
# print(f"task 2 result: {sum(card_count.values())}")
