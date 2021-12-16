import os

# How many measurements are larger than the previous measurement?
def measurement(lst):
	"""Counts the increases produced in a list of measurements."""
	return [int(lst[i]) > int(lst[i - 1]) for i in range(1, len(lst))].count(True)

# Consider sums of a three-measurement sliding window. 
# How many sums are larger than the previous sum?
def three_measurement(lst):
	"""Counts the increases produced from each sum of three measurements."""
	three_list = [int(lst[i - 2]) + int(lst[i - 1]) + int(lst[i]) for i in range(2, len(lst))]
	return measurement(three_list)

if __name__ == "__main__":
	# Get path from actual dirname
	dir = os.path.abspath(os.path.dirname(__file__))
	# Join path with filename
	with open(os.path.join(dir, "input.txt")) as file_path:
		# Read path into files
		file = file_path.read().splitlines()

	# First solution
	print(measurement(file))
	# Second solution
	print(three_measurement(file))
