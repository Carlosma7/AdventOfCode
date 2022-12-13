"""Advent of Code 2022 - Day 12. Part 1."""

import os


class Node:
    """Node class that controls all the info related to a node in
    a graph.
    """
    def __init__(self, value, x_value, y_value):
        """Constructor method considering f for A*"""
        self.__value = value
        self.__x = x_value
        self.__y = y_value
        self.__parent = None
        self.__neighbors = []
        self.__h = 0
        self.__g = 0

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

    def set_f(self, h_value, g_value):
        """Setter for f values."""
        self.__h = h_value
        self.__g = g_value

    def get_g(self):
        """Getter for value of g."""
        return self.__g

    def get_f(self):
        """Getter for coordinates."""
        return self.__h + self.__g

    def __eq__(self, other):
        """Equals method implementation, comparing just coordinates."""
        return self.get_pos() == other.get_pos()


def manhattan(current, destination):
    """Given a node and destination node, it computes the manhattan distance."""
    return sum(
        abs(coord_cur - coord_dest) for coord_cur, coord_dest in zip(
            current.get_pos(), destination.get_pos()))

def a_star_search(origin_node, destination_node):
    """Implementation of A* algorithm."""

    # Initialize open and close
    opened = []
    closed = []

    # Put starting node in open list
    opened.append(origin_node)
    # Until open list is empty
    end_loop = False
    while len(opened) > 0:
        print(len(opened))
        # 1. Find node with least f (f=h+q)
        opened.sort(key=lambda n: n.get_f())

        # 2. Remove it from open list
        current_node = opened.pop(0)

        # 3. Produce descendants
        descendants = current_node.get_neighbors()

        for descendant in descendants:

            # 3.1. If descendant is goal, stop
            if destination_node.get_value() == descendant.get_value():
                descendant.set_parent(current_node)
                closed.append(descendant)
                opened.clear()
                end_loop = True
                break

            # 3.2. Calculate g and h for descendant
            g_value = current_node.get_g() + 1
            h_value = manhattan(current_node, destination_node)
            f_value = g_value + h_value

            # 3.3. If descendant is in open, but has less f, replace parent
            open_node = [
                node for node in opened
                if node == descendant and f_value < node.get_f()
            ]
            if len(open_node) > 0:
                open_node[0].set_parent(current_node)
                open_node[0].set_f(h_value, g_value)
            # 3.4. If descendant is in closed, but has less f, replace parent
            close_node = [
                node for node in closed
                if node == descendant and f_value < node.get_f()
            ]
            if len(close_node) > 0:
                close_node[0].set_parent(current_node)
                close_node[0].set_f(h_value, g_value)

            # 3.5. If descendant not in closed or open list, add to open
            if len([node for node in opened + closed
                    if node == descendant]) == 0:
                descendant.set_parent(current_node)
                descendant.set_f(h_value, g_value)
                opened.append(descendant)

        if end_loop:
            break
        # 4. Add current to close list
        closed.append(current_node)

    # Retrieve the steps generated
    steps = []
    current_node = closed[-1]
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
        if index_i > 0:
            neighbors.append(graph[index_i - 1][index_j])
        if index_i < len(graph) - 1:
            neighbors.append(graph[index_i + 1][index_j])
        if index_j > 0:
            neighbors.append(graph[index_i][index_j - 1])
        if index_j < len(graph[index_i]) - 1:
            neighbors.append(graph[index_i][index_j + 1])

    return neighbors

def read_map(file, origin, destination):
    """Given a file it reads a map, also sets the origin and destination and
    finally it applies A* search algorithm.
    """

    graph = []
    destination_node = destination
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
            neighbors = check_origin_neighbors(elem, origin, graph, index_i, index_j)

            # Check left
            if index_i > 0 and (ord(graph[index_i - 1][index_j].get_value()) -
                                1) <= ord(elem.get_value()):
                neighbors.append(graph[index_i - 1][index_j])
            # Check right
            if index_i < len(graph) - 1 and (
                    ord(graph[index_i + 1][index_j].get_value()) - 1) <= ord(
                        elem.get_value()):
                neighbors.append(graph[index_i + 1][index_j])
            # Check up
            if index_j > 0 and (ord(row[index_j - 1].get_value()) -
                                1) <= ord(elem.get_value()):
                neighbors.append(row[index_j - 1])
            # Check down
            if index_j < len(row) - 1 and (
                    ord(row[index_j + 1].get_value()) - 1) <= ord(
                        elem.get_value()):
                neighbors.append(row[index_j + 1])

            # Filter so origin is not valid as neighbor
            neighbors = [
                neighbor for neighbor in neighbors
                if neighbor.get_value() != origin
            ]
            # Filter so only 'z' is a valid neighbor for 'E'
            for neighbor in neighbors:
                if neighbor.get_value(
                ) == destination and elem.get_value() != 'z':
                    neighbors = [
                        neighbor for neighbor in neighbors
                        if neighbor.get_value() != destination
                    ]
            # Add neighbors to elem
            elem.set_neighbors(neighbors)

            # Set origin node
            if elem.get_value() == origin:
                origin_node = elem

            # Set destination node
            if elem.get_value() == destination:
                destination_node = elem

    a_star_search(origin_node, destination_node)


if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read().splitlines()

    read_map(input_file, 'S', 'E')
