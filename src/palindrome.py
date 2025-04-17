def is_palindrome(word: str) -> bool:
    if word[0] == word[-1]:
        return True
    return False

import unittest

def is_palindrome(word: str) -> bool:
    if len(word) <= 1:
        return True
    
    left = 0
    right = len(word) - 1
    
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    
    return True
class TestPalindrome(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))
    
    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("X"))
        self.assertTrue(is_palindrome("5"))
    
    def test_two_characters(self):
        self.assertTrue(is_palindrome("aa"))
        self.assertTrue(is_palindrome("11"))
        self.assertFalse(is_palindrome("ab"))
        self.assertFalse(is_palindrome("xy"))