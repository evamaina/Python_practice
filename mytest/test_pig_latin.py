import unittest
from pig_latin import *

class TestPigLatin(unittest.TestCase):
  def test_starts_with_consonant(self):
    word = "dog"
    self.assertEqual(pig_latin(word), 'ogday')

  def test_starts_with_group_of_consonants(self):
    word = "trash"
    self.assertEqual(pig_latin(word), 'ashtray')

  def test_starts_with_a_vowel(self):
    word = "andela"
    self.assertEqual(pig_latin(word), 'andelaway')

  
  def test_white_space_string_input(self):
        word = " "
        self.assertEqual(
            pig_latin(word), 'invalid data')
  def test_empty_string_input(self):
      word = ''
      self.assertEqual(
          pig_latin(word), 'invalid data')

  def test_is_alpha_string_input(self):
        word = "2"
        self.assertEqual(
            pig_latin(word), 'invalid data')


  