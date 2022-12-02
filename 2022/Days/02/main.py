"""Advent of Code 2022 - Day 2."""

import os


def get_total_score(file):
    """Reads a file with several rock, paper, scissors plays and gets user total score.
    First column is opponent play, second column is our play.
    A and X stands for Rock (1 point).
    B and Y stands for Paper (2 points).
    C and Z stands for Scissors (3 points).

    Win scores 6 points + move.
    Draw scores 3 points+ move.
    Lose scores 0 points + move.
    """

    move_results = {
        'win': ['A Y', 'B Z', 'C X'],
        'draw': ['A X', 'B Y', 'C Z']
    }

    move_value = {'X': 1, 'Y': 2, 'Z': 3}

    total_score = 0

    for line in file:
        my_move = line.split()[1]
        score_move = move_value.get(my_move)

        if line in move_results.get('win'):
            score_move += 6
        elif line in move_results.get('draw'):
            score_move += 3

        total_score += score_move

    return total_score


def get_total_score_v2(file):
    """Reads a file with several rock, paper, scissors plays and gets user total score.
    First column is opponent play, second column is round result.
    A stands for Rock (1 point).
    B stands for Paper (2 points).
    C stands for Scissors (3 points).

    Z stands for win (scores 6 points + move).
    Y stands for draw (scores 3 points+ move).
    X stands for lose (scores 0 points + move).
    """

    round_result = {
        'X': {
            'A': 3,
            'B': 1,
            'C': 2
        },
        'Y': {
            'A': 4,
            'B': 5,
            'C': 6
        },
        'Z': {
            'A': 8,
            'B': 9,
            'C': 7
        }
    }

    total_score = 0
    for line in file:
        opponent_move, result = line.split()
        total_score += round_result.get(result).get(opponent_move)

    return total_score


if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read().splitlines()

    final_score = get_total_score(input_file)

    final_score_v2 = get_total_score_v2(input_file)

    print(final_score)
    print(final_score_v2)
