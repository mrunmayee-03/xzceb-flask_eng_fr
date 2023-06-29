"""Module for french-english translation"""
from deep_translator import MyMemoryTranslator

def english_to_french(englishtext):
    """english to french"""
    translator1 = MyMemoryTranslator(source = 'en-GB',target = 'french canada')
    frenchtext = translator1.translate(englishtext)

    return frenchtext

def french_to_english(frenchtext):
    """french to english"""
    translator2 = MyMemoryTranslator(source = 'french canada',target = 'en-GB')
    englishtext = translator2.translate(frenchtext)

    return englishtext
