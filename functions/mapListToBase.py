from functions.toBaseN import toBaseN

def mapListToBase(numbers, base = 10):
  """
  convert numpy array into integer of base
  """
  return list(map(toBaseN(base), list(map(int, numbers))))
