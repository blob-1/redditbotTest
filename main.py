import datetime as dt
import json

from RedditGetter import RedditGetter

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--get", type=eval, default = True, help="fetch data")
args = parser.parse_args()

if args.get:
	start = dt.datetime(2017, 1, 1)
	end   = dt.datetime(2017, 1, 3)

	Getter = RedditGetter('TIFU', start, end)

	Getter.save("test.json")
else:
	Getter = RedditGetter.loadData("test.json")
	
Getter.Show()



