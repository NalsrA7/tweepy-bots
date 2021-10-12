from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents
from nltk.tokenize import word_tokenize
import json
from collections import Counter

# Load tokenized tweets
#tweets = twitter_samples.strings('positive_tweets.json')
#tweets_tokens = twitter_samples.tokenized('positive_tweets.json')
with open("tweets_output.json", 'r') as f:
    tweets = json.load(f)
    
tweets_tokens = []

for tweet in tweets:
    tweets_tokens.append(word_tokenize(tweet))


# Tag tagged tweets
tweets_tagged = pos_tag_sents(tweets_tokens)

# Set counters
JJ_count = 0
NN_count = 0

# Loop through list of tweets
for tweet in tweets_tagged:
    for pair in tweet:
        tag = pair[1]
        if tag == 'JJ':
            JJ_count += 1
        elif tag == 'NN':
            NN_count += 1
            
# Create a for loop to have all the tokenised tweets into one big string and then count            

joined_tweets_tokens = ""

counted_tweets = Counter()
for x in tweets_tokens:
    for y in x:
        counted_tweets[y.lower()] += 1
        
print(counted_tweets.most_common(10))

# Print total numbers for each adjectives and nouns            
print('Total number of adjectives: ', JJ_count)
print('Total number of nouns: ', NN_count)