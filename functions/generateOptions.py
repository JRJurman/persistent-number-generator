import numpy as np
from functions.numOfDigits import numOfDigits

def generateOptions(start):
  nod = numOfDigits(start) + 1
  maxNod = np.amax(nod)
  ranges = np.tile(np.arange(10**maxNod), (len(start), 1))
  return np.where(ranges < np.array(10**nod)[:, None], ranges, 0)
