# from nltk import word_tokenize
from random import choice, randint
import codecs, json

class MarkovModel(object):
	def __init__(self, StartGrams = {}, nbStartGrams = 0, nGRAMS = {}, n = 0):
		self.__StartGrams = StartGrams
		self.__nbStartGrams = nbStartGrams
		self.__nGRAMS = nGRAMS
		self.__n = n
		
	def generateModel(self, Data, n = 3):
		self.__nGRAMS = {}
		self.__n = n
		
		for subList in Data:
			for sub in subList:
			
				wordTokens = cutAtSpaces(sub.gettext())
				
				if len(wordTokens) > 5:
					start = ""
					for word in wordTokens[:n]:
						start += word + " "

					if start not in self.__StartGrams.keys():
						self.__StartGrams[start] = 1
					else:
						self.__StartGrams[start] += 1
					self.__nbStartGrams += 1
						
				else:
					continue
				
				for i, word in enumerate(wordTokens):
					txt = wordTokens[i:i+n]
					ngram = ""
					for gram in txt:
						ngram += gram + " "
					try:
						nextGram = wordTokens[i+n]
					except IndexError:
						break
						
					if ngram not in self.__nGRAMS:
						self.__nGRAMS[ngram] = {nextGram:1}
					else:
						if nextGram not in self.__nGRAMS[ngram]:
							self.__nGRAMS[ngram][nextGram] = 1
						else:
							self.__nGRAMS[ngram][nextGram] += 1
						
		# print(sorted(self.__nGRAMS.items(), key=lambda item: sortNgram(item)))
		# print(self.__StartGrams)
		
	def generateText(self):
		# find first nGRAM
		target = randint(0, self.__nbStartGrams-1)
		i = 0
		STARTnGRAM = ""
		for key in self.__StartGrams.keys():
			if i == target:
				STARTnGRAM = key
				break
			i += 1
		else:
			STARTnGRAM = key
		
		# find subsequent GRAMS
		NEWnGRAM = STARTnGRAM
		TEXT = STARTnGRAM
		newgram = ""
		while True:
			try:
				newgram, NEWnGRAM = self.__findnextGram(NEWnGRAM)
			except KeyError: # if we reach a key error then we are at the end of a text ^^
				break
			TEXT += newgram + " "
		print(TEXT)
		
	def __findnextGram(self, PREVnGRAM):		
		cpt = 0
		for key in self.__nGRAMS[PREVnGRAM]:
			cpt += self.__nGRAMS[PREVnGRAM][key] # get nb of possibility
		
		target = randint(0, cpt)	
		i = 0
		newgram = ""
		for key in self.__nGRAMS[PREVnGRAM].keys():
			if i >= target:
				newgram = key
				break
			i += self.__nGRAMS[PREVnGRAM][key]
		else:
			newgram = key
			
		NEWGnRAM = ""
		for gram in cutAtSpaces(PREVnGRAM)[1:]:
			NEWGnRAM += gram + " "
		NEWGnRAM += newgram + " "
			
		return newgram, NEWGnRAM
		
	def save(self, file):		
		json.dump(self, codecs.open(file, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4, default = lambda o: o.__dict__)	
	
	@classmethod	
	def loadData(cls, file):
		with open(file, 'r') as j:
			return MarkovModel.from_json(json.loads(j.read()))
		
	@classmethod
	def from_json(cls, data):
		return MarkovModel(
						data["_MarkovModel__StartGrams"],
						data["_MarkovModel__nbStartGrams"],
						data["_MarkovModel__nGRAMS"],
						data["_MarkovModel__n"]
						)
		
def sortNgram(nGram):
	value = 0
	for item in nGram[1]:
		value += nGram[1][item]
	return value
	
def cutAtSpaces(string):
	tab = []
	word = ""
	for chars in string:
		if chars == " ":
			tab.append(word)
			word = ""
		else:
			word+=chars
	else:
		if word != "":
			tab.append(word)
	return tab