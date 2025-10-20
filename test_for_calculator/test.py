import unittest
from calculator_print import date1, date2

# define the unit tests
class my_unit_tests(unittest.TestCase):
    def test_date_difference(self):
        # test the difference between two dates
        expected_difference = date1 - date2
        self.assertEqual(expected_difference, date1 - date2)    

# run the tests 
if __name__ == "__main__":
    unittest.main()
    