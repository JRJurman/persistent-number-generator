from functions.multiplyDigits import multiplyDigits

def filterForTarget(listOfNumbers, target):
  """
  given a list of numbers, find which numbers multiply to get our number

  Example:
    ([20, 21, 22, 23, 24, 25, 26, 27, 28, 29], 8) -> [24]

  Parameters:
    listOfNumbers: nDim integers
    target: (n-1)Dim integers

  Returns:
    nDim results
  """
  products = multiplyDigits(listOfNumbers)
  return listOfNumbers[products == target]
