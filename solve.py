import sys
import numpy as np
from solver.solveInBase import solveInBase

number = sys.argv[1]
base = sys.argv[2] if(len(sys.argv) > 1) else '10'

results = solveInBase(number, int(base, 10))
print('Results:', results)
