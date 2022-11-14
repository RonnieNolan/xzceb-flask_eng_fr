import unittest
from translator import watson_trans
from translator import english_2_french
from translator import french_2_english

class english2french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_2_french("Hello"), "Bonjour")
        self.assertEqual(english_2_french("Goodbye"), "Au revoir")
        self.assertEqual(english_2_french("I'll be back"), "Je seral de retour")
        self.assertNotEqual(english_2_french("None"), " ") 
        

class french2english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_2_english("Bonjour"), "Hello")
        self.assertEqual(french_2_english("Au revoir"), "Goodbye")
        self.assertEqual(french_2_english("Je seral de retour"), "I'll be back")
        self.assertNotEqual(french_2_english("None")," ") 
        
unittest.main()
