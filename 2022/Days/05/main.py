"""Advent of Code 2022 - Day 5."""

import os

def move_crate_9000(stacks_list, qty, origin, destination):
    """Moves 'qty' crates in an 'origin' stack to a 'destination' stack using the
    LIFO logic.

    Returns stacks list with moves applied.
    """
    for _ in range(qty):
        stacks_list[destination].append(stacks_list[origin].pop())
    return stacks_list

def move_crate_9001(stacks_list, qty, origin, destination):
    """Moves 'qty' crates in an 'origin' stack to a 'destination' stack using the
    FIFO logic.

    Returns stacks list with moves applied.
    """
    machine_stack = []
    for _ in range(qty):
        machine_stack.append(stacks_list[origin].pop())
    for _ in range(qty):
        stacks_list[destination].append(machine_stack.pop())
    return stacks_list

def sort_stack(file, machine_9000):
    """Reads a file and desired machine to use and creates several stacks with
    their crates. After that it applies the different moves using the indicated
    machine's logic and shows the top crate of each stack.
    """

    # Search for number of stacks
    for line in file:
        if '1' in line:
            number_stacks = int(line[-2])
            break

    # Create all stacks
    stacks = [[] for i in range(number_stacks)]

    # Generate initial display of stacks
    for line in file:
        if '[' in line:
            i = 0
            for index in range(0, number_stacks*4, 4):
                if line[index+1] != ' ':
                    stacks[i].append(line[index+1])
                i+=1

    # Convert into stack by reverting the list
    for stack in stacks:
        stack.reverse()

    # Apply moves move 3 from 4 to 6
    for line in file:
        if 'move' in line:
            move = line.split()
            # Get just numbers
            move = [int(move[x]) for x in [1,3,5]]
            # Use corresponding machine
            if machine_9000:
                stacks = move_crate_9000(stacks, move[0], move[1]-1, move[2]-1)
            else:
                stacks = move_crate_9001(stacks, move[0], move[1]-1, move[2]-1)

    # Join top crates to create final word
    final_word = ''.join([stack.pop() for stack in stacks]).replace(' ', '')

    print(final_word)



if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read().splitlines()

    sort_stack(input_file, True)
    sort_stack(input_file, False)
