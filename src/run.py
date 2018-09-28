#!/usr/bin/env python

# Teal bananas are floating in guava juice.

import os
import re
import sys
import random

class Common(object):    
    adjListNor   = []
    adjListExq   = []
    nounList     = []
    verbList     = []
    silentEWords = []
    
    def getRandomFileLine(dataFile, listType, callback=None, callback2=None):
        with open(dataFile, 'r') as data:
            for i, each in enumerate(data):
                listType.append(callback(each))
            word = listType[random.randint(0, len(listType))-1].lower()
            if callback2:
                return callback2(word)
            else:
                return word
              
    def getRandomFileLineTest(dataFile, listType, callback=None, callback2=None):
        with open(dataFile, 'r') as data:
            for i, each in enumerate(data):
                word = callback(each).lower()
                print word
                if callback2:
                    print '  '+callback2(word)
                else:
                    print '  '+word

    def callback_adjListExq(text):
        return text.split(':')[0]
    
    def callback_verbList(text): return text.strip()

    def getVowels(): return 'aeiou'
    def getConsonants(): return 'bcdfghjklmnpqrstvwxyz'
    def getEWordsSilent(): return ['close','move','live','have']
    def getEWordsNonSilent(): return ['be','see']

    def callback_makePresentParticiple(text, consonants=getConsonants(), vowels=getVowels(), eWordsSilent=getEWordsSilent(), eWordsNonSilent=getEWordsNonSilent()):
        if text[-2:] == 'ie':
            return text[:-2]+'ying'
        elif text.endswith('e') and (text in eWordsNonSilent):
            return text+'ing'
        elif text.endswith('e') and (text in eWordsSilent):
            return text[:-1]+'ing'
        elif text[-1] == 'l':
            return text+'ling'
        elif text[-2:] == 'ic':
            return text+'king'
        elif (len([letter for letter in text if letter in vowels]) >= 2) and (text[-3] in consonants) and (text[-2] in vowels) and (text[-1] in consonants):
            return text+text[-1]+'ing'
        elif (len(text) == 3) and (len([letter for letter in text if letter in vowels]) == 1) and (text[-3] in consonants) and (text[-2] in vowels) and (text[-1] in consonants):        
            return text+text[2]+'ing'
        else:
            return text+'ing'
    
    #print getRandomFileLine('../res/exquisite-adjectives', adjListExq, callback_adjListExq)
    #print getRandomFileLine('../res/verbs-list-test', verbList, callback_verbList, callback_makePresentParticiple)
    print getRandomFileLineTest('../res/verbs-list-test', verbList, callback_verbList, callback_makePresentParticiple)