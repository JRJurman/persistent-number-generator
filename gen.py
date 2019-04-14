import sys
import numpy as np
from functions.generatePersistentNumbersAtStep import generatePersistentNumbersAtStep
from functions.mapListToBase import mapListToBase

start = sys.argv[1]
steps = sys.argv[2]
base = int(sys.argv[3]) if (len(sys.argv) > 3) else 10
extraDigits = int(sys.argv[4]) if (len(sys.argv) > 4) else 1

def parseIntArray(value):
  return np.array([int(value)], dtype='float64')

results = generatePersistentNumbersAtStep(parseIntArray(start), parseIntArray(steps), base, extraDigits)
print('Results:', mapListToBase(results, base))
