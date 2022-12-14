"""Advent of Code 2022 - Day 13."""

import os
import ast
from math import prod
import functools


def compare_packets(left, right) -> bool | str:
    """Given two packets, compares them and checks whether left one is lower than
    right one.

    Returns result of comparison.
    """
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            result = True
        elif left > right:
            result = False
        else:
            result = 'Equal'
        return result
    if isinstance(left, list) and isinstance(right, list):
        for l_val, r_val in zip(left, right):
            if compare_packets(l_val, r_val) == 'Equal':
                continue
            return compare_packets(l_val, r_val)
        if len(right) >= len(left):
            return True
    if isinstance(left, list) and isinstance(right, int):
        return compare_packets(left, [right])
    if isinstance(left, int) and isinstance(right, list):
        return compare_packets([left], right)
    return None


def get_sum_index_ordered_pairs(file):
    """Given a list of pairs of packets, it checks for each one if the left one
    is lower and sums the indexes of the ones that are ordered.
    """
    indexes = []
    pair = 1
    for index in range(0, len(file), 3):
        left = ast.literal_eval(file[index])
        right = ast.literal_eval(file[index + 1])
        if compare_packets(left, right):
            indexes.append(pair)
        pair += 1

    print(sum(indexes))


def get_decoder_key(file):
    """Given a list of packets, it sorts them and puts two decoder signals, then
    it checks the positions of the decoders after sorting and multiplies the indexes
    of them.
    """
    packets = []
    for line in file:
        if line:
            packets.append(ast.literal_eval(line))

    packets.append(ast.literal_eval('[[2]]'))
    packets.append(ast.literal_eval('[[6]]'))

    packets.sort(key=functools.cmp_to_key(lambda p1, p2: -1 if compare_packets(
        p1, p2) else 1 if compare_packets(p1, p2) else 0))

    decoder_signal = []
    decoder_signal.append(packets.index([[2]]) + 1)
    decoder_signal.append(packets.index([[6]]) + 1)

    print(prod(decoder_signal))


if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read().splitlines()

    get_sum_index_ordered_pairs(input_file)
    get_decoder_key(input_file)
