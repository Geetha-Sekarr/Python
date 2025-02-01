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

