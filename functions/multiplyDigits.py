import numpy as np
from functions.numOfDigits import numOfDigits

# multiplyDigits - takes in an array of numbers,
# and returns the product of it's digits
def multiplyDigits(number):
  # calculate the number of digits and the max number of digits
  # e.g. [4 -> 1, 20 -> 2, 153 -> 3], maxNod -> 3
  nod = numOfDigits(number)
  maxNod = np.amax(nod)

  # build a range from 0 to our max number of digits
  # repeat that for however many digits we have
  # e.g. 4 -> 0, 1, 2, 3
  mask = np.mgrid[0:maxNod]

  # split our numbers into digit arrays
  # (will have zeros at the end for any digits not counted)
  # e.g. 256, max=5 -> [2, 5, 6, 0, 0]
  # digits = number // 10 ** np.mgrid[0:maxNod][:, None] % 10
  digits = number // 10 ** np.arange(maxNod, dtype=object) % 10

  # fill in zeros from before with ones, if our nod is less than the max
  # e.g. 256, max=5 -> ([2, 5, 6, 0, 0], nod = 3) -> [2, 5, 6, 1, 1]
  # still keeps any zeros in the original below the nod
  # e.g. 206, max=5 -> ([2, 0, 6, 0, 0], nod = 3) -> [2, 0, 6, 1, 1]
  digitsWithOnes = np.where(mask < nod, digits, 1)

  # build product
  return np.prod(digitsWithOnes, axis=-1)
