#!/bin/bash

# This bot will retweet every 5 minutes, 
# using your search query for the 5 newest tweets.

# Setting up bot
# credentials.py contains twitter access app keys
# make sure twython and tweepy are installed
import tweepy, time 
from twython import Twython, TwythonError
from credentials import *

#This logs us in to twitter using the tweepy library
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#From this api we can search tweets, create tweets, 
# delete tweets and find twitter users.
api = tweepy.API(auth)

# tweets excluded from retweeting because of language
# key words used in search query
naughty_words = [" -RT", "fuck", "nigger"]
good_words = ["rams touchdown", "touchdown rams", "td rams"]
filter = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = filter + blacklist

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# harnessing twitter's search query
# decide how many times you wish to retweet per cycle. 
# As you see I put '5'.
search_results = twitter.search(q=keywords, count=5)
try:
   for tweet in search_results["statuses"]:
       try:
           twitter.retweet(id = tweet["id_str"])
       except TwythonError as e:
           print e
except TwythonError as e:
   print e
