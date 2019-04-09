from functions.generatePersistentNumbers import generatePersistentNumbers

def generatePersistentNumbersAtStep(start, step):
  if (step == 0):
    return start
  # recursive call
  nextSteps = generatePersistentNumbers(start)
  return generatePersistentNumbersAtStep(nextSteps, step - 1)
