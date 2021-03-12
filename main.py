import datetime as dt

from RedditGetter import RedditGetter
from MarkovModel import MarkovModel

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--get", type=eval, default = True, help="fetch data")
parser.add_argument("--sub", type=str, help="define the sub", required = True)
args = parser.parse_args()

if args.get:
	start = dt.datetime(2020, 2, 1)
	end   = dt.datetime(2020, 2, 4)

	Getter = RedditGetter(args.sub, start, end)

	Getter.save(args.sub+".json")
else:
	Getter = RedditGetter.loadData(args.sub+".json")
	
# Getter.Show()

# MM = MarkovModel()
# MM.generateModel(Getter.getData())


