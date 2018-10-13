'''
class Deprecated:
  @classmethod
  def getRandomFileLine_dep(cls, dataFile, listType):
    with open(dataFile, 'r') as data:
      for i, each in enumerate(data):
        listType.append(each)
      return listType[random.randint(0, len(listType))-1].lower()

  @classmethod
  @Decorators.wordStrip
  @Decorators.makePresentParticiple
  def getVerbIng(cls):
    return cls.getRandomFileLine_dep('../res/verbs-list', cls.verbList)

  @classmethod
  @Decorators.wordStrip
  def getAdjective(cls):
    return cls.getRandomFileLine_dep('../res/adjectives-list', cls.adjListNor)

  @classmethod
  @Decorators.adjListExq
  def getAdjectiveExq(cls):
    return cls.getRandomFileLine_dep('../res/adjectives-list-exquisite', cls.adjListExq)

  @classmethod
  @Decorators.wordStrip
  def getNoun(cls):
    return cls.getRandomFileLine_dep('../res/nouns-list', cls.nounList)

  @classmethod
  @Decorators.nounsListSat
  def getNounSat(cls):
    return cls.getRandomFileLine_dep('../res/words-sat-nouns', cls.nounListSat)

  @classmethod
  @Decorators.htmlSpan
  def buildSentenceSingle(cls):
    return cls.getDeterminer() +' '+ cls.getAdjectiveExq() +' '+ cls.getNounSat() +' is '+ cls.getVerbIng() +' '+ cls.getPrefixToBe(cls.getNoun()) +'.'

  @classmethod
  @Decorators.htmlSpan
  def buildSentencePlural(cls):
    return cls.getDeterminerPlural() +' '+ cls.getAdjectiveExq() +' '+ cls.getNounPlural(cls.getNounSat()) +' are '+ cls.getVerbIng() +' '+ cls.getPrefixToBe(cls.getNoun()) +'.'

  @classmethod
  def buildSentenceSingleMultiple_dep(cls, quantity):
    for n in xrange(quantity):
      sentence = cls.buildSentenceSingle()
      print sentence

  @classmethod
  def buildSentencePluralMultiple_dep(cls, quantity):
    for n in xrange(quantity):
      sentence = cls.buildSentencePlural()
      print sentence
'''