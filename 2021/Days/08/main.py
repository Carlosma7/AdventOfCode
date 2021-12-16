import os

representation = "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg"

def count_1_4_7_8(file):
  """Count number of 1,4,7,8 occurrences in outputs from file."""
  count = 0
  for line in file:
    output = line.split('|')[1]
    for o in output.split():
      if len(o) in [2,4,3,7]:
        count += 1
  
  return count

def get_frequencies(word):
  """Get the frequencies of letters in word"""
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  return {l: str(word.count(l)) for l in list(letters)}

def get_value(freq, word):
  """Get the frequency value for a word."""
  temp = [freq[l] for l in list(word)]
  temp.sort()
  return int(''.join(temp))

def sort_letters(word):
  word = list(word)
  word.sort()
  return ''.join(word)

def decode(file):
  """Decode the total sum of the outputs codes decoded."""
  frequency = get_frequencies(representation)
  value = {}

  for i, digit_representation in enumerate(representation.split(' ')):
    numeric_reppresentation = get_value(frequency, digit_representation)
    value[numeric_reppresentation] = str(i)

  total = 0
  for inputs, numbers in file:
    input_frequencies = get_frequencies(inputs)
    input_digits = {sort_letters(word): value[get_value(input_frequencies, word)]
                      for word in inputs.split(' ')}

    total += int(''.join([input_digits[sort_letters(number)] for number in numbers.split(" ")]))

  return total

if __name__ == "__main__":
    # Get path from actual dirname
    dir = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(dir, "input.txt")) as file_path:
        # Read path into files
        file = file_path.read().splitlines()
        inputs_outputs = [[part for part in line.split(" | ")] for line in file]

    # First solution
    print(count_1_4_7_8(file))
    # Second solution
    print(decode(inputs_outputs))
