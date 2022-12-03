"""Advent of Code 2022 - Day 3."""

import os


def get_sum_priorities(file):
    """Reads a file of rucksacks and divives them into two containers,
    then gets unique element in common in both containers and calculates
    the priority, based on alphabet:

    [a-z]: 1-26
    [A-Z]: 27-52

    Returns sum of priorities
    """

    total_sum = 0
    for line in file:
        split_pos = int(len(line)/2)
        line_list = [*line]
        compartments = [line_list[:split_pos], line_list[split_pos:]]
        match = list(set(compartments[0]) & set(compartments[1]))[0]
        if match.islower():
            priority = ord(match) - 96
        else:
            priority = ord(match) - 64 + 26

        total_sum += priority

    return total_sum

def get_sum_priorities_v2(file):
    """Reads a file of rucksacks and groups elves in groups of three,
    then gets unique element in common in three elves's rucksack (badge)
    and calculates the priority, based on alphabet:

    [a-z]: 1-26
    [A-Z]: 27-52

    Returns sum of priorities
    """

    total_sum = 0
    for group in range(0, len(file), 3):
        elves = [[*file[group]], [*file[group+1]], [*file[group+2]]]
        badge = list(set(elves[0]) & set(elves[1]) & set(elves[2]))[0]
        if badge.islower():
            priority = ord(badge) - 96
        else:
            priority = ord(badge) - 64 + 26

        total_sum += priority

    return total_sum


if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read().splitlines()

    sum_priorities = get_sum_priorities(input_file)
    sum_priorities_v2 = get_sum_priorities_v2(input_file)

    print(sum_priorities)
    print(sum_priorities_v2)
