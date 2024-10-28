from DiceUtility import calc_dice_average
import unittest

class DiceUtilityTest(unittest.TestCase):
    def test_calc_dice_average(self):
        """
        Test that DiceUtility.calc_dice_average calculates the correct average.
        """
        self.assertEqual(0, calc_dice_average(-1, 6))
        self.assertEqual(0, calc_dice_average(1, -6))
        self.assertEqual(0, calc_dice_average(1, 0))
        self.assertEqual(0, calc_dice_average(0, 1))
        self.assertEqual(3.5, calc_dice_average(1, 6))
        self.assertEqual(7, calc_dice_average(2, 6))
        self.assertEqual(4.5, calc_dice_average(1, 8))

if __name__ == 'main':
    unittest.main()