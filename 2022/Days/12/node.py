"""Advent of Code 2022 - Day 12. Node class."""


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
