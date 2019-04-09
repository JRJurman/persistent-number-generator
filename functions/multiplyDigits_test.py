import numpy as np
from functions.multiplyDigits import multiplyDigits
import unittest

class multiplyDigits_spec(unittest.TestCase):
  """Test multiplyDigits"""

  def test_single_digit(self):
    result = multiplyDigits([4])
    self.assertEqual(result, 4)

    result = multiplyDigits([1])
    self.assertEqual(result, 1)

    result = multiplyDigits([0])
    self.assertEqual(result, 0)

  def test_single_number(self):
    result = multiplyDigits([20])
    self.assertEqual(result, 0)

    result = multiplyDigits([300])
    self.assertEqual(result, 0)

    result = multiplyDigits([4872])
    self.assertEqual(result, 448)

    result = multiplyDigits([24])
    self.assertEqual(result, 8)

  def test_single_dimension_list(self):
    result = multiplyDigits(np.array([11,12,13,14,15]))
    self.assertEqual(result, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
