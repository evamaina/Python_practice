import unittest
from age import ageCalculator

class TestAge(unittest.TestCase):
  def test_correct_age_is_calculated(self):
    birth_year = 1990
    self.assertTrue(ageCalculator(birth_year) == 28)

# if __name__ == '__main__':
# 	unittest.main()