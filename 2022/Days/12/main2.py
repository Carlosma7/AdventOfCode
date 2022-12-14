"""Advent of Code 2022 - Day 12. Part 2."""

import os
from functions import read_graph, retrieve_path

def breadth_first_search(origin_node, dest_value):
    """Implementation of breadth first search algorithm."""
    visited = []
    queue = []
    visited.append(origin_node)
    queue.append(origin_node)

    while queue:
        node = queue.pop(0)
        for neighbor in node.get_neighbors():
            if neighbor not in visited:
                neighbor.set_parent(node)
                visited.append(neighbor)
                queue.append(neighbor)
            if neighbor.get_value() == dest_value:
                queue.clear()

    # Retrieve the steps generated
    retrieve_path(visited, origin_node)


def check_origin_neighbors(elem, origin, graph, index_i, index_j):
    """Given an element checks if its the origin node and calculates
    neighbors.

    Returns the neighbors.
    """
    neighbors = []
    # Add neighbors for origin node
    if elem.get_value() == origin:
        if index_i > 0 and graph[index_i -
                                 1][index_j].get_value() == 'z':
            neighbors.append(graph[index_i - 1][index_j])
        if index_i < len(graph) - 1 and graph[
                index_i + 1][index_j].get_value() == 'z':
            neighbors.append(graph[index_i + 1][index_j])
        if index_j > 0 and graph[index_i][index_j -
                                          1].get_value() == 'z':
            neighbors.append(graph[index_i][index_j - 1])
        if index_j < len(graph[index_i]) - 1 and graph[index_i][
                index_j + 1].get_value() == 'z':
            neighbors.append(graph[index_i][index_j + 1])

    return neighbors

def read_map(file, origin, destination):
    """Given a file it reads a map, also sets the origin and destination and
    finally it applies breadth first search algorithm.
    """
    graph = read_graph(file)

    for index_i, row in enumerate(graph):
        for index_j, elem in enumerate(row):
            neighbors = []

            # Add neighbors for origin node
            if elem.get_value() == origin:
                neighbors = check_origin_neighbors(elem, origin, graph, index_i, index_j)
            else:
                # Check left
                if index_i > 0 and (
                        ord(graph[index_i - 1][index_j].get_value()) +
                        1) >= ord(elem.get_value()):
                    neighbors.append(graph[index_i - 1][index_j])
                # Check right
                if index_i < len(graph) - 1 and (
                        ord(graph[index_i + 1][index_j].get_value()) +
                        1) >= ord(elem.get_value()):
                    neighbors.append(graph[index_i + 1][index_j])
                # Check up
                if index_j > 0 and (
                        ord(row[index_j - 1].get_value()) +
                        1) >= ord(elem.get_value()):
                    neighbors.append(row[index_j - 1])
                # Check down
                if index_j < len(row) - 1 and (
                        ord(row[index_j + 1].get_value()) +
                        1) >= ord(elem.get_value()):
                    neighbors.append(row[index_j + 1])

            # Filter so origin is not valid as neighbor
            neighbors = [
                neighbor for neighbor in neighbors
                if neighbor.get_value() != origin
            ]
            # Add neighbors to elem
            elem.set_neighbors(neighbors)

            # Set origin node
            if elem.get_value() == origin:
                origin_node = elem

    breadth_first_search(origin_node, destination)


if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read().splitlines()

    read_map(input_file, 'E', 'a')
