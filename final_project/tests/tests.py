import unittest
import sys

# setting path
sys.path.append('../')

from machinetranslation.translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour')['translations'][0]['translation'], 'Hello')

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello')['translations'][0]['translation'], 'Bonjour')


if __name__=='__main__':
    unittest.main()