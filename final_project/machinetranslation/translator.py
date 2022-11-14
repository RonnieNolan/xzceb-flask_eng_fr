import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os . environ [ 'apikey' ]
url = os . environ [ 'url' ]

apikey = IAMAuthenticator ( apikey )
watson_trans = LanguageTranslatorV3 ( version = '2018-05-01' , authenticator = apikey )
watson_trans . set_service_url ( url )

def english_2_french(english_text):
#We use the Watson instance to create a dictionary
    translation = watson_trans.translate(text=english_text,
    model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
#And now we have our tranlation ready
    return french_text

def french_2_english(french_text):
#We use the Watson instance to create a dictionary
    translation = watson_trans.translate(text=french_text,
    model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
#And now we have our tranlation ready
    return english_text
'''
print(english_2_french("How are you?"))
print(english_2_french("Hello"))
print(french_2_english("Bonjour"))
print(french_2_english("Comment es-tu?"))
'''