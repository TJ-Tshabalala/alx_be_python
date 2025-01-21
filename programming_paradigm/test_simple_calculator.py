import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-1,1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3,2),1)
        self.assertEqual(self.calc.subtract(1,7),-6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5,3), 15)
        self.assertEqual(self.calc.multiply(7,2),14)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8,2),4)
        self.assertEqual(self.calc.divide(200,10),20)

if __name__ =="__main__":
    unittest.main()