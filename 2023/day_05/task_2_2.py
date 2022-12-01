# attempt to solve it in a smart way
def check_intersection(a: tuple[int, int], b: tuple[int, int]) -> bool:
    if (a[1] >= b[0] and a[0] < b[1]) or (b[1] >= a[0] and b[0] < a[1]):
        return True
    else:
        return False


def check_maps(maps: list[list[int]]):
    intersection = False
    for map_i in maps:
        for map_j in maps:
            if map_i != map_j:
                intersection = check_intersection(
                    (map_i[1], map_i[1] + map_i[2] - 1),
                    (map_j[1], map_j[1] + map_j[2] - 1),
                )
                if intersection:
                    print(map_i, map_j)
    return intersection


def check_seeds(ranges: list[int]):
    intersection = False
    for range_i in ranges:
        for range_j in ranges:
            if range_i != range_j:
                intersection = check_intersection(
                    (range_i[0], range_i[0] + range_i[1] - 1),
                    (range_j[0], range_j[0] + range_j[1] - 1),
                )
                if intersection:
                    print(range_i, range_j)
    return intersection


# seeds = []
seed_to_soil_maps = []
soil_to_fertilizer_maps = []
fertilizer_to_water_maps = []
water_to_light_maps = []
light_to_temperature_maps = []
temperature_to_humidity_maps = []
humidity_to_location_maps = []
category = "seeds"
with open("test_input.txt") as file:
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


# print(f"seeds {check_seeds(seed_ranges)}")
# print(f"seed_to_soil_maps {check_maps(seed_to_soil_maps)}")
# print(f"soil_to_fertilizer_maps {check_maps(soil_to_fertilizer_maps)}")
# print(f"fertilizer_to_water_maps {check_maps(fertilizer_to_water_maps)}")
# print(f"water_to_light_maps {check_maps(water_to_light_maps)}")
# print(f"light_to_temperature_maps {check_maps(light_to_temperature_maps)}")
# print(f"temperature_to_humidity_maps {check_maps(temperature_to_humidity_maps)}")
# print(f"humidity_to_location_maps {check_maps(humidity_to_location_maps)}")

original_ranges = []
for seed_start, seed_length in seed_ranges:
    original_ranges.append((seed_start, seed_start + seed_length - 1))
#
# new_ranges = []
# for r in original_ranges:
#     for map_ in seed_to_soil_maps:
#         input_range = (map_[1], map_[1] + map_[2] - 1)
#         output_range = (map_[0], map_[0] + map_[2] - 1)
#     if check_intersection(r, input_range):
#         print(r)
#         print(input_range)
#         print(output_range)
#         if r[0] <= input_range[0] <= r[1] <= input_range[1]:
#             new_ranges.append((r[0], input_range[0] - 1))
#             offset = r[1] - input_range[0]
#             new_ranges.append((output_range[0], output_range[0] + offset))
#         elif input_range[0] <= r[0] <= input_range[1] <= r[1]:
#             offset = input_range[1] - r[0]
#             new_ranges.append((output_range[1] - offset, output_range[1]))
#             new_ranges.append((input_range[1], r[1]))
#         elif r[0] <= input_range[0] <= r[1] and r[0] <= input_range[1] <= r[1]:
#             new_ranges.append((r[0], input_range[0] - 1))
#             new_ranges.append((output_range[0], output_range[1]))
#             new_ranges.append((input_range[1] + 1, r[1]))
#         elif input_range[0] <= r[0] and r[1] <= input_range[1]:
#             new_ranges.append((output_range[0], output_range[1]))
#     else:
#         new_ranges.append(r)


# combine all maps together
# for map in maps:
#   new_ranges = []
#   for r in original_ranges:
#   original_ranges=new_ranges

maps = seed_to_soil_maps
maps.extend(soil_to_fertilizer_maps)
maps.extend(fertilizer_to_water_maps)
maps.extend(water_to_light_maps)
maps.extend(light_to_temperature_maps)
maps.extend(temperature_to_humidity_maps)
maps.extend(humidity_to_location_maps)

for map_ in maps:
    input_range = (map_[1], map_[1] + map_[2] - 1)
    output_range = (map_[0], map_[0] + map_[2] - 1)
    new_ranges = []
    for r in original_ranges:
        if check_intersection(r, input_range):
            # print(r)
            # print(input_range)
            # print(output_range)
            if r[0] <= input_range[0] <= r[1] <= input_range[1]:
                new_ranges.append((r[0], input_range[0] - 1))
                offset = r[1] - input_range[0]
                new_ranges.append((output_range[0], output_range[0] + offset))
            elif input_range[0] <= r[0] <= input_range[1] <= r[1]:
                offset = input_range[1] - r[0]
                new_ranges.append((output_range[1] - offset, output_range[1]))
                new_ranges.append((input_range[1] + 1, r[1]))
            elif r[0] <= input_range[0] <= r[1] and r[0] <= input_range[1] <= r[1]:
                new_ranges.append((r[0], input_range[0] - 1))
                new_ranges.append((output_range[0], output_range[1]))
                new_ranges.append((input_range[1] + 1, r[1]))
            elif input_range[0] <= r[0] and r[1] <= input_range[1]:
                new_ranges.append((output_range[0], output_range[1]))
        else:
            new_ranges.append(r)
    original_ranges = set(new_ranges)

print(original_ranges)
print(sorted(original_ranges, key=lambda a: a[0])[0])
print()
