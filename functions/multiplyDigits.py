import numpy as np
from functions.numOfDigits import numOfDigits

# multiplyDigits - takes in an array of numbers,
# and returns the product of it's digits
def multiplyDigits(number):
  """
  gives the product of all digits in a number

  Example:
    [567] -> [210]
    [5, 77, 435] -> [5, 49, 60]

  Parameters:
    number: an nDim list of numbers

  Returns:
    an nDim list of the number's digit's product
  """

  # calculate the number of digits and the max number of digits
  # e.g. [4 -> 1, 20 -> 2, 153 -> 3], maxNod -> 3
  nod = numOfDigits(number)
  maxNod = int(np.amax(nod))

  # extra dimensions used for building new shapes
  extraDimensions = (1,) * len(number.shape)

  # tile numbers for as many digits as there are
  # e.g. 212 -> [212, 212, 212]
  tiledNumber = np.tile(number, (maxNod,) + extraDimensions)

  # build range to operate on tiledNumber
  # e.g. maxNod=3 -> [[1], [10], [100]]
  # rangeOperator = 10 ** np.arange(maxNod)[:,None]
  rangeOperator = np.reshape(10 ** np.arange(maxNod), (maxNod,) + extraDimensions)

  # split our numbers into digit arrays
  # (will have fractions at the end for any digits not counted)
  # e.g. 256, max=5 -> [2, 5, 6, 0, 0]
  digitsWithFractions = tiledNumber / rangeOperator
  digits = (tiledNumber // rangeOperator) % 10

  # digits that are less than one before mod is a digit we shouldn't count
  digitsWithOnes = np.where((digitsWithFractions < 1) & (digitsWithFractions > 0), 1, digits)

  # build product
  return np.prod(digitsWithOnes, axis=0)
