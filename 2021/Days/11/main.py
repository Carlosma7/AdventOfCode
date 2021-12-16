import os

class Octopus:
    def __init__(self, id_o, energy):
        self.id_o = id_o
        self.get_neighbors_ids()
        self.energy = energy
        self.flashed = False
        self.neighbors = list()

    def get_neighbors_ids(self):
        if self.id_o == 0: # top left corner
            self.neighbor_id_o = [self.id_o + i for i in (1, 10, 11)]
        elif self.id_o == 9: # top right corner
            self.neighbor_id_o = [self.id_o + i for i in (-1, 9, 10)]
        elif self.id_o == 90: # bottom left corner
            self.neighbor_id_o = [self.id_o + i for i in (-10, -9, 1)]
        elif self.id_o == 99: # bottom right corner
            self.neighbor_id_o = [self.id_o + i for i in (-11, -10, -1)]
        elif self.id_o < 10: # top edge
            self.neighbor_id_o = [self.id_o + i for i in (-1, 1, 9, 10, 11)]
        elif self.id_o > 90: # bottom edge
            self.neighbor_id_o = [self.id_o + i for i in (-11, -10, -9, -1, 1)]
        elif self.id_o % 10 == 0: # left edge
            self.neighbor_id_o = [self.id_o + i for i in (-10, -9, 1, 10, 11)]
        elif self.id_o % 10 == 9: # right edge
            self.neighbor_id_o = [self.id_o + i for i in (-11, -10, -1, 9, 10)]
        else:
            self.neighbor_id_o = [self.id_o + i for i in (-11, -10, -9, -1, 1, 9, 10, 11)]

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def flash(self):
        self.flashed = True
        for neighbor in self.neighbors:
            neighbor.energy += 1

def create_octopuses(vals):
    """Defines a list of octopus objects saving their neighbors too."""
    octopuses = [Octopus(i, vals[i]) for i in range(len(vals))]
    for octopus in octopuses:
        for i in octopus.neighbor_id_o:
            octopus.add_neighbor(octopuses[i])
    return octopuses

def step(octopuses):
    """Computes a single step in the octopuses cavern for every octopus."""
    flashes = 0
    for octopus in octopuses:
        octopus.energy += 1

    repeat = True
    while repeat:
        repeat = False
        for octopus in octopuses:
            if octopus.energy > 9 and octopus.flashed == False:
                octopus.flash()
                flashes += 1
                repeat = True

    for octopus in octopuses:
        if octopus.flashed:
            octopus.flashed = False
            octopus.energy = 0

    return flashes

# How many total flashes are there after 100 steps?
def get_flashes(vals, steps):
    """Calculate the total flashes produced after a total amount of steps."""
    flashes = 0
    octopus = create_octopuses(vals)
    for _ in range(steps):
        flashes += step(octopus)
    return flashes

# What is the first step during which all octopuses flash?
def get_all_flash(vals):
    """Calculate the step where all octopuses flash at the same time."""
    octopus = create_octopuses(vals)
    count_flash = 0
    flashes = 0
    while flashes != 100:
        flashes = step(octopus)
        count_flash += 1
    return count_flash
    
if __name__ == "__main__":
    # Get path from actual dirname
    dir = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(dir, "input.txt")) as file_path:
        # Read path into files
        file = file_path.read().splitlines()
    
    vals = sum([list(map(int, list(line))) for line in file], [])
    print(get_flashes(vals, 100))
    print(get_all_flash(vals))
    