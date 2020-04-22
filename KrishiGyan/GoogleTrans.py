# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:00:35 2020

@author: Shubham
"""
#
#import googletrans
#
#print(googletrans.LANGUAGES)
#
from googletrans import Translator

text1 = '''
A Római Birodalom (latinul Imperium Romanum) az ókori Róma által létrehozott 
államalakulat volt a Földközi-tenger medencéjében
'''

text2 = '''
 chutie 
'''

translator = Translator()

translated = translator.translate('namaste aap kese ho', dest='s')

print(translated.text)
#
#dt1 = translator.detect(text1)
#print(dt1)
#
#dt2 = translator.detect(text2)
#print(dt2)