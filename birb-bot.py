import tweepy
import json
import time
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
    def __init__(self, api, time_limit=60):
        self.api = api
        self.me = api.me()
        self.start_time = time.time()
        self.limit = time_limit
        
    def on_status(self, tweet):
        print(f"{tweet.user.name} just tweeted\n{tweet.text}")
        
    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            with open("tweets_output.json", 'r') as tf:
                file = json.load(tf)
            json_load = json.loads(data)
            text = json_load['text']
            print(text)
            file.append(text)
            with open("tweets_output.json","w") as f:
                json.dump(file, f, indent=4)
            return True
        else:
            return False
        
    def on_error(self, status):
        print("ERRRRRRRRRRRRRRRORRRROROROR")
          
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["squid game"], languages=["en"])

print("Proccess complete!")    

"""
imagePath = "warbler.jpg"
status = "Hi! From my Python script =)"

# Send the tweet.
api.update_with_media(imagePath, status)    
"""