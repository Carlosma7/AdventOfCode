"""Advent of Code 2022 - Day 7."""

import os

class Node:
    """Class that controls the behaviour of a node in the tree representation"""
    def __init__(self, parent, name: str, size: int, ftype: str):
        self.__parent = parent
        self.__children = []
        self.__name = name
        self.__size = size
        self.__type = ftype

    def add(self, new_child):
        """Adds a new node as child of the current node"""
        self.__children.append(new_child)

    def get_children(self):
        """Getter for children"""
        return self.__children

    def get_name(self):
        """Getter for name"""
        return self.__name

    def get_parent(self):
        """Getter for parent node"""
        return self.__parent

    def get_size(self):
        """Getter for size"""
        return self.__size

    def is_file(self):
        """Checks whether the node is a file node or not"""
        if self.__type == 'file':
            return True
        return False

    def add_size(self, size):
        """Sums the size of a child node and sums to it's parent node too"""
        self.__size += size
        if self.__name != '/':
            self.__parent.add_size(size)

class Tree:
    """Class that controls the behaviour of a tree in a file system"""
    def __init__(self):
        self.__root = Node(parent=None, name='/', size=0, ftype='dir')
        self.__current_node = None
        self.__list_nodes = [self.__root]

    def cd_command(self, name):
        """Changes current directory between node changes"""
        if name == '/':
            self.__current_node = self.__root
        elif name == '..':
            self.__current_node = self.__current_node.get_parent()
        else:
            children = self.__current_node.get_children()
            for child in children:
                if child.get_name() == name:
                    self.__current_node = child
                    break

    def ls_command(self, ls_lines):
        """Given some lines it creates the corresponding nodes with it's information"""
        for line in ls_lines:
            data = line.split()
            if data[0] == 'dir':
                new_node = Node(parent=self.__current_node, name=data[1], size=0, ftype='dir')
            else:
                new_node = Node(parent=self.__current_node, name=data[1],
                    size=int(data[0]), ftype='file')
            self.__current_node.add(new_node)
            self.__list_nodes.append(new_node)

    def generate_tree(self, file):
        """Reads a file and generates the corresponding tree with the lines description"""
        for index, line in enumerate(file):
            if line[0] == '$':
                command = line[2:]
                if command[:2] == 'cd':
                    self.cd_command(command.split()[1])
                else:
                    ls_index = index+1
                    while '$' not in file[ls_index] and ls_index < len(file)-1:
                        ls_index += 1

                    self.ls_command(file[index+1: ls_index])

    def get_sum_less_100000(self):
        """Gets the sum of all directory nodes that has a size up to 100000"""
        # Get all file nodes
        files = [n for n in self.__list_nodes if n.is_file()]
        for file in files:
            file.get_parent().add_size(file.get_size())

        dirs = [d for d in self.__list_nodes if not d.is_file() and d.get_size() <= 100000]

        print(sum((dr.get_size() for dr in dirs)))

    def get_file_to_remove(self):
        """Gets the smallest file size that leaves 300000 of space when removing it"""
        dirs = [d for d in self.__list_nodes if not d.is_file()]

        dirs.sort(key=lambda d: d.get_size())

        free_space = 70000000 - dirs[-1].get_size()

        for dir_rem in dirs:
            if dir_rem.get_size() + free_space >= 30000000:
                print(dir_rem.get_size())
                break

if __name__ == "__main__":
    # Get path from actual dirname
    path = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(path, "input.txt"), encoding="utf8") as file_path:
        # Read path into groups
        input_file = file_path.read().splitlines()

    tree = Tree()
    tree.generate_tree(input_file)
    tree.get_sum_less_100000()
    tree.get_file_to_remove()
