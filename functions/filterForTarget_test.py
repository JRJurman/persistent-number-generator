import numpy as np
from functions.filterForTarget import filterForTarget
import unittest

class filterForTarget_spec(unittest.TestCase):
  """Test filterForTarget"""

  def test_single_digit_list(self):
    result = filterForTarget(np.array([1,2,3,4,5]), np.array([5]))
    self.assertEqual(result, [5])

  def test_double_digit_list(self):
    result = filterForTarget(np.array([11,12,13,14,15]), np.array([5]))
    self.assertEqual(result, [15])

  def test_odd_digit_list(self):
    result = filterForTarget(np.array([21,152,13,154,125]), np.array([10]))
    self.assertEqual(result.tolist(), [152, 125])

if __name__ == '__main__':
    unittest.main()
