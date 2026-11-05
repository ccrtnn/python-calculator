import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add1(self):
        self.assertEqual(self.calc.add(1, 3), 4)
    def test_add2(self):
        self.assertEqual(self.calc.add(2, 4), 6)
    def test_add3(self):
            self.assertEqual(self.calc.add(6, -4), 2)

    def test_sub1(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
    def test_sub2(self):
        self.assertEqual(self.calc.subtract(2, 4), -2)
    def test_sub3(self):
            self.assertEqual(self.calc.subtract(-8, -4), -4)

    def test_multi1(self):
        self.assertEqual(self.calc.multiply(0, 0), 0)
    def test_multi2(self):
        self.assertEqual(self.calc.multiply(-4, 2), -8)  
    def test_multi3(self):
            self.assertEqual(self.calc.multiply(-5, -2), 10)  


    def test_divide1(self):
        self.assertEqual(self.calc.divide(6, 0), "not define")
    def test_divide2(self):
        self.assertEqual(self.calc.divide(5, 2), 2)
    def test_divide3(self):
            self.assertEqual(self.calc.divide(8, 2), 4) 

    def test_mod1(self):
        self.assertEqual(self.calc.modulo(6, 2), 0)
    def test_mod2(self):
        self.assertEqual(self.calc.modulo(5, 3), 2)
    def test_mod3(self):
        self.assertEqual(self.calc.modulo(5, 0), "not define")

if __name__ == '__main__':
    unittest.main()