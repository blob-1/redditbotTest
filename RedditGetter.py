from psaw import PushshiftAPI # for the doc : https://pypi.org/project/psaw/
import time
import datetime as dt
import codecs, json

import Submission


class RedditGetter():
	def __init__(self, sub, dateStart, dateEnd):
		self.getDatas(sub, dateStart, dateEnd)
		
	def getDatas(self, sub, dateStart, dateEnd):
		self.__sub = sub
		self.__dateStart = dateStart.isoformat()
		self.__dateEnd = dateEnd.isoformat()
		
		self.__Data = []
		timedelta = dt.timedelta(days=1)	
		
		api = PushshiftAPI()
	
		while dateStart < dateEnd:
			Subs = Submission.SubmissionList(sub, dateStart, dateEnd, api)
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