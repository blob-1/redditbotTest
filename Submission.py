class Submission(object):
	def __init__(self, text = None):
		self.__text = text
	
	def gettext(self):return self.__text
	
	def __str__(self):
		text = ''
		for word in self.__text:
			text = text+word 
		return(text)

	def length(self):return len(self.__text)
	
	def set_text(self, text): self.__text = text
	
	@classmethod
	def from_json(cls, data): return Submission(data["_Submission__text"])
		
##################################################

class SubmissionList(object):
	def __init__(self, sub, start, end, Submissions =[]):
			self.__start = start
			self.__end = end
			self.__sub = sub
			self.__Submissions = Submissions
		
	def getStart(self): return self.__start
	def getEnd(self): return self.__end
	
	def addSubmission(self, sub): self.__Submissions.append(Submission(sub))
		
	def getSubmissions(self): return self.__Submissions
		
	def getFirstSubmission(self): return self.__Submissions[0]
	
	def __iter__(self): return iter(self.__Submissions)
	
	@classmethod
	def from_json(cls, data):
		__Submissions = []
		for d in data["_SubmissionList__Submissions"]:
			__Submissions.append(Submission.from_json(d))

		return SubmissionList(
							data["_SubmissionList__sub"],
							data["_SubmissionList__start"],
							data["_SubmissionList__end"],
							Submissions = __Submissions
							)