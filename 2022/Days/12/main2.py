"""Advent of Code 2022 - Day 12. Part 2."""

import os


class Node:
    """Node class that controls all the info related to a node in
    a graph.
    """
    def __init__(self, value, x_value, y_value):
        """Constructor method for node."""
        self.__value = value
        self.__x = x_value
        self.__y = y_value
        self.__parent = None
        self.__neighbors = []

    def get_value(self):
        """Getter for value of node."""
        return self.__value

    def set_parent(self, parent):
        """Setter for value of parent."""
        self.__parent = parent

    def get_parent(self):
        """Getter for value of parent."""
        return self.__parent

    def set_neighbors(self, neighbors):
        """Setter for value of neighbors."""
        self.__neighbors = neighbors

    def get_neighbors(self):
        """Getter for value of neighbors."""
        return self.__neighbors

    def get_pos(self):
        """Getter for coordinates."""
        return [self.__x, self.__y]

    def __eq__(self, other):
        """Equals method implementation, comparing just coordinates."""
        return self.get_pos() == other.get_pos()

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
    steps = []
    current_node = visited[-1]
    while current_node != origin_node:
        steps.append(current_node)
        current_node = current_node.get_parent()

    # Get total steps
    print(len(steps))


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
    graph = []
    for line in file:
        row = []
        line_list = []
        line_list[:0] = line
        for elem in line_list:
            row.append(Node(elem, len(graph), len(row)))
        graph.append(row)

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
