#!/usr/bin/env python
# Imaginary sentence builder
# Teal bananas are floating in guava juice.

import os
import re
import sys
import random

class Common(object):
  getVowels          = 'aeiou'
  getConsonants      = 'bcdfghjklmnpqrstvwxyz'
  getEWordsSilent    = ['close','move','live','have','catalogue']
  getEWordsNonSilent = ['be','see']
  adjListNor, adjListExq, verbList, nounList, nounListSat = ([] for i in xrange(5))

  @classmethod
  def getRandomFileLine(cls, dataFile, listType):
    with open(dataFile, 'r') as data:
      for i, each in enumerate(data):
        listType.append(each)
      return listType[random.randint(0, len(listType))-1].lower()

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
  def callback_htmlSpan(text):
    return '<span id="test">'+ text +'</span></ br>'

  @staticmethod
  def getToBe_(): return random.choice(['in', 'in a', 'in the', 'on', 'on a', 'on the'])

  @staticmethod
  def getDeterminer(): return random.choice(['The', 'My', 'Some', 'This', 'That', 'Their', 'His', 'Her'])

  @classmethod
  def test(cls, test=None): print cls.getConsonants

class Decorators(Common):
  @staticmethod
  def htmlSpan(func):
    def wrap(text):
      return '<span id="test">'+ func(text) +'</span></ br>'
    return wrap

  @staticmethod
  def wordStrip(func):
    def wrap(text):
      return func(text).strip()
    return wrap

  @staticmethod
  def adjListExq(func):
    def wrap(text):
      return func(text).split(':')[0]
    return wrap

  @staticmethod
  def nounsListSat(func):
    def wrap(text):
      return func(text).split()[1].strip()
    return wrap

  @classmethod
  def prefixToBe(cls, func):
    def wrap(text):
      vowels          = cls.getVowels
      text = func(text).strip()
      if text[0] in vowels:
        return random.choice(['at an ','in an ','on an ','at the ','in the ','on the '])+ text
      else:
        return random.choice(['at a ','in a ', 'on a '])+ text
    return wrap

  @classmethod
  def makePresentParticiple(cls, func):
    def wrap(text):
      consonants      = cls.getConsonants
      vowels          = cls.getVowels
      eWordsSilent    = cls.getEWordsSilent
      eWordsNonSilent = cls.getEWordsNonSilent
      text = func(text).strip()
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
      elif (len(text) >= 3) and (len([letter for letter in text if letter in vowels]) == 1) and (text[-3] in consonants) and (text[-2] in vowels) and (text[-1] in consonants):
        return text+text[2]+'ing'
      else:
        return text+'ing'
    return wrap

class Grammar(Common):
  @classmethod
  def callback_makeNounPlural(cls, text): pass

class Sentence(Grammar):
  @classmethod
  @Decorators.wordStrip
  @Decorators.makePresentParticiple
  def getVerbIng(cls):
    return cls.getRandomFileLine('../res/verbs-list', cls.verbList)

  @classmethod
  @Decorators.wordStrip
  def getAdjective(cls):
    return cls.getRandomFileLine('../res/adjectives-list', cls.adjListNor)

  @classmethod
  @Decorators.adjListExq
  def getAdjectiveExq(cls):
    return cls.getRandomFileLine('../res/adjectives-list-exquisite', cls.adjListExq)

  @classmethod
  @Decorators.wordStrip
  def getNoun(cls):
    return cls.getRandomFileLine('../res/nouns-list', cls.nounList)

  @classmethod
  @Decorators.nounsListSat
  def getNounSat(cls):
    return cls.getRandomFileLine('../res/nouns-list-sat', cls.nounListSat)

  @staticmethod
  @Decorators.prefixToBe
  def getPrefixToBe(text):
    return text

  @classmethod
  @Decorators.htmlSpan
  def buildSentenceSingle(cls):
    return cls.getDeterminer() +' '+ cls.getAdjectiveExq() +' '+ cls.getNounSat() +' is '+ cls.getVerbIng() +' '+ cls.getPrefixToBe(cls.getNoun()) +'.'

  @classmethod
  def buildSentencePlural(cls): pass

  @classmethod
  def buildSentenceSingle_genMultiple(cls, quantity):
    for n in xrange(quantity):
      sentence = cls.buildSentenceSingle()
      print sentence

if __name__ == '__main__':
  s = Sentence()
  #print s.buildSentenceSingle()
  s.buildSentenceSingle_genMultiple(110)
  #print s.getVerbIng()
  #print s.getAdjective()
  #print s.getAdjectiveExq()
  #print s.getNounSat()
  #print s.getNoun()
  #print s.getPrefixToBe(s.getNoun())
