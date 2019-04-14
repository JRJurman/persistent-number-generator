import sys
import numpy as np
from functions.generatePersistentNumbersAtStep import generatePersistentNumbersAtStep

start = sys.argv[1]
steps = sys.argv[2]
base = int(sys.argv[3]) if (len(sys.argv) > 3) else 10

def parseIntArray(value):
  return np.array([int(value)], dtype='float64')

results = generatePersistentNumbersAtStep(parseIntArray(start), parseIntArray(steps), base)
print('Results:', results)
