import os

# Compute the number of lanternfish
def compute_lanternfish(file, days):
  """Computes the evolutive behaviour of lanternfishes and procreates
  a new one every 7 days, creating a new one."""
  fishes = list(map(int, file.split(',')))
  
  # Every 7 days it creates a new fish
  for day in range(days):
    new_fishes = []
    for f in range(len(fishes)):
      # A day less for every fish
      fishes[f] = fishes[f]-1
      # Restart timer and create a new one
      if fishes[f] == -1:
        fishes[f] = 6
        new_fishes.append(8)
    fishes.extend(new_fishes)
  
  return len(fishes)


if __name__ == "__main__":
    # Get path from actual dirname
    dir = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(dir, "input.txt")) as file_path:
        # Read path into files
        file = file_path.read()

    # First solution
    print(compute_lanternfish(file, 80))
    # Second solution
    print(compute_lanternfish(file, 256))
