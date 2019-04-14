import numpy as np
from functions.numOfDigits import numOfDigits

def generateOptions(start, extraDigits = 1, base = 10):
  """
  build nDim range of all possible values that could multiply to starting value

  Example:
    1 -> [0, 1, 2, 3, ... 97, 98, 99]

  Parameters:
    start: nDim array of starting integers

  Returns:
    (n + 1)Dim array of possible integers
  """

  nod = numOfDigits(start, base) + extraDigits
  maxNod = np.amax(nod)
  ranges = np.tile(np.arange(base**maxNod), (len(start), 1))
  return np.where(ranges < np.array(base**nod)[:, None], ranges, 0)
