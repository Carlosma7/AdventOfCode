import os


def compute_fuel(pos, crabs, triang):
  """Compute fuel using triangular numbers or just distance."""
  fuel = 0
  for c in crabs:
    if not triang:
      fuel += abs(pos - c)
    else:
      distance = abs(pos - c)
      fuel += (distance ** 2 + distance) // 2

  return fuel

# How much fuel must they spend to align to that position?
def compute_least_fuel(file, triang):
  """Compute least fuel of all positions available."""
  crabs = list(map(int, file.split(',')))

  least_fuel_cost = compute_fuel(min(crabs), crabs, triang)
  for c in range(min(crabs), max(crabs)):
    fuel_cost = compute_fuel(c, crabs, triang)
    if fuel_cost < least_fuel_cost:
      least_fuel_cost = fuel_cost
  
  return least_fuel_cost


if __name__ == "__main__":
    # Get path from actual dirname
    dir = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(dir, "input.txt")) as file_path:
        # Read path into files
        file = file_path.read()

    # First solution
    print(compute_least_fuel(file, False))
    # Second solution
    print(compute_least_fuel(file, True))
