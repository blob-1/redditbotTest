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
			Subs = SB.SubmissionList(sub, dateStart, dateStart+timedelta, api)
			dateStart = dateStart + timedelta
			self.__Data.append(Subs)
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
				print(sub.gettext())
			print(data.getStart())
			print(data.getEnd())

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