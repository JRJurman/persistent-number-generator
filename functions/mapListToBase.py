from functions.toBaseN import toBaseN

def originalAndStringOfBaseN(base):
  def originalAndString(number):
    return (number, toBaseN(base)(number))
  return originalAndString

def mapListToBase(numbers, base = 10):
  """
  convert numpy array into integer of base

  only use for printing
  """
  return list(map(originalAndStringOfBaseN(base), list(map(int, numbers))))
