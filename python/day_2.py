PLAYER_1_CODE = {"A": "R", "B": "P", "C": "S"}
PLAYER_2_CODE = {"X": "R", "Y": "P", "Z": "S"}
MOVE_SCORE = {"R": 1, "P": 2, "S": 3}
STRATEGY_2_ROUND_SCORE = {"X": 0, "Y": 3, "Z": 6}


def determine_winner(move_1, move_2):
    if move_1 == "R":
        if move_2 == "S":
            return 1
        elif move_2 == "P":
            return 2
        elif move_2 == "R":
            return 0
    if move_1 == "P":
        if move_2 == "R":
            return 1
        elif move_2 == "S":
            return 2
        elif move_2 == "P":
            return 0
    if move_1 == "S":
        if move_2 == "P":
            return 1
        elif move_2 == "R":
            return 2
        elif move_2 == "S":
            return 0


def define_move_2(move_1, desired_result):
    if move_1 == "R":
        if desired_result == "X":
            return "S"
        elif desired_result == "Y":
            return "R"
        elif desired_result == "Z":
            return "P"
    if move_1 == "P":
        if desired_result == "X":
            return "R"
        elif desired_result == "Y":
            return "P"
        elif desired_result == "Z":
            return "S"
    if move_1 == "S":
        if desired_result == "X":
            return "P"
        elif desired_result == "Y":
            return "S"
        elif desired_result == "Z":
            return "R"


score_strategy_1 = 0
score_strategy_2 = 0
with open("../inputs/day_2.txt") as file:
    while True:
        line = file.readline().replace("\n", "")
        if line == "":
            print("file processed")
            break

        move_1_encoded, move_2_encoded = line.split(" ")
        move_1 = PLAYER_1_CODE[move_1_encoded]
        move_2_strategy_1 = PLAYER_2_CODE[move_2_encoded]

        result = move_2_encoded
        move_2_strategy_2 = define_move_2(move_1, result)

        round_score = 0
        if determine_winner(move_1, move_2_strategy_1) == 0:
            round_score = 3
        elif determine_winner(move_1, move_2_strategy_1) == 2:
            round_score = 6
        score_strategy_1 += MOVE_SCORE[move_2_strategy_1] + round_score

        score_strategy_2 += (
            MOVE_SCORE[move_2_strategy_2] + STRATEGY_2_ROUND_SCORE[result]
        )

print(f"task 1 result: {score_strategy_1}")
print(f"task 2 result: {score_strategy_2}")
