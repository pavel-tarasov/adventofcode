ITEM_PRIORITIES = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52}

sum = 0
sum_2 = 0
line_1 = None
line_2 = None
line_3 = None
i = 1
with open('../inputs/day_3.txt') as file:
    while True:
        line = file.readline().replace('\n', '')
        if line == '':
            print('file processed')
            break

        part_1 = set(line[:int(len(line) / 2)])
        part_2 = set(line[int(len(line) / 2):])

        intersection = part_1.intersection(part_2)
        # print(intersection)
        for item in intersection:
            sum += ITEM_PRIORITIES[item]

        if i == 1:
            line_1 = set(line)
            i += 1
        elif i == 2:
            line_2 = set(line)
            i += 1
        elif i == 3:
            line_3 = set(line)

            intersection3 = line_1.intersection(line_2).intersection(line_3)
            print(intersection3)
            for item in intersection3:
                sum_2 += ITEM_PRIORITIES[item]

            line_1 = None
            line_2 = None
            line_3 = None
            i = 1

print(f'task 1 result: {sum}')
print(f'task 2 result: {sum_2}')
