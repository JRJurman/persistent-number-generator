import numpy as np

def numOfDigits(number):
  numOfDigits = np.floor(np.log10(number))
  numOfDigits[numOfDigits < 0] = 0
  numOfDigits += 1
  return numOfDigits
