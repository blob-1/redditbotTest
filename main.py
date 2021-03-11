import datetime as dt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from RedditGetter import RedditGetter

start = dt.datetime(2017, 1, 1)
end   = dt.datetime(2017, 1, 2)

Getter = RedditGetter('TIFU', start, end)

# Getter.getData(day = None, firt = False)
# Getter.getData(day = 1, firt = False)
# Getter.getData(day = 1, firt = True)

Getter.save("test.json")
