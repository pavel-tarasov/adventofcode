class CPU:
    def __init__(self, cycles_to_check):
        self.register_value = 1
        self.cycle_index = 1
        self.cycles_to_check = cycles_to_check
        self.sum_of_checks = 0

    def process_command(self, command, value):
        if command == "addx":
            self.tik(None)
            self.tik(value)
        if command == "noop":
            self.tik(None)

    def tik(self, value):
        self.cycle_index += 1
        if value is not None:
            self.register_value += value
        self.check_register()

    def check_register(self):
        if self.cycle_index in self.cycles_to_check:
            # print(self.cycle_index, self.cycle_index * self.register_value)
            self.sum_of_checks += self.cycle_index * self.register_value


cpu = CPU([20, 60, 100, 140, 180, 220])
with open("../inputs/day_10.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            print("file processed")
            break

        command = line.split(" ")[0]
        if command == "addx":
            value = int(line.split(" ")[1])
            cpu.process_command(command, value)
        if command == "noop":
            cpu.process_command(command, None)

print(f"task 1 result: {cpu.sum_of_checks}")
