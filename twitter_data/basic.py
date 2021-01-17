import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'DgNQUkT9Vkq8bC2zfRVoxxg5F'
consumer_secret = 'aJGLZllbydCnExRDNNmj4wWnp7xlPrlGmGRYdqFwHMRyeqnGfI'
access_token = '1350260972762624001-LV6fdef040msGNe5kIcKD5fDN03W5v'
access_secret = 'AvNJmppiAg1SxTczfKe9e9mKGrQi4CATwZH4bYY8jhLK1'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)

#So the code above can be re-written to process/store the JSON:
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)
#What if we want to have a list of all our followers? There you go:
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)
#And how about a list of all our tweets? Simple:
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)

def process_or_store(tweet):
    print(json.dumps(tweet))

