import numpy as np
from functions.generatePersistentNumbersAtStep import generatePersistentNumbersAtStep
import unittest

class generatePersistentNumbersAtStep_spec(unittest.TestCase):
  """Test generatePersistentNumbersAtStep"""

  def test_single_step(self):
    result = generatePersistentNumbersAtStep(np.array([0]), 1)
    self.assertEqual(result.tolist(), [10, 20, 30, 40, 50, 60, 70, 80, 90])

    result = generatePersistentNumbersAtStep(np.array([3]), 1)
    self.assertEqual(result.tolist(), [13, 31])

    result = generatePersistentNumbersAtStep(np.array([9]), 1)
    self.assertEqual(result.tolist(), [19, 33, 91])

  def test_multi_step(self):
    result = generatePersistentNumbersAtStep(np.array([2]), 2)
    self.assertEqual(result.tolist(), [
        26,  34,  37,  43,  62,  73, 126, 134, 137, 143, 162, 173, 216, 223,
        232, 261, 314, 317, 322, 341, 371, 413, 431, 612, 621, 713, 731.
    ])

if __name__ == '__main__':
    unittest.main()
