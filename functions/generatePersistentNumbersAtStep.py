from functions.generatePersistentNumbers import generatePersistentNumbers

def generatePersistentNumbersAtStep(start, step):
  print('testing', step, start)
  if (step == 0):
    return start
  # recursive call
  nextSteps = list(generatePersistentNumbers([start])[0])
  return list(map(lambda nextstep: generatePersistentNumbersAtStep(nextstep, step - 1), nextSteps))
