import numpy as np
from functions.multiplyDigits import multiplyDigits
import unittest

class multiplyDigits_spec(unittest.TestCase):
  """Test multiplyDigits"""

  def test_single_digit(self):
    result = multiplyDigits(np.array([4]))
    self.assertEqual(result, 4)

    result = multiplyDigits(np.array([1]))
    self.assertEqual(result, 1)

    result = multiplyDigits(np.array([0]))
    self.assertEqual(result, 0)

  def test_single_number(self):
    result = multiplyDigits(np.array([20]))
    self.assertEqual(result, 0)

    result = multiplyDigits(np.array([300]))
    self.assertEqual(result, 0)

    result = multiplyDigits(np.array([4872]))
    self.assertEqual(result, 448)

    result = multiplyDigits(np.array([24]))
    self.assertEqual(result, 8)

  def test_single_dimension_list(self):
    result = multiplyDigits(np.array([11,12,13,14,15]))
    self.assertEqual(result.tolist(), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
