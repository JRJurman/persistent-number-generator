from functions.filterForTarget import filterForTarget
from functions.generateOptions import generateOptions

def generatePersistentNumbers(start):
  return filterForTarget(
    generateOptions(start),
    start
  )
