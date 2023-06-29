"""Module to test french-english translation"""
import unittest

from translator import french_to_english,english_to_french

class testTranslator(unittest.TestCase):
    def test1(self):
        """french to english"""
        self.assertEqual(french_to_english('Bonjour'),'Hello')

    def test2(self):
        """english to french"""
        self.assertEqual(english_to_french('Hello'),'Bonjour')

if __name__ == '__main__':
    unittest.main()

