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
    
    def getRandomFileLine(dataFile, listType, callback):
        with open(dataFile, 'r') as data:
            for i, each in enumerate(data):
                listType.append(callback(each))
            return listType[random.randint(0, len(listType))-1].lower()
     
    def callback_adjListExq(text):
        return text.split(':')[0]
    
    print getRandomFileLine('../res/exquisite-adjectives', adjListExq, callback_adjListExq)