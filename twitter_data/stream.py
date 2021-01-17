from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
 
consumer_key = 'DgNQUkT9Vkq8bC2zfRVoxxg5F'
consumer_secret = 'aJGLZllbydCnExRDNNmj4wWnp7xlPrlGmGRYdqFwHMRyeqnGfI'
access_token = '1350260972762624001-LV6fdef040msGNe5kIcKD5fDN03W5v'
access_secret = 'AvNJmppiAg1SxTczfKe9e9mKGrQi4CATwZH4bYY8jhLK1'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#covid'])