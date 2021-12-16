import os
from collections import deque

# What is the total syntax error score for those errors?
def get_corrupted_score(file):
  """Compute the score of a line checking if syntax markers doesn´t close each other."""
  score = 0
  for line in file:
    chars = []
    for symbol in list(line):
      if symbol in ['(', '[', '{', '<']:
        chars.append(symbol)
      else:
        if symbol == ')' and chars[-1] == '(':
          chars.pop(len(chars)-1)
        elif symbol == ']' and chars[-1] == '[':
          chars.pop(len(chars)-1)
        elif symbol == '}' and chars[-1] == '{':
          chars.pop(len(chars)-1)
        elif symbol == '>' and chars[-1] == '<':
          chars.pop(len(chars)-1)
        else:
          if symbol == ')':
            score += 3
          elif symbol == ']':
            score += 57
          elif symbol == '}':
            score += 1197
          elif symbol == '>':
            score += 25137
          break
  
  return score

# What is the middle score?
def get_incomplete_score(filename):
  """Compute the score of unclosed syntax markers to fit correctly."""
  scores = []
  for line in open(filename):
    error = False
    queue = deque()
    for c in line.strip():
      if c in ['(', '[', '{', '<']:
        queue.append(c)
      elif c == ')':
        if queue[-1] != '(':
          error = True
          break
        else:
          queue.pop()
      elif c == ']':
        if queue[-1] != '[':
          error = True
          break
        else:
          queue.pop()
      elif c == '}':
        if queue[-1] != '{':
          error = True
          break
        else:
          queue.pop()
      elif c == '>':
        if queue[-1] != '<':
          error = True
          break
        else:
          queue.pop()
    if not error:
      score = 0
      values = {'(': 1, '[': 2, '{': 3, '<': 4}
      for symbol in reversed(queue):
        score = score*5 + values[symbol]
      scores.append(score)
  scores.sort()
  return scores[len(scores)//2]

if __name__ == "__main__":
    # Get path from actual dirname
    dir = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(dir, "input.txt")) as file_path:
        # Read path into files
        file = file_path.read().splitlines()

    # First solution
    print(get_corrupted_score(file))
    # Second solution
    print(get_incomplete_score('input.txt'))
