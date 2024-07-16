import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
     def setUp(self):
        """Set up the SimpleCalculator instance before each test."""

        self.calc = SimpleCalculator()

     def test_addition(self):
        """Test the addition method."""

        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, 2), 7)
        self.assertEqual(self.calc.add(-2, 6), 4)
        self.assertEqual(self.calc.add(1.5, 2.5), 4) 
        self.assertEqual(self.calc.add(1.8, 9.2), 11)
        self.assertEqual(self.calc.add(3.4, 1.6), 5)
        self.assertEqual(self.calc.add(0.7, 2.5), 3.2)

     def test_subtraction(self):
          """Test the subtraction method."""

          self.assertEqual(self.calc.subtract(2, 1), 1)
          self.assertEqual(self.calc.subtract(6, 3), 3)
          self.assertEqual(self.calc.subtract(1, 4), -3)
          self.assertEqual(self.calc.subtract(4, 3), 1)
          self.assertEqual(self.calc.subtract(7, 5), 2)
          self.assertEqual(self.calc.subtract(3, 1), 2)

     def test_multiplication(self):
        """Test the multiply method."""

        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(6, 3), 18)
        self.assertEqual(self.calc.multiply(9, 4), 36)
        self.assertEqual(self.calc.multiply(7, 1), 7)
        self.assertEqual(self.calc.multiply(-2, -1), 2)
        self.assertEqual(self.calc.multiply(-7, -3), 21)

     def test_division(self):
        """Test the division method."""

        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertEqual(self.calc.divide(5, 2), 2.5)


if __name__ == "__main__":
    unittest.main()
