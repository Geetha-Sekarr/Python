import unittest

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main() #when you run this script the function will run automatically excute the script and get the reults
#assertequal(this assertion expression 1+1 equal 2)
#unittest.TextTestRunner() you want add one more details use the unittest.TextTestRunner()

#SETUP AND CLEANUP 
import unittest

class MyTestCase(unittest.TestCase):    
    def setUp(self):
        print("Setting up before each test.")
    
    def tearDown(self):
        print("Cleaning up after each test.")
    
    def test_example(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()

#normal opreations
def add_numbers(a,b):
    return a+b
def multiple_numbers(a,b):
    return a*b


#test_math opreations
import unittest
from math_operations import add_numbers, multiply_numbers

# Test case for add_numbers function
class TestAddNumbers(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 1)
        self.assertEqual(add_numbers(0, 0), 0)

# Test case for multiply_numbers function
class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-1, 1), -1)
        self.assertEqual(multiply_numbers(0, 5), 0)
