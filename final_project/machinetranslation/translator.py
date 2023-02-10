import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv('apikey')

url = os.getenv('url')

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-02-10',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)


def english_to_french(english_text):
    """
        Function that translates english text to french text
    """
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

    return translation

def french_to_english(french_text):
    """
    Function that translates french text to english text
    """

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    return translation
