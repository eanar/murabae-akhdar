#!/usr/bin/env python
# Imaginary sentence builder
# Teal bananas are floating in guava juice.

import os
import re
import sys
import random
import argparse

class Common(object):
  getVowels          = 'aeiou'
  getConsonants      = 'bcdfghjklmnpqrstvwxyz'
  getEWordsSilent    = ['close','move','live','have','catalogue']
  getEWordsNonSilent = ['agree','decree','disagree','flee','free',
                        'oversee','be','see','eye','guarantee']
  adjListNor, adjListExq, verbList, nounList, nounListSat = ([] for i in xrange(5))

  @staticmethod
  def writeToFile(dataFile):
    with open(dataFile, 'w') as data:
      data.write(lines)

  @classmethod
  def getRandomFileLine(cls, dataFile, listType, qty):
    with open(dataFile, 'r') as data:
      for i, each in enumerate(data):
        listType.append(each)
      return [ listType[random.randint(0, len(listType))-1].lower() for i in xrange(qty) ]

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
  def getDeterminer(): return random.choice(['The', 'My', 'Some', 'This', 'That', 'Their', 'His', 'Her'])

  @staticmethod
  def getDeterminerPlural(): return random.choice(['Those', 'My', 'Some', 'These', 'Their', 'His', 'Her'])

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
      return func(text).strip()
    return wrap

  @classmethod
  def makeNounPlural(cls, func):
    def wrap(text):
      consonants      = cls.getConsonants
      vowels          = cls.getVowels
      text = func(text).strip()
      if (text[-2] in consonants) and (text[-1] == 'y'):
        return text[:-1]+ 'ies'
      elif text[-2:] == 'ch':
        return text+'es'
      elif (text[-1] == 's'):
        return text
      else:
        return text+'s'
    return wrap

  @classmethod
  def prefixToBe(cls, func):
    def wrap(text):
      vowels          = cls.getVowels
      text = func(text).strip()
      if text[0] in vowels:
        return random.choice(['the ', 'at an ','in an ','on an ','in the ','on the '])+ text
      else:
        return random.choice(['the ','at a ','in a ', 'on a '])+ text
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
      elif text[-1] == 'y':
        return text+'ing'
      elif text.endswith('e') and (text in eWordsNonSilent):
        return text+'ing'
      elif text.endswith('e') and (text in eWordsSilent):
        return text[:-1]+'ing'
      elif text.endswith('e') and (text not in eWordsNonSilent):
        return text[:-1]+'ing'
      elif (text[-1] == 'l') and (text[-2] != 'l') and (len([letter for letter in text if letter in vowels]) == 1):
        return text+'ling'
      elif text[-2:] == 'ic':
        return text+'king'
      elif (len(text) == 3) and (len([letter for letter in text if letter in vowels]) >= 1) and (text[-3] in consonants) and (text[-2] in vowels) and (text[-1] in consonants):
        return text+text[-1]+'ing'
      elif (len(text) >= 4) and (len([letter for letter in text if letter in vowels]) == 1) and (text[-3] in consonants) and (text[-2] in vowels) and (text[-1] in consonants):
        return text+text[-1]+'ing'
      elif (len(text) == 3) and (len([letter for letter in text if letter in vowels]) == 1) and (text[-3] in consonants) and (text[-2] in vowels) and (text[-1] in consonants):
        return text+text[-1]+'ing'
      else:
        return text+'ing'
    return wrap

class Grammar(Common): pass

class Sentence(Grammar):
  @staticmethod
  @Decorators.wordStrip
  @Decorators.makePresentParticiple
  def processVerb(word): return word

  @classmethod
  def getVerbIngList(cls, qty):
      return [ cls.processVerb(each) for each in cls.getRandomFileLine('../res/verbs-list', cls.verbList, qty) ]

  @staticmethod
  @Decorators.wordStrip
  def processAdjective(word): return word

  @classmethod
  def getAdjectiveList(cls, qty):
    return [ cls.processAdjective(each) for each in cls.getRandomFileLine('../res/adjectives-list', cls.adjListNor, qty) ]

  @staticmethod
  @Decorators.adjListExq
  def processAdjectiveExq(word): return word

  @classmethod
  def getAdjectiveExqList(cls, qty):
    return [ cls.processAdjectiveExq(each) for each in cls.getRandomFileLine('../res/adjectives-list-exquisite', cls.adjListExq, qty) ]

  @staticmethod
  @Decorators.wordStrip
  def processNoun(word): return word

  @classmethod
  def getNounList(cls, qty, prefixToBo=False):
    fileName = '../res/nouns-list'
    if prefixToBo:
      return [ cls.getPrefixToBe(cls.processNoun(each)) for each in cls.getRandomFileLine(fileName, cls.nounList, qty) ]
    else:
      return [ cls.processNoun(each) for each in cls.getRandomFileLine(fileName, cls.nounList, qty) ]

  @staticmethod
  @Decorators.wordStrip
  def processNounSat(word): return word

  @staticmethod
  @Decorators.wordStrip
  @Decorators.makeNounPlural
  def processNounSatPlural(word): return word

  @classmethod
  def getNounSatList(cls, qty, pluralize=False):
    fileName = '../res/words-sat-nouns'
    if pluralize:
      return [ cls.processNounSatPlural(each) for each in cls.getRandomFileLine(fileName, cls.nounListSat, qty) ]
    else:
      return [ cls.processNounSat(each) for each in cls.getRandomFileLine(fileName, cls.nounListSat, qty) ]

  @staticmethod
  @Decorators.prefixToBe
  def getPrefixToBe(text): return text

  @staticmethod
  @Decorators.makeNounPlural
  def getNounPlural(text): return text

  @staticmethod
  @Decorators.htmlSpan
  def processHtmlSpan(text): return text

  @classmethod
  def buildSentenceSingleMultiple(cls, quantity):
    w1 = [ cls.getDeterminer() for x in xrange(quantity) ]
    w2 = cls.getAdjectiveExqList(quantity)
    w3 = cls.getNounSatList(quantity)
    w4 = cls.getVerbIngList(quantity)
    w5 = cls.getNounList(quantity, True)    # prefixToBo
    #print w1, w2, w3, w4, w5
    for i in xrange(quantity):
      #print cls.processHtmlSpan( w1[i] +' '+ w2[i] +' '+ w3[i] +' is '+ w4[i] +' '+ w5[i] +'.' )
      print w1[i] +' '+ w2[i] +' '+ w3[i] +' is '+ w4[i] +' '+ w5[i] +'.'

  @classmethod
  def buildSentencePluralMultiple(cls, quantity):
    w1 = [ cls.getDeterminerPlural() for x in xrange(quantity) ]
    w2 = cls.getAdjectiveExqList(quantity)
    w3 = cls.getNounSatList(quantity, True) # Pluralize
    w4 = cls.getVerbIngList(quantity)
    w5 = cls.getNounList(quantity, True)    # prefixToBo
    #print w1, w2, w3, w4, w5
    for i in xrange(quantity):
      #print cls.processHtmlSpan( w1[i] +' '+ w2[i] +' '+ w3[i] +' are '+ w4[i] +' '+ w5[i] +'.' )
      print w1[i] +' '+ w2[i] +' '+ w3[i] +' are '+ w4[i] +' '+ w5[i] +'.'

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-t',  '--type',  type=str, action='store', help='Type: [single|plural]', default='single')
  parser.add_argument('-c',  '--count', type=int, action='store', help='Count: # of sentences to generate', default=1)
  args = parser.parse_args()
  #print "OPTIONS %s" % (args)

  s = Sentence()
  if args.type == 'single':
    s.buildSentenceSingleMultiple(args.count)
  elif args.type == 'plural':
    s.buildSentencePluralMultiple(args.count)
  else:
    print "USAGE: run.py -t plural -c 10"
