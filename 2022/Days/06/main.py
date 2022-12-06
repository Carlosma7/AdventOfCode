"""Advent of Code 2022 - Day 6."""

import os

def detect_marker(sequence, packet=True):
    """Given a sequence it detects packet or message markers, using different
    consecutive characters in the sequence.

    Returns first position after a marker is found.
    """

    if packet:
        distinct_char = 4
    else:
        distinct_char = 14

    for index in range(len(sequence)):
        if len(set(sequence[index:index+distinct_char])) == distinct_char:
            print(index + distinct_char)
            break



if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read()

    detect_marker(input_file, True)
    detect_marker(input_file, False)
