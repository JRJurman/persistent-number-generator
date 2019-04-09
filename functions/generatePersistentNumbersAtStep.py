import numpy as np
from functions.generatePersistentNumbers import generatePersistentNumbers

def generatePersistentNumbersAtStep(start, step):
  print('Testing:', start)
  if (step == 0 or len(start) == 0):
    return start
  # recursive call
  nextSteps = generatePersistentNumbers(start)
  uniqueSteps = np.unique(nextSteps)
  uniqueStepsWithoutStart = np.setdiff1d(uniqueSteps, start)
  return generatePersistentNumbersAtStep(uniqueStepsWithoutStart, step - 1)
