import datetime as dt
import json

from RedditGetter import RedditGetter

# start = dt.datetime(2017, 1, 1)
# end   = dt.datetime(2017, 1, 10)

# Getter = RedditGetter('TIFU', start, end)

# Getter.save("test.json")

Getter = RedditGetter.loadData("test.json")
	
Getter.Show()