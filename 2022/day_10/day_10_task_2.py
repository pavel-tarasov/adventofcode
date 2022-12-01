class Device:
    def __init__(self):
        self.cycle_index = 1
        self.register_value = 1
        self.screen = []

    def process_command(self, command, value):
        if command == "addx":
            self.tik(None)
            self.tik(value)
        if command == "noop":
            self.tik(None)

    def tik(self, value):
        self.draw()
        if value is not None:
            self.register_value += value
        self.cycle_index += 1

    def draw(self):
        pixel_position = self.cycle_index - 1
        while pixel_position >= 40:
            pixel_position -= 40

        if self.register_value in [
            pixel_position - 1,
            pixel_position,
            pixel_position + 1,
        ]:
            self.screen.append("#")
        else:
            self.screen.append(".")

    def print_screen(self):
        for i, symbol in enumerate(self.screen):
            print(symbol, end="")
            if i in [39, 79, 119, 159, 199, 239]:
                print()


device = Device()

with open("day_10.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            print("file processed")
            break

        command = line.split(" ")[0]
        if command == "addx":
            value = int(line.split(" ")[1])
            device.process_command(command, value)
        if command == "noop":
            device.process_command(command, None)

device.print_screen()
