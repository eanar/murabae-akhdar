#!/usr/bin/env python

# Teal bananas are floating in guava juice.

import os
import re
import sys
import random

class common(object):    
    adjListNor = []
    adjListExq = []
    nounList   = []
    verbList   = []
    
    def getRandomFileLine(dataFile, listType, callback=None, callback2=None):
        with open(dataFile, 'r') as data:
            for i, each in enumerate(data):
                listType.append(callback(each))
            word = listType[random.randint(0, len(listType))-1].lower()
            if callback2:
                return callback2(word)
            else:
                return word
     
    def callback_adjListExq(text):
        return text.split(':')[0]
    
    def callback_verbList(text): return text.strip()

    def getVowels(): return 'aeiou'

    def getConsonants(): return 'bcdfghjklmnpqrstvwxyz'

    def callback_makePresentParticiple(text, consonants=getConsonants(), vowels=getVowels()):
        if text.endswith('e'):
            return text[:-1]+'ing'
        elif (len(text) == 3) and (text[0] in consonants) and (text[1] in vowels) and (text[2] in consonants):        
            return text+text[2]+'ing'
        else:
            return text+'ing'
    
    #print getRandomFileLine('../res/exquisite-adjectives', adjListExq, callback_adjListExq)
    print getRandomFileLine('../res/verbs-list-3', verbList, callback_verbList, callback_makePresentParticiple)