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

def english_2_french ( english_text ) :
#We use the Watson instance to create a dictionary
    french_text = watson_trans . translate ( english_text ,
    model_id = 'en-fr' ) . get_result ( )
    french_text = ( json . dumps ( french_text [ "translations" ]
    [ 0 ] [ "translation" ] , ensure_ascii = False ) )
#And now we have our tranlation ready
    return french_text

def french_2_english ( french_text ) :
#We use the Watson instance to create a dictionary
    english_text = watson_trans . translate ( french_text ,
    model_id = 'fr-en' ) . get_result ( )
    english_text = ( json . dumps ( english_text [ "translations" ]
    [ 0 ] [ "translation" ] , ensure_ascii = False ) )
#And now we have our tranlation ready
    return english_text

print(english_2_french("I'll be back"))
print(english_2_french("Hello"))
print(french_2_english("Je seral de retour"))
