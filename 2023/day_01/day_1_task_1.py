calibration_values=[]
with open("input.txt") as file:
    while True:
        line = file.readline()

        if line == "":
            print("file processed")
            break

        first_digit = None
        last_digit=None

        for char in line:
            try:
                first_digit = int(char)
                break
            except ValueError:
                pass
        for char in reversed(line):
            try:
                last_digit = int(char)
                break
            except ValueError:
                pass

        if first_digit and last_digit:
            calibration_values.append(int(str(first_digit)+str(last_digit)))

print(f"task 1 result: {sum(calibration_values)}")

