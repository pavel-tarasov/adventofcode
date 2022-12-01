CARD_STRENGTH = {
    "A": "13",
    "K": "12",
    "Q": "11",
    "J": "10",
    "T": "09",
    "9": "08",
    "8": "07",
    "7": "06",
    "6": "05",
    "5": "04",
    "4": "03",
    "3": "02",
    "2": "01",
}


class Hand:
    def __init__(self, cards: list[str], bid: int):
        self.cards = cards
        self.bid = bid

        card_groups = {}
        for card in self.cards:
            if card_groups.get(card):
                card_groups[card] += 1
            else:
                card_groups[card] = 1
        cards_amount = sorted(list(card_groups.values()), reverse=True)

        # Five of a kind, 7
        # Four of a kind, 6
        # Full house, 5
        # Three of a kind, 4
        # Two pair, 3
        # One pair, 2
        # High card, 1
        if cards_amount[0] == 5:
            self.type = 7
        elif cards_amount[0] == 4:
            self.type = 6
        elif cards_amount[0] == 3 and cards_amount[1] == 2:
            self.type = 5
        elif cards_amount[0] == 3:
            self.type = 4
        elif cards_amount[0] == 2 and cards_amount[1] == 2:
            self.type = 3
        elif cards_amount[0] == 2:
            self.type = 2
        elif cards_amount[0] == 1:
            self.type = 1

        self.score = str(self.type)
        for card in self.cards:
            self.score += CARD_STRENGTH[card]


hands = []
with open("input.txt") as file:
    while True:
        line = file.readline()

        if line == "":
            print("file processed")
            break

        cards, bid = line.split(" ")
        hands.append(Hand(cards, int(bid)))

rank = 0
result = 0
for hand in sorted(hands, key=lambda hand: hand.score):
    rank += 1
    result += rank * hand.bid

print(f"task 1 result: {result}")
