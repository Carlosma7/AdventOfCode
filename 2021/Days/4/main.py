import os

# Class panel/board of Bingo
class Panel():
  """Manages the  behaviour of a single panel, checking numbers, 
  if it has a winner or getting the final score."""

  # Create a panel using the values in a list of lists
  def __init__(self, values):
    """Constructor of a panel using values from a list of lists."""
    self.__values = values
    self.__checked = [[False for x in range(0, len(values))] for x in range(0, len(values))]

  # Mark a number in a panel
  def mark_number(self, number):
    """Mark a number if it´s contained in a panel, marking it with an X."""
    for row in range(0, len(self.__values)):
      if number in self.__values[row]:
        for col in range(0, len(self.__values)):
          if self.__values[row][col] == number:
            self.__values[row][col] = 'X'
  
  # Check winner by rows and columns
  def check_winner(self):
    """Checks if a panel has a row or a column complete with X, then it´s the winner."""
    # Check by rows
    for row in range(0, len(self.__values)):
        if all(x == 'X' for x in self.__values[row]):
          return f"Row {row}"
    
    # Check by columns transposing the matrix
    checked_values = list(map(list, zip(*self.__values)))
    for row in range(0, len(checked_values)):
        if all(x == 'X' for x in checked_values[row]):
          return f"Col {row}"
  
  # Get the final score
  def get_result(self, row_col, value, last_number):
    """Computes the result of the panel by summing all the non-X values."""
    result = 0

    if row_col:
      # Rows
      for row in range(0, len(self.__values)):
        if row != value:
          result += sum([x for x in self.__values[row] if x != 'X'])
    else:
      # Columns
      checked_values = list(map(list, zip(*self.__values)))
      for row in range(0, len(checked_values)):
        if row != value:
          result += sum([x for x in checked_values[row] if x != 'X'])

    return result * last_number

# Class Bingo for a game
class Bingo():
  """Manages the behaviour of a Bingo party with the first-wins approach
  or the last-wins approach."""

  # Create a list of numbers and the panels given a file
  def __init__(self, file):
    """Constructor of a panel using values from a file."""
    self.__numbers = list(map(int, file[0].split(',')))
    self.__panels = []

    for i in range(2, len(file), 6):
      new_panel_values = []
      for j in range(0, 5):
        new_panel_values.append(list(map(int, file[i+j].split())))
      new_panel = Panel(new_panel_values)
      self.__panels.append(new_panel)
  
  # What will your final score be if you choose that board?
  def play(self):
    """Plays a party of a first-wins approach."""
    for number in self.__numbers:
      for panel in self.__panels:
        panel.mark_number(number)
        winner = panel.check_winner()
        if winner:
          row_col = winner.split()[0]
          value = winner.split()[1]
          return panel.get_result(row_col, value, number)
  
  # Once it wins, what would its final score be?
  def play_last(self):
    """Plays a party of a last-wins approach. Removes any winner except
    the last one."""
    for number in self.__numbers:
      panels_to_remove = []
      for panel in self.__panels:
        panel.mark_number(number)
        winner = panel.check_winner()
        if winner:
          panels_to_remove.append(panel)
            
      for ptr in panels_to_remove:
        if len(self.__panels) > 1:
          self.__panels.remove(ptr)
        else:
          row_col = winner.split()[0]
          value = winner.split()[1]
          return panel.get_result(row_col, value, number)
          
    
if __name__ == "__main__":
    # Get path from actual dirname
    dir = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(dir, "input.txt")) as file_path:
        # Read path into files
        file = file_path.read().splitlines()

    # First solution
    bingo = Bingo(file)
    print(bingo.play())
    # Second solution
    bingo = Bingo(file)
    print(bingo.play_last())