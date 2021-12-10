import os


def calculate_position(moves):
    """helloda"""
    depth = 0
    horizontal = 0
    for m in moves:
        typ, inc = m.split()
        inc = int(inc)
        if typ == "forward":
            horizontal += inc
        elif typ == "up":
            depth -= inc
        else:
            depth += inc

    return depth * horizontal


def calculate_position_aim(moves):
    """helloda"""
    depth = 0
    horizontal = 0
    aim = 0
    for m in moves:
        typ, inc = m.split()
        inc = int(inc)
        if typ == "forward":
            horizontal += inc
            depth += aim * inc
        elif typ == "up":
            aim -= inc
        else:
            aim += inc

    return depth * horizontal


if __name__ == "__main__":
    # Get path from actual dirname
    dir = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(dir, "input.txt")) as file_path:
        # Read path into files
        file = file_path.read().splitlines()

    # First solution
    print(calculate_position(file))
    # Second solution
    print("a")