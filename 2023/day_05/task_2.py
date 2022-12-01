from multiprocessing import Pool


def process_seed(seed: int, map_to_process: list[list[int]]) -> int:
    found = False
    for destination_start, source_start, range_length in map_to_process:
        if source_start <= seed <= source_start + range_length - 1:
            offset = seed - source_start
            result = destination_start + offset
            found = True
            break
    if not found:
        result = seed
    return result


def process_seed_range(seed_range: tuple[int]) -> int:
    seed_start, seed_length = seed_range
    min_location = 99999999999
    for seed in range(seed_start, seed_start + seed_length):
        soil = process_seed(seed, seed_to_soil_maps)
        fertilizer = process_seed(soil, soil_to_fertilizer_maps)
        water = process_seed(fertilizer, fertilizer_to_water_maps)
        light = process_seed(water, water_to_light_maps)
        temperature = process_seed(light, light_to_temperature_maps)
        humidity = process_seed(temperature, temperature_to_humidity_maps)
        location = process_seed(humidity, humidity_to_location_maps)
        if location < min_location:
            min_location = location
    return min_location


seeds = []
seed_to_soil_maps = []
soil_to_fertilizer_maps = []
fertilizer_to_water_maps = []
water_to_light_maps = []
light_to_temperature_maps = []
temperature_to_humidity_maps = []
humidity_to_location_maps = []
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
            seed_ranges = []
            first = True
            for n in list(map(int, line.split(" ")[1:])):
                if first:
                    seed_ranges.append([n])
                    first = False
                else:
                    seed_ranges[-1].append(n)
                    first = True

        elif category == "seed-to-soil":
            seed_to_soil_maps.append(list(map(int, line.split(" "))))
        elif category == "soil-to-fertilizer":
            soil_to_fertilizer_maps.append(list(map(int, line.split(" "))))
        elif category == "fertilizer-to-water":
            fertilizer_to_water_maps.append(list(map(int, line.split(" "))))
        elif category == "water-to-light":
            water_to_light_maps.append(list(map(int, line.split(" "))))
        elif category == "light-to-temperature":
            light_to_temperature_maps.append(list(map(int, line.split(" "))))
        elif category == "temperature-to-humidity":
            temperature_to_humidity_maps.append(list(map(int, line.split(" "))))
        elif category == "humidity-to-location":
            humidity_to_location_maps.append(list(map(int, line.split(" "))))


with Pool(11) as p:
    results = p.map(process_seed_range, seed_ranges)

print(f"task 2 result: {min(results)}")
