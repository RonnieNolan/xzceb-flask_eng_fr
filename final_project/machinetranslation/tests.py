import unittest

from translator import english_2_french
from translator import french_2_english

class TestTranslator(unittest.TestCase): 
    def test_english_2_french(self): 
        self.assertEqual(english_2_french("Hello"), "Bonjour")
        self.assertEqual(english_2_french("Goodbye"), "Au revoir")
        self.assertEqual(english_2_french("I'll be back"), "Je serai de retour")
        self.assertNotEqual(english_2_french("None"), '')
                
    def test_french_2_english(self): 
        self.assertEqual(french_2_english("Bonjour"), "Hello")
        self.assertEqual(french_2_english("Au revoir"), "Goodbye")
        self.assertEqual(french_2_english("Je serai de retour"), "I'll be back")
        self.assertNotEqual(french_2_english("None"),'') 

unittest.main()
