from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Submission(object):
	def __init__(self, text = None):
		self.__text = text
	
	def gettext(self):return self.__text
	
	def __str__(self):
		text = ''
		for line in self.__text:
			text = text+line+"\n"
		return(text)

	def length(self):return len(self.__text)
	
	def set_text(self, text): self.__text = text
	
	@classmethod
	def from_json(cls, data): return Submission(data["_Submission__text"])
		
##################################################

class SubmissionList(object):
	def __init__(self, sub, start, end, api = None, Submissions = None):
		if api != None:
			self.fetchSubmissions(sub, start, end, api)
		else:
			self.__start = start
			self.__end = end
			self.__sub = sub
			self.__Submissions = Submissions
				
	def fetchSubmissions(self, sub = None, start = None, end = None, api = None):
		self.__start = start.isoformat()
		self.__end = end.isoformat()
		self.__sub = sub
		
		DATA = list(api.search_submissions(
								after=int(start.timestamp()),
								before=int(end.timestamp()),
								subreddit=sub,
								filter=['selftext'],
								limit=None))

		self.__Submissions = []
		for data in DATA:
			line = ""
			try:
				if not ("[removed]" == data.selftext or "[deleted]" == data.selftext):
					sub = Submission(data.selftext)
					self.__Submissions.append(sub)
				else:
					continue
			except AttributeError:
				continue
		
	def getStart(self): return self.__start
	def getEnd(self): return self.__end
		
	def getSubmissions(self): return self.__Submissions
		
	def getFirstSubmission(self): return self.__Submissions[0]
	
	def __iter__(self): return iter(self.__Submissions)
	
	@classmethod
	def from_json(cls, data):
		__Submissions = list()
		for d in data["_SubmissionList__Submissions"]:
			__Submissions.append(Submission.from_json(d))

		return SubmissionList(
							data["_SubmissionList__sub"],
							data["_SubmissionList__start"],
							data["_SubmissionList__end"],
							Submissions = __Submissions
							)