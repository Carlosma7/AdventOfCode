"""Advent of Code 2022 - Day 12. Node class."""

from node import Node

def read_graph(file):
    """Given a file it reads a graph with all nodes."""
    graph = []

    for line in file:
        row = []
        line_list = []
        line_list[:0] = line
        for elem in line_list:
            row.append(Node(elem, len(graph), len(row)))
        graph.append(row)
    return graph

def retrieve_path(path, origin_node):
    """Given a list of nodes it retrieves the path and prints total of steps."""
    # Retrieve the steps generated
    steps = []
    current_node = path[-1]
    while current_node != origin_node:
        steps.append(current_node)
        current_node = current_node.get_parent()

    # Get total steps
    print(len(steps))
