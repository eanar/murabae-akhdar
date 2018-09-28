#!/usr/bin/env python
# Imaginary sentence builder
# Teal bananas are floating in guava juice.

import os
import re
import sys
import random

class Common(object):
  adjListNor, adjListExq, verbList, nounList, nounListSat = ([] for i in xrange(5))
  getVowels          = 'aeiou'
  getConsonants      = 'bcdfghjklmnpqrstvwxyz'
  getEWordsSilent    = ['close','move','live','have']
  getEWordsNonSilent = ['be','see']

  @classmethod
  def getRandomFileLine(cls, dataFile, listType, callback=None, callback2=None):
    with open(dataFile, 'r') as data:
      for i, each in enumerate(data):
        if callback:
          each = callback(each)
        listType.append(each)
      word = listType[random.randint(0, len(listType))-1].lower()
      if callback2:
        return callback2(word)
      else:
        return word

  @classmethod
  def getRandomFileLineTest(cls, dataFile, listType, callback=None, callback2=None):
    with open(dataFile, 'r') as data:
      for i, each in enumerate(data):
        word = callback(each).lower()
        print word
        if callback2:
          print '  '+callback2(word)
        else:
          print '  '+word

  @staticmethod
  def callback_nounsListSat(text):
    return text.split()[1].strip()

  @staticmethod
  def callback_adjListExq(text):
    return text.split(':')[0]

  @staticmethod
  def callback_wordStrip(text): return text.strip()

  @staticmethod
  def getToBe(): return random.choice(['in', 'in a', 'in the', 'on', 'on a', 'on the'])

  @staticmethod
  def getDeterminer(): return random.choice(['The', 'My', 'Some', 'This'])

  @classmethod
  def test(cls, test=None): print cls.getConsonants

class Grammar(Common):
  @classmethod
  def callback_makePresentParticiple(cls, text):
    consonants      = cls.getConsonants
    vowels          = cls.getVowels
    eWordsSilent    = cls.getEWordsSilent
    eWordsNonSilent = cls.getEWordsNonSilent
    if text[-2:] == 'ie':
      return text[:-2]+'ying'
    elif text.endswith('e') and (text in eWordsNonSilent):
      return text+'ing'
    elif text.endswith('e') and (text in eWordsSilent):
      return text[:-1]+'ing'
    elif text.endswith('e') and (text not in eWordsNonSilent):
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

  @classmethod
  def callback_makeNounPlural(cls, text): pass

class Sentence(Grammar):
  @classmethod
  def getVerbIng(cls):
    return cls.getRandomFileLine('../res/verbs-list', cls.verbList, cls.callback_wordStrip, cls.callback_makePresentParticiple)

  @classmethod
  def getAdjective(cls):
    return cls.getRandomFileLine('../res/adjectives-list', cls.adjListNor, cls.callback_wordStrip)

  @classmethod
  def getAdjectiveExq(cls):
    return cls.getRandomFileLine('../res/adjectives-list-exquisite', cls.adjListExq, cls.callback_adjListExq)

  @classmethod
  def getNoun(cls):
    return cls.getRandomFileLine('../res/nouns-list', cls.nounList, cls.callback_wordStrip)

  @classmethod
  def getNounSat(cls):
    return cls.getRandomFileLine('../res/nouns-list-sat', cls.nounListSat, cls.callback_nounsListSat)

  @classmethod
  def buildSentenceSingle(cls):
    return cls.getDeterminer() +' '+ cls.getAdjectiveExq() +' '+ cls.getNounSat() +' is '+ cls.getVerbIng() +' '+ cls.getToBe() +' '+ cls.getNoun() +'.'

  @classmethod
  def buildSentencePlural(cls): pass

if __name__ == '__main__':
  s = Sentence()
  print s.buildSentenceSingle()
  #print s.getVerbIng()
  #print s.getAdjective()
  #print s.getAdjectiveExq()
  #print s.getNounSat()
  #print s.getNoun()