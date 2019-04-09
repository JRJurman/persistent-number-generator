import numpy as np
from functions.generatePersistentNumbersAtStep import generatePersistentNumbersAtStep
import unittest

class generatePersistentNumbersAtStep_spec(unittest.TestCase):
  """Test generatePersistentNumbersAtStep"""

  def test_single_step(self):
    result = generatePersistentNumbersAtStep(np.array([0]), 1)
    self.assertEqual(result.tolist(), [0, 10, 20, 30, 40, 50, 60, 70, 80, 90])

    result = generatePersistentNumbersAtStep(np.array([3]), 1)
    self.assertEqual(result.tolist(), [3, 13, 31])

    result = generatePersistentNumbersAtStep(np.array([9]), 1)
    self.assertEqual(result.tolist(), [9, 19, 33, 91])

  def test_multi_step(self):
    result = generatePersistentNumbersAtStep(np.array([3]), 2)
    self.assertEqual(result.tolist(), [3, 13, 31])

if __name__ == '__main__':
    unittest.main()
