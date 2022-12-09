"""Advent of Code 2022 - Day 9."""

import os

def move_position(rope_h, rope_t, direction):
    """Given a direction, moves the head of the rope and then
    does the following move of the tail in diagonal, vertical
    or horizontal.

    Returns the final state of the head and tail after movement.
    """
    if direction == 'L':
        rope_h[0] -= 1
    elif direction == 'R':
        rope_h[0] += 1
    elif direction == 'D':
        rope_h[1] -= 1
    else:
        rope_h[1] += 1

    # Check diagonal move
    if (abs(rope_h[0]-rope_t[0]) + abs(rope_h[1]-rope_t[1])) == 3:
        rope_t[0] += 1 if rope_h[0] > rope_t[0] else -1
        rope_t[1] += 1 if rope_h[1] > rope_t[1] else -1
    elif abs(rope_h[0]-rope_t[0]) == 2:
        rope_t[0] += 1 if rope_h[0] > rope_t[0] else -1
    elif abs(rope_h[1]-rope_t[1]) == 2:
        rope_t[1] += 1 if rope_h[1] > rope_t[1] else -1
    return rope_h, rope_t

def get_visited_positions(file):
    """Given a file with moves it moves the head and tail of a rope
    and computes the amount of visited positions by the tail.

    Returns the total of visited positions by the tail.
    """
    head = [0,0]
    tail = [0,0]
    positions = set()
    # Add first position
    positions.add((0,0))

    for line in file:
        move, number = line.split()

        for _ in range(int(number)):
            head, tail = move_position(head, tail, move)
            positions.add((tail[0], tail[1]))

    print(len(positions))

def move_9_position(rope_h, rope_t, direction):
    """Given a direction, moves the head of the rope and then
    does the following move for every part of the rope in
    diagonal, vertical or horizontal.

    Returns the final state of the head and rope after movement.
    """
    if direction == 'L':
        rope_h[0] -= 1
    elif direction == 'R':
        rope_h[0] += 1
    elif direction == 'D':
        rope_h[1] -= 1
    else:
        rope_h[1] += 1

    if (abs(rope_h[0]-rope_t[0][0]) + abs(rope_h[1]-rope_t[0][1])) == 3:
        rope_t[0][0] += 1 if rope_h[0] > rope_t[0][0] else -1
        rope_t[0][1] += 1 if rope_h[1] > rope_t[0][1] else -1
    elif abs(rope_h[0]-rope_t[0][0]) == 2:
        rope_t[0][0] += 1 if rope_h[0] > rope_t[0][0] else -1
    elif abs(rope_h[1]-rope_t[0][1]) == 2:
        rope_t[0][1] += 1 if rope_h[1] > rope_t[0][1] else -1

    for index, elem in enumerate(rope_t):
        if index < len(rope_t)-1:
            if abs(elem[0] - rope_t[index + 1][0]) + abs(
                    elem[1] - rope_t[index + 1][1]) >= 3:
                rope_t[index+1][0] += 1 if elem[0] > rope_t[index+1][0] else -1
                rope_t[index+1][1] += 1 if elem[1] > rope_t[index+1][1] else -1
            elif abs(elem[0]-rope_t[index+1][0]) == 2:
                rope_t[index+1][0] += 1 if elem[0] > rope_t[index+1][0] else -1
            elif abs(elem[1]-rope_t[index+1][1]) == 2:
                rope_t[index+1][1] += 1 if elem[1] > rope_t[index+1][1] else -1


    return rope_h, rope_t

def get_9_visited_positions(file):
    """Given a file with moves it moves the head and rope
    and computes the amount of visited positions by the last
    piece of the rope (9 is tail).

    Returns the total of visited positions by the tail.
    """
    head = [0,0]
    tail = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    positions = set()
    # Add first position
    positions.add((0,0))

    for line in file:
        move, number = line.split()

        for _ in range(int(number)):
            head, tail = move_9_position(head, tail, move)
            positions.add((tail[-1][0], tail[-1][1]))

    print(len(positions))



if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read().splitlines()

    get_visited_positions(input_file)
    get_9_visited_positions(input_file)
