class Submission():
	def __init__(self):
		self.__text = []
	
	def addline(self, line):self.__text.append(line)
	
	def gettext(self):return self.__text
	
	def __str__(self):
		text = ''
		for line in self.__text:
			text = text+line+"\n"
		return(text)

	def length(self):return len(self.__text)
		
##################################################

class SubmissionList():
	def __init__(self, sub, start, end, api):
		self.fetchSubmissions(sub, start, end, api)
				
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
			sub = Submission()
			try:
				for character in data.selftext:
					if character == "\n":
						sub.addline(line)
						line = ""
					else:
						line = line + character	

				if sub.length() > 1: 
					self.__Submissions.append(sub)
				else:
					continue
			
			except AttributeError:
				continue
				
	def getSubmissions(self): return self.__Submissions
		
	def getFirstSubmission(self): return self.__Submissions[0]
	
	def __iter__(self): return iter(self.__Submissions)