from psaw import PushshiftAPI # for the doc : https://pypi.org/project/psaw/
import time
import datetime as dt
import codecs, json

import Submission as SB


class RedditGetter(object):
	def __init__(self, sub, dateStart, dateEnd, data = None):
		if data == None:
			self.getDatas(sub, dateStart, dateEnd)
		else:
			self.__sub = sub
			self.__dateStart = dateStart
			self.__dateEnd = dateEnd
			self.__Data = data
		
	def getDatas(self, sub, dateStart, dateEnd):
		self.__sub = sub
		
		self.__Data = []
		timedelta = dt.timedelta(days=1)	
		
		api = PushshiftAPI()
		self.__dateStart = dateStart.isoformat()
		self.__dateEnd = dateEnd.isoformat()	
	
	
		while dateStart < dateEnd:
			self.__Data.append(self.fetchSubmissions(sub, dateStart, dateStart+timedelta, api))
			dateStart = dateStart + timedelta
			time.sleep(20)

	def getSub(self):return self.__sub
	def getStart(self):return self.__dateStart
	def getEnd(self):return self.__dateEnd
	
	def getData(self, day = None, firt = False):
		if day == None:
			return self.__Data
		else:
			if firt:
				return self.__Data[day].getFirstSubmission()
			else:
				return self.__Data[day]				
				
	def save(self, file):
		# jsonData = {}
		# date = self.__dateStart
		# timedelta = dt.timedelta(days=1)
		
		# for data in self.__Data:
			# jsonData[str(date)] = []
			# Subs = data.getSubmissions()
			# for sub in Subs:
				# jsonData[str(date)].append(sub.gettext())

			# date = date + timedelta
			
		json.dump(self, codecs.open(file, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4, default = lambda o: o.__dict__)

	# for testing ONLY !
	def Show(self):
		for data in self.__Data:
			subList = data.getSubmissions()
			for sub in subList:
				print(sub)
			print(data.getStart())
			print(data.getEnd())
			
	def fetchSubmissions(self, sub = None, start = None, end = None, api = None):
		DATA = list(api.search_submissions(
								after=int(start.timestamp()),
								before=int(end.timestamp()),
								subreddit=sub,
								filter=['selftext'],
								limit=None))

		subList = SB.SubmissionList(sub, start.isoformat(), end.isoformat())
		for data in DATA:
			try:
				if not ("[removed]" == data.selftext or "[deleted]" == data.selftext):
					subList.addSubmission(data.selftext)
				else:
					continue
			except AttributeError:
				continue
		return subList

	@classmethod
	def from_json(cls, data):		
		__Data = list(map(SB.SubmissionList.from_json, data["_RedditGetter__Data"]))
		
		return RedditGetter(
						data["_RedditGetter__sub"],
						data["_RedditGetter__dateStart"],
						data["_RedditGetter__dateEnd"],
						__Data
						)
	
	@classmethod	
	def loadData(cls, file):
		with open(file, 'r') as j:
			return RedditGetter.from_json(json.loads(j.read()))