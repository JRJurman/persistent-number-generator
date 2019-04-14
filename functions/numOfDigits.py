import numpy as np

def numOfDigits(number, base = 10):
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
  # natural log (number) / log (base) = log of base (number)
  numOfDigits = np.floor(np.log(number) / np.log(base))

  # log of 0 is -inf, so we'll just set that to 0 digits
  numOfDigits[numOfDigits < 0] = 0

  return numOfDigits + 1
