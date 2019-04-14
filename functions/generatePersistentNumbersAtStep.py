import numpy as np
from functions.generatePersistentNumbers import generatePersistentNumbers

def generatePersistentNumbersAtStep(start, step, base = 10):
  return generatePersistentNumbersAtStepRec(start, step, base)

def generatePersistentNumbersAtStepRec(start, step, base):
  if (step == 0 or len(start) == 0):
    return start
  # recursive call
  print('Testing:', start)
  nextSteps = generatePersistentNumbers(start, base)
  uniqueSteps = np.unique(nextSteps)
  uniqueStepsWithoutStart = np.setdiff1d(uniqueSteps, start)
  return generatePersistentNumbersAtStep(uniqueStepsWithoutStart, step - 1, base)

def generatePersistentNumbersAtStepLoop(start, step, base):
  while (step != 0 and len(start) != 0):
    print('Testing:', start)
    nextSteps = generatePersistentNumbers(start, base)
    uniqueSteps = np.unique(nextSteps)
    start = np.setdiff1d(uniqueSteps, start)
    step = step - 1
  return start
