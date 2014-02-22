"""
This program is an example of Python's unittest module. 
"""

import unittest
from unittest import TestCase

def title(s):
    "How close is this function to str.title()?"
    return s[0].upper() + s [1:]


class TestTitle(TestCase):
    """
    Class to test how close the function is to str.title().
    """
    
    def test_one_word(self):
        str_test = 'python'
        self.assertEqual(title(str_test), str_test.title(), "Titles are not the same for a single word")
        
    def test_multi_words(self):
        str_test = 'multiple words to test'
        self.assertEqual(title(str_test), str_test.title(), msg = "Titles are not the same for multi-words.")
        
        
if __name__ == '__main__':
    unittest.main()