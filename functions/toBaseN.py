import math

def toBaseN(base = 10):
  """
  converts a number to it's string equivilant in another base

  Example:
    toBase3 = toBaseN(3)
    toBase3(5) -> '12'

  Parameters:
    base: the base we want the new number in

  Returns:
    a function that will convert to that base
  """
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

