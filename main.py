from psaw import PushshiftAPI
# for the doc : https://pypi.org/project/psaw/
import datetime as dt
import time

import Submission

api = PushshiftAPI()

import datetime as dt

start = dt.datetime(2017, 1, 1)
end   = dt.datetime(2017, 1, 2)

Subs = Submission.SubmissionList(start, end, 'TIFU', api)
TotalSubs = []
timedelta = dt.timedelta(days=1)

for i in range(100):
	for submission in Subs:
		print(submission)
		print("="*20)
	start = start + timedelta
	end   = end   + timedelta
	TotalSubs.append(Subs)
	time.sleep(10)
	Subs = Submission.SubmissionList(start, end, 'TIFU', api)

