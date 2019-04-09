import numpy as np

def numOfDigits(number):
  """
  given a list of numbers, return the number of digits that number has

  Example:
    [567] -> [3]
    [5, 77, 435] -> [1, 2, 3]

  Parameters:
    number: an nDim list of numbers to process

  Returns:
    an nDim list of values
  """
  numOfDigits = np.floor(np.log10(number))

  # log10 of 0 is -inf, so we'll just set that to 0 digits
  numOfDigits[numOfDigits < 0] = 0

  numOfDigits += 1
  return numOfDigits
