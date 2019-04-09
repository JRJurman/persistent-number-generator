import numpy as np
from functions.numOfDigits import numOfDigits
import unittest

class numOfDigits_spec(unittest.TestCase):
  """Test numOfDigits"""

  def test_single_number(self):
    result = numOfDigits(np.array([10]))
    self.assertEqual(result, 2)

    result = numOfDigits(np.array([110]))
    self.assertEqual(result, 3)

    result = numOfDigits(np.array([4535]))
    self.assertEqual(result, 4)

  def test_single_dimension_list(self):
    result = numOfDigits(np.array([10, 20, 55]))
    self.assertEqual(result.tolist(), [2, 2, 2])

    result = numOfDigits(np.array([6554]))
    self.assertEqual(result.tolist(), [4])

    result = numOfDigits(np.array([10, 23054, 6554]))
    self.assertEqual(result.tolist(), [2, 5, 4])

  def test_multi_dimension_list(self):
    result = numOfDigits(np.array([[10, 20, 55], [30, 33, 35]]))
    self.assertEqual(result.tolist(), [[2, 2, 2], [2, 2, 2]])

    result = numOfDigits(np.array([[1, 2440, 5], [350, 33, 34346895]]))
    self.assertEqual(result.tolist(), [[1, 4, 1], [3, 2, 8]])

if __name__ == '__main__':
    unittest.main()
