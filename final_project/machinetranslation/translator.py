import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

'''
Add code to create an instance of the IBM Watson Language translator in translator.py.
Hint : You may refer to the IBM Watson Language Translation API documents here.
Take a screenshot of your functions and save it
as a .jpg or .png with the filename translator_instance.
You will be prompted to upload the screenshot in the Peer Assignement that follows.

apikey=IAMAuthenticator('2M54JgTID0QsipxoUpTYWJstAjO2Q-nU-I8sIlJzBU4U')
url=LanguageTranslatorV3(version='2018-05-01',authenticator=apikey)
url.set_service_url('https://api.us-south.language-translator.watson.cloud.
ibm.com/instances/5f165e80-9dd8-415f-9458-cdc35d795aec')
'''
#Translation to French
def englishToFrench(englishText):
    #write the code here
    return frenchText

#Translation to English
def frenchToEnglish(frenchText):
    #write the code here
    return englishText
