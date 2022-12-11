"""Advent of Code 2022 - Day 11."""

import os
from math import floor, prod

class Monkey:
    """Definition here"""

    def __init__(self, operation, items, test, true, false):
        self.__operation = operation
        self.__items = items
        self.__test = test
        self.__true = true
        self.__false = false
        self.__inspected = 0

    def play(self, relief=True):
        monkey_moves = []
        for item in self.__items:
            self.__inspected += 1
            level = item
            if self.__operation.split()[2] == 'old':
                level *= level
            elif self.__operation.split()[1] == '*':
                level *= int(self.__operation.split()[2])
            else:
                level += int(self.__operation.split()[2])

            if relief:
                level = floor(level/3)

            if level % self.__test == 0:
                monkey_moves.append([self.__true, level])
            else:
                monkey_moves.append([self.__false, level])
        self.__items = []
        return monkey_moves

    def add(self, item):
        self.__items.append(item)

    def get_inspected(self):
        return self.__inspected
    def get_items(self):
        return self.__items

def read_monkeys(file):
    monkeys = []
    for index, line in enumerate(file):
        if 'Monkey' in line:
            items = file[index+1].split(':')[1].split(',')
            items = [int(item) for item in items]
            operation = file[index+2].split('=')[1]
            test = int(file[index+3].split('by')[1])
            true = int(file[index+4].split('monkey')[1])
            false = int(file[index+5].split('monkey')[1])
            monkeys.append(Monkey(operation, items, test, true, false))
    return monkeys

def get_monkey_business(monkeys):
    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            monkey_moves = monkey.play()
            for mov in monkey_moves:
                monkeys[mov[0]].add(mov[1])
    inspected = [mon.get_inspected() for mon in monkeys]

    two_most = sorted(inspected, reverse=True)[:2]

    print(prod(two_most))

def get_monkey_business_no_relief(monkeys):
    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            monkey_moves = monkey.play(False)
            for mov in monkey_moves:
                monkeys[mov[0]].add(mov[1])
    inspected = [mon.get_inspected() for mon in monkeys]

    two_most = sorted(inspected, reverse=True)[:2]

    print(prod(two_most))


if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read().splitlines()

    monkey_list = read_monkeys(input_file)
    get_monkey_business(monkey_list)
    monkey_list = read_monkeys(input_file)
    get_monkey_business_no_relief(monkey_list)
