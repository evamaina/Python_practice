import unittest
from is_palindrome import *

class TestPalindrome(unittest.TestCase):
  def test_is_palindrome(self):
    self.assertTrue(is_palindrome("madam"))

  def test_is_not_palindrome(self):
    self.assertFalse(is_palindrome("tim")) 

  def test_empty_string_input(self):
        word = ""
        self.assertEqual(
            is_palindrome(word), 'invalid input')

  def test_white_space_string_input(self):
        word = "  "
        self.assertEqual(
            is_palindrome(word), 'invalid input')

  def test_digit_string_input(self):
        word = "2"
        self.assertEqual(
            is_palindrome(word), 'invalid input')
        

  def test_is_palindrome_with_whitespace(self):
        # palindromes with whitespace
        self.assertTrue(is_palindrome("taco cat"))
        self.assertTrue(is_palindrome('race car'))
        self.assertTrue(is_palindrome('nurses run'))

  def test_records_last_5_entries(self):
        store = ["madam", "dad", "nurses run", "nurses", "race car", "cat"]
        self.assertEqual(
            history_record(store), ["dad","nurses run", "nurses", "race car", "cat"])

  def test_records_less_than_5_entries_returns_all(self):
    	store = ["madam", "dad", "nurses run"]
    	self.assertEqual(
        	history_record(store), ["madam", "dad", "nurses run"])
