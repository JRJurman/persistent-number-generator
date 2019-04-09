import numpy as np
from functions.numOfDigits import numOfDigits

def generateOptions(start):
  """
  build nDim range of all possible values that could multiply to starting value

  Example:
    1 -> [0, 1, 2, 3, ... 97, 98, 99]

  Parameters:
    start: nDim array of starting integers

  Returns:
    (n + 1)Dim array of possible integers
  """

  nod = numOfDigits(start) + 1
  maxNod = np.amax(nod)
  ranges = np.tile(np.arange(10**maxNod), (len(start), 1))
  return np.where(ranges < np.array(10**nod)[:, None], ranges, 0)
