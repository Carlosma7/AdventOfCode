"""Advent of Code 2022 - Day 8."""

import os

def get_sum_visible(file):
    """Given a matrix of trees in a file, it gets the total of visible ones.

    Visible trees are the ones that doesn't have a higher or equal tree in one of the
    four directions (top, bottom, right, left).

    Returns total number of visible trees
    """
    matrix = [[*line] for line in file]

    # Get transposed matrix
    transposed_tuples = list(zip(*matrix))
    transposed = [list(sublist) for sublist in transposed_tuples]

    total_visible = 0

    # Iterate over matrix
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            # Not an edge element
            if 0 < i < len(matrix)-1 and 0 < j < len(row)-1:
                invisible_x = max((x for x in row[:j])) >= elem and max(
                    (x for x in row[j + 1:])) >= elem
                invisible_y = max((
                    x for x in transposed[j][:i]
                )) >= elem and max((x for x in transposed[j][i + 1:])) >= elem
                # Check that is not invisible in one of the axis
                if not invisible_x or not invisible_y:
                    total_visible += 1

    # Add horizontal edges
    total_visible += len(matrix) * 2
    # Add vertical edges (excluding horizontal)
    total_visible += (len(transposed) * 2) - 4

    print(total_visible)

def get_trees_visible(tree, list_trees):
    """Gets all trees visible in the list_trees from the actual tree.

    Returns total of visible ones.
    """
    visible = 0
    for list_elem in list_trees:
        visible += 1
        if list_elem >= tree:
            break
    return visible

def get_highest_scenic(file):
    """Given a matrix of trees in a file, it gets the max scenic value of the tree matrix.

    Scenic is computed by checking in four direction the max number of trees reachable
    (until one higher or equal is found)

    Returns max scenic of the matrix.
    """
    matrix = [[*line] for line in file]
    # Get transposed matrix
    transposed_tuples = list(zip(*matrix))
    transposed = [list(sublist) for sublist in transposed_tuples]

    max_scenic = 0

    # Iterate over matrix
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            # Not an edge element
            if 0 < i < len(matrix)-1 and 0 < j < len(row)-1:
                # Get left value
                left = get_trees_visible(elem, reversed(row[:j]))
                right = get_trees_visible(elem, row[j+1:])
                top = get_trees_visible(elem, reversed(transposed[j][:i]))
                bottom = get_trees_visible(elem, transposed[j][i+1:])

                # Compute scenic of tree
                scenic = top * bottom * right * left
                # Check if it's now max scenic
                if scenic > max_scenic:
                    max_scenic = scenic

    print(max_scenic)



if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read().splitlines()

    get_sum_visible(input_file)
    get_highest_scenic(input_file)
