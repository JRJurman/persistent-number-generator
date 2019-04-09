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
    result = generatePersistentNumbersAtStep(np.array([2]), 2)
    self.assertEqual(result.tolist(), [
        2,  12,  21,  26,  34,  43,  62, 126, 134, 143, 162, 216, 223,
        232, 261, 314, 322, 341, 413, 431, 612, 621, 37, 73, 137, 173,
        317, 371, 713, 731
    ])

if __name__ == '__main__':
    unittest.main()
