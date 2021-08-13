import tweepy
import json

with open("tokens.json","r") as f:
    tokens = json.load(f)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(tokens["api key"], tokens["api secret key"])
auth.set_access_token(tokens["access token"], tokens["access token secret"])

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Create a tweet
#api.update_status("@maxhalim likes to eat shoes")

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        
    def on_status(self, tweet):
        print(f"{tweet.user.name} just tweeted\n{tweet.text}")
        
    def on_error(self, status):
        print("ERRRRRRRRRRRRRRRORRRROROROR")
'''     
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=[""], languages=["en","id"])
'''
imagePath = "warbler.jpg"
status = "Hi! From my Python script =)"

# Send the tweet.
api.update_with_media(imagePath, status)    
    