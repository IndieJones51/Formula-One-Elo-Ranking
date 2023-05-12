def k_factor(score):
    if score > 2400:
        return 16
    elif 2100 <= score <= 2400:
        return 24
    else:
        return 32


def probability_of_win(player_a_score, player_b_score):
    return 1 / (1 + 10 ** ((player_b_score - player_a_score) / 400))


def updated_score(score):

    return score + k_factor(score) * ()