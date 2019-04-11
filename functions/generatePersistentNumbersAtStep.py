import numpy as np
from functions.generatePersistentNumbers import generatePersistentNumbers

def generatePersistentNumbersAtStep(start, step):
  return generatePersistentNumbersAtStepRec(start, step)

def generatePersistentNumbersAtStepRec(start, step):
  if (step == 0 or len(start) == 0):
    return start
  # recursive call
  print('Testing:', start)
  nextSteps = generatePersistentNumbers(start)
  uniqueSteps = np.unique(nextSteps)
  uniqueStepsWithoutStart = np.setdiff1d(uniqueSteps, start)
  return generatePersistentNumbersAtStep(uniqueStepsWithoutStart, step - 1)

def generatePersistentNumbersAtStepLoop(start, step):
  while (step != 0 and len(start) != 0):
    print('Testing:', start)
    nextSteps = generatePersistentNumbers(start)
    uniqueSteps = np.unique(nextSteps)
    start = np.setdiff1d(uniqueSteps, start)
    step = step - 1
  return start
