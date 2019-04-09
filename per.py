import sys
from 'functions/generatePersistentNumbersAtStep.py' import generatePersistentNumbersAtStep

start = sys.argv[1]
steps = sys.argv[2]

results = generatePersistentNumbersAtStep(int(start), int(steps))
print(results)
