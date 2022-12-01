class Card:
    def __init__(self, id: int, card_numbers: list[int], winning_numbers: list[int]):
        self.id = id
        self.card_numbers = card_numbers
        self.winning_numbers = winning_numbers

        # sanity check
        if len(winning_numbers) != len(set(winning_numbers)) or len(
            card_numbers
        ) != len(set(card_numbers)):
            raise Exception("same numbers in a row")

        matching_numbers = set(card_numbers).intersection(set(winning_numbers))
        self.numbers = len(matching_numbers)
        if matching_numbers != set():
            self.points = 1
            for _ in range(len(matching_numbers) - 1):
                self.points *= 2
        else:
            self.points = 0


cards = {}
with open("input.txt") as file:
    while True:
        line = file.readline().rstrip("\n")

        if line == "":
            print("file processed")
            break

        card_id = int(
            line.split(":")[0].replace("  ", " ").replace("  ", " ").split(" ")[1]
        )
        line = line.split(":")[1]
        winning_numbers, card_numbers = line.split("|")
        winning_numbers = list(
            map(int, winning_numbers.strip(" ").replace("  ", " ").split(" "))
        )
        card_numbers = list(
            map(int, card_numbers.strip(" ").replace("  ", " ").split(" "))
        )

        cards[card_id] = Card(card_id, winning_numbers, card_numbers)
        max_card_id = card_id

card_count = dict.fromkeys(cards, 1)
for card_id, card in cards.items():
    for _ in range(card_count[card_id]):
        for i in range(card.numbers):
            new_card_id = card_id + i + 1
            if new_card_id <= max_card_id:
                card_count[new_card_id] += 1

print(f"task 1 result: {sum([card.points for card in cards.values()])}")
print(f"task 2 result: {sum(card_count.values())}")
