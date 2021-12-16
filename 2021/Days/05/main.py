import os
from collections import defaultdict

# Get lines from a file splitting them
def get_lines(file):
    """Process a file splitting the points by origin and end points. Also splits points by coordinates."""
    lines = []
    for f in file:
        line = f.split("->")
        origin = map(int, line[0].split(","))
        end = map(int, line[1].split(","))
        lines.append([tuple(origin), tuple(end)])
    return lines


# Computes the move in both axis
def compute_move(line):
    """Takes an origin and end and computes in its axis the move to be done."""
    if line[0] == line[1]:
        return 0
    else:
        return (line[1] - line[0]) / abs(line[1] - line[0])


# Draws the line in a defaultdict object
def draw_line(line, picture):
    """Draws a line in the picture by adding in a defaultdict object map.
    It computes the move to be done, takes the distance and origin and end points."""
    origin, end = line
    # Compute move in both axis and distance
    x_move = compute_move((origin[0], end[0]))
    y_move = compute_move((origin[1], end[1]))
    distance = max(abs(end[0] - origin[0]), abs(end[1] - origin[1])) + 1
    # Compute new points
    for i in range(0, distance):
        x = origin[0] + i * x_move
        y = origin[1] + i * y_move
        # Draw
        picture[(x, y)] += 1

# Compute the total overlaps for the picture
def compute_overlaps(picture):
    """Checks all the points in the picture that has a value greater than one."""
    counter = 0
    for point in picture.values():
        if point > 1:
            counter += 1
    return counter


# At how many points do at least two lines overlap? Non-diagonal
def no_diagonal(lines):
    picture = defaultdict(int)
    for origin, end in lines:
        if origin[0] == end[0] or origin[1] == end[1]:
            draw_line((origin, end), picture)
    return compute_overlaps(picture)


# At how many points do at least two lines overlap? Diagonal
def diagonal(lines):
    picture = defaultdict(int)
    for points in lines:
        draw_line(points, picture)
    return compute_overlaps(picture)


if __name__ == "__main__":
    # Get path from actual dirname
    dir = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(dir, "input.txt")) as file_path:
        # Read path into files
        file = file_path.read().splitlines()

    # Split lines by "->" operator
    lines = get_lines(file)

    # First solution
    print(no_diagonal(lines))
    # Second solution
    print(diagonal(lines))
