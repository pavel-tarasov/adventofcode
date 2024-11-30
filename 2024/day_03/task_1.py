result = None
with open("input.txt") as file:
    while True:
        line = file.readline()

        if line == "":
            print("file processed")
            break

print(f"task 1 result: {result}")
