import sys
import numpy as np
from functions.generatePersistentNumbersAtStep import generatePersistentNumbersAtStep

start = sys.argv[1]
steps = sys.argv[2]

def parseIntArray(value):
  return np.array([int(value)], dtype='float64')

results = generatePersistentNumbersAtStep(parseIntArray(start), parseIntArray(steps))
print(results)
