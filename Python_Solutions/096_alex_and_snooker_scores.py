def parse_scores(player_result):
    i = player_result.find("(")

    if i > -1:
        player_result = player_result[0:i]

    return int(player_result)


def frame(score):
    first_player_wins = 0
    second_player_wins = 0
    frames = [f.strip() for f in score.split(";")]

    for frame in frames:
        first_player_result, second_player_result = frame.split("-")
        first_player_scores = parse_scores(first_player_result)
        second_player_scores = parse_scores(second_player_result)

        if first_player_scores > second_player_scores:
            first_player_wins += 1
        elif second_player_scores > first_player_scores:
            second_player_wins += 1

    return [first_player_wins, second_player_wins]


# score = "24-79(72); 16-101(53); 86(58)-27; 31-90(74); 0-115(115); 67-40; 61-21; 81(55)-23; 51-14; 124(56,68)-4; 67-12; 108(85)-15; 1-117(117); 1-92(92); 130(112)-0; 1-106(53); 59-39"
# print(frame(score))
