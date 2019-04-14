from functions.filterForTarget import filterForTarget
from functions.generateOptions import generateOptions

def generatePersistentNumbers(start, base = 10):
  """
  generates a list of numbers when multiplied down go to the start number

  Example:
    3 -> [3, 13, 31]
    9 -> [9, 19, 33, 91]
  """
  return filterForTarget(
    generateOptions(start, 1, base),
    start[:,None],
    base
  )
