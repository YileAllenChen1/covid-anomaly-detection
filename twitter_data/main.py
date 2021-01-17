import json
import tweepy as tw
from tweepy import OAuthHandler
 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tw.API(auth)

#search_term = '#covid'   #('#covid OR #coronavirus')
search_term = "#covid"

tweets = tw.Cursor(api.search,
                   q=search_term,
                   lang="en",
                   since='2020-11-01',
                   ).items(100)  # until='2020-11-8'

with open('results.json', 'a') as f:
    for tweet in tweets:
        f.write(tweet.text)

all_tweets = [tweet.text for tweet in tweets]

print(all_tweets[:5])
