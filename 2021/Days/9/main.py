import os
from math import prod

# What is the sum of the risk levels of all low points on your heightmap?
def sum_risk_levels(file):
  sum_risk = 0
  heatmap = []
  for line in file:
    heatmap.append(list(map(int,list(line))))
  
  for row in range(len(heatmap)):
    for col in range(len(heatmap[0])):
      adjacents = []
      if row > 0:
        adjacents.append(heatmap[row-1][col])
      if row < len(heatmap)-1:
        adjacents.append(heatmap[row+1][col])
      if col > 0:
        adjacents.append(heatmap[row][col-1])
      if col < len(heatmap[0])-1:
        adjacents.append(heatmap[row][col+1])
      if all(heatmap[row][col] < x for x in adjacents):
        sum_risk += heatmap[row][col] + 1

  return sum_risk

def define_heightmap(file):
  """Define the height map using the file."""
  heightmap = {}
  for y, row in enumerate(file):
      for x, height in enumerate(row):
          heightmap[(x, y)] = int(height)
  return heightmap

def get_lowpoints(heightmap):
  """Calculate the low points from height map. These are the ones that doesn´t have lower points in their nearest."""
  points = []

  for coords, height in heightmap.items():
      x, y = coords
      neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

      if all(height < heightmap.get(neighbour, 10) for neighbour in neighbours):
          points.append(coords)

  return points

def move_basin(heightmap, point):
  """Calculats the basins from a low point in the height map."""
  basin = set([point])
  stack = [point]
  while stack:
      x, y = stack.pop()
      neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
      for neighbour in neighbours:
          height = heightmap.get(neighbour, 0)
          if heightmap[(x, y)] < height and height != 9:
              stack.append(neighbour)
              basin.add(neighbour)
  return len(basin)

# What do you get if you multiply together the sizes of the three largest basins?
def multiply_basins(file):
  """Get the prod of the 3 highest basins, calculating the height map, lows and then the basins."""
  heightmap = define_heightmap(file)
  lowpoints = get_lowpoints(heightmap)
  basins = sorted([move_basin(heightmap, l) for l in lowpoints], reverse=True)

  return prod(basins[:3])

if __name__ == "__main__":
    # Get path from actual dirname
    dir = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(dir, "input.txt")) as file_path:
        # Read path into files
        file = file_path.read().splitlines()

    # First solution
    print(sum_risk_levels(file))
    # Second solution
    print(multiply_basins(file))
