from functools import reduce
import math


def toBaseN(base):
  def toBaseN_inner(number):
    if (number == 0): return '0'
    maxPower = math.floor(math.log(number, base) + 1e-6)

    def baseBuilderRec(number, power):
      if (power == 0):
        return str(number)

      coeff = number // base ** power
      remainder = number - (coeff * base ** power)
      return str(coeff) + baseBuilderRec(remainder, power - 1)

    return baseBuilderRec(number, maxPower)

  return toBaseN_inner

def multiplyInBase(base):
  def multiply(x, y):
    return toBaseN(base)(int(x, base)*int(y, base))
  return multiply

def spreadCoeff(x):
  return [coeff for coeff in str(x)]

def coeffProdInBase(number, base):
  coeff_prod = reduce(multiplyInBase(base), spreadCoeff(number))
  return coeff_prod

def depth_coeff(N, base, i=0):
  print('Step', i, ':', N)
  return i if int(N, base) < base else depth_coeff(coeffProdInBase(N, base), base, i+1)

def solveInBase(number, base):
  return depth_coeff(number, base)
