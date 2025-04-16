import unittest
def is_palindrome():...

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
    def test_palindromos_frases(self):
            self.assertTrue(is_palindrome("Anita lava la tina"))
            self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
            self.assertTrue(is_palindrome("No lemon, no melon"))
            self.assertFalse(is_palindrome("Esta frase no es un palíndromo"))

    def test_no_palindromos(self):
            self.assertTrue(is_palindrome(" la tina"))
            self.assertTrue(is_palindrome("maxi"))
            self.assertTrue(is_palindrome("melon"))
            self.assertFalse(is_palindrome("palindromo"))