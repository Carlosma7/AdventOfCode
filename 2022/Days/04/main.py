"""Advent of Code 2022 - Day 4."""

import os


def get_assignments_contained(file):
    """Reads a file of sections and detects pairs of elfs that clean sections fully
    contained by the other elf.

    Returns sum of contained sections.
    """

    total_contained = 0
    for line in file:
        assignments = line.split(',')
        assignments = [[int(a) for a in elf.split('-')] for elf in assignments]
        assignments = [set([*range(elf[0], elf[1]+1)]) for elf in assignments]
        if assignments[0].issubset(assignments[1]) or assignments[1].issubset(assignments[0]):
            total_contained += 1

    print(total_contained)

def get_assignments_overlaped(file):
    """Reads a file of sections and detects pairs of elfs that clean sections overlaped
    by the other elf.

    Returns sum of overlaped sections.
    """

    total_overlaped = 0
    for line in file:
        assignments = line.split(',')
        assignments = [[int(a) for a in elf.split('-')] for elf in assignments]
        assignments = [set([*range(elf[0], elf[1]+1)]) for elf in assignments]
        if assignments[0].intersection(assignments[1]) != set():
            total_overlaped += 1

    print(total_overlaped)


if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read().splitlines()

    get_assignments_contained(input_file)
    get_assignments_overlaped(input_file)
