


# This bot will retweet every 5 minutes, 
# using your search query for the 5 newest tweets.

# If you haven't changed credentials.py yet with your own Twitter
# account settings, this script will tweet at twitter.com/lacunybot

# Setting up bot
# credentials.py contains twitter access app keys
import tweepy, time 
from twython import Twython, TwythonError
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# tweets excluded from retweeting because of language
# key words used in search query
naughty_words = [" -RT", "fuck", "niger"]
good_words = ["rams touchdown", "touchdown rams", "td rams"]
filter = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = filter + blacklist

# harnessing twitter's search query
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

search_results = twitter.search(q=keywords, count=10)
try:
   for tweet in search_results["statuses"]:
       try:
           twitter.retweet(id = tweet["id_str"])
       except TwythonError as e:
           print e
except TwythonError as e:
   print e




