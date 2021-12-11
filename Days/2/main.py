import os

# What do you get if you multiply your final horizontal position by your final depth?
def calculate_position(moves):
    """Calculates position by moving forward in horizontal and up/down in depth.
    Calculates final position multiplying depth with horizontal."""
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

# What do you get if you multiply your final horizontal position by your final depth?
def calculate_position_aim(moves):
    """Adds new aim concept to previous position calculation.
    Calculates position by modifying aim with up/down and moves with forward taking
    increment in horizontal and aim multiplied by increment in depth."""
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