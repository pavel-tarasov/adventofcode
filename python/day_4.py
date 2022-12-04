sum = 0
sum_2 = 0
with open('../inputs/day_4.txt') as file:
    while True:
        line = file.readline().replace('\n', '')
        if line == '':
            print('file processed')
            break

        range_1, range_2 = line.split(',')
        range_1_left, range_1_right = map(int, range_1.split('-'))
        range_2_left, range_2_right = map(int, range_2.split('-'))
        print('---')
        print(f"range 1: {range_1_left} - {range_1_right}")
        print(f"range 2: {range_2_left} - {range_2_right}")

        if (range_1_left <= range_2_left and range_1_right >= range_2_right) \
                or (range_2_left <= range_1_left and range_2_right >= range_1_right):
            # print('full overlapping!')
            sum += 1

        if (range_1_right >= range_2_left >= range_1_left) \
                or (range_1_right >= range_2_right >= range_1_left) \
                or (range_2_left <= range_1_right <= range_2_right) \
                or (range_2_left <= range_1_left <= range_2_right):
            print('overlapping!')
            sum_2 += 1

print(f'task 1 result: {sum}')
print(f'task 2 result: {sum_2}')
