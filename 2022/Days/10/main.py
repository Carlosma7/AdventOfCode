"""Advent of Code 2022 - Day 10."""

import os
from math import floor

def check_signal_strenght(cycle, value_x, signal_dict):
    """Given a cycle and x value, it computes the signal strength
    for that interval with the formula:
        signal_strenght = x * cycle
    """
    if str(cycle) in signal_dict.keys():
        signal_dict[cycle] = cycle*value_x

def get_sum_six_signal_strenghts(file):
    """Given a file, it gets the signal strength for some intervals and
    summarizes all the intervals signal strength.

    Returns sum of signal strenghts.
    """
    cycle = 0
    x_value = 1
    signal_strenghts = {'20': 0,
                        '60': 0,
                        '100': 0,
                        '140': 0,
                        '180': 0,
                        '220': 0,
                        }
    for line in file:
        if line == 'noop':
            cycle += 1
            check_signal_strenght(cycle, x_value, signal_strenghts)
        else:
            cycle += 1
            check_signal_strenght(cycle, x_value, signal_strenghts)
            cycle += 1
            check_signal_strenght(cycle, x_value, signal_strenghts)
            x_value += int(line.split()[1])

    print(sum(signal_strenghts.values()))

def move_sprite(x_value):
    """Given an X it moves the signal in the sprite to the correct
    position.

    Returns updated sprite.
    """
    new_sprite = [*'.........................................']
    for pos in range(x_value, x_value+3):
        if 0 <= pos < 40:
            new_sprite[pos] = '#'
    return new_sprite

def get_crt_image(file):
    """Given a file, it computes the crt image by applying the proper
    operations and computing the crt with the sprite.
    """
    sprite = [*'###.....................................']
    crt = [[], [], [], [], [], []]
    cycle = 0
    x_value = 0
    for line in file:

        if line == 'noop':
            crt[floor(cycle/40)].append(sprite[cycle%40])
            cycle += 1
        else:
            crt[floor(cycle/40)].append(sprite[cycle%40])
            cycle += 1
            crt[floor(cycle/40)].append(sprite[(cycle%40)+1])
            cycle += 1
            x_value += int(line.split()[1])
            sprite = move_sprite(x_value+1)

    for crt_line in crt:
        print(''.join(crt_line))




if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read().splitlines()

    get_sum_six_signal_strenghts(input_file)
    get_crt_image(input_file)
