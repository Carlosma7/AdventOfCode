"""Advent of Code 2022 - Day 11."""

import os
from math import floor, prod

class Monkey:
    """Class that represents a monkey and its behaviour. It controlls the
    the play of a monkey and the adding of items.
    """

    def __init__(self, operation, items, test, new_monkey):
        """Init of monkey that gets all parameters to represent it."""
        self.__operation = operation
        self.__items = items
        self.__test = test
        self.__true = new_monkey[0]
        self.__false = new_monkey[1]
        self.__inspected = 0

    def play(self, relief=True):
        """Given a relief or not, it reproduces the behaviour of a monkey, consisting on:
        For each item:
        1. Checks item and computes stress on it.
        2. If relief, reduces stress by dividing it by 3.
        3. Checks to which monkey it should send the item to.

        Returns the monkey moves.
        """
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
        """Adds a new item to the ones that the monkey has."""
        self.__items.append(item)

    def get_inspected(self):
        """Getter method for monkey total number of inspected items."""
        return self.__inspected

def read_monkeys(file):
    """Given a file it reads all the monkeys on it and creates a list
    of them.

    Returns a list of monkeys.
    """
    monkeys = []
    for index, line in enumerate(file):
        if 'Monkey' in line:
            items = file[index+1].split(':')[1].split(',')
            items = [int(item) for item in items]
            operation = file[index+2].split('=')[1]
            test = int(file[index+3].split('by')[1])
            new_monkey = []
            new_monkey.append(int(file[index+4].split('monkey')[1]))
            new_monkey.append(int(file[index+5].split('monkey')[1]))
            monkeys.append(Monkey(operation, items, test, new_monkey))
    return monkeys

def get_monkey_business(monkeys):
    """Given a list of monkeys, reproduces the behaviour of them in 20 rounds
    and computes the monkey business for all of them. Considers relief.

    Returns the prod of the two most active monkey business.
    """
    for _ in range(20):
        for monkey in monkeys:
            monkey_moves = monkey.play()
            for mov in monkey_moves:
                monkeys[mov[0]].add(mov[1])
    inspected = [mon.get_inspected() for mon in monkeys]

    two_most = sorted(inspected, reverse=True)[:2]

    print(prod(two_most))

def get_monkey_business_no_relief(monkeys):
    """Given a list of monkeys, reproduces the behaviour of them in 10000 rounds
    and computes the monkey business for all of them. Does not consider relief.

    Returns the prod of the two most active monkey business.
    """
    for _ in range(10000):
        for monkey in monkeys:
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
