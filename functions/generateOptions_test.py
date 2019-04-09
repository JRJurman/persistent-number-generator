import numpy as np
from functions.generateOptions import generateOptions
import unittest

class generateOptions_spec(unittest.TestCase):
  """Test generateOptions"""

  def test_single_digit_number(self):
    result = generateOptions(np.array([0]))
    self.assertEqual(result.tolist()[0], np.arange(0, 100).tolist())

    result = generateOptions(np.array([3]))
    self.assertEqual(result.tolist()[0], np.arange(0, 100).tolist())

    result = generateOptions(np.array([9]))
    self.assertEqual(result.tolist()[0], np.arange(0, 100).tolist())

  def test_multi_digit_number(self):
    result = generateOptions(np.array([10]))
    self.assertEqual(result.tolist()[0], np.arange(0, 1000).tolist())

    result = generateOptions(np.array([43]))
    self.assertEqual(result.tolist()[0], np.arange(0, 1000).tolist())

    result = generateOptions(np.array([132]))
    self.assertEqual(result.tolist()[0], np.arange(0, 10000).tolist())

  def test_even_single_dimension(self):
    result = generateOptions(np.array([0, 1, 2]))
    self.assertEqual(result.tolist()[0], np.arange(0, 100).tolist())
    self.assertEqual(result.tolist()[1], np.arange(0, 100).tolist())
    self.assertEqual(result.tolist()[2], np.arange(0, 100).tolist())

  def test_odd_single_dimension(self):
    result = generateOptions(np.array([0, 10, 2]))
    solution = np.arange(0, 1000)
    solutionAsList = solution.tolist()
    resultAsList = result.tolist()
    self.assertEqual(len(resultAsList[0]), len(solutionAsList))
    self.assertEqual(len(resultAsList[1]), len(solutionAsList))
    self.assertEqual(len(resultAsList[2]), len(solutionAsList))

if __name__ == '__main__':
    unittest.main()
