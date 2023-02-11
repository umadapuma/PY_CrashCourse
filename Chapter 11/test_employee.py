import unittest
from Exercise_2 import Employee

class Employee(unittest.TestCase):
    
    def setUp(self):
        self.bob = Employee("Bob","Billy",30000)

    def test_give_default_raise(self):
        self.bob.salary.give_raise()
        self.assertEqual(self.bob.salary,35000)

 #   def test_give_custom_raise(self):
  #      pass
if __name__ == '__main__':
    unittest.main()