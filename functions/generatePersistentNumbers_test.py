import numpy as np
from functions.generatePersistentNumbers import generatePersistentNumbers
import unittest

class generatePersistentNumbers_spec(unittest.TestCase):
  """Test generatePersistentNumbers"""

  def test_single_digit_number(self):
    result = generatePersistentNumbers(np.array([0]))
    self.assertEqual(result.tolist(), [0, 10, 20, 30, 40, 50, 60, 70, 80, 90])

    result = generatePersistentNumbers(np.array([3]))
    self.assertEqual(result.tolist(), [3, 13, 31])

    result = generatePersistentNumbers(np.array([9]))
    self.assertEqual(result.tolist(), [9, 19, 33, 91])

  def test_multi_digit_number(self):
    result = generatePersistentNumbers(np.array([10]))
    self.assertEqual(result.tolist(), [ 25,  52, 125, 152, 215, 251, 512, 521])

  def test_even_single_dimension(self):
    result = generatePersistentNumbers(np.array([3, 4, 5]))
    self.assertEqual(result.tolist(), [3, 13, 31, 4, 14, 22, 41, 5, 15, 51])

    result = generatePersistentNumbers(np.array([13, 24]))
    self.assertEqual(result.tolist(), [38, 46, 64, 83, 138, 146, 164, 183, 226, 234, 243, 262, 318, 324, 342, 381, 416, 423, 432, 461, 614, 622, 641, 813, 831])

  # def test_odd_single_dimension(self):
  #   result = generatePersistentNumbers(np.array([0, 10, 2]))
  #   solution = np.arange(0, 1000)
  #   solutionAsList = solution.tolist()
  #   resultAsList = result.tolist()
  #   self.assertEqual(len(resultAsList[0]), len(solutionAsList))
  #   self.assertEqual(len(resultAsList[1]), len(solutionAsList))
  #   self.assertEqual(len(resultAsList[2]), len(solutionAsList))

if __name__ == '__main__':
    unittest.main()
