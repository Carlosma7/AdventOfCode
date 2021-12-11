import os

# What is the power consumption of the submarine?
def power_consumption(report):
    """Calculates power consumption by taking most or least popular value
    for each bit (gamma rate is most and epsilon rate is least).
    Calculates power consumption by multiplying gamma by epsilon rates."""
    gamma_rate = []
    epsilon_rate = []
    # For each bit in any observation
    for bit in range(0, len(report[0])):
      count_ones = [r[bit] == '1' for r in report].count(True)
      count_zeros = [r[bit] == '0' for r in report].count(True)
      if count_ones > count_zeros:
        gamma_rate.append('1')
        epsilon_rate.append('0')
      else:
        gamma_rate.append('0')
        epsilon_rate.append('1')
    
    gamma_rate = int(''.join(gamma_rate), 2)
    epsilon_rate = int(''.join(epsilon_rate), 2)

    return gamma_rate * epsilon_rate

# What is the life support rating of the submarine?
def life_support_rating(report):
  """Calculates life support rating by removing candidates that doesn´t have
  the most or least popular value for each bit (oxygen generator rating
  is most and CO2 scrubber rating is least).
  Calculates life support rating by multiplying them."""
  report_oxr = report.copy()
  # For each bit in any observation for oxygen generator rating
  for bit in range(0, len(report_oxr[0])):
    if len(report_oxr) == 1:
      break
    count_ones = [r[bit] == '1' for r in report_oxr].count(True)
    count_zeros = [r[bit] == '0' for r in report_oxr].count(True)
    if count_ones >= count_zeros:
      index_remove = [index for index in range(0, len(report_oxr)) if report_oxr[index][bit] == '0']
    else:
      index_remove = [index for index in range(0, len(report_oxr)) if report_oxr[index][bit] == '1']
    elem_remove = [report_oxr[i] for i in index_remove]
    [report_oxr.remove(e) for e in elem_remove]

  report_co2 = report.copy()
  # For each bit in any observation for CO2 scrubber rating
  for bit in range(0, len(report_co2[0])):
    if len(report_co2) == 1:
      break
    count_ones = [r[bit] == '1' for r in report_co2].count(True)
    count_zeros = [r[bit] == '0' for r in report_co2].count(True)
    if count_ones >= count_zeros:
      index_remove = [index for index in range(0, len(report_co2)) if report_co2[index][bit] == '1']
    else:
      index_remove = [index for index in range(0, len(report_co2)) if report_co2[index][bit] == '0']
    elem_remove = [report_co2[i] for i in index_remove]
    [report_co2.remove(e) for e in elem_remove]

  
  oxr = int(''.join(report_oxr), 2)
  co2 = int(''.join(report_co2), 2)
  
  return oxr*co2


if __name__ == "__main__":
    # Get path from actual dirname
    dir = os.path.abspath(os.path.dirname(__file__))
    # Join path with filename
    with open(os.path.join(dir, "input.txt")) as file_path:
        # Read path into files
        file = file_path.read().splitlines()

    # First solution
    print(power_consumption(file))
    # Second solution
    print(life_support_rating(file))