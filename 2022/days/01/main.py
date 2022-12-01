"""Advent of Code 2022 - Day 1."""

import os

def read_elves_food(file):
    """Reads a file with several elves's calories and returns max and sum of top 3."""

    elves = []
    food = []
    for line in file:
        # No empty line
        if len(line) > 1:
            food.append(int(line))
        else:
            elves.append(food)
            food = []

    calories = [sum(elf) for elf in elves]
    calories = sorted(calories, reverse=True)

    return calories[0], sum(calories[:3])

if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read().splitlines()

    max_calories, top_3_calories = read_elves_food(input_file)

    print(max_calories)
    print(top_3_calories)
