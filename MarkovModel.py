from nltk import word_tokenize

class MarkovModel(object):
	def __init__(self):
		self.__StartGrams = []
		self.__nGRAMS = {}
		
	def generateModel(self, Data, n = 3):
		self.__nGRAMS = {}
		ngram = ""
		
		for subList in Data:
			for sub in subList:
			
				wordTokens = word_tokenize(sub.gettext())
				
				if len(wordTokens) > 5:
					start = ""
					for word in wordTokens[:3]:
						start += word + " "
					self.__StartGrams.append(start)
				else:
					continue
				
				for i, word in enumerate(wordTokens):
					txt = wordTokens[i:i+n]
					for gram in txt:ngram+=gram+" "
					try:
						nextGram = wordTokens[i+n+1]
					except IndexError:
						break
						
					if ngram not in self.__nGRAMS:
						self.__nGRAMS[ngram] = {nextGram:1}
					else:
						if nextGram not in self.__nGRAMS[ngram]:
							self.__nGRAMS[ngram][nextGram] = 1
						else:
							self.__nGRAMS[ngram][nextGram] += 1
					ngram = ""
						
		print(sorted(self.__nGRAMS.items(), key=lambda item: sortNgram(item)))
		
def sortNgram(nGram):
	value = 0
	for item in nGram[1]:
		value += nGram[1][item]
	return value