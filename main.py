import datetime as dt

from RedditGetter import RedditGetter
from MarkovModel import MarkovModel

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--sub", type=str, help="define the sub", required = True)

parser.add_argument("--get", type=eval, default = False, help="fetch data")
parser.add_argument("-n", type=int, default = 0, help="generate a MarkovModel with n-grams")

parser.add_argument("--generate", type=eval, default = False, help="generate a new text tentative")
args = parser.parse_args()

if args.get:
	start = dt.datetime(2020, 2, 1)
	end   = dt.datetime(2020, 2, 2)

	Getter = RedditGetter(args.sub, start, end)

	Getter.save(args.sub+".json")
else:
	Getter = RedditGetter.loadData(args.sub+".json")
	
# Getter.Show()

if args.n:
	MM = MarkovModel()
	MM.generateModel(Getter.getData(), )
	
	MM.save(args.sub+"_MM.json")
else:
	MM = MarkovModel.loadData(args.sub+"_MM.json")
			

if args.generate:
	MM.generateText()
else:
	pass


