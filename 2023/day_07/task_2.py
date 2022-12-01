CARD_STRENGTH = {
    "A": "13",
    "K": "12",
    "Q": "11",
    "T": "10",
    "9": "09",
    "8": "08",
    "7": "07",
    "6": "06",
    "5": "05",
    "4": "04",
    "3": "03",
    "2": "02",
    "J": "01",
}


class Hand:
    def __init__(self, cards: list[str], bid: int):
        self.cards = cards
        self.bid = bid

        card_groups = {}
        for card in [card for card in cards if card != "J"]:
            if card_groups.get(card):
                card_groups[card] += 1
            else:
                card_groups[card] = 1
        other_cards_amount = sorted(list(card_groups.values()), reverse=True)

        j_amount = len([card for card in cards if card == "J"])

        # Five of a kind, 7
        # Four of a kind, 6
        # Full house, 5
        # Three of a kind, 4
        # Two pair, 3
        # One pair, 2
        # High card, 1
        if j_amount == 5 or (other_cards_amount[0] + j_amount) == 5:
            self.type = 7
        elif (other_cards_amount[0] + j_amount) == 4:
            self.type = 6
        elif (other_cards_amount[0] + j_amount) == 3 and other_cards_amount[1] == 2:
            self.type = 5
        elif (other_cards_amount[0] + j_amount) == 3:
            self.type = 4
        elif other_cards_amount[0] == 2 and other_cards_amount[1] == 2:
            self.type = 3
        elif (other_cards_amount[0] + j_amount) == 2:
            self.type = 2
        elif other_cards_amount[0] == 1 or j_amount == 1:
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

print(f"task 2 result: {result}")
