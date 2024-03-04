import unittest


# Define a class that inherits from unittest.TestCase
class TestMathFunctions(unittest.TestCase):

    # Define test methods starting with 'test_'
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(3 - 1, 2)


# This block allows running the tests from the command line
if __name__ == '__main__':
    unittest.main()
